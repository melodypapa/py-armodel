from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    TcpProps,
    UdpProps,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    ARElement,
)


class EthTcpIpProps(ARElement):
    """
    This meta-class is used to configure the EcuInstance specific TcpIp Stack
    attributes.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::EthTcpIpProps

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 153, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # TCP configuration properties.
        self._tcpProps: Optional["TcpProps"] = None

    @property
    def tcp_props(self) -> Optional["TcpProps"]:
        """Get tcpProps (Pythonic accessor)."""
        return self._tcpProps

    @tcp_props.setter
    def tcp_props(self, value: Optional["TcpProps"]) -> None:
        """
        Set tcpProps with validation.

        Args:
            value: The tcpProps to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpProps = None
            return

        if not isinstance(value, TcpProps):
            raise TypeError(
                f"tcpProps must be TcpProps or None, got {type(value).__name__}"
            )
        self._tcpProps = value
        # UDP configuration properties.
        self._udpProps: Optional["UdpProps"] = None

    @property
    def udp_props(self) -> Optional["UdpProps"]:
        """Get udpProps (Pythonic accessor)."""
        return self._udpProps

    @udp_props.setter
    def udp_props(self, value: Optional["UdpProps"]) -> None:
        """
        Set udpProps with validation.

        Args:
            value: The udpProps to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._udpProps = None
            return

        if not isinstance(value, UdpProps):
            raise TypeError(
                f"udpProps must be UdpProps or None, got {type(value).__name__}"
            )
        self._udpProps = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTcpProps(self) -> "TcpProps":
        """
        AUTOSAR-compliant getter for tcpProps.

        Returns:
            The tcpProps value

        Note:
            Delegates to tcp_props property (CODING_RULE_V2_00017)
        """
        return self.tcp_props  # Delegates to property

    def setTcpProps(self, value: "TcpProps") -> "EthTcpIpProps":
        """
        AUTOSAR-compliant setter for tcpProps with method chaining.

        Args:
            value: The tcpProps to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_props property setter (gets validation automatically)
        """
        self.tcp_props = value  # Delegates to property setter
        return self

    def getUdpProps(self) -> "UdpProps":
        """
        AUTOSAR-compliant getter for udpProps.

        Returns:
            The udpProps value

        Note:
            Delegates to udp_props property (CODING_RULE_V2_00017)
        """
        return self.udp_props  # Delegates to property

    def setUdpProps(self, value: "UdpProps") -> "EthTcpIpProps":
        """
        AUTOSAR-compliant setter for udpProps with method chaining.

        Args:
            value: The udpProps to set

        Returns:
            self for method chaining

        Note:
            Delegates to udp_props property setter (gets validation automatically)
        """
        self.udp_props = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_tcp_props(self, value: Optional["TcpProps"]) -> "EthTcpIpProps":
        """
        Set tcpProps and return self for chaining.

        Args:
            value: The tcpProps to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_props("value")
        """
        self.tcp_props = value  # Use property setter (gets validation)
        return self

    def with_udp_props(self, value: Optional["UdpProps"]) -> "EthTcpIpProps":
        """
        Set udpProps and return self for chaining.

        Args:
            value: The udpProps to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_udp_props("value")
        """
        self.udp_props = value  # Use property setter (gets validation)
        return self
