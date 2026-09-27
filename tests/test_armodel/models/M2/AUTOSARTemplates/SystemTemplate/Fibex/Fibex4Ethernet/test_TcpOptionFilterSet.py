import inspect

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.TcpOptionFilterSet import (
    TcpOptionFilterList,
    TcpOptionFilterSet,
)

CLASS_NOTE = """Set of TcpOptionFilterLists. Tags: atp.recommendedPackage=TcpOptionFilterSets"""


class TestTcpOptionFilterSet:
    """Test cases for TcpOptionFilterSet (Table 6.122, p.457)."""

    def test_create_tcp_option_filter_list(self):
        filter_set = TcpOptionFilterSet(None, "Set")
        filter_list = filter_set.createTcpOptionFilterList("list1")
        assert isinstance(filter_list, TcpOptionFilterList)
        assert filter_set.getTcpOptionFilterLists() == [filter_list]
        assert filter_set.createTcpOptionFilterList("list1") is filter_list

    def test_class_docstring_note(self):
        assert inspect.cleandoc(TcpOptionFilterSet.__doc__) == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        filter_set = TcpOptionFilterSet(None, "Set")
        n = "Collection of permitted lists for the filtering of TCP options."
        assert inspect.cleandoc(filter_set.getTcpOptionFilterLists.__doc__).split("\n")[0] == n
        assert inspect.cleandoc(filter_set.createTcpOptionFilterList.__doc__).split("\n")[0] == n
