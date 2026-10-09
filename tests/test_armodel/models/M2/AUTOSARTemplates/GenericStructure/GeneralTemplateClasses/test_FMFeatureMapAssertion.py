"""
This module contains tests for the FMFeatureMapAssertion class in the
AUTOSAR GenericStructure.GeneralTemplateClasses module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate import FMConditionByFeaturesAndSwSystemconsts
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import FMFeatureMapAssertion


class TestFMFeatureMapAssertion:
    """
    Test class for FMFeatureMapAssertion functionality.
    """

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _obj(self):
        return FMFeatureMapAssertion(self._parent(), "MapElement")

    def test_initialization(self):
        obj = self._obj()
        assert isinstance(obj, FMFeatureMapAssertion)
        assert obj.getFmSyscond() is None

    def test_get_set(self):
        obj = self._obj()
        formula = FMConditionByFeaturesAndSwSystemconsts()
        assert obj.setFmSyscond(formula) is obj
        assert obj.getFmSyscond() is formula

    def test_set_none_noop(self):
        obj = self._obj()
        formula = FMConditionByFeaturesAndSwSystemconsts()
        obj.setFmSyscond(formula)
        assert obj.setFmSyscond(None) is obj
        assert obj.getFmSyscond() is formula
