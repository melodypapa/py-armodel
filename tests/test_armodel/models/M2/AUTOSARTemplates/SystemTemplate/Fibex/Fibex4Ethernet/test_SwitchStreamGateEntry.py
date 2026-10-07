"""
Test suite for SwitchStreamGateEntry (CP_TPS_SystemTemplate Table 3.97, p.143, R23-11).

Validates the member defaults, setter semantics (None no-ops), getter/setter
round-trips, the verbatim class-level spec Note and the member declaration
order (markdown displayed row order) of the SwitchStreamGateEntry
model class.
"""

import ast
import importlib
import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    SwitchStreamGateEntry,
)

CLASS_NOTE = "Defines a Asynchronous Traffic Shapter (ATS) Group for a switch. Tags: atp.Status=candidate"

INTERNAL_PRIORITY_VALUE_NOTE = "Internal Priority Value (IPV), a priority value that determines the assigned traffic class. Tags: atp.Status=candidate"


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class TestSwitchStreamGateEntry:
    def test_inheritance(self):
        assert issubclass(SwitchStreamGateEntry, Identifiable)

    def test_concrete_class_instantiable(self):
        stream_gate = SwitchStreamGateEntry(MockParent(), "Gate1")
        assert isinstance(stream_gate, Identifiable)
        assert stream_gate.getShortName() == "Gate1"
        assert stream_gate.getParent() is not None

    def test_class_docstring_note(self):
        assert inspect.cleandoc(SwitchStreamGateEntry.__doc__) == CLASS_NOTE

    def test_initialization(self):
        stream_gate = SwitchStreamGateEntry(MockParent(), "Gate1")

        assert stream_gate.getShortName() == "Gate1"
        assert stream_gate.getInternalPriorityValue() is None

    def test_member_annotations_and_declaration_order(self):
        module = importlib.import_module("armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology")
        module_source = open(module.__file__, encoding="utf-8").read()
        tree = ast.parse(module_source)
        cls = next(n for n in ast.walk(tree) if isinstance(n, ast.ClassDef) and n.name == "SwitchStreamGateEntry")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = [(st.target.attr, ast.get_source_segment(module_source, st.annotation)) for st in ast.walk(init) if isinstance(st, ast.AnnAssign)]

        assert annotations == [
            ("internalPriorityValue", "Optional[PositiveInteger]"),
        ]

    def test_member_accessor_type_hints(self):
        assert typing.get_type_hints(SwitchStreamGateEntry.getInternalPriorityValue).get("return") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(SwitchStreamGateEntry.setInternalPriorityValue).get("value") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(SwitchStreamGateEntry.setInternalPriorityValue).get("return") is SwitchStreamGateEntry

    def test_member_docstrings_are_verbatim_spec_notes(self):
        assert inspect.cleandoc(SwitchStreamGateEntry.getInternalPriorityValue.__doc__) == INTERNAL_PRIORITY_VALUE_NOTE
        assert (
            inspect.cleandoc(SwitchStreamGateEntry.setInternalPriorityValue.__doc__)
            == INTERNAL_PRIORITY_VALUE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing internalPriorityValue."
        )

    def test_get_set_internal_priority_value(self):
        stream_gate = SwitchStreamGateEntry(MockParent(), "Gate1")

        value = PositiveInteger().setValue("5")
        assert stream_gate.setInternalPriorityValue(value) is stream_gate
        assert stream_gate.getInternalPriorityValue() is value
        assert stream_gate.getInternalPriorityValue().getValue() == 5

        assert stream_gate.setInternalPriorityValue(None) is stream_gate
        assert stream_gate.getInternalPriorityValue() is value
