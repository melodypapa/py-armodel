"""
This module contains tests for the InterpolationRoutineMappingSet class
in the AUTOSAR SWComponentTemplate MeasurementAndCalibration InterpolationRoutineMappingSet module.
"""

import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.MeasurementAndCalibration.InterpolationRoutineMappingSet import InterpolationRoutineMapping, InterpolationRoutineMappingSet

SPEC_NOTE = "This meta-class specifies a set of interpolation routine mappings. Tags: atp.recommendedPackage=InterpolationRoutineMappingSets"


class TestInterpolationRoutineMappingSet:
    def test_initialization(self):
        """Test that the concrete InterpolationRoutineMappingSet is an ARElement wired with parent and short name"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        mapping_set = InterpolationRoutineMappingSet(ar_root, "TestMappingSet")

        assert isinstance(mapping_set, ARElement)
        assert mapping_set.getShortName() == "TestMappingSet"
        assert mapping_set.getInterpolationRoutineMappings() == []

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (R23-11 Table 2.4)"""
        assert InterpolationRoutineMappingSet.__doc__.strip() == SPEC_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert InterpolationRoutineMappingSet.__init__.__doc__ is None

    def test_member_order_matches_spec(self):
        """Test member declaration order follows the R23-11 displayed row order"""
        source = inspect.getsource(InterpolationRoutineMappingSet.__init__)
        assert "self.interpolationRoutineMappings" in source

    def test_create_interpolation_routine_mapping(self):
        """Test createInterpolationRoutineMapping appends a new child per call (no SHORT-NAME, no duplicate protection)"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        mapping_set = InterpolationRoutineMappingSet(ar_root, "TestCreate")

        mapping = mapping_set.createInterpolationRoutineMapping()
        assert isinstance(mapping, InterpolationRoutineMapping)
        assert mapping_set.getInterpolationRoutineMappings() == [mapping]

        mapping2 = mapping_set.createInterpolationRoutineMapping()
        assert mapping2 is not mapping
        assert mapping_set.getInterpolationRoutineMappings() == [mapping, mapping2]

    def test_add_interpolation_routine_mapping(self):
        """Test addInterpolationRoutineMapping appends and returns self for chaining"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        mapping_set = InterpolationRoutineMappingSet(ar_root, "TestAdd")
        mapping = InterpolationRoutineMapping()

        assert mapping_set is mapping_set.addInterpolationRoutineMapping(mapping)
        assert mapping_set.getInterpolationRoutineMappings() == [mapping]

    def test_get_interpolation_routine_mappings(self):
        """Test getInterpolationRoutineMappings typing"""
        getter_hints = typing.get_type_hints(InterpolationRoutineMappingSet.getInterpolationRoutineMappings)
        assert getter_hints.get("return") == typing.List[InterpolationRoutineMapping]

        setter_hints = typing.get_type_hints(InterpolationRoutineMappingSet.addInterpolationRoutineMapping)
        assert setter_hints.get("value") is InterpolationRoutineMapping
        assert setter_hints.get("return") is InterpolationRoutineMappingSet
