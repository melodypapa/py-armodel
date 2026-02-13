"""
V2 M2::AUTOSARTemplates::CommonStructure package.

This package contains common structure classes for AUTOSAR models.
"""

# Import from submodules
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Implementation import (
    Implementation,
    ImplementationProps,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import (
    AbstractEvent,
    ApiPrincipleEnum,
    ExclusiveArea,
    ExclusiveAreaNestingOrder,
    ExecutableEntity,
    ExecutableEntityActivationReason,
    InternalBehavior,
    ReentrancyLevelEnum,
)

__all__ = [
    # From Implementation
    "Implementation",
    "ImplementationProps",
    # From InternalBehavior
    AbstractEvent,
    ApiPrincipleEnum,
    "ExclusiveArea",
    "ExclusiveAreaNestingOrder",
    "ExecutableEntity",
    "ExecutableEntityActivationReason",
    InternalBehavior,
    "ReentrancyLevelEnum",
]
