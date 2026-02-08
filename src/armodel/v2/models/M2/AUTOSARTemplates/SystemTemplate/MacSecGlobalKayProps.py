from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)


class MacSecGlobalKayProps(ARElement):
    """
    Configuration of the MAC Security Key Agreement Entity properties that are
    shared by different KaY configurations.

    Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 174, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # by MACsec.
        # The providedEtherType will not be.
        self._bypassEther: "PositiveInteger" = None

    @property
    def bypass_ether(self) -> "PositiveInteger":
        """Get bypassEther (Pythonic accessor)."""
        return self._bypassEther

    @bypass_ether.setter
    def bypass_ether(self, value: "PositiveInteger") -> None:
        """
        Set bypassEther with validation.

        Args:
            value: The bypassEther to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"bypassEther must be PositiveInteger, got {type(value).__name__}"
            )
        self._bypassEther = value
        # MACsec.
        # The provided VLAN-IDs will not be (VLAN-ID 0 is interpreted as Bypass
                # untagged traffic).
        self._bypassVlan: "PositiveInteger" = None

    @property
    def bypass_vlan(self) -> "PositiveInteger":
        """Get bypassVlan (Pythonic accessor)."""
        return self._bypassVlan

    @bypass_vlan.setter
    def bypass_vlan(self, value: "PositiveInteger") -> None:
        """
        Set bypassVlan with validation.

        Args:
            value: The bypassVlan to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"bypassVlan must be PositiveInteger, got {type(value).__name__}"
            )
        self._bypassVlan = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBypassEther(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for bypassEther.

        Returns:
            The bypassEther value

        Note:
            Delegates to bypass_ether property (CODING_RULE_V2_00017)
        """
        return self.bypass_ether  # Delegates to property

    def setBypassEther(self, value: "PositiveInteger") -> "MacSecGlobalKayProps":
        """
        AUTOSAR-compliant setter for bypassEther with method chaining.

        Args:
            value: The bypassEther to set

        Returns:
            self for method chaining

        Note:
            Delegates to bypass_ether property setter (gets validation automatically)
        """
        self.bypass_ether = value  # Delegates to property setter
        return self

    def getBypassVlan(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for bypassVlan.

        Returns:
            The bypassVlan value

        Note:
            Delegates to bypass_vlan property (CODING_RULE_V2_00017)
        """
        return self.bypass_vlan  # Delegates to property

    def setBypassVlan(self, value: "PositiveInteger") -> "MacSecGlobalKayProps":
        """
        AUTOSAR-compliant setter for bypassVlan with method chaining.

        Args:
            value: The bypassVlan to set

        Returns:
            self for method chaining

        Note:
            Delegates to bypass_vlan property setter (gets validation automatically)
        """
        self.bypass_vlan = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bypass_ether(self, value: "PositiveInteger") -> "MacSecGlobalKayProps":
        """
        Set bypassEther and return self for chaining.

        Args:
            value: The bypassEther to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bypass_ether("value")
        """
        self.bypass_ether = value  # Use property setter (gets validation)
        return self

    def with_bypass_vlan(self, value: "PositiveInteger") -> "MacSecGlobalKayProps":
        """
        Set bypassVlan and return self for chaining.

        Args:
            value: The bypassVlan to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bypass_vlan("value")
        """
        self.bypass_vlan = value  # Use property setter (gets validation)
        return self
