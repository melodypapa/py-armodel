from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class Ipv4ArpProps(ARObject):
    """
    Specifies the configuration options for the ARP (Address Resolution
    Protocol).
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::Ipv4ArpProps
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 146, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute specifies the number of gratuitous ARP which shall be sent on
        # assignment of a new IP.
        self._tcpIpArpNum: Optional["PositiveInteger"] = None

    @property
    def tcp_ip_arp_num(self) -> Optional["PositiveInteger"]:
        """Get tcpIpArpNum (Pythonic accessor)."""
        return self._tcpIpArpNum

    @tcp_ip_arp_num.setter
    def tcp_ip_arp_num(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set tcpIpArpNum with validation.
        
        Args:
            value: The tcpIpArpNum to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpArpNum = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"tcpIpArpNum must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._tcpIpArpNum = value
        # This attribute enables (TRUE) or disables (FALSE) of the ARP Packet Queue
                # according to IETF RFC 2.
        # 3.
        # 2.
        # 2.
        self._tcpIpArpPacket: Optional["Boolean"] = None

    @property
    def tcp_ip_arp_packet(self) -> Optional["Boolean"]:
        """Get tcpIpArpPacket (Pythonic accessor)."""
        return self._tcpIpArpPacket

    @tcp_ip_arp_packet.setter
    def tcp_ip_arp_packet(self, value: Optional["Boolean"]) -> None:
        """
        Set tcpIpArpPacket with validation.
        
        Args:
            value: The tcpIpArpPacket to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpArpPacket = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"tcpIpArpPacket must be Boolean or None, got {type(value).__name__}"
            )
        self._tcpIpArpPacket = value
        # This attribute specifies a timeout in seconds for the of ARP requests.
        # After the transmission of an request the TcpIp shall skip the transmission of
                # any requests to the same destination within a tcpIpArpRequestTimeout seconds.
        # (IETF RFC 2.
        # 3.
        # 2.
        # 1).
        self._tcpIpArp: Optional["TimeValue"] = None

    @property
    def tcp_ip_arp(self) -> Optional["TimeValue"]:
        """Get tcpIpArp (Pythonic accessor)."""
        return self._tcpIpArp

    @tcp_ip_arp.setter
    def tcp_ip_arp(self, value: Optional["TimeValue"]) -> None:
        """
        Set tcpIpArp with validation.
        
        Args:
            value: The tcpIpArp to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpArp = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"tcpIpArp must be TimeValue or None, got {type(value).__name__}"
            )
        self._tcpIpArp = value
        # This attribute specifies the timeout in seconds after which unused ARP entry
        # is removed.
        self._tcpIpArpTable: Optional["TimeValue"] = None

    @property
    def tcp_ip_arp_table(self) -> Optional["TimeValue"]:
        """Get tcpIpArpTable (Pythonic accessor)."""
        return self._tcpIpArpTable

    @tcp_ip_arp_table.setter
    def tcp_ip_arp_table(self, value: Optional["TimeValue"]) -> None:
        """
        Set tcpIpArpTable with validation.
        
        Args:
            value: The tcpIpArpTable to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpArpTable = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"tcpIpArpTable must be TimeValue or None, got {type(value).__name__}"
            )
        self._tcpIpArpTable = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTcpIpArpNum(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for tcpIpArpNum.
        
        Returns:
            The tcpIpArpNum value
        
        Note:
            Delegates to tcp_ip_arp_num property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_arp_num  # Delegates to property

    def setTcpIpArpNum(self, value: "PositiveInteger") -> "Ipv4ArpProps":
        """
        AUTOSAR-compliant setter for tcpIpArpNum with method chaining.
        
        Args:
            value: The tcpIpArpNum to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to tcp_ip_arp_num property setter (gets validation automatically)
        """
        self.tcp_ip_arp_num = value  # Delegates to property setter
        return self

    def getTcpIpArpPacket(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for tcpIpArpPacket.
        
        Returns:
            The tcpIpArpPacket value
        
        Note:
            Delegates to tcp_ip_arp_packet property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_arp_packet  # Delegates to property

    def setTcpIpArpPacket(self, value: "Boolean") -> "Ipv4ArpProps":
        """
        AUTOSAR-compliant setter for tcpIpArpPacket with method chaining.
        
        Args:
            value: The tcpIpArpPacket to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to tcp_ip_arp_packet property setter (gets validation automatically)
        """
        self.tcp_ip_arp_packet = value  # Delegates to property setter
        return self

    def getTcpIpArp(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for tcpIpArp.
        
        Returns:
            The tcpIpArp value
        
        Note:
            Delegates to tcp_ip_arp property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_arp  # Delegates to property

    def setTcpIpArp(self, value: "TimeValue") -> "Ipv4ArpProps":
        """
        AUTOSAR-compliant setter for tcpIpArp with method chaining.
        
        Args:
            value: The tcpIpArp to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to tcp_ip_arp property setter (gets validation automatically)
        """
        self.tcp_ip_arp = value  # Delegates to property setter
        return self

    def getTcpIpArpTable(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for tcpIpArpTable.
        
        Returns:
            The tcpIpArpTable value
        
        Note:
            Delegates to tcp_ip_arp_table property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_arp_table  # Delegates to property

    def setTcpIpArpTable(self, value: "TimeValue") -> "Ipv4ArpProps":
        """
        AUTOSAR-compliant setter for tcpIpArpTable with method chaining.
        
        Args:
            value: The tcpIpArpTable to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to tcp_ip_arp_table property setter (gets validation automatically)
        """
        self.tcp_ip_arp_table = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_tcp_ip_arp_num(self, value: Optional["PositiveInteger"]) -> "Ipv4ArpProps":
        """
        Set tcpIpArpNum and return self for chaining.
        
        Args:
            value: The tcpIpArpNum to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_tcp_ip_arp_num("value")
        """
        self.tcp_ip_arp_num = value  # Use property setter (gets validation)
        return self

    def with_tcp_ip_arp_packet(self, value: Optional["Boolean"]) -> "Ipv4ArpProps":
        """
        Set tcpIpArpPacket and return self for chaining.
        
        Args:
            value: The tcpIpArpPacket to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_tcp_ip_arp_packet("value")
        """
        self.tcp_ip_arp_packet = value  # Use property setter (gets validation)
        return self

    def with_tcp_ip_arp(self, value: Optional["TimeValue"]) -> "Ipv4ArpProps":
        """
        Set tcpIpArp and return self for chaining.
        
        Args:
            value: The tcpIpArp to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_tcp_ip_arp("value")
        """
        self.tcp_ip_arp = value  # Use property setter (gets validation)
        return self

    def with_tcp_ip_arp_table(self, value: Optional["TimeValue"]) -> "Ipv4ArpProps":
        """
        Set tcpIpArpTable and return self for chaining.
        
        Args:
            value: The tcpIpArpTable to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_tcp_ip_arp_table("value")
        """
        self.tcp_ip_arp_table = value  # Use property setter (gets validation)
        return self