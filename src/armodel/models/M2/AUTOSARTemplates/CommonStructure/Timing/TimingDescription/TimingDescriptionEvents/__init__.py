"""
This module contains timing description event classes for AUTOSAR models.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventOccurrenceExpression import (  # noqa: F401
    AutosarOperationArgumentInstance,
    AutosarVariableInstance,
    OperationArgumentInComponentInstanceRef,
    TDEventOccurrenceExpression,
    TDEventOccurrenceExpressionFormula,
    VariableInComponentInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventVfb import (  # noqa: F401
    TDEventModeDeclarationTypeEnum,
    TDEventOperationTypeEnum,
    TDEventTriggerTypeEnum,
    TDEventVariableDataPrototypeTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventSwcInternalBehavior import (  # noqa: F401
    TDEventSwcInternalBehaviorTypeEnum,
)

__all__ = [
    "AutosarOperationArgumentInstance",
    "AutosarVariableInstance",
    "OperationArgumentInComponentInstanceRef",
    "TDEventOccurrenceExpression",
    "TDEventOccurrenceExpressionFormula",
    "VariableInComponentInstanceRef",
    "TDEventVariableDataPrototypeTypeEnum",
    "TDEventOperationTypeEnum",
    "TDEventModeDeclarationTypeEnum",
    "TDEventTriggerTypeEnum",
    "TDEventSwcInternalBehaviorTypeEnum",
]
