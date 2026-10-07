"""Tests for the readEthTpConfig handler (R23-11 EthTpConfig, Table 6.262, p.617)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import EthTpConfig
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test and pin the R23-11 release."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    """Fresh ARXMLParser instance."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLParser()


def _snip(inner: str, root_tag: str = "ROOT") -> ET.Element:
    """Wrap an inner XML fragment in a root element bound to the AUTOSAR NS."""
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


def _config() -> EthTpConfig:
    package = AUTOSAR.getInstance().createARPackage("TpConfigs")
    return EthTpConfig(package, "EthTpConfig1")


class TestReadEthTpConfig:
    """Tests for readEthTpConfig handler (R23-11 EthTpConfig, Table 6.262, p.617)."""

    def test_read_eth_tp_config_full(self, parser):
        element = _snip(
            """
                <SHORT-NAME>EthTpConfig1</SHORT-NAME>
                <TP-CONNECTIONS>
                    <ETH-TP-CONNECTION>
                        <SHORT-NAME>Connection1</SHORT-NAME>
                    </ETH-TP-CONNECTION>
                    <ETH-TP-CONNECTION>
                        <SHORT-NAME>Connection2</SHORT-NAME>
                    </ETH-TP-CONNECTION>
                </TP-CONNECTIONS>
            """,
            root_tag="ETH-TP-CONFIG",
        )
        config = _config()
        parser.readEthTpConfig(element, config)
        connections = config.getTpConnections()
        assert len(connections) == 2

    def test_read_eth_tp_config_empty(self, parser):
        element = _snip(
            """
                <SHORT-NAME>EthTpConfig1</SHORT-NAME>
            """,
            root_tag="ETH-TP-CONFIG",
        )
        config = _config()
        parser.readEthTpConfig(element, config)
        assert config.getTpConnections() == []
