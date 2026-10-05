"""Writer round-trip tests for FlexrayFifoRange (Table 3.32, p.87).

FLEXRAY-FIFO-RANGE has no standalone element dispatch: setFlexrayFifoConfiguration
emits the FIFO-RANGES wrapper (only when the list is non-empty) between FIFO-DEPTH
and MSG-ID-MASK per the XSD FLEXRAY-FIFO-CONFIGURATION group, and each
FLEXRAY-FIFO-RANGE child carries RANGE-MAX then RANGE-MIN per the XSD
FLEXRAY-FIFO-RANGE group. setFlexrayFifoRange (the class's writer entry point)
calls writeARObject exactly once so the inherited S/T attributes round-trip.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, Integer, String
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology import FlexrayFifoConfiguration
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _integer(value):
    return Integer().setValue(value)


def _configuration_with_ranges():
    configuration = FlexrayFifoConfiguration()
    configuration.setFifoDepth(_integer("8"))

    first = configuration.createFlexrayFifoRange()
    first.setRangeMax(_integer("200"))
    first.setRangeMin(_integer("100"))
    first.setChecksum(String().setValue("chk-1"))
    first.setTimestamp(DateTime().setValue("2009-07-23T13:38:00Z"))

    second = configuration.createFlexrayFifoRange()
    second.setRangeMin(_integer("5"))

    configuration.setMsgIdMask(_integer("16"))
    return configuration


def _write_fifo(configuration):
    parent = ET.Element("PARENT")
    ARXMLWriter().setFlexrayFifoConfiguration(parent, "FLEXRAY-FIFO-CONFIGURATION", configuration)
    return parent


def _fifo(parent):
    return parent.find("FLEXRAY-FIFO-CONFIGURATION")


def _namespaced_first_child(parent):
    xml_text = ET.tostring(parent, encoding="unicode")
    namespaced = ET.fromstring(xml_text.replace(parent[0].tag, "%s xmlns='%s'" % (parent[0].tag, NS), 1))
    return namespaced[0]


class TestWriteFlexrayFifoRange:
    def test_writes_ranges_under_fifo_ranges_wrapper_in_xsd_position(self):
        fifo = _fifo(_write_fifo(_configuration_with_ranges()))

        assert [child.tag for child in fifo] == ["FIFO-DEPTH", "FIFO-RANGES", "MSG-ID-MASK"]

        wrapper = fifo.find("FIFO-RANGES")
        ranges = wrapper.findall("FLEXRAY-FIFO-RANGE")
        assert len(ranges) == 2

    def test_writes_range_field_values_in_xsd_order(self):
        fifo = _fifo(_write_fifo(_configuration_with_ranges()))

        first, second = fifo.findall("FIFO-RANGES/FLEXRAY-FIFO-RANGE")

        assert [child.tag for child in first] == ["RANGE-MAX", "RANGE-MIN"]
        assert first.find("RANGE-MAX").text == "200"
        assert first.find("RANGE-MIN").text == "100"

        assert [child.tag for child in second] == ["RANGE-MIN"]
        assert second.find("RANGE-MIN").text == "5"

    def test_writes_checksum_and_timestamp_attributes(self):
        fifo = _fifo(_write_fifo(_configuration_with_ranges()))

        first, second = fifo.findall("FIFO-RANGES/FLEXRAY-FIFO-RANGE")
        assert first.attrib["S"] == "chk-1"
        assert first.attrib["T"] == "2009-07-23T13:38:00Z"
        assert "S" not in second.attrib
        assert "T" not in second.attrib

    def test_configuration_without_ranges_emits_no_wrapper(self):
        fifo = _fifo(_write_fifo(FlexrayFifoConfiguration()))

        assert fifo.find("FIFO-RANGES") is None
        assert len(fifo) == 0

    def test_round_trip_through_flexray_fifo_configuration(self):
        parent = _write_fifo(_configuration_with_ranges())
        reloaded = ARXMLParser().getFlexrayFifoConfiguration(_namespaced_first_child(parent), ".")

        assert [child.tag for child in _fifo(_write_fifo(reloaded))] == ["FIFO-DEPTH", "FIFO-RANGES", "MSG-ID-MASK"]

        ranges = reloaded.getFlexrayFifoRanges()
        assert len(ranges) == 2

        first, second = ranges[0], ranges[1]
        assert first.getRangeMax().getValue() == 200
        assert first.getRangeMin().getValue() == 100
        assert first.getChecksum().getValue() == "chk-1"
        assert first.getTimestamp().getValue() == "2009-07-23T13:38:00Z"
        assert second.getRangeMax() is None
        assert second.getRangeMin().getValue() == 5
        assert second.getChecksum() is None
