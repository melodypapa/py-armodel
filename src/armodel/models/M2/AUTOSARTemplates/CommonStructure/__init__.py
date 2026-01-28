"""
CommonStructure module re-exports classes from submodules for backward compatibility.
"""

# Re-export ValueSpecification classes from Constants submodule
from .Constants import (
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
