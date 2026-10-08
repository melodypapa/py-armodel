"""Tests for the readJ1939TpConfig handler (R23-11 J1939TpConfig, Table 6.267, p.624)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import J1939TpConfig, J1939TpConnection, J1939TpNode
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


def _config() -> J1939TpConfig:
    package = AUTOSAR.getInstance().createARPackage("TpConfigs")
    return J1939TpConfig(package, "J1939TpConfig1")


class TestReadJ1939TpConfig:
    """Tests for readJ1939TpConfig handler (R23-11 J1939TpConfig, Table 6.267, p.624)."""

    def test_read_j1939_tp_config_full(self, parser):
        element = _snip(
            """
                <SHORT-NAME>J1939TpConfig1</SHORT-NAME>
                <TP-ADDRESSS>
                    <TP-ADDRESS>
                        <SHORT-NAME>TpAddress1</SHORT-NAME>
                        <TP-ADDRESS>2047</TP-ADDRESS>
                    </TP-ADDRESS>
                </TP-ADDRESSS>
                <TP-CONNECTIONS>
                    <J-1939-TP-CONNECTION>
                        <SHORT-NAME>Connection1</SHORT-NAME>
                    </J-1939-TP-CONNECTION>
                </TP-CONNECTIONS>
                <TP-NODES>
                    <J-1939-TP-NODE>
                        <SHORT-NAME>Node1</SHORT-NAME>
                    </J-1939-TP-NODE>
                </TP-NODES>
            """,
            root_tag="J-1939-TP-CONFIG",
        )
        config = _config()
        parser.readJ1939TpConfig(element, config)

        addresses = config.getTpAddresses()
        assert len(addresses) == 1
        assert addresses[0].getShortName() == "TpAddress1"
        assert addresses[0].getTpAddress() is not None
        assert addresses[0].getTpAddress().getValue() == 2047

        connections = config.getTpConnections()
        assert len(connections) == 1
        assert isinstance(connections[0], J1939TpConnection)

        nodes = config.getTpNodes()
        assert len(nodes) == 1
        assert isinstance(nodes[0], J1939TpNode)
        assert nodes[0].getShortName() == "Node1"

    def test_read_j1939_tp_config_empty(self, parser):
        element = _snip(
            """
                <SHORT-NAME>J1939TpConfig1</SHORT-NAME>
            """,
            root_tag="J-1939-TP-CONFIG",
        )
        config = _config()
        parser.readJ1939TpConfig(element, config)

        assert config.getTpAddresses() == []
        assert config.getTpConnections() == []
        assert config.getTpNodes() == []
