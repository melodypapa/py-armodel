from typing import Optional


class DiagnosticEventToEnableConditionGroupMapping(DiagnosticMapping):
    """
    Defines which EnableConditionGroup is applicable for a DiagnosticEvent.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::DiagnosticEventToEnableConditionGroupMapping

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 247, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to a DiagnosticEvent to which an Enable assigned.
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
        # Reference to an EnableConditionGroup assigned to a DiagnosticEvent.
        self._enableCondition: Optional["DiagnosticEnable"] = None

    @property
    def enable_condition(self) -> Optional["DiagnosticEnable"]:
        """Get enableCondition (Pythonic accessor)."""
        return self._enableCondition

    @enable_condition.setter
    def enable_condition(self, value: Optional["DiagnosticEnable"]) -> None:
        """
        Set enableCondition with validation.

        Args:
            value: The enableCondition to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._enableCondition = None
            return

        if not isinstance(value, DiagnosticEnable):
            raise TypeError(
                f"enableCondition must be DiagnosticEnable or None, got {type(value).__name__}"
            )
        self._enableCondition = value

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

    def setDiagnosticEvent(self, value: "DiagnosticEvent") -> "DiagnosticEventToEnableConditionGroupMapping":
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

    def getEnableCondition(self) -> "DiagnosticEnable":
        """
        AUTOSAR-compliant getter for enableCondition.

        Returns:
            The enableCondition value

        Note:
            Delegates to enable_condition property (CODING_RULE_V2_00017)
        """
        return self.enable_condition  # Delegates to property

    def setEnableCondition(self, value: "DiagnosticEnable") -> "DiagnosticEventToEnableConditionGroupMapping":
        """
        AUTOSAR-compliant setter for enableCondition with method chaining.

        Args:
            value: The enableCondition to set

        Returns:
            self for method chaining

        Note:
            Delegates to enable_condition property setter (gets validation automatically)
        """
        self.enable_condition = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_diagnostic_event(self, value: Optional["DiagnosticEvent"]) -> "DiagnosticEventToEnableConditionGroupMapping":
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

    def with_enable_condition(self, value: Optional["DiagnosticEnable"]) -> "DiagnosticEventToEnableConditionGroupMapping":
        """
        Set enableCondition and return self for chaining.

        Args:
            value: The enableCondition to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_enable_condition("value")
        """
        self.enable_condition = value  # Use property setter (gets validation)
        return self
