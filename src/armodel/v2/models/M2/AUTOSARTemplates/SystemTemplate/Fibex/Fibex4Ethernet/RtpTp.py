from typing import Optional


class RtpTp(TransportProtocolConfiguration):
    """
    RTP over UDP or over TCP as transport protocol.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::RtpTp

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 460, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Synchronization source identifier uniquely identifies the a stream.
        # The synchronization sources within RTP session will be unique.
        self._ssrc: Optional["PositiveInteger"] = None

    @property
    def ssrc(self) -> Optional["PositiveInteger"]:
        """Get ssrc (Pythonic accessor)."""
        return self._ssrc

    @ssrc.setter
    def ssrc(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set ssrc with validation.

        Args:
            value: The ssrc to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ssrc = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"ssrc must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._ssrc = value
        # Tcp or Udp Configuration.
        self._tcpUdpConfig: Optional["TcpUdpConfig"] = None

    @property
    def tcp_udp_config(self) -> Optional["TcpUdpConfig"]:
        """Get tcpUdpConfig (Pythonic accessor)."""
        return self._tcpUdpConfig

    @tcp_udp_config.setter
    def tcp_udp_config(self, value: Optional["TcpUdpConfig"]) -> None:
        """
        Set tcpUdpConfig with validation.

        Args:
            value: The tcpUdpConfig to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpUdpConfig = None
            return

        if not isinstance(value, TcpUdpConfig):
            raise TypeError(
                f"tcpUdpConfig must be TcpUdpConfig or None, got {type(value).__name__}"
            )
        self._tcpUdpConfig = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSsrc(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for ssrc.

        Returns:
            The ssrc value

        Note:
            Delegates to ssrc property (CODING_RULE_V2_00017)
        """
        return self.ssrc  # Delegates to property

    def setSsrc(self, value: "PositiveInteger") -> "RtpTp":
        """
        AUTOSAR-compliant setter for ssrc with method chaining.

        Args:
            value: The ssrc to set

        Returns:
            self for method chaining

        Note:
            Delegates to ssrc property setter (gets validation automatically)
        """
        self.ssrc = value  # Delegates to property setter
        return self

    def getTcpUdpConfig(self) -> "TcpUdpConfig":
        """
        AUTOSAR-compliant getter for tcpUdpConfig.

        Returns:
            The tcpUdpConfig value

        Note:
            Delegates to tcp_udp_config property (CODING_RULE_V2_00017)
        """
        return self.tcp_udp_config  # Delegates to property

    def setTcpUdpConfig(self, value: "TcpUdpConfig") -> "RtpTp":
        """
        AUTOSAR-compliant setter for tcpUdpConfig with method chaining.

        Args:
            value: The tcpUdpConfig to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_udp_config property setter (gets validation automatically)
        """
        self.tcp_udp_config = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ssrc(self, value: Optional["PositiveInteger"]) -> "RtpTp":
        """
        Set ssrc and return self for chaining.

        Args:
            value: The ssrc to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ssrc("value")
        """
        self.ssrc = value  # Use property setter (gets validation)
        return self

    def with_tcp_udp_config(self, value: Optional["TcpUdpConfig"]) -> "RtpTp":
        """
        Set tcpUdpConfig and return self for chaining.

        Args:
            value: The tcpUdpConfig to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_udp_config("value")
        """
        self.tcp_udp_config = value  # Use property setter (gets validation)
        return self
