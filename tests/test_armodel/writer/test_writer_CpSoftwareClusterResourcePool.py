"""Writer/reader round-trip tests for CpSoftwareClusterResourcePool (Table 11.5, p.901)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import CpSoftwareClusterResourcePool
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    CpSoftwareClusterCommunicationResource,
    CpSoftwareClusterServiceResource,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    RefType,
    String,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    autosar = AUTOSAR.getInstance()
    autosar.new()
    autosar.setARRelease("R23-11")
    yield
    autosar.new()


@pytest.fixture
def writer():
    return ARXMLWriter()


@pytest.fixture
def parser():
    return ARXMLParser()


def _new_pool():
    pool = CpSoftwareClusterResourcePool(None, "pool1")
    pool.setUuid(String().setValue("1a2b3c4d-5e6f-4aaa-bbbc-2e3f4a5b6c7d"))
    pool.addEcuScopeRef(RefType().setValue("/Ecu/Ecu1").setDest("ECU-INSTANCE"))
    pool.addEcuScopeRef(RefType().setValue("/Ecu/Ecu2").setDest("ECU-INSTANCE"))
    comm = pool.createCpSoftwareClusterCommunicationResource("comm1")
    comm.setGlobalResourceId(PositiveInteger().setValue(5))
    comm.setIsMandatory(Boolean().setValue(True))
    pool.createCpSoftwareClusterServiceResource("service1")
    return pool


class TestWriteCpSoftwareClusterResourcePool:
    def test_write_all_elements_in_xsd_order(self, writer):
        """
        The helper writes the SHORT-NAME first, then the two Table 11.5 members in the
        XSD group element order (ECU-SCOPE-REFS then RESOURCES); the aggregation wrappers
        are emitted only when non-empty.
        """
        parent = ET.Element("AR-PACKAGE")
        writer.writeCpSoftwareClusterResourcePool(parent, _new_pool())

        element = parent[0]
        assert element.tag == "CP-SOFTWARE-CLUSTER-RESOURCE-POOL"
        assert element.attrib["UUID"] == "1a2b3c4d-5e6f-4aaa-bbbc-2e3f4a5b6c7d"
        assert [child.tag for child in element][0] == "SHORT-NAME"
        assert element.find("SHORT-NAME").text == "pool1"

        ecu_scope_refs = element.find("ECU-SCOPE-REFS")
        assert [child.tag for child in ecu_scope_refs] == ["ECU-SCOPE-REF", "ECU-SCOPE-REF"]
        assert ecu_scope_refs[0].text == "/Ecu/Ecu1"
        assert ecu_scope_refs[0].attrib["DEST"] == "ECU-INSTANCE"
        assert ecu_scope_refs[1].text == "/Ecu/Ecu2"

        resources = element.find("RESOURCES")
        assert [child.tag for child in resources] == ["CP-SOFTWARE-CLUSTER-COMMUNICATION-RESOURCE", "CP-SOFTWARE-CLUSTER-SERVICE-RESOURCE"]
        assert resources[0].find("SHORT-NAME").text == "comm1"
        assert resources[0].find("GLOBAL-RESOURCE-ID").text == "5"
        assert resources[0].find("IS-MANDATORY").text == "true"
        assert resources[1].find("SHORT-NAME").text == "service1"

        tags = [child.tag for child in element]
        assert tags.index("SHORT-NAME") < tags.index("ECU-SCOPE-REFS") < tags.index("RESOURCES")

    def test_write_empty_element(self, writer):
        """
        A pool without members emits no aggregation wrappers.
        """
        parent = ET.Element("AR-PACKAGE")
        writer.writeCpSoftwareClusterResourcePool(parent, CpSoftwareClusterResourcePool(None, "pool2"))

        element = parent[0]
        assert element.find("ECU-SCOPE-REFS") is None
        assert element.find("RESOURCES") is None


class TestCpSoftwareClusterResourcePoolRoundTrip:
    def test_round_trip_preserves_field_values(self, writer, parser):
        """
        Write -> serialize -> parse keeps every field value including the concrete
        subtype elements inside the RESOURCES wrapper.
        """
        parent = ET.Element("AR-PACKAGE")
        writer.writeCpSoftwareClusterResourcePool(parent, _new_pool())
        xml = ET.tostring(parent[0], encoding="unicode")

        parsed_element = ET.fromstring("<WRAP xmlns='%s'>%s</WRAP>" % (NS, xml))[0]
        pool = parser.readCpSoftwareClusterResourcePool(parsed_element, CpSoftwareClusterResourcePool(None, "pool1"))

        assert pool.getShortName() == "pool1"
        assert pool.getUuid().getValue() == "1a2b3c4d-5e6f-4aaa-bbbc-2e3f4a5b6c7d"

        refs = pool.getEcuScopeRefs()
        assert [ref.getValue() for ref in refs] == ["/Ecu/Ecu1", "/Ecu/Ecu2"]
        assert refs[0].getDest() == "ECU-INSTANCE"

        resources = pool.getResources()
        assert len(resources) == 2
        assert isinstance(resources[0], CpSoftwareClusterCommunicationResource)
        assert resources[0].getShortName() == "comm1"
        assert resources[0].getGlobalResourceId().getValue() == 5
        assert resources[0].getIsMandatory().getValue() is True
        assert isinstance(resources[1], CpSoftwareClusterServiceResource)
        assert resources[1].getShortName() == "service1"
