"""Writer/reader round-trip tests for UserDefinedGlobalTimeMaster (Table 9.23, p.879)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import UserDefinedGlobalTimeMaster
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
    String,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    return ARXMLWriter()


@pytest.fixture
def parser():
    return ARXMLParser()


def _new_master():
    master = UserDefinedGlobalTimeMaster(None, "userDefinedMaster")
    master.setUuid(String().setValue("5e6f7a8b-9c0d-4bcc-ddee-4a5b6c7d8e9f"))
    ref = RefType()
    ref.setValue("/Clusters/Cluster1/Connector5")
    ref.setDest("COMMUNICATION-CONNECTOR")
    master.setCommunicationConnectorRef(ref)
    master.setSyncPeriod(TimeValue().setValue("0.2"))
    variation_point = VariationPoint()
    variation_point.setShortLabel(String().setValue("vpUdMaster"))
    master.setVariationPoint(variation_point)
    return master


class TestWriteUserDefinedGlobalTimeMaster:
    def test_write_base_group_elements(self, writer):
        """
        The helper writes the Table 9.4 base group ending in its VARIATION-POINT; the XSD
        USER-DEFINED-GLOBAL-TIME-MASTER group (AUTOSAR_00052.xsd l.128818) has an empty
        sequence, so the helper owns only the base level reached through
        writeGlobalTimeMaster.
        """
        element = ET.Element("USER-DEFINED-GLOBAL-TIME-MASTER")
        writer.writeUserDefinedGlobalTimeMaster(element, _new_master())

        tags = [child.tag for child in element]
        assert tags[0] == "SHORT-NAME"
        assert tags[-1] == "VARIATION-POINT"
        assert element.attrib["UUID"] == "5e6f7a8b-9c0d-4bcc-ddee-4a5b6c7d8e9f"
        assert element.find("COMMUNICATION-CONNECTOR-REF").text == "/Clusters/Cluster1/Connector5"
        assert element.find("SYNC-PERIOD").text == "0.2"
        assert element.find("VARIATION-POINT").find("SHORT-LABEL").text == "vpUdMaster"

    def test_write_empty_element(self, writer):
        """
        An unset master emits no group content beyond the SHORT-NAME and no VARIATION-POINT.
        """
        element = ET.Element("USER-DEFINED-GLOBAL-TIME-MASTER")
        writer.writeUserDefinedGlobalTimeMaster(element, UserDefinedGlobalTimeMaster(None, "userDefinedMaster"))

        assert [child.tag for child in element] == ["SHORT-NAME"]
        assert element.find("VARIATION-POINT") is None


class TestUserDefinedGlobalTimeMasterRoundTrip:
    def test_round_trip_preserves_field_values(self, writer, parser):
        """
        Write -> serialize -> parse keeps every inherited base group field value.
        """
        element = ET.Element("USER-DEFINED-GLOBAL-TIME-MASTER")
        writer.writeUserDefinedGlobalTimeMaster(element, _new_master())
        xml = ET.tostring(element, encoding="unicode")

        parsed_element = ET.fromstring("<WRAP xmlns='%s'>%s</WRAP>" % (NS, xml))[0]
        master = parser.readUserDefinedGlobalTimeMaster(parsed_element, UserDefinedGlobalTimeMaster(None, "userDefinedMaster"))

        assert master.getShortName() == "userDefinedMaster"
        assert master.getUuid().getValue() == "5e6f7a8b-9c0d-4bcc-ddee-4a5b6c7d8e9f"
        assert master.getCommunicationConnectorRef().getValue() == "/Clusters/Cluster1/Connector5"
        assert master.getSyncPeriod().getValue() == pytest.approx(0.2)
        assert master.getVariationPoint().getShortLabel().getValue() == "vpUdMaster"
