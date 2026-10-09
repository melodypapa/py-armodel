"""Tests for the writeIEEE1722TpAafConnection handler (R23-11 IEEE1722TpAafConnection, Table 6.280, p.643)."""

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
    IEEE1722TpAafAes3DataTypeEnum,
    IEEE1722TpAafConnection,
    IEEE1722TpAafFormatEnum,
    IEEE1722TpAafNominalRateEnum,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_CHILD_ORDER = [
    "SHORT-NAME",
    "MAX-TRANSIT-TIME",
    "SDU-REFS",
    "AAF-AES-3-DATA-TYPE",
    "AAF-FORMAT",
    "AAF-NOMINAL-RATE",
    "AES-3-DATA-TYPE-H",
    "AES-3-DATA-TYPE-L",
    "CHANNELS-PER-FRAME",
    "EVENT-DEFAULT-VALUE",
    "PCM-BIT-DEPTH",
    "SPARSE-TIMESTAMP-ENABLED",
    "STREAMS-PER-FRAME",
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


def _fill_connection(connection: IEEE1722TpAafConnection) -> IEEE1722TpAafConnection:
    connection.setMaxTransitTime(_time(0.002))
    connection.addSduRef(_ref("/Pkgs/Pt1", "PDU-TRIGGERING"))
    aes3_data_type = IEEE1722TpAafAes3DataTypeEnum()
    aes3_data_type.setValue(IEEE1722TpAafAes3DataTypeEnum.ENUM_PCM)
    connection.setAafAes3DataType(aes3_data_type)
    aaf_format = IEEE1722TpAafFormatEnum()
    aaf_format.setValue(IEEE1722TpAafFormatEnum.AES3_32BIT)
    connection.setAafFormat(aaf_format)
    nominal_rate = IEEE1722TpAafNominalRateEnum()
    nominal_rate.setValue(IEEE1722TpAafNominalRateEnum.ENUM_48KHZ)
    connection.setAafNominalRate(nominal_rate)
    connection.setAes3DataTypeH(_pos_int(2))
    connection.setAes3DataTypeL(_pos_int(1))
    connection.setChannelsPerFrame(_pos_int(2))
    connection.setEventDefaultValue(_pos_int(0))
    connection.setPcmBitDepth(_pos_int(24))
    sparse = Boolean()
    sparse.setValue(True)
    connection.setSparseTimestampEnabled(sparse)
    connection.setStreamsPerFrame(_pos_int(4))
    return connection


class TestWriteIEEE1722TpAafConnection:
    """Tests for writeIEEE1722TpAafConnection handler (R23-11 IEEE1722TpAafConnection, Table 6.280, p.643)."""

    def test_children_in_xsd_order(self, writer):
        connection = _fill_connection(IEEE1722TpAafConnection(None, "AafStream"))

        parent = _parent()
        writer.writeIEEE1722TpAafConnection(parent, connection)
        child = parent.find("IEEE-1722-TP-AAF-CONNECTION")
        assert child is not None
        child_tags = [element.tag for element in child]
        assert child_tags == XSD_CHILD_ORDER

    def test_field_values_in_xml(self, writer):
        connection = _fill_connection(IEEE1722TpAafConnection(None, "AafStream"))

        parent = _parent()
        writer.writeIEEE1722TpAafConnection(parent, connection)
        child = parent.find("IEEE-1722-TP-AAF-CONNECTION")
        assert child.find("AAF-AES-3-DATA-TYPE").text == "PCM"
        assert child.find("AAF-FORMAT").text == "AES-3-32-BIT"
        assert child.find("AAF-NOMINAL-RATE").text == "48-KHZ"
        assert child.find("AES-3-DATA-TYPE-H").text == "2"
        assert child.find("AES-3-DATA-TYPE-L").text == "1"
        assert child.find("CHANNELS-PER-FRAME").text == "2"
        assert child.find("EVENT-DEFAULT-VALUE").text == "0"
        assert child.find("PCM-BIT-DEPTH").text == "24"
        assert child.find("SPARSE-TIMESTAMP-ENABLED").text == "true"
        assert child.find("STREAMS-PER-FRAME").text == "4"

    def test_empty_connection_writes_only_identifiable(self, writer):
        connection = IEEE1722TpAafConnection(None, "AafStream")

        parent = _parent()
        writer.writeIEEE1722TpAafConnection(parent, connection)
        child = parent.find("IEEE-1722-TP-AAF-CONNECTION")
        assert child is not None
        assert [element.tag for element in child] == ["SHORT-NAME"]

    def test_round_trip(self, writer, parser):
        connection = _fill_connection(IEEE1722TpAafConnection(None, "AafStream"))

        parent = _parent()
        writer.writeIEEE1722TpAafConnection(parent, connection)
        element = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))[0]

        reloaded = IEEE1722TpAafConnection(None, "AafStream")
        parser.readIEEE1722TpAafConnection(element, reloaded)
        assert reloaded.getMaxTransitTime().getValue() == 0.002
        assert reloaded.getSduRefs()[0].getValue() == "/Pkgs/Pt1"
        assert reloaded.getAafAes3DataType().getValue() == IEEE1722TpAafAes3DataTypeEnum.ENUM_PCM
        assert reloaded.getAafFormat().getValue() == IEEE1722TpAafFormatEnum.AES3_32BIT
        assert reloaded.getAafNominalRate().getValue() == IEEE1722TpAafNominalRateEnum.ENUM_48KHZ
        assert reloaded.getAes3DataTypeH().getValue() == 2
        assert reloaded.getAes3DataTypeL().getValue() == 1
        assert reloaded.getChannelsPerFrame().getValue() == 2
        assert reloaded.getEventDefaultValue().getValue() == 0
        assert reloaded.getPcmBitDepth().getValue() == 24
        assert reloaded.getSparseTimestampEnabled().getValue() is True
        assert reloaded.getStreamsPerFrame().getValue() == 4
