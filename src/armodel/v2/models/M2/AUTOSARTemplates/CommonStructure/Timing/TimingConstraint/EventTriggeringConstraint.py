from abc import ABC
from typing import Optional


class EventTriggeringConstraint(TimingConstraint, ABC):
    """
    Describes the occurrence behavior of the referenced timing event. The
    occurrence behavior can only be determined when a mapping from the timing
    events to the implementation can be obtained. However, such an occurrence
    behavior can also be described by the modeler as an assumption or as a
    requirement about the occurrence of the event.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::EventTriggeringConstraint::EventTriggeringConstraint

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 100, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is EventTriggeringConstraint:
            raise TypeError("EventTriggeringConstraint is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The referenced timing event.
        self._event: Optional["TimingDescriptionEvent"] = None

    @property
    def event(self) -> Optional["TimingDescriptionEvent"]:
        """Get event (Pythonic accessor)."""
        return self._event

    @event.setter
    def event(self, value: Optional["TimingDescriptionEvent"]) -> None:
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

        if not isinstance(value, TimingDescriptionEvent):
            raise TypeError(
                f"event must be TimingDescriptionEvent or None, got {type(value).__name__}"
            )
        self._event = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEvent(self) -> "TimingDescriptionEvent":
        """
        AUTOSAR-compliant getter for event.

        Returns:
            The event value

        Note:
            Delegates to event property (CODING_RULE_V2_00017)
        """
        return self.event  # Delegates to property

    def setEvent(self, value: "TimingDescriptionEvent") -> "EventTriggeringConstraint":
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_event(self, value: Optional["TimingDescriptionEvent"]) -> "EventTriggeringConstraint":
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
