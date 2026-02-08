from typing import Optional


class DiagnosticSessionControl(DiagnosticServiceInstance):
    """
    This represents an instance of the "Session Control" diagnostic service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::SessionControl::DiagnosticSessionControl

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 93, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the applicable DiagnosticSessions.
        self._diagnosticSession: Optional["DiagnosticSession"] = None

    @property
    def diagnostic_session(self) -> Optional["DiagnosticSession"]:
        """Get diagnosticSession (Pythonic accessor)."""
        return self._diagnosticSession

    @diagnostic_session.setter
    def diagnostic_session(self, value: Optional["DiagnosticSession"]) -> None:
        """
        Set diagnosticSession with validation.

        Args:
            value: The diagnosticSession to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._diagnosticSession = None
            return

        if not isinstance(value, DiagnosticSession):
            raise TypeError(
                f"diagnosticSession must be DiagnosticSession or None, got {type(value).__name__}"
            )
        self._diagnosticSession = value
        # This reference substantiates that abstract reference in the reference
        # represents the ability to access among all DiagnosticSessionControl in
        # context.
        self._sessionControl: Optional["DiagnosticSession"] = None

    @property
    def session_control(self) -> Optional["DiagnosticSession"]:
        """Get sessionControl (Pythonic accessor)."""
        return self._sessionControl

    @session_control.setter
    def session_control(self, value: Optional["DiagnosticSession"]) -> None:
        """
        Set sessionControl with validation.

        Args:
            value: The sessionControl to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sessionControl = None
            return

        if not isinstance(value, DiagnosticSession):
            raise TypeError(
                f"sessionControl must be DiagnosticSession or None, got {type(value).__name__}"
            )
        self._sessionControl = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDiagnosticSession(self) -> "DiagnosticSession":
        """
        AUTOSAR-compliant getter for diagnosticSession.

        Returns:
            The diagnosticSession value

        Note:
            Delegates to diagnostic_session property (CODING_RULE_V2_00017)
        """
        return self.diagnostic_session  # Delegates to property

    def setDiagnosticSession(self, value: "DiagnosticSession") -> "DiagnosticSessionControl":
        """
        AUTOSAR-compliant setter for diagnosticSession with method chaining.

        Args:
            value: The diagnosticSession to set

        Returns:
            self for method chaining

        Note:
            Delegates to diagnostic_session property setter (gets validation automatically)
        """
        self.diagnostic_session = value  # Delegates to property setter
        return self

    def getSessionControl(self) -> "DiagnosticSession":
        """
        AUTOSAR-compliant getter for sessionControl.

        Returns:
            The sessionControl value

        Note:
            Delegates to session_control property (CODING_RULE_V2_00017)
        """
        return self.session_control  # Delegates to property

    def setSessionControl(self, value: "DiagnosticSession") -> "DiagnosticSessionControl":
        """
        AUTOSAR-compliant setter for sessionControl with method chaining.

        Args:
            value: The sessionControl to set

        Returns:
            self for method chaining

        Note:
            Delegates to session_control property setter (gets validation automatically)
        """
        self.session_control = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_diagnostic_session(self, value: Optional["DiagnosticSession"]) -> "DiagnosticSessionControl":
        """
        Set diagnosticSession and return self for chaining.

        Args:
            value: The diagnosticSession to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_diagnostic_session("value")
        """
        self.diagnostic_session = value  # Use property setter (gets validation)
        return self

    def with_session_control(self, value: Optional["DiagnosticSession"]) -> "DiagnosticSessionControl":
        """
        Set sessionControl and return self for chaining.

        Args:
            value: The sessionControl to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_session_control("value")
        """
        self.session_control = value  # Use property setter (gets validation)
        return self
