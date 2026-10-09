"""
This module contains tests for the FMFeatureRestriction class in the
AUTOSAR GenericStructure.GeneralTemplateClasses module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate import FMConditionByFeaturesAndAttributes
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import FMFeatureRestriction


class TestFMFeatureRestriction:
    """
    Test class for FMFeatureRestriction functionality.
    """

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _obj(self):
        return FMFeatureRestriction(self._parent(), "Restriction")

    def test_initialization(self):
        obj = self._obj()
        assert isinstance(obj, FMFeatureRestriction)
        assert obj.getRestriction() is None

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
