from typing import Optional


class UdpTp(TcpUdpConfig):
    """
    Content Model for UDP configuration.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::UdpTp

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 459, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Udp Port configuration.
        self._udpTpPort: Optional["TpPort"] = None

    @property
    def udp_tp_port(self) -> Optional["TpPort"]:
        """Get udpTpPort (Pythonic accessor)."""
        return self._udpTpPort

    @udp_tp_port.setter
    def udp_tp_port(self, value: Optional["TpPort"]) -> None:
        """
        Set udpTpPort with validation.

        Args:
            value: The udpTpPort to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._udpTpPort = None
            return

        if not isinstance(value, TpPort):
            raise TypeError(
                f"udpTpPort must be TpPort or None, got {type(value).__name__}"
            )
        self._udpTpPort = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getUdpTpPort(self) -> "TpPort":
        """
        AUTOSAR-compliant getter for udpTpPort.

        Returns:
            The udpTpPort value

        Note:
            Delegates to udp_tp_port property (CODING_RULE_V2_00017)
        """
        return self.udp_tp_port  # Delegates to property

    def setUdpTpPort(self, value: "TpPort") -> "UdpTp":
        """
        AUTOSAR-compliant setter for udpTpPort with method chaining.

        Args:
            value: The udpTpPort to set

        Returns:
            self for method chaining

        Note:
            Delegates to udp_tp_port property setter (gets validation automatically)
        """
        self.udp_tp_port = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_udp_tp_port(self, value: Optional["TpPort"]) -> "UdpTp":
        """
        Set udpTpPort and return self for chaining.

        Args:
            value: The udpTpPort to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_udp_tp_port("value")
        """
        self.udp_tp_port = value  # Use property setter (gets validation)
        return self
