"""
Reader tests for StreamFilterPortRange (CP_TPS_SystemTemplate Table 3.91, p.139, R23-11).

Covers the MAX / MIN children of the STREAM-FILTER-PORT-RANGE element shape
(AUTOSAR_00052.xsd group STREAM-FILTER-PORT-RANGE — emitted in live documents as the
STREAM-FILTER-PORT-RANGE children of the DESTINATION-PORTS / SOURCE-PORTS wrappers of
the SWITCH-STREAM-FILTER-RULE IP/TP rule), the absent-element case and the
empty-element case.

Round-trip counterpart: tests/test_armodel/writer/test_stream_filter_port_range.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import StreamFilterPortRange
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<STREAM-FILTER-PORT-RANGE xmlns='{NS}'>{inner}</STREAM-FILTER-PORT-RANGE>")


class TestReadStreamFilterPortRange:
    def test_read_all_attributes(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<MAX>65535</MAX><MIN>1024</MIN>")
        port_range = StreamFilterPortRange()
        parser.readStreamFilterPortRange(element, port_range)

        assert isinstance(port_range.getMax(), PositiveInteger)
        assert port_range.getMax().getValue() == 65535
        assert isinstance(port_range.getMin(), PositiveInteger)
        assert port_range.getMin().getValue() == 1024

    def test_read_partial_attributes(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<MIN>80</MIN>")
        port_range = StreamFilterPortRange()
        parser.readStreamFilterPortRange(element, port_range)

        assert port_range.getMax() is None
        assert port_range.getMin().getValue() == 80

    def test_read_empty_element(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("")
        port_range = StreamFilterPortRange()
        parser.readStreamFilterPortRange(element, port_range)

        assert port_range.getMax() is None
        assert port_range.getMin() is None
