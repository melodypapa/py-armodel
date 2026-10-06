"""
Writer tests for StreamFilterIEEE1722Tp (CP_TPS_SystemTemplate Table 3.92, p.139, R23-11).

Checks the child element value and the XSD sequence order (STREAM-ID per group
STREAM-FILTER-IEEE-1722-TP — the element is emitted in live documents as the
IEEE-1722-TP-RULE child of the SWITCH-STREAM-FILTER-RULE), the partial-emission case
and the write→parse round-trip.

Round-trip counterpart: tests/test_armodel/parser/test_stream_filter_ieee_1722_tp.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveUnlimitedInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import StreamFilterIEEE1722Tp
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _stream_id(value):
    stream_id = PositiveUnlimitedInteger()
    stream_id.setValue(value)
    return stream_id


def _full_tp_rule() -> StreamFilterIEEE1722Tp:
    tp_rule = StreamFilterIEEE1722Tp()
    tp_rule.setStreamId(_stream_id("0x0102030405060708"))
    return tp_rule


def _write(tp_rule):
    element = ET.Element("IEEE-1722-TP-RULE")
    ARXMLWriter().writeStreamFilterIEEE1722Tp(element, tp_rule)
    return element


class TestWriteStreamFilterIEEE1722Tp:
    def test_write_all_attributes_in_xsd_order(self):
        element = _write(_full_tp_rule())

        assert [child.tag for child in element] == ["STREAM-ID"]
        assert element.find("STREAM-ID").text == "0x0102030405060708"

    def test_write_empty_emits_no_children(self):
        element = _write(StreamFilterIEEE1722Tp())

        assert len(element) == 0

    def test_write_and_reparse_round_trip(self):
        element = _write(_full_tp_rule())

        inner = ET.tostring(element).decode("utf-8")
        namespaced = ET.fromstring(inner.replace(element.tag, "%s xmlns='%s'" % (element.tag, NS), 1))

        recovered = StreamFilterIEEE1722Tp()
        ARXMLParser(options={"warning": True}).readStreamFilterIEEE1722Tp(namespaced, recovered)

        assert isinstance(recovered.getStreamId(), PositiveUnlimitedInteger)
        assert recovered.getStreamId().getValue() == 0x0102030405060708
