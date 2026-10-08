"""Writer/reader round-trip tests for EthTSynCrcFlags (Table 9.15, p.868)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import EthTSynCrcFlags
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean
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


def _new_flags():
    flags = EthTSynCrcFlags()
    flags.setCrcCorrectionField(Boolean().setValue(True))
    flags.setCrcDomainNumber(Boolean().setValue(True))
    flags.setCrcMessageLength(Boolean().setValue(False))
    flags.setCrcPreciseOriginTimestamp(Boolean().setValue(True))
    flags.setCrcSequenceId(Boolean().setValue(True))
    flags.setCrcSourcePortIdentity(Boolean().setValue(True))
    return flags


class TestWriteEthTSynCrcFlags:
    def test_write_all_elements_in_xsd_order(self, writer):
        """
        The helper emits the ETH-T-SYN-CRC-FLAGS element with its six attributes in the XSD
        sequenceOffset order.
        """
        parent = ET.Element("ETH-GLOBAL-TIME-DOMAIN-PROPS")
        writer.writeEthTSynCrcFlags(parent, _new_flags())

        element = parent.find("ETH-T-SYN-CRC-FLAGS")
        assert element is not None
        assert [child.tag for child in element] == [
            "CRC-CORRECTION-FIELD",
            "CRC-DOMAIN-NUMBER",
            "CRC-MESSAGE-LENGTH",
            "CRC-PRECISE-ORIGIN-TIMESTAMP",
            "CRC-SEQUENCE-ID",
            "CRC-SOURCE-PORT-IDENTITY",
        ]
        assert element.find("CRC-CORRECTION-FIELD").text == "true"
        assert element.find("CRC-DOMAIN-NUMBER").text == "true"
        assert element.find("CRC-MESSAGE-LENGTH").text == "false"
        assert element.find("CRC-PRECISE-ORIGIN-TIMESTAMP").text == "true"
        assert element.find("CRC-SEQUENCE-ID").text == "true"
        assert element.find("CRC-SOURCE-PORT-IDENTITY").text == "true"

    def test_write_empty_element(self, writer):
        """
        An unset flags object emits the element without attribute content.
        """
        parent = ET.Element("ETH-GLOBAL-TIME-DOMAIN-PROPS")
        writer.writeEthTSynCrcFlags(parent, EthTSynCrcFlags())

        element = parent.find("ETH-T-SYN-CRC-FLAGS")
        assert element is not None
        assert len(element) == 0


class TestEthTSynCrcFlagsRoundTrip:
    def test_round_trip_preserves_field_values(self, writer, parser):
        """
        Write -> serialize -> parse keeps every field value.
        """
        parent = ET.Element("ETH-GLOBAL-TIME-DOMAIN-PROPS")
        writer.writeEthTSynCrcFlags(parent, _new_flags())
        xml = ET.tostring(parent, encoding="unicode")

        parsed_parent = ET.fromstring("<WRAP xmlns='%s'>%s</WRAP>" % (NS, xml))
        element = parsed_parent[0][0]
        flags = EthTSynCrcFlags()
        parser.readEthTSynCrcFlags(element, flags)

        assert flags.getCrcCorrectionField().getValue() is True
        assert flags.getCrcDomainNumber().getValue() is True
        assert flags.getCrcMessageLength().getValue() is False
        assert flags.getCrcPreciseOriginTimestamp().getValue() is True
        assert flags.getCrcSequenceId().getValue() is True
        assert flags.getCrcSourcePortIdentity().getValue() is True
