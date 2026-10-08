"""
Reader tests for MacSecCryptoAlgoConfig (CP_TPS_SystemTemplate Table 3.123, p.175, R23-11).

Covers the AR-OBJECT base level (S/T attributes carried by readARObject), the five
optional children — CAPABILITY (MacSecCapabilityEnum), CIPHER-SUITE-CONFIGS (wrapper
holding up to four MAC-SEC-CIPHER-SUITE-CONFIG items), CONFIDENTIALITY-OFFSET
(MacSecConfidentialityOffsetEnum), REPLAY-PROTECTION (Boolean) and
REPLAY-PROTECTION-WINDOW (PositiveInteger) — the partial and empty cases, and the
CRYPTO-ALGO-CONFIG role-element dispatch from readMacSecKayParticipant (the role tag
per AUTOSAR_00052.xsd line 79113; group MAC-SEC-CRYPTO-ALGO-CONFIG at line 78974 fixes
the child order CAPABILITY -> CIPHER-SUITE-CONFIGS -> CONFIDENTIALITY-OFFSET ->
REPLAY-PROTECTION -> REPLAY-PROTECTION-WINDOW). Fixtures follow the XSD child order.

Round-trip counterpart: tests/test_armodel/writer/test_mac_sec_crypto_algo_config.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR as AutosarDocument
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import MacSecCryptoAlgoConfig, MacSecKayParticipant
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<CRYPTO-ALGO-CONFIG xmlns='{NS}'>{inner}</CRYPTO-ALGO-CONFIG>")


def _snip_with_attrs(attrs: str, inner: str) -> ET.Element:
    return ET.fromstring(f"<CRYPTO-ALGO-CONFIG xmlns='{NS}' {attrs}>{inner}</CRYPTO-ALGO-CONFIG>")


def _full_inner() -> str:
    return (
        "<CAPABILITY>INTERGRITY-AND-CONFIDENTIALITY</CAPABILITY>"
        "<CIPHER-SUITE-CONFIGS>"
        "<MAC-SEC-CIPHER-SUITE-CONFIG><CIPHER-SUITE>GCM-AES-128</CIPHER-SUITE><CIPHER-SUITE-PRIORITY>1</CIPHER-SUITE-PRIORITY></MAC-SEC-CIPHER-SUITE-CONFIG>"
        "<MAC-SEC-CIPHER-SUITE-CONFIG><CIPHER-SUITE>GCM-AES-256</CIPHER-SUITE><CIPHER-SUITE-PRIORITY>2</CIPHER-SUITE-PRIORITY></MAC-SEC-CIPHER-SUITE-CONFIG>"
        "</CIPHER-SUITE-CONFIGS>"
        "<CONFIDENTIALITY-OFFSET>CONFIDENTIALITY-OFFSET--30</CONFIDENTIALITY-OFFSET>"
        "<REPLAY-PROTECTION>true</REPLAY-PROTECTION>"
        "<REPLAY-PROTECTION-WINDOW>100</REPLAY-PROTECTION-WINDOW>"
    )


class TestReadMacSecCryptoAlgoConfig:
    def test_read_arobject_base_level(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip_with_attrs(
            "S='chk-123' T='2010-04-05T06:07:08Z'",
            "<CAPABILITY>INTERGRITY-WITHOUT-CONFIDENTIALITY</CAPABILITY>",
        )
        config = MacSecCryptoAlgoConfig()
        parser.readMacSecCryptoAlgoConfig(element, config)

        assert config.getChecksum().getValue() == "chk-123"
        assert config.getTimestamp().getValue() == "2010-04-05T06:07:08Z"

    def test_read_all_fields(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip(_full_inner())
        config = MacSecCryptoAlgoConfig()
        parser.readMacSecCryptoAlgoConfig(element, config)

        assert config.getCapability().getValue() == "INTERGRITY-AND-CONFIDENTIALITY"
        cipher_configs = config.getCipherSuiteConfigs()
        assert [c.getCipherSuite().getValue() for c in cipher_configs] == ["GCM-AES-128", "GCM-AES-256"]
        assert [c.getCipherSuitePriority().getValue() for c in cipher_configs] == [1, 2]
        assert config.getConfidentialityOffset().getValue() == "CONFIDENTIALITY-OFFSET--30"
        assert config.getReplayProtection().getValue() is True
        assert config.getReplayProtectionWindow().getValue() == 100

    def test_read_partial(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<CAPABILITY>INTERGRITY-AND-CONFIDENTIALITY</CAPABILITY>" "<REPLAY-PROTECTION-WINDOW>7</REPLAY-PROTECTION-WINDOW>")
        config = MacSecCryptoAlgoConfig()
        parser.readMacSecCryptoAlgoConfig(element, config)

        assert config.getCapability().getValue() == "INTERGRITY-AND-CONFIDENTIALITY"
        assert config.getCipherSuiteConfigs() == []
        assert config.getConfidentialityOffset() is None
        assert config.getReplayProtection() is None
        assert config.getReplayProtectionWindow().getValue() == 7

    def test_read_empty_element(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("")
        config = MacSecCryptoAlgoConfig()
        parser.readMacSecCryptoAlgoConfig(element, config)

        assert config.getCapability() is None
        assert config.getCipherSuiteConfigs() == []
        assert config.getConfidentialityOffset() is None
        assert config.getReplayProtection() is None
        assert config.getReplayProtectionWindow() is None

    def test_read_empty_cipher_suite_configs_wrapper(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<CIPHER-SUITE-CONFIGS/>")
        config = MacSecCryptoAlgoConfig()
        parser.readMacSecCryptoAlgoConfig(element, config)

        assert config.getCipherSuiteConfigs() == []

    def test_role_element_dispatch_via_mac_sec_kay_participant(self):
        parser = ARXMLParser(options={"warning": True})
        element = ET.fromstring(
            "<MAC-SEC-KAY-PARTICIPANT xmlns='%s'>"
            "<SHORT-NAME>MKA1</SHORT-NAME>"
            "<CRYPTO-ALGO-CONFIG>"
            "<CAPABILITY>INTERGRITY-AND-CONFIDENTIALITY</CAPABILITY>"
            "<REPLAY-PROTECTION>true</REPLAY-PROTECTION>"
            "</CRYPTO-ALGO-CONFIG>"
            "</MAC-SEC-KAY-PARTICIPANT>" % NS
        )
        participant = MacSecKayParticipant(AutosarDocument.getInstance(), "MKA1")
        parser.readMacSecKayParticipant(element, participant)

        config = participant.getCryptoAlgoConfig()
        assert config is not None
        assert config.getCapability().getValue() == "INTERGRITY-AND-CONFIDENTIALITY"
        assert config.getReplayProtection().getValue() is True
