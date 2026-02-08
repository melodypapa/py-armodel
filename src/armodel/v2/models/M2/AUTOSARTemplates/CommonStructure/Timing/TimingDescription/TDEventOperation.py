from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription import TDEventVfbPort


class TDEventOperation(TDEventVfbPort):
    """
    This is used to describe timing events related to client-server
    communication at VFB level.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription::TDEventOperation

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 55, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The referenced operation.
        self._operation: Optional["ClientServerOperation"] = None

    @property
    def operation(self) -> Optional["ClientServerOperation"]:
        """Get operation (Pythonic accessor)."""
        return self._operation

    @operation.setter
    def operation(self, value: Optional["ClientServerOperation"]) -> None:
        """
        Set operation with validation.

        Args:
            value: The operation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._operation = None
            return

        if not isinstance(value, ClientServerOperation):
            raise TypeError(
                f"operation must be ClientServerOperation or None, got {type(value).__name__}"
            )
        self._operation = value
        # The specific type of this timing event.
        self._tdEvent: Optional["TDEventOperationType"] = None

    @property
    def td_event(self) -> Optional["TDEventOperationType"]:
        """Get tdEvent (Pythonic accessor)."""
        return self._tdEvent

    @td_event.setter
    def td_event(self, value: Optional["TDEventOperationType"]) -> None:
        """
        Set tdEvent with validation.

        Args:
            value: The tdEvent to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tdEvent = None
            return

        if not isinstance(value, TDEventOperationType):
            raise TypeError(
                f"tdEvent must be TDEventOperationType or None, got {type(value).__name__}"
            )
        self._tdEvent = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getOperation(self) -> "ClientServerOperation":
        """
        AUTOSAR-compliant getter for operation.

        Returns:
            The operation value

        Note:
            Delegates to operation property (CODING_RULE_V2_00017)
        """
        return self.operation  # Delegates to property

    def setOperation(self, value: "ClientServerOperation") -> "TDEventOperation":
        """
        AUTOSAR-compliant setter for operation with method chaining.

        Args:
            value: The operation to set

        Returns:
            self for method chaining

        Note:
            Delegates to operation property setter (gets validation automatically)
        """
        self.operation = value  # Delegates to property setter
        return self

    def getTdEvent(self) -> "TDEventOperationType":
        """
        AUTOSAR-compliant getter for tdEvent.

        Returns:
            The tdEvent value

        Note:
            Delegates to td_event property (CODING_RULE_V2_00017)
        """
        return self.td_event  # Delegates to property

    def setTdEvent(self, value: "TDEventOperationType") -> "TDEventOperation":
        """
        AUTOSAR-compliant setter for tdEvent with method chaining.

        Args:
            value: The tdEvent to set

        Returns:
            self for method chaining

        Note:
            Delegates to td_event property setter (gets validation automatically)
        """
        self.td_event = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_operation(self, value: Optional["ClientServerOperation"]) -> "TDEventOperation":
        """
        Set operation and return self for chaining.

        Args:
            value: The operation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_operation("value")
        """
        self.operation = value  # Use property setter (gets validation)
        return self

    def with_td_event(self, value: Optional["TDEventOperationType"]) -> "TDEventOperation":
        """
        Set tdEvent and return self for chaining.

        Args:
            value: The tdEvent to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_td_event("value")
        """
        self.td_event = value  # Use property setter (gets validation)
        return self
