"""
CommonStructure module re-exports classes from submodules for backward compatibility.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import (
    ValueSpecification,
    CompositeValueSpecification,
    CompositeRuleBasedValueArgument,
    CompositeRuleBasedValueSpecification,
    ApplicationValueSpecification,
    ApplicationRuleBasedValueSpecification,
    RecordValueSpecification,
    TextValueSpecification,
    NumericalValueSpecification,
    ArrayValueSpecification,
    ConstantSpecification,
    ConstantReference,
    RuleBasedAxisCont,
    RuleBasedValueCont,
    RuleArguments,
    RuleBasedValueSpecification,
    NumericalOrText,
)

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import (
    ModeTransition,
    ModeErrorBehavior,
    ModeErrorReactionPolicyEnum,
)

from armodel.models.M2.AUTOSARTemplates.CommonStructure.SignalServiceTranslation import (
    SignalServiceTranslationControlEnum,
    SignalServiceTranslationElementProps,
    SignalServiceTranslationEventProps,
    SignalServiceTranslationProps,
    SignalServiceTranslationPropsSet,
)

__all__ = [
    "ValueSpecification",
    "CompositeValueSpecification",
    "CompositeRuleBasedValueArgument",
    "CompositeRuleBasedValueSpecification",
    "ApplicationValueSpecification",
    "ApplicationRuleBasedValueSpecification",
    "RecordValueSpecification",
    "TextValueSpecification",
    "NumericalValueSpecification",
    "ArrayValueSpecification",
    "ConstantSpecification",
    "ConstantReference",
    "RuleBasedAxisCont",
    "RuleBasedValueCont",
    "RuleArguments",
    "RuleBasedValueSpecification",
    "NumericalOrText",
    "ModeTransition",
    "ModeErrorBehavior",
    "ModeErrorReactionPolicyEnum",
    "SignalServiceTranslationControlEnum",
    "SignalServiceTranslationElementProps",
    "SignalServiceTranslationEventProps",
    "SignalServiceTranslationProps",
    "SignalServiceTranslationPropsSet",
]
