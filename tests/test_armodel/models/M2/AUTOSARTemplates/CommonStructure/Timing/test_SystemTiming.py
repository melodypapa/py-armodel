"""
Test suite for SystemTiming (CP_TPS_TimingExtensions Table 3.3, p.27, R23-11).

Validates the member defaults, getter/setter round-trips (None no-ops), the
verbatim class-level spec Note and the member declaration order (markdown
displayed row order) of the SystemTiming model class.
"""

import ast
import importlib
import inspect
import typing

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions import SwcTiming, SystemTiming, TimingExtension
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

CLASS_NOTE = (
    "A model element used to refine timing descriptions and constraints (from a VfbTiming) at System level, "
    "utilizing information about topology, software deployment, and signal mapping described in the System Template. "
    "TimingDescriptions aggregated by SystemTiming are restricted to events which are derived from the class "
    "TDEventVfb, TDEventSwcInternalBehavior and TDEventCom. Tags: atp.recommendedPackage=TimingExtensions"
)

SYSTEM_NOTE = "This defines the scope of a SystemTiming. All corresponding timing descriptions and constraints shall be defined within this scope."


class TestSystemTiming:
    def _create_timing(self) -> SystemTiming:
        return SystemTiming(AUTOSAR.getInstance(), "SystemTiming1")

    def test_inheritance(self):
        assert issubclass(SystemTiming, TimingExtension)

    def test_concrete_class_instantiable(self):
        timing = self._create_timing()
        assert isinstance(timing, TimingExtension)
        assert timing.getShortName() == "SystemTiming1"

    def test_class_docstring_note(self):
        assert inspect.cleandoc(SystemTiming.__doc__) == CLASS_NOTE

    def test_initialization(self):
        timing = self._create_timing()

        assert timing.getShortName() == "SystemTiming1"
        assert timing.getSystemRef() is None

    def test_member_annotations_and_declaration_order(self):
        module = importlib.import_module("armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions")
        module_source = open(module.__file__, encoding="utf-8").read()
        tree = ast.parse(module_source)
        cls = next(n for n in ast.walk(tree) if isinstance(n, ast.ClassDef) and n.name == "SystemTiming")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = [(st.target.attr, ast.get_source_segment(module_source, st.annotation)) for st in ast.walk(init) if isinstance(st, ast.AnnAssign)]

        assert annotations == [
            ("systemRef", "Optional[RefType]"),
        ]

    def test_member_accessor_type_hints(self):
        assert typing.get_type_hints(SystemTiming.getSystemRef).get("return") == typing.Optional[RefType]
        assert typing.get_type_hints(SystemTiming.setSystemRef).get("value") == typing.Optional[RefType]
        assert typing.get_type_hints(SystemTiming.setSystemRef).get("return") is SystemTiming

    def test_member_docstrings_are_verbatim_spec_notes(self):
        assert inspect.cleandoc(SystemTiming.getSystemRef.__doc__) == SYSTEM_NOTE
        assert inspect.cleandoc(SystemTiming.setSystemRef.__doc__) == SYSTEM_NOTE + "\n\nA None value is a no-op and does not overwrite an existing systemRef."

    def test_get_set_system_ref(self):
        timing = self._create_timing()

        value = RefType().setDest("SYSTEM").setValue("/Systems/MySystem")
        assert timing.setSystemRef(value) is timing
        assert timing.getSystemRef() is value
        assert timing.getSystemRef().getValue() == "/Systems/MySystem"
        assert timing.getSystemRef().getDest() == "SYSTEM"

        assert timing.setSystemRef(None) is timing
        assert timing.getSystemRef() is value

    def test_sibling_timing_extensions_distinct(self):
        package = AUTOSAR.getInstance().createARPackage("Timing")

        system_timing = package.createSystemTiming("SystemTiming1")
        swc_timing = package.createSwcTiming("SwcTiming1")

        assert isinstance(system_timing, SystemTiming)
        assert not isinstance(system_timing, SwcTiming)
        assert isinstance(swc_timing, SwcTiming)
