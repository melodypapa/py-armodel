"""Tests for the readDoIpTpConfig handler (R23-11 DoIpTpConfig, Table 6.205, p.555)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import DoIpTpConfig
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
    """Fresh ARXMLParser instance running in strict mode."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLParser()


def _snip(inner: str, root_tag: str = "ROOT") -> ET.Element:
    """Wrap an inner XML fragment in a root element bound to the AUTOSAR NS."""
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


def _config() -> DoIpTpConfig:
    package = AUTOSAR.getInstance().createARPackage("TpConfigs")
    return DoIpTpConfig(package, "DoIpTpConfig1")


class TestReadDoIpTpConfig:
    """Tests for readDoIpTpConfig handler (R23-11 DoIpTpConfig, Table 6.205, p.555)."""

    def test_read_doip_tp_config_full(self, parser):
        element = _snip(
            """
                <SHORT-NAME>DoIpTpConfig1</SHORT-NAME>
                <DO-IP-LOGIC-ADDRESSS>
                    <DO-IP-LOGIC-ADDRESS>
                        <SHORT-NAME>LogicAddress1</SHORT-NAME>
                        <ADDRESS>2048</ADDRESS>
                    </DO-IP-LOGIC-ADDRESS>
                    <DO-IP-LOGIC-ADDRESS>
                        <SHORT-NAME>LogicAddress2</SHORT-NAME>
                        <ADDRESS>4096</ADDRESS>
                    </DO-IP-LOGIC-ADDRESS>
                </DO-IP-LOGIC-ADDRESSS>
                <TP-CONNECTIONS>
                    <DO-IP-TP-CONNECTION>
                        <SHORT-NAME>Connection1</SHORT-NAME>
                        <DO-IP-SOURCE-ADDRESS-REF DEST="DO-IP-LOGIC-ADDRESS">/DoIp/TpConfigs/DoIpTpConfig1/LogicAddress1</DO-IP-SOURCE-ADDRESS-REF>
                        <DO-IP-TARGET-ADDRESS-REF DEST="DO-IP-LOGIC-ADDRESS">/DoIp/TpConfigs/DoIpTpConfig1/LogicAddress2</DO-IP-TARGET-ADDRESS-REF>
                        <TP-SDU-REF DEST="PDU-TRIGGERING">/SoAd/PduTriggering1</TP-SDU-REF>
                    </DO-IP-TP-CONNECTION>
                </TP-CONNECTIONS>
            """,
            root_tag="DO-IP-TP-CONFIG",
        )
        config = _config()
        parser.readDoIpTpConfig(element, config)
        addresses = config.getDoIpLogicAddresses()
        assert len(addresses) == 2
        assert addresses[0].getShortName() == "LogicAddress1"
        assert addresses[0].getAddress().getValue() == 2048
        assert addresses[1].getShortName() == "LogicAddress2"
        assert addresses[1].getAddress().getValue() == 4096
        connections = config.getTpConnections()
        assert len(connections) == 1
        assert connections[0].getDoIpSourceAddressRef().getValue() == "/DoIp/TpConfigs/DoIpTpConfig1/LogicAddress1"
        assert connections[0].getDoIpSourceAddressRef().getDest() == "DO-IP-LOGIC-ADDRESS"
        assert connections[0].getDoIpTargetAddressRef().getValue() == "/DoIp/TpConfigs/DoIpTpConfig1/LogicAddress2"
        assert connections[0].getTpSduRef().getValue() == "/SoAd/PduTriggering1"

    def test_read_doip_tp_config_empty(self, parser):
        element = _snip(
            """
                <SHORT-NAME>DoIpTpConfig1</SHORT-NAME>
            """,
            root_tag="DO-IP-TP-CONFIG",
        )
        config = _config()
        parser.readDoIpTpConfig(element, config)
        assert config.getDoIpLogicAddresses() == []
        assert config.getTpConnections() == []
