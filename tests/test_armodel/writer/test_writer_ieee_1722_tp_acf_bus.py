"""Tests for the writeIEEE1722TpAcfBus handler (R23-11 IEEE1722TpAcfBus, Table 6.291, p.657)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf import IEEE1722TpAcfBus
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


def _concrete_bus(short_name: str) -> IEEE1722TpAcfBus:
    class _Bus(IEEE1722TpAcfBus):
        pass

    return _Bus(None, short_name)


def _fill_bus(bus: IEEE1722TpAcfBus) -> IEEE1722TpAcfBus:
    bus.createIEEE1722TpAcfCanPart("CanPart1")
    bus.createIEEE1722TpAcfLinPart("LinPart1")
    bus.setBusId(_pos_int(7))
    return bus


class TestWriteIEEE1722TpAcfBus:
    """Tests for writeIEEE1722TpAcfBus handler (R23-11 IEEE1722TpAcfBus, Table 6.291, p.657)."""

    def test_children_in_xsd_order(self, writer):
        bus = _fill_bus(_concrete_bus("CanBus"))

        parent = _parent()
        writer.writeIEEE1722TpAcfBus(parent, bus)
        child_tags = [element.tag for element in parent]
        assert child_tags == ["SHORT-NAME", "ACF-PARTS", "BUS-ID"]

    def test_field_values_in_xml(self, writer):
        bus = _fill_bus(_concrete_bus("CanBus"))

        parent = _parent()
        writer.writeIEEE1722TpAcfBus(parent, bus)
        parts = parent.find("ACF-PARTS")
        assert parts is not None
        part_tags = [(element.tag, element.find("SHORT-NAME").text) for element in parts]
        assert part_tags == [
            ("IEEE-1722-TP-ACF-CAN-PART", "CanPart1"),
            ("IEEE-1722-TP-ACF-LIN-PART", "LinPart1"),
        ]
        assert parent.find("BUS-ID").text == "7"

    def test_empty_bus_writes_only_short_name(self, writer):
        bus = _concrete_bus("CanBus")

        parent = _parent()
        writer.writeIEEE1722TpAcfBus(parent, bus)
        assert [element.tag for element in parent] == ["SHORT-NAME"]
        assert parent.find("ACF-PARTS") is None

    def test_variation_point_written_last(self, writer):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint

        bus = _fill_bus(_concrete_bus("CanBus"))
        bus.setVariationPoint(VariationPoint())

        parent = _parent()
        writer.writeIEEE1722TpAcfBus(parent, bus)
        child_tags = [element.tag for element in parent]
        assert child_tags == ["SHORT-NAME", "ACF-PARTS", "BUS-ID", "VARIATION-POINT"]
        assert len(parent.findall("VARIATION-POINT")) == 1

    def test_round_trip(self, writer, parser):
        bus = _fill_bus(_concrete_bus("CanBus"))

        parent = _parent()
        writer.writeIEEE1722TpAcfBus(parent, bus)
        element = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        reloaded = _concrete_bus("CanBus")
        parser.readIEEE1722TpAcfBus(element, reloaded)
        parts = reloaded.getAcfParts()
        assert len(parts) == 2
        assert isinstance(parts[0], type(bus.getAcfParts()[0]))
        assert parts[0].getShortName() == "CanPart1"
        assert isinstance(parts[1], type(bus.getAcfParts()[1]))
        assert parts[1].getShortName() == "LinPart1"
        assert reloaded.getBusId().getValue() == 7
