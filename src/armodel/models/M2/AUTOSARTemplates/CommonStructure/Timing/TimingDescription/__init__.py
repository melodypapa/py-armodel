"""
This module contains timing description classes for AUTOSAR models.
"""

from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    RefType,
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
        self.occurrenceExpression: "Optional[TDEventOccurrenceExpression]" = None

    def getClockReferenceRef(self) -> Optional[RefType]:
        """Optional reference to a clock that holds the time base for an TD event. Tags: atp.Status=draft"""
        return self.clockReferenceRef

    def setClockReferenceRef(self, value: Optional[RefType]) -> "TimingDescriptionEvent":
        """Optional reference to a clock that holds the time base for an TD event. Tags: atp.Status=draft. A None value is a no-op and does not overwrite an existing clockReferenceRef."""
        if value is not None:
            self.clockReferenceRef = value
        return self

    def getOccurrenceExpression(self) -> "Optional[TDEventOccurrenceExpression]":
        """The occurrence expression for this event."""
        return self.occurrenceExpression

    def setOccurrenceExpression(self, value: "Optional[TDEventOccurrenceExpression]") -> "TimingDescriptionEvent":
        """The occurrence expression for this event. A None value is a no-op and does not overwrite an existing occurrenceExpression."""
        if value is not None:
            self.occurrenceExpression = value
        return self


class TimingDescriptionEventChain(TimingDescription):
    """
    An event chain describes the causal order for a set of functionally dependent timing events. Each event chain has a well defined stimulus and response, which describe its start and end point. Furthermore, it can be hierarchically decomposed into an arbitrary number of sub-chains, so called ''event chain segments''.
    """

    # TimingDescriptionEventChain method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.13, p.41
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getIsPipeliningPermitted     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setIsPipeliningPermitted     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getStimulusRef               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setStimulusRef               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getResponseRef               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setResponseRef               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] addSegmentRef                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSegmentRefs               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)

        # States whether the scheduled entities in an LET interval shall use pipelined execution or not i.e. "permitted pipelining property" If TRUE, then the scheduled entities must implement pipelining. If FALSE or undefined, no pipelining applies. Tags: atp.Status=draft
        self.isPipeliningPermitted: Optional[Boolean] = None

        # The stimulus event representing the point in time where the event chain is activated. Tags: xml.sequenceOffset=10
        self.stimulusRef: Optional[RefType] = None

        # The response event representing the point in time where the event chain is terminated. Tags: xml.sequenceOffset=20
        self.responseRef: Optional[RefType] = None

        # A composed event chain consists of an arbitrary number of sub-chains. Tags: xml.sequenceOffset=30
        self.segmentRefs: List[RefType] = []

    def getIsPipeliningPermitted(self) -> Optional[Boolean]:
        """States whether the scheduled entities in an LET interval shall use pipelined execution or not i.e. "permitted pipelining property" If TRUE, then the scheduled entities must implement pipelining. If FALSE or undefined, no pipelining applies. Tags: atp.Status=draft"""
        return self.isPipeliningPermitted

    def setIsPipeliningPermitted(self, value: Optional[Boolean]) -> "TimingDescriptionEventChain":
        """States whether the scheduled entities in an LET interval shall use pipelined execution or not i.e. "permitted pipelining property" If TRUE, then the scheduled entities must implement pipelining. If FALSE or undefined, no pipelining applies. Tags: atp.Status=draft. A None value is a no-op and does not overwrite an existing isPipeliningPermitted."""
        if value is not None:
            self.isPipeliningPermitted = value
        return self

    def getStimulusRef(self) -> Optional[RefType]:
        """The stimulus event representing the point in time where the event chain is activated. Tags: xml.sequenceOffset=10"""
        return self.stimulusRef

    def setStimulusRef(self, value: Optional[RefType]) -> "TimingDescriptionEventChain":
        """The stimulus event representing the point in time where the event chain is activated. Tags: xml.sequenceOffset=10. A None value is a no-op and does not overwrite an existing stimulusRef."""
        if value is not None:
            self.stimulusRef = value
        return self

    def getResponseRef(self) -> Optional[RefType]:
        """The response event representing the point in time where the event chain is terminated. Tags: xml.sequenceOffset=20"""
        return self.responseRef

    def setResponseRef(self, value: Optional[RefType]) -> "TimingDescriptionEventChain":
        """The response event representing the point in time where the event chain is terminated. Tags: xml.sequenceOffset=20. A None value is a no-op and does not overwrite an existing responseRef."""
        if value is not None:
            self.responseRef = value
        return self

    def addSegmentRef(self, value: Optional[RefType]) -> "TimingDescriptionEventChain":
        """A composed event chain consists of an arbitrary number of sub-chains. Tags: xml.sequenceOffset=30. A None value is a no-op."""
        if value is not None:
            self.segmentRefs.append(value)
        return self

    def getSegmentRefs(self) -> List[RefType]:
        """A composed event chain consists of an arbitrary number of sub-chains. Tags: xml.sequenceOffset=30"""
        return self.segmentRefs


__all__ = [
    "AutosarOperationArgumentInstance",
    "AutosarVariableInstance",
    "OperationArgumentInComponentInstanceRef",
    "VariableInComponentInstanceRef",
    "TDEventOccurrenceExpression",
    "TimingDescription",
    "TimingDescriptionEvent",
    "TimingDescriptionEventChain",
]


from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventOccurrenceExpression import (  # noqa: F401, E402
    AutosarOperationArgumentInstance,
    AutosarVariableInstance,
    OperationArgumentInComponentInstanceRef,
    TDEventOccurrenceExpression,
    VariableInComponentInstanceRef,
)


