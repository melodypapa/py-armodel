"""Reader tests for IPv6ExtHeaderFilterList (R23-11 Table 6.121, p.456).

The allowedIPv6ExtHeader attribute is a spec `*` `attr` serialized as a wrapper
(ALLOWED-I-PV-6-EXT-HEADERS) of ALLOWED-I-PV-6-EXT-HEADER (AR:POSITIVE-INTEGER)
items (AUTOSAR_00052.xsd L66606), read through the class's own helper.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.IPv6HeaderFilterList import (
    IPv6ExtHeaderFilterList,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = 'xmlns="http://autosar.org/schema/r4.0"'


@pytest.fixture(autouse=True)
def reset_autosar():
    document = AUTOSAR.getInstance()
    document.new()
    document.setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    return ARXMLParser(options={"warning": True})


def _read(parser, xml, obj):
    parser.readIPv6ExtHeaderFilterList(ET.fromstring(xml), obj)


class TestIPv6ExtHeaderFilterListReader:
    def test_read_wrapper_list_values(self, parser):
        obj = IPv6ExtHeaderFilterList(None, "Filter")
        _read(
            parser,
            "<I-PV-6-EXT-HEADER-FILTER-LIST %s>"
            "<SHORT-NAME>Filter</SHORT-NAME>"
            "<ALLOWED-I-PV-6-EXT-HEADERS>"
            "<ALLOWED-I-PV-6-EXT-HEADER>0</ALLOWED-I-PV-6-EXT-HEADER>"
            "<ALLOWED-I-PV-6-EXT-HEADER>60</ALLOWED-I-PV-6-EXT-HEADER>"
            "</ALLOWED-I-PV-6-EXT-HEADERS>"
            "</I-PV-6-EXT-HEADER-FILTER-LIST>" % NS,
            obj,
        )
        assert [int(value.getValue()) for value in obj.getAllowedIPv6ExtHeaders()] == [0, 60]

    def test_read_without_wrapper_yields_empty(self, parser):
        obj = IPv6ExtHeaderFilterList(None, "Empty")
        _read(parser, "<I-PV-6-EXT-HEADER-FILTER-LIST %s><SHORT-NAME>Empty</SHORT-NAME></I-PV-6-EXT-HEADER-FILTER-LIST>" % NS, obj)
        assert obj.getAllowedIPv6ExtHeaders() == []

    def test_read_empty_wrapper_yields_empty(self, parser):
        obj = IPv6ExtHeaderFilterList(None, "Empty")
        _read(
            parser,
            "<I-PV-6-EXT-HEADER-FILTER-LIST %s><SHORT-NAME>Empty</SHORT-NAME>" "<ALLOWED-I-PV-6-EXT-HEADERS/></I-PV-6-EXT-HEADER-FILTER-LIST>" % NS,
            obj,
        )
        assert obj.getAllowedIPv6ExtHeaders() == []
