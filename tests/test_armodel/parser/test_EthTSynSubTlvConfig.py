"""Reader tests for EthTSynSubTlvConfig (Table 9.12, p.867)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import EthTSynSubTlvConfig
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


class TestReadEthTSynSubTlvConfig:
    def test_read_all_elements(self, parser):
        """
        All four Table 9.12 attributes are read from the ETH-T-SYN-SUB-TLV-CONFIG element.
        """
        element = ET.fromstring(
            "<ETH-T-SYN-SUB-TLV-CONFIG xmlns='%s'>"
            "<OFS-SUB-TLV>true</OFS-SUB-TLV>"
            "<STATUS-SUB-TLV>false</STATUS-SUB-TLV>"
            "<TIME-SUB-TLV>true</TIME-SUB-TLV>"
            "<USER-DATA-SUB-TLV>true</USER-DATA-SUB-TLV>"
            "</ETH-T-SYN-SUB-TLV-CONFIG>" % NS
        )

        config = EthTSynSubTlvConfig()
        parser.readEthTSynSubTlvConfig(element, config)

        assert config.getOfsSubTlv().getValue() is True
        assert config.getStatusSubTlv().getValue() is False
        assert config.getTimeSubTlv().getValue() is True
        assert config.getUserDataSubTlv().getValue() is True

    def test_read_empty_element(self, parser):
        """
        An element without attribute content leaves the fields unset.
        """
        element = ET.fromstring("<ETH-T-SYN-SUB-TLV-CONFIG xmlns='%s'></ETH-T-SYN-SUB-TLV-CONFIG>" % NS)

        config = EthTSynSubTlvConfig()
        parser.readEthTSynSubTlvConfig(element, config)

        assert config.getOfsSubTlv() is None
        assert config.getStatusSubTlv() is None
        assert config.getTimeSubTlv() is None
        assert config.getUserDataSubTlv() is None
