from typing import Optional


class DiagnosticEventToDebounceAlgorithmMapping(DiagnosticMapping):
    """
    Defines which Debounce Algorithm is applicable for a DiagnosticEvent.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::DiagnosticEventToDebounceAlgorithmMapping

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 246, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to a DebounceAlgorithm assigned to a DiagnosticEvent.
        self._debounce: Optional["DiagnosticDebounce"] = None

    @property
    def debounce(self) -> Optional["DiagnosticDebounce"]:
        """Get debounce (Pythonic accessor)."""
        return self._debounce

    @debounce.setter
    def debounce(self, value: Optional["DiagnosticDebounce"]) -> None:
        """
        Set debounce with validation.

        Args:
            value: The debounce to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._debounce = None
            return

        if not isinstance(value, DiagnosticDebounce):
            raise TypeError(
                f"debounce must be DiagnosticDebounce or None, got {type(value).__name__}"
            )
        self._debounce = value
        # Reference to a DiagnosticEvent to which a Debounce assigned.
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

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDebounce(self) -> "DiagnosticDebounce":
        """
        AUTOSAR-compliant getter for debounce.

        Returns:
            The debounce value

        Note:
            Delegates to debounce property (CODING_RULE_V2_00017)
        """
        return self.debounce  # Delegates to property

    def setDebounce(self, value: "DiagnosticDebounce") -> "DiagnosticEventToDebounceAlgorithmMapping":
        """
        AUTOSAR-compliant setter for debounce with method chaining.

        Args:
            value: The debounce to set

        Returns:
            self for method chaining

        Note:
            Delegates to debounce property setter (gets validation automatically)
        """
        self.debounce = value  # Delegates to property setter
        return self

    def getDiagnosticEvent(self) -> "DiagnosticEvent":
        """
        AUTOSAR-compliant getter for diagnosticEvent.

        Returns:
            The diagnosticEvent value

        Note:
            Delegates to diagnostic_event property (CODING_RULE_V2_00017)
        """
        return self.diagnostic_event  # Delegates to property

    def setDiagnosticEvent(self, value: "DiagnosticEvent") -> "DiagnosticEventToDebounceAlgorithmMapping":
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_debounce(self, value: Optional["DiagnosticDebounce"]) -> "DiagnosticEventToDebounceAlgorithmMapping":
        """
        Set debounce and return self for chaining.

        Args:
            value: The debounce to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_debounce("value")
        """
        self.debounce = value  # Use property setter (gets validation)
        return self

    def with_diagnostic_event(self, value: Optional["DiagnosticEvent"]) -> "DiagnosticEventToDebounceAlgorithmMapping":
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
