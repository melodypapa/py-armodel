"""Parser tests for FlexrayFifoRange (Table 3.32, p.87).

FLEXRAY-FIFO-RANGE has no standalone element dispatch: it serializes only as a
choice of FLEXRAY-FIFO-RANGE elements under the FIFO-RANGES wrapper inside
FLEXRAY-FIFO-CONFIGURATION (consumer path, Rule 0001.7), positioned after
FIFO-DEPTH and before MSG-ID-MASK per the XSD FLEXRAY-FIFO-CONFIGURATION group.
Element order per the XSD FLEXRAY-FIFO-RANGE group: RANGE-MAX, RANGE-MIN.
getFlexrayFifoRange (the class's reader entry point) calls readARObject exactly
once so the inherited S/T attributes round-trip.
"""

import xml.etree.ElementTree as ET

from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

FULL_FIFO_RANGES = (
    "<FLEXRAY-FIFO-CONFIGURATION>"
    "<ADMIT-WITHOUT-MESSAGE-ID>true</ADMIT-WITHOUT-MESSAGE-ID>"
    "<FIFO-DEPTH>8</FIFO-DEPTH>"
    "<FIFO-RANGES>"
    '<FLEXRAY-FIFO-RANGE S="chk-1" T="2009-07-23T13:38:00Z">'
    "<RANGE-MAX>200</RANGE-MAX>"
    "<RANGE-MIN>100</RANGE-MIN>"
    "</FLEXRAY-FIFO-RANGE>"
    "<FLEXRAY-FIFO-RANGE>"
    "<RANGE-MIN>5</RANGE-MIN>"
    "</FLEXRAY-FIFO-RANGE>"
    "</FIFO-RANGES>"
    "<MSG-ID-MASK>16</MSG-ID-MASK>"
    "</FLEXRAY-FIFO-CONFIGURATION>"
)

BARE_FIFO = "<FLEXRAY-FIFO-CONFIGURATION>" "<FIFO-DEPTH>8</FIFO-DEPTH>" "</FLEXRAY-FIFO-CONFIGURATION>"

EMPTY_WRAPPER_FIFO = "<FLEXRAY-FIFO-CONFIGURATION>" "<FIFO-RANGES>" "</FIFO-RANGES>" "</FLEXRAY-FIFO-CONFIGURATION>"


def _read_fifo(xml):
    root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, xml))
    return ARXMLParser().getFlexrayFifoConfiguration(root, "FLEXRAY-FIFO-CONFIGURATION")


class TestReadFlexrayFifoRange:
    def test_reads_range_field_values_under_fifo_ranges_wrapper(self):
        fifo = _read_fifo(FULL_FIFO_RANGES)

        ranges = fifo.getFlexrayFifoRanges()
        assert len(ranges) == 2

        first, second = ranges[0], ranges[1]
        assert first.getRangeMax().getValue() == 200
        assert first.getRangeMin().getValue() == 100
        assert second.getRangeMax() is None
        assert second.getRangeMin().getValue() == 5

    def test_reads_inherited_checksum_and_timestamp(self):
        fifo = _read_fifo(FULL_FIFO_RANGES)

        first = fifo.getFlexrayFifoRanges()[0]
        assert first.getChecksum().getValue() == "chk-1"
        assert first.getTimestamp().getValue() == "2009-07-23T13:38:00Z"

        second = fifo.getFlexrayFifoRanges()[1]
        assert second.getChecksum() is None
        assert second.getTimestamp() is None

    def test_reads_empty_fifo_ranges_wrapper_to_no_ranges(self):
        fifo = _read_fifo(EMPTY_WRAPPER_FIFO)

        assert fifo.getFlexrayFifoRanges() == []

    def test_reads_fifo_without_ranges_wrapper_to_no_ranges(self):
        fifo = _read_fifo(BARE_FIFO)

        assert fifo.getFlexrayFifoRanges() == []
