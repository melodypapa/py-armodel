"""Reader tests for EthTSynCrcFlags (Table 9.15, p.868)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import EthTSynCrcFlags
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


class TestReadEthTSynCrcFlags:
    def test_read_all_elements(self, parser):
        """
        All six Table 9.15 attributes are read from the ETH-T-SYN-CRC-FLAGS element.
        """
        element = ET.fromstring(
            "<ETH-T-SYN-CRC-FLAGS xmlns='%s'>"
            "<CRC-CORRECTION-FIELD>true</CRC-CORRECTION-FIELD>"
            "<CRC-DOMAIN-NUMBER>true</CRC-DOMAIN-NUMBER>"
            "<CRC-MESSAGE-LENGTH>false</CRC-MESSAGE-LENGTH>"
            "<CRC-PRECISE-ORIGIN-TIMESTAMP>true</CRC-PRECISE-ORIGIN-TIMESTAMP>"
            "<CRC-SEQUENCE-ID>true</CRC-SEQUENCE-ID>"
            "<CRC-SOURCE-PORT-IDENTITY>true</CRC-SOURCE-PORT-IDENTITY>"
            "</ETH-T-SYN-CRC-FLAGS>" % NS
        )

        flags = EthTSynCrcFlags()
        parser.readEthTSynCrcFlags(element, flags)

        assert flags.getCrcCorrectionField().getValue() is True
        assert flags.getCrcDomainNumber().getValue() is True
        assert flags.getCrcMessageLength().getValue() is False
        assert flags.getCrcPreciseOriginTimestamp().getValue() is True
        assert flags.getCrcSequenceId().getValue() is True
        assert flags.getCrcSourcePortIdentity().getValue() is True

    def test_read_empty_element(self, parser):
        """
        An element without attribute content leaves the fields unset.
        """
        element = ET.fromstring("<ETH-T-SYN-CRC-FLAGS xmlns='%s'></ETH-T-SYN-CRC-FLAGS>" % NS)

        flags = EthTSynCrcFlags()
        parser.readEthTSynCrcFlags(element, flags)

        assert flags.getCrcCorrectionField() is None
        assert flags.getCrcDomainNumber() is None
        assert flags.getCrcMessageLength() is None
        assert flags.getCrcPreciseOriginTimestamp() is None
        assert flags.getCrcSequenceId() is None
        assert flags.getCrcSourcePortIdentity() is None
