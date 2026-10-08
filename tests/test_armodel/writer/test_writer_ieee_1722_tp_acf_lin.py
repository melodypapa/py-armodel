"""Tests for the writeIEEE1722TpAcfLin handler (R23-11 IEEE1722TpAcfLin, Table 6.296, p.667)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf import (
    IEEE1722TpAcfLin,
    IEEE1722TpAcfLinPart,
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


def _bool(value):
    boolean = Boolean()
    boolean.setValue(value)
    return boolean


def _fill_bus(bus: IEEE1722TpAcfLin) -> IEEE1722TpAcfLin:
    bus.createIEEE1722TpAcfLinPart("LinPart1")
    bus.setBusId(_pos_int(5))
    bus.setBaseFrequency(_pos_int(48000))
    bus.setFrameSyncEnabled(_bool(True))
    bus.setTimestampInterval(_pos_int(4))
    return bus


class TestWriteIEEE1722TpAcfLin:
    """Tests for writeIEEE1722TpAcfLin handler (R23-11 IEEE1722TpAcfLin, Table 6.296, p.667)."""

    def test_children_in_xsd_order(self, writer):
        bus = _fill_bus(IEEE1722TpAcfLin(None, "LinBus"))

        parent = _parent()
        writer.writeIEEE1722TpAcfLin(parent, bus)
        child_tags = [element.tag for element in parent.find("IEEE-1722-TP-ACF-LIN")]
        assert child_tags == [
            "SHORT-NAME",
            "ACF-PARTS",
            "BUS-ID",
            "BASE-FREQUENCY",
            "FRAME-SYNC-ENABLED",
            "TIMESTAMP-INTERVAL",
        ]

    def test_field_values_in_xml(self, writer):
        bus = _fill_bus(IEEE1722TpAcfLin(None, "LinBus"))

        parent = _parent()
        writer.writeIEEE1722TpAcfLin(parent, bus)
        child = parent.find("IEEE-1722-TP-ACF-LIN")
        assert child.find("BUS-ID").text == "5"
        assert child.find("BASE-FREQUENCY").text == "48000"
        assert child.find("FRAME-SYNC-ENABLED").text == "true"
        assert child.find("TIMESTAMP-INTERVAL").text == "4"

    def test_empty_bus_writes_only_short_name(self, writer):
        bus = IEEE1722TpAcfLin(None, "LinBus")

        parent = _parent()
        writer.writeIEEE1722TpAcfLin(parent, bus)
        child = parent.find("IEEE-1722-TP-ACF-LIN")
        assert [element.tag for element in child] == ["SHORT-NAME"]
        assert child.find("BASE-FREQUENCY") is None
        assert child.find("FRAME-SYNC-ENABLED") is None
        assert child.find("TIMESTAMP-INTERVAL") is None

    def test_round_trip(self, writer, parser):
        bus = _fill_bus(IEEE1722TpAcfLin(None, "LinBus"))

        parent = _parent()
        writer.writeIEEE1722TpAcfLin(parent, bus)
        element = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))[0]

        reloaded = IEEE1722TpAcfLin(None, "LinBus")
        parser.readIEEE1722TpAcfLin(element, reloaded)
        parts = reloaded.getAcfParts()
        assert len(parts) == 1
        assert parts[0].getShortName() == "LinPart1"
        assert reloaded.getBusId().getValue() == 5
        assert reloaded.getBaseFrequency().getValue() == 48000
        assert reloaded.getFrameSyncEnabled().getValue() is True
        assert reloaded.getTimestampInterval().getValue() == 4

    def test_round_trip_via_acf_connection_dispatch(self, writer, parser):
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp import (
            IEEE1722TpAcfConnection,
        )

        connection = IEEE1722TpAcfConnection(None, "AcfConnection")
        bus = connection.createIEEE1722TpAcfLin("LinBus")
        bus.createIEEE1722TpAcfLinPart("LinPart1")
        bus.setBusId(_pos_int(5))
        bus.setBaseFrequency(_pos_int(48000))
        bus.setTimestampInterval(_pos_int(4))

        parent = _parent()
        writer.writeIEEE1722TpAcfConnection(parent, connection)
        element = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))[0]

        reloaded = IEEE1722TpAcfConnection(None, "AcfConnection")
        parser.readIEEE1722TpAcfConnection(element, reloaded)
        buses = reloaded.getAcfTransportedBuses()
        assert len(buses) == 1
        assert isinstance(buses[0], IEEE1722TpAcfLin)
        lin_bus = buses[0]
        assert lin_bus.getBusId().getValue() == 5
        assert lin_bus.getBaseFrequency().getValue() == 48000
        assert lin_bus.getTimestampInterval().getValue() == 4
        parts = lin_bus.getAcfParts()
        assert len(parts) == 1
        assert isinstance(parts[0], IEEE1722TpAcfLinPart)
        assert parts[0].getShortName() == "LinPart1"
