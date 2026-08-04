"""
CommonStructure module re-exports classes from submodules for backward compatibility.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import (
    ValueSpecification,
    CompositeValueSpecification,
    CompositeRuleBasedValueArgument,
    ApplicationValueSpecification,
    RecordValueSpecification,
    TextValueSpecification,
    NumericalValueSpecification,
    ArrayValueSpecification,
    ConstantSpecification,
    ConstantReference,
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
    "RecordValueSpecification",
    "TextValueSpecification",
    "NumericalValueSpecification",
    "ArrayValueSpecification",
    "ConstantSpecification",
    "ConstantReference",
    "ModeTransition",
    "ModeErrorBehavior",
    "ModeErrorReactionPolicyEnum",
]
