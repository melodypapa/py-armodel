"""Tests for the CompositeRuleBasedValueSpecification model class."""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import (
    ApplicationRuleBasedValueSpecification,
    ArrayValueSpecification,
    CompositeRuleBasedValueSpecification,
    RecordValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, PositiveInteger


class TestCompositeRuleBasedValueSpecification:
    """Test class for CompositeRuleBasedValueSpecification class."""

    def test_initialization(self):
        """Test CompositeRuleBasedValueSpecification initialization defaults."""
        spec = CompositeRuleBasedValueSpecification()
        assert spec.arguments == []
        assert spec.compoundPrimitiveArguments == []
        assert spec.maxSizeToFill is None
        assert spec.rule is None

    def test_add_get_arguments(self):
        """Test addArgument/getArguments append, return value and None no-op."""
        spec = CompositeRuleBasedValueSpecification()
        assert spec.getArguments() == []

        argument1 = ArrayValueSpecification()
        assert spec.addArgument(argument1) is spec
        argument2 = RecordValueSpecification()
        spec.addArgument(argument2)
        assert spec.getArguments() == [argument1, argument2]

        spec.addArgument(None)
        assert spec.getArguments() == [argument1, argument2]

    def test_add_get_compound_primitive_arguments(self):
        """Test addCompoundPrimitiveArgument/getCompoundPrimitiveArguments append, return value and None no-op."""
        spec = CompositeRuleBasedValueSpecification()
        assert spec.getCompoundPrimitiveArguments() == []

        argument1 = ApplicationRuleBasedValueSpecification()
        assert spec.addCompoundPrimitiveArgument(argument1) is spec
        assert spec.getCompoundPrimitiveArguments() == [argument1]

        spec.addCompoundPrimitiveArgument(None)
        assert spec.getCompoundPrimitiveArguments() == [argument1]

    def test_get_set_max_size_to_fill(self):
        """Test getMaxSizeToFill/setMaxSizeToFill round-trip and None no-op."""
        spec = CompositeRuleBasedValueSpecification()
        assert spec.getMaxSizeToFill() is None

        value = PositiveInteger().setValue("4")
        assert spec.setMaxSizeToFill(value) is spec
        assert spec.getMaxSizeToFill() == value

        spec.setMaxSizeToFill(None)
        assert spec.getMaxSizeToFill() == value

    def test_get_set_rule(self):
        """Test getRule/setRule round-trip and None no-op."""
        spec = CompositeRuleBasedValueSpecification()
        assert spec.getRule() is None

        rule = Identifier().setValue("INCREASE")
        assert spec.setRule(rule) is spec
        assert spec.getRule() == rule

        spec.setRule(None)
        assert spec.getRule() == rule
