from typing import Optional


class EthernetCommunicationConnector(CommunicationConnector):
    """
    Ethernet specific attributes to the CommunicationConnector.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::EthernetCommunicationConnector

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 117, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # EcuInstance specific IP attributes.
        self._ethIpProps: Optional["EthIpProps"] = None

    @property
    def eth_ip_props(self) -> Optional["EthIpProps"]:
        """Get ethIpProps (Pythonic accessor)."""
        return self._ethIpProps

    @eth_ip_props.setter
    def eth_ip_props(self, value: Optional["EthIpProps"]) -> None:
        """
        Set ethIpProps with validation.

        Args:
            value: The ethIpProps to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ethIpProps = None
            return

        if not isinstance(value, EthIpProps):
            raise TypeError(
                f"ethIpProps must be EthIpProps or None, got {type(value).__name__}"
            )
        self._ethIpProps = value
        # This attribute specifies the maximum transmission unit in.
        self._maximum: Optional["PositiveInteger"] = None

    @property
    def maximum(self) -> Optional["PositiveInteger"]:
        """Get maximum (Pythonic accessor)."""
        return self._maximum

    @maximum.setter
    def maximum(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maximum with validation.

        Args:
            value: The maximum to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maximum = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"maximum must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._maximum = value
        # This attribute specifies the size of neighbor cache or ARP in units of
        # entries.
        self._neighborCache: Optional["PositiveInteger"] = None

    @property
    def neighbor_cache(self) -> Optional["PositiveInteger"]:
        """Get neighborCache (Pythonic accessor)."""
        return self._neighborCache

    @neighbor_cache.setter
    def neighbor_cache(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set neighborCache with validation.

        Args:
            value: The neighborCache to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._neighborCache = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"neighborCache must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._neighborCache = value
        # If enabled the IPv4/IPv6 processes incoming ICMP Too Big" messages and stores
        # a MTU value for address.
        self._pathMtu: Optional["Boolean"] = None

    @property
    def path_mtu(self) -> Optional["Boolean"]:
        """Get pathMtu (Pythonic accessor)."""
        return self._pathMtu

    @path_mtu.setter
    def path_mtu(self, value: Optional["Boolean"]) -> None:
        """
        Set pathMtu with validation.

        Args:
            value: The pathMtu to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pathMtu = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"pathMtu must be Boolean or None, got {type(value).__name__}"
            )
        self._pathMtu = value
        # If this value is >0 the IPv4/IPv6 will reset the MTU value each destination
        # after n seconds.
        self._pathMtuTimeout: Optional["TimeValue"] = None

    @property
    def path_mtu_timeout(self) -> Optional["TimeValue"]:
        """Get pathMtuTimeout (Pythonic accessor)."""
        return self._pathMtuTimeout

    @path_mtu_timeout.setter
    def path_mtu_timeout(self, value: Optional["TimeValue"]) -> None:
        """
        Set pathMtuTimeout with validation.

        Args:
            value: The pathMtuTimeout to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pathMtuTimeout = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"pathMtuTimeout must be TimeValue or None, got {type(value).__name__}"
            )
        self._pathMtuTimeout = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEthIpProps(self) -> "EthIpProps":
        """
        AUTOSAR-compliant getter for ethIpProps.

        Returns:
            The ethIpProps value

        Note:
            Delegates to eth_ip_props property (CODING_RULE_V2_00017)
        """
        return self.eth_ip_props  # Delegates to property

    def setEthIpProps(self, value: "EthIpProps") -> "EthernetCommunicationConnector":
        """
        AUTOSAR-compliant setter for ethIpProps with method chaining.

        Args:
            value: The ethIpProps to set

        Returns:
            self for method chaining

        Note:
            Delegates to eth_ip_props property setter (gets validation automatically)
        """
        self.eth_ip_props = value  # Delegates to property setter
        return self

    def getMaximum(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maximum.

        Returns:
            The maximum value

        Note:
            Delegates to maximum property (CODING_RULE_V2_00017)
        """
        return self.maximum  # Delegates to property

    def setMaximum(self, value: "PositiveInteger") -> "EthernetCommunicationConnector":
        """
        AUTOSAR-compliant setter for maximum with method chaining.

        Args:
            value: The maximum to set

        Returns:
            self for method chaining

        Note:
            Delegates to maximum property setter (gets validation automatically)
        """
        self.maximum = value  # Delegates to property setter
        return self

    def getNeighborCache(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for neighborCache.

        Returns:
            The neighborCache value

        Note:
            Delegates to neighbor_cache property (CODING_RULE_V2_00017)
        """
        return self.neighbor_cache  # Delegates to property

    def setNeighborCache(self, value: "PositiveInteger") -> "EthernetCommunicationConnector":
        """
        AUTOSAR-compliant setter for neighborCache with method chaining.

        Args:
            value: The neighborCache to set

        Returns:
            self for method chaining

        Note:
            Delegates to neighbor_cache property setter (gets validation automatically)
        """
        self.neighbor_cache = value  # Delegates to property setter
        return self

    def getPathMtu(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for pathMtu.

        Returns:
            The pathMtu value

        Note:
            Delegates to path_mtu property (CODING_RULE_V2_00017)
        """
        return self.path_mtu  # Delegates to property

    def setPathMtu(self, value: "Boolean") -> "EthernetCommunicationConnector":
        """
        AUTOSAR-compliant setter for pathMtu with method chaining.

        Args:
            value: The pathMtu to set

        Returns:
            self for method chaining

        Note:
            Delegates to path_mtu property setter (gets validation automatically)
        """
        self.path_mtu = value  # Delegates to property setter
        return self

    def getPathMtuTimeout(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for pathMtuTimeout.

        Returns:
            The pathMtuTimeout value

        Note:
            Delegates to path_mtu_timeout property (CODING_RULE_V2_00017)
        """
        return self.path_mtu_timeout  # Delegates to property

    def setPathMtuTimeout(self, value: "TimeValue") -> "EthernetCommunicationConnector":
        """
        AUTOSAR-compliant setter for pathMtuTimeout with method chaining.

        Args:
            value: The pathMtuTimeout to set

        Returns:
            self for method chaining

        Note:
            Delegates to path_mtu_timeout property setter (gets validation automatically)
        """
        self.path_mtu_timeout = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_eth_ip_props(self, value: Optional["EthIpProps"]) -> "EthernetCommunicationConnector":
        """
        Set ethIpProps and return self for chaining.

        Args:
            value: The ethIpProps to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_eth_ip_props("value")
        """
        self.eth_ip_props = value  # Use property setter (gets validation)
        return self

    def with_maximum(self, value: Optional["PositiveInteger"]) -> "EthernetCommunicationConnector":
        """
        Set maximum and return self for chaining.

        Args:
            value: The maximum to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_maximum("value")
        """
        self.maximum = value  # Use property setter (gets validation)
        return self

    def with_neighbor_cache(self, value: Optional["PositiveInteger"]) -> "EthernetCommunicationConnector":
        """
        Set neighborCache and return self for chaining.

        Args:
            value: The neighborCache to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_neighbor_cache("value")
        """
        self.neighbor_cache = value  # Use property setter (gets validation)
        return self

    def with_path_mtu(self, value: Optional["Boolean"]) -> "EthernetCommunicationConnector":
        """
        Set pathMtu and return self for chaining.

        Args:
            value: The pathMtu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_path_mtu("value")
        """
        self.path_mtu = value  # Use property setter (gets validation)
        return self

    def with_path_mtu_timeout(self, value: Optional["TimeValue"]) -> "EthernetCommunicationConnector":
        """
        Set pathMtuTimeout and return self for chaining.

        Args:
            value: The pathMtuTimeout to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_path_mtu_timeout("value")
        """
        self.path_mtu_timeout = value  # Use property setter (gets validation)
        return self
