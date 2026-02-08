from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import (
    CommunicationCycle,
)


class CycleCounter(CommunicationCycle):
    """
    The communication cycle where the frame is send is described by the
    attribute "cycleCounter".

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreTopology

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 424, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The communication cycle where the frame described by is sent.
        # If a timing is given in this way the shall specify the cycleCount upper bound
                # and point of total repetition.
        # This incremented at the beginning of each new cycle, 0 to cycleCountMax, and
                # is reset to 0 after a cycleCountMax+1 cycles.
        self._CycleCounter: Optional["Integer"] = None

    @property
    def cycle_counter(self) -> Optional["Integer"]:
        """Get CycleCounter (Pythonic accessor)."""
        return self._CycleCounter

    @cycle_counter.setter
    def cycle_counter(self, value: Optional["Integer"]) -> None:
        """
        Set CycleCounter with validation.

        Args:
            value: The CycleCounter to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._CycleCounter = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"CycleCounter must be Integer or None, got {type(value).__name__}"
            )
        self._CycleCounter = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCycleCounter(self) -> "Integer":
        """
        AUTOSAR-compliant getter for CycleCounter.

        Returns:
            The CycleCounter value

        Note:
            Delegates to cycle_counter property (CODING_RULE_V2_00017)
        """
        return self.cycle_counter  # Delegates to property

    def setCycleCounter(self, value: "Integer") -> "CycleCounter":
        """
        AUTOSAR-compliant setter for CycleCounter with method chaining.

        Args:
            value: The CycleCounter to set

        Returns:
            self for method chaining

        Note:
            Delegates to cycle_counter property setter (gets validation automatically)
        """
        self.cycle_counter = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_cycle_counter(self, value: Optional["Integer"]) -> "CycleCounter":
        """
        Set CycleCounter and return self for chaining.

        Args:
            value: The CycleCounter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_cycle_counter("value")
        """
        self.cycle_counter = value  # Use property setter (gets validation)
        return self
