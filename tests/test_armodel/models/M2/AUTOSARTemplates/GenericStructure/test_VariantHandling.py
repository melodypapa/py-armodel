"""
Tests for GenericStructure VariantHandling model classes.
"""

import typing

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintGenerator import (
    BlueprintGenerator,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
    ARPackage,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import AtpMixedString
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Enumerations import (
    BindingTimeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARNumerical,
    Identifier,
    Integer,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import (
    ConditionByFormula,
    PostBuildVariantCondition,
    PostBuildVariantCriterion,
    PostBuildVariantCriterionValue,
    PredefinedVariant,
    SwSystemconstantValueSet,
    SwSystemconstValue,
    VariationPoint,
)
from armodel.models.M2.MSR.AsamHdo.SpecialData import Sdg
from armodel.models.M2.MSR.Documentation.Annotation import Annotation
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageOverviewParagraph


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
    # Spec Table 7.25: Base is ARElement (most-derived)
    assert isinstance(value_set, ARElement)


def test_predefined_variant_initial_state_and_adders():
    parent = ARPackage(None, "ParentPkg")
    variant = PredefinedVariant(parent, "MyPredefinedVariant")

    included_variant = RefType().setValue("/RootPkg/Variants/IncludedVariant")
    post_build_value_set = RefType().setValue("/RootPkg/Criteria/PbCriterionValueSet")
    sw_systemconstant_value_set = RefType().setValue("/RootPkg/SystemConstants/MyValueSet")

    result_included = variant.addIncludedVariantRef(included_variant)
    result_post_build = variant.addPostBuildVariantCriterionValueSetRef(post_build_value_set)
    result_systemconstant = variant.addSwSystemconstantValueSetRef(sw_systemconstant_value_set)

    assert variant.getIncludedVariantRefs() == [included_variant]
    assert variant.getPostBuildVariantCriterionValueSetRefs() == [post_build_value_set]
    assert variant.getSwSystemconstantValueSetRefs() == [sw_systemconstant_value_set]
    assert result_included is variant
    assert result_post_build is variant
    assert result_systemconstant is variant
    # Spec Table 7.24: Base is ARElement (most-derived)
    assert isinstance(variant, ARElement)


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

    criterion_ref = RefType().setValue("/RootPkg/Criteria/MyCriterion")

    value = Integer()
    value.setValue(42)

    condition = PostBuildVariantCondition()
    condition.setMatchingCriterionRef(criterion_ref)
    condition.setValue(value)

    assert condition.getMatchingCriterionRef() == criterion_ref
    assert condition.getValue() == value


def test_post_build_variant_condition_method_chaining():
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer

    criterion_ref = RefType().setValue("/RootPkg/Criteria/MyCriterion")

    value = Integer()
    value.setValue(42)

    condition = PostBuildVariantCondition()
    result_criterion = condition.setMatchingCriterionRef(criterion_ref)
    result_value = condition.setValue(value)

    assert result_criterion is condition
    assert result_value is condition


def test_post_build_variant_condition_none_values():
    condition = PostBuildVariantCondition()

    condition.setMatchingCriterionRef(None)
    condition.setValue(None)

    assert condition.getMatchingCriterionRef() is None
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

    criterion_ref1 = RefType().setValue("/RootPkg/Criteria/Criterion1")
    value1 = Integer()
    value1.setValue(1)
    condition1 = PostBuildVariantCondition()
    condition1.setMatchingCriterionRef(criterion_ref1).setValue(value1)

    criterion_ref2 = RefType().setValue("/RootPkg/Criteria/Criterion2")
    value2 = Integer()
    value2.setValue(2)
    condition2 = PostBuildVariantCondition()
    condition2.setMatchingCriterionRef(criterion_ref2).setValue(value2)

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

    result = variation_point.setShortLabel(label).setSwSyscond(sys_condition)

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

    criterion_ref = RefType().setValue("/RootPkg/Criteria/TestCriterion")
    pb_condition = PostBuildVariantCondition()
    pb_condition.setMatchingCriterionRef(criterion_ref).setValue(100)
    variation_point.addPostBuildVariantCondition(pb_condition)

    assert variation_point.getShortLabel() == "VP_Complete"
    assert variation_point.getSwSyscond() == sys_cond
    assert len(variation_point.getPostBuildVariantConditions()) == 1
    assert variation_point.getPostBuildVariantConditions()[0] == pb_condition


class TestPostBuildVariantCriterion:
    def test_initialization(self):
        parent = ARPackage(None, "ParentPkg")
        criterion = PostBuildVariantCriterion(parent, "MyCriterion")
        assert criterion.getCompuMethodRef() is None

    def test_set_get_compu_method_ref(self):
        parent = ARPackage(None, "ParentPkg")
        criterion = PostBuildVariantCriterion(parent, "MyCriterion")
        compu_method_ref = RefType().setValue("/RootPkg/CompuMethods/MyCompuMethod")
        assert criterion.setCompuMethodRef(compu_method_ref) is criterion
        assert criterion.getCompuMethodRef() == compu_method_ref

    def test_set_compu_method_ref_none_is_noop(self):
        parent = ARPackage(None, "ParentPkg")
        criterion = PostBuildVariantCriterion(parent, "MyCriterion")
        compu_method_ref = RefType().setValue("/RootPkg/CompuMethods/MyCompuMethod")
        criterion.setCompuMethodRef(compu_method_ref)
        criterion.setCompuMethodRef(None)
        assert criterion.getCompuMethodRef() == compu_method_ref


class TestPostBuildVariantCriterionValue:
    def test_initialization(self):
        value = PostBuildVariantCriterionValue()
        assert value.getAnnotations() == []
        assert value.getValue() is None
        assert value.getVariantCriterionRef() is None

    def test_add_annotations_and_get(self):
        value = PostBuildVariantCriterionValue()
        annotation = Annotation()
        assert value.addAnnotation(annotation) is value
        assert value.getAnnotations() == [annotation]

    def test_add_annotation_none_is_noop(self):
        value = PostBuildVariantCriterionValue()
        annotation = Annotation()
        value.addAnnotation(annotation)
        value.addAnnotation(None)
        assert value.getAnnotations() == [annotation]

    def test_set_get_value(self):
        value = PostBuildVariantCriterionValue()
        integer_value = Integer().setValue(5)
        assert value.setValue(integer_value) is value
        assert value.getValue() == integer_value

    def test_set_value_none_is_noop(self):
        value = PostBuildVariantCriterionValue()
        integer_value = Integer().setValue(5)
        value.setValue(integer_value)
        value.setValue(None)
        assert value.getValue() == integer_value

    def test_set_get_variant_criterion_ref(self):
        value = PostBuildVariantCriterionValue()
        criterion_ref = RefType().setValue("/RootPkg/Criteria/MyCriterion")
        assert value.setVariantCriterionRef(criterion_ref) is value
        assert value.getVariantCriterionRef() == criterion_ref

    def test_set_variant_criterion_ref_none_is_noop(self):
        value = PostBuildVariantCriterionValue()
        criterion_ref = RefType().setValue("/RootPkg/Criteria/MyCriterion")
        value.setVariantCriterionRef(criterion_ref)
        value.setVariantCriterionRef(None)
        assert value.getVariantCriterionRef() == criterion_ref


class TestPostBuildVariantCriterionValueSpecContract:
    """Table 7.27 (AUTOSAR_FO_TPS_GenericStructureTemplate, p.259) spec contract
    for PostBuildVariantCriterionValue."""

    def test_class_docstring_verbatim(self):
        """
        Test that the class docstring is the Table 7.27 Note verbatim.
        """
        assert PostBuildVariantCriterionValue.__doc__.strip() == (
            "This class specifies the value which shall be assigned to a particular variant criterion "
            "in order to bind the variation point. If multiple criterion/value pairs are specified, "
            "they all shall match to bind the variation point."
        )

    def test_init_has_no_docstring(self):
        """
        Test that __init__ has no docstring (spec Notes live in inline member comments).
        """
        assert PostBuildVariantCriterionValue.__init__.__doc__ is None

    def test_base_is_arobject(self):
        """
        Test that the Base per Table 7.27 is ARObject (most-derived — not an
        ARElement; aggregation is via PostBuildVariantCriterionValueSet).
        """
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

        assert issubclass(PostBuildVariantCriterionValue, ARObject)
        assert not issubclass(PostBuildVariantCriterionValue, ARElement)

    def test_annotations_typed_list_of_annotation(self):
        """
        Test that annotation (Annotation, * aggr) maps to a List[Annotation] accessor pair.
        """
        getter_hints = typing.get_type_hints(PostBuildVariantCriterionValue.getAnnotations)
        assert getter_hints.get("return") == typing.List[Annotation]

        setter_hints = typing.get_type_hints(PostBuildVariantCriterionValue.addAnnotation)
        assert setter_hints.get("value") is Annotation
        assert setter_hints.get("return") is PostBuildVariantCriterionValue

    def test_value_typed_optional_integer(self):
        """
        Test that value (Integer, 1 attr) is typed Optional[Integer]
        (the spec type name maps to the repo Integer class).
        """
        getter_hints = typing.get_type_hints(PostBuildVariantCriterionValue.getValue)
        assert getter_hints.get("return") == typing.Optional[Integer]

        setter_hints = typing.get_type_hints(PostBuildVariantCriterionValue.setValue)
        assert setter_hints.get("value") == typing.Optional[Integer]
        assert setter_hints.get("return") is PostBuildVariantCriterionValue

    def test_variant_criterion_ref_typed_ref_type(self):
        """
        Test that variantCriterion (PostBuildVariantCriterion, 1 ref) maps to a RefType
        accessor pair (Kind ref suffix per the matchingCriterionRef precedent).
        """
        getter_hints = typing.get_type_hints(PostBuildVariantCriterionValue.getVariantCriterionRef)
        assert getter_hints.get("return") is RefType

        setter_hints = typing.get_type_hints(PostBuildVariantCriterionValue.setVariantCriterionRef)
        assert setter_hints.get("value") is RefType
        assert setter_hints.get("return") is PostBuildVariantCriterionValue

    def test_getter_docstrings_are_notes_verbatim(self):
        """
        Test that getter docstrings are the Table 7.27 Notes verbatim without the Tags suffix.
        """
        assert PostBuildVariantCriterionValue.getAnnotations.__doc__.strip() == "This provides the ability to add information why the value is set like it is."
        assert PostBuildVariantCriterionValue.getValue.__doc__.strip() == "This is the particular value of the post-build variant criterion."
        assert PostBuildVariantCriterionValue.getVariantCriterionRef.__doc__.strip() == "This association selects the variant criterion whose value is specified."

    def test_setter_docstrings_are_notes_with_none_noop(self):
        """
        Test that setter docstrings are the Table 7.27 Notes verbatim plus the None-no-op sentence.
        """
        assert PostBuildVariantCriterionValue.addAnnotation.__doc__.strip() == (
            "This provides the ability to add information why the value is set like it is. " "A None value is a no-op and is not appended."
        )
        assert PostBuildVariantCriterionValue.setValue.__doc__.strip() == (
            "This is the particular value of the post-build variant criterion. " "A None value is a no-op and does not overwrite an existing value."
        )
        assert PostBuildVariantCriterionValue.setVariantCriterionRef.__doc__.strip() == (
            "This association selects the variant criterion whose value is specified. " "A None value is a no-op and does not overwrite an existing variantCriterionRef."
        )


class TestPostBuildVariantCondition:
    def test_initialization(self):
        condition = PostBuildVariantCondition()
        assert condition.getMatchingCriterionRef() is None
        assert condition.getValue() is None

    def test_get_set_matching_criterion_ref(self):
        condition = PostBuildVariantCondition()
        ref = RefType().setValue("/Criterions/Country").setDest("POST-BUILD-VARIANT-CRITERION")
        assert condition.setMatchingCriterionRef(ref) is condition
        assert condition.getMatchingCriterionRef() == ref
        condition.setMatchingCriterionRef(None)
        assert condition.getMatchingCriterionRef() == ref

    def test_get_set_value(self):
        condition = PostBuildVariantCondition()
        value = Integer().setValue("1")
        assert condition.setValue(value) is condition
        assert condition.getValue() == value
        condition.setValue(None)
        assert condition.getValue() == value


class TestConditionByFormula:
    def test_initialization(self):
        condition = ConditionByFormula()
        assert condition.getBindingTime() is None


class TestConditionByFormulaSpecContract:
    """Table 7.5 (AUTOSAR_FO_TPS_GenericStructureTemplate, p.231) spec contract
    for ConditionByFormula."""

    def test_class_docstring_verbatim(self):
        """
        Test that the class docstring is the Table 7.5 Note verbatim.
        """
        assert ConditionByFormula.__doc__.strip() == (
            "This class represents a condition which is computed based on system constants "
            "according to the specified expression. The expected result is considered as boolean "
            "value. The result of the expression is interpreted as a condition. "
            '• "0" represents "false"; • a value other than zero is considered "true"'
        )

    def test_init_has_no_docstring(self):
        """
        Test that __init__ has no docstring (spec Notes live in inline member comments).
        """
        assert ConditionByFormula.__init__.__doc__ is None

    def test_binding_time_typed_binding_time_enum(self):
        """
        Test that bindingTime is typed BindingTimeEnum per Table 7.5 (getter/setter annotations).
        """
        getter_hints = typing.get_type_hints(ConditionByFormula.getBindingTime)
        assert getter_hints.get("return") == typing.Optional[BindingTimeEnum]

        setter_hints = typing.get_type_hints(ConditionByFormula.setBindingTime)
        assert setter_hints.get("value") == typing.Optional[BindingTimeEnum]
        assert setter_hints.get("return") is ConditionByFormula

    def test_getter_docstring_is_note_without_tags(self):
        """
        Test that the getter docstring is the Table 7.5 Note verbatim without the Tags suffix.
        """
        assert ConditionByFormula.getBindingTime.__doc__.strip() == (
            "This attribute specifies the point in time when condition may be evaluated at " "earliest. At this point in time all referenced system constants shall have a value."
        )

    def test_setter_docstring_is_note_with_none_noop(self):
        """
        Test that the setter docstring is the Table 7.5 Note plus the None-no-op sentence.
        """
        assert ConditionByFormula.setBindingTime.__doc__.strip() == (
            "This attribute specifies the point in time when condition may be evaluated at "
            "earliest. At this point in time all referenced system constants shall have a value. "
            "A None value is a no-op and does not overwrite an existing bindingTime."
        )

    def test_text_default_none(self):
        """
        Test that the <<atpMixedString>> mixed content defaults to None.
        """
        condition = ConditionByFormula()
        assert condition.getMixedString() is None

    def test_text_round_trip_and_chaining(self):
        """
        Test the mixed string content accessors (the value IS the mixed text per the
        empty XSD element group / mixed="true" complexType).
        """
        condition = ConditionByFormula()
        assert isinstance(condition, AtpMixedString)
        assert condition.setMixedString('sysc == "A"') is condition
        assert condition.getMixedString() == 'sysc == "A"'
        condition.setMixedString(None)
        assert condition.getMixedString() == 'sysc == "A"'


class TestSwSystemconstValueSpecContract:
    """Table 7.9 (AUTOSAR_FO_TPS_GenericStructureTemplate, p.235) spec contract
    for SwSystemconstValue."""

    def test_class_docstring_verbatim(self):
        """
        Test that the class docstring is the Table 7.9 Note verbatim.
        """
        assert SwSystemconstValue.__doc__.strip() == "This meta-class assigns a particular value to a system constant."

    def test_init_has_no_docstring(self):
        """
        Test that __init__ has no docstring (spec Notes live in inline member comments).
        """
        assert SwSystemconstValue.__init__.__doc__ is None

    def test_annotations_typed_list_of_annotation(self):
        """
        Test that annotation (Annotation, * aggr) maps to a List[Annotation] accessor pair.
        """
        getter_hints = typing.get_type_hints(SwSystemconstValue.getAnnotations)
        assert getter_hints.get("return") == typing.List[Annotation]

        setter_hints = typing.get_type_hints(SwSystemconstValue.addAnnotation)
        assert setter_hints.get("value") is Annotation
        assert setter_hints.get("return") is SwSystemconstValue

    def test_sw_systemconst_ref_typed_ref_type(self):
        """
        Test that swSystemconst (SwSystemconst, 1 ref) maps to a RefType accessor pair
        (field base name verbatim + Kind suffix per the compuMethodRef precedent).
        """
        getter_hints = typing.get_type_hints(SwSystemconstValue.getSwSystemconstRef)
        assert getter_hints.get("return") is RefType

        setter_hints = typing.get_type_hints(SwSystemconstValue.setSwSystemconstRef)
        assert setter_hints.get("value") is RefType
        assert setter_hints.get("return") is SwSystemconstValue

    def test_value_typed_optional_ar_numerical(self):
        """
        Test that value (Numerical, 1 attr) is typed Optional[ARNumerical]
        (the repo class for the spec Numerical type).
        """
        getter_hints = typing.get_type_hints(SwSystemconstValue.getValue)
        assert getter_hints.get("return") == typing.Optional[ARNumerical]

        setter_hints = typing.get_type_hints(SwSystemconstValue.setValue)
        assert setter_hints.get("value") == typing.Optional[ARNumerical]
        assert setter_hints.get("return") is SwSystemconstValue

    def test_getter_docstrings_are_notes_without_tags(self):
        """
        Test that getter docstrings are the Table 7.9 Notes verbatim without the Tags suffix.
        """
        assert SwSystemconstValue.getAnnotations.__doc__.strip() == "This provides the ability to add information why the value is set like it is."
        assert SwSystemconstValue.getSwSystemconstRef.__doc__.strip() == "This is the system constant to which the value applies."
        assert SwSystemconstValue.getValue.__doc__.strip() == (
            "This is the particular value of a system constant. It is specified as Numerical. "
            "Further restrictions may apply by the definition of the system constant. "
            "The value attribute defines the internal value of the SwSystemconst as it is processed in the Formula Language."
        )

    def test_setter_docstrings_are_notes_with_none_noop(self):
        """
        Test that setter docstrings are the Table 7.9 Notes verbatim plus the None-no-op sentence.
        """
        assert SwSystemconstValue.addAnnotation.__doc__.strip() == ("This provides the ability to add information why the value is set like it is. " "A None value is a no-op and is not appended.")
        assert SwSystemconstValue.setSwSystemconstRef.__doc__.strip() == (
            "This is the system constant to which the value applies. " "A None value is a no-op and does not overwrite an existing swSystemconstRef."
        )
        assert SwSystemconstValue.setValue.__doc__.strip() == (
            "This is the particular value of a system constant. It is specified as Numerical. "
            "Further restrictions may apply by the definition of the system constant. "
            "The value attribute defines the internal value of the SwSystemconst as it is processed in the Formula Language. "
            "A None value is a no-op and does not overwrite an existing value."
        )

    def test_defaults(self):
        """
        Test the initial state of a fresh SwSystemconstValue.
        """
        value = SwSystemconstValue()
        assert value.getAnnotations() == []
        assert value.getSwSystemconstRef() is None
        assert value.getValue() is None

    def test_setter_none_noops(self):
        """
        Test that setters ignore None (field values preserved).
        """
        value = SwSystemconstValue()
        annotation = Annotation()
        ref = RefType().setValue("/Constants/MyConst")
        numerical = ARNumerical().setValue(1)

        value.addAnnotation(annotation)
        value.setSwSystemconstRef(ref)
        value.setValue(numerical)

        assert value.addAnnotation(None) is value
        assert value.setSwSystemconstRef(None) is value
        assert value.setValue(None) is value
        assert value.getAnnotations() == [annotation]
        assert value.getSwSystemconstRef() is ref
        assert value.getValue() is numerical


class TestPostBuildVariantConditionSpecContract:
    """Table 7.6 (AUTOSAR_FO_TPS_GenericStructureTemplate, p.232) spec contract
    for PostBuildVariantCondition."""

    def test_class_docstring_verbatim(self):
        """
        Test that the class docstring is the Table 7.6 Note verbatim.
        """
        assert PostBuildVariantCondition.__doc__.strip() == (
            "This class specifies the value which shall be assigned to a particular variant criterion "
            "in order to bind the variation point. If multiple criterion/value pairs are specified, "
            "they shall all match to bind the variation point. In other words binding can be represented "
            "by (criterion1 == value1) && (condition2 == value2) ..."
        )

    def test_init_has_no_docstring(self):
        """
        Test that __init__ has no docstring (spec Notes live in inline member comments).
        """
        assert PostBuildVariantCondition.__init__.__doc__ is None

    def test_matching_criterion_ref_typed_ref_type(self):
        """
        Test that matchingCriterion (PostBuildVariantCriterion, 1 ref) maps to a RefType
        accessor pair (Kind ref suffix per the compuMethodRef precedent).
        """
        getter_hints = typing.get_type_hints(PostBuildVariantCondition.getMatchingCriterionRef)
        assert getter_hints.get("return") is RefType

        setter_hints = typing.get_type_hints(PostBuildVariantCondition.setMatchingCriterionRef)
        assert setter_hints.get("value") is RefType
        assert setter_hints.get("return") is PostBuildVariantCondition

    def test_value_typed_optional_integer(self):
        """
        Test that value (Integer, 1 attr) is typed Optional[Integer]
        (the spec type name maps to the repo Integer class).
        """
        getter_hints = typing.get_type_hints(PostBuildVariantCondition.getValue)
        assert getter_hints.get("return") == typing.Optional[Integer]

        setter_hints = typing.get_type_hints(PostBuildVariantCondition.setValue)
        assert setter_hints.get("value") == typing.Optional[Integer]
        assert setter_hints.get("return") is PostBuildVariantCondition

    def test_getter_docstrings_are_notes_verbatim(self):
        """
        Test that getter docstrings are the Table 7.6 Notes verbatim without the Tags suffix.
        """
        assert PostBuildVariantCondition.getMatchingCriterionRef.__doc__.strip() == "This is the criterion which needs to match the value in order to make the PostbuildVariantCondition to be true."
        assert PostBuildVariantCondition.getValue.__doc__.strip() == "This is the particular value of the post-build variant criterion."

    def test_setter_docstrings_are_notes_with_none_noop(self):
        """
        Test that setter docstrings are the Table 7.6 Notes verbatim plus the None-no-op sentence.
        """
        assert PostBuildVariantCondition.setMatchingCriterionRef.__doc__.strip() == (
            "This is the criterion which needs to match the value in order to make the PostbuildVariantCondition to be true. "
            "A None value is a no-op and does not overwrite an existing matchingCriterionRef."
        )
        assert PostBuildVariantCondition.setValue.__doc__.strip() == (
            "This is the particular value of the post-build variant criterion. " "A None value is a no-op and does not overwrite an existing value."
        )

    def test_defaults(self):
        """
        Test the initial state of a fresh PostBuildVariantCondition.
        """
        condition = PostBuildVariantCondition()
        assert condition.getMatchingCriterionRef() is None
        assert condition.getValue() is None

    def test_setter_none_noops(self):
        """
        Test that setters ignore None (field values preserved).
        """
        condition = PostBuildVariantCondition()
        ref = RefType().setValue("/Criterions/Country")
        value = Integer().setValue(42)

        condition.setMatchingCriterionRef(ref)
        condition.setValue(value)

        assert condition.setMatchingCriterionRef(None) is condition
        assert condition.setValue(None) is condition
        assert condition.getMatchingCriterionRef() is ref
        assert condition.getValue() is value


class TestPostBuildVariantCriterionSpecContract:
    """Table 7.63 (AUTOSAR_CP_TPS_SoftwareComponentTemplate, p.614) spec contract
    for PostBuildVariantCriterion."""

    def test_class_docstring_verbatim(self):
        """
        Test that the class docstring is the Table 7.63 Note verbatim (including the
        class-level Tags suffix).
        """
        assert PostBuildVariantCriterion.__doc__.strip() == ("This class specifies one particular PostBuildVariantSelector. " "Tags: atp.recommendedPackage=PostBuildVariantCriterions")

    def test_init_has_no_docstring(self):
        """
        Test that __init__ has no docstring (spec Notes live in inline member comments).
        """
        assert PostBuildVariantCriterion.__init__.__doc__ is None

    def test_base_is_arelement(self):
        """
        Test that the most-derived Base per Table 7.63 is ARElement
        (ARPackage.element aggregation — an ARPackage-level element).
        """
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement

        assert issubclass(PostBuildVariantCriterion, ARElement)

    def test_compu_method_ref_typed_ref_type(self):
        """
        Test that compuMethod (CompuMethod, 1 ref) maps to a RefType accessor pair
        (Kind ref suffix per the compuMethodRef precedent).
        """
        getter_hints = typing.get_type_hints(PostBuildVariantCriterion.getCompuMethodRef)
        assert getter_hints.get("return") is RefType

        setter_hints = typing.get_type_hints(PostBuildVariantCriterion.setCompuMethodRef)
        assert setter_hints.get("value") is RefType
        assert setter_hints.get("return") is PostBuildVariantCriterion

    def test_getter_docstring_is_note_verbatim(self):
        """
        Test that the getter docstring is the Table 7.63 Note verbatim.
        """
        assert PostBuildVariantCriterion.getCompuMethodRef.__doc__.strip() == ("The compuMethod specifies the possible values for the variant criterion serving as an enumerator.")

    def test_setter_docstring_is_note_with_none_noop(self):
        """
        Test that the setter docstring is the Table 7.63 Note verbatim plus the None-no-op sentence.
        """
        assert PostBuildVariantCriterion.setCompuMethodRef.__doc__.strip() == (
            "The compuMethod specifies the possible values for the variant criterion serving as an enumerator. " "A None value is a no-op and does not overwrite an existing compuMethodRef."
        )


def test_criterion_holds_variation_point_via_mixin():
    # PostBuildVariantCriterion is VariationPointCapable through the PackageableElement
    # anchor (ARPackage.element carries atpVariation, GST Table 4.1); the slot is no
    # longer provided by Identifiable.
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage

    parent = ARPackage(None, "Pkg")
    criterion = PostBuildVariantCriterion(parent, "MyCriterion")
    variation_point = VariationPoint()

    assert criterion.getVariationPoint() is None

    result = criterion.setVariationPoint(variation_point)

    assert criterion.getVariationPoint() is variation_point
    assert result is criterion


class TestVariationPoint:
    def test_initialization(self):
        variation_point = VariationPoint()
        assert variation_point.getBlueprintCondition() is None
        assert variation_point.getDesc() is None
        assert variation_point.getFormalBlueprintGenerator() is None
        assert variation_point.getPostBuildVariantConditions() == []
        assert variation_point.getSdg() is None
        assert variation_point.getShortLabel() is None
        assert variation_point.getSwSyscond() is None

    def test_set_get_formal_blueprint_generator(self):
        variation_point = VariationPoint()
        generator = BlueprintGenerator()
        assert variation_point.setFormalBlueprintGenerator(generator) is variation_point
        assert variation_point.getFormalBlueprintGenerator() == generator

    def test_set_formal_blueprint_generator_none_is_noop(self):
        variation_point = VariationPoint()
        generator = BlueprintGenerator()
        variation_point.setFormalBlueprintGenerator(generator)
        variation_point.setFormalBlueprintGenerator(None)
        assert variation_point.getFormalBlueprintGenerator() == generator

    def test_set_get_blueprint_condition(self):
        variation_point = VariationPoint()
        block = DocumentationBlock()
        assert variation_point.setBlueprintCondition(block) is variation_point
        assert variation_point.getBlueprintCondition() == block
        variation_point.setBlueprintCondition(None)
        assert variation_point.getBlueprintCondition() == block

    def test_set_get_desc(self):
        variation_point = VariationPoint()
        desc = MultiLanguageOverviewParagraph()
        assert variation_point.setDesc(desc) is variation_point
        assert variation_point.getDesc() == desc
        variation_point.setDesc(None)
        assert variation_point.getDesc() == desc

    def test_set_get_sdg(self):
        variation_point = VariationPoint()
        sdg = Sdg()
        assert variation_point.setSdg(sdg) is variation_point
        assert variation_point.getSdg() == sdg
        variation_point.setSdg(None)
        assert variation_point.getSdg() == sdg

    def test_set_get_short_label(self):
        variation_point = VariationPoint()
        label = Identifier().setValue("VP_Label")
        assert variation_point.setShortLabel(label) is variation_point
        assert variation_point.getShortLabel() == label
        variation_point.setShortLabel(None)
        assert variation_point.getShortLabel() == label

    def test_set_get_sw_syscond(self):
        variation_point = VariationPoint()
        syscond = ConditionByFormula()
        assert variation_point.setSwSyscond(syscond) is variation_point
        assert variation_point.getSwSyscond() == syscond
        variation_point.setSwSyscond(None)
        assert variation_point.getSwSyscond() == syscond


class TestVariationPointSpecContract:
    """Table 7.4 (AUTOSAR_FO_TPS_GenericStructureTemplate, p.226) spec contract
    for VariationPoint. The mid-identifier spaces in the PDF-extracted Note
    ("postBuildVariant Criterion", "formal BlueprintGenerator") are extraction
    artifacts — the XSD 00052 documentation strings (AUTOSAR_00052.xsd group
    VARIATION-POINT, line 130012) confirm the camelCase forms."""

    def test_class_docstring_verbatim(self):
        """
        Test that the class docstring is the Table 7.4 Note verbatim.
        """
        assert VariationPoint.__doc__.strip() == (
            'This meta-class represents the ability to express a "structural variation point". '
            "The container of the variation point is part of the selected variant if swSyscond "
            "evaluates to true and each postBuildVariantCriterion is fulfilled."
        )

    def test_init_has_no_docstring(self):
        """
        Test that __init__ has no docstring (spec Notes live in inline member comments).
        """
        assert VariationPoint.__init__.__doc__ is None

    def test_base_is_arobject(self):
        """
        Test that the Base per Table 7.4 is ARObject (most-derived).
        """
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

        assert issubclass(VariationPoint, ARObject)

    def test_blueprint_condition_typed_documentation_block(self):
        """
        Test that blueprintCondition (DocumentationBlock, 0..1 aggr) is typed
        Optional[DocumentationBlock].
        """
        getter_hints = typing.get_type_hints(VariationPoint.getBlueprintCondition)
        assert getter_hints.get("return") == typing.Optional[DocumentationBlock]

        setter_hints = typing.get_type_hints(VariationPoint.setBlueprintCondition)
        assert setter_hints.get("value") == typing.Optional[DocumentationBlock]
        assert setter_hints.get("return") is VariationPoint

    def test_desc_typed_multi_language_overview_paragraph(self):
        """
        Test that desc (MultiLanguageOverviewParagraph, 0..1 aggr) is typed
        Optional[MultiLanguageOverviewParagraph].
        """
        getter_hints = typing.get_type_hints(VariationPoint.getDesc)
        assert getter_hints.get("return") == typing.Optional[MultiLanguageOverviewParagraph]

        setter_hints = typing.get_type_hints(VariationPoint.setDesc)
        assert setter_hints.get("value") == typing.Optional[MultiLanguageOverviewParagraph]
        assert setter_hints.get("return") is VariationPoint

    def test_formal_blueprint_generator_typed_blueprint_generator(self):
        """
        Test that formalBlueprintGenerator (BlueprintGenerator, 0..1 aggr,
        atp.Status=draft) is typed Optional[BlueprintGenerator].
        """
        getter_hints = typing.get_type_hints(VariationPoint.getFormalBlueprintGenerator)
        assert getter_hints.get("return") == typing.Optional[BlueprintGenerator]

        setter_hints = typing.get_type_hints(VariationPoint.setFormalBlueprintGenerator)
        assert setter_hints.get("value") == typing.Optional[BlueprintGenerator]
        assert setter_hints.get("return") is VariationPoint

    def test_post_build_variant_conditions_typed_list(self):
        """
        Test that postBuildVariantCondition (PostBuildVariantCondition, * aggr) maps to
        a List[PostBuildVariantCondition] accessor pair (singular `*` -> plural field).
        """
        getter_hints = typing.get_type_hints(VariationPoint.getPostBuildVariantConditions)
        assert getter_hints.get("return") == typing.List[PostBuildVariantCondition]

        setter_hints = typing.get_type_hints(VariationPoint.addPostBuildVariantCondition)
        assert setter_hints.get("value") is PostBuildVariantCondition
        assert setter_hints.get("return") is VariationPoint

    def test_sdg_typed_optional_sdg(self):
        """
        Test that sdg (Sdg, 0..1 aggr) is typed Optional[Sdg].
        """
        getter_hints = typing.get_type_hints(VariationPoint.getSdg)
        assert getter_hints.get("return") == typing.Optional[Sdg]

        setter_hints = typing.get_type_hints(VariationPoint.setSdg)
        assert setter_hints.get("value") == typing.Optional[Sdg]
        assert setter_hints.get("return") is VariationPoint

    def test_short_label_typed_identifier(self):
        """
        Test that shortLabel (Identifier, 0..1 attr, atpIdentityContributor) is typed
        Optional[Identifier].
        """
        getter_hints = typing.get_type_hints(VariationPoint.getShortLabel)
        assert getter_hints.get("return") == typing.Optional[Identifier]

        setter_hints = typing.get_type_hints(VariationPoint.setShortLabel)
        assert setter_hints.get("value") == typing.Optional[Identifier]
        assert setter_hints.get("return") is VariationPoint

    def test_sw_syscond_typed_condition_by_formula(self):
        """
        Test that swSyscond (ConditionByFormula, 0..1 aggr) is typed
        Optional[ConditionByFormula].
        """
        getter_hints = typing.get_type_hints(VariationPoint.getSwSyscond)
        assert getter_hints.get("return") == typing.Optional[ConditionByFormula]

        setter_hints = typing.get_type_hints(VariationPoint.setSwSyscond)
        assert setter_hints.get("value") == typing.Optional[ConditionByFormula]
        assert setter_hints.get("return") is VariationPoint

    def test_getter_docstrings_are_notes_without_tags(self):
        """
        Test that getter docstrings are the Table 7.4 Notes verbatim without the
        Tags/Stereotypes suffix.
        """
        assert VariationPoint.getBlueprintCondition.__doc__.strip() == (
            "This represents a description that documents how the variation point shall be "
            "resolved when deriving objects from the blueprint. Note that variationPoints are "
            "not allowed within a blueprintCondition."
        )
        assert VariationPoint.getDesc.__doc__.strip() == "This allows to describe shortly the purpose of the variation point."
        assert VariationPoint.getFormalBlueprintGenerator.__doc__.strip() == (
            "This represents a description that documents how the variation point shall be "
            "resolved when deriving objects from the blueprint by using ARMQL. Note that "
            "variationPoints are not allowed within a formalBlueprintGenerator."
        )
        assert VariationPoint.getPostBuildVariantConditions.__doc__.strip() == (
            "This is the set of post build variant conditions which all shall be fulfilled in " "order to (postbuild) bind the variation point."
        )
        assert VariationPoint.getSdg.__doc__.strip() == (
            "An optional special data group is attached to every variation point. These data "
            "can be used by external software systems to attach application specific data. "
            "For example, a variant management system might add an identifier, an URL or a "
            "specific classifier."
        )
        assert VariationPoint.getShortLabel.__doc__.strip() == (
            "This provides a name to the particular variation point to support the RTE "
            "generator. It is necessary for supporting splitable aggregations and if binding "
            "time is later than codeGenerationTime, as well as some RTE conditions. It needs "
            "to be unique with in the enclosing Identifiables with the same ShortName."
        )
        assert VariationPoint.getSwSyscond.__doc__.strip() == (
            "This condition acts as Binding Function for the Variation Point. Note that the " "multiplicity is 0..1 in order to support pure postBuild variants."
        )

    def test_setter_docstrings_are_notes_with_none_noop(self):
        """
        Test that setter docstrings are the Table 7.4 Notes verbatim plus the None-no-op
        sentence.
        """
        assert VariationPoint.setBlueprintCondition.__doc__.strip() == (
            "This represents a description that documents how the variation point shall be "
            "resolved when deriving objects from the blueprint. Note that variationPoints are "
            "not allowed within a blueprintCondition. A None value is a no-op and does not "
            "overwrite an existing blueprintCondition."
        )
        assert VariationPoint.setDesc.__doc__.strip() == ("This allows to describe shortly the purpose of the variation point. A None value " "is a no-op and does not overwrite an existing desc.")
        assert VariationPoint.setFormalBlueprintGenerator.__doc__.strip() == (
            "This represents a description that documents how the variation point shall be "
            "resolved when deriving objects from the blueprint by using ARMQL. Note that "
            "variationPoints are not allowed within a formalBlueprintGenerator. A None value "
            "is a no-op and does not overwrite an existing formalBlueprintGenerator."
        )
        assert VariationPoint.addPostBuildVariantCondition.__doc__.strip() == (
            "This is the set of post build variant conditions which all shall be fulfilled in " "order to (postbuild) bind the variation point. A None value is a no-op and is " "not appended."
        )
        assert VariationPoint.setSdg.__doc__.strip() == (
            "An optional special data group is attached to every variation point. These data "
            "can be used by external software systems to attach application specific data. "
            "For example, a variant management system might add an identifier, an URL or a "
            "specific classifier. A None value is a no-op and does not overwrite an existing "
            "sdg."
        )
        assert VariationPoint.setShortLabel.__doc__.strip() == (
            "This provides a name to the particular variation point to support the RTE "
            "generator. It is necessary for supporting splitable aggregations and if binding "
            "time is later than codeGenerationTime, as well as some RTE conditions. It needs "
            "to be unique with in the enclosing Identifiables with the same ShortName. A None "
            "value is a no-op and does not overwrite an existing shortLabel."
        )
        assert VariationPoint.setSwSyscond.__doc__.strip() == (
            "This condition acts as Binding Function for the Variation Point. Note that the "
            "multiplicity is 0..1 in order to support pure postBuild variants. A None value "
            "is a no-op and does not overwrite an existing swSyscond."
        )

    def test_defaults(self):
        """
        Test the initial state of a fresh VariationPoint.
        """
        variation_point = VariationPoint()
        assert variation_point.getBlueprintCondition() is None
        assert variation_point.getDesc() is None
        assert variation_point.getFormalBlueprintGenerator() is None
        assert variation_point.getPostBuildVariantConditions() == []
        assert variation_point.getSdg() is None
        assert variation_point.getShortLabel() is None
        assert variation_point.getSwSyscond() is None

    def test_setter_none_noops(self):
        """
        Test that setters ignore None (field values preserved).
        """
        variation_point = VariationPoint()
        block = DocumentationBlock()
        desc = MultiLanguageOverviewParagraph()
        generator = BlueprintGenerator()
        condition = PostBuildVariantCondition()
        sdg = Sdg()
        label = Identifier().setValue("VP_Label")
        syscond = ConditionByFormula()

        variation_point.setBlueprintCondition(block)
        variation_point.setDesc(desc)
        variation_point.setFormalBlueprintGenerator(generator)
        variation_point.addPostBuildVariantCondition(condition)
        variation_point.setSdg(sdg)
        variation_point.setShortLabel(label)
        variation_point.setSwSyscond(syscond)

        assert variation_point.setBlueprintCondition(None) is variation_point
        assert variation_point.setDesc(None) is variation_point
        assert variation_point.setFormalBlueprintGenerator(None) is variation_point
        assert variation_point.addPostBuildVariantCondition(None) is variation_point
        assert variation_point.setSdg(None) is variation_point
        assert variation_point.setShortLabel(None) is variation_point
        assert variation_point.setSwSyscond(None) is variation_point

        assert variation_point.getBlueprintCondition() is block
        assert variation_point.getDesc() is desc
        assert variation_point.getFormalBlueprintGenerator() is generator
        assert variation_point.getPostBuildVariantConditions() == [condition]
        assert variation_point.getSdg() is sdg
        assert variation_point.getShortLabel() is label
        assert variation_point.getSwSyscond() is syscond
