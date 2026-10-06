import typing

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import (
    RuleArguments,
    RuleBasedValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, Integer

CLASS_NOTE = (
    "This meta-class is used to support a rule-based initialization approach for data types with an "
    "array-nature (ApplicationArrayDataType and ImplementationDataType of category ARRAY) or a compound "
    "Application PrimitiveDataType (which also boils down to an array-nature)."
)

ARGUMENTS_NOTE = (
    "This represents the arguments for the RuleBasedValue Specification. "
    "Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=arguments, arguments.variationPoint.short Label "
    "vh.latestBindingTime=preCompileTime xml.sequenceOffset=30"
)
MAX_SIZE_TO_FILL_NOTE = "If a rule is chosen which does not fill until the end, this determines until which size the rule shall " "fill the values. Tags: xml.sequenceOffset=40"
RULE_NOTE = (
    "This denotes the name of the rule of the RuleBasedValue Specification. The rule determines the "
    "calculation specification according which the arguments are used to calculated the values. "
    "Tags: xml.sequenceOffset=20"
)


class TestRuleBasedValueSpecification:
    def test_inheritance(self):
        spec = RuleBasedValueSpecification()
        assert isinstance(spec, ARObject)

    def test_initialization(self):
        spec = RuleBasedValueSpecification()
        assert spec.getArguments() == []
        assert spec.getMaxSizeToFill() is None
        assert spec.getRule() is None

    def test_class_docstring_verbatim(self):
        docstring = RuleBasedValueSpecification.__doc__ or ""
        assert docstring.strip().startswith(CLASS_NOTE)
        assert "[constr_1926]" in docstring
        assert "[constr_1927]" in docstring

    def test_add_get_arguments(self):
        spec = RuleBasedValueSpecification()
        first = RuleArguments()
        second = RuleArguments()

        assert spec.addArgument(first) is spec
        assert spec.addArgument(second) is spec
        assert spec.getArguments() == [first, second]

        spec.addArgument(None)
        assert spec.getArguments() == [first, second]

    def test_get_set_max_size_to_fill(self):
        spec = RuleBasedValueSpecification()
        max_size = Integer().setValue("8")

        assert spec.setMaxSizeToFill(max_size) is spec
        assert spec.getMaxSizeToFill() is max_size

        spec.setMaxSizeToFill(None)
        assert spec.getMaxSizeToFill() is max_size

    def test_get_set_rule(self):
        spec = RuleBasedValueSpecification()
        rule = Identifier().setValue("FILL_UNTIL_END")

        assert spec.setRule(rule) is spec
        assert spec.getRule() is rule

        spec.setRule(None)
        assert spec.getRule() is rule

    def test_accessor_type_annotations(self):
        assert typing.get_type_hints(RuleBasedValueSpecification.addArgument)["argument"] == RuleArguments
        assert typing.get_type_hints(RuleBasedValueSpecification.getArguments)["return"] == typing.List[RuleArguments]

        assert typing.get_type_hints(RuleBasedValueSpecification.setMaxSizeToFill)["value"] == typing.Optional[Integer]
        assert typing.get_type_hints(RuleBasedValueSpecification.getMaxSizeToFill)["return"] == typing.Optional[Integer]

        assert typing.get_type_hints(RuleBasedValueSpecification.setRule)["value"] == typing.Optional[Identifier]
        assert typing.get_type_hints(RuleBasedValueSpecification.getRule)["return"] == typing.Optional[Identifier]

    def test_member_docstrings_verbatim(self):
        spec = RuleBasedValueSpecification()
        assert (spec.getArguments.__doc__ or "").strip() == ARGUMENTS_NOTE
        assert (spec.addArgument.__doc__ or "").strip().split("\n")[0] == ARGUMENTS_NOTE
        assert (spec.getMaxSizeToFill.__doc__ or "").strip() == MAX_SIZE_TO_FILL_NOTE
        assert (spec.setMaxSizeToFill.__doc__ or "").strip().split("\n")[0] == MAX_SIZE_TO_FILL_NOTE
        assert (spec.getRule.__doc__ or "").strip() == RULE_NOTE
        assert (spec.setRule.__doc__ or "").strip().split("\n")[0] == RULE_NOTE
