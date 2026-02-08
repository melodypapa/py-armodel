from typing import Optional


class J1939NmCluster(NmCluster):
    """
    J1939 specific NmCluster attributes

    Package: M2::AUTOSARTemplates::SystemTemplate::NetworkManagement::J1939NmCluster

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 691, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute specifies whether the J1939Nm Bsw is used or not.
        # If this attribute is set to false then configuration shall not be derived
                # from the But even in this case the nmNodeId be necessary for the J1939Rm and
                # J1939Tp.
        self._addressClaim: Optional["Boolean"] = None

    @property
    def address_claim(self) -> Optional["Boolean"]:
        """Get addressClaim (Pythonic accessor)."""
        return self._addressClaim

    @address_claim.setter
    def address_claim(self, value: Optional["Boolean"]) -> None:
        """
        Set addressClaim with validation.

        Args:
            value: The addressClaim to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._addressClaim = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"addressClaim must be Boolean or None, got {type(value).__name__}"
            )
        self._addressClaim = value
        # Defines whether fully dynamic address resolution to SAE J1939-81 shall be
                # supported on this The dynamically allocated addresses on the bus at runtime
                # to the configured addresses.
        # The addresses on the bus resemble the.
        self._usesDynamic: Optional["Boolean"] = None

    @property
    def uses_dynamic(self) -> Optional["Boolean"]:
        """Get usesDynamic (Pythonic accessor)."""
        return self._usesDynamic

    @uses_dynamic.setter
    def uses_dynamic(self, value: Optional["Boolean"]) -> None:
        """
        Set usesDynamic with validation.

        Args:
            value: The usesDynamic to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._usesDynamic = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"usesDynamic must be Boolean or None, got {type(value).__name__}"
            )
        self._usesDynamic = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAddressClaim(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for addressClaim.

        Returns:
            The addressClaim value

        Note:
            Delegates to address_claim property (CODING_RULE_V2_00017)
        """
        return self.address_claim  # Delegates to property

    def setAddressClaim(self, value: "Boolean") -> "J1939NmCluster":
        """
        AUTOSAR-compliant setter for addressClaim with method chaining.

        Args:
            value: The addressClaim to set

        Returns:
            self for method chaining

        Note:
            Delegates to address_claim property setter (gets validation automatically)
        """
        self.address_claim = value  # Delegates to property setter
        return self

    def getUsesDynamic(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for usesDynamic.

        Returns:
            The usesDynamic value

        Note:
            Delegates to uses_dynamic property (CODING_RULE_V2_00017)
        """
        return self.uses_dynamic  # Delegates to property

    def setUsesDynamic(self, value: "Boolean") -> "J1939NmCluster":
        """
        AUTOSAR-compliant setter for usesDynamic with method chaining.

        Args:
            value: The usesDynamic to set

        Returns:
            self for method chaining

        Note:
            Delegates to uses_dynamic property setter (gets validation automatically)
        """
        self.uses_dynamic = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_address_claim(self, value: Optional["Boolean"]) -> "J1939NmCluster":
        """
        Set addressClaim and return self for chaining.

        Args:
            value: The addressClaim to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_address_claim("value")
        """
        self.address_claim = value  # Use property setter (gets validation)
        return self

    def with_uses_dynamic(self, value: Optional["Boolean"]) -> "J1939NmCluster":
        """
        Set usesDynamic and return self for chaining.

        Args:
            value: The usesDynamic to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_uses_dynamic("value")
        """
        self.uses_dynamic = value  # Use property setter (gets validation)
        return self
