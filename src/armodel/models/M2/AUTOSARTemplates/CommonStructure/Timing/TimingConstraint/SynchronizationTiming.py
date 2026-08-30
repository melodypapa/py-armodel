"""
This module defines synchronization timing constraints in AUTOSAR timing specifications.

Synchronization timing constraints specify timing requirements for
synchronization between AUTOSAR elements.

Classes:
    SynchronizationTimingConstraint: Specifies synchronization timing requirements
    SynchronizationTypeEnum: Enumeration for synchronization types
    EventOccurrenceKindEnum: Enumeration for event occurrence kinds
"""

from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime import (
    MultidimensionalTime,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint import TimingConstraint


class SynchronizationTypeEnum(AREnum):
    """
    Specifies the synchronizationConstraintType for a SynchronizationTimingConstraint .
    """

    # SynchronizationTypeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.55, p.93
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on SynchronizationTimingConstraint.synchronizationConstraintType
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    # In case that the Synchronization Timing Constraint is specified for event chains, the response events of the associated event chains shall occur synchronously with respect to the specified tolerance.
    # All associated event chains shall have the same stimulus event. In case that the Synchronization Timing Constraint is specified for events, the associated events shall occur synchronously with respect to the specified tolerance.
    # All associated events represent the response events of a common stimulus event, even such a stimulus event is not known yet or not available in the scope of the model.
    # Tags: atp.EnumerationLiteralIndex=0
    RESPONSE_SYNCHRONIZATION = "responseSynchronization"

    # In case that the Synchronization Timing Constraint is specified for event chains, the stimulus events of the associated event chains shall occur synchronously with respect to the specified tolerance.
    # All associated event chains shall have the same response event. In case that the Synchronization Timing Constraint is specified for events, the associated events shall occur synchronously with respect to the specified tolerance.
    # All associated events represent the stimulus events of a common response event, even such a response event is not known yet or not available in the scope of the model.
    # Tags: atp.EnumerationLiteralIndex=1
    STIMULUS_SYNCHRONIZATION = "stimulusSynchronization"

    def __init__(self):
        """
        Initializes the SynchronizationTypeEnum with valid values.
        """
        super().__init__(
            (
                SynchronizationTypeEnum.RESPONSE_SYNCHRONIZATION,
                SynchronizationTypeEnum.STIMULUS_SYNCHRONIZATION,
            )
        )


class EventOccurrenceKindEnum(AREnum):
    """
    Specifies the eventOccurrenceKind for a SynchronizationTimingConstraint .
    """

    # EventOccurrenceKindEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.56, p.93
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on SynchronizationTimingConstraint.eventOccurrenceKind
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    # Specifies that an event may occur more than once in a given time interval.
    # Tags: atp.EnumerationLiteralIndex=0
    MULTIPLE_OCCURRENCES = "multipleOccurrences"

    # The referenced event shall occur only once in a given time interval. Indicates whether the referenced events shall occur only once (single occurrence) or multiple times (multiple occurrences) in the given time interval.
    # Tags: atp.EnumerationLiteralIndex=1
    SINGLE_OCCURRENCE = "singleOccurrence"

    def __init__(self):
        """
        Initializes the EventOccurrenceKindEnum with valid values.
        """
        super().__init__(
            (
                EventOccurrenceKindEnum.MULTIPLE_OCCURRENCES,
                EventOccurrenceKindEnum.SINGLE_OCCURRENCE,
            )
        )


class SynchronizationTimingConstraint(TimingConstraint):
    """
    This constraint is used to restrict the timing behavior of different, but correlated events or event chains,
    with regard to synchronization. Two scenarios are supported: • If ( synchronizationConstraintType ==
    responseSynchronization ) - TimingDescriptionEvent s: An arbitrary number of correlated events which play the role of
    responses shall occur synchronously with respect to a predefined tolerance. - TimingDescriptionEventChain s: An
    arbitrary number of correlated event chains with a common stimulus, but different responses, where the responses
    shall occur synchronously with respect to a predefined tolerance. • If ( synchronizationConstraintType ==
    stimulusSynchronization ) - TimingDescriptionEvent s:An arbitrary number of correlated events which play the role of
    stimuli shall occur synchronously with respect to a predefined tolerance. - TimingDescriptionEventChain s: An
    arbitrary number of correlated event chains with a common response, but different stimuli, where the stimuli shall
    occur synchronously with respect to a predefined tolerance. In case the constraint is imposed on events the following
    two scenarios are supported: • If ( eventOccurrenceKind == singleOccurrence ): any of the events shall occur only once
    in the given time interval. • If ( eventOccurrenceKind == multipleOccurrences ): any of the events may occur more than
    once in the given time interval. In other words multiple occurrences of an event within the given time

    [constr_4522] SynchronizationTimingConstraint shall either reference events or event chains: The SynchronizationTimingConstraint
    shall either reference TimingDescriptionEvent s or TimingDescriptionEventChain s, but not both at the same time.
    [constr_4514] SynchronizationTimingConstraint shall reference at least two event chains: In the case, that the
    SynchronizationTimingConstraint is imposed on TimingDescriptionEventChain s then at least two (2) TimingDescriptionEventChain s
    shall be referenced.
    [constr_4521] Specifying attribute synchronizationConstraintType: The attribute synchronizationConstraintType shall be specified
    if the SynchronizationTimingConstraint is imposed on TimingDescriptionEventChain s.
    """

    # SynchronizationTimingConstraint method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.54, p.92
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getEventOccurrenceKind           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setEventOccurrenceKind           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] addScope                         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getScopes                        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addScopeEvent                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getScopeEvents                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getSynchronizationConstraintType [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSynchronizationConstraintType [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTolerance                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTolerance                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)

        # Indicates whether the referenced events shall occur only once (single occurrence) or multiple times (multiple occurrences) in the given time interval.
        self.eventOccurrenceKind: Optional[EventOccurrenceKindEnum] = None

        # The event chains that are in the scope of the constraint. Mutually exclusive to scopeEvent , see ([constr_4522]).
        self.scopeRefs: List[RefType] = []

        # The events that are in the scope of the constraint. Mutually exclusive to scope , see ([constr_4522])
        self.scopeEventRefs: List[RefType] = []

        # Indicates whether the associated events of the SynchronizationTimingConstraint have a common stimulus or response.
        self.synchronizationConstraintType: Optional[SynchronizationTypeEnum] = None

        # The maximum time interval, within which the synchronized events shall occur. The events may occur in any order within this time interval. The time interval starts at the point-in-time when one of the referenced events occurs.
        self.tolerance: Optional[MultidimensionalTime] = None

    def getEventOccurrenceKind(self) -> Optional[EventOccurrenceKindEnum]:
        """Indicates whether the referenced events shall occur only once (single occurrence) or multiple times (multiple occurrences) in the given time interval."""
        return self.eventOccurrenceKind

    def setEventOccurrenceKind(self, value: Optional[EventOccurrenceKindEnum]) -> "SynchronizationTimingConstraint":
        """Indicates whether the referenced events shall occur only once (single occurrence) or multiple times (multiple occurrences) in the given time interval. A None value is a no-op and does not overwrite an existing eventOccurrenceKind."""
        if value is not None:
            self.eventOccurrenceKind = value
        return self

    def addScope(self, value: Optional[RefType]) -> "SynchronizationTimingConstraint":
        """The event chains that are in the scope of the constraint. Mutually exclusive to scopeEvent , see ([constr_4522]). A None value is a no-op."""
        if value is not None:
            self.scopeRefs.append(value)
        return self

    def getScopes(self) -> List[RefType]:
        """The event chains that are in the scope of the constraint. Mutually exclusive to scopeEvent , see ([constr_4522])."""
        return self.scopeRefs

    def addScopeEvent(self, value: Optional[RefType]) -> "SynchronizationTimingConstraint":
        """The events that are in the scope of the constraint. Mutually exclusive to scope , see ([constr_4522]). A None value is a no-op."""
        if value is not None:
            self.scopeEventRefs.append(value)
        return self

    def getScopeEvents(self) -> List[RefType]:
        """The events that are in the scope of the constraint. Mutually exclusive to scope , see ([constr_4522])."""
        return self.scopeEventRefs

    def getSynchronizationConstraintType(self) -> Optional[SynchronizationTypeEnum]:
        """Indicates whether the associated events of the SynchronizationTimingConstraint have a common stimulus or response."""
        return self.synchronizationConstraintType

    def setSynchronizationConstraintType(self, value: Optional[SynchronizationTypeEnum]) -> "SynchronizationTimingConstraint":
        """Indicates whether the associated events of the SynchronizationTimingConstraint have a common stimulus or response. A None value is a no-op and does not overwrite an existing synchronizationConstraintType."""
        if value is not None:
            self.synchronizationConstraintType = value
        return self

    def getTolerance(self) -> Optional[MultidimensionalTime]:
        """The maximum time interval, within which the synchronized events shall occur. The events may occur in any order within this time interval. The time interval starts at the point-in-time when one of the referenced events occurs."""
        return self.tolerance

    def setTolerance(self, value: Optional[MultidimensionalTime]) -> "SynchronizationTimingConstraint":
        """The maximum time interval, within which the synchronized events shall occur. The events may occur in any order within this time interval. The time interval starts at the point-in-time when one of the referenced events occurs. A None value is a no-op and does not overwrite an existing tolerance."""
        if value is not None:
            self.tolerance = value
        return self
