"""
Test suite for SwcTiming (CP_TPS_TimingExtensions Table 3.2, p.25, R23-11).

Validates the member defaults, getter/setter round-trips (None no-ops), the
verbatim class-level spec Note and the member declaration order (markdown
displayed row order) of the SwcTiming model class.
"""

import ast
import importlib
import inspect
import typing

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions import SwcTiming, TimingExtension
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

CLASS_NOTE = (
    "The SwcTiming is used to describe the timing of an atomic software component. "
    "TimingDescriptions aggregated by SwcTiming are restricted to event chains referring to events "
    "which are derived from the classes TDEventVfb and TDEventSwcInternalBehavior. "
    "Tags: atp.recommendedPackage=TimingExtensions"
)

BEHAVIOR_NOTE = (
    "This defines the scope of a SwcTiming. All corresponding timing descriptions and constraints "
    "shall be defined within this scope. Note! The reason for the cardinality of 0..1 is to ensure "
    "backward compatibility."
)


class TestSwcTiming:
    def _create_timing(self) -> SwcTiming:
        return SwcTiming(AUTOSAR.getInstance(), "SwcTiming1")

    def test_inheritance(self):
        assert issubclass(SwcTiming, TimingExtension)

    def test_concrete_class_instantiable(self):
        timing = self._create_timing()
        assert isinstance(timing, TimingExtension)
        assert timing.getShortName() == "SwcTiming1"

    def test_class_docstring_note(self):
        assert inspect.cleandoc(SwcTiming.__doc__) == CLASS_NOTE

    def test_initialization(self):
        timing = self._create_timing()

        assert timing.getShortName() == "SwcTiming1"
        assert timing.getBehaviorRef() is None

    def test_member_annotations_and_declaration_order(self):
        module = importlib.import_module("armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions")
        module_source = open(module.__file__, encoding="utf-8").read()
        tree = ast.parse(module_source)
        cls = next(n for n in ast.walk(tree) if isinstance(n, ast.ClassDef) and n.name == "SwcTiming")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = [(st.target.attr, ast.get_source_segment(module_source, st.annotation)) for st in ast.walk(init) if isinstance(st, ast.AnnAssign)]

        assert annotations == [
            ("behaviorRef", "Optional[RefType]"),
        ]

    def test_member_accessor_type_hints(self):
        assert typing.get_type_hints(SwcTiming.getBehaviorRef).get("return") == typing.Optional[RefType]
        assert typing.get_type_hints(SwcTiming.setBehaviorRef).get("value") == typing.Optional[RefType]
        assert typing.get_type_hints(SwcTiming.setBehaviorRef).get("return") is SwcTiming

    def test_member_docstrings_are_verbatim_spec_notes(self):
        assert inspect.cleandoc(SwcTiming.getBehaviorRef.__doc__) == BEHAVIOR_NOTE
        assert inspect.cleandoc(SwcTiming.setBehaviorRef.__doc__) == BEHAVIOR_NOTE + "\n\nA None value is a no-op and does not overwrite an existing behaviorRef."

    def test_get_set_behavior_ref(self):
        timing = self._create_timing()

        value = RefType().setDest("SWC-INTERNAL-BEHAVIOR").setValue("/Swc/InternalBehavior/Behav1")
        assert timing.setBehaviorRef(value) is timing
        assert timing.getBehaviorRef() is value
        assert timing.getBehaviorRef().getValue() == "/Swc/InternalBehavior/Behav1"
        assert timing.getBehaviorRef().getDest() == "SWC-INTERNAL-BEHAVIOR"

        assert timing.setBehaviorRef(None) is timing
        assert timing.getBehaviorRef() is value
