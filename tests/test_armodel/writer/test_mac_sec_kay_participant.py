"""
Writer/reader round-trip tests for MacSecKayParticipant (Table 3.122, p.175).

MacSecKayParticipant is an Identifiable class aggregated by
MacSecParticipantSet.mkaParticipant (0..*, excluded from this closure). It carries
the optional attributes ckn (CryptoServiceKey, element CKN-REF), cryptoAlgoConfig
(MacSecCryptoAlgoConfig, element CRYPTO-ALGO-CONFIG) and sak (CryptoServiceKey,
element SAK-REF); the XSD group MAC-SEC-KAY-PARTICIPANT (AUTOSAR_00052.xsd line
79093) fixes the child order CKN-REF -> CRYPTO-ALGO-CONFIG -> SAK-REF, and both REF
elements require the DEST facet CRYPTO-SERVICE-KEY--SUBTYPES-ENUM.

Reader counterpart: tests/test_armodel/parser/test_mac_sec_kay_participant.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger, RefType, String
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import (
    MacSecCapabilityEnum,
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


def _ref(value):
    ref = RefType()
    ref.setValue(value)
    ref.setDest("CRYPTO-SERVICE-KEY")
    return ref


def _new_kay_participant():
    participant = MacSecKayParticipant(MockParent(), "participant_1")
    participant.setCknRef(_ref("/Sec/CryptoKeyCkn"))
    config = MacSecCryptoAlgoConfig()
    capability = MacSecCapabilityEnum()
    capability.setValue(MacSecCapabilityEnum.INTERGRITY_AND_CONFIDENTIALITY)
    config.setCapability(capability)
    replay = Boolean()
    replay.setValue("true")
    config.setReplayProtection(replay)
    window = PositiveInteger()
    window.setValue("100")
    config.setReplayProtectionWindow(window)
    participant.setCryptoAlgoConfig(config)
    participant.setSakRef(_ref("/Sec/CryptoKeySak"))
    return participant


class TestWriteMacSecKayParticipant:
    def test_write_all_fields(self, writer):
        participant = _new_kay_participant()
        parent = ET.Element("CONFIGS")
        writer.writeMacSecKayParticipant(parent, participant)

        node = parent.find("MAC-SEC-KAY-PARTICIPANT")
        assert node is not None
        assert node.find("SHORT-NAME").text == "participant_1"
        assert [child.tag for child in node] == ["SHORT-NAME", "CKN-REF", "CRYPTO-ALGO-CONFIG", "SAK-REF"]
        ckn_ref = node.find("CKN-REF")
        assert ckn_ref.text == "/Sec/CryptoKeyCkn"
        assert ckn_ref.get("DEST") == "CRYPTO-SERVICE-KEY"
        algo = node.find("CRYPTO-ALGO-CONFIG")
        assert algo is not None
        assert algo.find("CAPABILITY").text == "INTERGRITY-AND-CONFIDENTIALITY"
        assert algo.find("REPLAY-PROTECTION").text == "true"
        assert algo.find("REPLAY-PROTECTION-WINDOW").text == "100"
        sak_ref = node.find("SAK-REF")
        assert sak_ref.text == "/Sec/CryptoKeySak"
        assert sak_ref.get("DEST") == "CRYPTO-SERVICE-KEY"

    def test_write_empty_omits_fields(self, writer):
        participant = MacSecKayParticipant(MockParent(), "participant_1")
        parent = ET.Element("CONFIGS")
        writer.writeMacSecKayParticipant(parent, participant)

        node = parent.find("MAC-SEC-KAY-PARTICIPANT")
        assert node is not None
        assert [child.tag for child in node] == ["SHORT-NAME"]
        assert node.find("CKN-REF") is None
        assert node.find("CRYPTO-ALGO-CONFIG") is None
        assert node.find("SAK-REF") is None


class TestMacSecKayParticipantRoundTrip:
    def test_round_trip_preserves_all_values(self, writer, parser, tmp_path):
        participant = _new_kay_participant()
        uuid = String()
        uuid.setValue("8e2f7c1a-9b34-4cde-a1d2-73f4a5b6c7d8")
        participant.setUuid(uuid)

        parent = ET.Element("CONFIGS")
        writer.writeMacSecKayParticipant(parent, participant)

        out_file = str(tmp_path / "mac_sec_kay_participant.arxml")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(ET.tostring(_wrap(parent), encoding="unicode"))

        tree = ET.parse(out_file)
        recovered = MacSecKayParticipant(MockParent(), "participant_1")
        parser.readMacSecKayParticipant(tree.getroot()[0][0], recovered)

        assert recovered.getShortName() == "participant_1"
        assert recovered.getUuid().getValue() == "8e2f7c1a-9b34-4cde-a1d2-73f4a5b6c7d8"
        assert recovered.getCknRef().getValue() == "/Sec/CryptoKeyCkn"
        assert recovered.getCknRef().getDest() == "CRYPTO-SERVICE-KEY"
        algo = recovered.getCryptoAlgoConfig()
        assert algo is not None
        assert algo.getCapability().getValue() == MacSecCapabilityEnum.INTERGRITY_AND_CONFIDENTIALITY
        assert algo.getReplayProtection().getValue() is True
        assert algo.getReplayProtectionWindow().getValue() == 100
        assert recovered.getSakRef().getValue() == "/Sec/CryptoKeySak"
        assert recovered.getSakRef().getDest() == "CRYPTO-SERVICE-KEY"

    def test_reader_empty_fields(self, parser):
        xml = "<AUTOSAR xmlns='%s'>" "<CONFIGS><MAC-SEC-KAY-PARTICIPANT/></CONFIGS>" "</AUTOSAR>" % NS
        root = ET.fromstring(xml)
        recovered = MacSecKayParticipant(MockParent(), "participant_1")
        parser.readMacSecKayParticipant(root[0][0], recovered)

        assert recovered.getCknRef() is None
        assert recovered.getCryptoAlgoConfig() is None
        assert recovered.getSakRef() is None
