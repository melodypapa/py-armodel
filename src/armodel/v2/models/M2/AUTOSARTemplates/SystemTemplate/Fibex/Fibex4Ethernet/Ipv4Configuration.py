from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    NetworkEndpointAddress,
)


class Ipv4Configuration(NetworkEndpointAddress):
    """
    Internet Protocol version 4 (IPv4) configuration.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 465, Classic Platform R23-11)
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
        # IP address of the default gateway.
        self._defaultGateway: Optional["Ip4AddressString"] = None

    @property
    def default_gateway(self) -> Optional["Ip4AddressString"]:
        """Get defaultGateway (Pythonic accessor)."""
        return self._defaultGateway

    @default_gateway.setter
    def default_gateway(self, value: Optional["Ip4AddressString"]) -> None:
        """
        Set defaultGateway with validation.

        Args:
            value: The defaultGateway to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._defaultGateway = None
            return

        if not isinstance(value, Ip4AddressString):
            raise TypeError(
                f"defaultGateway must be Ip4AddressString or None, got {type(value).__name__}"
            )
        self._defaultGateway = value
        # IP addresses of preconfigured DNS servers.
        # xml.
        # namePlural=DNS-SERVER-ADDRESSES.
        self._dnsServer: List["Ip4AddressString"] = []

    @property
    def dns_server(self) -> List["Ip4AddressString"]:
        """Get dnsServer (Pythonic accessor)."""
        return self._dnsServer
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
        # Defines how the node obtains its IP address.
        self._ipv4Address: Optional["Ipv4AddressSource"] = None

    @property
    def ipv4_address(self) -> Optional["Ipv4AddressSource"]:
        """Get ipv4Address (Pythonic accessor)."""
        return self._ipv4Address

    @ipv4_address.setter
    def ipv4_address(self, value: Optional["Ipv4AddressSource"]) -> None:
        """
        Set ipv4Address with validation.

        Args:
            value: The ipv4Address to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ipv4Address = None
            return

        if not isinstance(value, Ipv4AddressSource):
            raise TypeError(
                f"ipv4Address must be Ipv4AddressSource or None, got {type(value).__name__}"
            )
        self._ipv4Address = value
        # Network mask.
        # Notation 255.
        # 255.
        # 255.
        # 255.
        self._networkMask: Optional["Ip4AddressString"] = None

    @property
    def network_mask(self) -> Optional["Ip4AddressString"]:
        """Get networkMask (Pythonic accessor)."""
        return self._networkMask

    @network_mask.setter
    def network_mask(self, value: Optional["Ip4AddressString"]) -> None:
        """
        Set networkMask with validation.

        Args:
            value: The networkMask to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._networkMask = None
            return

        if not isinstance(value, Ip4AddressString):
            raise TypeError(
                f"networkMask must be Ip4AddressString or None, got {type(value).__name__}"
            )
        self._networkMask = value
        # Lifespan of data (0.
        # 255).
        # The purpose of the TimeToLive to avoid a situation in which an undeliverable
                # circulating on a system.
        self._ttl: Optional["PositiveInteger"] = None

    @property
    def ttl(self) -> Optional["PositiveInteger"]:
        """Get ttl (Pythonic accessor)."""
        return self._ttl

    @ttl.setter
    def ttl(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set ttl with validation.

        Args:
            value: The ttl to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ttl = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"ttl must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._ttl = value

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

    def setAssignment(self, value: "PositiveInteger") -> "Ipv4Configuration":
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

    def getDefaultGateway(self) -> "Ip4AddressString":
        """
        AUTOSAR-compliant getter for defaultGateway.

        Returns:
            The defaultGateway value

        Note:
            Delegates to default_gateway property (CODING_RULE_V2_00017)
        """
        return self.default_gateway  # Delegates to property

    def setDefaultGateway(self, value: "Ip4AddressString") -> "Ipv4Configuration":
        """
        AUTOSAR-compliant setter for defaultGateway with method chaining.

        Args:
            value: The defaultGateway to set

        Returns:
            self for method chaining

        Note:
            Delegates to default_gateway property setter (gets validation automatically)
        """
        self.default_gateway = value  # Delegates to property setter
        return self

    def getDnsServer(self) -> List["Ip4AddressString"]:
        """
        AUTOSAR-compliant getter for dnsServer.

        Returns:
            The dnsServer value

        Note:
            Delegates to dns_server property (CODING_RULE_V2_00017)
        """
        return self.dns_server  # Delegates to property

    def getIpAddressKeep(self) -> "IpAddressKeepEnum":
        """
        AUTOSAR-compliant getter for ipAddressKeep.

        Returns:
            The ipAddressKeep value

        Note:
            Delegates to ip_address_keep property (CODING_RULE_V2_00017)
        """
        return self.ip_address_keep  # Delegates to property

    def setIpAddressKeep(self, value: "IpAddressKeepEnum") -> "Ipv4Configuration":
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

    def getIpv4Address(self) -> "Ipv4AddressSource":
        """
        AUTOSAR-compliant getter for ipv4Address.

        Returns:
            The ipv4Address value

        Note:
            Delegates to ipv4_address property (CODING_RULE_V2_00017)
        """
        return self.ipv4_address  # Delegates to property

    def setIpv4Address(self, value: "Ipv4AddressSource") -> "Ipv4Configuration":
        """
        AUTOSAR-compliant setter for ipv4Address with method chaining.

        Args:
            value: The ipv4Address to set

        Returns:
            self for method chaining

        Note:
            Delegates to ipv4_address property setter (gets validation automatically)
        """
        self.ipv4_address = value  # Delegates to property setter
        return self

    def getNetworkMask(self) -> "Ip4AddressString":
        """
        AUTOSAR-compliant getter for networkMask.

        Returns:
            The networkMask value

        Note:
            Delegates to network_mask property (CODING_RULE_V2_00017)
        """
        return self.network_mask  # Delegates to property

    def setNetworkMask(self, value: "Ip4AddressString") -> "Ipv4Configuration":
        """
        AUTOSAR-compliant setter for networkMask with method chaining.

        Args:
            value: The networkMask to set

        Returns:
            self for method chaining

        Note:
            Delegates to network_mask property setter (gets validation automatically)
        """
        self.network_mask = value  # Delegates to property setter
        return self

    def getTtl(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for ttl.

        Returns:
            The ttl value

        Note:
            Delegates to ttl property (CODING_RULE_V2_00017)
        """
        return self.ttl  # Delegates to property

    def setTtl(self, value: "PositiveInteger") -> "Ipv4Configuration":
        """
        AUTOSAR-compliant setter for ttl with method chaining.

        Args:
            value: The ttl to set

        Returns:
            self for method chaining

        Note:
            Delegates to ttl property setter (gets validation automatically)
        """
        self.ttl = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_assignment(self, value: Optional["PositiveInteger"]) -> "Ipv4Configuration":
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

    def with_default_gateway(self, value: Optional["Ip4AddressString"]) -> "Ipv4Configuration":
        """
        Set defaultGateway and return self for chaining.

        Args:
            value: The defaultGateway to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_default_gateway("value")
        """
        self.default_gateway = value  # Use property setter (gets validation)
        return self

    def with_ip_address_keep(self, value: Optional["IpAddressKeepEnum"]) -> "Ipv4Configuration":
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

    def with_ipv4_address(self, value: Optional["Ipv4AddressSource"]) -> "Ipv4Configuration":
        """
        Set ipv4Address and return self for chaining.

        Args:
            value: The ipv4Address to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ipv4_address("value")
        """
        self.ipv4_address = value  # Use property setter (gets validation)
        return self

    def with_network_mask(self, value: Optional["Ip4AddressString"]) -> "Ipv4Configuration":
        """
        Set networkMask and return self for chaining.

        Args:
            value: The networkMask to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_network_mask("value")
        """
        self.network_mask = value  # Use property setter (gets validation)
        return self

    def with_ttl(self, value: Optional["PositiveInteger"]) -> "Ipv4Configuration":
        """
        Set ttl and return self for chaining.

        Args:
            value: The ttl to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ttl("value")
        """
        self.ttl = value  # Use property setter (gets validation)
        return self
