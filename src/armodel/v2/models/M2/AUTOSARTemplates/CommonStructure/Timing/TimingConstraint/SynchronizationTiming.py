"""
AUTOSAR Package - SynchronizationTiming

Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::SynchronizationTiming
"""


from __future__ import annotations
from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.__init__ import (
    TimingConstraint,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)


class SynchronizationTimingConstraint(TimingConstraint):
    """
    This constraint is used to restrict the timing behavior of different, but
    correlated events or event chains, with regard to synchronization. Two
    scenarios are supported: • If
    (synchronizationConstraintType==responseSynchronization) –
    TimingDescriptionEvents: An arbitrary number of correlated events which play
    the role of responses shall occur synchronously with respect to a predefined
    tolerance. – TimingDescriptionEventChains: An arbitrary number of correlated
    event chains with a common stimulus, but different responses, where the
    responses shall occur synchronously with respect to a predefined tolerance.
    • If (synchronizationConstraintType==stimulusSynchronization) –
    TimingDescriptionEvents:An arbitrary number of correlated events which play
    the role of stimuli shall occur synchronously with respect to a predefined
    tolerance. – TimingDescriptionEventChains: An arbitrary number of correlated
    event chains with a common response, but different stimuli, where the
    stimuli shall occur synchronously with respect to a predefined tolerance. In
    case the constraint is imposed on events the following two scenarios are
    supported: • If (eventOccurrenceKind==singleOccurrence): any of the events
    shall occur only once in the given time interval. • If
    (eventOccurrenceKind==multipleOccurrences): any of the events may occur more
    than once in the given time interval. In other words multiple occurrences of
    an event within the given time interval are permitted.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::SynchronizationTiming::SynchronizationTimingConstraint

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 92, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Indicates whether the referenced events shall occur only once (single
        # occurrence) or multiple times (multiple the given time interval.
        self._event: Optional["EventOccurrenceKind"] = None

    @property
    def event(self) -> Optional["EventOccurrenceKind"]:
        """Get event (Pythonic accessor)."""
        return self._event

    @event.setter
    def event(self, value: Optional["EventOccurrenceKind"]) -> None:
        """
        Set event with validation.

        Args:
            value: The event to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._event = None
            return

        if not isinstance(value, EventOccurrenceKind):
            raise TypeError(
                f"event must be EventOccurrenceKind or None, got {type(value).__name__}"
            )
        self._event = value
        # exclusive to scopeEvent, see ([constr_4522]).
        self._scope: List[TimingDescriptionEvent] = []

    @property
    def scope(self) -> List[TimingDescriptionEvent]:
        """Get scope (Pythonic accessor)."""
        return self._scope
        # The events that are in the scope of the constraint.
        # to scope, see ([constr_4522]).
        self._scopeEvent: List[TimingDescriptionEvent] = []

    @property
    def scope_event(self) -> List[TimingDescriptionEvent]:
        """Get scopeEvent (Pythonic accessor)."""
        return self._scopeEvent
        # Indicates whether the associated events of the
        # SynchronizationTimingConstraint have a common response.
        self._synchronization: Optional["SynchronizationType"] = None

    @property
    def synchronization(self) -> Optional["SynchronizationType"]:
        """Get synchronization (Pythonic accessor)."""
        return self._synchronization

    @synchronization.setter
    def synchronization(self, value: Optional["SynchronizationType"]) -> None:
        """
        Set synchronization with validation.

        Args:
            value: The synchronization to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._synchronization = None
            return

        if not isinstance(value, SynchronizationType):
            raise TypeError(
                f"synchronization must be SynchronizationType or None, got {type(value).__name__}"
            )
        self._synchronization = value
        # The events may occur in within this time interval.
        # The time interval starts point-in-time when one of the referenced events.
        self._tolerance: Optional["MultidimensionalTime"] = None

    @property
    def tolerance(self) -> Optional["MultidimensionalTime"]:
        """Get tolerance (Pythonic accessor)."""
        return self._tolerance

    @tolerance.setter
    def tolerance(self, value: Optional["MultidimensionalTime"]) -> None:
        """
        Set tolerance with validation.

        Args:
            value: The tolerance to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tolerance = None
            return

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"tolerance must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._tolerance = value

    def with_scope(self, value):
        """
        Set scope and return self for chaining.

        Args:
            value: The scope to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_scope("value")
        """
        self.scope = value  # Use property setter (gets validation)
        return self

    def with_scope_event(self, value):
        """
        Set scope_event and return self for chaining.

        Args:
            value: The scope_event to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_scope_event("value")
        """
        self.scope_event = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEvent(self) -> "EventOccurrenceKind":
        """
        AUTOSAR-compliant getter for event.

        Returns:
            The event value

        Note:
            Delegates to event property (CODING_RULE_V2_00017)
        """
        return self.event  # Delegates to property

    def setEvent(self, value: "EventOccurrenceKind") -> SynchronizationTimingConstraint:
        """
        AUTOSAR-compliant setter for event with method chaining.

        Args:
            value: The event to set

        Returns:
            self for method chaining

        Note:
            Delegates to event property setter (gets validation automatically)
        """
        self.event = value  # Delegates to property setter
        return self

    def getScope(self) -> List[TimingDescriptionEvent]:
        """
        AUTOSAR-compliant getter for scope.

        Returns:
            The scope value

        Note:
            Delegates to scope property (CODING_RULE_V2_00017)
        """
        return self.scope  # Delegates to property

    def getScopeEvent(self) -> List[TimingDescriptionEvent]:
        """
        AUTOSAR-compliant getter for scopeEvent.

        Returns:
            The scopeEvent value

        Note:
            Delegates to scope_event property (CODING_RULE_V2_00017)
        """
        return self.scope_event  # Delegates to property

    def getSynchronization(self) -> "SynchronizationType":
        """
        AUTOSAR-compliant getter for synchronization.

        Returns:
            The synchronization value

        Note:
            Delegates to synchronization property (CODING_RULE_V2_00017)
        """
        return self.synchronization  # Delegates to property

    def setSynchronization(self, value: "SynchronizationType") -> SynchronizationTimingConstraint:
        """
        AUTOSAR-compliant setter for synchronization with method chaining.

        Args:
            value: The synchronization to set

        Returns:
            self for method chaining

        Note:
            Delegates to synchronization property setter (gets validation automatically)
        """
        self.synchronization = value  # Delegates to property setter
        return self

    def getTolerance(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for tolerance.

        Returns:
            The tolerance value

        Note:
            Delegates to tolerance property (CODING_RULE_V2_00017)
        """
        return self.tolerance  # Delegates to property

    def setTolerance(self, value: "MultidimensionalTime") -> SynchronizationTimingConstraint:
        """
        AUTOSAR-compliant setter for tolerance with method chaining.

        Args:
            value: The tolerance to set

        Returns:
            self for method chaining

        Note:
            Delegates to tolerance property setter (gets validation automatically)
        """
        self.tolerance = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_event(self, value: Optional["EventOccurrenceKind"]) -> SynchronizationTimingConstraint:
        """
        Set event and return self for chaining.

        Args:
            value: The event to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_event("value")
        """
        self.event = value  # Use property setter (gets validation)
        return self

    def with_synchronization(self, value: Optional["SynchronizationType"]) -> SynchronizationTimingConstraint:
        """
        Set synchronization and return self for chaining.

        Args:
            value: The synchronization to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_synchronization("value")
        """
        self.synchronization = value  # Use property setter (gets validation)
        return self

    def with_tolerance(self, value: Optional["MultidimensionalTime"]) -> SynchronizationTimingConstraint:
        """
        Set tolerance and return self for chaining.

        Args:
            value: The tolerance to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tolerance("value")
        """
        self.tolerance = value  # Use property setter (gets validation)
        return self


class SynchronizationTypeEnum(AREnum):
    """
    SynchronizationTypeEnum enumeration

Specifies the synchronizationConstraintType for a SynchronizationTimingConstraint. Aggregated by SynchronizationTimingConstraint.synchronizationConstraintType

Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::SynchronizationTiming
    """
    # In case that the Synchronization Timing Constraint is specified for event chains, the response events Synchronization of the associated event chains shall occur synchronously with respect to the specified tolerance. All associated event chains shall have the same stimulus event. In case that the Synchronization Timing Constraint is specified for events, the associated events shall occur synchronously with respect to the specified tolerance. All associated events represent the response events of a common stimulus event, even such a stimulus event is not known yet or not available in the scope of the model.
    response = "0"

    # In case that the Synchronization Timing Constraint is specified for event chains, the stimulus events Synchronization of the associated event chains shall occur synchronously with respect to the specified tolerance. All associated event chains shall have the same response event. In case that the Synchronization Timing Constraint is specified for events, the associated events shall occur synchronously with respect to the specified tolerance. All associated events represent the stimulus events of a common response event, even such a response event is not known yet or not available in the scope of the model.
    stimulus = "1"



class EventOccurrenceKindEnum(AREnum):
    """
    EventOccurrenceKindEnum enumeration

Specifies the eventOccurrenceKind for a SynchronizationTimingConstraint. Aggregated by SynchronizationTimingConstraint.eventOccurrenceKind

Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::SynchronizationTiming
    """
    # Specifies that an event may occur more than once in a given time interval.
    multipleOccurrences = "0"

    # The referenced event shall occur only once in a given time interval. Indicates whether the referenced events shall occur only once (single occurrence) or multiple times
    singleOccurrence = "1"
