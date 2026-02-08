from abc import ABC
from typing import Optional


class TimingDescriptionEvent(TimingDescription, ABC):
    """
    A timing event is the abstract representation of a specific system behavior
    – that can be observed at runtime – in the AUTOSAR specification. Timing
    events are used to define the scope for timing constraints. Depending on the
    specific scope, the view on the system, and the level of abstraction
    different types of events are defined. In order to avoid confusion with
    existing event descriptions in the AUTOSAR templates the timing specific
    event types use the prefix TD.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescriptionEvent

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 253, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is TimingDescriptionEvent:
            raise TypeError("TimingDescriptionEvent is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Optional reference to a clock that holds the time base for event.
        self._clockReference: Optional["TimingClock"] = None

    @property
    def clock_reference(self) -> Optional["TimingClock"]:
        """Get clockReference (Pythonic accessor)."""
        return self._clockReference

    @clock_reference.setter
    def clock_reference(self, value: Optional["TimingClock"]) -> None:
        """
        Set clockReference with validation.

        Args:
            value: The clockReference to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._clockReference = None
            return

        if not isinstance(value, TimingClock):
            raise TypeError(
                f"clockReference must be TimingClock or None, got {type(value).__name__}"
            )
        self._clockReference = value
        # The occurrence expression for this event.
        self._occurrence: Optional["TDEventOccurrence"] = None

    @property
    def occurrence(self) -> Optional["TDEventOccurrence"]:
        """Get occurrence (Pythonic accessor)."""
        return self._occurrence

    @occurrence.setter
    def occurrence(self, value: Optional["TDEventOccurrence"]) -> None:
        """
        Set occurrence with validation.

        Args:
            value: The occurrence to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._occurrence = None
            return

        if not isinstance(value, TDEventOccurrence):
            raise TypeError(
                f"occurrence must be TDEventOccurrence or None, got {type(value).__name__}"
            )
        self._occurrence = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getClockReference(self) -> "TimingClock":
        """
        AUTOSAR-compliant getter for clockReference.

        Returns:
            The clockReference value

        Note:
            Delegates to clock_reference property (CODING_RULE_V2_00017)
        """
        return self.clock_reference  # Delegates to property

    def setClockReference(self, value: "TimingClock") -> "TimingDescriptionEvent":
        """
        AUTOSAR-compliant setter for clockReference with method chaining.

        Args:
            value: The clockReference to set

        Returns:
            self for method chaining

        Note:
            Delegates to clock_reference property setter (gets validation automatically)
        """
        self.clock_reference = value  # Delegates to property setter
        return self

    def getOccurrence(self) -> "TDEventOccurrence":
        """
        AUTOSAR-compliant getter for occurrence.

        Returns:
            The occurrence value

        Note:
            Delegates to occurrence property (CODING_RULE_V2_00017)
        """
        return self.occurrence  # Delegates to property

    def setOccurrence(self, value: "TDEventOccurrence") -> "TimingDescriptionEvent":
        """
        AUTOSAR-compliant setter for occurrence with method chaining.

        Args:
            value: The occurrence to set

        Returns:
            self for method chaining

        Note:
            Delegates to occurrence property setter (gets validation automatically)
        """
        self.occurrence = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_clock_reference(self, value: Optional["TimingClock"]) -> "TimingDescriptionEvent":
        """
        Set clockReference and return self for chaining.

        Args:
            value: The clockReference to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_clock_reference("value")
        """
        self.clock_reference = value  # Use property setter (gets validation)
        return self

    def with_occurrence(self, value: Optional["TDEventOccurrence"]) -> "TimingDescriptionEvent":
        """
        Set occurrence and return self for chaining.

        Args:
            value: The occurrence to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_occurrence("value")
        """
        self.occurrence = value  # Use property setter (gets validation)
        return self
