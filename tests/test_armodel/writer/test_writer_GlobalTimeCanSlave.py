"""Writer/reader round-trip tests for GlobalTimeCanSlave (Table 9.9, p.864)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import GlobalTimeCanSlave
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    GlobalTimeCrcValidationEnum,
    PositiveInteger,
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


def _new_slave():
    slave = GlobalTimeCanSlave(None, "canSlave")
    slave.setUuid(String().setValue("6f7a8b9c-0d1e-4cdd-eeef-5b6c7d8e9f0a"))
    ref = RefType()
    ref.setValue("/Clusters/Cluster1/Connector2")
    ref.setDest("CAN-COMMUNICATION-CONNECTOR")
    slave.setCommunicationConnectorRef(ref)
    slave.setFollowUpTimeoutValue(TimeValue().setValue("0.05"))
    slave.setCrcValidated(GlobalTimeCrcValidationEnum().setValue(GlobalTimeCrcValidationEnum.CRC_VALIDATED))
    slave.setSequenceCounterJumpWidth(PositiveInteger().setValue("2"))
    variation_point = VariationPoint()
    variation_point.setShortLabel(String().setValue("vpCanSlave"))
    slave.setVariationPoint(variation_point)
    return slave


class TestWriteGlobalTimeCanSlave:
    def test_write_all_elements_in_xsd_order(self, writer):
        """
        The helper writes the Table 9.5 base group first (via writeGlobalTimeSlave, ending in
        its VARIATION-POINT) and then the two own group elements in the XSD sequenceOffset order.
        """
        element = ET.Element("GLOBAL-TIME-CAN-SLAVE")
        writer.writeGlobalTimeCanSlave(element, _new_slave())

        tags = [child.tag for child in element]
        assert tags[0] == "SHORT-NAME"
        assert tags[-3:] == [
            "VARIATION-POINT",
            "CRC-VALIDATED",
            "SEQUENCE-COUNTER-JUMP-WIDTH",
        ]
        assert element.attrib["UUID"] == "6f7a8b9c-0d1e-4cdd-eeef-5b6c7d8e9f0a"
        assert element.find("COMMUNICATION-CONNECTOR-REF").text == "/Clusters/Cluster1/Connector2"
        assert element.find("FOLLOW-UP-TIMEOUT-VALUE").text == "0.05"
        assert element.find("CRC-VALIDATED").text == "CRC-VALIDATED"
        assert element.find("SEQUENCE-COUNTER-JUMP-WIDTH").text == "2"
        assert element.find("VARIATION-POINT").find("SHORT-LABEL").text == "vpCanSlave"

    def test_write_empty_element(self, writer):
        """
        An unset slave emits no group content beyond the SHORT-NAME and no VARIATION-POINT.
        """
        element = ET.Element("GLOBAL-TIME-CAN-SLAVE")
        writer.writeGlobalTimeCanSlave(element, GlobalTimeCanSlave(None, "canSlave"))

        assert [child.tag for child in element] == ["SHORT-NAME"]
        assert element.find("CRC-VALIDATED") is None
        assert element.find("VARIATION-POINT") is None


class TestGlobalTimeCanSlaveRoundTrip:
    def test_round_trip_preserves_field_values(self, writer, parser):
        """
        Write -> serialize -> parse keeps every field value including the inherited base group.
        """
        element = ET.Element("GLOBAL-TIME-CAN-SLAVE")
        writer.writeGlobalTimeCanSlave(element, _new_slave())
        xml = ET.tostring(element, encoding="unicode")

        parsed_element = ET.fromstring("<WRAP xmlns='%s'>%s</WRAP>" % (NS, xml))[0]
        slave = parser.readGlobalTimeCanSlave(parsed_element, GlobalTimeCanSlave(None, "canSlave"))

        assert slave.getShortName() == "canSlave"
        assert slave.getUuid().getValue() == "6f7a8b9c-0d1e-4cdd-eeef-5b6c7d8e9f0a"
        assert slave.getCommunicationConnectorRef().getValue() == "/Clusters/Cluster1/Connector2"
        assert slave.getFollowUpTimeoutValue().getValue() == pytest.approx(0.05)
        assert slave.getCrcValidated().getValue() == "CRC-VALIDATED"
        assert slave.getSequenceCounterJumpWidth().getValue() == 2
        assert slave.getVariationPoint().getShortLabel().getValue() == "vpCanSlave"
