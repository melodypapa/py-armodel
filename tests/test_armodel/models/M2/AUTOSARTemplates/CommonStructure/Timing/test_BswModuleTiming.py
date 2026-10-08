"""
Test suite for BswModuleTiming (CP_TPS_TimingExtensions Table 3.4, p.28, R23-11).

Validates the member defaults, getter/setter round-trips (None no-ops), the
verbatim class-level spec Note and the member declaration order (markdown
displayed row order) of the BswModuleTiming model class.
"""

import ast
import importlib
import inspect
import typing

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions import BswModuleTiming, TimingExtension
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

CLASS_NOTE = (
    "A model element used to define timing descriptions and constraints for the BswInternalBehavior of one BSW Module. "
    "Thereby, for each BswInternalBehavior a separate timing can be specified. A constraint defined at this level holds "
    "true for all Implementations of that BswInternalBehavior. TimingDescriptions aggregated by BswModuleTiming are "
    "restricted to event chains referring to events which are derived from the class TDEventBswInternalBehavior. "
    "Tags: atp.recommendedPackage=TimingExtensions"
)

BEHAVIOR_NOTE = "This defines the scope of a BswModuleTiming. All corresponding timing descriptions and constraints shall be defined within this scope."


class TestBswModuleTiming:
    def _create_timing(self) -> BswModuleTiming:
        return BswModuleTiming(AUTOSAR.getInstance(), "BswModuleTiming1")

    def test_inheritance(self):
        assert issubclass(BswModuleTiming, TimingExtension)

    def test_concrete_class_instantiable(self):
        timing = self._create_timing()
        assert isinstance(timing, TimingExtension)
        assert timing.getShortName() == "BswModuleTiming1"

    def test_class_docstring_note(self):
        assert inspect.cleandoc(BswModuleTiming.__doc__) == CLASS_NOTE

    def test_initialization(self):
        timing = self._create_timing()

        assert timing.getShortName() == "BswModuleTiming1"
        assert timing.getBehaviorRef() is None

    def test_member_annotations_and_declaration_order(self):
        module = importlib.import_module("armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions")
        module_source = open(module.__file__, encoding="utf-8").read()
        tree = ast.parse(module_source)
        cls = next(n for n in ast.walk(tree) if isinstance(n, ast.ClassDef) and n.name == "BswModuleTiming")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = [(st.target.attr, ast.get_source_segment(module_source, st.annotation)) for st in ast.walk(init) if isinstance(st, ast.AnnAssign)]

        assert annotations == [
            ("behaviorRef", "Optional[RefType]"),
        ]

    def test_member_accessor_type_hints(self):
        assert typing.get_type_hints(BswModuleTiming.getBehaviorRef).get("return") == typing.Optional[RefType]
        assert typing.get_type_hints(BswModuleTiming.setBehaviorRef).get("value") == typing.Optional[RefType]
        assert typing.get_type_hints(BswModuleTiming.setBehaviorRef).get("return") is BswModuleTiming

    def test_member_docstrings_are_verbatim_spec_notes(self):
        assert inspect.cleandoc(BswModuleTiming.getBehaviorRef.__doc__) == BEHAVIOR_NOTE
        assert inspect.cleandoc(BswModuleTiming.setBehaviorRef.__doc__) == BEHAVIOR_NOTE + "\n\nA None value is a no-op and does not overwrite an existing behaviorRef."

    def test_get_set_behavior_ref(self):
        timing = self._create_timing()

        value = RefType().setDest("BSW-INTERNAL-BEHAVIOR").setValue("/BswModule/InternalBehavior/Behav1")
        assert timing.setBehaviorRef(value) is timing
        assert timing.getBehaviorRef() is value
        assert timing.getBehaviorRef().getValue() == "/BswModule/InternalBehavior/Behav1"
        assert timing.getBehaviorRef().getDest() == "BSW-INTERNAL-BEHAVIOR"

        assert timing.setBehaviorRef(None) is timing
        assert timing.getBehaviorRef() is value
