import typing

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import (
    AbstractRuleBasedValueSpecification,
    NumericalRuleBasedValueSpecification,
    RuleBasedValueSpecification,
    ValueSpecification,
)

CLASS_NOTE = "This meta-class is used to support a rule-based initialization approach for data types with an " "array-nature (ImplementationDataType of category ARRAY)."

RULE_BASED_VALUES_NOTE = "This represents the rule based value specification for the array. " "Tags: xml.roleElement=true xml.roleWrapperElement=false xml.typeWrapperElement=false"


class TestNumericalRuleBasedValueSpecification:
    def test_inheritance(self):
        spec = NumericalRuleBasedValueSpecification()
        assert isinstance(spec, AbstractRuleBasedValueSpecification)
        assert isinstance(spec, ValueSpecification)

    def test_initialization(self):
        spec = NumericalRuleBasedValueSpecification()
        assert spec.getRuleBasedValues() is None

    def test_class_docstring_verbatim(self):
        docstring = NumericalRuleBasedValueSpecification.__doc__ or ""
        assert docstring.strip().startswith(CLASS_NOTE)
        assert "[constr_1925]" in docstring

    def test_get_set_rule_based_values(self):
        spec = NumericalRuleBasedValueSpecification()
        value = RuleBasedValueSpecification()

        assert spec.setRuleBasedValues(value) is spec
        assert spec.getRuleBasedValues() is value

        spec.setRuleBasedValues(None)
        assert spec.getRuleBasedValues() is value

    def test_accessor_type_annotations(self):
        assert typing.get_type_hints(NumericalRuleBasedValueSpecification.setRuleBasedValues)["value"] == typing.Optional[RuleBasedValueSpecification]
        assert typing.get_type_hints(NumericalRuleBasedValueSpecification.getRuleBasedValues)["return"] == typing.Optional[RuleBasedValueSpecification]

    def test_member_docstrings_verbatim(self):
        spec = NumericalRuleBasedValueSpecification()
        assert (spec.getRuleBasedValues.__doc__ or "").strip() == RULE_BASED_VALUES_NOTE
        assert (spec.setRuleBasedValues.__doc__ or "").strip().split("\n")[0] == RULE_BASED_VALUES_NOTE
