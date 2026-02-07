"""
This module defines synchronization timing constraints in AUTOSAR timing specifications.

Synchronization timing constraints specify timing requirements for
synchronization between AUTOSAR elements.

Classes:
    SynchronizationTimingConstraint: Specifies synchronization timing requirements
    SynchronizationTypeEnum: Enumeration for synchronization types
    EventOccurrenceKindEnum: Enumeration for event occurrence kinds
"""

from typing import Union

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.TimingConstraint import (
    TimingConstraint,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)


class SynchronizationTypeEnum(AREnum):
    """
    Enumeration for synchronization types.
    """

    HARD_SYNCHRONIZATION = "hard-synchronization"
    SOFT_SYNCHRONIZATION = "soft-synchronization"
    NO_SYNCHRONIZATION = "no-synchronization"

    def __init__(self) -> None:
        super().__init__([
            SynchronizationTypeEnum.HARD_SYNCHRONIZATION,
            SynchronizationTypeEnum.SOFT_SYNCHRONIZATION,
            SynchronizationTypeEnum.NO_SYNCHRONIZATION,
        ])


class EventOccurrenceKindEnum(AREnum):
    """
    Enumeration for event occurrence kinds.
    """

    START = "start"
    END = "end"
    START_AND_END = "start-and-end"

    def __init__(self) -> None:
        super().__init__([
            EventOccurrenceKindEnum.START,
            EventOccurrenceKindEnum.END,
            EventOccurrenceKindEnum.START_AND_END,
        ])


class SynchronizationTimingConstraint(TimingConstraint):
    """
    Specifies synchronization timing requirements in AUTOSAR timing specifications.
    This constraint defines timing requirements for synchronization between
    AUTOSAR elements.
    """

    def __init__(self, parent, short_name: str) -> None:
        """
        Initializes the SynchronizationTimingConstraint with a parent and short name.

        Args:
            parent: The parent ARObject that contains this synchronization timing constraint
            short_name: The unique short name of this synchronization timing constraint
        """
        super().__init__(parent, short_name)

        # Type of synchronization
        self.synchronization_type: Union[Union[SynchronizationTypeEnum, None] , None] = None
        # Event occurrence kind
        self.event_occurrence_kind: Union[Union[EventOccurrenceKindEnum, None] , None] = None

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
