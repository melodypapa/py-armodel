"""
CommonStructure module re-exports classes from submodules for backward compatibility.
"""

# Import AbstractBlueprintStructure (a light module) first: AbstractStructure imports it,
# and its parent-package initialization must not re-enter AbstractStructure while the
# latter is only partially initialized (see Task 15 bootstrap-cycle fix).
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import AtpBlueprintable  # noqa: F401

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
    ReferenceValueSpecification,
    NumericalRuleBasedValueSpecification,
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
    "ReferenceValueSpecification",
    "NumericalRuleBasedValueSpecification",
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
