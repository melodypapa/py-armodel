"""
Test suite for VfbTiming (CP_TPS_TimingExtensions Table 3.1, p.24, R23-11).

Validates the member defaults, getter/setter round-trips (None no-ops), the
verbatim class-level spec Note and the member declaration order (markdown
displayed row order) of the VfbTiming model class.
"""

import ast
import importlib
import inspect
import typing

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions import TimingExtension, VfbTiming
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

CLASS_NOTE = (
    "A model element used to define timing descriptions and constraints at VFB level. "
    "TimingDescriptions aggregated by VfbTiming are restricted to event chains referring to events "
    "which are derived from the class TDEventVfb. Tags: atp.recommendedPackage=TimingExtensions"
)

COMPONENT_NOTE = "This defines the scope of a VfbTiming. All corresponding timing descriptions and constraints shall be defined within this scope."


class TestVfbTiming:
    def _create_timing(self) -> VfbTiming:
        return VfbTiming(AUTOSAR.getInstance(), "VfbTiming1")

    def test_inheritance(self):
        assert issubclass(VfbTiming, TimingExtension)

    def test_concrete_class_instantiable(self):
        timing = self._create_timing()
        assert isinstance(timing, TimingExtension)
        assert timing.getShortName() == "VfbTiming1"

    def test_class_docstring_note(self):
        assert inspect.cleandoc(VfbTiming.__doc__) == CLASS_NOTE

    def test_initialization(self):
        timing = self._create_timing()

        assert timing.getShortName() == "VfbTiming1"
        assert timing.getComponentRef() is None

    def test_member_annotations_and_declaration_order(self):
        module = importlib.import_module("armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions")
        module_source = open(module.__file__, encoding="utf-8").read()
        tree = ast.parse(module_source)
        cls = next(n for n in ast.walk(tree) if isinstance(n, ast.ClassDef) and n.name == "VfbTiming")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = [(st.target.attr, ast.get_source_segment(module_source, st.annotation)) for st in ast.walk(init) if isinstance(st, ast.AnnAssign)]

        assert annotations == [
            ("componentRef", "Optional[RefType]"),
        ]

    def test_member_accessor_type_hints(self):
        assert typing.get_type_hints(VfbTiming.getComponentRef).get("return") == typing.Optional[RefType]
        assert typing.get_type_hints(VfbTiming.setComponentRef).get("value") == typing.Optional[RefType]
        assert typing.get_type_hints(VfbTiming.setComponentRef).get("return") is VfbTiming

    def test_member_docstrings_are_verbatim_spec_notes(self):
        assert inspect.cleandoc(VfbTiming.getComponentRef.__doc__) == COMPONENT_NOTE
        assert inspect.cleandoc(VfbTiming.setComponentRef.__doc__) == COMPONENT_NOTE + "\n\nA None value is a no-op and does not overwrite an existing componentRef."

    def test_get_set_component_ref(self):
        timing = self._create_timing()

        value = RefType().setDest("SW-COMPONENT-TYPE").setValue("/SwComponentTypes/MySwc")
        assert timing.setComponentRef(value) is timing
        assert timing.getComponentRef() is value
        assert timing.getComponentRef().getValue() == "/SwComponentTypes/MySwc"
        assert timing.getComponentRef().getDest() == "SW-COMPONENT-TYPE"

        assert timing.setComponentRef(None) is timing
        assert timing.getComponentRef() is value

    def test_arpackage_create_vfb_timing(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage

        package = ARPackage(AUTOSAR.getInstance(), "Timing")
        timing = package.createVfbTiming("VfbTiming1")

        assert isinstance(timing, VfbTiming)
        assert package.getReferrableElement("VfbTiming1", VfbTiming) is timing
