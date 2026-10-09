"""
This module contains tests for the FMFeatureRelation class in the
AUTOSAR GenericStructure.GeneralTemplateClasses module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate import FMConditionByFeaturesAndAttributes
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import FMFeatureRelation
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TestFMFeatureRelation:
    """
    Test class for FMFeatureRelation functionality.
    """

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _obj(self):
        return FMFeatureRelation(self._parent(), "Relation")

    def test_initialization(self):
        obj = self._obj()
        assert isinstance(obj, FMFeatureRelation)
        assert obj.getFeatureRefs() == []
        assert obj.getRestriction() is None

    def test_add_get_feature_refs(self):
        obj = self._obj()
        ref = RefType().setValue("/Pkg/Feature").setDest("FM-FEATURE")
        assert obj.addFeatureRef(ref) is obj
        assert obj.getFeatureRefs() == [ref]

    def test_get_set_restriction(self):
        obj = self._obj()
        condition = FMConditionByFeaturesAndAttributes()
        assert obj.setRestriction(condition) is obj
        assert obj.getRestriction() is condition

    def test_set_restriction_none_noop(self):
        obj = self._obj()
        condition = FMConditionByFeaturesAndAttributes()
        obj.setRestriction(condition)
        assert obj.setRestriction(None) is obj
        assert obj.getRestriction() is condition
