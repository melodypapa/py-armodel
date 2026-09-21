"""Tests for the readDoIpConfig handler (R23-11 DoIpConfig, Table 6.202, p.551)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DoIP import DoIpConfig
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import EcuInstance
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


def _config() -> DoIpConfig:
    return DoIpConfig()


class TestReadDoIpConfig:
    """Tests for readDoIpConfig handler (R23-11 DoIpConfig, Table 6.202, p.551)."""

    def test_read_doip_config_full(self, parser):
        element = _snip(
            """
                <DOIP-INTERFACES>
                    <DO-IP-INTERFACE>
                        <SHORT-NAME>Interface1</SHORT-NAME>
                        <MAX-TESTER-CONNECTIONS>4</MAX-TESTER-CONNECTIONS>
                        <SOCKET-CONNECTION-REFS>
                            <SOCKET-CONNECTION-REF DEST="STATIC-SOCKET-CONNECTION">/Ethernet/StaticSocketConnection1</SOCKET-CONNECTION-REF>
                        </SOCKET-CONNECTION-REFS>
                    </DO-IP-INTERFACE>
                </DOIP-INTERFACES>
                <LOGIC-ADDRESS>
                    <SHORT-NAME>LogicAddress1</SHORT-NAME>
                    <ADDRESS>2048</ADDRESS>
                </LOGIC-ADDRESS>
            """,
            root_tag="DO-IP-CONFIG",
        )
        config = _config()
        parser.readDoIpConfig(element, config)
        interfaces = config.getDoIpInterfaces()
        assert len(interfaces) == 1
        assert interfaces[0].getShortName() == "Interface1"
        assert interfaces[0].getMaxTesterConnections().getValue() == 4
        socket_connection_refs = interfaces[0].getSocketConnectionRefs()
        assert len(socket_connection_refs) == 1
        assert socket_connection_refs[0].getValue() == "/Ethernet/StaticSocketConnection1"
        assert socket_connection_refs[0].getDest() == "STATIC-SOCKET-CONNECTION"
        assert config.getLogicAddress().getShortName() == "LogicAddress1"
        assert config.getLogicAddress().getAddress().getValue() == 2048

    def test_read_doip_config_empty(self, parser):
        element = _snip(
            """
            """,
            root_tag="DO-IP-CONFIG",
        )
        config = _config()
        parser.readDoIpConfig(element, config)
        assert config.getDoIpInterfaces() == []
        assert config.getLogicAddress() is None

    def test_read_ecu_instance_do_ip_config(self, parser):
        element = _snip(
            """
                <SHORT-NAME>ecu</SHORT-NAME>
                <DO-IP-CONFIG>
                    <DOIP-INTERFACES>
                        <DO-IP-INTERFACE>
                            <SHORT-NAME>Interface1</SHORT-NAME>
                            <MAX-TESTER-CONNECTIONS>4</MAX-TESTER-CONNECTIONS>
                        </DO-IP-INTERFACE>
                    </DOIP-INTERFACES>
                    <LOGIC-ADDRESS>
                        <SHORT-NAME>LogicAddress1</SHORT-NAME>
                        <ADDRESS>2048</ADDRESS>
                    </LOGIC-ADDRESS>
                </DO-IP-CONFIG>
            """,
            root_tag="ECU-INSTANCE",
        )
        instance = EcuInstance(parent=AUTOSAR.getInstance(), short_name="ecu")
        parser.readEcuInstance(element, instance)
        config = instance.getDoIpConfig()
        assert config is not None
        assert [interface.getShortName() for interface in config.getDoIpInterfaces()] == ["Interface1"]
        assert config.getDoIpInterfaces()[0].getMaxTesterConnections().getValue() == 4
        assert config.getLogicAddress().getShortName() == "LogicAddress1"
        assert config.getLogicAddress().getAddress().getValue() == 2048
