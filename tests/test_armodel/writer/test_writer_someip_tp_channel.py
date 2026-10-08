"""Tests for the writeSomeipTpChannel handler (R23-11 SomeipTpChannel, Table 6.266, p.620)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import SomeipTpChannel
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_CHILD_ORDER = [
    "SHORT-NAME",
    "BURST-SIZE",
    "RX-TIMEOUT-TIME",
    "SEPARATION-TIME",
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


def _positive_integer(value):
    integer = PositiveInteger()
    integer.setValue(value)
    return integer


def _time_value(value):
    time_value = TimeValue()
    time_value.setValue(value)
    return time_value


def _fill_channel(channel: SomeipTpChannel) -> SomeipTpChannel:
    channel.setBurstSize(_positive_integer("8"))
    channel.setRxTimeoutTime(_time_value("0.5"))
    channel.setSeparationTime(_time_value("0.02"))
    return channel


class TestWriteSomeipTpChannel:
    """Tests for writeSomeipTpChannel handler (R23-11 SomeipTpChannel, Table 6.266, p.620)."""

    def test_children_in_xsd_order(self, writer):
        channel = _fill_channel(SomeipTpChannel(None, "Chan1"))

        parent = _parent()
        writer.writeSomeipTpChannel(parent, channel)
        child = parent.find("SOMEIP-TP-CHANNEL")
        assert child is not None
        child_tags = [element.tag for element in child]
        assert child_tags == XSD_CHILD_ORDER

    def test_field_values_in_xml(self, writer):
        channel = _fill_channel(SomeipTpChannel(None, "Chan1"))

        parent = _parent()
        writer.writeSomeipTpChannel(parent, channel)
        child = parent.find("SOMEIP-TP-CHANNEL")
        assert child.find("SHORT-NAME").text == "Chan1"
        assert child.find("BURST-SIZE").text == "8"
        assert child.find("RX-TIMEOUT-TIME").text == "0.5"
        assert child.find("SEPARATION-TIME").text == "0.02"

    def test_empty_channel_writes_no_own_elements(self, writer):
        channel = SomeipTpChannel(None, "Chan1")

        parent = _parent()
        writer.writeSomeipTpChannel(parent, channel)
        child = parent.find("SOMEIP-TP-CHANNEL")
        assert child is not None
        child_tags = [element.tag for element in child if element.tag != "SHORT-NAME"]
        assert child_tags == []

    def test_round_trip(self, writer, parser):
        channel = _fill_channel(SomeipTpChannel(None, "Chan1"))

        parent = _parent()
        writer.writeSomeipTpChannel(parent, channel)
        element = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))[0]

        reloaded = SomeipTpChannel(None, "Chan1")
        parser.readSomeipTpChannel(element, reloaded)
        assert reloaded.getShortName() == "Chan1"
        assert reloaded.getBurstSize() is not None
        assert reloaded.getBurstSize().getValue() == 8
        assert reloaded.getRxTimeoutTime() is not None
        assert reloaded.getRxTimeoutTime().getValue() == 0.5
        assert reloaded.getSeparationTime() is not None
        assert reloaded.getSeparationTime().getValue() == 0.02
