"""Writer/reader round-trip tests for GlobalTimeCanMaster (Table 9.8, p.864)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import GlobalTimeCanMaster
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    GlobalTimeCrcSupportEnum,
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
    master = GlobalTimeCanMaster(None, "canMaster")
    master.setUuid(String().setValue("5e6f7a8b-9c0d-4bcc-ddee-4a5b6c7d8e9f"))
    ref = RefType()
    ref.setValue("/Clusters/Cluster1/Connector1")
    ref.setDest("CAN-COMMUNICATION-CONNECTOR")
    master.setCommunicationConnectorRef(ref)
    master.setSyncPeriod(TimeValue().setValue("0.2"))
    master.setCrcSecured(GlobalTimeCrcSupportEnum().setValue(GlobalTimeCrcSupportEnum.CRC_SUPPORTED))
    master.setSyncConfirmationTimeout(TimeValue().setValue("1.0"))
    variation_point = VariationPoint()
    variation_point.setShortLabel(String().setValue("vpCanMaster"))
    master.setVariationPoint(variation_point)
    return master


class TestWriteGlobalTimeCanMaster:
    def test_write_all_elements_in_xsd_order(self, writer):
        """
        The helper writes the Table 9.4 base group first (via writeGlobalTimeMaster, ending in
        its VARIATION-POINT) and then the two own group elements in the XSD sequenceOffset order.
        """
        element = ET.Element("GLOBAL-TIME-CAN-MASTER")
        writer.writeGlobalTimeCanMaster(element, _new_master())

        tags = [child.tag for child in element]
        assert tags[0] == "SHORT-NAME"
        assert tags[-3:] == [
            "VARIATION-POINT",
            "CRC-SECURED",
            "SYNC-CONFIRMATION-TIMEOUT",
        ]
        assert element.attrib["UUID"] == "5e6f7a8b-9c0d-4bcc-ddee-4a5b6c7d8e9f"
        assert element.find("COMMUNICATION-CONNECTOR-REF").text == "/Clusters/Cluster1/Connector1"
        assert element.find("SYNC-PERIOD").text == "0.2"
        assert element.find("CRC-SECURED").text == "CRC-SUPPORTED"
        assert element.find("SYNC-CONFIRMATION-TIMEOUT").text == "1.0"
        assert element.find("VARIATION-POINT").find("SHORT-LABEL").text == "vpCanMaster"

    def test_write_empty_element(self, writer):
        """
        An unset master emits no group content beyond the SHORT-NAME and no VARIATION-POINT.
        """
        element = ET.Element("GLOBAL-TIME-CAN-MASTER")
        writer.writeGlobalTimeCanMaster(element, GlobalTimeCanMaster(None, "canMaster"))

        assert [child.tag for child in element] == ["SHORT-NAME"]
        assert element.find("CRC-SECURED") is None
        assert element.find("VARIATION-POINT") is None


class TestGlobalTimeCanMasterRoundTrip:
    def test_round_trip_preserves_field_values(self, writer, parser):
        """
        Write -> serialize -> parse keeps every field value including the inherited base group.
        """
        element = ET.Element("GLOBAL-TIME-CAN-MASTER")
        writer.writeGlobalTimeCanMaster(element, _new_master())
        xml = ET.tostring(element, encoding="unicode")

        parsed_element = ET.fromstring("<WRAP xmlns='%s'>%s</WRAP>" % (NS, xml))[0]
        master = parser.readGlobalTimeCanMaster(parsed_element, GlobalTimeCanMaster(None, "canMaster"))

        assert master.getShortName() == "canMaster"
        assert master.getUuid().getValue() == "5e6f7a8b-9c0d-4bcc-ddee-4a5b6c7d8e9f"
        assert master.getCommunicationConnectorRef().getValue() == "/Clusters/Cluster1/Connector1"
        assert master.getSyncPeriod().getValue() == pytest.approx(0.2)
        assert master.getCrcSecured().getValue() == "CRC-SUPPORTED"
        assert master.getSyncConfirmationTimeout().getValue() == pytest.approx(1.0)
        assert master.getVariationPoint().getShortLabel().getValue() == "vpCanMaster"
