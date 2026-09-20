"""Tests for the writeDoIpConfig handler (R23-11 DoIpConfig, Table 6.202, p.551)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DoIP import DoIpConfig
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import EcuInstance
from armodel.writer.arxml_writer import ARXMLWriter

XSD_CHILD_ORDER = [
    "DOIP-INTERFACES",
    "LOGIC-ADDRESS",
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


def _positive_integer(value):
    integer = PositiveInteger()
    integer.setValue(value)
    return integer


def _fill_config(config):
    interface = config.createDoIpInterface("Interface1")
    interface.setMaxTesterConnections(_positive_integer("4"))
    interface.addSocketConnectionRef(_ref("/Ethernet/StaticSocketConnection1", "STATIC-SOCKET-CONNECTION"))
    address = config.createLogicAddress("LogicAddress1")
    address.setAddress(_positive_integer("2048"))
    return config


class TestWriteDoIpConfig:
    """Tests for writeDoIpConfig handler (R23-11 DoIpConfig, Table 6.202, p.551)."""

    def test_children_in_xsd_order(self, writer):
        config = _fill_config(DoIpConfig())

        parent = _parent()
        writer.writeDoIpConfig(parent, config)
        child = parent.find("DO-IP-CONFIG")
        assert child is not None
        child_tags = [element.tag for element in child]
        assert child_tags == XSD_CHILD_ORDER
        interfaces_wrapper = child.find("DOIP-INTERFACES")
        interface_tags = interfaces_wrapper.findall("DO-IP-INTERFACE")
        assert len(interface_tags) == 1
        assert interface_tags[0].find("SHORT-NAME").text == "Interface1"
        assert interface_tags[0].find("MAX-TESTER-CONNECTIONS").text == "4"
        socket_connection_refs = interface_tags[0].findall("SOCKET-CONNECTION-REFS/SOCKET-CONNECTION-REF")
        assert len(socket_connection_refs) == 1
        assert socket_connection_refs[0].text == "/Ethernet/StaticSocketConnection1"
        assert socket_connection_refs[0].get("DEST") == "STATIC-SOCKET-CONNECTION"
        logic_address = child.find("LOGIC-ADDRESS")
        assert logic_address.find("SHORT-NAME").text == "LogicAddress1"
        assert logic_address.find("ADDRESS").text == "2048"

    def test_empty_children_omitted(self, writer):
        config = DoIpConfig()
        parent = _parent()
        writer.writeDoIpConfig(parent, config)
        child = parent.find("DO-IP-CONFIG")
        assert child is not None
        for tag in XSD_CHILD_ORDER:
            assert child.find(tag) is None

    def test_write_ecu_instance_do_ip_config(self, writer):
        instance = EcuInstance(parent=AUTOSAR.getInstance(), short_name="ecu")
        instance.setDoIpConfig(_fill_config(DoIpConfig()))

        parent = _parent()
        writer.writeEcuInstance(parent, instance)
        ecu = parent.find("ECU-INSTANCE")
        assert ecu is not None
        config_element = ecu.find("DO-IP-CONFIG")
        assert config_element is not None
        child_tags = [element.tag for element in config_element]
        assert child_tags == XSD_CHILD_ORDER
        interface_tags = config_element.findall("DOIP-INTERFACES/DO-IP-INTERFACE")
        assert len(interface_tags) == 1
        assert interface_tags[0].find("SHORT-NAME").text == "Interface1"
        assert interface_tags[0].find("MAX-TESTER-CONNECTIONS").text == "4"
        logic_address = config_element.find("LOGIC-ADDRESS")
        assert logic_address.find("SHORT-NAME").text == "LogicAddress1"
        assert logic_address.find("ADDRESS").text == "2048"

    def test_write_ecu_instance_without_do_ip_config_omits_element(self, writer):
        instance = EcuInstance(parent=AUTOSAR.getInstance(), short_name="ecu")
        parent = _parent()
        writer.writeEcuInstance(parent, instance)
        ecu = parent.find("ECU-INSTANCE")
        assert ecu.find("DO-IP-CONFIG") is None
