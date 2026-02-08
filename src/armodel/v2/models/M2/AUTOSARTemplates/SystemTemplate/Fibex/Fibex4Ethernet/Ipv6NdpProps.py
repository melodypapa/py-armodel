from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import TimeValue
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class Ipv6NdpProps(ARObject):
    """
    This meta-class specifies the configuration options for the Neighbor
    Discovery Protocol for IPv6.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::Ipv6NdpProps

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 150, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Configures the default value (s) for the RetransTimer specified in [RFC4861
                # 6.
        # 3.
        # 2.
        # Host Variables].
        self._tcpIpNdpDefault: Optional["TimeValue"] = None

    @property
    def tcp_ip_ndp_default(self) -> Optional["TimeValue"]:
        """Get tcpIpNdpDefault (Pythonic accessor)."""
        return self._tcpIpNdpDefault

    @tcp_ip_ndp_default.setter
    def tcp_ip_ndp_default(self, value: Optional["TimeValue"]) -> None:
        """
        Set tcpIpNdpDefault with validation.

        Args:
            value: The tcpIpNdpDefault to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpNdpDefault = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"tcpIpNdpDefault must be TimeValue or None, got {type(value).__name__}"
            )
        self._tcpIpNdpDefault = value
        # Maximum number of default router entries.
        self._tcpIpNdpDefaultRouterListSize: Optional["PositiveInteger"] = None

    @property
    def tcp_ip_ndp_default_router_list_size(self) -> Optional["PositiveInteger"]:
        """Get tcpIpNdpDefaultRouterListSize (Pythonic accessor)."""
        return self._tcpIpNdpDefaultRouterListSize

    @tcp_ip_ndp_default_router_list_size.setter
    def tcp_ip_ndp_default_router_list_size(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set tcpIpNdpDefaultRouterListSize with validation.

        Args:
            value: The tcpIpNdpDefaultRouterListSize to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpNdpDefaultRouterListSize = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"tcpIpNdpDefaultRouterListSize must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._tcpIpNdpDefaultRouterListSize = value
        # If enabled the value of ReachableTime will be multiplied a random value
        # between MIN_RANDOM_FACTOR MAX_RANDOM_FACTOR in order to prevent nodes from
        # transmitting at exactly the same time.
        self._tcpIpNdp: Optional["Boolean"] = None

    @property
    def tcp_ip_ndp(self) -> Optional["Boolean"]:
        """Get tcpIpNdp (Pythonic accessor)."""
        return self._tcpIpNdp

    @tcp_ip_ndp.setter
    def tcp_ip_ndp(self, value: Optional["Boolean"]) -> None:
        """
        Set tcpIpNdp with validation.

        Args:
            value: The tcpIpNdp to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpNdp = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"tcpIpNdp must be Boolean or None, got {type(value).__name__}"
            )
        self._tcpIpNdp = value
        # Delay before sending the first NUD probe in (s).
        self._tcpIpNdpDelayFirstProbeTimeValue: Optional["TimeValue"] = None

    @property
    def tcp_ip_ndp_delay_first_probe_time_value(self) -> Optional["TimeValue"]:
        """Get tcpIpNdpDelayFirstProbeTimeValue (Pythonic accessor)."""
        return self._tcpIpNdpDelayFirstProbeTimeValue

    @tcp_ip_ndp_delay_first_probe_time_value.setter
    def tcp_ip_ndp_delay_first_probe_time_value(self, value: Optional["TimeValue"]) -> None:
        """
        Set tcpIpNdpDelayFirstProbeTimeValue with validation.

        Args:
            value: The tcpIpNdpDelayFirstProbeTimeValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpNdpDelayFirstProbeTimeValue = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"tcpIpNdpDelayFirstProbeTimeValue must be TimeValue or None, got {type(value).__name__}"
            )
        self._tcpIpNdpDelayFirstProbeTimeValue = value
        # Maximum random factor used for randomization.
        self._tcpIpNdpMaxRandomFactor: Optional["PositiveInteger"] = None

    @property
    def tcp_ip_ndp_max_random_factor(self) -> Optional["PositiveInteger"]:
        """Get tcpIpNdpMaxRandomFactor (Pythonic accessor)."""
        return self._tcpIpNdpMaxRandomFactor

    @tcp_ip_ndp_max_random_factor.setter
    def tcp_ip_ndp_max_random_factor(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set tcpIpNdpMaxRandomFactor with validation.

        Args:
            value: The tcpIpNdpMaxRandomFactor to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpNdpMaxRandomFactor = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"tcpIpNdpMaxRandomFactor must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._tcpIpNdpMaxRandomFactor = value
        # Maximum number of Router Solicitations that will be sent the first Router
        # Advertisement has been received.
        self._tcpIpNdpMaxRtr: Optional["PositiveInteger"] = None

    @property
    def tcp_ip_ndp_max_rtr(self) -> Optional["PositiveInteger"]:
        """Get tcpIpNdpMaxRtr (Pythonic accessor)."""
        return self._tcpIpNdpMaxRtr

    @tcp_ip_ndp_max_rtr.setter
    def tcp_ip_ndp_max_rtr(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set tcpIpNdpMaxRtr with validation.

        Args:
            value: The tcpIpNdpMaxRtr to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpNdpMaxRtr = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"tcpIpNdpMaxRtr must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._tcpIpNdpMaxRtr = value
        # Minimum random factor used for randomization.
        self._tcpIpNdpMinRandomFactor: Optional["PositiveInteger"] = None

    @property
    def tcp_ip_ndp_min_random_factor(self) -> Optional["PositiveInteger"]:
        """Get tcpIpNdpMinRandomFactor (Pythonic accessor)."""
        return self._tcpIpNdpMinRandomFactor

    @tcp_ip_ndp_min_random_factor.setter
    def tcp_ip_ndp_min_random_factor(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set tcpIpNdpMinRandomFactor with validation.

        Args:
            value: The tcpIpNdpMinRandomFactor to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpNdpMinRandomFactor = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"tcpIpNdpMinRandomFactor must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._tcpIpNdpMinRandomFactor = value
        # Maximum number of unicast solicitations that will be sent performig Neighbor
        # Unreachability Detection.
        self._tcpIpNdpNum: Optional["PositiveInteger"] = None

    @property
    def tcp_ip_ndp_num(self) -> Optional["PositiveInteger"]:
        """Get tcpIpNdpNum (Pythonic accessor)."""
        return self._tcpIpNdpNum

    @tcp_ip_ndp_num.setter
    def tcp_ip_ndp_num(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set tcpIpNdpNum with validation.

        Args:
            value: The tcpIpNdpNum to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpNdpNum = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"tcpIpNdpNum must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._tcpIpNdpNum = value
        # Enables (TRUE) or disables (FALSE) support of a NDP Queue according to IETF
        # RFC 4861, section.
        self._tcpIpNdpPacket: Optional["Boolean"] = None

    @property
    def tcp_ip_ndp_packet(self) -> Optional["Boolean"]:
        """Get tcpIpNdpPacket (Pythonic accessor)."""
        return self._tcpIpNdpPacket

    @tcp_ip_ndp_packet.setter
    def tcp_ip_ndp_packet(self, value: Optional["Boolean"]) -> None:
        """
        Set tcpIpNdpPacket with validation.

        Args:
            value: The tcpIpNdpPacket to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpNdpPacket = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"tcpIpNdpPacket must be Boolean or None, got {type(value).__name__}"
            )
        self._tcpIpNdpPacket = value
        # Maximum number of entries in the on-link prefix list.
        self._tcpIpNdpPrefix: Optional["PositiveInteger"] = None

    @property
    def tcp_ip_ndp_prefix(self) -> Optional["PositiveInteger"]:
        """Get tcpIpNdpPrefix (Pythonic accessor)."""
        return self._tcpIpNdpPrefix

    @tcp_ip_ndp_prefix.setter
    def tcp_ip_ndp_prefix(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set tcpIpNdpPrefix with validation.

        Args:
            value: The tcpIpNdpPrefix to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpNdpPrefix = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"tcpIpNdpPrefix must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._tcpIpNdpPrefix = value
        # If enabled the first router solicitation will be delayed from [0.
        # MAX_RTR_SOLICITATION_DELAY].
        # the first router solicitation will be sent after milliseconds.
        self._tcpIpNdpRndRtr: Optional["Boolean"] = None

    @property
    def tcp_ip_ndp_rnd_rtr(self) -> Optional["Boolean"]:
        """Get tcpIpNdpRndRtr (Pythonic accessor)."""
        return self._tcpIpNdpRndRtr

    @tcp_ip_ndp_rnd_rtr.setter
    def tcp_ip_ndp_rnd_rtr(self, value: Optional["Boolean"]) -> None:
        """
        Set tcpIpNdpRndRtr with validation.

        Args:
            value: The tcpIpNdpRndRtr to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpNdpRndRtr = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"tcpIpNdpRndRtr must be Boolean or None, got {type(value).__name__}"
            )
        self._tcpIpNdpRndRtr = value
        # Interval between consecutive Router Solicitations in (s).
        self._tcpIpNdpRtr: Optional["TimeValue"] = None

    @property
    def tcp_ip_ndp_rtr(self) -> Optional["TimeValue"]:
        """Get tcpIpNdpRtr (Pythonic accessor)."""
        return self._tcpIpNdpRtr

    @tcp_ip_ndp_rtr.setter
    def tcp_ip_ndp_rtr(self, value: Optional["TimeValue"]) -> None:
        """
        Set tcpIpNdpRtr with validation.

        Args:
            value: The tcpIpNdpRtr to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpNdpRtr = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"tcpIpNdpRtr must be TimeValue or None, got {type(value).__name__}"
            )
        self._tcpIpNdpRtr = value
        # Enable Optimistic Duplicate Address Detection (DAD) to RFC4429.
        self._tcpIpNdpSlaac: Optional["Boolean"] = None

    @property
    def tcp_ip_ndp_slaac(self) -> Optional["Boolean"]:
        """Get tcpIpNdpSlaac (Pythonic accessor)."""
        return self._tcpIpNdpSlaac

    @tcp_ip_ndp_slaac.setter
    def tcp_ip_ndp_slaac(self, value: Optional["Boolean"]) -> None:
        """
        Set tcpIpNdpSlaac with validation.

        Args:
            value: The tcpIpNdpSlaac to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpNdpSlaac = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"tcpIpNdpSlaac must be Boolean or None, got {type(value).__name__}"
            )
        self._tcpIpNdpSlaac = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTcpIpNdpDefault(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for tcpIpNdpDefault.

        Returns:
            The tcpIpNdpDefault value

        Note:
            Delegates to tcp_ip_ndp_default property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_ndp_default  # Delegates to property

    def setTcpIpNdpDefault(self, value: "TimeValue") -> "Ipv6NdpProps":
        """
        AUTOSAR-compliant setter for tcpIpNdpDefault with method chaining.

        Args:
            value: The tcpIpNdpDefault to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_ndp_default property setter (gets validation automatically)
        """
        self.tcp_ip_ndp_default = value  # Delegates to property setter
        return self

    def getTcpIpNdpDefaultRouterListSize(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for tcpIpNdpDefaultRouterListSize.

        Returns:
            The tcpIpNdpDefaultRouterListSize value

        Note:
            Delegates to tcp_ip_ndp_default_router_list_size property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_ndp_default_router_list_size  # Delegates to property

    def setTcpIpNdpDefaultRouterListSize(self, value: "PositiveInteger") -> "Ipv6NdpProps":
        """
        AUTOSAR-compliant setter for tcpIpNdpDefaultRouterListSize with method chaining.

        Args:
            value: The tcpIpNdpDefaultRouterListSize to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_ndp_default_router_list_size property setter (gets validation automatically)
        """
        self.tcp_ip_ndp_default_router_list_size = value  # Delegates to property setter
        return self

    def getTcpIpNdp(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for tcpIpNdp.

        Returns:
            The tcpIpNdp value

        Note:
            Delegates to tcp_ip_ndp property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_ndp  # Delegates to property

    def setTcpIpNdp(self, value: "Boolean") -> "Ipv6NdpProps":
        """
        AUTOSAR-compliant setter for tcpIpNdp with method chaining.

        Args:
            value: The tcpIpNdp to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_ndp property setter (gets validation automatically)
        """
        self.tcp_ip_ndp = value  # Delegates to property setter
        return self

    def getTcpIpNdpDelayFirstProbeTimeValue(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for tcpIpNdpDelayFirstProbeTimeValue.

        Returns:
            The tcpIpNdpDelayFirstProbeTimeValue value

        Note:
            Delegates to tcp_ip_ndp_delay_first_probe_time_value property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_ndp_delay_first_probe_time_value  # Delegates to property

    def setTcpIpNdpDelayFirstProbeTimeValue(self, value: "TimeValue") -> "Ipv6NdpProps":
        """
        AUTOSAR-compliant setter for tcpIpNdpDelayFirstProbeTimeValue with method chaining.

        Args:
            value: The tcpIpNdpDelayFirstProbeTimeValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_ndp_delay_first_probe_time_value property setter (gets validation automatically)
        """
        self.tcp_ip_ndp_delay_first_probe_time_value = value  # Delegates to property setter
        return self

    def getTcpIpNdpMaxRandomFactor(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for tcpIpNdpMaxRandomFactor.

        Returns:
            The tcpIpNdpMaxRandomFactor value

        Note:
            Delegates to tcp_ip_ndp_max_random_factor property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_ndp_max_random_factor  # Delegates to property

    def setTcpIpNdpMaxRandomFactor(self, value: "PositiveInteger") -> "Ipv6NdpProps":
        """
        AUTOSAR-compliant setter for tcpIpNdpMaxRandomFactor with method chaining.

        Args:
            value: The tcpIpNdpMaxRandomFactor to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_ndp_max_random_factor property setter (gets validation automatically)
        """
        self.tcp_ip_ndp_max_random_factor = value  # Delegates to property setter
        return self

    def getTcpIpNdpMaxRtr(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for tcpIpNdpMaxRtr.

        Returns:
            The tcpIpNdpMaxRtr value

        Note:
            Delegates to tcp_ip_ndp_max_rtr property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_ndp_max_rtr  # Delegates to property

    def setTcpIpNdpMaxRtr(self, value: "PositiveInteger") -> "Ipv6NdpProps":
        """
        AUTOSAR-compliant setter for tcpIpNdpMaxRtr with method chaining.

        Args:
            value: The tcpIpNdpMaxRtr to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_ndp_max_rtr property setter (gets validation automatically)
        """
        self.tcp_ip_ndp_max_rtr = value  # Delegates to property setter
        return self

    def getTcpIpNdpMinRandomFactor(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for tcpIpNdpMinRandomFactor.

        Returns:
            The tcpIpNdpMinRandomFactor value

        Note:
            Delegates to tcp_ip_ndp_min_random_factor property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_ndp_min_random_factor  # Delegates to property

    def setTcpIpNdpMinRandomFactor(self, value: "PositiveInteger") -> "Ipv6NdpProps":
        """
        AUTOSAR-compliant setter for tcpIpNdpMinRandomFactor with method chaining.

        Args:
            value: The tcpIpNdpMinRandomFactor to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_ndp_min_random_factor property setter (gets validation automatically)
        """
        self.tcp_ip_ndp_min_random_factor = value  # Delegates to property setter
        return self

    def getTcpIpNdpNum(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for tcpIpNdpNum.

        Returns:
            The tcpIpNdpNum value

        Note:
            Delegates to tcp_ip_ndp_num property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_ndp_num  # Delegates to property

    def setTcpIpNdpNum(self, value: "PositiveInteger") -> "Ipv6NdpProps":
        """
        AUTOSAR-compliant setter for tcpIpNdpNum with method chaining.

        Args:
            value: The tcpIpNdpNum to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_ndp_num property setter (gets validation automatically)
        """
        self.tcp_ip_ndp_num = value  # Delegates to property setter
        return self

    def getTcpIpNdpPacket(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for tcpIpNdpPacket.

        Returns:
            The tcpIpNdpPacket value

        Note:
            Delegates to tcp_ip_ndp_packet property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_ndp_packet  # Delegates to property

    def setTcpIpNdpPacket(self, value: "Boolean") -> "Ipv6NdpProps":
        """
        AUTOSAR-compliant setter for tcpIpNdpPacket with method chaining.

        Args:
            value: The tcpIpNdpPacket to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_ndp_packet property setter (gets validation automatically)
        """
        self.tcp_ip_ndp_packet = value  # Delegates to property setter
        return self

    def getTcpIpNdpPrefix(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for tcpIpNdpPrefix.

        Returns:
            The tcpIpNdpPrefix value

        Note:
            Delegates to tcp_ip_ndp_prefix property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_ndp_prefix  # Delegates to property

    def setTcpIpNdpPrefix(self, value: "PositiveInteger") -> "Ipv6NdpProps":
        """
        AUTOSAR-compliant setter for tcpIpNdpPrefix with method chaining.

        Args:
            value: The tcpIpNdpPrefix to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_ndp_prefix property setter (gets validation automatically)
        """
        self.tcp_ip_ndp_prefix = value  # Delegates to property setter
        return self

    def getTcpIpNdpRndRtr(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for tcpIpNdpRndRtr.

        Returns:
            The tcpIpNdpRndRtr value

        Note:
            Delegates to tcp_ip_ndp_rnd_rtr property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_ndp_rnd_rtr  # Delegates to property

    def setTcpIpNdpRndRtr(self, value: "Boolean") -> "Ipv6NdpProps":
        """
        AUTOSAR-compliant setter for tcpIpNdpRndRtr with method chaining.

        Args:
            value: The tcpIpNdpRndRtr to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_ndp_rnd_rtr property setter (gets validation automatically)
        """
        self.tcp_ip_ndp_rnd_rtr = value  # Delegates to property setter
        return self

    def getTcpIpNdpRtr(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for tcpIpNdpRtr.

        Returns:
            The tcpIpNdpRtr value

        Note:
            Delegates to tcp_ip_ndp_rtr property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_ndp_rtr  # Delegates to property

    def setTcpIpNdpRtr(self, value: "TimeValue") -> "Ipv6NdpProps":
        """
        AUTOSAR-compliant setter for tcpIpNdpRtr with method chaining.

        Args:
            value: The tcpIpNdpRtr to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_ndp_rtr property setter (gets validation automatically)
        """
        self.tcp_ip_ndp_rtr = value  # Delegates to property setter
        return self

    def getTcpIpNdpSlaac(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for tcpIpNdpSlaac.

        Returns:
            The tcpIpNdpSlaac value

        Note:
            Delegates to tcp_ip_ndp_slaac property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_ndp_slaac  # Delegates to property

    def setTcpIpNdpSlaac(self, value: "Boolean") -> "Ipv6NdpProps":
        """
        AUTOSAR-compliant setter for tcpIpNdpSlaac with method chaining.

        Args:
            value: The tcpIpNdpSlaac to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_ndp_slaac property setter (gets validation automatically)
        """
        self.tcp_ip_ndp_slaac = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_tcp_ip_ndp_default(self, value: Optional["TimeValue"]) -> "Ipv6NdpProps":
        """
        Set tcpIpNdpDefault and return self for chaining.

        Args:
            value: The tcpIpNdpDefault to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_ndp_default("value")
        """
        self.tcp_ip_ndp_default = value  # Use property setter (gets validation)
        return self

    def with_tcp_ip_ndp_default_router_list_size(self, value: Optional["PositiveInteger"]) -> "Ipv6NdpProps":
        """
        Set tcpIpNdpDefaultRouterListSize and return self for chaining.

        Args:
            value: The tcpIpNdpDefaultRouterListSize to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_ndp_default_router_list_size("value")
        """
        self.tcp_ip_ndp_default_router_list_size = value  # Use property setter (gets validation)
        return self

    def with_tcp_ip_ndp(self, value: Optional["Boolean"]) -> "Ipv6NdpProps":
        """
        Set tcpIpNdp and return self for chaining.

        Args:
            value: The tcpIpNdp to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_ndp("value")
        """
        self.tcp_ip_ndp = value  # Use property setter (gets validation)
        return self

    def with_tcp_ip_ndp_delay_first_probe_time_value(self, value: Optional["TimeValue"]) -> "Ipv6NdpProps":
        """
        Set tcpIpNdpDelayFirstProbeTimeValue and return self for chaining.

        Args:
            value: The tcpIpNdpDelayFirstProbeTimeValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_ndp_delay_first_probe_time_value("value")
        """
        self.tcp_ip_ndp_delay_first_probe_time_value = value  # Use property setter (gets validation)
        return self

    def with_tcp_ip_ndp_max_random_factor(self, value: Optional["PositiveInteger"]) -> "Ipv6NdpProps":
        """
        Set tcpIpNdpMaxRandomFactor and return self for chaining.

        Args:
            value: The tcpIpNdpMaxRandomFactor to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_ndp_max_random_factor("value")
        """
        self.tcp_ip_ndp_max_random_factor = value  # Use property setter (gets validation)
        return self

    def with_tcp_ip_ndp_max_rtr(self, value: Optional["PositiveInteger"]) -> "Ipv6NdpProps":
        """
        Set tcpIpNdpMaxRtr and return self for chaining.

        Args:
            value: The tcpIpNdpMaxRtr to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_ndp_max_rtr("value")
        """
        self.tcp_ip_ndp_max_rtr = value  # Use property setter (gets validation)
        return self

    def with_tcp_ip_ndp_min_random_factor(self, value: Optional["PositiveInteger"]) -> "Ipv6NdpProps":
        """
        Set tcpIpNdpMinRandomFactor and return self for chaining.

        Args:
            value: The tcpIpNdpMinRandomFactor to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_ndp_min_random_factor("value")
        """
        self.tcp_ip_ndp_min_random_factor = value  # Use property setter (gets validation)
        return self

    def with_tcp_ip_ndp_num(self, value: Optional["PositiveInteger"]) -> "Ipv6NdpProps":
        """
        Set tcpIpNdpNum and return self for chaining.

        Args:
            value: The tcpIpNdpNum to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_ndp_num("value")
        """
        self.tcp_ip_ndp_num = value  # Use property setter (gets validation)
        return self

    def with_tcp_ip_ndp_packet(self, value: Optional["Boolean"]) -> "Ipv6NdpProps":
        """
        Set tcpIpNdpPacket and return self for chaining.

        Args:
            value: The tcpIpNdpPacket to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_ndp_packet("value")
        """
        self.tcp_ip_ndp_packet = value  # Use property setter (gets validation)
        return self

    def with_tcp_ip_ndp_prefix(self, value: Optional["PositiveInteger"]) -> "Ipv6NdpProps":
        """
        Set tcpIpNdpPrefix and return self for chaining.

        Args:
            value: The tcpIpNdpPrefix to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_ndp_prefix("value")
        """
        self.tcp_ip_ndp_prefix = value  # Use property setter (gets validation)
        return self

    def with_tcp_ip_ndp_rnd_rtr(self, value: Optional["Boolean"]) -> "Ipv6NdpProps":
        """
        Set tcpIpNdpRndRtr and return self for chaining.

        Args:
            value: The tcpIpNdpRndRtr to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_ndp_rnd_rtr("value")
        """
        self.tcp_ip_ndp_rnd_rtr = value  # Use property setter (gets validation)
        return self

    def with_tcp_ip_ndp_rtr(self, value: Optional["TimeValue"]) -> "Ipv6NdpProps":
        """
        Set tcpIpNdpRtr and return self for chaining.

        Args:
            value: The tcpIpNdpRtr to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_ndp_rtr("value")
        """
        self.tcp_ip_ndp_rtr = value  # Use property setter (gets validation)
        return self

    def with_tcp_ip_ndp_slaac(self, value: Optional["Boolean"]) -> "Ipv6NdpProps":
        """
        Set tcpIpNdpSlaac and return self for chaining.

        Args:
            value: The tcpIpNdpSlaac to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_ndp_slaac("value")
        """
        self.tcp_ip_ndp_slaac = value  # Use property setter (gets validation)
        return self
