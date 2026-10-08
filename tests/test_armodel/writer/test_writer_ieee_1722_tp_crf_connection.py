"""Tests for the writeIEEE1722TpCrfConnection handler (R23-11 IEEE1722TpCrfConnection, Table 6.277, p.640)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    RefType,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAv import (
    IEEE1722TpCrfConnection,
    IEEE1722TpCrfPullEnum,
    IEEE1722TpCrfTypeEnum,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_CHILD_ORDER = [
    "SHORT-NAME",
    "MAX-TRANSIT-TIME",
    "SDU-REFS",
    "BASE-FREQUENCY",
    "CRF-PULL",
    "CRF-TYPE",
    "FRAME-SYNC-ENABLED",
    "TIMESTAMP-INTERVAL",
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


def _fill_connection(connection: IEEE1722TpCrfConnection) -> IEEE1722TpCrfConnection:
    connection.setMaxTransitTime(_time(0.002))
    connection.addSduRef(_ref("/Pkgs/Pt1", "PDU-TRIGGERING"))
    connection.setBaseFrequency(_pos_int(8000))
    crf_pull = IEEE1722TpCrfPullEnum()
    crf_pull.setValue(IEEE1722TpCrfPullEnum.ENUM_1_0)
    connection.setCrfPull(crf_pull)
    crf_type = IEEE1722TpCrfTypeEnum()
    crf_type.setValue(IEEE1722TpCrfTypeEnum.ENUM_VIDEO_FRAME)
    connection.setCrfType(crf_type)
    frame_sync = Boolean()
    frame_sync.setValue(True)
    connection.setFrameSyncEnabled(frame_sync)
    connection.setTimestampInterval(_pos_int(4))
    return connection


def _time(value):
    t = TimeValue()
    t.setValue(value)
    return t


class TestWriteIEEE1722TpCrfConnection:
    """Tests for writeIEEE1722TpCrfConnection handler (R23-11 IEEE1722TpCrfConnection, Table 6.277, p.640)."""

    def test_children_in_xsd_order(self, writer):
        connection = _fill_connection(IEEE1722TpCrfConnection(None, "CrfStream"))

        parent = _parent()
        writer.writeIEEE1722TpCrfConnection(parent, connection)
        child = parent.find("IEEE-1722-TP-CRF-CONNECTION")
        assert child is not None
        child_tags = [element.tag for element in child]
        assert child_tags == XSD_CHILD_ORDER

    def test_field_values_in_xml(self, writer):
        connection = _fill_connection(IEEE1722TpCrfConnection(None, "CrfStream"))

        parent = _parent()
        writer.writeIEEE1722TpCrfConnection(parent, connection)
        child = parent.find("IEEE-1722-TP-CRF-CONNECTION")
        assert child.find("BASE-FREQUENCY").text == "8000"
        assert child.find("CRF-PULL").text == "1-0"
        assert child.find("CRF-TYPE").text == "VIDEO-FRAME"
        assert child.find("FRAME-SYNC-ENABLED").text == "true"
        assert child.find("TIMESTAMP-INTERVAL").text == "4"

    def test_empty_connection_writes_only_identifiable(self, writer):
        connection = IEEE1722TpCrfConnection(None, "CrfStream")

        parent = _parent()
        writer.writeIEEE1722TpCrfConnection(parent, connection)
        child = parent.find("IEEE-1722-TP-CRF-CONNECTION")
        assert child is not None
        assert [element.tag for element in child] == ["SHORT-NAME"]

    def test_round_trip(self, writer, parser):
        connection = _fill_connection(IEEE1722TpCrfConnection(None, "CrfStream"))

        parent = _parent()
        writer.writeIEEE1722TpCrfConnection(parent, connection)
        element = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))[0]

        reloaded = IEEE1722TpCrfConnection(None, "CrfStream")
        parser.readIEEE1722TpCrfConnection(element, reloaded)
        assert reloaded.getMaxTransitTime().getValue() == 0.002
        assert reloaded.getSduRefs()[0].getValue() == "/Pkgs/Pt1"
        assert reloaded.getBaseFrequency().getValue() == 8000
        assert reloaded.getCrfPull().getValue() == IEEE1722TpCrfPullEnum.ENUM_1_0
        assert reloaded.getCrfType().getValue() == IEEE1722TpCrfTypeEnum.ENUM_VIDEO_FRAME
        assert reloaded.getFrameSyncEnabled().getValue() is True
        assert reloaded.getTimestampInterval().getValue() == 4
