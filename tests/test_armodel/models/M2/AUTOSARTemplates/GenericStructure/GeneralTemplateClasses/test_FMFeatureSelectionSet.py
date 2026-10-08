"""
This module contains tests for the FMFeatureSelectionSet class in the
AUTOSAR GenericStructure.GeneralTemplateClasses module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import FMFeatureSelectionSet
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import FMFeatureSelection
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TestFMFeatureSelectionSet:
    """
    Test class for FMFeatureSelectionSet functionality.
    """

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _obj(self):
        return FMFeatureSelectionSet(self._parent(), "SelectionSet")

    def test_initialization(self):
        obj = self._obj()
        assert isinstance(obj, FMFeatureSelectionSet)
        assert obj.getFeatureModelRefs() == []
        assert obj.getIncludeRefs() == []
        assert obj.getSelections() == []

    def test_add_get_feature_model_refs(self):
        obj = self._obj()
        ref = RefType().setValue("/Pkg/FeatureModel").setDest("FM-FEATURE-MODEL")
        assert obj.addFeatureModelRef(ref) is obj
        assert obj.getFeatureModelRefs() == [ref]

    def test_add_get_include_refs(self):
        obj = self._obj()
        ref = RefType().setValue("/Pkg/OtherSet").setDest("FM-FEATURE-SELECTION-SET")
        assert obj.addIncludeRef(ref) is obj
        assert obj.getIncludeRefs() == [ref]

    def test_add_get_selections(self):
        obj = self._obj()
        selection = FMFeatureSelection(obj, "Selection")
        assert obj.addSelection(selection) is obj
        assert obj.getSelections() == [selection]
