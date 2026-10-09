"""Reader tests for GlobalTimeEthMaster (Table 9.11, p.866)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import GlobalTimeEthMaster
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    from armodel.models import AUTOSAR

    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    return ARXMLParser()


class TestReadGlobalTimeEthMaster:
    def test_read_all_elements(self, parser):
        """
        The three GLOBAL-TIME-ETH-MASTER group elements plus the Table 9.4 base group
        (via readGlobalTimeMaster: COMMUNICATION-CONNECTOR-REF ... SYNC-PERIOD, SHORT-NAME,
        UUID, VARIATION-POINT) are read into the object.
        """
        element = ET.fromstring(
            "<GLOBAL-TIME-ETH-MASTER xmlns='%s' UUID='5e6f7a8b-9c0d-4bcc-ddee-4a5b6c7d8e9f'>"
            "<SHORT-NAME>ethMaster</SHORT-NAME>"
            "<COMMUNICATION-CONNECTOR-REF DEST='ETHERNET-COMMUNICATION-CONNECTOR'>/Clusters/Cluster1/Connector1</COMMUNICATION-CONNECTOR-REF>"
            "<SYNC-PERIOD>0.2</SYNC-PERIOD>"
            "<CRC-SECURED>CRC-SUPPORTED</CRC-SECURED>"
            "<HOLD-OVER-TIME>2.0</HOLD-OVER-TIME>"
            "<SUB-TLV-CONFIG>"
            "<OFS-SUB-TLV>true</OFS-SUB-TLV>"
            "<TIME-SUB-TLV>false</TIME-SUB-TLV>"
            "</SUB-TLV-CONFIG>"
            "<VARIATION-POINT><SHORT-LABEL>vpEthMaster</SHORT-LABEL></VARIATION-POINT>"
            "</GLOBAL-TIME-ETH-MASTER>" % NS
        )

        master = parser.readGlobalTimeEthMaster(element, GlobalTimeEthMaster(None, "ethMaster"))

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

    def test_read_empty_element(self, parser):
        """
        A GLOBAL-TIME-ETH-MASTER element without group content leaves the fields unset.
        """
        element = ET.fromstring("<GLOBAL-TIME-ETH-MASTER xmlns='%s'></GLOBAL-TIME-ETH-MASTER>" % NS)

        master = parser.readGlobalTimeEthMaster(element, GlobalTimeEthMaster(None, "ethMaster"))

        assert master.getCrcSecured() is None
        assert master.getHoldOverTime() is None
        assert master.getSubTlvConfig() is None
        assert master.getCommunicationConnectorRef() is None
        assert master.getVariationPoint() is None
