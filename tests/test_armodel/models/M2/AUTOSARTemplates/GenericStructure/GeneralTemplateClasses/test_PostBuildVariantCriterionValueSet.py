"""
This module contains tests for the PostBuildVariantCriterionValueSet class in the
AUTOSAR GenericStructure.GeneralTemplateClasses module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import PostBuildVariantCriterionValueSet
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import PostBuildVariantCriterionValue


class TestPostBuildVariantCriterionValueSet:
    """
    Test class for PostBuildVariantCriterionValueSet functionality.
    """

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _obj(self):
        return PostBuildVariantCriterionValueSet(self._parent(), "ValueSet")

    def test_initialization(self):
        obj = self._obj()
        assert isinstance(obj, PostBuildVariantCriterionValueSet)
        assert obj.getPostBuildVariantCriterionValues() == []

    def test_add_get(self):
        obj = self._obj()
        value = PostBuildVariantCriterionValue()
        assert obj.addPostBuildVariantCriterionValue(value) is obj
        assert obj.getPostBuildVariantCriterionValues() == [value]
