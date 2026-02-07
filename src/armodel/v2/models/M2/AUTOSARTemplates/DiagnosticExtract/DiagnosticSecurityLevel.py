from typing import Optional


class DiagnosticSecurityLevel(DiagnosticCommonElement):
    """
    This meta-class represents the ability to define a security level considered
    for diagnostic purposes.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticSecurityLevel

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 75, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the size of the AccessDataRecord used GetSeed.
        # Unit:byte.
        self._accessData: Optional["PositiveInteger"] = None

    @property
    def access_data(self) -> Optional["PositiveInteger"]:
        """Get accessData (Pythonic accessor)."""
        return self._accessData

    @access_data.setter
    def access_data(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set accessData with validation.

        Args:
            value: The accessData to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._accessData = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"accessData must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._accessData = value
        # This represents the size of the security key.
        # Unit: byte.
        self._keySize: Optional["PositiveInteger"] = None

    @property
    def key_size(self) -> Optional["PositiveInteger"]:
        """Get keySize (Pythonic accessor)."""
        return self._keySize

    @key_size.setter
    def key_size(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set keySize with validation.

        Args:
            value: The keySize to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._keySize = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"keySize must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._keySize = value
        # This represents the number of failed security accesses which the delay time
        # is activated.
        self._numFailed: Optional["PositiveInteger"] = None

    @property
    def num_failed(self) -> Optional["PositiveInteger"]:
        """Get numFailed (Pythonic accessor)."""
        return self._numFailed

    @num_failed.setter
    def num_failed(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set numFailed with validation.

        Args:
            value: The numFailed to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._numFailed = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"numFailed must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._numFailed = value
        # This represents the delay time after a failed security Unit: second.
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
        # This represents the size of the security seed.
        # Unit: byte.
        self._seedSize: Optional["PositiveInteger"] = None

    @property
    def seed_size(self) -> Optional["PositiveInteger"]:
        """Get seedSize (Pythonic accessor)."""
        return self._seedSize

    @seed_size.setter
    def seed_size(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set seedSize with validation.

        Args:
            value: The seedSize to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._seedSize = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"seedSize must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._seedSize = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAccessData(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for accessData.

        Returns:
            The accessData value

        Note:
            Delegates to access_data property (CODING_RULE_V2_00017)
        """
        return self.access_data  # Delegates to property

    def setAccessData(self, value: "PositiveInteger") -> "DiagnosticSecurityLevel":
        """
        AUTOSAR-compliant setter for accessData with method chaining.

        Args:
            value: The accessData to set

        Returns:
            self for method chaining

        Note:
            Delegates to access_data property setter (gets validation automatically)
        """
        self.access_data = value  # Delegates to property setter
        return self

    def getKeySize(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for keySize.

        Returns:
            The keySize value

        Note:
            Delegates to key_size property (CODING_RULE_V2_00017)
        """
        return self.key_size  # Delegates to property

    def setKeySize(self, value: "PositiveInteger") -> "DiagnosticSecurityLevel":
        """
        AUTOSAR-compliant setter for keySize with method chaining.

        Args:
            value: The keySize to set

        Returns:
            self for method chaining

        Note:
            Delegates to key_size property setter (gets validation automatically)
        """
        self.key_size = value  # Delegates to property setter
        return self

    def getNumFailed(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for numFailed.

        Returns:
            The numFailed value

        Note:
            Delegates to num_failed property (CODING_RULE_V2_00017)
        """
        return self.num_failed  # Delegates to property

    def setNumFailed(self, value: "PositiveInteger") -> "DiagnosticSecurityLevel":
        """
        AUTOSAR-compliant setter for numFailed with method chaining.

        Args:
            value: The numFailed to set

        Returns:
            self for method chaining

        Note:
            Delegates to num_failed property setter (gets validation automatically)
        """
        self.num_failed = value  # Delegates to property setter
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

    def setSecurityDelay(self, value: "TimeValue") -> "DiagnosticSecurityLevel":
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

    def getSeedSize(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for seedSize.

        Returns:
            The seedSize value

        Note:
            Delegates to seed_size property (CODING_RULE_V2_00017)
        """
        return self.seed_size  # Delegates to property

    def setSeedSize(self, value: "PositiveInteger") -> "DiagnosticSecurityLevel":
        """
        AUTOSAR-compliant setter for seedSize with method chaining.

        Args:
            value: The seedSize to set

        Returns:
            self for method chaining

        Note:
            Delegates to seed_size property setter (gets validation automatically)
        """
        self.seed_size = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_access_data(self, value: Optional["PositiveInteger"]) -> "DiagnosticSecurityLevel":
        """
        Set accessData and return self for chaining.

        Args:
            value: The accessData to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_access_data("value")
        """
        self.access_data = value  # Use property setter (gets validation)
        return self

    def with_key_size(self, value: Optional["PositiveInteger"]) -> "DiagnosticSecurityLevel":
        """
        Set keySize and return self for chaining.

        Args:
            value: The keySize to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_key_size("value")
        """
        self.key_size = value  # Use property setter (gets validation)
        return self

    def with_num_failed(self, value: Optional["PositiveInteger"]) -> "DiagnosticSecurityLevel":
        """
        Set numFailed and return self for chaining.

        Args:
            value: The numFailed to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_num_failed("value")
        """
        self.num_failed = value  # Use property setter (gets validation)
        return self

    def with_security_delay(self, value: Optional["TimeValue"]) -> "DiagnosticSecurityLevel":
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

    def with_seed_size(self, value: Optional["PositiveInteger"]) -> "DiagnosticSecurityLevel":
        """
        Set seedSize and return self for chaining.

        Args:
            value: The seedSize to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_seed_size("value")
        """
        self.seed_size = value  # Use property setter (gets validation)
        return self
