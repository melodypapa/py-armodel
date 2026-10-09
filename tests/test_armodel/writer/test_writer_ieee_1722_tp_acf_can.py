"""Tests for the writeIEEE1722TpAcfCan handler (R23-11 IEEE1722TpAcfCan, Table 6.293, p.661)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf import (
    IEEE1722TpAcfCan,
    IEEE1722TpAcfCanMessageTypeEnum,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


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


def _pos_int(value):
    integer = PositiveInteger()
    integer.setValue(value)
    return integer


def _message_type(value: str) -> IEEE1722TpAcfCanMessageTypeEnum:
    enum = IEEE1722TpAcfCanMessageTypeEnum()
    enum.setValue(value)
    return enum


def _fill_bus(bus: IEEE1722TpAcfCan) -> IEEE1722TpAcfCan:
    bus.createIEEE1722TpAcfCanPart("CanPart1")
    bus.setBusId(_pos_int(4))
    bus.setMessageType(_message_type("CAN-BRIEF"))
    return bus


class TestWriteIEEE1722TpAcfCan:
    """Tests for writeIEEE1722TpAcfCan handler (R23-11 IEEE1722TpAcfCan, Table 6.293, p.661)."""

    def test_children_in_xsd_order(self, writer):
        bus = _fill_bus(IEEE1722TpAcfCan(None, "CanBus"))

        parent = _parent()
        writer.writeIEEE1722TpAcfCan(parent, bus)
        child_tags = [element.tag for element in parent.find("IEEE-1722-TP-ACF-CAN")]
        assert child_tags == ["SHORT-NAME", "ACF-PARTS", "BUS-ID", "MESSAGE-TYPE"]

    def test_message_type_value_in_xml(self, writer):
        bus = _fill_bus(IEEE1722TpAcfCan(None, "CanBus"))

        parent = _parent()
        writer.writeIEEE1722TpAcfCan(parent, bus)
        child = parent.find("IEEE-1722-TP-ACF-CAN")
        assert child.find("MESSAGE-TYPE").text == "CAN-BRIEF"
        assert child.find("BUS-ID").text == "4"

    def test_empty_bus_writes_only_short_name(self, writer):
        bus = IEEE1722TpAcfCan(None, "CanBus")

        parent = _parent()
        writer.writeIEEE1722TpAcfCan(parent, bus)
        child = parent.find("IEEE-1722-TP-ACF-CAN")
        assert [element.tag for element in child] == ["SHORT-NAME"]
        assert child.find("MESSAGE-TYPE") is None

    def test_round_trip(self, writer, parser):
        bus = _fill_bus(IEEE1722TpAcfCan(None, "CanBus"))

        parent = _parent()
        writer.writeIEEE1722TpAcfCan(parent, bus)
        element = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))[0]

        reloaded = IEEE1722TpAcfCan(None, "CanBus")
        parser.readIEEE1722TpAcfCan(element, reloaded)
        parts = reloaded.getAcfParts()
        assert len(parts) == 1
        assert parts[0].getShortName() == "CanPart1"
        assert reloaded.getBusId().getValue() == 4
        assert reloaded.getMessageType() is not None
        assert reloaded.getMessageType().getValue() == "CAN-BRIEF"

    def test_round_trip_via_acf_connection_dispatch(self, writer, parser):
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp import (
            IEEE1722TpAcfConnection,
        )

        connection = IEEE1722TpAcfConnection(None, "AcfConnection")
        bus = connection.createIEEE1722TpAcfCan("CanBus")
        bus.setBusId(_pos_int(4))
        bus.setMessageType(_message_type("CAN-BRIEF"))

        parent = _parent()
        writer.writeIEEE1722TpAcfConnection(parent, connection)
        element = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))[0]

        reloaded = IEEE1722TpAcfConnection(None, "AcfConnection")
        parser.readIEEE1722TpAcfConnection(element, reloaded)
        buses = reloaded.getAcfTransportedBuses()
        assert len(buses) == 1
        assert isinstance(buses[0], IEEE1722TpAcfCan)
        assert buses[0].getBusId().getValue() == 4
        assert buses[0].getMessageType().getValue() == "CAN-BRIEF"
