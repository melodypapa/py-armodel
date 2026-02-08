from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService import (
    DiagnosticServiceInstance,
)


class DiagnosticSessionControl(DiagnosticServiceInstance):
    """
    This represents an instance of the "Session Control" diagnostic service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::SessionControl

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

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService import (
    DiagnosticServiceClass,
)


class DiagnosticSessionControlClass(DiagnosticServiceClass):
    """
    This meta-class contains attributes shared by all instances of the "Session
    Control" diagnostic service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::SessionControl

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 93, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Time for the server to keep a diagnostic session other the default session
        # active while not receiving any message.
        self._s3Server: Optional["TimeValue"] = None

    @property
    def s3_server(self) -> Optional["TimeValue"]:
        """Get s3Server (Pythonic accessor)."""
        return self._s3Server

    @s3_server.setter
    def s3_server(self, value: Optional["TimeValue"]) -> None:
        """
        Set s3Server with validation.

        Args:
            value: The s3Server to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._s3Server = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"s3Server must be TimeValue or None, got {type(value).__name__}"
            )
        self._s3Server = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getS3Server(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for s3Server.

        Returns:
            The s3Server value

        Note:
            Delegates to s3_server property (CODING_RULE_V2_00017)
        """
        return self.s3_server  # Delegates to property

    def setS3Server(self, value: "TimeValue") -> "DiagnosticSessionControlClass":
        """
        AUTOSAR-compliant setter for s3Server with method chaining.

        Args:
            value: The s3Server to set

        Returns:
            self for method chaining

        Note:
            Delegates to s3_server property setter (gets validation automatically)
        """
        self.s3_server = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_s3_server(self, value: Optional["TimeValue"]) -> "DiagnosticSessionControlClass":
        """
        Set s3Server and return self for chaining.

        Args:
            value: The s3Server to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_s3_server("value")
        """
        self.s3_server = value  # Use property setter (gets validation)
        return self
