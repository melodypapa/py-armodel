from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService import DiagnosticServiceInstance


class DiagnosticSecurityAccess(DiagnosticServiceInstance):
    """
    This represents an instance of the "Security Access" diagnostic service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::SecurityAccess::DiagnosticSecurityAccess

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 96, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This would be 0x01, 0x03, 0x05,.
        # id can be computed by adding 1 to the.
        self._requestSeedId: Optional["PositiveInteger"] = None

    @property
    def request_seed_id(self) -> Optional["PositiveInteger"]:
        """Get requestSeedId (Pythonic accessor)."""
        return self._requestSeedId

    @request_seed_id.setter
    def request_seed_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set requestSeedId with validation.

        Args:
            value: The requestSeedId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._requestSeedId = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"requestSeedId must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._requestSeedId = value
        # This reference substantiates that abstract reference in the reference
        # represents the ability to access among all DiagnosticSecurityAccess in
        # context.
        self._securityAccess: Optional["DiagnosticSecurity"] = None

    @property
    def security_access(self) -> Optional["DiagnosticSecurity"]:
        """Get securityAccess (Pythonic accessor)."""
        return self._securityAccess

    @security_access.setter
    def security_access(self, value: Optional["DiagnosticSecurity"]) -> None:
        """
        Set securityAccess with validation.

        Args:
            value: The securityAccess to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._securityAccess = None
            return

        if not isinstance(value, DiagnosticSecurity):
            raise TypeError(
                f"securityAccess must be DiagnosticSecurity or None, got {type(value).__name__}"
            )
        self._securityAccess = value
        # Start delay timer on power on in seconds.
        # This delay the time after ECU boot power-on where no request is accepted.
        self._securityDelay: Optional["TimeValue"] = None

    @property
    def security_delay(self) -> Optional["TimeValue"]:
        """Get securityDelay (Pythonic accessor)."""
        return self._securityDelay

    @security_delay.setter
    def security_delay(self, value: Optional["TimeValue"]) -> None:
        """
        Set securityDelay with validation.

        Args:
            value: The securityDelay to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._securityDelay = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"securityDelay must be TimeValue or None, got {type(value).__name__}"
            )
        self._securityDelay = value
        # This reference identifies the applicable security level for access.
        self._securityLevel: Optional["DiagnosticSecurityLevel"] = None

    @property
    def security_level(self) -> Optional["DiagnosticSecurityLevel"]:
        """Get securityLevel (Pythonic accessor)."""
        return self._securityLevel

    @security_level.setter
    def security_level(self, value: Optional["DiagnosticSecurityLevel"]) -> None:
        """
        Set securityLevel with validation.

        Args:
            value: The securityLevel to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._securityLevel = None
            return

        if not isinstance(value, DiagnosticSecurityLevel):
            raise TypeError(
                f"securityLevel must be DiagnosticSecurityLevel or None, got {type(value).__name__}"
            )
        self._securityLevel = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRequestSeedId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for requestSeedId.

        Returns:
            The requestSeedId value

        Note:
            Delegates to request_seed_id property (CODING_RULE_V2_00017)
        """
        return self.request_seed_id  # Delegates to property

    def setRequestSeedId(self, value: "PositiveInteger") -> "DiagnosticSecurityAccess":
        """
        AUTOSAR-compliant setter for requestSeedId with method chaining.

        Args:
            value: The requestSeedId to set

        Returns:
            self for method chaining

        Note:
            Delegates to request_seed_id property setter (gets validation automatically)
        """
        self.request_seed_id = value  # Delegates to property setter
        return self

    def getSecurityAccess(self) -> "DiagnosticSecurity":
        """
        AUTOSAR-compliant getter for securityAccess.

        Returns:
            The securityAccess value

        Note:
            Delegates to security_access property (CODING_RULE_V2_00017)
        """
        return self.security_access  # Delegates to property

    def setSecurityAccess(self, value: "DiagnosticSecurity") -> "DiagnosticSecurityAccess":
        """
        AUTOSAR-compliant setter for securityAccess with method chaining.

        Args:
            value: The securityAccess to set

        Returns:
            self for method chaining

        Note:
            Delegates to security_access property setter (gets validation automatically)
        """
        self.security_access = value  # Delegates to property setter
        return self

    def getSecurityDelay(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for securityDelay.

        Returns:
            The securityDelay value

        Note:
            Delegates to security_delay property (CODING_RULE_V2_00017)
        """
        return self.security_delay  # Delegates to property

    def setSecurityDelay(self, value: "TimeValue") -> "DiagnosticSecurityAccess":
        """
        AUTOSAR-compliant setter for securityDelay with method chaining.

        Args:
            value: The securityDelay to set

        Returns:
            self for method chaining

        Note:
            Delegates to security_delay property setter (gets validation automatically)
        """
        self.security_delay = value  # Delegates to property setter
        return self

    def getSecurityLevel(self) -> "DiagnosticSecurityLevel":
        """
        AUTOSAR-compliant getter for securityLevel.

        Returns:
            The securityLevel value

        Note:
            Delegates to security_level property (CODING_RULE_V2_00017)
        """
        return self.security_level  # Delegates to property

    def setSecurityLevel(self, value: "DiagnosticSecurityLevel") -> "DiagnosticSecurityAccess":
        """
        AUTOSAR-compliant setter for securityLevel with method chaining.

        Args:
            value: The securityLevel to set

        Returns:
            self for method chaining

        Note:
            Delegates to security_level property setter (gets validation automatically)
        """
        self.security_level = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_request_seed_id(self, value: Optional["PositiveInteger"]) -> "DiagnosticSecurityAccess":
        """
        Set requestSeedId and return self for chaining.

        Args:
            value: The requestSeedId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_request_seed_id("value")
        """
        self.request_seed_id = value  # Use property setter (gets validation)
        return self

    def with_security_access(self, value: Optional["DiagnosticSecurity"]) -> "DiagnosticSecurityAccess":
        """
        Set securityAccess and return self for chaining.

        Args:
            value: The securityAccess to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_security_access("value")
        """
        self.security_access = value  # Use property setter (gets validation)
        return self

    def with_security_delay(self, value: Optional["TimeValue"]) -> "DiagnosticSecurityAccess":
        """
        Set securityDelay and return self for chaining.

        Args:
            value: The securityDelay to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_security_delay("value")
        """
        self.security_delay = value  # Use property setter (gets validation)
        return self

    def with_security_level(self, value: Optional["DiagnosticSecurityLevel"]) -> "DiagnosticSecurityAccess":
        """
        Set securityLevel and return self for chaining.

        Args:
            value: The securityLevel to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_security_level("value")
        """
        self.security_level = value  # Use property setter (gets validation)
        return self
