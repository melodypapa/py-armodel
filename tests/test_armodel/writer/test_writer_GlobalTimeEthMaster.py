"""Writer/reader round-trip tests for GlobalTimeEthMaster (Table 9.11, p.866)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import EthTSynSubTlvConfig
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import GlobalTimeEthMaster
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
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
    master = GlobalTimeEthMaster(None, "ethMaster")
    master.setUuid(String().setValue("5e6f7a8b-9c0d-4bcc-ddee-4a5b6c7d8e9f"))
    ref = RefType()
    ref.setValue("/Clusters/Cluster1/Connector1")
    ref.setDest("ETHERNET-COMMUNICATION-CONNECTOR")
    master.setCommunicationConnectorRef(ref)
    master.setSyncPeriod(TimeValue().setValue("0.2"))
    master.setCrcSecured(GlobalTimeCrcSupportEnum().setValue(GlobalTimeCrcSupportEnum.CRC_SUPPORTED))
    master.setHoldOverTime(TimeValue().setValue("2.0"))
    sub_tlv_config = EthTSynSubTlvConfig()
    sub_tlv_config.setOfsSubTlv(Boolean().setValue(True))
    sub_tlv_config.setTimeSubTlv(Boolean().setValue(False))
    master.setSubTlvConfig(sub_tlv_config)
    variation_point = VariationPoint()
    variation_point.setShortLabel(String().setValue("vpEthMaster"))
    master.setVariationPoint(variation_point)
    return master


class TestWriteGlobalTimeEthMaster:
    def test_write_all_elements_in_xsd_order(self, writer):
        """
        The helper writes the Table 9.4 base group first (via writeGlobalTimeMaster, ending in
        its VARIATION-POINT) and then the three own group elements in the XSD sequenceOffset
        order (CRC-SECURED, HOLD-OVER-TIME, SUB-TLV-CONFIG; AUTOSAR_00052.xsd l.64689).
        """
        element = ET.Element("GLOBAL-TIME-ETH-MASTER")
        writer.writeGlobalTimeEthMaster(element, _new_master())

        tags = [child.tag for child in element]
        assert tags[0] == "SHORT-NAME"
        assert tags[-4:] == [
            "VARIATION-POINT",
            "CRC-SECURED",
            "HOLD-OVER-TIME",
            "SUB-TLV-CONFIG",
        ]
        assert element.attrib["UUID"] == "5e6f7a8b-9c0d-4bcc-ddee-4a5b6c7d8e9f"
        assert element.find("COMMUNICATION-CONNECTOR-REF").text == "/Clusters/Cluster1/Connector1"
        assert element.find("SYNC-PERIOD").text == "0.2"
        assert element.find("CRC-SECURED").text == "CRC-SUPPORTED"
        assert element.find("HOLD-OVER-TIME").text == "2.0"
        assert element.find("SUB-TLV-CONFIG").find("OFS-SUB-TLV").text == "true"
        assert element.find("SUB-TLV-CONFIG").find("TIME-SUB-TLV").text == "false"
        assert element.find("VARIATION-POINT").find("SHORT-LABEL").text == "vpEthMaster"

    def test_write_empty_element(self, writer):
        """
        An unset master emits no group content beyond the SHORT-NAME and no VARIATION-POINT.
        """
        element = ET.Element("GLOBAL-TIME-ETH-MASTER")
        writer.writeGlobalTimeEthMaster(element, GlobalTimeEthMaster(None, "ethMaster"))

        assert [child.tag for child in element] == ["SHORT-NAME"]
        assert element.find("CRC-SECURED") is None
        assert element.find("HOLD-OVER-TIME") is None
        assert element.find("SUB-TLV-CONFIG") is None
        assert element.find("VARIATION-POINT") is None


class TestGlobalTimeEthMasterRoundTrip:
    def test_round_trip_preserves_field_values(self, writer, parser):
        """
        Write -> serialize -> parse keeps every field value including the inherited base group
        and the aggregated EthTSynSubTlvConfig.
        """
        element = ET.Element("GLOBAL-TIME-ETH-MASTER")
        writer.writeGlobalTimeEthMaster(element, _new_master())
        xml = ET.tostring(element, encoding="unicode")

        parsed_element = ET.fromstring("<WRAP xmlns='%s'>%s</WRAP>" % (NS, xml))[0]
        master = parser.readGlobalTimeEthMaster(parsed_element, GlobalTimeEthMaster(None, "ethMaster"))

        assert master.getShortName() == "ethMaster"
        assert master.getUuid().getValue() == "5e6f7a8b-9c0d-4bcc-ddee-4a5b6c7d8e9f"
        assert master.getCommunicationConnectorRef().getValue() == "/Clusters/Cluster1/Connector1"
        assert master.getSyncPeriod().getValue() == pytest.approx(0.2)
        assert master.getCrcSecured().getValue() == "CRC-SUPPORTED"
        assert master.getHoldOverTime().getValue() == pytest.approx(2.0)
        assert master.getSubTlvConfig().getOfsSubTlv().getValue() is True
        assert master.getSubTlvConfig().getTimeSubTlv().getValue() is False
        assert master.getSubTlvConfig().getStatusSubTlv() is None
        assert master.getVariationPoint().getShortLabel().getValue() == "vpEthMaster"

    def test_round_trip_empty_sub_tlv_config_list_case(self, writer, parser):
        """
        An empty wrapper case: unset optional group elements serialize to nothing and re-parse
        to None fields (no empty SUB-TLV-CONFIG element is emitted).
        """
        element = ET.Element("GLOBAL-TIME-ETH-MASTER")
        writer.writeGlobalTimeEthMaster(element, GlobalTimeEthMaster(None, "ethMaster"))
        xml = ET.tostring(element, encoding="unicode")

        assert "SUB-TLV-CONFIG" not in xml
        assert "CRC-SECURED" not in xml

        parsed_element = ET.fromstring("<WRAP xmlns='%s'>%s</WRAP>" % (NS, xml))[0]
        master = parser.readGlobalTimeEthMaster(parsed_element, GlobalTimeEthMaster(None, "ethMaster"))

        assert master.getCrcSecured() is None
        assert master.getHoldOverTime() is None
        assert master.getSubTlvConfig() is None
