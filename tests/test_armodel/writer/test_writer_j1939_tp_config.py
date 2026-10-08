"""Tests for the writeJ1939TpConfig handler (R23-11 J1939TpConfig, Table 6.267, p.624)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Integer, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import J1939TpConfig, J1939TpConnection
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_CHILD_ORDER = [
    "TP-ADDRESSS",
    "TP-CONNECTIONS",
    "TP-NODES",
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


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLParser()


def _parent():
    return ET.Element("PARENT")


def _int(value):
    integer = Integer()
    integer.setValue(str(value))
    return integer


def _ref(value):
    ref = RefType()
    ref.setValue(value)
    return ref


def _fill_config(config: J1939TpConfig) -> J1939TpConfig:
    address = config.createTpAddress("TpAddress1")
    address.setTpAddress(_int(2047))
    connection = J1939TpConnection()
    connection.setBroadcast(Boolean().setValue(True))
    config.addTpConnection(connection)
    node = config.createJ1939TpNode("Node1")
    node.setTpAddressRef(_ref("/TpConfigs/J1939TpConfig1/TpAddress1"))
    return config


class TestWriteJ1939TpConfig:
    """Tests for writeJ1939TpConfig handler (R23-11 J1939TpConfig, Table 6.267, p.624)."""

    def test_children_in_xsd_order(self, writer):
        config = _fill_config(J1939TpConfig(AUTOSAR.getInstance().createARPackage("TpConfigs"), "J1939TpConfig1"))

        parent = _parent()
        writer.writeJ1939TpConfig(parent, config)
        child = parent.find("J-1939-TP-CONFIG")
        assert child is not None
        child_tags = [element.tag for element in child if element.tag != "SHORT-NAME"]
        assert child_tags == XSD_CHILD_ORDER
        assert len(child.findall("TP-ADDRESSS/TP-ADDRESS")) == 1
        assert len(child.findall("TP-CONNECTIONS/J-1939-TP-CONNECTION")) == 1
        assert len(child.findall("TP-NODES/J-1939-TP-NODE")) == 1

    def test_empty_config_writes_no_wrappers(self, writer):
        config = J1939TpConfig(AUTOSAR.getInstance().createARPackage("TpConfigs"), "J1939TpConfig1")

        parent = _parent()
        writer.writeJ1939TpConfig(parent, config)
        child = parent.find("J-1939-TP-CONFIG")
        assert child is not None
        child_tags = [element.tag for element in child if element.tag != "SHORT-NAME"]
        assert child_tags == []

    def test_round_trip(self, writer, parser):
        config = _fill_config(J1939TpConfig(AUTOSAR.getInstance().createARPackage("TpConfigs"), "J1939TpConfig1"))

        parent = _parent()
        writer.writeJ1939TpConfig(parent, config)
        element = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))[0]

        reloaded = J1939TpConfig(AUTOSAR.getInstance().createARPackage("TpConfigs"), "J1939TpConfig1")
        parser.readJ1939TpConfig(element, reloaded)
        addresses = reloaded.getTpAddresses()
        assert len(addresses) == 1
        assert addresses[0].getShortName() == "TpAddress1"
        assert addresses[0].getTpAddress() is not None
        assert addresses[0].getTpAddress().getValue() == 2047
        connections = reloaded.getTpConnections()
        assert len(connections) == 1
        assert isinstance(connections[0], J1939TpConnection)
        assert connections[0].getBroadcast() is not None
        assert connections[0].getBroadcast().getValue() is True
        nodes = reloaded.getTpNodes()
        assert len(nodes) == 1
        assert nodes[0].getShortName() == "Node1"
        assert nodes[0].getTpAddressRef() is not None
        assert nodes[0].getTpAddressRef().getValue() == "/TpConfigs/J1939TpConfig1/TpAddress1"
