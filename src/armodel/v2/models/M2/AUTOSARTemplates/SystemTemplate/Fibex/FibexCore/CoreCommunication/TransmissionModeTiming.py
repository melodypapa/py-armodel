from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    CyclicTiming,
    EventControlledTiming,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class TransmissionModeTiming(ARObject):
    """
    If the COM Transmission Mode is false the timing is aggregated by the
    TransmissionModeTiming element in the role of transmissionModeFalseTiming.
    If the COM Transmission Mode is true the timing is aggregated by the
    TransmissionModeTiming element in the role of transmissionModeTrueTiming.
    COM supports the following Transmission Modes: • Periodic (Cyclic Timing) •
    Direct /n-times (EventControlledTiming) • Mixed (Cyclic and
    EventControlledTiming are assigned) • None (no timing is assigned)

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::Timing::TransmissionModeTiming

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 393, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Periodic Transmission Mode.
        self._cyclicTiming: Optional["CyclicTiming"] = None

    @property
    def cyclic_timing(self) -> Optional["CyclicTiming"]:
        """Get cyclicTiming (Pythonic accessor)."""
        return self._cyclicTiming

    @cyclic_timing.setter
    def cyclic_timing(self, value: Optional["CyclicTiming"]) -> None:
        """
        Set cyclicTiming with validation.

        Args:
            value: The cyclicTiming to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._cyclicTiming = None
            return

        if not isinstance(value, CyclicTiming):
            raise TypeError(
                f"cyclicTiming must be CyclicTiming or None, got {type(value).__name__}"
            )
        self._cyclicTiming = value
        # Direct Transmission Mode.
        self._eventControlledTiming: Optional["EventControlledTiming"] = None

    @property
    def event_controlled_timing(self) -> Optional["EventControlledTiming"]:
        """Get eventControlledTiming (Pythonic accessor)."""
        return self._eventControlledTiming

    @event_controlled_timing.setter
    def event_controlled_timing(self, value: Optional["EventControlledTiming"]) -> None:
        """
        Set eventControlledTiming with validation.

        Args:
            value: The eventControlledTiming to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._eventControlledTiming = None
            return

        if not isinstance(value, EventControlledTiming):
            raise TypeError(
                f"eventControlledTiming must be EventControlledTiming or None, got {type(value).__name__}"
            )
        self._eventControlledTiming = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCyclicTiming(self) -> "CyclicTiming":
        """
        AUTOSAR-compliant getter for cyclicTiming.

        Returns:
            The cyclicTiming value

        Note:
            Delegates to cyclic_timing property (CODING_RULE_V2_00017)
        """
        return self.cyclic_timing  # Delegates to property

    def setCyclicTiming(self, value: "CyclicTiming") -> "TransmissionModeTiming":
        """
        AUTOSAR-compliant setter for cyclicTiming with method chaining.

        Args:
            value: The cyclicTiming to set

        Returns:
            self for method chaining

        Note:
            Delegates to cyclic_timing property setter (gets validation automatically)
        """
        self.cyclic_timing = value  # Delegates to property setter
        return self

    def getEventControlledTiming(self) -> "EventControlledTiming":
        """
        AUTOSAR-compliant getter for eventControlledTiming.

        Returns:
            The eventControlledTiming value

        Note:
            Delegates to event_controlled_timing property (CODING_RULE_V2_00017)
        """
        return self.event_controlled_timing  # Delegates to property

    def setEventControlledTiming(self, value: "EventControlledTiming") -> "TransmissionModeTiming":
        """
        AUTOSAR-compliant setter for eventControlledTiming with method chaining.

        Args:
            value: The eventControlledTiming to set

        Returns:
            self for method chaining

        Note:
            Delegates to event_controlled_timing property setter (gets validation automatically)
        """
        self.event_controlled_timing = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_cyclic_timing(self, value: Optional["CyclicTiming"]) -> "TransmissionModeTiming":
        """
        Set cyclicTiming and return self for chaining.

        Args:
            value: The cyclicTiming to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_cyclic_timing("value")
        """
        self.cyclic_timing = value  # Use property setter (gets validation)
        return self

    def with_event_controlled_timing(self, value: Optional["EventControlledTiming"]) -> "TransmissionModeTiming":
        """
        Set eventControlledTiming and return self for chaining.

        Args:
            value: The eventControlledTiming to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_event_controlled_timing("value")
        """
        self.event_controlled_timing = value  # Use property setter (gets validation)
        return self
