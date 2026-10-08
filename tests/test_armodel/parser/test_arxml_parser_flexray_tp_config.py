"""Tests for the readFlexrayTpConfig handler (R23-11 FlexrayTpConfig, Table 6.239, p.592)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import FlexrayTpConfig
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


def _config() -> FlexrayTpConfig:
    package = AUTOSAR.getInstance().createARPackage("TpConfigs")
    return FlexrayTpConfig(package, "FlexrayTpConfig1")


class TestReadFlexrayTpConfig:
    """Tests for readFlexrayTpConfig handler (R23-11 FlexrayTpConfig, Table 6.239, p.592)."""

    def test_read_flexray_tp_config_full(self, parser):
        element = _snip(
            """
                <SHORT-NAME>FlexrayTpConfig1</SHORT-NAME>
                <PDU-POOLS>
                    <FLEXRAY-TP-PDU-POOL>
                        <SHORT-NAME>Pool1</SHORT-NAME>
                    </FLEXRAY-TP-PDU-POOL>
                </PDU-POOLS>
                <TP-ADDRESSS>
                    <TP-ADDRESS>
                        <SHORT-NAME>Address1</SHORT-NAME>
                        <TP-ADDRESS>2048</TP-ADDRESS>
                    </TP-ADDRESS>
                    <TP-ADDRESS>
                        <SHORT-NAME>Address2</SHORT-NAME>
                        <TP-ADDRESS>4096</TP-ADDRESS>
                    </TP-ADDRESS>
                </TP-ADDRESSS>
                <TP-CONNECTIONS>
                    <FLEXRAY-TP-CONNECTION>
                        <SHORT-NAME>Connection1</SHORT-NAME>
                    </FLEXRAY-TP-CONNECTION>
                </TP-CONNECTIONS>
                <TP-CONNECTION-CONTROLS>
                    <FLEXRAY-TP-CONNECTION-CONTROL>
                        <SHORT-NAME>Control1</SHORT-NAME>
                    </FLEXRAY-TP-CONNECTION-CONTROL>
                </TP-CONNECTION-CONTROLS>
                <TP-ECUS>
                    <FLEXRAY-TP-ECU/>
                </TP-ECUS>
                <TP-NODES>
                    <FLEXRAY-TP-NODE>
                        <SHORT-NAME>Node1</SHORT-NAME>
                    </FLEXRAY-TP-NODE>
                </TP-NODES>
            """,
            root_tag="FLEXRAY-TP-CONFIG",
        )
        config = _config()
        parser.readFlexrayTpConfig(element, config)
        pools = config.getPduPools()
        assert len(pools) == 1
        assert pools[0].getShortName() == "Pool1"
        addresses = config.getTpAddresses()
        assert len(addresses) == 2
        assert addresses[0].getShortName() == "Address1"
        assert addresses[0].getTpAddress().getValue() == 2048
        assert addresses[1].getShortName() == "Address2"
        assert addresses[1].getTpAddress().getValue() == 4096
        connections = config.getTpConnections()
        assert len(connections) == 1
        controls = config.getTpConnectionControls()
        assert len(controls) == 1
        assert controls[0].getShortName() == "Control1"
        ecus = config.getTpEcus()
        assert len(ecus) == 1
        nodes = config.getTpNodes()
        assert len(nodes) == 1
        assert nodes[0].getShortName() == "Node1"

    def test_read_flexray_tp_config_empty(self, parser):
        element = _snip(
            """
                <SHORT-NAME>FlexrayTpConfig1</SHORT-NAME>
            """,
            root_tag="FLEXRAY-TP-CONFIG",
        )
        config = _config()
        parser.readFlexrayTpConfig(element, config)
        assert config.getPduPools() == []
        assert config.getTpAddresses() == []
        assert config.getTpConnections() == []
        assert config.getTpConnectionControls() == []
        assert config.getTpEcus() == []
        assert config.getTpNodes() == []
