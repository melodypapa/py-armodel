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
    TDEventBsw,
    TDEventBswModule,
    TDEventBswModuleTypeEnum,
    TDEventBswModeDeclaration,
    TDEventBswModeDeclarationTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventSwcInternalBehavior import (  # noqa: F401
    TDEventSwc,
    TDEventSwcInternalBehavior,
    TDEventSwcInternalBehaviorReference,
    TDEventSwcInternalBehaviorTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventBswInternalBehavior import (  # noqa: F401
    TDEventBswInternalBehavior,
    TDEventBswInternalBehaviorTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventCom import (  # noqa: F401
    TDEventCom,
    TDEventCycleStart,
    TDEventISignal,
    TDEventISignalTypeEnum,
    TDEventIPdu,
    TDEventIPduTypeEnum,
    TDEventFrame,
    TDEventFrameTypeEnum,
    TDEventFrameEthernet,
    TDEventFrameEthernetTypeEnum,
    TDHeaderIdRange,
    TDEventFrClusterCycleStart,
    TDEventTTCanCycleStart,
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
    "TDEventBsw",
    "TDEventBswModule",
    "TDEventBswModeDeclaration",
    "TDEventBswInternalBehaviorTypeEnum",
    "TDEventSwc",
    "TDEventSwcInternalBehavior",
    "TDEventSwcInternalBehaviorReference",
    "TDEventSwcInternalBehaviorTypeEnum",
    "TDEventBswInternalBehavior",
    "TDEventBswInternalBehaviorTypeEnum",
    "TDEventISignalTypeEnum",
    "TDEventISignal",
    "TDEventCom",
    "TDEventCycleStart",
    "TDEventIPdu",
    "TDEventIPduTypeEnum",
    "TDEventFrame",
    "TDEventFrameTypeEnum",
    "TDEventFrameEthernet",
    "TDHeaderIdRange",
    "TDEventFrameEthernetTypeEnum",
    "TDEventFrClusterCycleStart",
    "TDEventTTCanCycleStart",
]
