"""
Test suite for StreamFilterIEEE1722Tp (CP_TPS_SystemTemplate Table 3.92, p.139, R23-11).

Validates the member defaults, getter/setter round-trips (None no-ops), the
verbatim class-level spec Note and the member declaration order (markdown
displayed row order) of the StreamFilterIEEE1722Tp model class.
"""

import ast
import importlib
import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveUnlimitedInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    StreamFilterIEEE1722Tp,
)

CLASS_NOTE = "Configuration of filter rules for IP and TP. Tags: atp.Status=candidate"

STREAM_ID_NOTE = "Filter to match IEEE1722Tp packets with the stream Id number. Defined as 64bit stream id. Tags: atp.Status=candidate"


class TestStreamFilterIEEE1722Tp:
    def test_inheritance(self):
        assert issubclass(StreamFilterIEEE1722Tp, ARObject)

    def test_concrete_class_instantiable(self):
        tp_rule = StreamFilterIEEE1722Tp()
        assert isinstance(tp_rule, ARObject)

    def test_class_docstring_note(self):
        assert inspect.cleandoc(StreamFilterIEEE1722Tp.__doc__) == CLASS_NOTE

    def test_initialization(self):
        tp_rule = StreamFilterIEEE1722Tp()

        assert tp_rule.getStreamId() is None

    def test_member_annotations_and_declaration_order(self):
        module = importlib.import_module("armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology")
        module_source = open(module.__file__, encoding="utf-8").read()
        tree = ast.parse(module_source)
        cls = next(n for n in ast.walk(tree) if isinstance(n, ast.ClassDef) and n.name == "StreamFilterIEEE1722Tp")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = [(st.target.attr, ast.get_source_segment(module_source, st.annotation)) for st in ast.walk(init) if isinstance(st, ast.AnnAssign)]

        assert annotations == [
            ("streamId", "Optional[PositiveUnlimitedInteger]"),
        ]

    def test_member_accessor_type_hints(self):
        assert typing.get_type_hints(StreamFilterIEEE1722Tp.getStreamId).get("return") == typing.Optional[PositiveUnlimitedInteger]
        assert typing.get_type_hints(StreamFilterIEEE1722Tp.setStreamId).get("value") == typing.Optional[PositiveUnlimitedInteger]
        assert typing.get_type_hints(StreamFilterIEEE1722Tp.setStreamId).get("return") is StreamFilterIEEE1722Tp

    def test_member_docstrings_are_verbatim_spec_notes(self):
        assert inspect.cleandoc(StreamFilterIEEE1722Tp.getStreamId.__doc__) == STREAM_ID_NOTE
        assert inspect.cleandoc(StreamFilterIEEE1722Tp.setStreamId.__doc__) == STREAM_ID_NOTE + "\n\nA None value is a no-op and does not overwrite an existing streamId."

    def test_get_set_stream_id(self):
        tp_rule = StreamFilterIEEE1722Tp()

        value = PositiveUnlimitedInteger().setValue("0x0102030405060708")
        assert tp_rule.setStreamId(value) is tp_rule
        assert tp_rule.getStreamId() is value
        assert tp_rule.getStreamId().getValue() == 0x0102030405060708

        assert tp_rule.setStreamId(None) is tp_rule
        assert tp_rule.getStreamId() is value
