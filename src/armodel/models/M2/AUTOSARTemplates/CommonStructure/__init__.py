"""
CommonStructure module re-exports classes from submodules for backward compatibility.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import (
    ValueSpecification,
    CompositeValueSpecification,
    CompositeRuleBasedValueArgument,
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
)

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import (
    ModeTransition,
    ModeErrorBehavior,
    ModeErrorReactionPolicyEnum,
)

__all__ = [
    "ValueSpecification",
    "CompositeValueSpecification",
    "CompositeRuleBasedValueArgument",
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
    "ModeTransition",
    "ModeErrorBehavior",
    "ModeErrorReactionPolicyEnum",
]
