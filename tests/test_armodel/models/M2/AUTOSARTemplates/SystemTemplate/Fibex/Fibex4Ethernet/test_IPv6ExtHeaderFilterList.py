import ast
import inspect
import sys
import typing

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

    def test_no_quoted_top_level_annotations(self):
        module = sys.modules[IPv6ExtHeaderFilterList.__module__]
        tree = ast.parse(inspect.getsource(module))
        quoted = []
        for node in ast.walk(tree):
            if not isinstance(node, ast.FunctionDef):
                continue
            params = list(node.args.args) + list(node.args.posonlyargs) + list(node.args.kwonlyargs)
            annotations = [p.annotation for p in params if p.annotation is not None]
            if node.returns is not None:
                annotations.append(node.returns)
            for annotation in annotations:
                if isinstance(annotation, ast.Constant) and isinstance(annotation.value, str):
                    quoted.append(node.name)
        assert quoted == []

    def test_add_accessor_return_type_resolves_to_class(self):
        hints = typing.get_type_hints(IPv6ExtHeaderFilterList.addAllowedIPv6ExtHeader)
        assert hints["return"] is IPv6ExtHeaderFilterList
