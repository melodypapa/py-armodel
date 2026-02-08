from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class TcpIpIcmpv4Props(ARObject):
    """
    This meta-class specifies the configuration options for ICMPv4 (Internet
    Control Message Protocol).

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::TcpIpIcmpv4Props

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 156, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute enables or disables transmission of ICMP reply message in case
        # of a ICMP echo reception.
        self._tcpIpIcmp: Optional["Boolean"] = None

    @property
    def tcp_ip_icmp(self) -> Optional["Boolean"]:
        """Get tcpIpIcmp (Pythonic accessor)."""
        return self._tcpIpIcmp

    @tcp_ip_icmp.setter
    def tcp_ip_icmp(self, value: Optional["Boolean"]) -> None:
        """
        Set tcpIpIcmp with validation.

        Args:
            value: The tcpIpIcmp to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpIcmp = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"tcpIpIcmp must be Boolean or None, got {type(value).__name__}"
            )
        self._tcpIpIcmp = value
        # This attribute is only relevant in case that ICMP (Internet Protocol) is
                # used.
        # It specifies the default of outgoing ICMP packets.
        self._tcpIpIcmpV4Ttl: Optional["PositiveInteger"] = None

    @property
    def tcp_ip_icmp_v4_ttl(self) -> Optional["PositiveInteger"]:
        """Get tcpIpIcmpV4Ttl (Pythonic accessor)."""
        return self._tcpIpIcmpV4Ttl

    @tcp_ip_icmp_v4_ttl.setter
    def tcp_ip_icmp_v4_ttl(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set tcpIpIcmpV4Ttl with validation.

        Args:
            value: The tcpIpIcmpV4Ttl to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpIcmpV4Ttl = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"tcpIpIcmpV4Ttl must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._tcpIpIcmpV4Ttl = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTcpIpIcmp(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for tcpIpIcmp.

        Returns:
            The tcpIpIcmp value

        Note:
            Delegates to tcp_ip_icmp property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_icmp  # Delegates to property

    def setTcpIpIcmp(self, value: "Boolean") -> "TcpIpIcmpv4Props":
        """
        AUTOSAR-compliant setter for tcpIpIcmp with method chaining.

        Args:
            value: The tcpIpIcmp to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_icmp property setter (gets validation automatically)
        """
        self.tcp_ip_icmp = value  # Delegates to property setter
        return self

    def getTcpIpIcmpV4Ttl(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for tcpIpIcmpV4Ttl.

        Returns:
            The tcpIpIcmpV4Ttl value

        Note:
            Delegates to tcp_ip_icmp_v4_ttl property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_icmp_v4_ttl  # Delegates to property

    def setTcpIpIcmpV4Ttl(self, value: "PositiveInteger") -> "TcpIpIcmpv4Props":
        """
        AUTOSAR-compliant setter for tcpIpIcmpV4Ttl with method chaining.

        Args:
            value: The tcpIpIcmpV4Ttl to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_icmp_v4_ttl property setter (gets validation automatically)
        """
        self.tcp_ip_icmp_v4_ttl = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_tcp_ip_icmp(self, value: Optional["Boolean"]) -> "TcpIpIcmpv4Props":
        """
        Set tcpIpIcmp and return self for chaining.

        Args:
            value: The tcpIpIcmp to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_icmp("value")
        """
        self.tcp_ip_icmp = value  # Use property setter (gets validation)
        return self

    def with_tcp_ip_icmp_v4_ttl(self, value: Optional["PositiveInteger"]) -> "TcpIpIcmpv4Props":
        """
        Set tcpIpIcmpV4Ttl and return self for chaining.

        Args:
            value: The tcpIpIcmpV4Ttl to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_icmp_v4_ttl("value")
        """
        self.tcp_ip_icmp_v4_ttl = value  # Use property setter (gets validation)
        return self
