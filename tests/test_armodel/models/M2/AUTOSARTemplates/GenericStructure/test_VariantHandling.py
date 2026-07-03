"""
Tests for GenericStructure VariantHandling model classes.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARPackage,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARNumerical,
    RefType,
    String,
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import (
    PredefinedVariant,
    SwSystemconstValue,
    SwSystemconstantValueSet,
    VariationPoint,
    PostBuildVariantCondition,
    PostBuildVariantCriterion,
    ConditionByFormula,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Enumerations import (
    BindingTimeEnum,
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


def test_binding_time_enum_initialization():
    enum = BindingTimeEnum()

    assert enum.getEnumValues() == [
        "codeGenerationTime",
        "linkTime",
        "preCompileTime",
        "systemDesignTime",
    ]


def test_binding_time_enum_validate_enum_value():
    enum = BindingTimeEnum()

    assert enum.validateEnumValue("preCompileTime") is True
    assert enum.validateEnumValue("codeGenerationTime") is True
    assert enum.validateEnumValue("linkTime") is True
    assert enum.validateEnumValue("systemDesignTime") is True
    assert enum.validateEnumValue("systemDescriptionTime") is False
    assert enum.validateEnumValue("invalidValue") is False


def test_post_build_variant_condition_getters_and_setters():
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer
    
    criterion = PostBuildVariantCriterion()
    criterion.setCriterionName("MyCriterion")
    
    value = Integer()
    value.setValue(42)

    condition = PostBuildVariantCondition()
    condition.setMatchingCriterion(criterion)
    condition.setValue(value)

    assert condition.getMatchingCriterion() == criterion
    assert condition.getValue() == value


def test_post_build_variant_condition_method_chaining():
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer
    
    criterion = PostBuildVariantCriterion()
    criterion.setCriterionName("MyCriterion")

    value = Integer()
    value.setValue(42)

    condition = PostBuildVariantCondition()
    result_criterion = condition.setMatchingCriterion(criterion)
    result_value = condition.setValue(value)

    assert result_criterion is condition
    assert result_value is condition


def test_post_build_variant_condition_none_values():
    condition = PostBuildVariantCondition()

    condition.setMatchingCriterion(None)
    condition.setValue(None)

    assert condition.getMatchingCriterion() is None
    assert condition.getValue() is None


def test_condition_by_formula_getters_and_setters():
    binding_time = BindingTimeEnum()
    binding_time.setValue("preCompileTime")

    condition = ConditionByFormula()
    condition.setBindingTime(binding_time)

    assert condition.getBindingTime() == binding_time


def test_condition_by_formula_method_chaining():
    binding_time = BindingTimeEnum()
    binding_time.setValue("codeGenerationTime")

    condition = ConditionByFormula()
    result = condition.setBindingTime(binding_time)

    assert result is condition


def test_condition_by_formula_none_values():
    condition = ConditionByFormula()

    condition.setBindingTime(None)

    assert condition.getBindingTime() is None


def test_variation_point_short_label():
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier
    
    variation_point = VariationPoint()
    label = Identifier()
    label.setValue("VP_Label_01")

    result = variation_point.setShortLabel(label)

    assert variation_point.getShortLabel() == label
    assert result is variation_point


def test_variation_point_add_post_build_conditions():
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer
    
    variation_point = VariationPoint()
    
    criterion1 = PostBuildVariantCriterion()
    criterion1.setCriterionName("Criterion1")
    value1 = Integer()
    value1.setValue(1)
    condition1 = PostBuildVariantCondition()
    condition1.setMatchingCriterion(criterion1).setValue(value1)

    criterion2 = PostBuildVariantCriterion()
    criterion2.setCriterionName("Criterion2")
    value2 = Integer()
    value2.setValue(2)
    condition2 = PostBuildVariantCondition()
    condition2.setMatchingCriterion(criterion2).setValue(value2)

    result1 = variation_point.addPostBuildVariantCondition(condition1)
    result2 = variation_point.addPostBuildVariantCondition(condition2)

    conditions = variation_point.getPostBuildVariantConditions()
    assert len(conditions) == 2
    assert conditions[0] == condition1
    assert conditions[1] == condition2
    assert result1 is variation_point
    assert result2 is variation_point


def test_variation_point_method_chaining():
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier
    
    variation_point = VariationPoint()
    binding_time = BindingTimeEnum()
    binding_time.setValue("preCompileTime")
    sys_condition = ConditionByFormula()
    sys_condition.setBindingTime(binding_time)

    label = Identifier()
    label.setValue("VP_Test")

    result = (
        variation_point
        .setShortLabel(label)
        .setSwSyscond(sys_condition)
    )

    assert result is variation_point
    assert variation_point.getShortLabel() == label
    assert variation_point.getSwSyscond() == sys_condition


def test_variation_point_none_values_ignored():
    variation_point = VariationPoint()

    variation_point.setShortLabel(None)
    variation_point.setSwSyscond(None)
    variation_point.addPostBuildVariantCondition(None)

    assert variation_point.getShortLabel() is None
    assert variation_point.getSwSyscond() is None
    assert len(variation_point.getPostBuildVariantConditions()) == 0


def test_variation_point_all_new_attributes():
    variation_point = VariationPoint()

    variation_point.setShortLabel("VP_Complete")
    binding_time = BindingTimeEnum()
    binding_time.setValue("codeGenerationTime")
    sys_cond = ConditionByFormula()
    sys_cond.setBindingTime(binding_time)
    variation_point.setSwSyscond(sys_cond)

    criterion = PostBuildVariantCriterion()
    criterion.setCriterionName("TestCriterion")
    pb_condition = PostBuildVariantCondition()
    pb_condition.setMatchingCriterion(criterion).setValue(100)
    variation_point.addPostBuildVariantCondition(pb_condition)

    assert variation_point.getShortLabel() == "VP_Complete"
    assert variation_point.getSwSyscond() == sys_cond
    assert len(variation_point.getPostBuildVariantConditions()) == 1
    assert variation_point.getPostBuildVariantConditions()[0] == pb_condition
