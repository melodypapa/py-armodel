from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class VlanMembership(ARObject):
    """
    Static logical channel or VLAN binding to a switch-port. The reference to an
    EthernetPhysicalChannel without a VLAN defined represents the handling of
    untagged frames. (cid:53) 111 of 2090 Document ID 63:
    AUTOSAR_CP_TPS_SystemTemplate System Template AUTOSAR CP R23-11 (cid:52)

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 111, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Standard output-priority outgoing Frames will be tagged priority that
                # received frames are assigned the VLAN Id (defaultVlan).
        # The values from effort) to 7 (highest) are allowed.
        # modifyVlan and an already tagged received actual priority of the received
                # frame is not.
        self._defaultPriority: Optional["PositiveInteger"] = None

    @property
    def default_priority(self) -> Optional["PositiveInteger"]:
        """Get defaultPriority (Pythonic accessor)."""
        return self._defaultPriority

    @default_priority.setter
    def default_priority(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set defaultPriority with validation.

        Args:
            value: The defaultPriority to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._defaultPriority = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"defaultPriority must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._defaultPriority = value
        # Specifies the IP Address which will be assigned to a DHCP Client at this
                # SwitchPort.
        # If no dhcpAddress provided all DHCP-Discover messages this Port will be
                # discarded by the DHCP.
        self._dhcpAddress: Optional["DhcpServer"] = None

    @property
    def dhcp_address(self) -> Optional["DhcpServer"]:
        """Get dhcpAddress (Pythonic accessor)."""
        return self._dhcpAddress

    @dhcp_address.setter
    def dhcp_address(self, value: Optional["DhcpServer"]) -> None:
        """
        Set dhcpAddress with validation.

        Args:
            value: The dhcpAddress to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dhcpAddress = None
            return

        if not isinstance(value, DhcpServer):
            raise TypeError(
                f"dhcpAddress must be DhcpServer or None, got {type(value).__name__}"
            )
        self._dhcpAddress = value
        # Attribute denotes whether a VLAN tagged ethernet frame be with its VLAN tag
        # (sentTagged) without a VLAN tag (sentUntagged) be dropped at this port
        # (notSent or VLAN not this list).
        self._sendActivity: Optional["EthernetSwitchVlan"] = None

    @property
    def send_activity(self) -> Optional["EthernetSwitchVlan"]:
        """Get sendActivity (Pythonic accessor)."""
        return self._sendActivity

    @send_activity.setter
    def send_activity(self, value: Optional["EthernetSwitchVlan"]) -> None:
        """
        Set sendActivity with validation.

        Args:
            value: The sendActivity to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sendActivity = None
            return

        if not isinstance(value, EthernetSwitchVlan):
            raise TypeError(
                f"sendActivity must be EthernetSwitchVlan or None, got {type(value).__name__}"
            )
        self._sendActivity = value
        # References a channel that represents a VLAN or an channel.
        self._vlan: Optional["EthernetPhysical"] = None

    @property
    def vlan(self) -> Optional["EthernetPhysical"]:
        """Get vlan (Pythonic accessor)."""
        return self._vlan

    @vlan.setter
    def vlan(self, value: Optional["EthernetPhysical"]) -> None:
        """
        Set vlan with validation.

        Args:
            value: The vlan to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._vlan = None
            return

        if not isinstance(value, EthernetPhysical):
            raise TypeError(
                f"vlan must be EthernetPhysical or None, got {type(value).__name__}"
            )
        self._vlan = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDefaultPriority(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for defaultPriority.

        Returns:
            The defaultPriority value

        Note:
            Delegates to default_priority property (CODING_RULE_V2_00017)
        """
        return self.default_priority  # Delegates to property

    def setDefaultPriority(self, value: "PositiveInteger") -> "VlanMembership":
        """
        AUTOSAR-compliant setter for defaultPriority with method chaining.

        Args:
            value: The defaultPriority to set

        Returns:
            self for method chaining

        Note:
            Delegates to default_priority property setter (gets validation automatically)
        """
        self.default_priority = value  # Delegates to property setter
        return self

    def getDhcpAddress(self) -> "DhcpServer":
        """
        AUTOSAR-compliant getter for dhcpAddress.

        Returns:
            The dhcpAddress value

        Note:
            Delegates to dhcp_address property (CODING_RULE_V2_00017)
        """
        return self.dhcp_address  # Delegates to property

    def setDhcpAddress(self, value: "DhcpServer") -> "VlanMembership":
        """
        AUTOSAR-compliant setter for dhcpAddress with method chaining.

        Args:
            value: The dhcpAddress to set

        Returns:
            self for method chaining

        Note:
            Delegates to dhcp_address property setter (gets validation automatically)
        """
        self.dhcp_address = value  # Delegates to property setter
        return self

    def getSendActivity(self) -> "EthernetSwitchVlan":
        """
        AUTOSAR-compliant getter for sendActivity.

        Returns:
            The sendActivity value

        Note:
            Delegates to send_activity property (CODING_RULE_V2_00017)
        """
        return self.send_activity  # Delegates to property

    def setSendActivity(self, value: "EthernetSwitchVlan") -> "VlanMembership":
        """
        AUTOSAR-compliant setter for sendActivity with method chaining.

        Args:
            value: The sendActivity to set

        Returns:
            self for method chaining

        Note:
            Delegates to send_activity property setter (gets validation automatically)
        """
        self.send_activity = value  # Delegates to property setter
        return self

    def getVlan(self) -> "EthernetPhysical":
        """
        AUTOSAR-compliant getter for vlan.

        Returns:
            The vlan value

        Note:
            Delegates to vlan property (CODING_RULE_V2_00017)
        """
        return self.vlan  # Delegates to property

    def setVlan(self, value: "EthernetPhysical") -> "VlanMembership":
        """
        AUTOSAR-compliant setter for vlan with method chaining.

        Args:
            value: The vlan to set

        Returns:
            self for method chaining

        Note:
            Delegates to vlan property setter (gets validation automatically)
        """
        self.vlan = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_default_priority(self, value: Optional["PositiveInteger"]) -> "VlanMembership":
        """
        Set defaultPriority and return self for chaining.

        Args:
            value: The defaultPriority to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_default_priority("value")
        """
        self.default_priority = value  # Use property setter (gets validation)
        return self

    def with_dhcp_address(self, value: Optional["DhcpServer"]) -> "VlanMembership":
        """
        Set dhcpAddress and return self for chaining.

        Args:
            value: The dhcpAddress to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dhcp_address("value")
        """
        self.dhcp_address = value  # Use property setter (gets validation)
        return self

    def with_send_activity(self, value: Optional["EthernetSwitchVlan"]) -> "VlanMembership":
        """
        Set sendActivity and return self for chaining.

        Args:
            value: The sendActivity to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_send_activity("value")
        """
        self.send_activity = value  # Use property setter (gets validation)
        return self

    def with_vlan(self, value: Optional["EthernetPhysical"]) -> "VlanMembership":
        """
        Set vlan and return self for chaining.

        Args:
            value: The vlan to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_vlan("value")
        """
        self.vlan = value  # Use property setter (gets validation)
        return self
