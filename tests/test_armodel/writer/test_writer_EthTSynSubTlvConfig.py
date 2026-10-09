"""Writer/reader round-trip tests for EthTSynSubTlvConfig (Table 9.12, p.867)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import EthTSynSubTlvConfig
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


def _new_config():
    config = EthTSynSubTlvConfig()
    config.setOfsSubTlv(Boolean().setValue(True))
    config.setStatusSubTlv(Boolean().setValue(False))
    config.setTimeSubTlv(Boolean().setValue(True))
    config.setUserDataSubTlv(Boolean().setValue(True))
    return config


class TestWriteEthTSynSubTlvConfig:
    def test_write_all_elements_in_xsd_order(self, writer):
        """
        The helper emits the ETH-T-SYN-SUB-TLV-CONFIG element with its four attributes in the
        XSD sequenceOffset order.
        """
        parent = ET.Element("GLOBAL-TIME-ETH-MASTER")
        writer.writeEthTSynSubTlvConfig(parent, _new_config())

        element = parent.find("ETH-T-SYN-SUB-TLV-CONFIG")
        assert element is not None
        assert [child.tag for child in element] == [
            "OFS-SUB-TLV",
            "STATUS-SUB-TLV",
            "TIME-SUB-TLV",
            "USER-DATA-SUB-TLV",
        ]
        assert element.find("OFS-SUB-TLV").text == "true"
        assert element.find("STATUS-SUB-TLV").text == "false"
        assert element.find("TIME-SUB-TLV").text == "true"
        assert element.find("USER-DATA-SUB-TLV").text == "true"

    def test_write_empty_element(self, writer):
        """
        An unset config emits the element without attribute content.
        """
        parent = ET.Element("GLOBAL-TIME-ETH-MASTER")
        writer.writeEthTSynSubTlvConfig(parent, EthTSynSubTlvConfig())

        element = parent.find("ETH-T-SYN-SUB-TLV-CONFIG")
        assert element is not None
        assert len(element) == 0


class TestEthTSynSubTlvConfigRoundTrip:
    def test_round_trip_preserves_field_values(self, writer, parser):
        """
        Write -> serialize -> parse keeps every field value.
        """
        parent = ET.Element("GLOBAL-TIME-ETH-MASTER")
        writer.writeEthTSynSubTlvConfig(parent, _new_config())
        xml = ET.tostring(parent, encoding="unicode")

        parsed_parent = ET.fromstring("<WRAP xmlns='%s'>%s</WRAP>" % (NS, xml))
        element = parsed_parent[0][0]
        config = EthTSynSubTlvConfig()
        parser.readEthTSynSubTlvConfig(element, config)

        assert config.getOfsSubTlv().getValue() is True
        assert config.getStatusSubTlv().getValue() is False
        assert config.getTimeSubTlv().getValue() is True
        assert config.getUserDataSubTlv().getValue() is True
