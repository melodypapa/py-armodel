import inspect

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.IPv6HeaderFilterList import IPv6ExtHeaderFilterList

CLASS_NOTE = """Permitted list for the filtering of IPv6 extension headers."""


class TestIPv6ExtHeaderFilterList:
    """Test cases for IPv6ExtHeaderFilterList (Table 6.121, p.456)."""

    def test_initialization_defaults(self):
        obj = IPv6ExtHeaderFilterList(None, "Obj")
        assert obj.getAllowedIPv6ExtHeaders() == []

    def test_add_round_trip_and_none_noop(self):
        obj = IPv6ExtHeaderFilterList(None, "Obj")
        assert obj.addAllowedIPv6ExtHeader(7) is obj
        assert obj.getAllowedIPv6ExtHeaders() == [7]
        obj.addAllowedIPv6ExtHeader(None)
        assert obj.getAllowedIPv6ExtHeaders() == [7]

    def test_class_docstring_note(self):
        assert inspect.cleandoc(IPv6ExtHeaderFilterList.__doc__) == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        obj = IPv6ExtHeaderFilterList(None, "Obj")
        n = "IPv6 Extension Header type allowed by this filter."
        assert inspect.cleandoc(obj.getAllowedIPv6ExtHeaders.__doc__) == n
        assert inspect.cleandoc(obj.addAllowedIPv6ExtHeader.__doc__).split("\n")[0] == n
