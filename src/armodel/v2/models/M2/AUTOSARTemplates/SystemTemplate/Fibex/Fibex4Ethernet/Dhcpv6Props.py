from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class Dhcpv6Props(ARObject):
    """
    This meta-class specifies the configuration options for DHCPv6.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::Dhcpv6Props

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 149, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Minimum delay in seconds before the first Confirm will be sent.
        self._tcpIpDhcp: Optional["TimeValue"] = None

    @property
    def tcp_ip_dhcp(self) -> Optional["TimeValue"]:
        """Get tcpIpDhcp (Pythonic accessor)."""
        return self._tcpIpDhcp

    @tcp_ip_dhcp.setter
    def tcp_ip_dhcp(self, value: Optional["TimeValue"]) -> None:
        """
        Set tcpIpDhcp with validation.

        Args:
            value: The tcpIpDhcp to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpDhcp = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"tcpIpDhcp must be TimeValue or None, got {type(value).__name__}"
            )
        self._tcpIpDhcp = value
        # Minimum delay (s) before the first Information Request will be sent.
        self._tcpIpDhcpV6Inf: Optional["TimeValue"] = None

    @property
    def tcp_ip_dhcp_v6_inf(self) -> Optional["TimeValue"]:
        """Get tcpIpDhcpV6Inf (Pythonic accessor)."""
        return self._tcpIpDhcpV6Inf

    @tcp_ip_dhcp_v6_inf.setter
    def tcp_ip_dhcp_v6_inf(self, value: Optional["TimeValue"]) -> None:
        """
        Set tcpIpDhcpV6Inf with validation.

        Args:
            value: The tcpIpDhcpV6Inf to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpDhcpV6Inf = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"tcpIpDhcpV6Inf must be TimeValue or None, got {type(value).__name__}"
            )
        self._tcpIpDhcpV6Inf = value
        # Minimum delay (s) before the first Solicit message will be.
        self._tcpIpDhcpV6Sol: Optional["TimeValue"] = None

    @property
    def tcp_ip_dhcp_v6_sol(self) -> Optional["TimeValue"]:
        """Get tcpIpDhcpV6Sol (Pythonic accessor)."""
        return self._tcpIpDhcpV6Sol

    @tcp_ip_dhcp_v6_sol.setter
    def tcp_ip_dhcp_v6_sol(self, value: Optional["TimeValue"]) -> None:
        """
        Set tcpIpDhcpV6Sol with validation.

        Args:
            value: The tcpIpDhcpV6Sol to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpDhcpV6Sol = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"tcpIpDhcpV6Sol must be TimeValue or None, got {type(value).__name__}"
            )
        self._tcpIpDhcpV6Sol = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTcpIpDhcp(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for tcpIpDhcp.

        Returns:
            The tcpIpDhcp value

        Note:
            Delegates to tcp_ip_dhcp property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_dhcp  # Delegates to property

    def setTcpIpDhcp(self, value: "TimeValue") -> "Dhcpv6Props":
        """
        AUTOSAR-compliant setter for tcpIpDhcp with method chaining.

        Args:
            value: The tcpIpDhcp to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_dhcp property setter (gets validation automatically)
        """
        self.tcp_ip_dhcp = value  # Delegates to property setter
        return self

    def getTcpIpDhcpV6Inf(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for tcpIpDhcpV6Inf.

        Returns:
            The tcpIpDhcpV6Inf value

        Note:
            Delegates to tcp_ip_dhcp_v6_inf property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_dhcp_v6_inf  # Delegates to property

    def setTcpIpDhcpV6Inf(self, value: "TimeValue") -> "Dhcpv6Props":
        """
        AUTOSAR-compliant setter for tcpIpDhcpV6Inf with method chaining.

        Args:
            value: The tcpIpDhcpV6Inf to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_dhcp_v6_inf property setter (gets validation automatically)
        """
        self.tcp_ip_dhcp_v6_inf = value  # Delegates to property setter
        return self

    def getTcpIpDhcpV6Sol(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for tcpIpDhcpV6Sol.

        Returns:
            The tcpIpDhcpV6Sol value

        Note:
            Delegates to tcp_ip_dhcp_v6_sol property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_dhcp_v6_sol  # Delegates to property

    def setTcpIpDhcpV6Sol(self, value: "TimeValue") -> "Dhcpv6Props":
        """
        AUTOSAR-compliant setter for tcpIpDhcpV6Sol with method chaining.

        Args:
            value: The tcpIpDhcpV6Sol to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_dhcp_v6_sol property setter (gets validation automatically)
        """
        self.tcp_ip_dhcp_v6_sol = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_tcp_ip_dhcp(self, value: Optional["TimeValue"]) -> "Dhcpv6Props":
        """
        Set tcpIpDhcp and return self for chaining.

        Args:
            value: The tcpIpDhcp to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_dhcp("value")
        """
        self.tcp_ip_dhcp = value  # Use property setter (gets validation)
        return self

    def with_tcp_ip_dhcp_v6_inf(self, value: Optional["TimeValue"]) -> "Dhcpv6Props":
        """
        Set tcpIpDhcpV6Inf and return self for chaining.

        Args:
            value: The tcpIpDhcpV6Inf to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_dhcp_v6_inf("value")
        """
        self.tcp_ip_dhcp_v6_inf = value  # Use property setter (gets validation)
        return self

    def with_tcp_ip_dhcp_v6_sol(self, value: Optional["TimeValue"]) -> "Dhcpv6Props":
        """
        Set tcpIpDhcpV6Sol and return self for chaining.

        Args:
            value: The tcpIpDhcpV6Sol to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_dhcp_v6_sol("value")
        """
        self.tcp_ip_dhcp_v6_sol = value  # Use property setter (gets validation)
        return self
