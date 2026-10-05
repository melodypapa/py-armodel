"""Parser tests for FlexrayFifoConfiguration (Table 3.31, p.87).

FLEXRAY-FIFO-CONFIGURATION has no standalone element dispatch: it serializes only
inside FLEXRAY-FIFOS under FlexrayCommunicationController (consumer path, Rule
0001.7). Element order per the XSD FLEXRAY-FIFO-CONFIGURATION group:
ADMIT-WITHOUT-MESSAGE-ID, BASE-CYCLE, CHANNEL-REF, CYCLE-REPETITION, FIFO-DEPTH,
FIFO-RANGES, MSG-ID-MASK, MSG-ID-MATCH. getFlexrayFifoConfiguration (the class's
reader entry point) calls readARObject exactly once so the inherited S/T
attributes round-trip.
"""

import xml.etree.ElementTree as ET

from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

FULL_FIFO = (
    '<FLEXRAY-FIFO-CONFIGURATION S="chk-cfg" T="2009-07-23T13:38:00Z">'
    "<ADMIT-WITHOUT-MESSAGE-ID>true</ADMIT-WITHOUT-MESSAGE-ID>"
    "<BASE-CYCLE>2</BASE-CYCLE>"
    '<CHANNEL-REF DEST="FLEXRAY-PHYSICAL-CHANNEL">/FlexrayCluster/ChannelA</CHANNEL-REF>'
    "<CYCLE-REPETITION>4</CYCLE-REPETITION>"
    "<FIFO-DEPTH>8</FIFO-DEPTH>"
    "<FIFO-RANGES>"
    "<FLEXRAY-FIFO-RANGE><RANGE-MAX>200</RANGE-MAX><RANGE-MIN>100</RANGE-MIN></FLEXRAY-FIFO-RANGE>"
    "<FLEXRAY-FIFO-RANGE><RANGE-MIN>5</RANGE-MIN></FLEXRAY-FIFO-RANGE>"
    "</FIFO-RANGES>"
    "<MSG-ID-MASK>16</MSG-ID-MASK>"
    "<MSG-ID-MATCH>32</MSG-ID-MATCH>"
    "</FLEXRAY-FIFO-CONFIGURATION>"
)

BARE_FIFO = "<FLEXRAY-FIFO-CONFIGURATION>" "<FIFO-DEPTH>8</FIFO-DEPTH>" "</FLEXRAY-FIFO-CONFIGURATION>"

EMPTY_WRAPPER_FIFO = "<FLEXRAY-FIFO-CONFIGURATION>" "<FIFO-RANGES>" "</FIFO-RANGES>" "</FLEXRAY-FIFO-CONFIGURATION>"


def _read_fifo(xml):
    root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, xml))
    return ARXMLParser().getFlexrayFifoConfiguration(root, "FLEXRAY-FIFO-CONFIGURATION")


class TestReadFlexrayFifoConfiguration:
    def test_reads_all_field_values(self):
        fifo = _read_fifo(FULL_FIFO)

        assert fifo.getAdmitWithoutMessageId().getValue() is True
        assert fifo.getBaseCycle().getValue() == 2

        channel_ref = fifo.getChannelRef()
        assert channel_ref.getValue() == "/FlexrayCluster/ChannelA"
        assert channel_ref.getDest() == "FLEXRAY-PHYSICAL-CHANNEL"

        assert fifo.getCycleRepetition().getValue() == 4
        assert fifo.getFifoDepth().getValue() == 8
        assert fifo.getMsgIdMask().getValue() == 16
        assert fifo.getMsgIdMatch().getValue() == 32

    def test_reads_ranges_under_fifo_ranges_wrapper(self):
        fifo = _read_fifo(FULL_FIFO)

        ranges = fifo.getFlexrayFifoRanges()
        assert len(ranges) == 2

        first, second = ranges[0], ranges[1]
        assert first.getRangeMax().getValue() == 200
        assert first.getRangeMin().getValue() == 100
        assert second.getRangeMax() is None
        assert second.getRangeMin().getValue() == 5

    def test_reads_inherited_checksum_and_timestamp(self):
        fifo = _read_fifo(FULL_FIFO)

        assert fifo.getChecksum().getValue() == "chk-cfg"
        assert fifo.getTimestamp().getValue() == "2009-07-23T13:38:00Z"

    def test_reads_empty_fifo_ranges_wrapper_to_no_ranges(self):
        fifo = _read_fifo(EMPTY_WRAPPER_FIFO)

        assert fifo.getFlexrayFifoRanges() == []

    def test_reads_fifo_without_optional_fields_to_defaults(self):
        fifo = _read_fifo(BARE_FIFO)

        assert fifo.getAdmitWithoutMessageId() is None
        assert fifo.getChannelRef() is None
        assert fifo.getFlexrayFifoRanges() == []
