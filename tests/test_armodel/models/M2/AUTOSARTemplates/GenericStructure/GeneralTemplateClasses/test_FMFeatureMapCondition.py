"""
This module contains tests for the FMFeatureMapCondition class in the
AUTOSAR GenericStructure.GeneralTemplateClasses module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate import FMConditionByFeaturesAndAttributes
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import FMFeatureMapCondition


class TestFMFeatureMapCondition:
    """
    Test class for FMFeatureMapCondition functionality.
    """

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _obj(self):
        return FMFeatureMapCondition(self._parent(), "MapElement")

    def test_initialization(self):
        obj = self._obj()
        assert isinstance(obj, FMFeatureMapCondition)
        assert obj.getFmCond() is None

    def test_get_set(self):
        obj = self._obj()
        formula = FMConditionByFeaturesAndAttributes()
        assert obj.setFmCond(formula) is obj
        assert obj.getFmCond() is formula

    def test_set_none_noop(self):
        obj = self._obj()
        formula = FMConditionByFeaturesAndAttributes()
        obj.setFmCond(formula)
        assert obj.setFmCond(None) is obj
        assert obj.getFmCond() is formula
