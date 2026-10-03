"""Writer + round-trip tests for IPv6ExtHeaderFilterList (R23-11 Table 6.121, p.456).

Asserts the allowedIPv6ExtHeader wrapper list (ALLOWED-I-PV-6-EXT-HEADERS /
ALLOWED-I-PV-6-EXT-HEADER, AUTOSAR_00052.xsd L66606) is emitted one item per
entry, that an empty list emits no wrapper tag, and that values survive a
write -> read cycle through the class's own helper pair.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.IPv6HeaderFilterList import (
    IPv6ExtHeaderFilterList,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS_URI = "http://autosar.org/schema/r4.0"
NS = 'xmlns="%s"' % NS_URI
FILTER_LIST_TAG = "{%s}I-PV-6-EXT-HEADER-FILTER-LIST" % NS_URI


@pytest.fixture(autouse=True)
def reset_autosar():
    document = AUTOSAR.getInstance()
    document.new()
    document.setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    return ARXMLWriter()


@pytest.fixture
def parser():
    return ARXMLParser(options={"warning": True})


def _option(value):
    option = PositiveInteger()
    option.setValue(str(value))
    return option


def _serialized(writer, obj):
    root = ET.Element("ROOT", {"xmlns": NS_URI})
    writer.writeIPv6ExtHeaderFilterList(root, obj)
    return ET.tostring(root, encoding="unicode")


def _reload(parser, xml):
    element = ET.fromstring(xml).find(FILTER_LIST_TAG)
    assert element is not None
    obj = IPv6ExtHeaderFilterList(None, "RELOAD")
    parser.readIPv6ExtHeaderFilterList(element, obj)
    return obj


class TestIPv6ExtHeaderFilterListWriter:
    def test_write_emits_wrapper_with_one_item_per_entry(self, writer):
        obj = IPv6ExtHeaderFilterList(None, "Filter")
        obj.addAllowedIPv6ExtHeader(_option(0))
        obj.addAllowedIPv6ExtHeader(_option(60))
        xml = _serialized(writer, obj)
        assert "<ALLOWED-I-PV-6-EXT-HEADERS>" in xml
        assert xml.count("<ALLOWED-I-PV-6-EXT-HEADER>") == 2
        assert "<ALLOWED-I-PV-6-EXT-HEADER>0</ALLOWED-I-PV-6-EXT-HEADER>" in xml
        assert "<ALLOWED-I-PV-6-EXT-HEADER>60</ALLOWED-I-PV-6-EXT-HEADER>" in xml

    def test_empty_wrapper_is_not_emitted(self, writer):
        obj = IPv6ExtHeaderFilterList(None, "Empty")
        xml = _serialized(writer, obj)
        assert "ALLOWED-I-PV-6-EXT-HEADERS" not in xml


class TestIPv6ExtHeaderFilterListRoundTrip:
    def test_round_trip_preserves_values(self, writer, parser):
        obj = IPv6ExtHeaderFilterList(None, "Filter")
        obj.addAllowedIPv6ExtHeader(_option(0))
        obj.addAllowedIPv6ExtHeader(_option(60))
        reloaded = _reload(parser, _serialized(writer, obj))
        assert [int(value.getValue()) for value in reloaded.getAllowedIPv6ExtHeaders()] == [0, 60]

    def test_round_trip_empty_yields_empty(self, writer, parser):
        obj = IPv6ExtHeaderFilterList(None, "Empty")
        reloaded = _reload(parser, _serialized(writer, obj))
        assert reloaded.getAllowedIPv6ExtHeaders() == []
