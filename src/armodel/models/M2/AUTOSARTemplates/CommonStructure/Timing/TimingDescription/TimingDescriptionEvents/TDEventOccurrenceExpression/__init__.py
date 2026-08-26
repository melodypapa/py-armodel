"""
This module contains the TDEventOccurrenceExpression package classes for AUTOSAR models.

Per AUTOSAR_00052.xsd these classes belong to
AUTOSAR Templates::CommonStructure::Timing::TimingDescription::TimingDescriptionEvents::TDEventOccurrenceExpression.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventOccurrenceExpression.AutosarOperationArgumentInstance import (
    AutosarOperationArgumentInstance,
)  # noqa: F401
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventOccurrenceExpression.AutosarVariableInstance import (
    AutosarVariableInstance,
)  # noqa: F401
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventOccurrenceExpression.OperationArgumentInComponentInstanceRef import (
    OperationArgumentInComponentInstanceRef,
)  # noqa: F401
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventOccurrenceExpression.VariableInComponentInstanceRef import (
    VariableInComponentInstanceRef,
)  # noqa: F401

__all__ = [
    "AutosarOperationArgumentInstance",
    "AutosarVariableInstance",
    "OperationArgumentInComponentInstanceRef",
    "VariableInComponentInstanceRef",
]
