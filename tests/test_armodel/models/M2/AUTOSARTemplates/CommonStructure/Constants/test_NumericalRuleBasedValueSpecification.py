from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import (
    AbstractRuleBasedValueSpecification,
    NumericalRuleBasedValueSpecification,
    RuleBasedValueSpecification,
)


class TestNumericalRuleBasedValueSpecification:
    def test_inheritance(self):
        """Test that NumericalRuleBasedValueSpecification inherits from AbstractRuleBasedValueSpecification"""
        spec = NumericalRuleBasedValueSpecification()
        assert isinstance(spec, AbstractRuleBasedValueSpecification)

    def test_initialization(self):
        """Test NumericalRuleBasedValueSpecification initialization defaults"""
        spec = NumericalRuleBasedValueSpecification()
        assert spec is not None
        assert spec.ruleBasedValues is None

    def test_get_rule_based_values(self):
        """Test getRuleBasedValues method"""
        spec = NumericalRuleBasedValueSpecification()
        assert spec.getRuleBasedValues() is None

    def test_set_rule_based_values(self):
        """Test setRuleBasedValues method"""
        spec = NumericalRuleBasedValueSpecification()
        value = RuleBasedValueSpecification()
        result = spec.setRuleBasedValues(value)
        assert result is spec
        assert spec.getRuleBasedValues() is value

    def test_set_rule_based_values_none(self):
        """Test setRuleBasedValues with None value is a no-op"""
        spec = NumericalRuleBasedValueSpecification()
        value = RuleBasedValueSpecification()
        spec.setRuleBasedValues(value)
        result = spec.setRuleBasedValues(None)
        assert result is spec
        assert spec.getRuleBasedValues() is value
