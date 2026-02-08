from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    DiagnosticEvent,
    DiagnosticMapping,
    DiagnosticOperation,
)


class DiagnosticEventToOperationCycleMapping(DiagnosticMapping):
    """
    Defines which OperationCycle is applicable for a DiagnosticEvent.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::DiagnosticEventToOperationCycleMapping

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 245, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to a DiagnosticEvent to which an Operation assigned.
        self._diagnosticEvent: Optional["DiagnosticEvent"] = None

    @property
    def diagnostic_event(self) -> Optional["DiagnosticEvent"]:
        """Get diagnosticEvent (Pythonic accessor)."""
        return self._diagnosticEvent

    @diagnostic_event.setter
    def diagnostic_event(self, value: Optional["DiagnosticEvent"]) -> None:
        """
        Set diagnosticEvent with validation.

        Args:
            value: The diagnosticEvent to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._diagnosticEvent = None
            return

        if not isinstance(value, DiagnosticEvent):
            raise TypeError(
                f"diagnosticEvent must be DiagnosticEvent or None, got {type(value).__name__}"
            )
        self._diagnosticEvent = value
        # Reference to an OperationCycle assigned to a Diagnostic.
        self._operationCycle: Optional["DiagnosticOperation"] = None

    @property
    def operation_cycle(self) -> Optional["DiagnosticOperation"]:
        """Get operationCycle (Pythonic accessor)."""
        return self._operationCycle

    @operation_cycle.setter
    def operation_cycle(self, value: Optional["DiagnosticOperation"]) -> None:
        """
        Set operationCycle with validation.

        Args:
            value: The operationCycle to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._operationCycle = None
            return

        if not isinstance(value, DiagnosticOperation):
            raise TypeError(
                f"operationCycle must be DiagnosticOperation or None, got {type(value).__name__}"
            )
        self._operationCycle = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDiagnosticEvent(self) -> "DiagnosticEvent":
        """
        AUTOSAR-compliant getter for diagnosticEvent.

        Returns:
            The diagnosticEvent value

        Note:
            Delegates to diagnostic_event property (CODING_RULE_V2_00017)
        """
        return self.diagnostic_event  # Delegates to property

    def setDiagnosticEvent(self, value: "DiagnosticEvent") -> "DiagnosticEventToOperationCycleMapping":
        """
        AUTOSAR-compliant setter for diagnosticEvent with method chaining.

        Args:
            value: The diagnosticEvent to set

        Returns:
            self for method chaining

        Note:
            Delegates to diagnostic_event property setter (gets validation automatically)
        """
        self.diagnostic_event = value  # Delegates to property setter
        return self

    def getOperationCycle(self) -> "DiagnosticOperation":
        """
        AUTOSAR-compliant getter for operationCycle.

        Returns:
            The operationCycle value

        Note:
            Delegates to operation_cycle property (CODING_RULE_V2_00017)
        """
        return self.operation_cycle  # Delegates to property

    def setOperationCycle(self, value: "DiagnosticOperation") -> "DiagnosticEventToOperationCycleMapping":
        """
        AUTOSAR-compliant setter for operationCycle with method chaining.

        Args:
            value: The operationCycle to set

        Returns:
            self for method chaining

        Note:
            Delegates to operation_cycle property setter (gets validation automatically)
        """
        self.operation_cycle = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_diagnostic_event(self, value: Optional["DiagnosticEvent"]) -> "DiagnosticEventToOperationCycleMapping":
        """
        Set diagnosticEvent and return self for chaining.

        Args:
            value: The diagnosticEvent to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_diagnostic_event("value")
        """
        self.diagnostic_event = value  # Use property setter (gets validation)
        return self

    def with_operation_cycle(self, value: Optional["DiagnosticOperation"]) -> "DiagnosticEventToOperationCycleMapping":
        """
        Set operationCycle and return self for chaining.

        Args:
            value: The operationCycle to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_operation_cycle("value")
        """
        self.operation_cycle = value  # Use property setter (gets validation)
        return self
