from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class TcpIpIcmpv6Props(ARObject):
    """
    This meta-class specifies the configuration options for ICMPv6 (Internet
    Control Message Protocol).
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::TcpIpIcmpv6Props
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 156, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # If enabled an ICMPv6 parameter problem message will sent if a received packet
        # has been dropped due to options or headers that are found in the packet.
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

    def setTcpIpIcmp(self, value: "Boolean") -> "TcpIpIcmpv6Props":
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_tcp_ip_icmp(self, value: Optional["Boolean"]) -> "TcpIpIcmpv6Props":
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