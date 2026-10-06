"""Writer round-trip tests for FlexrayFifoConfiguration (Table 3.31, p.87).

setFlexrayFifoConfiguration emits the children in the XSD FLEXRAY-FIFO-CONFIGURATION
group order — ADMIT-WITHOUT-MESSAGE-ID, BASE-CYCLE, CHANNEL-REF, CYCLE-REPETITION,
FIFO-DEPTH, FIFO-RANGES (only when the list is non-empty), MSG-ID-MASK,
MSG-ID-MATCH — and calls writeARObject exactly once so the inherited S/T
attributes round-trip.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, DateTime, Integer, RefType, String
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology import FlexrayFifoConfiguration, FlexrayFifoRange
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_CHILD_ORDER = [
    "ADMIT-WITHOUT-MESSAGE-ID",
    "BASE-CYCLE",
    "CHANNEL-REF",
    "CYCLE-REPETITION",
    "FIFO-DEPTH",
    "FIFO-RANGES",
    "MSG-ID-MASK",
    "MSG-ID-MATCH",
]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _boolean(value):
    return Boolean().setValue(value)


def _integer(value):
    return Integer().setValue(value)


def _full_configuration():
    configuration = FlexrayFifoConfiguration()
    configuration.setAdmitWithoutMessageId(_boolean(True))
    configuration.setBaseCycle(_integer("2"))
    ref = RefType()
    ref.setDest("FLEXRAY-PHYSICAL-CHANNEL")
    ref.setValue("/FlexrayCluster/ChannelA")
    configuration.setChannelRef(ref)
    configuration.setCycleRepetition(_integer("4"))
    configuration.setFifoDepth(_integer("8"))
    configuration.setChecksum(String().setValue("chk-cfg"))
    configuration.setTimestamp(DateTime().setValue("2009-07-23T13:38:00Z"))

    first = FlexrayFifoRange()
    first.setRangeMax(_integer("200"))
    first.setRangeMin(_integer("100"))
    configuration.addFlexrayFifoRange(first)

    second = FlexrayFifoRange()
    second.setRangeMin(_integer("5"))
    configuration.addFlexrayFifoRange(second)

    configuration.setMsgIdMask(_integer("16"))
    configuration.setMsgIdMatch(_integer("32"))
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


class TestWriteFlexrayFifoConfiguration:
    def test_writes_children_in_xsd_sequence_order(self):
        fifo = _fifo(_write_fifo(_full_configuration()))

        assert [child.tag for child in fifo] == XSD_CHILD_ORDER

    def test_writes_field_values(self):
        fifo = _fifo(_write_fifo(_full_configuration()))

        assert fifo.find("ADMIT-WITHOUT-MESSAGE-ID").text == "true"
        assert fifo.find("BASE-CYCLE").text == "2"

        channel_ref = fifo.find("CHANNEL-REF")
        assert channel_ref.attrib["DEST"] == "FLEXRAY-PHYSICAL-CHANNEL"
        assert channel_ref.text == "/FlexrayCluster/ChannelA"

        assert fifo.find("CYCLE-REPETITION").text == "4"
        assert fifo.find("FIFO-DEPTH").text == "8"
        assert fifo.find("MSG-ID-MASK").text == "16"
        assert fifo.find("MSG-ID-MATCH").text == "32"

    def test_writes_fifo_ranges_wrapper_between_fifo_depth_and_msg_id_mask(self):
        fifo = _fifo(_write_fifo(_full_configuration()))

        tags = [child.tag for child in fifo]
        assert tags.index("FIFO-RANGES") == tags.index("FIFO-DEPTH") + 1
        assert tags.index("FIFO-RANGES") == tags.index("MSG-ID-MASK") - 1

        ranges = fifo.findall("FIFO-RANGES/FLEXRAY-FIFO-RANGE")
        assert len(ranges) == 2

        first, second = ranges[0], ranges[1]
        assert [child.tag for child in first] == ["RANGE-MAX", "RANGE-MIN"]
        assert first.find("RANGE-MAX").text == "200"
        assert first.find("RANGE-MIN").text == "100"
        assert [child.tag for child in second] == ["RANGE-MIN"]
        assert second.find("RANGE-MIN").text == "5"

    def test_writes_inherited_checksum_and_timestamp_attributes(self):
        fifo = _fifo(_write_fifo(_full_configuration()))

        assert fifo.attrib["S"] == "chk-cfg"
        assert fifo.attrib["T"] == "2009-07-23T13:38:00Z"

    def test_configuration_without_ranges_emits_no_wrapper(self):
        fifo = _fifo(_write_fifo(FlexrayFifoConfiguration()))

        assert fifo.find("FIFO-RANGES") is None
        assert len(fifo) == 0

    def test_round_trip_through_flexray_fifo_configuration(self):
        reloaded = ARXMLParser().getFlexrayFifoConfiguration(_namespaced_first_child(_write_fifo(_full_configuration())), ".")

        assert [child.tag for child in _fifo(_write_fifo(reloaded))] == XSD_CHILD_ORDER

        assert reloaded.getAdmitWithoutMessageId().getValue() is True
        assert reloaded.getBaseCycle().getValue() == 2
        assert reloaded.getChannelRef().getValue() == "/FlexrayCluster/ChannelA"
        assert reloaded.getChannelRef().getDest() == "FLEXRAY-PHYSICAL-CHANNEL"
        assert reloaded.getCycleRepetition().getValue() == 4
        assert reloaded.getFifoDepth().getValue() == 8
        assert reloaded.getMsgIdMask().getValue() == 16
        assert reloaded.getMsgIdMatch().getValue() == 32
        assert reloaded.getChecksum().getValue() == "chk-cfg"
        assert reloaded.getTimestamp().getValue() == "2009-07-23T13:38:00Z"

        ranges = reloaded.getFlexrayFifoRanges()
        assert len(ranges) == 2

        first, second = ranges[0], ranges[1]
        assert first.getRangeMax().getValue() == 200
        assert first.getRangeMin().getValue() == 100
        assert second.getRangeMax() is None
        assert second.getRangeMin().getValue() == 5
