import inspect

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.TcpOptionFilterSet import TcpOptionFilterList

CLASS_NOTE = """Permitted list for the filtering of TCP options."""


class TestTcpOptionFilterList:
    """Test cases for TcpOptionFilterList (Table 6.123, p.457)."""

    def test_initialization_defaults(self):
        obj = TcpOptionFilterList(None, "Obj")
        assert obj.getAllowedTcpOptions() == []

    def test_add_round_trip_and_none_noop(self):
        obj = TcpOptionFilterList(None, "Obj")
        assert obj.addAllowedTcpOption(7) is obj
        assert obj.getAllowedTcpOptions() == [7]
        obj.addAllowedTcpOption(None)
        assert obj.getAllowedTcpOptions() == [7]

    def test_class_docstring_note(self):
        assert inspect.cleandoc(TcpOptionFilterList.__doc__) == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        obj = TcpOptionFilterList(None, "Obj")
        n = "TCP option kind allowed by this filter."
        assert inspect.cleandoc(obj.getAllowedTcpOptions.__doc__) == n
        assert inspect.cleandoc(obj.addAllowedTcpOption.__doc__).split("\n")[0] == n
