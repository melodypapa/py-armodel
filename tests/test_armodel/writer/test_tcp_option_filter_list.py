"""Writer + round-trip tests for TcpOptionFilterList (R23-11 Table 6.123, p.457).

Asserts the allowedTcpOption wrapper list (ALLOWED-TCP-OPTIONS /
ALLOWED-TCP-OPTION, AUTOSAR_00052.xsd L120400-120419) is emitted one item per
entry, that an empty list emits no wrapper tag, and that values survive a
write -> read cycle through the class's own helper pair.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.TcpOptionFilterSet import (
    TcpOptionFilterList,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS_URI = "http://autosar.org/schema/r4.0"
NS = 'xmlns="%s"' % NS_URI
FILTER_LIST_TAG = "{%s}TCP-OPTION-FILTER-LIST" % NS_URI


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
    writer.writeTcpOptionFilterList(root, obj)
    return ET.tostring(root, encoding="unicode")


def _reload(parser, xml):
    element = ET.fromstring(xml).find(FILTER_LIST_TAG)
    assert element is not None
    obj = TcpOptionFilterList(None, "RELOAD")
    parser.readTcpOptionFilterList(element, obj)
    return obj


class TestTcpOptionFilterListWriter:
    def test_write_emits_wrapper_with_one_item_per_entry(self, writer):
        obj = TcpOptionFilterList(None, "Filter")
        obj.addAllowedTcpOption(_option(7))
        obj.addAllowedTcpOption(_option(60))
        xml = _serialized(writer, obj)
        assert "<ALLOWED-TCP-OPTIONS>" in xml
        assert xml.count("<ALLOWED-TCP-OPTION>") == 2
        assert "<ALLOWED-TCP-OPTION>7</ALLOWED-TCP-OPTION>" in xml
        assert "<ALLOWED-TCP-OPTION>60</ALLOWED-TCP-OPTION>" in xml

    def test_empty_wrapper_is_not_emitted(self, writer):
        obj = TcpOptionFilterList(None, "Empty")
        xml = _serialized(writer, obj)
        assert "ALLOWED-TCP-OPTIONS" not in xml


class TestTcpOptionFilterListRoundTrip:
    def test_round_trip_preserves_values(self, writer, parser):
        obj = TcpOptionFilterList(None, "Filter")
        obj.addAllowedTcpOption(_option(7))
        obj.addAllowedTcpOption(_option(60))
        reloaded = _reload(parser, _serialized(writer, obj))
        assert [int(option.getValue()) for option in reloaded.getAllowedTcpOptions()] == [7, 60]

    def test_round_trip_empty_yields_empty(self, writer, parser):
        obj = TcpOptionFilterList(None, "Empty")
        reloaded = _reload(parser, _serialized(writer, obj))
        assert reloaded.getAllowedTcpOptions() == []
