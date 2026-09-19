"""
This module contains tests for the InterpolationRoutineMapping class
in the AUTOSAR SWComponentTemplate MeasurementAndCalibration InterpolationRoutineMappingSet module.
"""

import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.MeasurementAndCalibration.InterpolationRoutineMappingSet import InterpolationRoutine, InterpolationRoutineMapping

SPEC_NOTE = "This meta-class provides a mapping between one record layout and its matching interpolation routines. This allows to formally specify the semantics of the interpolation routines."
SPEC_USE_CASE = "The use case is such that the curves/Maps define an interpolation method."


class TestInterpolationRoutineMapping:
    def test_initialization(self):
        """Test that InterpolationRoutineMapping derives from ARObject with empty members"""
        mapping = InterpolationRoutineMapping()

        assert isinstance(mapping, ARObject)
        assert mapping.getInterpolationRoutines() == []
        assert mapping.getSwRecordLayoutRef() is None

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (R23-11 Table 2.5)"""
        doc = InterpolationRoutineMapping.__doc__.strip()
        assert doc.startswith(SPEC_NOTE)
        assert SPEC_USE_CASE in doc

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert InterpolationRoutineMapping.__init__.__doc__ is None

    def test_member_order_matches_spec(self):
        """Test member declaration order follows the R23-11 displayed row order"""
        source = inspect.getsource(InterpolationRoutineMapping.__init__)
        assert source.find("self.interpolationRoutines") < source.find("self.swRecordLayoutRef")

    def test_create_interpolation_routine(self):
        """Test createInterpolationRoutine appends a new child per call (no SHORT-NAME, no duplicate protection)"""
        mapping = InterpolationRoutineMapping()

        routine = mapping.createInterpolationRoutine()
        assert isinstance(routine, InterpolationRoutine)
        assert mapping.getInterpolationRoutines() == [routine]

        routine2 = mapping.createInterpolationRoutine()
        assert routine2 is not routine
        assert mapping.getInterpolationRoutines() == [routine, routine2]

    def test_add_interpolation_routine(self):
        """Test addInterpolationRoutine appends and returns self for chaining"""
        mapping = InterpolationRoutineMapping()
        routine = InterpolationRoutine()

        assert mapping is mapping.addInterpolationRoutine(routine)
        assert mapping.getInterpolationRoutines() == [routine]

    def test_get_set_sw_record_layout_ref(self):
        """Test swRecordLayoutRef round-trip and None no-op"""
        mapping = InterpolationRoutineMapping()
        ref = RefType()
        ref.setDest("SW-RECORD-LAYOUT")
        ref.setValue("/SwRecordLayouts/LinearLayout")

        assert mapping is mapping.setSwRecordLayoutRef(ref)
        assert mapping.getSwRecordLayoutRef() is ref
        assert mapping.setSwRecordLayoutRef(None) is mapping
        assert mapping.getSwRecordLayoutRef() is ref

        hints = typing.get_type_hints(InterpolationRoutineMapping.setSwRecordLayoutRef)
        assert hints.get("value") == typing.Optional[RefType]
        assert typing.get_type_hints(InterpolationRoutineMapping.getSwRecordLayoutRef).get("return") == typing.Optional[RefType]
