"""Writer/reader round-trip tests for MacSecCryptoAlgoConfig (Table 3.123, p.175).

MacSecCryptoAlgoConfig is an ARObject aggregated by
MacSecKayParticipant.cryptoAlgoConfig (0..1). It carries the optional attributes
capability (MacSecCapabilityEnum, element CAPABILITY), cipherSuiteConfig
(MacSecCipherSuiteConfig, 0..4, wrapper CIPHER-SUITE-CONFIGS),
confidentialityOffset (MacSecConfidentialityOffsetEnum, element
CONFIDENTIALITY-OFFSET), replayProtection (Boolean, element REPLAY-PROTECTION)
and replayProtectionWindow (PositiveInteger, element REPLAY-PROTECTION-WINDOW).
"""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger, String
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import (
    MacSecCapabilityEnum,
    MacSecConfidentialityOffsetEnum,
    MacSecCryptoAlgoConfig,
)
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
    AUTOSAR.getInstance().new()
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    return ARXMLWriter()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    return ARXMLParser()


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


def _wrap(element: ET.Element) -> ET.Element:
    inner = ET.tostring(element).decode("utf-8")
    return ET.fromstring(f"<AUTOSAR xmlns='{NS}'>{inner}</AUTOSAR>")


def _string(value):
    s = String()
    s.setValue(value)
    return s


def _pos_int(value):
    p = PositiveInteger()
    p.setValue(str(value))
    return p


def _bool(value):
    b = Boolean()
    b.setValue(value)
    return b


def _enum(enum_cls, value):
    e = enum_cls()
    e.setValue(value)
    return e


def _new_crypto_algo_config():
    config = MacSecCryptoAlgoConfig()
    config.setCapability(_enum(MacSecCapabilityEnum, "intergrityAndConfidentiality"))
    c1 = config.createCipherSuiteConfig()
    c1.setCipherSuite(_string("GCM-AES-128"))
    c1.setCipherSuitePriority(_pos_int(1))
    c2 = config.createCipherSuiteConfig()
    c2.setCipherSuite(_string("GCM-AES-256"))
    c2.setCipherSuitePriority(_pos_int(2))
    config.setConfidentialityOffset(_enum(MacSecConfidentialityOffsetEnum, "CONFIDENTIALITY-OFFSET-30"))
    config.setReplayProtection(_bool("true"))
    config.setReplayProtectionWindow(_pos_int(100))
    return config


class TestWriteMacSecCryptoAlgoConfig:
    def test_write_all_fields(self, writer):
        config = _new_crypto_algo_config()
        parent = ET.Element("CONFIGS")
        writer.writeMacSecCryptoAlgoConfig(parent, config)

        node = parent.find("MAC-SEC-CRYPTO-ALGO-CONFIG")
        assert node is not None
        assert node.find("CAPABILITY").text == "intergrityAndConfidentiality"
        wrapper = node.find("CIPHER-SUITE-CONFIGS")
        assert wrapper is not None
        children = wrapper.findall("MAC-SEC-CIPHER-SUITE-CONFIG")
        assert len(children) == 2
        assert children[0].find("CIPHER-SUITE").text == "GCM-AES-128"
        assert children[0].find("CIPHER-SUITE-PRIORITY").text == "1"
        assert children[1].find("CIPHER-SUITE").text == "GCM-AES-256"
        assert children[1].find("CIPHER-SUITE-PRIORITY").text == "2"
        assert node.find("CONFIDENTIALITY-OFFSET").text == "CONFIDENTIALITY-OFFSET-30"
        assert node.find("REPLAY-PROTECTION").text == "true"
        assert node.find("REPLAY-PROTECTION-WINDOW").text == "100"

    def test_write_empty_omits_fields(self, writer):
        config = MacSecCryptoAlgoConfig()
        parent = ET.Element("CONFIGS")
        writer.writeMacSecCryptoAlgoConfig(parent, config)

        node = parent.find("MAC-SEC-CRYPTO-ALGO-CONFIG")
        assert node is not None
        assert node.find("CAPABILITY") is None
        assert node.find("CIPHER-SUITE-CONFIGS") is None
        assert node.find("CONFIDENTIALITY-OFFSET") is None
        assert node.find("REPLAY-PROTECTION") is None
        assert node.find("REPLAY-PROTECTION-WINDOW") is None


class TestMacSecCryptoAlgoConfigRoundTrip:
    def test_round_trip_preserves_all_values(self, writer, parser, tmp_path):
        config = _new_crypto_algo_config()

        parent = ET.Element("CONFIGS")
        writer.writeMacSecCryptoAlgoConfig(parent, config)

        out_file = str(tmp_path / "mac_sec_crypto_algo_config.arxml")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(ET.tostring(_wrap(parent), encoding="unicode"))

        tree = ET.parse(out_file)
        recovered = MacSecCryptoAlgoConfig()
        parser.readMacSecCryptoAlgoConfig(tree.getroot()[0][0], recovered)

        assert recovered.getCapability().getValue() == "intergrityAndConfidentiality"
        cipher_configs = recovered.getCipherSuiteConfigs()
        assert [c.getCipherSuite().getValue() for c in cipher_configs] == ["GCM-AES-128", "GCM-AES-256"]
        assert [c.getCipherSuitePriority().getValue() for c in cipher_configs] == [1, 2]
        assert recovered.getConfidentialityOffset().getValue() == "CONFIDENTIALITY-OFFSET-30"
        assert recovered.getReplayProtection().getValue() is True
        assert recovered.getReplayProtectionWindow().getValue() == 100

    def test_reader_empty_fields(self, parser):
        xml = "<AUTOSAR xmlns='%s'>" "<CONFIGS><MAC-SEC-CRYPTO-ALGO-CONFIG/></CONFIGS>" "</AUTOSAR>" % NS
        root = ET.fromstring(xml)
        recovered = MacSecCryptoAlgoConfig()
        parser.readMacSecCryptoAlgoConfig(root[0][0], recovered)

        assert recovered.getCapability() is None
        assert recovered.getCipherSuiteConfigs() == []
        assert recovered.getConfidentialityOffset() is None
        assert recovered.getReplayProtection() is None
        assert recovered.getReplayProtectionWindow() is None

    def test_reader_empty_wrapper_list(self, parser):
        xml = "<AUTOSAR xmlns='%s'>" "<CONFIGS><MAC-SEC-CRYPTO-ALGO-CONFIG><CIPHER-SUITE-CONFIGS/></MAC-SEC-CRYPTO-ALGO-CONFIG></CONFIGS>" "</AUTOSAR>" % NS
        root = ET.fromstring(xml)
        recovered = MacSecCryptoAlgoConfig()
        parser.readMacSecCryptoAlgoConfig(root[0][0], recovered)

        assert recovered.getCipherSuiteConfigs() == []
