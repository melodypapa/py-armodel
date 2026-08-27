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
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventBsw import (  # noqa: F401
    TDEventBswModuleTypeEnum,
    TDEventBswModeDeclarationTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventSwcInternalBehavior import (  # noqa: F401
    TDEventSwc,
    TDEventSwcInternalBehavior,
    TDEventSwcInternalBehaviorReference,
    TDEventSwcInternalBehaviorTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventBswInternalBehavior import (  # noqa: F401
    TDEventBswInternalBehaviorTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventCom import (  # noqa: F401
    TDEventCom,
    TDEventISignal,
    TDEventISignalTypeEnum,
    TDEventIPduTypeEnum,
    TDEventFrameTypeEnum,
    TDEventFrameEthernetTypeEnum,
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
    "TDEventBswModeDeclarationTypeEnum",
    "TDEventBswModuleTypeEnum",
    "TDEventBswInternalBehaviorTypeEnum",
    "TDEventSwc",
    "TDEventSwcInternalBehavior",
    "TDEventSwcInternalBehaviorReference",
    "TDEventSwcInternalBehaviorTypeEnum",
    "TDEventISignalTypeEnum",
    "TDEventISignal",
    "TDEventCom",
    "TDEventIPduTypeEnum",
    "TDEventFrameTypeEnum",
    "TDEventFrameEthernetTypeEnum",
]
