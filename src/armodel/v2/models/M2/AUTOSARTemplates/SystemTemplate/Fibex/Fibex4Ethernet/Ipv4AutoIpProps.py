from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class Ipv4AutoIpProps(ARObject):
    """
    Specifies the configuration options for Auto-IP (automatic private IP
    addressing).

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::Ipv4AutoIpProps

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 147, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute specifies the time in seconds Auto-IP waits startup, before
                # beginning with ARP probing.
        # This delay to give DHCP time to acquire a lease in case a is present.
        self._tcpIpAutoIpInit: Optional["TimeValue"] = None

    @property
    def tcp_ip_auto_ip_init(self) -> Optional["TimeValue"]:
        """Get tcpIpAutoIpInit (Pythonic accessor)."""
        return self._tcpIpAutoIpInit

    @tcp_ip_auto_ip_init.setter
    def tcp_ip_auto_ip_init(self, value: Optional["TimeValue"]) -> None:
        """
        Set tcpIpAutoIpInit with validation.

        Args:
            value: The tcpIpAutoIpInit to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpAutoIpInit = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"tcpIpAutoIpInit must be TimeValue or None, got {type(value).__name__}"
            )
        self._tcpIpAutoIpInit = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTcpIpAutoIpInit(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for tcpIpAutoIpInit.

        Returns:
            The tcpIpAutoIpInit value

        Note:
            Delegates to tcp_ip_auto_ip_init property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_auto_ip_init  # Delegates to property

    def setTcpIpAutoIpInit(self, value: "TimeValue") -> "Ipv4AutoIpProps":
        """
        AUTOSAR-compliant setter for tcpIpAutoIpInit with method chaining.

        Args:
            value: The tcpIpAutoIpInit to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_auto_ip_init property setter (gets validation automatically)
        """
        self.tcp_ip_auto_ip_init = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_tcp_ip_auto_ip_init(self, value: Optional["TimeValue"]) -> "Ipv4AutoIpProps":
        """
        Set tcpIpAutoIpInit and return self for chaining.

        Args:
            value: The tcpIpAutoIpInit to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_auto_ip_init("value")
        """
        self.tcp_ip_auto_ip_init = value  # Use property setter (gets validation)
        return self
