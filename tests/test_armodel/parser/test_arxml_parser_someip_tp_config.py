"""Tests for the readSomeipTpConfig handler (R23-11 SomeipTpConfig, Table 6.264, p.619)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import SomeipTpConfig
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


def _config() -> SomeipTpConfig:
    package = AUTOSAR.getInstance().createARPackage("TpConfigs")
    return SomeipTpConfig(package, "SomeipTpConfig1")


class TestReadSomeipTpConfig:
    """Tests for readSomeipTpConfig handler (R23-11 SomeipTpConfig, Table 6.264, p.619)."""

    def test_read_someip_tp_config_full(self, parser):
        element = _snip(
            """
                <SHORT-NAME>SomeipTpConfig1</SHORT-NAME>
                <TP-CHANNELS>
                    <SOMEIP-TP-CHANNEL>
                        <SHORT-NAME>Channel1</SHORT-NAME>
                    </SOMEIP-TP-CHANNEL>
                </TP-CHANNELS>
                <TP-CONNECTIONS>
                    <SOMEIP-TP-CONNECTION>
                        <SHORT-NAME>Connection1</SHORT-NAME>
                    </SOMEIP-TP-CONNECTION>
                    <SOMEIP-TP-CONNECTION>
                        <SHORT-NAME>Connection2</SHORT-NAME>
                    </SOMEIP-TP-CONNECTION>
                </TP-CONNECTIONS>
            """,
            root_tag="SOMEIP-TP-CONFIG",
        )
        config = _config()
        parser.readSomeipTpConfig(element, config)
        channels = config.getTpChannels()
        assert len(channels) == 1
        assert channels[0].getShortName() == "Channel1"
        connections = config.getTpConnections()
        assert len(connections) == 2

    def test_read_someip_tp_config_empty(self, parser):
        element = _snip(
            """
                <SHORT-NAME>SomeipTpConfig1</SHORT-NAME>
            """,
            root_tag="SOMEIP-TP-CONFIG",
        )
        config = _config()
        parser.readSomeipTpConfig(element, config)
        assert config.getTpChannels() == []
        assert config.getTpConnections() == []
