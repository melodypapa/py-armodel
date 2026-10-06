import pytest

import armodel
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import (
    AbstractRuleBasedValueSpecification,
    CompositeRuleBasedValueSpecification,
    ValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier

CLASS_NOTE = "This represents an abstract base class for all rule-based value specifications."


class ConcreteRuleBasedValueSpecification(AbstractRuleBasedValueSpecification):
    pass


class TestAbstractRuleBasedValueSpecification:
    def test_abstract_class_cannot_be_instantiated(self):
        with pytest.raises(TypeError, match="AbstractRuleBasedValueSpecification is an abstract class"):
            AbstractRuleBasedValueSpecification()

    def test_top_level_export(self):
        assert hasattr(armodel, "AbstractRuleBasedValueSpecification")

    def test_concrete_subclass_inheritance(self):
        spec = ConcreteRuleBasedValueSpecification()
        assert isinstance(spec, AbstractRuleBasedValueSpecification)
        assert isinstance(spec, ValueSpecification)

        composite_spec = CompositeRuleBasedValueSpecification()
        assert isinstance(composite_spec, AbstractRuleBasedValueSpecification)
        assert isinstance(composite_spec, ValueSpecification)

    def test_class_docstring_verbatim(self):
        docstring = AbstractRuleBasedValueSpecification.__doc__ or ""
        assert docstring.strip().startswith(CLASS_NOTE)
        assert "[constr_1779]" in docstring

    def test_concrete_subclass_base_accessors(self):
        spec = ConcreteRuleBasedValueSpecification()
        assert spec.getShortLabel() is None

        short_label = Identifier().setValue("ruleLabel")
        assert spec.setShortLabel(short_label) is spec
        assert spec.getShortLabel() is short_label

        spec.setShortLabel(None)
        assert spec.getShortLabel() is short_label
