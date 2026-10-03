import ast
import inspect
import sys
import typing

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

    def test_no_quoted_top_level_annotations(self):
        module = sys.modules[TcpOptionFilterList.__module__]
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
        hints = typing.get_type_hints(TcpOptionFilterList.addAllowedTcpOption)
        assert hints["return"] is TcpOptionFilterList

    def test_list_pair_is_mutator_first_in_source(self):
        module = sys.modules[TcpOptionFilterList.__module__]
        tree = ast.parse(inspect.getsource(module))
        cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "TcpOptionFilterList")
        methods = [n.name for n in cls.body if isinstance(n, ast.FunctionDef)]
        assert methods.index("addAllowedTcpOption") < methods.index("getAllowedTcpOptions")
