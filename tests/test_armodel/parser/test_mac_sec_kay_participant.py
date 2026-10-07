"""
Reader tests for MacSecKayParticipant (CP_TPS_SystemTemplate Table 3.122, p.175, R23-11).

Covers the IDENTIFIABLE base level (SHORT-NAME/UUID round-trip plus the S/T attributes
carried by readIdentifiable's chain down to readARObjectAttributes), the optional
CKN-REF/SAK-REF (REF elements whose required DEST facet is
CRYPTO-SERVICE-KEY--SUBTYPES-ENUM per AUTOSAR_00052.xsd group MAC-SEC-KAY-PARTICIPANT,
line 79093) and the nested CRYPTO-ALGO-CONFIG (read through the dedicated
readMacSecCryptoAlgoConfig level), the partial and empty cases. Fixtures follow the XSD
child order CKN-REF -> CRYPTO-ALGO-CONFIG -> SAK-REF.

Round-trip counterpart: tests/test_armodel/writer/test_mac_sec_kay_participant.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR as AutosarDocument
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import MacSecKayParticipant
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<MAC-SEC-KAY-PARTICIPANT xmlns='{NS}'>{inner}</MAC-SEC-KAY-PARTICIPANT>")


def _snip_with_attrs(attrs: str, inner: str) -> ET.Element:
    return ET.fromstring(f"<MAC-SEC-KAY-PARTICIPANT xmlns='{NS}' {attrs}>{inner}</MAC-SEC-KAY-PARTICIPANT>")


def _full_inner() -> str:
    return (
        "<SHORT-NAME>MKA1</SHORT-NAME>"
        "<CKN-REF DEST='CRYPTO-SERVICE-KEY'>/Keys/CknKey</CKN-REF>"
        "<CRYPTO-ALGO-CONFIG>"
        "<CAPABILITY>INTERGRITY-AND-CONFIDENTIALITY</CAPABILITY>"
        "<REPLAY-PROTECTION>true</REPLAY-PROTECTION>"
        "</CRYPTO-ALGO-CONFIG>"
        "<SAK-REF DEST='CRYPTO-SERVICE-KEY'>/Keys/SakKey</SAK-REF>"
    )


class TestReadMacSecKayParticipant:
    def test_read_identifiable_base_level(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip_with_attrs(
            "UUID='8e2f7c1a-9b34-4cde-a1d2-73f4a5b6c7d8' S='chk-7' T='2010-01-08T09:10:11Z'",
            "<SHORT-NAME>MKA1</SHORT-NAME>",
        )
        participant = MacSecKayParticipant(AutosarDocument.getInstance(), "MKA1")
        parser.readMacSecKayParticipant(element, participant)

        assert participant.getUuid().getValue() == "8e2f7c1a-9b34-4cde-a1d2-73f4a5b6c7d8"
        assert participant.getChecksum().getValue() == "chk-7"
        assert participant.getTimestamp().getValue() == "2010-01-08T09:10:11Z"
        assert participant.getCknRef() is None
        assert participant.getCryptoAlgoConfig() is None
        assert participant.getSakRef() is None

    def test_read_all_fields(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip(_full_inner())
        participant = MacSecKayParticipant(AutosarDocument.getInstance(), "Initial")
        parser.readMacSecKayParticipant(element, participant)

        assert participant.getCknRef().getValue() == "/Keys/CknKey"
        assert participant.getCknRef().getDest() == "CRYPTO-SERVICE-KEY"
        config = participant.getCryptoAlgoConfig()
        assert config is not None
        assert config.getCapability().getValue() == "INTERGRITY-AND-CONFIDENTIALITY"
        assert config.getReplayProtection().getValue() is True
        assert participant.getSakRef().getValue() == "/Keys/SakKey"
        assert participant.getSakRef().getDest() == "CRYPTO-SERVICE-KEY"

    def test_read_partial(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<SHORT-NAME>MKA1</SHORT-NAME>" "<CKN-REF DEST='CRYPTO-SERVICE-KEY'>/Keys/OnlyCkn</CKN-REF>")
        participant = MacSecKayParticipant(AutosarDocument.getInstance(), "Initial")
        parser.readMacSecKayParticipant(element, participant)

        assert participant.getCknRef().getValue() == "/Keys/OnlyCkn"
        assert participant.getCryptoAlgoConfig() is None
        assert participant.getSakRef() is None

    def test_read_empty_element(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<SHORT-NAME>MKA1</SHORT-NAME>")
        participant = MacSecKayParticipant(AutosarDocument.getInstance(), "MKA1")
        parser.readMacSecKayParticipant(element, participant)

        assert participant.getCknRef() is None
        assert participant.getCryptoAlgoConfig() is None
        assert participant.getSakRef() is None

    def test_read_empty_crypto_algo_config(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<SHORT-NAME>MKA1</SHORT-NAME>" "<CRYPTO-ALGO-CONFIG></CRYPTO-ALGO-CONFIG>")
        participant = MacSecKayParticipant(AutosarDocument.getInstance(), "Initial")
        parser.readMacSecKayParticipant(element, participant)

        config = participant.getCryptoAlgoConfig()
        assert config is not None
        assert config.getCapability() is None
        assert config.getReplayProtection() is None
