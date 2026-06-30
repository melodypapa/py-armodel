"""
Tests for GenericStructure VariantHandling model classes.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARPackage,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARNumerical,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import (
    PredefinedVariant,
    SwSystemconstValue,
    SwSystemconstantValueSet,
)
from armodel.models.M2.MSR.Documentation.Annotation import Annotation


def test_sw_systemconst_value_getters_setters_and_chaining():
    system_const_ref = RefType().setValue("/RootPkg/MyConst")
    annotation = Annotation()
    numerical_value = ARNumerical()
    numerical_value.setValue(42)

    value = SwSystemconstValue()

    result_annotation = value.addAnnotation(annotation)
    result_systemconst = value.setSwSystemconstRef(system_const_ref)
    result_value = value.setValue(numerical_value)

    assert value.getAnnotations() == [annotation]
    assert value.getSwSystemconstRef() == system_const_ref
    assert value.getValue() == numerical_value
    assert result_annotation is value
    assert result_systemconst is value
    assert result_value is value


def test_sw_systemconstant_value_set_add_and_get_values():
    parent = ARPackage(None, "ParentPkg")
    value_set = SwSystemconstantValueSet(parent, "MyValueSet")
    value = SwSystemconstValue()

    result = value_set.addSwSystemconstantValue(value)

    assert result is value_set
    assert value_set.getSwSystemconstantValues() == [value]


def test_predefined_variant_initial_state_and_adders():
    parent = ARPackage(None, "ParentPkg")
    variant = PredefinedVariant(parent, "MyPredefinedVariant")

    included_variant = RefType().setValue("/RootPkg/Variants/IncludedVariant")
    post_build_value_set = RefType().setValue(
        "/RootPkg/Criteria/PbCriterionValueSet"
    )
    sw_systemconstant_value_set = RefType().setValue(
        "/RootPkg/SystemConstants/MyValueSet"
    )

    result_included = variant.addIncludedVariantRef(included_variant)
    result_post_build = variant.addPostBuildVariantCriterionValueSetRef(
        post_build_value_set
    )
    result_systemconstant = variant.addSwSystemconstantValueSetRef(
        sw_systemconstant_value_set
    )

    assert variant.getIncludedVariantRefs() == [included_variant]
    assert variant.getPostBuildVariantCriterionValueSetRefs() == [post_build_value_set]
    assert variant.getSwSystemconstantValueSetRefs() == [sw_systemconstant_value_set]
    assert result_included is variant
    assert result_post_build is variant
    assert result_systemconstant is variant


def test_predefined_variant_adders_ignore_none():
    parent = ARPackage(None, "ParentPkg")
    variant = PredefinedVariant(parent, "MyPredefinedVariant")

    variant.addIncludedVariantRef(None)
    variant.addPostBuildVariantCriterionValueSetRef(None)
    variant.addSwSystemconstantValueSetRef(None)

    assert variant.getIncludedVariantRefs() == []
    assert variant.getPostBuildVariantCriterionValueSetRefs() == []
    assert variant.getSwSystemconstantValueSetRefs() == []
