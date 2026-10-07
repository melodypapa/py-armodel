"""Parser tests for IPv6ExtHeaderFilterSet (Table 6.120, p.455):
the ARPackage ELEMENTS choice instantiates the ARElement subclass.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.IPv6HeaderFilterList import (
    IPv6ExtHeaderFilterList,
    IPv6ExtHeaderFilterSet,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    return ARXMLParser()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<ROOT xmlns='{NS}'>{inner}</ROOT>")


def _package():
    return AUTOSAR.getInstance().createARPackage("Pkg")


def test_read_ipv6_ext_header_filter_set(parser):
    root = _snip(
        "<ELEMENTS>"
        "<I-PV-6-EXT-HEADER-FILTER-SET>"
        "<SHORT-NAME>FilterSet</SHORT-NAME>"
        "<EXT-HEADER-FILTER-LISTS>"
        "<I-PV-6-EXT-HEADER-FILTER-LIST>"
        "<SHORT-NAME>FilterList</SHORT-NAME>"
        "<ALLOWED-I-PV-6-EXT-HEADERS>"
        "<ALLOWED-I-PV-6-EXT-HEADER>0</ALLOWED-I-PV-6-EXT-HEADER>"
        "<ALLOWED-I-PV-6-EXT-HEADER>60</ALLOWED-I-PV-6-EXT-HEADER>"
        "</ALLOWED-I-PV-6-EXT-HEADERS>"
        "</I-PV-6-EXT-HEADER-FILTER-LIST>"
        "</EXT-HEADER-FILTER-LISTS>"
        "</I-PV-6-EXT-HEADER-FILTER-SET>"
        "</ELEMENTS>"
    )
    package = _package()
    parser.readARPackageElements(root, package)

    filter_set = package.getReferrableElement("FilterSet", IPv6ExtHeaderFilterSet)
    assert isinstance(filter_set, IPv6ExtHeaderFilterSet)
    filter_lists = filter_set.getExtHeaderFilterLists()
    assert len(filter_lists) == 1
    assert isinstance(filter_lists[0], IPv6ExtHeaderFilterList)
    assert filter_lists[0].getShortName() == "FilterList"
    headers = filter_lists[0].getAllowedIPv6ExtHeaders()
    assert len(headers) == 2
    assert headers[0].getValue() == 0
    assert headers[1].getValue() == 60


def test_read_ipv6_ext_header_filter_set_empty(parser):
    root = _snip("<ELEMENTS><I-PV-6-EXT-HEADER-FILTER-SET><SHORT-NAME>EmptySet</SHORT-NAME></I-PV-6-EXT-HEADER-FILTER-SET></ELEMENTS>")
    package = _package()
    parser.readARPackageElements(root, package)

    filter_set = package.getReferrableElement("EmptySet", IPv6ExtHeaderFilterSet)
    assert isinstance(filter_set, IPv6ExtHeaderFilterSet)
    assert filter_set.getExtHeaderFilterLists() == []
