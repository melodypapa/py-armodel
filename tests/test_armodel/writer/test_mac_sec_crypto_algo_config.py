"""
Writer/reader round-trip tests for MacSecCryptoAlgoConfig (Table 3.123, p.175, R23-11).

MacSecCryptoAlgoConfig is an ARObject aggregated by MacSecKayParticipant.cryptoAlgoConfig
(0..1). The dedicated writer level emits the XSD ROLE element CRYPTO-ALGO-CONFIG
(AUTOSAR_00052.xsd line 79113 — the type-name element MAC-SEC-CRYPTO-ALGO-CONFIG never
appears on the wire inside MAC-SEC-KAY-PARTICIPANT) and calls writeARObject once (S/T);
the XSD group MAC-SEC-CRYPTO-ALGO-CONFIG (line 78974) fixes the child order CAPABILITY ->
CIPHER-SUITE-CONFIGS (wrapper, up to four MAC-SEC-CIPHER-SUITE-CONFIG items) ->
CONFIDENTIALITY-OFFSET -> REPLAY-PROTECTION -> REPLAY-PROTECTION-WINDOW. The dispatch
test pins the byte-identical inline emission of the role element by
writeMacSecKayParticipant.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, DateTime, PositiveInteger, String
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import (
    MacSecCapabilityEnum,
    MacSecCipherSuiteConfig,
    MacSecConfidentialityOffsetEnum,
    MacSecCryptoAlgoConfig,
    MacSecKayParticipant,
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
    config.setCapability(_enum(MacSecCapabilityEnum, "INTERGRITY-AND-CONFIDENTIALITY"))
    c1 = MacSecCipherSuiteConfig()
    c1.setCipherSuite(_string("GCM-AES-128"))
    c1.setCipherSuitePriority(_pos_int(1))
    config.addCipherSuiteConfig(c1)
    c2 = MacSecCipherSuiteConfig()
    c2.setCipherSuite(_string("GCM-AES-256"))
    c2.setCipherSuitePriority(_pos_int(2))
    config.addCipherSuiteConfig(c2)
    config.setConfidentialityOffset(_enum(MacSecConfidentialityOffsetEnum, "CONFIDENTIALITY-OFFSET--30"))
    config.setReplayProtection(_bool("true"))
    config.setReplayProtectionWindow(_pos_int(100))
    return config


class TestWriteMacSecCryptoAlgoConfig:
    def test_write_all_fields(self, writer):
        config = _new_crypto_algo_config()
        parent = ET.Element("CONFIGS")
        writer.writeMacSecCryptoAlgoConfig(parent, config)

        node = parent.find("CRYPTO-ALGO-CONFIG")
        assert node is not None
        assert node.find("CAPABILITY").text == "INTERGRITY-AND-CONFIDENTIALITY"
        wrapper = node.find("CIPHER-SUITE-CONFIGS")
        assert wrapper is not None
        children = wrapper.findall("MAC-SEC-CIPHER-SUITE-CONFIG")
        assert len(children) == 2
        assert children[0].find("CIPHER-SUITE").text == "GCM-AES-128"
        assert children[0].find("CIPHER-SUITE-PRIORITY").text == "1"
        assert children[1].find("CIPHER-SUITE").text == "GCM-AES-256"
        assert children[1].find("CIPHER-SUITE-PRIORITY").text == "2"
        assert node.find("CONFIDENTIALITY-OFFSET").text == "CONFIDENTIALITY-OFFSET--30"
        assert node.find("REPLAY-PROTECTION").text == "true"
        assert node.find("REPLAY-PROTECTION-WINDOW").text == "100"

    def test_write_xsd_child_order(self, writer):
        config = _new_crypto_algo_config()
        parent = ET.Element("CONFIGS")
        writer.writeMacSecCryptoAlgoConfig(parent, config)

        node = parent.find("CRYPTO-ALGO-CONFIG")
        assert [child.tag for child in node] == [
            "CAPABILITY",
            "CIPHER-SUITE-CONFIGS",
            "CONFIDENTIALITY-OFFSET",
            "REPLAY-PROTECTION",
            "REPLAY-PROTECTION-WINDOW",
        ]

    def test_write_arobject_base_level(self, writer):
        config = MacSecCryptoAlgoConfig()
        config.setCapability(_enum(MacSecCapabilityEnum, "INTERGRITY-AND-CONFIDENTIALITY"))
        config.setChecksum(_string("chk-123"))
        timestamp = DateTime()
        timestamp.setValue("2010-04-05T06:07:08Z")
        config.setTimestamp(timestamp)

        parent = ET.Element("CONFIGS")
        writer.writeMacSecCryptoAlgoConfig(parent, config)

        node = parent.find("CRYPTO-ALGO-CONFIG")
        assert node is not None
        assert node.get("S") == "chk-123"
        assert node.get("T") == "2010-04-05T06:07:08Z"

    def test_write_empty_omits_fields(self, writer):
        config = MacSecCryptoAlgoConfig()
        parent = ET.Element("CONFIGS")
        writer.writeMacSecCryptoAlgoConfig(parent, config)

        node = parent.find("CRYPTO-ALGO-CONFIG")
        assert node is not None
        assert len(node) == 0
        assert node.find("CAPABILITY") is None
        assert node.find("CIPHER-SUITE-CONFIGS") is None
        assert node.find("CONFIDENTIALITY-OFFSET") is None
        assert node.find("REPLAY-PROTECTION") is None
        assert node.find("REPLAY-PROTECTION-WINDOW") is None

    def test_dispatch_via_write_mac_sec_kay_participant(self, writer):
        participant = MacSecKayParticipant(MockParent(), "participant_1")
        participant.setCryptoAlgoConfig(_new_crypto_algo_config())

        parent = ET.Element("CONFIGS")
        writer.writeMacSecKayParticipant(parent, participant)

        node = parent.find("MAC-SEC-KAY-PARTICIPANT")
        assert node is not None
        assert [child.tag for child in node] == ["SHORT-NAME", "CRYPTO-ALGO-CONFIG"]
        algo = node.find("CRYPTO-ALGO-CONFIG")
        assert algo.find("CAPABILITY").text == "INTERGRITY-AND-CONFIDENTIALITY"
        assert [child.tag for child in algo] == [
            "CAPABILITY",
            "CIPHER-SUITE-CONFIGS",
            "CONFIDENTIALITY-OFFSET",
            "REPLAY-PROTECTION",
            "REPLAY-PROTECTION-WINDOW",
        ]
        assert algo.find("REPLAY-PROTECTION-WINDOW").text == "100"


class TestMacSecCryptoAlgoConfigRoundTrip:
    def test_round_trip_preserves_all_values(self, writer, parser, tmp_path):
        config = _new_crypto_algo_config()
        config.setChecksum(_string("chk-rt"))
        timestamp = DateTime()
        timestamp.setValue("2011-01-02T03:04:05Z")
        config.setTimestamp(timestamp)

        parent = ET.Element("CONFIGS")
        writer.writeMacSecCryptoAlgoConfig(parent, config)

        out_file = str(tmp_path / "mac_sec_crypto_algo_config.arxml")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(ET.tostring(_wrap(parent), encoding="unicode"))

        tree = ET.parse(out_file)
        recovered = MacSecCryptoAlgoConfig()
        parser.readMacSecCryptoAlgoConfig(tree.getroot()[0][0], recovered)

        assert recovered.getChecksum().getValue() == "chk-rt"
        assert recovered.getTimestamp().getValue() == "2011-01-02T03:04:05Z"
        assert recovered.getCapability().getValue() == MacSecCapabilityEnum.INTERGRITY_AND_CONFIDENTIALITY
        cipher_configs = recovered.getCipherSuiteConfigs()
        assert [c.getCipherSuite().getValue() for c in cipher_configs] == ["GCM-AES-128", "GCM-AES-256"]
        assert [c.getCipherSuitePriority().getValue() for c in cipher_configs] == [1, 2]
        assert recovered.getConfidentialityOffset().getValue() == MacSecConfidentialityOffsetEnum.CONFIDENTIALITY_OFFSET_30
        assert recovered.getReplayProtection().getValue() is True
        assert recovered.getReplayProtectionWindow().getValue() == 100

    def test_reader_empty_fields(self, parser):
        xml = "<AUTOSAR xmlns='%s'>" "<CONFIGS><CRYPTO-ALGO-CONFIG/></CONFIGS>" "</AUTOSAR>" % NS
        root = ET.fromstring(xml)
        recovered = MacSecCryptoAlgoConfig()
        parser.readMacSecCryptoAlgoConfig(root[0][0], recovered)

        assert recovered.getCapability() is None
        assert recovered.getCipherSuiteConfigs() == []
        assert recovered.getConfidentialityOffset() is None
        assert recovered.getReplayProtection() is None
        assert recovered.getReplayProtectionWindow() is None

    def test_reader_empty_wrapper_list(self, parser):
        xml = "<AUTOSAR xmlns='%s'>" "<CONFIGS><CRYPTO-ALGO-CONFIG><CIPHER-SUITE-CONFIGS/></CRYPTO-ALGO-CONFIG></CONFIGS>" "</AUTOSAR>" % NS
        root = ET.fromstring(xml)
        recovered = MacSecCryptoAlgoConfig()
        parser.readMacSecCryptoAlgoConfig(root[0][0], recovered)

        assert recovered.getCipherSuiteConfigs() == []
