"""
Test suite for StreamFilterPortRange (CP_TPS_SystemTemplate Table 3.91, p.139, R23-11).

Validates the member defaults, getter/setter round-trips (None no-ops), the
verbatim class-level spec Note and the member declaration order (markdown
displayed row order) of the StreamFilterPortRange model class.
"""

import ast
import importlib
import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    StreamFilterPortRange,
)

CLASS_NOTE = "Configuration of filter rules for IP and TP. Tags: atp.Status=candidate"

MAX_NOTE = "Filter to match packets with the maximum UDP/TCP port number. Tags: atp.Status=candidate"
MIN_NOTE = "Filter to match packets with the minimum UDP/TCP port number. Tags: atp.Status=candidate"


class TestStreamFilterPortRange:
    def test_inheritance(self):
        assert issubclass(StreamFilterPortRange, ARObject)

    def test_concrete_class_instantiable(self):
        port_range = StreamFilterPortRange()
        assert isinstance(port_range, ARObject)

    def test_class_docstring_note(self):
        assert inspect.cleandoc(StreamFilterPortRange.__doc__) == CLASS_NOTE

    def test_initialization(self):
        port_range = StreamFilterPortRange()

        assert port_range.getMax() is None
        assert port_range.getMin() is None

    def test_member_annotations_and_declaration_order(self):
        module = importlib.import_module("armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology")
        module_source = open(module.__file__, encoding="utf-8").read()
        tree = ast.parse(module_source)
        cls = next(n for n in ast.walk(tree) if isinstance(n, ast.ClassDef) and n.name == "StreamFilterPortRange")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = [(st.target.attr, ast.get_source_segment(module_source, st.annotation)) for st in ast.walk(init) if isinstance(st, ast.AnnAssign)]

        assert annotations == [
            ("max", "Optional[PositiveInteger]"),
            ("min", "Optional[PositiveInteger]"),
        ]

    def test_member_accessor_type_hints(self):
        assert typing.get_type_hints(StreamFilterPortRange.getMax).get("return") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(StreamFilterPortRange.setMax).get("value") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(StreamFilterPortRange.setMax).get("return") is StreamFilterPortRange
        assert typing.get_type_hints(StreamFilterPortRange.getMin).get("return") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(StreamFilterPortRange.setMin).get("value") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(StreamFilterPortRange.setMin).get("return") is StreamFilterPortRange

    def test_member_docstrings_are_verbatim_spec_notes(self):
        assert inspect.cleandoc(StreamFilterPortRange.getMax.__doc__) == MAX_NOTE
        assert inspect.cleandoc(StreamFilterPortRange.setMax.__doc__) == MAX_NOTE + "\n\nA None value is a no-op and does not overwrite an existing max."
        assert inspect.cleandoc(StreamFilterPortRange.getMin.__doc__) == MIN_NOTE
        assert inspect.cleandoc(StreamFilterPortRange.setMin.__doc__) == MIN_NOTE + "\n\nA None value is a no-op and does not overwrite an existing min."

    def test_get_set_max(self):
        port_range = StreamFilterPortRange()

        value = PositiveInteger().setValue("65535")
        assert port_range.setMax(value) is port_range
        assert port_range.getMax() is value
        assert port_range.getMax().getValue() == 65535

        assert port_range.setMax(None) is port_range
        assert port_range.getMax() is value

    def test_get_set_min(self):
        port_range = StreamFilterPortRange()

        value = PositiveInteger().setValue("1024")
        assert port_range.setMin(value) is port_range
        assert port_range.getMin() is value
        assert port_range.getMin().getValue() == 1024

        assert port_range.setMin(None) is port_range
        assert port_range.getMin() is value
