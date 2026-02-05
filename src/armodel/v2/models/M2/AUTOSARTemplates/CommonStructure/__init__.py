"""
CommonStructure module re-exports classes from submodules for backward compatibility.
"""

# Re-export ValueSpecification classes from Constants submodule
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Constants import (
    ApplicationValueSpecification,
    ArrayValueSpecification,
    CompositeRuleBasedValueArgument,
    CompositeValueSpecification,
    ConstantReference,
    ConstantSpecification,
    NumericalValueSpecification,
    RecordValueSpecification,
    TextValueSpecification,
    ValueSpecification,
)

__all__ = [
    "ApplicationValueSpecification",
    "ArrayValueSpecification",
    "CompositeRuleBasedValueArgument",
    "CompositeValueSpecification",
    "ConstantReference",
    "ConstantSpecification",
    "NumericalValueSpecification",
    "RecordValueSpecification",
    "TextValueSpecification",
    "ValueSpecification",
]
