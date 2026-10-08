"""
Test suite for BswCompositionTiming (CP_TPS_TimingExtensions Table 3.5, p.29, R23-11).

Validates the member defaults, getter/adder round-trips (None no-ops), the
verbatim class-level spec Note and the member declaration order (markdown
displayed row order) of the BswCompositionTiming model class.
"""

import ast
import importlib
import inspect
import typing

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions import BswCompositionTiming, TimingExtension
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

CLASS_NOTE = (
    "A model element used to define timing descriptions and constraints for a set of BswImplementations representing "
    "a BSW composition. A constraint defined at this level holds true for all referenced BswImplementations. Note, "
    "that multiple implementations of the same basic software module could be involved. TimingDescriptions aggregated "
    "by BswCompositionTiming are restricted to event chains referring to events which are derived from the class "
    "TDEventBswInternalBehavior and TDEventBsw. Tags: atp.recommendedPackage=TimingExtensions"
)

IMPLEMENTATION_NOTE = "This defines the scope of a BswCompositionTiming. All corresponding timing descriptions and constraints shall be defined within this scope."


class TestBswCompositionTiming:
    def _create_timing(self) -> BswCompositionTiming:
        return BswCompositionTiming(AUTOSAR.getInstance(), "BswCompositionTiming1")

    def test_inheritance(self):
        assert issubclass(BswCompositionTiming, TimingExtension)

    def test_concrete_class_instantiable(self):
        timing = self._create_timing()
        assert isinstance(timing, TimingExtension)
        assert timing.getShortName() == "BswCompositionTiming1"

    def test_class_docstring_note(self):
        assert inspect.cleandoc(BswCompositionTiming.__doc__) == CLASS_NOTE

    def test_initialization(self):
        timing = self._create_timing()

        assert timing.getShortName() == "BswCompositionTiming1"
        assert timing.getImplementationRefs() == []

    def test_member_annotations_and_declaration_order(self):
        module = importlib.import_module("armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions")
        module_source = open(module.__file__, encoding="utf-8").read()
        tree = ast.parse(module_source)
        cls = next(n for n in ast.walk(tree) if isinstance(n, ast.ClassDef) and n.name == "BswCompositionTiming")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = [(st.target.attr, ast.get_source_segment(module_source, st.annotation)) for st in ast.walk(init) if isinstance(st, ast.AnnAssign)]

        assert annotations == [
            ("implementationRefs", "List[RefType]"),
        ]

    def test_member_accessor_type_hints(self):
        assert typing.get_type_hints(BswCompositionTiming.addImplementationRef).get("value") == typing.Optional[RefType]
        assert typing.get_type_hints(BswCompositionTiming.addImplementationRef).get("return") is BswCompositionTiming
        assert typing.get_type_hints(BswCompositionTiming.getImplementationRefs).get("return") == typing.List[RefType]

    def test_member_docstrings_are_verbatim_spec_notes(self):
        assert inspect.cleandoc(BswCompositionTiming.addImplementationRef.__doc__) == IMPLEMENTATION_NOTE
        assert inspect.cleandoc(BswCompositionTiming.getImplementationRefs.__doc__) == IMPLEMENTATION_NOTE

    def test_add_implementation_refs(self):
        timing = self._create_timing()

        ref1 = RefType().setDest("BSW-IMPLEMENTATION").setValue("/BswImplementations/Impl1")
        ref2 = RefType().setDest("BSW-IMPLEMENTATION").setValue("/BswImplementations/Impl2")
        assert timing.addImplementationRef(ref1) is timing
        assert timing.addImplementationRef(ref2) is timing
        assert timing.getImplementationRefs() == [ref1, ref2]

        assert timing.addImplementationRef(None) is timing
        assert timing.getImplementationRefs() == [ref1, ref2]
