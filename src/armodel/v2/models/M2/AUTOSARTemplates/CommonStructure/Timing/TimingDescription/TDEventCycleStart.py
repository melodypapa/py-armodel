from abc import ABC
from typing import Optional


class TDEventCycleStart(TDEventCom, ABC):
    """
    This is the abstract parent class to describe timing events related to a
    point in time where a communication cycle starts. Via the attribute
    "cycleRepetition", a filtered view to the cycle start can be defined.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription::TDEventCycleStart

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 71, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is TDEventCycleStart:
            raise TypeError("TDEventCycleStart is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The start of every <cycleRepetition> cycle is targeted by.
        self._cycleRepetition: Optional["Integer"] = None

    @property
    def cycle_repetition(self) -> Optional["Integer"]:
        """Get cycleRepetition (Pythonic accessor)."""
        return self._cycleRepetition

    @cycle_repetition.setter
    def cycle_repetition(self, value: Optional["Integer"]) -> None:
        """
        Set cycleRepetition with validation.

        Args:
            value: The cycleRepetition to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._cycleRepetition = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"cycleRepetition must be Integer or None, got {type(value).__name__}"
            )
        self._cycleRepetition = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCycleRepetition(self) -> "Integer":
        """
        AUTOSAR-compliant getter for cycleRepetition.

        Returns:
            The cycleRepetition value

        Note:
            Delegates to cycle_repetition property (CODING_RULE_V2_00017)
        """
        return self.cycle_repetition  # Delegates to property

    def setCycleRepetition(self, value: "Integer") -> "TDEventCycleStart":
        """
        AUTOSAR-compliant setter for cycleRepetition with method chaining.

        Args:
            value: The cycleRepetition to set

        Returns:
            self for method chaining

        Note:
            Delegates to cycle_repetition property setter (gets validation automatically)
        """
        self.cycle_repetition = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_cycle_repetition(self, value: Optional["Integer"]) -> "TDEventCycleStart":
        """
        Set cycleRepetition and return self for chaining.

        Args:
            value: The cycleRepetition to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_cycle_repetition("value")
        """
        self.cycle_repetition = value  # Use property setter (gets validation)
        return self
