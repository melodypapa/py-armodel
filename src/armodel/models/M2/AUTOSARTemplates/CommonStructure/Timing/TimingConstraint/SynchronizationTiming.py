"""
This module defines synchronization timing constraints in AUTOSAR timing specifications.

Synchronization timing constraints specify timing requirements for
synchronization between AUTOSAR elements.

Classes:
    SynchronizationTimingConstraint: Specifies synchronization timing requirements
    SynchronizationTypeEnum: Enumeration for synchronization types
    EventOccurrenceKindEnum: Enumeration for event occurrence kinds
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint import TimingConstraint


class SynchronizationTypeEnum(AREnum):
    """
    Specifies the synchronizationConstraintType for a SynchronizationTimingConstraint .
    """

    # SynchronizationTypeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.55, p.93
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
    Specifies synchronization timing requirements in AUTOSAR timing specifications.
    This constraint defines timing requirements for synchronization between
    AUTOSAR elements.
    """

    # SynchronizationTimingConstraint method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test
    # [ ] getSynchronizationType       [x] impl  [x] docstring  [ ] test
    # [ ] setSynchronizationType       [x] impl  [x] docstring  [ ] test
    # [ ] getEventOccurrenceKind       [x] impl  [x] docstring  [ ] test
    # [ ] setEventOccurrenceKind       [x] impl  [x] docstring  [ ] test

    def __init__(self, parent, short_name: str):
        """
        Initializes the SynchronizationTimingConstraint with a parent and short name.

        Args:
            parent: The parent ARObject that contains this synchronization timing constraint
            short_name: The unique short name of this synchronization timing constraint
        """
        super().__init__(parent, short_name)

        # Type of synchronization
        self.synchronization_type: SynchronizationTypeEnum = None
        # Event occurrence kind
        self.event_occurrence_kind: EventOccurrenceKindEnum = None

    def getSynchronizationType(self):
        """
        Gets the synchronization type.

        Returns:
            SynchronizationTypeEnum: The synchronization type
        """
        return self.synchronization_type

    def setSynchronizationType(self, value):
        """
        Sets the synchronization type.

        Args:
            value: The synchronization type to set

        Returns:
            self for method chaining
        """
        self.synchronization_type = value
        return self

    def getEventOccurrenceKind(self):
        """
        Gets the event occurrence kind.

        Returns:
            EventOccurrenceKindEnum: The event occurrence kind
        """
        return self.event_occurrence_kind

    def setEventOccurrenceKind(self, value):
        """
        Sets the event occurrence kind.

        Args:
            value: The event occurrence kind to set

        Returns:
            self for method chaining
        """
        self.event_occurrence_kind = value
        return self
