from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import (
    DiagnosticCommonElement,
)


class DiagnosticAccessPermission(DiagnosticCommonElement):
    """
    This represents the specification of whether a given service can be accessed
    according to the existence of meta-classes referenced by a particular
    DiagnosticAccessPermission. In other words, this meta-class acts as a
    mapping element between several (otherwise unrelated) pieces of information
    that are put into context for the purpose of checking for access rights.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 73, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The existence of this aggregation indicates that an authentication is
                # foreseen.
        # The details are clarified by the.
        self._authentication: Optional["DiagnosticAuthRole"] = None

    @property
    def authentication(self) -> Optional["DiagnosticAuthRole"]:
        """Get authentication (Pythonic accessor)."""
        return self._authentication

    @authentication.setter
    def authentication(self, value: Optional["DiagnosticAuthRole"]) -> None:
        """
        Set authentication with validation.

        Args:
            value: The authentication to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._authentication = None
            return

        if not isinstance(value, DiagnosticAuthRole):
            raise TypeError(
                f"authentication must be DiagnosticAuthRole or None, got {type(value).__name__}"
            )
        self._authentication = value
        # This represents the associated DiagnosticSessions atpSplitable.
        self._diagnostic: List["DiagnosticSession"] = []

    @property
    def diagnostic(self) -> List["DiagnosticSession"]:
        """Get diagnostic (Pythonic accessor)."""
        return self._diagnostic
        # This represents the environmental conditions associated with the access
        # permission.
        self._environmental: Optional["Diagnostic"] = None

    @property
    def environmental(self) -> Optional["Diagnostic"]:
        """Get environmental (Pythonic accessor)."""
        return self._environmental

    @environmental.setter
    def environmental(self, value: Optional["Diagnostic"]) -> None:
        """
        Set environmental with validation.

        Args:
            value: The environmental to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._environmental = None
            return

        if not isinstance(value, Diagnostic):
            raise TypeError(
                f"environmental must be Diagnostic or None, got {type(value).__name__}"
            )
        self._environmental = value
        # This represents the associated DiagnosticSecurityLevels.
        self._securityLevel: List["DiagnosticSecurityLevel"] = []

    @property
    def security_level(self) -> List["DiagnosticSecurityLevel"]:
        """Get securityLevel (Pythonic accessor)."""
        return self._securityLevel

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAuthentication(self) -> "DiagnosticAuthRole":
        """
        AUTOSAR-compliant getter for authentication.

        Returns:
            The authentication value

        Note:
            Delegates to authentication property (CODING_RULE_V2_00017)
        """
        return self.authentication  # Delegates to property

    def setAuthentication(self, value: "DiagnosticAuthRole") -> "DiagnosticAccessPermission":
        """
        AUTOSAR-compliant setter for authentication with method chaining.

        Args:
            value: The authentication to set

        Returns:
            self for method chaining

        Note:
            Delegates to authentication property setter (gets validation automatically)
        """
        self.authentication = value  # Delegates to property setter
        return self

    def getDiagnostic(self) -> List["DiagnosticSession"]:
        """
        AUTOSAR-compliant getter for diagnostic.

        Returns:
            The diagnostic value

        Note:
            Delegates to diagnostic property (CODING_RULE_V2_00017)
        """
        return self.diagnostic  # Delegates to property

    def getEnvironmental(self) -> "Diagnostic":
        """
        AUTOSAR-compliant getter for environmental.

        Returns:
            The environmental value

        Note:
            Delegates to environmental property (CODING_RULE_V2_00017)
        """
        return self.environmental  # Delegates to property

    def setEnvironmental(self, value: "Diagnostic") -> "DiagnosticAccessPermission":
        """
        AUTOSAR-compliant setter for environmental with method chaining.

        Args:
            value: The environmental to set

        Returns:
            self for method chaining

        Note:
            Delegates to environmental property setter (gets validation automatically)
        """
        self.environmental = value  # Delegates to property setter
        return self

    def getSecurityLevel(self) -> List["DiagnosticSecurityLevel"]:
        """
        AUTOSAR-compliant getter for securityLevel.

        Returns:
            The securityLevel value

        Note:
            Delegates to security_level property (CODING_RULE_V2_00017)
        """
        return self.security_level  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_authentication(self, value: Optional["DiagnosticAuthRole"]) -> "DiagnosticAccessPermission":
        """
        Set authentication and return self for chaining.

        Args:
            value: The authentication to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_authentication("value")
        """
        self.authentication = value  # Use property setter (gets validation)
        return self

    def with_environmental(self, value: Optional["Diagnostic"]) -> "DiagnosticAccessPermission":
        """
        Set environmental and return self for chaining.

        Args:
            value: The environmental to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_environmental("value")
        """
        self.environmental = value  # Use property setter (gets validation)
        return self
