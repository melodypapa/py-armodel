"""
This module contains timing description classes for AUTOSAR models.
"""

from abc import ABC
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents import (  # noqa: F401
    AutosarOperationArgumentInstance,
    AutosarVariableInstance,
    OperationArgumentInComponentInstanceRef,
    TDEventOccurrenceExpression,
    TDEventVariableDataPrototypeTypeEnum,
    TDEventOperationTypeEnum,
    TDEventModeDeclarationTypeEnum,
    TDEventTriggerTypeEnum,
    VariableInComponentInstanceRef,
)


class TimingDescription(Identifiable, ABC):
    """
    The abstract parent class of the model elements that are used to define the scope of a timing constraint.
    """

    # TimingDescription method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table D.62, p.253
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self, parent, short_name: str):
        if type(self) is TimingDescription:
            raise TypeError("TimingDescription is an abstract class.")

        super().__init__(parent, short_name)


class TimingDescriptionEvent(TimingDescription, ABC):
    """
    A timing event is the abstract representation of a specific system behavior - that can be observed at runtime - in the AUTOSAR specification. Timing events are used to define the scope for timing constraints. Depending on the specific scope, the view on the system, and the level of abstraction different types of events are defined. In order to avoid confusion with existing event descriptions in the AUTOSAR templates the timing specific event types use the prefix TD.
    """

    # TimingDescriptionEvent method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table D.63, p.253
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getClockReferenceRef         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setClockReferenceRef         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getOccurrenceExpression      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setOccurrenceExpression      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent, short_name: str):
        if type(self) is TimingDescriptionEvent:
            raise TypeError("TimingDescriptionEvent is an abstract class.")

        super().__init__(parent, short_name)

        # Optional reference to a clock that holds the time base for an TD event. Tags: atp.Status=draft
        self.clockReferenceRef: Optional[RefType] = None

        # The occurrence expression for this event.
        self.occurrenceExpression: Optional[TDEventOccurrenceExpression] = None

    def getClockReferenceRef(self) -> Optional[RefType]:
        """Optional reference to a clock that holds the time base for an TD event. Tags: atp.Status=draft"""
        return self.clockReferenceRef

    def setClockReferenceRef(self, value: Optional[RefType]) -> "TimingDescriptionEvent":
        """Optional reference to a clock that holds the time base for an TD event. Tags: atp.Status=draft. A None value is a no-op and does not overwrite an existing clockReferenceRef."""
        if value is not None:
            self.clockReferenceRef = value
        return self

    def getOccurrenceExpression(self) -> Optional[TDEventOccurrenceExpression]:
        """The occurrence expression for this event."""
        return self.occurrenceExpression

    def setOccurrenceExpression(self, value: Optional[TDEventOccurrenceExpression]) -> "TimingDescriptionEvent":
        """The occurrence expression for this event. A None value is a no-op and does not overwrite an existing occurrenceExpression."""
        if value is not None:
            self.occurrenceExpression = value
        return self


__all__ = [
    "AutosarOperationArgumentInstance",
    "AutosarVariableInstance",
    "OperationArgumentInComponentInstanceRef",
    "VariableInComponentInstanceRef",
    "TDEventOccurrenceExpression",
    "TimingDescription",
    "TimingDescriptionEvent",
]
