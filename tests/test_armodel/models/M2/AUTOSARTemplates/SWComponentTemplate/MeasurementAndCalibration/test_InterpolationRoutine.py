"""
This module contains tests for the InterpolationRoutine class
in the AUTOSAR SWComponentTemplate MeasurementAndCalibration module.
"""

import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Identifier, RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.MeasurementAndCalibration import InterpolationRoutine

SPEC_NOTE = "This represents an interpolation routine taken to evaluate the contents of a curve or map against a specific input value."


class TestInterpolationRoutine:
    def test_initialization(self):
        """Test that InterpolationRoutine derives from ARObject with None-valued members"""
        routine = InterpolationRoutine()

        assert isinstance(routine, ARObject)
        assert routine.getInterpolationRoutineRef() is None
        assert routine.getIsDefault() is None
        assert routine.getShortLabel() is None

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (R4.3.1 Table 5.115) plus the R23-11 constraint"""
        doc = InterpolationRoutine.__doc__.strip()
        assert doc.startswith(SPEC_NOTE)
        assert "[constr_5114] Semantics of InterpolationRoutine.isDefault:" in doc

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert InterpolationRoutine.__init__.__doc__ is None

    def test_member_order_matches_spec(self):
        """Test member declaration order follows the R4.3.1 displayed row order"""
        source = inspect.getsource(InterpolationRoutine.__init__)
        assert source.find("self.interpolationRoutineRef") < source.find("self.isDefault") < source.find("self.shortLabel")

    def test_get_set_interpolation_routine_ref(self):
        """Test interpolationRoutineRef round-trip and None no-op"""
        routine = InterpolationRoutine()
        ref = RefType()
        ref.setDest("BswModuleEntry")
        ref.setValue("/BswM/BswEntries/InterpolationEntry")

        assert routine is routine.setInterpolationRoutineRef(ref)
        assert routine.getInterpolationRoutineRef() is ref
        assert routine.setInterpolationRoutineRef(None) is routine
        assert routine.getInterpolationRoutineRef() is ref

        hints = typing.get_type_hints(InterpolationRoutine.setInterpolationRoutineRef)
        assert hints.get("value") == typing.Optional[RefType]
        assert typing.get_type_hints(InterpolationRoutine.getInterpolationRoutineRef).get("return") == typing.Optional[RefType]

    def test_get_set_is_default(self):
        """Test isDefault round-trip and None no-op"""
        routine = InterpolationRoutine()
        value = Boolean()
        value.setValue(True)

        assert routine is routine.setIsDefault(value)
        assert routine.getIsDefault() is value
        assert routine.setIsDefault(None) is routine
        assert routine.getIsDefault() is value

    def test_get_set_short_label(self):
        """Test shortLabel round-trip and None no-op"""
        routine = InterpolationRoutine()
        value = Identifier()
        value.setValue("LinearInterpolation")

        assert routine is routine.setShortLabel(value)
        assert routine.getShortLabel() is value
        assert routine.setShortLabel(None) is routine
        assert routine.getShortLabel() is value
