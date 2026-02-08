from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    NetworkEndpointAddress,
)


class Ipv6Configuration(NetworkEndpointAddress):
    """
    Internet Protocol version 6 (IPv6) configuration.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 466, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Priority of assignment (1 is highest).
        # If a new address an assignment method with a higher priority is overwrites
                # the IP address previously assigned assignment method with a lower priority.
        self._assignment: Optional["PositiveInteger"] = None

    @property
    def assignment(self) -> Optional["PositiveInteger"]:
        """Get assignment (Pythonic accessor)."""
        return self._assignment

    @assignment.setter
    def assignment(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set assignment with validation.

        Args:
            value: The assignment to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._assignment = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"assignment must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._assignment = value
        # IP address of the default router.
        self._defaultRouter: Optional["Ip6AddressString"] = None

    @property
    def default_router(self) -> Optional["Ip6AddressString"]:
        """Get defaultRouter (Pythonic accessor)."""
        return self._defaultRouter

    @default_router.setter
    def default_router(self, value: Optional["Ip6AddressString"]) -> None:
        """
        Set defaultRouter with validation.

        Args:
            value: The defaultRouter to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._defaultRouter = None
            return

        if not isinstance(value, Ip6AddressString):
            raise TypeError(
                f"defaultRouter must be Ip6AddressString or None, got {type(value).__name__}"
            )
        self._defaultRouter = value
        # IP addresses of pre configured DNS servers.
        # xml.
        # namePlural=DNS-SERVER-ADDRESSES.
        self._dnsServer: List["Ip6AddressString"] = []

    @property
    def dns_server(self) -> List["Ip6AddressString"]:
        """Get dnsServer (Pythonic accessor)."""
        return self._dnsServer
        # This attribute is used to enable anycast addressing (i.
        # e.
        # to multiple receivers).
        self._enableAnycast: Optional["Boolean"] = None

    @property
    def enable_anycast(self) -> Optional["Boolean"]:
        """Get enableAnycast (Pythonic accessor)."""
        return self._enableAnycast

    @enable_anycast.setter
    def enable_anycast(self, value: Optional["Boolean"]) -> None:
        """
        Set enableAnycast with validation.

        Args:
            value: The enableAnycast to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._enableAnycast = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"enableAnycast must be Boolean or None, got {type(value).__name__}"
            )
        self._enableAnycast = value
        # The distance between two hosts.
        # The hop count n means gateways separate the source host from the (Range 0.
        # 255).
        self._hopCount: Optional["PositiveInteger"] = None

    @property
    def hop_count(self) -> Optional["PositiveInteger"]:
        """Get hopCount (Pythonic accessor)."""
        return self._hopCount

    @hop_count.setter
    def hop_count(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set hopCount with validation.

        Args:
            value: The hopCount to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._hopCount = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"hopCount must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._hopCount = value
        # Defines the lifetime of a dynamically fetched IP address.
        self._ipAddressKeep: Optional["IpAddressKeepEnum"] = None

    @property
    def ip_address_keep(self) -> Optional["IpAddressKeepEnum"]:
        """Get ipAddressKeep (Pythonic accessor)."""
        return self._ipAddressKeep

    @ip_address_keep.setter
    def ip_address_keep(self, value: Optional["IpAddressKeepEnum"]) -> None:
        """
        Set ipAddressKeep with validation.

        Args:
            value: The ipAddressKeep to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ipAddressKeep = None
            return

        if not isinstance(value, IpAddressKeepEnum):
            raise TypeError(
                f"ipAddressKeep must be IpAddressKeepEnum or None, got {type(value).__name__}"
            )
        self._ipAddressKeep = value
        # IPv6 prefix length defines the part of the IPv6 address is the network
        # prefix.
        self._ipAddressPrefix: Optional["PositiveInteger"] = None

    @property
    def ip_address_prefix(self) -> Optional["PositiveInteger"]:
        """Get ipAddressPrefix (Pythonic accessor)."""
        return self._ipAddressPrefix

    @ip_address_prefix.setter
    def ip_address_prefix(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set ipAddressPrefix with validation.

        Args:
            value: The ipAddressPrefix to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ipAddressPrefix = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"ipAddressPrefix must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._ipAddressPrefix = value
        # Defines how the node obtains its IP address.
        self._ipv6Address: Optional["Ipv6AddressSource"] = None

    @property
    def ipv6_address(self) -> Optional["Ipv6AddressSource"]:
        """Get ipv6Address (Pythonic accessor)."""
        return self._ipv6Address

    @ipv6_address.setter
    def ipv6_address(self, value: Optional["Ipv6AddressSource"]) -> None:
        """
        Set ipv6Address with validation.

        Args:
            value: The ipv6Address to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ipv6Address = None
            return

        if not isinstance(value, Ipv6AddressSource):
            raise TypeError(
                f"ipv6Address must be Ipv6AddressSource or None, got {type(value).__name__}"
            )
        self._ipv6Address = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAssignment(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for assignment.

        Returns:
            The assignment value

        Note:
            Delegates to assignment property (CODING_RULE_V2_00017)
        """
        return self.assignment  # Delegates to property

    def setAssignment(self, value: "PositiveInteger") -> "Ipv6Configuration":
        """
        AUTOSAR-compliant setter for assignment with method chaining.

        Args:
            value: The assignment to set

        Returns:
            self for method chaining

        Note:
            Delegates to assignment property setter (gets validation automatically)
        """
        self.assignment = value  # Delegates to property setter
        return self

    def getDefaultRouter(self) -> "Ip6AddressString":
        """
        AUTOSAR-compliant getter for defaultRouter.

        Returns:
            The defaultRouter value

        Note:
            Delegates to default_router property (CODING_RULE_V2_00017)
        """
        return self.default_router  # Delegates to property

    def setDefaultRouter(self, value: "Ip6AddressString") -> "Ipv6Configuration":
        """
        AUTOSAR-compliant setter for defaultRouter with method chaining.

        Args:
            value: The defaultRouter to set

        Returns:
            self for method chaining

        Note:
            Delegates to default_router property setter (gets validation automatically)
        """
        self.default_router = value  # Delegates to property setter
        return self

    def getDnsServer(self) -> List["Ip6AddressString"]:
        """
        AUTOSAR-compliant getter for dnsServer.

        Returns:
            The dnsServer value

        Note:
            Delegates to dns_server property (CODING_RULE_V2_00017)
        """
        return self.dns_server  # Delegates to property

    def getEnableAnycast(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for enableAnycast.

        Returns:
            The enableAnycast value

        Note:
            Delegates to enable_anycast property (CODING_RULE_V2_00017)
        """
        return self.enable_anycast  # Delegates to property

    def setEnableAnycast(self, value: "Boolean") -> "Ipv6Configuration":
        """
        AUTOSAR-compliant setter for enableAnycast with method chaining.

        Args:
            value: The enableAnycast to set

        Returns:
            self for method chaining

        Note:
            Delegates to enable_anycast property setter (gets validation automatically)
        """
        self.enable_anycast = value  # Delegates to property setter
        return self

    def getHopCount(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for hopCount.

        Returns:
            The hopCount value

        Note:
            Delegates to hop_count property (CODING_RULE_V2_00017)
        """
        return self.hop_count  # Delegates to property

    def setHopCount(self, value: "PositiveInteger") -> "Ipv6Configuration":
        """
        AUTOSAR-compliant setter for hopCount with method chaining.

        Args:
            value: The hopCount to set

        Returns:
            self for method chaining

        Note:
            Delegates to hop_count property setter (gets validation automatically)
        """
        self.hop_count = value  # Delegates to property setter
        return self

    def getIpAddressKeep(self) -> "IpAddressKeepEnum":
        """
        AUTOSAR-compliant getter for ipAddressKeep.

        Returns:
            The ipAddressKeep value

        Note:
            Delegates to ip_address_keep property (CODING_RULE_V2_00017)
        """
        return self.ip_address_keep  # Delegates to property

    def setIpAddressKeep(self, value: "IpAddressKeepEnum") -> "Ipv6Configuration":
        """
        AUTOSAR-compliant setter for ipAddressKeep with method chaining.

        Args:
            value: The ipAddressKeep to set

        Returns:
            self for method chaining

        Note:
            Delegates to ip_address_keep property setter (gets validation automatically)
        """
        self.ip_address_keep = value  # Delegates to property setter
        return self

    def getIpAddressPrefix(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for ipAddressPrefix.

        Returns:
            The ipAddressPrefix value

        Note:
            Delegates to ip_address_prefix property (CODING_RULE_V2_00017)
        """
        return self.ip_address_prefix  # Delegates to property

    def setIpAddressPrefix(self, value: "PositiveInteger") -> "Ipv6Configuration":
        """
        AUTOSAR-compliant setter for ipAddressPrefix with method chaining.

        Args:
            value: The ipAddressPrefix to set

        Returns:
            self for method chaining

        Note:
            Delegates to ip_address_prefix property setter (gets validation automatically)
        """
        self.ip_address_prefix = value  # Delegates to property setter
        return self

    def getIpv6Address(self) -> "Ipv6AddressSource":
        """
        AUTOSAR-compliant getter for ipv6Address.

        Returns:
            The ipv6Address value

        Note:
            Delegates to ipv6_address property (CODING_RULE_V2_00017)
        """
        return self.ipv6_address  # Delegates to property

    def setIpv6Address(self, value: "Ipv6AddressSource") -> "Ipv6Configuration":
        """
        AUTOSAR-compliant setter for ipv6Address with method chaining.

        Args:
            value: The ipv6Address to set

        Returns:
            self for method chaining

        Note:
            Delegates to ipv6_address property setter (gets validation automatically)
        """
        self.ipv6_address = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_assignment(self, value: Optional["PositiveInteger"]) -> "Ipv6Configuration":
        """
        Set assignment and return self for chaining.

        Args:
            value: The assignment to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_assignment("value")
        """
        self.assignment = value  # Use property setter (gets validation)
        return self

    def with_default_router(self, value: Optional["Ip6AddressString"]) -> "Ipv6Configuration":
        """
        Set defaultRouter and return self for chaining.

        Args:
            value: The defaultRouter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_default_router("value")
        """
        self.default_router = value  # Use property setter (gets validation)
        return self

    def with_enable_anycast(self, value: Optional["Boolean"]) -> "Ipv6Configuration":
        """
        Set enableAnycast and return self for chaining.

        Args:
            value: The enableAnycast to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_enable_anycast("value")
        """
        self.enable_anycast = value  # Use property setter (gets validation)
        return self

    def with_hop_count(self, value: Optional["PositiveInteger"]) -> "Ipv6Configuration":
        """
        Set hopCount and return self for chaining.

        Args:
            value: The hopCount to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_hop_count("value")
        """
        self.hop_count = value  # Use property setter (gets validation)
        return self

    def with_ip_address_keep(self, value: Optional["IpAddressKeepEnum"]) -> "Ipv6Configuration":
        """
        Set ipAddressKeep and return self for chaining.

        Args:
            value: The ipAddressKeep to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ip_address_keep("value")
        """
        self.ip_address_keep = value  # Use property setter (gets validation)
        return self

    def with_ip_address_prefix(self, value: Optional["PositiveInteger"]) -> "Ipv6Configuration":
        """
        Set ipAddressPrefix and return self for chaining.

        Args:
            value: The ipAddressPrefix to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ip_address_prefix("value")
        """
        self.ip_address_prefix = value  # Use property setter (gets validation)
        return self

    def with_ipv6_address(self, value: Optional["Ipv6AddressSource"]) -> "Ipv6Configuration":
        """
        Set ipv6Address and return self for chaining.

        Args:
            value: The ipv6Address to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ipv6_address("value")
        """
        self.ipv6_address = value  # Use property setter (gets validation)
        return self
