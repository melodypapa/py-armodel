"""Tests for the writeIEEE1722TpConnection handler (R23-11 IEEE1722TpConnection, Table 6.275, p.637)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    MacAddressString,
    PositiveInteger,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp import IEEE1722TpConnection
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_CHILD_ORDER = [
    "SHORT-NAME",
    "DESTINATION-MAC-ADDRESS",
    "MAC-ADDRESS-STREAM-ID",
    "PDU-REF",
    "UNIQUE-STREAM-ID",
    "VERSION",
    "VLAN-PRIORITY",
]


class _Conn(IEEE1722TpConnection):
    pass


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


def _ref(value, dest):
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _mac(value):
    mac = MacAddressString()
    mac.setValue(value)
    return mac


def _pos_int(value):
    integer = PositiveInteger()
    integer.setValue(value)
    return integer


def _fill_connection(connection: IEEE1722TpConnection) -> IEEE1722TpConnection:
    connection.setDestinationMacAddress(_mac("02:00:00:00:00:01"))
    connection.setMacAddressStreamId(_mac("91:E0:F0:00:FE:00"))
    connection.setPduRef(_ref("/Pkgs/Pt1", "PDU-TRIGGERING"))
    connection.setUniqueStreamId(_pos_int(42))
    connection.setVersion(_pos_int(2))
    connection.setVlanPriority(_pos_int(5))
    return connection


class TestWriteIEEE1722TpConnection:
    """Tests for writeIEEE1722TpConnection handler (R23-11 IEEE1722TpConnection, Table 6.275, p.637)."""

    def test_children_in_xsd_order(self, writer):
        connection = _fill_connection(_Conn(None, "StreamConn"))

        parent = _parent()
        writer.writeIEEE1722TpConnection(parent, connection)
        child_tags = [element.tag for element in parent]
        assert child_tags == XSD_CHILD_ORDER

    def test_field_values_in_xml(self, writer):
        connection = _fill_connection(_Conn(None, "StreamConn"))

        parent = _parent()
        writer.writeIEEE1722TpConnection(parent, connection)
        assert parent.find("DESTINATION-MAC-ADDRESS").text == "02:00:00:00:00:01"
        assert parent.find("MAC-ADDRESS-STREAM-ID").text == "91:E0:F0:00:FE:00"
        assert parent.find("PDU-REF").text == "/Pkgs/Pt1"
        assert parent.find("PDU-REF").get("DEST") == "PDU-TRIGGERING"
        assert parent.find("UNIQUE-STREAM-ID").text == "42"
        assert parent.find("VERSION").text == "2"
        assert parent.find("VLAN-PRIORITY").text == "5"

    def test_empty_connection_writes_no_own_elements(self, writer):
        connection = _Conn(None, "StreamConn")

        parent = _parent()
        writer.writeIEEE1722TpConnection(parent, connection)
        assert [element.tag for element in parent] == ["SHORT-NAME"]

    def test_round_trip(self, writer, parser):
        connection = _fill_connection(_Conn(None, "StreamConn"))

        parent = _parent()
        writer.writeIEEE1722TpConnection(parent, connection)
        element = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        reloaded = _Conn(None, "StreamConn")
        parser.readIEEE1722TpConnection(element, reloaded)
        assert reloaded.getDestinationMacAddress().getValue() == "02:00:00:00:00:01"
        assert reloaded.getMacAddressStreamId().getValue() == "91:E0:F0:00:FE:00"
        assert reloaded.getPduRef().getValue() == "/Pkgs/Pt1"
        assert reloaded.getPduRef().getDest() == "PDU-TRIGGERING"
        assert reloaded.getUniqueStreamId().getValue() == 42
        assert reloaded.getVersion().getValue() == 2
        assert reloaded.getVlanPriority().getValue() == 5
