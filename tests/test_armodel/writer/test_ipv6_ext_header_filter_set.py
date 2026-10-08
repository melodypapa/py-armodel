"""Writer round-trip tests for IPv6ExtHeaderFilterSet (Table 6.120, p.455):
the ARPackage ELEMENTS choice serializes the ARElement subclass.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.IPv6HeaderFilterList import (
    IPv6ExtHeaderFilterSet,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _new_filter_set():
    filter_set = IPv6ExtHeaderFilterSet(None, "FilterSet")
    filter_list = filter_set.createExtHeaderFilterList("FilterList")
    filter_list.addAllowedIPv6ExtHeader(PositiveInteger().setValue("0"))
    filter_list.addAllowedIPv6ExtHeader(PositiveInteger().setValue("60"))
    return filter_set


class TestWriteIPv6ExtHeaderFilterSet:
    def test_write_ipv6_ext_header_filter_set(self):
        package = AUTOSAR.getInstance().createARPackage("Pkg")
        package.addReferrableElement(_new_filter_set())
        parent = ET.Element("PARENT")
        ARXMLWriter().writeARPackageElements(parent, package)

        node = parent.find("ELEMENTS/I-PV-6-EXT-HEADER-FILTER-SET")
        assert node is not None
        assert node.find("SHORT-NAME").text == "FilterSet"
        lists_node = node.find("EXT-HEADER-FILTER-LISTS")
        assert lists_node is not None
        filter_list_node = lists_node.find("I-PV-6-EXT-HEADER-FILTER-LIST")
        assert filter_list_node is not None
        assert filter_list_node.find("SHORT-NAME").text == "FilterList"
        headers = filter_list_node.findall("ALLOWED-I-PV-6-EXT-HEADERS/ALLOWED-I-PV-6-EXT-HEADER")
        assert [h.text for h in headers] == ["0", "60"]

    def test_write_ipv6_ext_header_filter_set_empty_omits_wrapper(self):
        package = AUTOSAR.getInstance().createARPackage("Pkg")
        package.addReferrableElement(IPv6ExtHeaderFilterSet(None, "EmptySet"))
        parent = ET.Element("PARENT")
        ARXMLWriter().writeARPackageElements(parent, package)

        node = parent.find("ELEMENTS/I-PV-6-EXT-HEADER-FILTER-SET")
        assert node is not None
        assert node.find("EXT-HEADER-FILTER-LISTS") is None

    def test_round_trip_ipv6_ext_header_filter_set_preserves_values(self):
        package = AUTOSAR.getInstance().createARPackage("Pkg")
        package.addReferrableElement(_new_filter_set())
        parent = ET.Element("PARENT")
        ARXMLWriter().writeARPackageElements(parent, package)
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring(inner.replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))

        reloaded_package = AUTOSAR.getInstance().createARPackage("Pkg2")
        ARXMLParser().readARPackageElements(root, reloaded_package)

        filter_set = reloaded_package.getReferrableElement("FilterSet", IPv6ExtHeaderFilterSet)
        assert isinstance(filter_set, IPv6ExtHeaderFilterSet)
        filter_lists = filter_set.getExtHeaderFilterLists()
        assert len(filter_lists) == 1
        assert filter_lists[0].getShortName() == "FilterList"
        headers = filter_lists[0].getAllowedIPv6ExtHeaders()
        assert len(headers) == 2
        assert headers[0].getValue() == 0
        assert headers[1].getValue() == 60
