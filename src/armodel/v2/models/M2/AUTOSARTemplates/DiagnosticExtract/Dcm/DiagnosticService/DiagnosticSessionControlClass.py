from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    DiagnosticServiceClass,
    TimeValue,
)


class DiagnosticSessionControlClass(DiagnosticServiceClass):
    """
    This meta-class contains attributes shared by all instances of the "Session
    Control" diagnostic service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::SessionControl::DiagnosticSessionControlClass

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
