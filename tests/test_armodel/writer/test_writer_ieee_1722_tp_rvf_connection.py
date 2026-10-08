"""Tests for the writeIEEE1722TpRvfConnection handler (R23-11 IEEE1722TpRvfConnection, Table 6.285, p.650)."""

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
    IEEE1722TpRvfConnection,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAv import (
    IEEE1722TpRvfColorSpaceEnum,
    IEEE1722TpRvfFrameRateEnum,
    IEEE1722TpRvfPixelDepthEnum,
    IEEE1722TpRvfPixelFormatEnum,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_CHILD_ORDER = [
    "SHORT-NAME",
    "MAX-TRANSIT-TIME",
    "SDU-REFS",
    "RVF-ACTIVE-PIXELS",
    "RVF-COLOR-SPACE",
    "RVF-EVENT-DEFAULT",
    "RVF-FRAME-RATE",
    "RVF-INTERLACED",
    "RVF-PIXEL-DEPTH",
    "RVF-PIXEL-FORMAT",
    "RVF-TOTAL-LINES",
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


def _enum(enum_class, member):
    enum = enum_class()
    enum.setValue(member)
    return enum


def _fill_connection(connection: IEEE1722TpRvfConnection) -> IEEE1722TpRvfConnection:
    connection.setMaxTransitTime(_time(0.002))
    connection.addSduRef(_ref("/Pkgs/Pt1", "PDU-TRIGGERING"))
    connection.setRvfActivePixels(_pos_int(1920))
    connection.setRvfColorSpace(_enum(IEEE1722TpRvfColorSpaceEnum, IEEE1722TpRvfColorSpaceEnum.ENUM_YCBCR))
    connection.setRvfEventDefault(_pos_int(8))
    connection.setRvfFrameRate(_enum(IEEE1722TpRvfFrameRateEnum, IEEE1722TpRvfFrameRateEnum.ENUM_60))
    interlaced = Boolean()
    interlaced.setValue(True)
    connection.setRvfInterlaced(interlaced)
    connection.setRvfPixelDepth(_enum(IEEE1722TpRvfPixelDepthEnum, IEEE1722TpRvfPixelDepthEnum.ENUM_10))
    connection.setRvfPixelFormat(_enum(IEEE1722TpRvfPixelFormatEnum, IEEE1722TpRvfPixelFormatEnum.ENUM_4_2_0))
    connection.setRvfTotalLines(_pos_int(1080))
    return connection


class TestWriteIEEE1722TpRvfConnection:
    """Tests for writeIEEE1722TpRvfConnection handler (R23-11 IEEE1722TpRvfConnection, Table 6.285, p.650)."""

    def test_children_in_xsd_order(self, writer):
        connection = _fill_connection(IEEE1722TpRvfConnection(None, "RvfStream"))

        parent = _parent()
        writer.writeIEEE1722TpRvfConnection(parent, connection)
        child = parent.find("IEEE-1722-TP-RVF-CONNECTION")
        assert child is not None
        child_tags = [element.tag for element in child]
        assert child_tags == XSD_CHILD_ORDER

    def test_field_values_in_xml(self, writer):
        connection = _fill_connection(IEEE1722TpRvfConnection(None, "RvfStream"))

        parent = _parent()
        writer.writeIEEE1722TpRvfConnection(parent, connection)
        child = parent.find("IEEE-1722-TP-RVF-CONNECTION")
        assert child.find("RVF-ACTIVE-PIXELS").text == "1920"
        assert child.find("RVF-COLOR-SPACE").text == "YCBCR"
        assert child.find("RVF-EVENT-DEFAULT").text == "8"
        assert child.find("RVF-FRAME-RATE").text == "60"
        assert child.find("RVF-INTERLACED").text == "true"
        assert child.find("RVF-PIXEL-DEPTH").text == "10"
        assert child.find("RVF-PIXEL-FORMAT").text == "4-2-0"
        assert child.find("RVF-TOTAL-LINES").text == "1080"

    def test_empty_connection_writes_only_identifiable(self, writer):
        connection = IEEE1722TpRvfConnection(None, "RvfStream")

        parent = _parent()
        writer.writeIEEE1722TpRvfConnection(parent, connection)
        child = parent.find("IEEE-1722-TP-RVF-CONNECTION")
        assert child is not None
        assert [element.tag for element in child] == ["SHORT-NAME"]

    def test_round_trip(self, writer, parser):
        connection = _fill_connection(IEEE1722TpRvfConnection(None, "RvfStream"))

        parent = _parent()
        writer.writeIEEE1722TpRvfConnection(parent, connection)
        element = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))[0]

        reloaded = IEEE1722TpRvfConnection(None, "RvfStream")
        parser.readIEEE1722TpRvfConnection(element, reloaded)
        assert reloaded.getMaxTransitTime().getValue() == 0.002
        assert reloaded.getSduRefs()[0].getValue() == "/Pkgs/Pt1"
        assert reloaded.getRvfActivePixels().getValue() == 1920
        assert reloaded.getRvfColorSpace().getValue() == "YCBCR"
        assert reloaded.getRvfEventDefault().getValue() == 8
        assert reloaded.getRvfFrameRate().getValue() == "60"
        assert reloaded.getRvfInterlaced().getValue() is True
        assert reloaded.getRvfPixelDepth().getValue() == "10"
        assert reloaded.getRvfPixelFormat().getValue() == "4-2-0"
        assert reloaded.getRvfTotalLines().getValue() == 1080
