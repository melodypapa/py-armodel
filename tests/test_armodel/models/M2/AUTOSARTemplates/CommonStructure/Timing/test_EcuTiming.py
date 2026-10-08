"""
Test suite for EcuTiming (CP_TPS_TimingExtensions Table 3.6, p.30, R23-11).

Validates the member defaults, getter/setter round-trips (None no-ops), the
verbatim class-level spec Note and the member declaration order (markdown
displayed row order) of the EcuTiming model class.
"""

import ast
import importlib
import inspect
import typing

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions import EcuTiming, TimingExtension
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

CLASS_NOTE = (
    "A model element used to define timing descriptions and constraints within the scope of one ECU configuration. "
    "TimingDescriptions aggregated by EcuTiming are allowed to use all events derived from the class "
    "TimingDescriptionEvent. Tags: atp.recommendedPackage=TimingExtensions"
)

ECU_CONFIGURATION_NOTE = "This defines the scope of an EcuTiming. All corresponding timing descriptions and constraints shall be defined within this scope."


class TestEcuTiming:
    def _create_timing(self) -> EcuTiming:
        return EcuTiming(AUTOSAR.getInstance(), "EcuTiming1")

    def test_inheritance(self):
        assert issubclass(EcuTiming, TimingExtension)

    def test_concrete_class_instantiable(self):
        timing = self._create_timing()
        assert isinstance(timing, TimingExtension)
        assert timing.getShortName() == "EcuTiming1"

    def test_class_docstring_note(self):
        assert inspect.cleandoc(EcuTiming.__doc__) == CLASS_NOTE

    def test_initialization(self):
        timing = self._create_timing()

        assert timing.getShortName() == "EcuTiming1"
        assert timing.getEcuConfigurationRef() is None

    def test_member_annotations_and_declaration_order(self):
        module = importlib.import_module("armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions")
        module_source = open(module.__file__, encoding="utf-8").read()
        tree = ast.parse(module_source)
        cls = next(n for n in ast.walk(tree) if isinstance(n, ast.ClassDef) and n.name == "EcuTiming")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = [(st.target.attr, ast.get_source_segment(module_source, st.annotation)) for st in ast.walk(init) if isinstance(st, ast.AnnAssign)]

        assert annotations == [
            ("ecuConfigurationRef", "Optional[RefType]"),
        ]

    def test_member_accessor_type_hints(self):
        assert typing.get_type_hints(EcuTiming.getEcuConfigurationRef).get("return") == typing.Optional[RefType]
        assert typing.get_type_hints(EcuTiming.setEcuConfigurationRef).get("value") == typing.Optional[RefType]
        assert typing.get_type_hints(EcuTiming.setEcuConfigurationRef).get("return") is EcuTiming

    def test_member_docstrings_are_verbatim_spec_notes(self):
        assert inspect.cleandoc(EcuTiming.getEcuConfigurationRef.__doc__) == ECU_CONFIGURATION_NOTE
        assert inspect.cleandoc(EcuTiming.setEcuConfigurationRef.__doc__) == ECU_CONFIGURATION_NOTE + "\n\nA None value is a no-op and does not overwrite an existing ecuConfigurationRef."

    def test_get_set_ecu_configuration_ref(self):
        timing = self._create_timing()

        value = RefType().setDest("ECUC-VALUE-COLLECTION").setValue("/EcuExtract/EcuConfigValues")
        assert timing.setEcuConfigurationRef(value) is timing
        assert timing.getEcuConfigurationRef() is value
        assert timing.getEcuConfigurationRef().getValue() == "/EcuExtract/EcuConfigValues"
        assert timing.getEcuConfigurationRef().getDest() == "ECUC-VALUE-COLLECTION"

        assert timing.setEcuConfigurationRef(None) is timing
        assert timing.getEcuConfigurationRef() is value
