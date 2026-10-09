"""Writer/reader round-trip tests for GlobalTimeEthSlave (Table 9.13, p.867)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import GlobalTimeEthSlave
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    GlobalTimeCrcValidationEnum,
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
    slave = GlobalTimeEthSlave(None, "ethSlave")
    slave.setUuid(String().setValue("5e6f7a8b-9c0d-4bcc-ddee-4a5b6c7d8e9f"))
    ref = RefType()
    ref.setValue("/Clusters/Cluster1/Connector2")
    ref.setDest("ETHERNET-COMMUNICATION-CONNECTOR")
    slave.setCommunicationConnectorRef(ref)
    slave.setFollowUpTimeoutValue(TimeValue().setValue("0.05"))
    slave.setCrcValidated(GlobalTimeCrcValidationEnum().setValue(GlobalTimeCrcValidationEnum.CRC_VALIDATED))
    variation_point = VariationPoint()
    variation_point.setShortLabel(String().setValue("vpEthSlave"))
    slave.setVariationPoint(variation_point)
    return slave


class TestWriteGlobalTimeEthSlave:
    def test_write_all_elements_in_xsd_order(self, writer):
        """
        The helper writes the Table 9.5 base group first (via writeGlobalTimeSlave, ending in
        its VARIATION-POINT) and then the own group element CRC-VALIDATED (XSD
        GLOBAL-TIME-ETH-SLAVE, AUTOSAR_00052.xsd l.64735).
        """
        element = ET.Element("GLOBAL-TIME-ETH-SLAVE")
        writer.writeGlobalTimeEthSlave(element, _new_slave())

        tags = [child.tag for child in element]
        assert tags[0] == "SHORT-NAME"
        assert tags[-2:] == [
            "VARIATION-POINT",
            "CRC-VALIDATED",
        ]
        assert element.attrib["UUID"] == "5e6f7a8b-9c0d-4bcc-ddee-4a5b6c7d8e9f"
        assert element.find("COMMUNICATION-CONNECTOR-REF").text == "/Clusters/Cluster1/Connector2"
        assert element.find("FOLLOW-UP-TIMEOUT-VALUE").text == "0.05"
        assert element.find("CRC-VALIDATED").text == "CRC-VALIDATED"
        assert element.find("VARIATION-POINT").find("SHORT-LABEL").text == "vpEthSlave"

    def test_write_empty_element(self, writer):
        """
        An unset slave emits no group content beyond the SHORT-NAME and no VARIATION-POINT.
        """
        element = ET.Element("GLOBAL-TIME-ETH-SLAVE")
        writer.writeGlobalTimeEthSlave(element, GlobalTimeEthSlave(None, "ethSlave"))

        assert [child.tag for child in element] == ["SHORT-NAME"]
        assert element.find("CRC-VALIDATED") is None
        assert element.find("VARIATION-POINT") is None


class TestGlobalTimeEthSlaveRoundTrip:
    def test_round_trip_preserves_field_values(self, writer, parser):
        """
        Write -> serialize -> parse keeps every field value including the inherited base group.
        """
        element = ET.Element("GLOBAL-TIME-ETH-SLAVE")
        writer.writeGlobalTimeEthSlave(element, _new_slave())
        xml = ET.tostring(element, encoding="unicode")

        parsed_element = ET.fromstring("<WRAP xmlns='%s'>%s</WRAP>" % (NS, xml))[0]
        slave = parser.readGlobalTimeEthSlave(parsed_element, GlobalTimeEthSlave(None, "ethSlave"))

        assert slave.getShortName() == "ethSlave"
        assert slave.getUuid().getValue() == "5e6f7a8b-9c0d-4bcc-ddee-4a5b6c7d8e9f"
        assert slave.getCommunicationConnectorRef().getValue() == "/Clusters/Cluster1/Connector2"
        assert slave.getFollowUpTimeoutValue().getValue() == pytest.approx(0.05)
        assert slave.getCrcValidated().getValue() == "CRC-VALIDATED"
        assert slave.getVariationPoint().getShortLabel().getValue() == "vpEthSlave"
