"""
CommonStructure module re-exports classes from submodules for backward compatibility.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import (
    ApplicationRuleBasedValueSpecification,
    ApplicationValueSpecification,
    ArrayValueSpecification,
    CompositeRuleBasedValueArgument,
    CompositeValueSpecification,
    ConstantReference,
    ConstantSpecification,
    NumericalValueSpecification,
    RecordValueSpecification,
    RuleArguments,
    RuleBasedAxisCont,
    RuleBasedValueCont,
    RuleBasedValueSpecification,
    TextValueSpecification,
    ValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import (
    ModeErrorBehavior,
    ModeErrorReactionPolicyEnum,
    ModeTransition,
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
