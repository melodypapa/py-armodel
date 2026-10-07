"""
Reader tests for StreamFilterIEEE1722Tp (CP_TPS_SystemTemplate Table 3.92, p.139, R23-11).

Covers the STREAM-ID child of the STREAM-FILTER-IEEE-1722-TP element shape
(AUTOSAR_00052.xsd group STREAM-FILTER-IEEE-1722-TP — emitted in live documents as the
IEEE-1722-TP-RULE child of the SWITCH-STREAM-FILTER-RULE), the absent-element case and
the empty-element case.

Round-trip counterpart: tests/test_armodel/writer/test_stream_filter_ieee_1722_tp.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveUnlimitedInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import StreamFilterIEEE1722Tp
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<IEEE-1722-TP-RULE xmlns='{NS}'>{inner}</IEEE-1722-TP-RULE>")


class TestReadStreamFilterIEEE1722Tp:
    def test_read_all_attributes(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<STREAM-ID>0x0102030405060708</STREAM-ID>")
        tp_rule = StreamFilterIEEE1722Tp()
        parser.readStreamFilterIEEE1722Tp(element, tp_rule)

        assert isinstance(tp_rule.getStreamId(), PositiveUnlimitedInteger)
        assert tp_rule.getStreamId().getValue() == 0x0102030405060708

    def test_read_empty_element(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("")
        tp_rule = StreamFilterIEEE1722Tp()
        parser.readStreamFilterIEEE1722Tp(element, tp_rule)

        assert tp_rule.getStreamId() is None
