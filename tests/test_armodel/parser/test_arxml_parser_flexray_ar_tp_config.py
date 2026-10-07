"""Tests for the readFlexrayArTpConfig handler (R23-11 FlexrayArTpConfig, Table 6.245, p.600)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import FlexrayArTpConfig
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


def _config() -> FlexrayArTpConfig:
    package = AUTOSAR.getInstance().createARPackage("TpConfigs")
    return FlexrayArTpConfig(package, "FlexrayArTpConfig1")


class TestReadFlexrayArTpConfig:
    """Tests for readFlexrayArTpConfig handler (R23-11 FlexrayArTpConfig, Table 6.245, p.600)."""

    def test_read_flexray_ar_tp_config_full(self, parser):
        element = _snip(
            """
                <SHORT-NAME>FlexrayArTpConfig1</SHORT-NAME>
                <TP-ADDRESSS>
                    <TP-ADDRESS>
                        <SHORT-NAME>Address1</SHORT-NAME>
                        <TP-ADDRESS>2048</TP-ADDRESS>
                    </TP-ADDRESS>
                </TP-ADDRESSS>
                <TP-CHANNELS>
                    <FLEXRAY-AR-TP-CHANNEL>
                        <SHORT-NAME>Channel1</SHORT-NAME>
                    </FLEXRAY-AR-TP-CHANNEL>
                </TP-CHANNELS>
                <TP-NODES>
                    <FLEXRAY-AR-TP-NODE>
                        <SHORT-NAME>Node1</SHORT-NAME>
                    </FLEXRAY-AR-TP-NODE>
                </TP-NODES>
            """,
            root_tag="FLEXRAY-AR-TP-CONFIG",
        )
        config = _config()
        parser.readFlexrayArTpConfig(element, config)
        addresses = config.getTpAddresses()
        assert len(addresses) == 1
        assert addresses[0].getShortName() == "Address1"
        assert addresses[0].getTpAddress().getValue() == 2048
        channels = config.getTpChannels()
        assert len(channels) == 1
        nodes = config.getTpNodes()
        assert len(nodes) == 1
        assert nodes[0].getShortName() == "Node1"

    def test_read_flexray_ar_tp_config_empty(self, parser):
        element = _snip(
            """
                <SHORT-NAME>FlexrayArTpConfig1</SHORT-NAME>
            """,
            root_tag="FLEXRAY-AR-TP-CONFIG",
        )
        config = _config()
        parser.readFlexrayArTpConfig(element, config)
        assert config.getTpAddresses() == []
        assert config.getTpChannels() == []
        assert config.getTpNodes() == []
