"""Tests for the readDoIpInterface handler (R23-11 DoIpInterface, Table 6.203, p.552)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DoIP import DoIpInterface
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


def _interface(short_name: str) -> DoIpInterface:
    parent = AUTOSAR.getInstance().createARPackage("DoIpInterfacePkg")
    return DoIpInterface(parent, short_name)


class TestReadDoIpInterface:
    """Tests for readDoIpInterface handler (R23-11 DoIpInterface, Table 6.203, p.552)."""

    def test_read_doip_interface_full(self, parser):
        element = _snip(
            """
                <SHORT-NAME>Interface1</SHORT-NAME>
                <ALIVE-CHECK-RESPONSE-TIMEOUT>60.0</ALIVE-CHECK-RESPONSE-TIMEOUT>
                <DO-IP-ROUTING-ACTIVATIONS>
                    <DO-IP-ROUTING-ACTIVATION>
                        <SHORT-NAME>RoutingActivation1</SHORT-NAME>
                        <DO-IP-TARGET-ADDRESS-REFS>
                            <DO-IP-TARGET-ADDRESS-REF DEST="DO-IP-LOGIC-TARGET-ADDRESS-PROPS">/DoIp/TargetAddress1</DO-IP-TARGET-ADDRESS-REF>
                        </DO-IP-TARGET-ADDRESS-REFS>
                    </DO-IP-ROUTING-ACTIVATION>
                </DO-IP-ROUTING-ACTIVATIONS>
                <DOIP-CHANNEL-COLLECTION-REF DEST="DO-IP-TP-CONFIG">/DoIp/TpConfigs/DoIpTpConfig1</DOIP-CHANNEL-COLLECTION-REF>
                <DOIP-CONNECTION-REFS>
                    <DOIP-CONNECTION-REF DEST="SOCKET-CONNECTION-BUNDLE">/Ethernet/SocketConnectionBundle1</DOIP-CONNECTION-REF>
                    <DOIP-CONNECTION-REF DEST="SOCKET-CONNECTION-BUNDLE">/Ethernet/SocketConnectionBundle2</DOIP-CONNECTION-REF>
                </DOIP-CONNECTION-REFS>
                <GENERAL-INACTIVITY-TIME>50.0</GENERAL-INACTIVITY-TIME>
                <INITIAL-INACTIVITY-TIME>1.0</INITIAL-INACTIVITY-TIME>
                <INITIAL-VEHICLE-ANNOUNCEMENT-TIME>0.5</INITIAL-VEHICLE-ANNOUNCEMENT-TIME>
                <IS-ACTIVATION-LINE-DEPENDENT>true</IS-ACTIVATION-LINE-DEPENDENT>
                <MAX-TESTER-CONNECTIONS>4</MAX-TESTER-CONNECTIONS>
                <SOCKET-CONNECTION-REFS>
                    <SOCKET-CONNECTION-REF DEST="STATIC-SOCKET-CONNECTION">/Ethernet/StaticSocketConnection1</SOCKET-CONNECTION-REF>
                    <SOCKET-CONNECTION-REF DEST="STATIC-SOCKET-CONNECTION">/Ethernet/StaticSocketConnection2</SOCKET-CONNECTION-REF>
                </SOCKET-CONNECTION-REFS>
                <USE-MAC-ADDRESS-FOR-IDENTIFICATION>false</USE-MAC-ADDRESS-FOR-IDENTIFICATION>
                <USE-VEHICLE-IDENTIFICATION-SYNC-STATUS>true</USE-VEHICLE-IDENTIFICATION-SYNC-STATUS>
                <VEHICLE-ANNOUNCEMENT-COUNT>3</VEHICLE-ANNOUNCEMENT-COUNT>
                <VEHICLE-ANNOUNCEMENT-INTERVAL>2.0</VEHICLE-ANNOUNCEMENT-INTERVAL>
            """,
            root_tag="DO-IP-INTERFACE",
        )
        interface = _interface("Interface1")
        parser.readDoIpInterface(element, interface)
        assert interface.getAliveCheckResponseTimeout().getValue() == 60.0
        activations = interface.getDoIpRoutingActivations()
        assert len(activations) == 1
        assert activations[0].getShortName() == "RoutingActivation1"
        assert [ref.getValue() for ref in activations[0].getDoIpTargetAddressRefs()] == ["/DoIp/TargetAddress1"]
        assert interface.getDoipChannelCollectionRef().getValue() == "/DoIp/TpConfigs/DoIpTpConfig1"
        assert interface.getDoipChannelCollectionRef().getDest() == "DO-IP-TP-CONFIG"
        doip_connection_refs = interface.getDoipConnectionRefs()
        assert len(doip_connection_refs) == 2
        assert doip_connection_refs[0].getValue() == "/Ethernet/SocketConnectionBundle1"
        assert doip_connection_refs[0].getDest() == "SOCKET-CONNECTION-BUNDLE"
        assert doip_connection_refs[1].getValue() == "/Ethernet/SocketConnectionBundle2"
        assert interface.getGeneralInactivityTime().getValue() == 50.0
        assert interface.getInitialInactivityTime().getValue() == 1.0
        assert interface.getInitialVehicleAnnouncementTime().getValue() == 0.5
        assert interface.getIsActivationLineDependent().getValue() is True
        assert interface.getMaxTesterConnections().getValue() == 4
        socket_connection_refs = interface.getSocketConnectionRefs()
        assert len(socket_connection_refs) == 2
        assert socket_connection_refs[0].getValue() == "/Ethernet/StaticSocketConnection1"
        assert socket_connection_refs[0].getDest() == "STATIC-SOCKET-CONNECTION"
        assert socket_connection_refs[1].getValue() == "/Ethernet/StaticSocketConnection2"
        assert interface.getUseMacAddressForIdentification().getValue() is False
        assert interface.getUseVehicleIdentificationSyncStatus().getValue() is True
        assert interface.getVehicleAnnouncementCount().getValue() == 3
        assert interface.getVehicleAnnouncementInterval().getValue() == 2.0

    def test_read_doip_interface_empty(self, parser):
        element = _snip(
            """
                <SHORT-NAME>Interface1</SHORT-NAME>
            """,
            root_tag="DO-IP-INTERFACE",
        )
        interface = _interface("Interface1")
        parser.readDoIpInterface(element, interface)
        assert interface.getAliveCheckResponseTimeout() is None
        assert interface.getDoIpRoutingActivations() == []
        assert interface.getDoipChannelCollectionRef() is None
        assert interface.getDoipConnectionRefs() == []
        assert interface.getGeneralInactivityTime() is None
        assert interface.getInitialInactivityTime() is None
        assert interface.getInitialVehicleAnnouncementTime() is None
        assert interface.getIsActivationLineDependent() is None
        assert interface.getMaxTesterConnections() is None
        assert interface.getSocketConnectionRefs() == []
        assert interface.getUseMacAddressForIdentification() is None
        assert interface.getUseVehicleIdentificationSyncStatus() is None
        assert interface.getVehicleAnnouncementCount() is None
        assert interface.getVehicleAnnouncementInterval() is None
