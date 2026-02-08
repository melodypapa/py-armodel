from typing import List, Optional
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Describable


class Ipv4DhcpServerConfiguration(Describable):
    """
    Defines the configuration of a IPv4 DHCP server that runs on the network
    endpoint.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::Ipv4DhcpServerConfiguration

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 131, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Upper range of IP addresses to be issued to DHCP Pv4 Address.
        # Notation: 255.
        # 255.
        # 255.
        # 255.
        self._addressRange: Optional["Ip4AddressString"] = None

    @property
    def address_range(self) -> Optional["Ip4AddressString"]:
        """Get addressRange (Pythonic accessor)."""
        return self._addressRange

    @address_range.setter
    def address_range(self, value: Optional["Ip4AddressString"]) -> None:
        """
        Set addressRange with validation.

        Args:
            value: The addressRange to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._addressRange = None
            return

        if not isinstance(value, Ip4AddressString):
            raise TypeError(
                f"addressRange must be Ip4AddressString or None, got {type(value).__name__}"
            )
        self._addressRange = value
        # IP address of the default gateway.
        # Notation.
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
        # Amount of time in seconds that a client may keep the IP.
        self._defaultLease: Optional["TimeValue"] = None

    @property
    def default_lease(self) -> Optional["TimeValue"]:
        """Get defaultLease (Pythonic accessor)."""
        return self._defaultLease

    @default_lease.setter
    def default_lease(self, value: Optional["TimeValue"]) -> None:
        """
        Set defaultLease with validation.

        Args:
            value: The defaultLease to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._defaultLease = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"defaultLease must be TimeValue or None, got {type(value).__name__}"
            )
        self._defaultLease = value
        # IP addresses of preconfigured DNS servers.
        # Notation.
        self._dnsServer: List["Ip4AddressString"] = []

    @property
    def dns_server(self) -> List["Ip4AddressString"]:
        """Get dnsServer (Pythonic accessor)."""
        return self._dnsServer
        # Default network mask to be used by DHCP clients.
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

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAddressRange(self) -> "Ip4AddressString":
        """
        AUTOSAR-compliant getter for addressRange.

        Returns:
            The addressRange value

        Note:
            Delegates to address_range property (CODING_RULE_V2_00017)
        """
        return self.address_range  # Delegates to property

    def setAddressRange(self, value: "Ip4AddressString") -> "Ipv4DhcpServerConfiguration":
        """
        AUTOSAR-compliant setter for addressRange with method chaining.

        Args:
            value: The addressRange to set

        Returns:
            self for method chaining

        Note:
            Delegates to address_range property setter (gets validation automatically)
        """
        self.address_range = value  # Delegates to property setter
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

    def setDefaultGateway(self, value: "Ip4AddressString") -> "Ipv4DhcpServerConfiguration":
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

    def getDefaultLease(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for defaultLease.

        Returns:
            The defaultLease value

        Note:
            Delegates to default_lease property (CODING_RULE_V2_00017)
        """
        return self.default_lease  # Delegates to property

    def setDefaultLease(self, value: "TimeValue") -> "Ipv4DhcpServerConfiguration":
        """
        AUTOSAR-compliant setter for defaultLease with method chaining.

        Args:
            value: The defaultLease to set

        Returns:
            self for method chaining

        Note:
            Delegates to default_lease property setter (gets validation automatically)
        """
        self.default_lease = value  # Delegates to property setter
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

    def getNetworkMask(self) -> "Ip4AddressString":
        """
        AUTOSAR-compliant getter for networkMask.

        Returns:
            The networkMask value

        Note:
            Delegates to network_mask property (CODING_RULE_V2_00017)
        """
        return self.network_mask  # Delegates to property

    def setNetworkMask(self, value: "Ip4AddressString") -> "Ipv4DhcpServerConfiguration":
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_address_range(self, value: Optional["Ip4AddressString"]) -> "Ipv4DhcpServerConfiguration":
        """
        Set addressRange and return self for chaining.

        Args:
            value: The addressRange to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_address_range("value")
        """
        self.address_range = value  # Use property setter (gets validation)
        return self

    def with_default_gateway(self, value: Optional["Ip4AddressString"]) -> "Ipv4DhcpServerConfiguration":
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

    def with_default_lease(self, value: Optional["TimeValue"]) -> "Ipv4DhcpServerConfiguration":
        """
        Set defaultLease and return self for chaining.

        Args:
            value: The defaultLease to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_default_lease("value")
        """
        self.default_lease = value  # Use property setter (gets validation)
        return self

    def with_network_mask(self, value: Optional["Ip4AddressString"]) -> "Ipv4DhcpServerConfiguration":
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
