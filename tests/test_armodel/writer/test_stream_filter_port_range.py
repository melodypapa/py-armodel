"""
Writer tests for StreamFilterPortRange (CP_TPS_SystemTemplate Table 3.91, p.139, R23-11).

Checks the child element values and the XSD sequence order (MAX, MIN per group
STREAM-FILTER-PORT-RANGE — the element is emitted in live documents as the
STREAM-FILTER-PORT-RANGE children of the DESTINATION-PORTS / SOURCE-PORTS wrappers of
the SWITCH-STREAM-FILTER-RULE IP/TP rule), the partial-emission case and the
write→parse round-trip.

Round-trip counterpart: tests/test_armodel/parser/test_stream_filter_port_range.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import StreamFilterPortRange
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _port(value):
    port = PositiveInteger()
    port.setValue(value)
    return port


def _full_port_range() -> StreamFilterPortRange:
    port_range = StreamFilterPortRange()
    port_range.setMax(_port("65535"))
    port_range.setMin(_port("1024"))
    return port_range


def _write(port_range):
    element = ET.Element("STREAM-FILTER-PORT-RANGE")
    ARXMLWriter().writeStreamFilterPortRange(element, port_range)
    return element


class TestWriteStreamFilterPortRange:
    def test_write_all_attributes_in_xsd_order(self):
        element = _write(_full_port_range())

        assert [child.tag for child in element] == ["MAX", "MIN"]
        assert element.find("MAX").text == "65535"
        assert element.find("MIN").text == "1024"

    def test_write_partial_omits_absent_elements(self):
        port_range = StreamFilterPortRange()
        port_range.setMin(_port("80"))

        element = _write(port_range)

        assert [child.tag for child in element] == ["MIN"]
        assert element.find("MIN").text == "80"

    def test_write_empty_emits_no_children(self):
        element = _write(StreamFilterPortRange())

        assert len(element) == 0

    def test_write_and_reparse_round_trip(self):
        element = _write(_full_port_range())

        inner = ET.tostring(element).decode("utf-8")
        namespaced = ET.fromstring(inner.replace(element.tag, "%s xmlns='%s'" % (element.tag, NS), 1))

        recovered = StreamFilterPortRange()
        ARXMLParser(options={"warning": True}).readStreamFilterPortRange(namespaced, recovered)

        assert isinstance(recovered.getMax(), PositiveInteger)
        assert recovered.getMax().getValue() == 65535
        assert isinstance(recovered.getMin(), PositiveInteger)
        assert recovered.getMin().getValue() == 1024
