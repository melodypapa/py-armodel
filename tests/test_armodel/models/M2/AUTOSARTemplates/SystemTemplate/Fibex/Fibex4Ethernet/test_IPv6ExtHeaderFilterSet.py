import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.IPv6HeaderFilterList import (
    IPv6ExtHeaderFilterList,
    IPv6ExtHeaderFilterSet,
)

CLASS_NOTE = """Set of IPv6 Extension Header Filters. Tags: atp.recommendedPackage=IPv6ExtHeaderFilterSets"""

LIST_NOTE = "In order to permit or deny certain types of IPv6 extension headers a permitted list of IPv6 extension headers can be configured."


class TestIPv6ExtHeaderFilterSet:
    """Test cases for IPv6ExtHeaderFilterSet (Table 6.120, p.455)."""

    def test_create_ext_header_filter_list(self):
        filter_set = IPv6ExtHeaderFilterSet(None, "Set")
        filter_list = filter_set.createExtHeaderFilterList("list1")
        assert isinstance(filter_list, IPv6ExtHeaderFilterList)
        assert filter_set.getExtHeaderFilterLists() == [filter_list]
        assert filter_set.createExtHeaderFilterList("list1") is filter_list

    def test_initialization_defaults(self):
        filter_set = IPv6ExtHeaderFilterSet(None, "Set")
        assert filter_set.getExtHeaderFilterLists() == []

    def test_inheritance(self):
        filter_set = IPv6ExtHeaderFilterSet(None, "Set")
        assert isinstance(filter_set, ARElement)

    def test_class_docstring_note(self):
        assert inspect.cleandoc(IPv6ExtHeaderFilterSet.__doc__) == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        filter_set = IPv6ExtHeaderFilterSet(None, "Set")
        assert inspect.cleandoc(filter_set.getExtHeaderFilterLists.__doc__) == LIST_NOTE
        assert inspect.cleandoc(filter_set.createExtHeaderFilterList.__doc__).split("\n")[0] == LIST_NOTE
