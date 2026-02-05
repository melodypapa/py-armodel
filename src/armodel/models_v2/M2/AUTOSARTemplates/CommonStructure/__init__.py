"""
CommonStructure module re-exports classes from submodules for backward compatibility.
"""

# Re-export ValueSpecification classes from Constants submodule
from armodel.models_v2.M2.AUTOSARTemplates.CommonStructure.Constants import (

__all__ = []

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
