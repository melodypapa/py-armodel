from typing import Optional


class DiagnosticTestResult(DiagnosticCommonElement):
    """
    This meta-class represents the ability to define diagnostic test results.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticTestResult::DiagnosticTestResult

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 204, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 804, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute represents the diagnostic event that is the diagnostic test
                # result.
        # atpVariation.
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
        # This attribute represents the related diagnostic monitored identifier.
        self._monitored: Optional["Diagnostic"] = None

    @property
    def monitored(self) -> Optional["Diagnostic"]:
        """Get monitored (Pythonic accessor)."""
        return self._monitored

    @monitored.setter
    def monitored(self, value: Optional["Diagnostic"]) -> None:
        """
        Set monitored with validation.

        Args:
            value: The monitored to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._monitored = None
            return

        if not isinstance(value, Diagnostic):
            raise TypeError(
                f"monitored must be Diagnostic or None, got {type(value).__name__}"
            )
        self._monitored = value
        # This attribute represents the applicable test identifier.
        self._testIdentifier: Optional["DiagnosticTestIdentifier"] = None

    @property
    def test_identifier(self) -> Optional["DiagnosticTestIdentifier"]:
        """Get testIdentifier (Pythonic accessor)."""
        return self._testIdentifier

    @test_identifier.setter
    def test_identifier(self, value: Optional["DiagnosticTestIdentifier"]) -> None:
        """
        Set testIdentifier with validation.

        Args:
            value: The testIdentifier to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._testIdentifier = None
            return

        if not isinstance(value, DiagnosticTestIdentifier):
            raise TypeError(
                f"testIdentifier must be DiagnosticTestIdentifier or None, got {type(value).__name__}"
            )
        self._testIdentifier = value
        # This attribute controls the update behavior of the DiagnosticTestResult.
        self._updateKind: Optional["DiagnosticTestResult"] = None

    @property
    def update_kind(self) -> Optional["DiagnosticTestResult"]:
        """Get updateKind (Pythonic accessor)."""
        return self._updateKind

    @update_kind.setter
    def update_kind(self, value: Optional["DiagnosticTestResult"]) -> None:
        """
        Set updateKind with validation.

        Args:
            value: The updateKind to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._updateKind = None
            return

        if not isinstance(value, DiagnosticTestResult):
            raise TypeError(
                f"updateKind must be DiagnosticTestResult or None, got {type(value).__name__}"
            )
        self._updateKind = value

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

    def setDiagnosticEvent(self, value: "DiagnosticEvent") -> "DiagnosticTestResult":
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

    def getMonitored(self) -> "Diagnostic":
        """
        AUTOSAR-compliant getter for monitored.

        Returns:
            The monitored value

        Note:
            Delegates to monitored property (CODING_RULE_V2_00017)
        """
        return self.monitored  # Delegates to property

    def setMonitored(self, value: "Diagnostic") -> "DiagnosticTestResult":
        """
        AUTOSAR-compliant setter for monitored with method chaining.

        Args:
            value: The monitored to set

        Returns:
            self for method chaining

        Note:
            Delegates to monitored property setter (gets validation automatically)
        """
        self.monitored = value  # Delegates to property setter
        return self

    def getTestIdentifier(self) -> "DiagnosticTestIdentifier":
        """
        AUTOSAR-compliant getter for testIdentifier.

        Returns:
            The testIdentifier value

        Note:
            Delegates to test_identifier property (CODING_RULE_V2_00017)
        """
        return self.test_identifier  # Delegates to property

    def setTestIdentifier(self, value: "DiagnosticTestIdentifier") -> "DiagnosticTestResult":
        """
        AUTOSAR-compliant setter for testIdentifier with method chaining.

        Args:
            value: The testIdentifier to set

        Returns:
            self for method chaining

        Note:
            Delegates to test_identifier property setter (gets validation automatically)
        """
        self.test_identifier = value  # Delegates to property setter
        return self

    def getUpdateKind(self) -> "DiagnosticTestResult":
        """
        AUTOSAR-compliant getter for updateKind.

        Returns:
            The updateKind value

        Note:
            Delegates to update_kind property (CODING_RULE_V2_00017)
        """
        return self.update_kind  # Delegates to property

    def setUpdateKind(self, value: "DiagnosticTestResult") -> "DiagnosticTestResult":
        """
        AUTOSAR-compliant setter for updateKind with method chaining.

        Args:
            value: The updateKind to set

        Returns:
            self for method chaining

        Note:
            Delegates to update_kind property setter (gets validation automatically)
        """
        self.update_kind = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_diagnostic_event(self, value: Optional["DiagnosticEvent"]) -> "DiagnosticTestResult":
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

    def with_monitored(self, value: Optional["Diagnostic"]) -> "DiagnosticTestResult":
        """
        Set monitored and return self for chaining.

        Args:
            value: The monitored to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_monitored("value")
        """
        self.monitored = value  # Use property setter (gets validation)
        return self

    def with_test_identifier(self, value: Optional["DiagnosticTestIdentifier"]) -> "DiagnosticTestResult":
        """
        Set testIdentifier and return self for chaining.

        Args:
            value: The testIdentifier to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_test_identifier("value")
        """
        self.test_identifier = value  # Use property setter (gets validation)
        return self

    def with_update_kind(self, value: Optional["DiagnosticTestResult"]) -> "DiagnosticTestResult":
        """
        Set updateKind and return self for chaining.

        Args:
            value: The updateKind to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_update_kind("value")
        """
        self.update_kind = value  # Use property setter (gets validation)
        return self
