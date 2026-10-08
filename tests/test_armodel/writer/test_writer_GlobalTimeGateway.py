"""Writer/reader round-trip tests for GlobalTimeGateway (Table 9.6, p.861)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import GlobalTimeGateway
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, String
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


def _new_gateway():
    gateway = GlobalTimeGateway(None, "gateway1")
    gateway.setUuid(String().setValue("4d5e6f7a-8b9c-4abb-ccdd-3f4a5b6c7d8e"))
    host = RefType()
    host.setValue("/ECUs/EcuInstance1")
    host.setDest("ECU-INSTANCE")
    gateway.setHostRef(host)
    master = RefType()
    master.setValue("/TimeDomains/Domain1/Master")
    master.setDest("GLOBAL-TIME-CAN-MASTER")
    gateway.setMasterRef(master)
    slave = RefType()
    slave.setValue("/TimeDomains/Domain1/Slave")
    slave.setDest("GLOBAL-TIME-CAN-SLAVE")
    gateway.setSlaveRef(slave)
    variation_point = VariationPoint()
    variation_point.setShortLabel(String().setValue("vpGateway"))
    gateway.setVariationPoint(variation_point)
    return gateway


class TestWriteGlobalTimeGateway:
    def test_write_all_elements_in_xsd_order(self, writer):
        """
        The helper writes the Identifiable level, the three group elements in the XSD
        sequenceOffset order and the VARIATION-POINT tail last.
        """
        element = ET.Element("GLOBAL-TIME-GATEWAY")
        writer.writeGlobalTimeGateway(element, _new_gateway())

        tags = [child.tag for child in element]
        assert tags[0] == "SHORT-NAME"
        assert tags[-1] == "VARIATION-POINT"
        assert tags[-4:] == [
            "HOST-REF",
            "MASTER-REF",
            "SLAVE-REF",
            "VARIATION-POINT",
        ]
        assert element.attrib["UUID"] == "4d5e6f7a-8b9c-4abb-ccdd-3f4a5b6c7d8e"
        assert element.find("HOST-REF").text == "/ECUs/EcuInstance1"
        assert element.find("HOST-REF").attrib["DEST"] == "ECU-INSTANCE"
        assert element.find("MASTER-REF").text == "/TimeDomains/Domain1/Master"
        assert element.find("MASTER-REF").attrib["DEST"] == "GLOBAL-TIME-CAN-MASTER"
        assert element.find("SLAVE-REF").text == "/TimeDomains/Domain1/Slave"
        assert element.find("SLAVE-REF").attrib["DEST"] == "GLOBAL-TIME-CAN-SLAVE"
        assert element.find("VARIATION-POINT").find("SHORT-LABEL").text == "vpGateway"

    def test_write_empty_element(self, writer):
        """
        An unset gateway emits no group content beyond the SHORT-NAME and no VARIATION-POINT.
        """
        element = ET.Element("GLOBAL-TIME-GATEWAY")
        writer.writeGlobalTimeGateway(element, GlobalTimeGateway(None, "gateway2"))

        assert [child.tag for child in element] == ["SHORT-NAME"]
        assert element.find("VARIATION-POINT") is None


class TestGlobalTimeGatewayRoundTrip:
    def test_round_trip_preserves_field_values(self, writer, parser):
        """
        Write -> serialize -> parse keeps every field value including the variation point.
        """
        element = ET.Element("GLOBAL-TIME-GATEWAY")
        writer.writeGlobalTimeGateway(element, _new_gateway())
        xml = ET.tostring(element, encoding="unicode")

        parsed_element = ET.fromstring("<WRAP xmlns='%s'>%s</WRAP>" % (NS, xml))[0]
        gateway = parser.readGlobalTimeGateway(parsed_element, GlobalTimeGateway(None, "gateway1"))

        assert gateway.getShortName() == "gateway1"
        assert gateway.getUuid().getValue() == "4d5e6f7a-8b9c-4abb-ccdd-3f4a5b6c7d8e"
        assert gateway.getHostRef().getValue() == "/ECUs/EcuInstance1"
        assert gateway.getHostRef().getDest() == "ECU-INSTANCE"
        assert gateway.getMasterRef().getValue() == "/TimeDomains/Domain1/Master"
        assert gateway.getMasterRef().getDest() == "GLOBAL-TIME-CAN-MASTER"
        assert gateway.getSlaveRef().getValue() == "/TimeDomains/Domain1/Slave"
        assert gateway.getSlaveRef().getDest() == "GLOBAL-TIME-CAN-SLAVE"
        assert gateway.getVariationPoint().getShortLabel().getValue() == "vpGateway"
