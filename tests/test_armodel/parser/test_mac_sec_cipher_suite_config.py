"""
Reader tests for MacSecCipherSuiteConfig (CP_TPS_SystemTemplate Table 3.124, p.176, R23-11).

Covers the AR-OBJECT base level (S/T attributes carried by readARObject), the two
optional children — CIPHER-SUITE (String) and CIPHER-SUITE-PRIORITY (PositiveInteger) —
the partial and empty cases, and the CIPHER-SUITE-CONFIGS wrapper dispatch from
readMacSecCryptoAlgoConfig (the item element is the type name MAC-SEC-CIPHER-SUITE-CONFIG
per AUTOSAR_00052.xsd line 78994; group MAC-SEC-CIPHER-SUITE-CONFIG at line 78937 fixes
the child order CIPHER-SUITE -> CIPHER-SUITE-PRIORITY). Fixtures follow the XSD child
order.

Round-trip counterpart: tests/test_armodel/writer/test_mac_sec_cipher_suite_config.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import MacSecCipherSuiteConfig, MacSecCryptoAlgoConfig
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<MAC-SEC-CIPHER-SUITE-CONFIG xmlns='{NS}'>{inner}</MAC-SEC-CIPHER-SUITE-CONFIG>")


def _snip_with_attrs(attrs: str, inner: str) -> ET.Element:
    return ET.fromstring(f"<MAC-SEC-CIPHER-SUITE-CONFIG xmlns='{NS}' {attrs}>{inner}</MAC-SEC-CIPHER-SUITE-CONFIG>")


class TestReadMacSecCipherSuiteConfig:
    def test_read_arobject_base_level(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip_with_attrs(
            "S='chk-777' T='2011-07-08T09:10:11Z'",
            "<CIPHER-SUITE>GCM-AES-128</CIPHER-SUITE>",
        )
        config = MacSecCipherSuiteConfig()
        parser.readMacSecCipherSuiteConfig(element, config)

        assert config.getChecksum().getValue() == "chk-777"
        assert config.getTimestamp().getValue() == "2011-07-08T09:10:11Z"

    def test_read_all_fields(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<CIPHER-SUITE>GCM-AES-XPN-256</CIPHER-SUITE>" "<CIPHER-SUITE-PRIORITY>4</CIPHER-SUITE-PRIORITY>")
        config = MacSecCipherSuiteConfig()
        parser.readMacSecCipherSuiteConfig(element, config)

        assert config.getCipherSuite().getValue() == "GCM-AES-XPN-256"
        assert config.getCipherSuitePriority().getValue() == 4

    def test_read_partial(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<CIPHER-SUITE>GCM-AES-256</CIPHER-SUITE>")
        config = MacSecCipherSuiteConfig()
        parser.readMacSecCipherSuiteConfig(element, config)

        assert config.getCipherSuite().getValue() == "GCM-AES-256"
        assert config.getCipherSuitePriority() is None

    def test_read_empty_element(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("")
        config = MacSecCipherSuiteConfig()
        parser.readMacSecCipherSuiteConfig(element, config)

        assert config.getCipherSuite() is None
        assert config.getCipherSuitePriority() is None

    def test_wrapper_dispatch_via_mac_sec_crypto_algo_config(self):
        parser = ARXMLParser(options={"warning": True})
        element = ET.fromstring(
            "<MAC-SEC-CRYPTO-ALGO-CONFIG xmlns='%s'>"
            "<CIPHER-SUITE-CONFIGS>"
            "<MAC-SEC-CIPHER-SUITE-CONFIG><CIPHER-SUITE>GCM-AES-128</CIPHER-SUITE><CIPHER-SUITE-PRIORITY>1</CIPHER-SUITE-PRIORITY></MAC-SEC-CIPHER-SUITE-CONFIG>"
            "<MAC-SEC-CIPHER-SUITE-CONFIG S='chk-42'><CIPHER-SUITE>GCM-AES-256</CIPHER-SUITE><CIPHER-SUITE-PRIORITY>2</CIPHER-SUITE-PRIORITY></MAC-SEC-CIPHER-SUITE-CONFIG>"
            "</CIPHER-SUITE-CONFIGS>"
            "</MAC-SEC-CRYPTO-ALGO-CONFIG>" % NS
        )
        config = MacSecCryptoAlgoConfig()
        parser.readMacSecCryptoAlgoConfig(element, config)

        cipher_configs = config.getCipherSuiteConfigs()
        assert [c.getCipherSuite().getValue() for c in cipher_configs] == ["GCM-AES-128", "GCM-AES-256"]
        assert [c.getCipherSuitePriority().getValue() for c in cipher_configs] == [1, 2]
        assert cipher_configs[1].getChecksum().getValue() == "chk-42"
