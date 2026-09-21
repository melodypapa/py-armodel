"""Tests for the writeDoIpInterface handler (R23-11 DoIpInterface, Table 6.203, p.552)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger, RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DoIP import DoIpInterface
from armodel.writer.arxml_writer import ARXMLWriter

XSD_CHILD_ORDER = [
    "ALIVE-CHECK-RESPONSE-TIMEOUT",
    "DO-IP-ROUTING-ACTIVATIONS",
    "DOIP-CHANNEL-COLLECTION-REF",
    "DOIP-CONNECTION-REFS",
    "GENERAL-INACTIVITY-TIME",
    "INITIAL-INACTIVITY-TIME",
    "INITIAL-VEHICLE-ANNOUNCEMENT-TIME",
    "IS-ACTIVATION-LINE-DEPENDENT",
    "MAX-TESTER-CONNECTIONS",
    "SOCKET-CONNECTION-REFS",
    "USE-MAC-ADDRESS-FOR-IDENTIFICATION",
    "USE-VEHICLE-IDENTIFICATION-SYNC-STATUS",
    "VEHICLE-ANNOUNCEMENT-COUNT",
    "VEHICLE-ANNOUNCEMENT-INTERVAL",
]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLWriter()


def _parent():
    return ET.Element("PARENT")


def _ref(value, dest=None):
    ref = RefType()
    ref.setValue(value)
    if dest is not None:
        ref.setDest(dest)
    return ref


def _time(value):
    time_value = TimeValue()
    time_value.setValue(value)
    return time_value


def _positive_integer(value):
    integer = PositiveInteger()
    integer.setValue(value)
    return integer


def _boolean(value):
    boolean = Boolean()
    boolean.setValue(value)
    return boolean


def _interface(short_name: str) -> DoIpInterface:
    parent = AUTOSAR.getInstance().createARPackage("DoIpInterfacePkg")
    return DoIpInterface(parent, short_name)


class TestWriteDoIpInterface:
    """Tests for writeDoIpInterface handler (R23-11 DoIpInterface, Table 6.203, p.552)."""

    def test_children_in_xsd_order(self, writer):
        interface = _interface("Interface1")
        interface.setAliveCheckResponseTimeout(_time("60.0"))
        activation = interface.createDoIpRoutingActivation("RoutingActivation1")
        activation.addDoIpTargetAddressRef(_ref("/DoIp/TargetAddress1", "DO-IP-LOGIC-TARGET-ADDRESS-PROPS"))
        interface.setDoipChannelCollectionRef(_ref("/DoIp/TpConfigs/DoIpTpConfig1", "DO-IP-TP-CONFIG"))
        interface.addDoipConnectionRef(_ref("/Ethernet/SocketConnectionBundle1", "SOCKET-CONNECTION-BUNDLE"))
        interface.addDoipConnectionRef(_ref("/Ethernet/SocketConnectionBundle2", "SOCKET-CONNECTION-BUNDLE"))
        interface.setGeneralInactivityTime(_time("50.0"))
        interface.setInitialInactivityTime(_time("1.0"))
        interface.setInitialVehicleAnnouncementTime(_time("0.5"))
        interface.setIsActivationLineDependent(_boolean("true"))
        interface.setMaxTesterConnections(_positive_integer("4"))
        interface.addSocketConnectionRef(_ref("/Ethernet/StaticSocketConnection1", "STATIC-SOCKET-CONNECTION"))
        interface.addSocketConnectionRef(_ref("/Ethernet/StaticSocketConnection2", "STATIC-SOCKET-CONNECTION"))
        interface.setUseMacAddressForIdentification(_boolean("false"))
        interface.setUseVehicleIdentificationSyncStatus(_boolean("true"))
        interface.setVehicleAnnouncementCount(_positive_integer("3"))
        interface.setVehicleAnnouncementInterval(_time("2.0"))

        parent = _parent()
        writer.writeDoIpInterface(parent, interface)
        child = parent.find("DO-IP-INTERFACE")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Interface1"
        child_tags = [element.tag for element in child if element.tag != "SHORT-NAME"]
        assert child_tags == XSD_CHILD_ORDER
        assert child.find("ALIVE-CHECK-RESPONSE-TIMEOUT").text == "60.0"
        activations_wrapper = child.find("DO-IP-ROUTING-ACTIVATIONS")
        activation_tags = activations_wrapper.findall("DO-IP-ROUTING-ACTIVATION")
        assert len(activation_tags) == 1
        assert activation_tags[0].find("SHORT-NAME").text == "RoutingActivation1"
        target_refs = activation_tags[0].findall("DO-IP-TARGET-ADDRESS-REFS/DO-IP-TARGET-ADDRESS-REF")
        assert len(target_refs) == 1
        assert target_refs[0].text == "/DoIp/TargetAddress1"
        assert target_refs[0].get("DEST") == "DO-IP-LOGIC-TARGET-ADDRESS-PROPS"
        channel_ref = child.find("DOIP-CHANNEL-COLLECTION-REF")
        assert channel_ref.text == "/DoIp/TpConfigs/DoIpTpConfig1"
        assert channel_ref.get("DEST") == "DO-IP-TP-CONFIG"
        doip_connection_refs = child.findall("DOIP-CONNECTION-REFS/DOIP-CONNECTION-REF")
        assert len(doip_connection_refs) == 2
        assert doip_connection_refs[0].text == "/Ethernet/SocketConnectionBundle1"
        assert doip_connection_refs[0].get("DEST") == "SOCKET-CONNECTION-BUNDLE"
        assert doip_connection_refs[1].text == "/Ethernet/SocketConnectionBundle2"
        assert child.find("GENERAL-INACTIVITY-TIME").text == "50.0"
        assert child.find("INITIAL-INACTIVITY-TIME").text == "1.0"
        assert child.find("INITIAL-VEHICLE-ANNOUNCEMENT-TIME").text == "0.5"
        assert child.find("IS-ACTIVATION-LINE-DEPENDENT").text == "true"
        assert child.find("MAX-TESTER-CONNECTIONS").text == "4"
        socket_connection_refs = child.findall("SOCKET-CONNECTION-REFS/SOCKET-CONNECTION-REF")
        assert len(socket_connection_refs) == 2
        assert socket_connection_refs[0].text == "/Ethernet/StaticSocketConnection1"
        assert socket_connection_refs[0].get("DEST") == "STATIC-SOCKET-CONNECTION"
        assert socket_connection_refs[1].text == "/Ethernet/StaticSocketConnection2"
        assert child.find("USE-MAC-ADDRESS-FOR-IDENTIFICATION").text == "false"
        assert child.find("USE-VEHICLE-IDENTIFICATION-SYNC-STATUS").text == "true"
        assert child.find("VEHICLE-ANNOUNCEMENT-COUNT").text == "3"
        assert child.find("VEHICLE-ANNOUNCEMENT-INTERVAL").text == "2.0"

    def test_empty_children_omitted(self, writer):
        interface = _interface("Interface1")
        parent = _parent()
        writer.writeDoIpInterface(parent, interface)
        child = parent.find("DO-IP-INTERFACE")
        assert child is not None
        for tag in XSD_CHILD_ORDER:
            assert child.find(tag) is None
