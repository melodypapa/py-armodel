import pytest

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import (
    AbstractRuleBasedValueSpecification,
    CompositeRuleBasedValueSpecification,
    ValueSpecification,
)


class TestAbstractRuleBasedValueSpecification:
    def test_abstract_class_cannot_be_instantiated(self):
        """Test that AbstractRuleBasedValueSpecification abstract class cannot be instantiated directly"""
        with pytest.raises(TypeError, match="AbstractRuleBasedValueSpecification is an abstract class"):
            AbstractRuleBasedValueSpecification()

    def test_concrete_subclass_inheritance(self):
        """Test that a concrete subclass inherits from AbstractRuleBasedValueSpecification and ValueSpecification"""
        spec = CompositeRuleBasedValueSpecification()
        assert isinstance(spec, AbstractRuleBasedValueSpecification)
        assert isinstance(spec, ValueSpecification)

    def test_concrete_subclass_initialization(self):
        """Test that a concrete subclass of AbstractRuleBasedValueSpecification initializes without members"""
        spec = CompositeRuleBasedValueSpecification()
        assert spec is not None
