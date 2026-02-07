from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class UdpProps(ARObject):
    """
    This meta-class specifies the configuration options for UDP (User Datagram
    Protocol).
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::UdpProps
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 154, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Default Time-to-live value of outgoing UDP packets.
        self._udpTtl: Optional["PositiveInteger"] = None

    @property
    def udp_ttl(self) -> Optional["PositiveInteger"]:
        """Get udpTtl (Pythonic accessor)."""
        return self._udpTtl

    @udp_ttl.setter
    def udp_ttl(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set udpTtl with validation.
        
        Args:
            value: The udpTtl to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._udpTtl = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"udpTtl must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._udpTtl = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getUdpTtl(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for udpTtl.
        
        Returns:
            The udpTtl value
        
        Note:
            Delegates to udp_ttl property (CODING_RULE_V2_00017)
        """
        return self.udp_ttl  # Delegates to property

    def setUdpTtl(self, value: "PositiveInteger") -> "UdpProps":
        """
        AUTOSAR-compliant setter for udpTtl with method chaining.
        
        Args:
            value: The udpTtl to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to udp_ttl property setter (gets validation automatically)
        """
        self.udp_ttl = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_udp_ttl(self, value: Optional["PositiveInteger"]) -> "UdpProps":
        """
        Set udpTtl and return self for chaining.
        
        Args:
            value: The udpTtl to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_udp_ttl("value")
        """
        self.udp_ttl = value  # Use property setter (gets validation)
        return self