"""Tests for the writeIEEE1722TpIidcConnection handler (R23-11 IEEE1722TpIidcConnection, Table 6.284, p.648)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    RefType,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp import (
    IEEE1722TpIidcConnection,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_CHILD_ORDER = [
    "SHORT-NAME",
    "MAX-TRANSIT-TIME",
    "SDU-REFS",
    "IIDC-CHANNEL",
    "IIDC-DATA-BLOCK-SIZE",
    "IIDC-FRACTION-NUMBER",
    "IIDC-SOURCE-PACKET-HEADER",
    "IIDC-STREAM-FORMAT",
    "IIDC-SY",
    "IIDC-T-CODE",
    "IIDC-TAG",
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


def _ref(value, dest):
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _pos_int(value):
    integer = PositiveInteger()
    integer.setValue(value)
    return integer


def _time(value):
    t = TimeValue()
    t.setValue(value)
    return t


def _fill_connection(connection: IEEE1722TpIidcConnection) -> IEEE1722TpIidcConnection:
    connection.setMaxTransitTime(_time(0.002))
    connection.addSduRef(_ref("/Pkgs/Pt1", "PDU-TRIGGERING"))
    connection.setIidcChannel(_pos_int(1))
    connection.setIidcDataBlockSize(_pos_int(128))
    connection.setIidcFractionNumber(_pos_int(2))
    source_packet_header = Boolean()
    source_packet_header.setValue(True)
    connection.setIidcSourcePacketHeader(source_packet_header)
    connection.setIidcStreamFormat(_pos_int(0))
    connection.setIidcSy(_pos_int(255))
    connection.setIidcTCode(_pos_int(16))
    connection.setIidcTag(_pos_int(8))
    return connection


class TestWriteIEEE1722TpIidcConnection:
    """Tests for writeIEEE1722TpIidcConnection handler (R23-11 IEEE1722TpIidcConnection, Table 6.284, p.648)."""

    def test_children_in_xsd_order(self, writer):
        connection = _fill_connection(IEEE1722TpIidcConnection(None, "IidcStream"))

        parent = _parent()
        writer.writeIEEE1722TpIidcConnection(parent, connection)
        child = parent.find("IEEE-1722-TP-IIDC-CONNECTION")
        assert child is not None
        child_tags = [element.tag for element in child]
        assert child_tags == XSD_CHILD_ORDER

    def test_field_values_in_xml(self, writer):
        connection = _fill_connection(IEEE1722TpIidcConnection(None, "IidcStream"))

        parent = _parent()
        writer.writeIEEE1722TpIidcConnection(parent, connection)
        child = parent.find("IEEE-1722-TP-IIDC-CONNECTION")
        assert child.find("IIDC-CHANNEL").text == "1"
        assert child.find("IIDC-DATA-BLOCK-SIZE").text == "128"
        assert child.find("IIDC-FRACTION-NUMBER").text == "2"
        assert child.find("IIDC-SOURCE-PACKET-HEADER").text == "true"
        assert child.find("IIDC-STREAM-FORMAT").text == "0"
        assert child.find("IIDC-SY").text == "255"
        assert child.find("IIDC-T-CODE").text == "16"
        assert child.find("IIDC-TAG").text == "8"

    def test_empty_connection_writes_only_identifiable(self, writer):
        connection = IEEE1722TpIidcConnection(None, "IidcStream")

        parent = _parent()
        writer.writeIEEE1722TpIidcConnection(parent, connection)
        child = parent.find("IEEE-1722-TP-IIDC-CONNECTION")
        assert child is not None
        assert [element.tag for element in child] == ["SHORT-NAME"]

    def test_round_trip(self, writer, parser):
        connection = _fill_connection(IEEE1722TpIidcConnection(None, "IidcStream"))

        parent = _parent()
        writer.writeIEEE1722TpIidcConnection(parent, connection)
        element = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))[0]

        reloaded = IEEE1722TpIidcConnection(None, "IidcStream")
        parser.readIEEE1722TpIidcConnection(element, reloaded)
        assert reloaded.getMaxTransitTime().getValue() == 0.002
        assert reloaded.getSduRefs()[0].getValue() == "/Pkgs/Pt1"
        assert reloaded.getIidcChannel().getValue() == 1
        assert reloaded.getIidcDataBlockSize().getValue() == 128
        assert reloaded.getIidcFractionNumber().getValue() == 2
        assert reloaded.getIidcSourcePacketHeader().getValue() is True
        assert reloaded.getIidcStreamFormat().getValue() == 0
        assert reloaded.getIidcSy().getValue() == 255
        assert reloaded.getIidcTCode().getValue() == 16
        assert reloaded.getIidcTag().getValue() == 8
