"""
This module contains tests for the FMFeatureSelectionState enumeration in the
AUTOSAR GenericStructure.GeneralTemplateClasses module.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import FMFeatureSelectionState


class TestFMFeatureSelectionState:
    """
    Test class for FMFeatureSelectionState functionality.
    """

    def test_member_presence_and_values(self):
        assert FMFeatureSelectionState.DESELECTED == "DESELECTED"
        assert FMFeatureSelectionState.SELECTED == "SELECTED"
        assert FMFeatureSelectionState.UNDECIDED == "UNDECIDED"

    def test_instantiability(self):
        obj = FMFeatureSelectionState()
        assert isinstance(obj, FMFeatureSelectionState)
        obj.setValue(FMFeatureSelectionState.SELECTED)
        assert obj.getValue() == "SELECTED"

    def test_enum_values_order(self):
        obj = FMFeatureSelectionState()
        assert list(obj.getEnumValues()) == ["DESELECTED", "SELECTED", "UNDECIDED"]
