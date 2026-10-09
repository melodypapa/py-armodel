"""
This module contains tests for the FMFeatureModel class in the
AUTOSAR GenericStructure.GeneralTemplateClasses module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import FMFeatureModel
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TestFMFeatureModel:
    """
    Test class for FMFeatureModel functionality.
    """

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _obj(self):
        return FMFeatureModel(self._parent(), "FeatureModel")

    def test_initialization(self):
        obj = self._obj()
        assert isinstance(obj, FMFeatureModel)
        assert obj.getFeatureRefs() == []
        assert obj.getRootRef() is None

    def test_add_get_feature_refs(self):
        obj = self._obj()
        ref = RefType().setValue("/Pkg/Feature").setDest("FM-FEATURE")
        assert obj.addFeatureRef(ref) is obj
        assert obj.getFeatureRefs() == [ref]

    def test_get_set_root_ref(self):
        obj = self._obj()
        ref = RefType().setValue("/Pkg/Root").setDest("FM-FEATURE")
        assert obj.setRootRef(ref) is obj
        assert obj.getRootRef() is ref

    def test_set_root_ref_none_noop(self):
        obj = self._obj()
        ref = RefType().setValue("/Pkg/Root").setDest("FM-FEATURE")
        obj.setRootRef(ref)
        assert obj.setRootRef(None) is obj
        assert obj.getRootRef() is ref
