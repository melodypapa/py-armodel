"""
This module contains tests for the FMFeatureMapElement class in the
AUTOSAR GenericStructure.GeneralTemplateClasses module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import FMFeatureMapAssertion, FMFeatureMapCondition, FMFeatureMapElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TestFMFeatureMapElement:
    """
    Test class for FMFeatureMapElement functionality.
    """

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _obj(self):
        return FMFeatureMapElement(self._parent(), "MapElement")

    def test_initialization(self):
        obj = self._obj()
        assert isinstance(obj, FMFeatureMapElement)
        assert obj.getAssertions() == []
        assert obj.getConditions() == []
        assert obj.getPostBuildVariantCriterionValueSetRefs() == []
        assert obj.getSwSystemconstantValueSetRefs() == []

    def test_add_get_assertions(self):
        obj = self._obj()
        assertion = obj.createAssertion("Assertion")
        assert isinstance(assertion, FMFeatureMapAssertion)
        assert obj.getAssertions() == [assertion]
        assert obj.createAssertion("Assertion") is assertion

    def test_add_get_conditions(self):
        obj = self._obj()
        condition = obj.createCondition("Condition")
        assert isinstance(condition, FMFeatureMapCondition)
        assert obj.getConditions() == [condition]
        assert obj.createCondition("Condition") is condition

    def test_add_get_post_build_variant_criterion_value_set_refs(self):
        obj = self._obj()
        ref = RefType().setValue("/Pkg/ValueSet").setDest("POST-BUILD-VARIANT-CRITERION-VALUE-SET")
        assert obj.addPostBuildVariantCriterionValueSetRef(ref) is obj
        assert obj.getPostBuildVariantCriterionValueSetRefs() == [ref]

    def test_add_get_sw_systemconstant_value_set_refs(self):
        obj = self._obj()
        ref = RefType().setValue("/Pkg/ValueSet").setDest("SW-SYSTEMCONSTANT-VALUE-SET")
        assert obj.addSwSystemconstantValueSetRef(ref) is obj
        assert obj.getSwSystemconstantValueSetRefs() == [ref]
