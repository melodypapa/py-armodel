from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class Ipv4FragmentationProps(ARObject):
    """
    Specifies the configuration options for IPv4 packet
    fragmentation/reassembly.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::Ipv4FragmentationProps

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 147, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Enables (TRUE) or disables (FALSE) support for of incoming datagrams that are
        # fragmented to IETF RFC 815 (IP Datagram Reassembly.
        self._tcpIpIp: Optional["Boolean"] = None

    @property
    def tcp_ip_ip(self) -> Optional["Boolean"]:
        """Get tcpIpIp (Pythonic accessor)."""
        return self._tcpIpIp

    @tcp_ip_ip.setter
    def tcp_ip_ip(self, value: Optional["Boolean"]) -> None:
        """
        Set tcpIpIp with validation.

        Args:
            value: The tcpIpIp to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpIp = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"tcpIpIp must be Boolean or None, got {type(value).__name__}"
            )
        self._tcpIpIp = value
        # Specifies the maximum number of fragmented IP that can be reassembled in
        # parallel.
        self._tcpIpIpNum: Optional["PositiveInteger"] = None

    @property
    def tcp_ip_ip_num(self) -> Optional["PositiveInteger"]:
        """Get tcpIpIpNum (Pythonic accessor)."""
        return self._tcpIpIpNum

    @tcp_ip_ip_num.setter
    def tcp_ip_ip_num(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set tcpIpIpNum with validation.

        Args:
            value: The tcpIpIpNum to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpIpNum = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"tcpIpIpNum must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._tcpIpIpNum = value
        # Specifies the timeout in [s] after which an incomplete gets discarded.
        self._tcpIpIpReass: Optional["TimeValue"] = None

    @property
    def tcp_ip_ip_reass(self) -> Optional["TimeValue"]:
        """Get tcpIpIpReass (Pythonic accessor)."""
        return self._tcpIpIpReass

    @tcp_ip_ip_reass.setter
    def tcp_ip_ip_reass(self, value: Optional["TimeValue"]) -> None:
        """
        Set tcpIpIpReass with validation.

        Args:
            value: The tcpIpIpReass to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpIpReass = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"tcpIpIpReass must be TimeValue or None, got {type(value).__name__}"
            )
        self._tcpIpIpReass = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTcpIpIp(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for tcpIpIp.

        Returns:
            The tcpIpIp value

        Note:
            Delegates to tcp_ip_ip property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_ip  # Delegates to property

    def setTcpIpIp(self, value: "Boolean") -> "Ipv4FragmentationProps":
        """
        AUTOSAR-compliant setter for tcpIpIp with method chaining.

        Args:
            value: The tcpIpIp to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_ip property setter (gets validation automatically)
        """
        self.tcp_ip_ip = value  # Delegates to property setter
        return self

    def getTcpIpIpNum(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for tcpIpIpNum.

        Returns:
            The tcpIpIpNum value

        Note:
            Delegates to tcp_ip_ip_num property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_ip_num  # Delegates to property

    def setTcpIpIpNum(self, value: "PositiveInteger") -> "Ipv4FragmentationProps":
        """
        AUTOSAR-compliant setter for tcpIpIpNum with method chaining.

        Args:
            value: The tcpIpIpNum to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_ip_num property setter (gets validation automatically)
        """
        self.tcp_ip_ip_num = value  # Delegates to property setter
        return self

    def getTcpIpIpReass(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for tcpIpIpReass.

        Returns:
            The tcpIpIpReass value

        Note:
            Delegates to tcp_ip_ip_reass property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_ip_reass  # Delegates to property

    def setTcpIpIpReass(self, value: "TimeValue") -> "Ipv4FragmentationProps":
        """
        AUTOSAR-compliant setter for tcpIpIpReass with method chaining.

        Args:
            value: The tcpIpIpReass to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_ip_reass property setter (gets validation automatically)
        """
        self.tcp_ip_ip_reass = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_tcp_ip_ip(self, value: Optional["Boolean"]) -> "Ipv4FragmentationProps":
        """
        Set tcpIpIp and return self for chaining.

        Args:
            value: The tcpIpIp to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_ip("value")
        """
        self.tcp_ip_ip = value  # Use property setter (gets validation)
        return self

    def with_tcp_ip_ip_num(self, value: Optional["PositiveInteger"]) -> "Ipv4FragmentationProps":
        """
        Set tcpIpIpNum and return self for chaining.

        Args:
            value: The tcpIpIpNum to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_ip_num("value")
        """
        self.tcp_ip_ip_num = value  # Use property setter (gets validation)
        return self

    def with_tcp_ip_ip_reass(self, value: Optional["TimeValue"]) -> "Ipv4FragmentationProps":
        """
        Set tcpIpIpReass and return self for chaining.

        Args:
            value: The tcpIpIpReass to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_ip_reass("value")
        """
        self.tcp_ip_ip_reass = value  # Use property setter (gets validation)
        return self
