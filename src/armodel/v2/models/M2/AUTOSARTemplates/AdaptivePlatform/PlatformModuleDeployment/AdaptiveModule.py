"""
AUTOSAR Package - AdaptiveModule

Package: M2::AUTOSARTemplates::AdaptivePlatform::PlatformModuleDeployment::AdaptiveModule
"""

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)


class PlatformModuleEthernetEndpointConfiguration(ARElement):
    """
    This meta-class defines the attributes for the configuration of a port,
    protocol type and IP address of the communication on a VLAN.
    
    Package: M2::AUTOSARTemplates::AdaptivePlatform::PlatformModuleDeployment::AdaptiveModule::PlatformModuleEthernetEndpointConfiguration
    
    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 65, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the CommunicationConnector (VLAN) for which the network
        # configuration is defined.
        self._communication: Optional["EthernetCommunication"] = None

    @property
    def communication(self) -> Optional["EthernetCommunication"]:
        """Get communication (Pythonic accessor)."""
        return self._communication

    @communication.setter
    def communication(self, value: Optional["EthernetCommunication"]) -> None:
        """
        Set communication with validation.
        
        Args:
            value: The communication to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._communication = None
            return

        if not isinstance(value, EthernetCommunication):
            raise TypeError(
                f"communication must be EthernetCommunication or None, got {type(value).__name__}"
            )
        self._communication = value
        self._ipv4MulticastIp: Optional["Ip4AddressString"] = None

    @property
    def ipv4_multicast_ip(self) -> Optional["Ip4AddressString"]:
        """Get ipv4MulticastIp (Pythonic accessor)."""
        return self._ipv4MulticastIp

    @ipv4_multicast_ip.setter
    def ipv4_multicast_ip(self, value: Optional["Ip4AddressString"]) -> None:
        """
        Set ipv4MulticastIp with validation.
        
        Args:
            value: The ipv4MulticastIp to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ipv4MulticastIp = None
            return

        if not isinstance(value, Ip4AddressString):
            raise TypeError(
                f"ipv4MulticastIp must be Ip4AddressString or None, got {type(value).__name__}"
            )
        self._ipv4MulticastIp = value
        # Multicast IPv6 Address to which the message will be.
        self._ipv6MulticastIp: Optional["Ip6AddressString"] = None

    @property
    def ipv6_multicast_ip(self) -> Optional["Ip6AddressString"]:
        """Get ipv6MulticastIp (Pythonic accessor)."""
        return self._ipv6MulticastIp

    @ipv6_multicast_ip.setter
    def ipv6_multicast_ip(self, value: Optional["Ip6AddressString"]) -> None:
        """
        Set ipv6MulticastIp with validation.
        
        Args:
            value: The ipv6MulticastIp to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ipv6MulticastIp = None
            return

        if not isinstance(value, Ip6AddressString):
            raise TypeError(
                f"ipv6MulticastIp must be Ip6AddressString or None, got {type(value).__name__}"
            )
        self._ipv6MulticastIp = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCommunication(self) -> "EthernetCommunication":
        """
        AUTOSAR-compliant getter for communication.
        
        Returns:
            The communication value
        
        Note:
            Delegates to communication property (CODING_RULE_V2_00017)
        """
        return self.communication  # Delegates to property

    def setCommunication(self, value: "EthernetCommunication") -> "PlatformModuleEthernetEndpointConfiguration":
        """
        AUTOSAR-compliant setter for communication with method chaining.
        
        Args:
            value: The communication to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to communication property setter (gets validation automatically)
        """
        self.communication = value  # Delegates to property setter
        return self

    def getIpv4MulticastIp(self) -> "Ip4AddressString":
        """
        AUTOSAR-compliant getter for ipv4MulticastIp.
        
        Returns:
            The ipv4MulticastIp value
        
        Note:
            Delegates to ipv4_multicast_ip property (CODING_RULE_V2_00017)
        """
        return self.ipv4_multicast_ip  # Delegates to property

    def setIpv4MulticastIp(self, value: "Ip4AddressString") -> "PlatformModuleEthernetEndpointConfiguration":
        """
        AUTOSAR-compliant setter for ipv4MulticastIp with method chaining.
        
        Args:
            value: The ipv4MulticastIp to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to ipv4_multicast_ip property setter (gets validation automatically)
        """
        self.ipv4_multicast_ip = value  # Delegates to property setter
        return self

    def getIpv6MulticastIp(self) -> "Ip6AddressString":
        """
        AUTOSAR-compliant getter for ipv6MulticastIp.
        
        Returns:
            The ipv6MulticastIp value
        
        Note:
            Delegates to ipv6_multicast_ip property (CODING_RULE_V2_00017)
        """
        return self.ipv6_multicast_ip  # Delegates to property

    def setIpv6MulticastIp(self, value: "Ip6AddressString") -> "PlatformModuleEthernetEndpointConfiguration":
        """
        AUTOSAR-compliant setter for ipv6MulticastIp with method chaining.
        
        Args:
            value: The ipv6MulticastIp to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to ipv6_multicast_ip property setter (gets validation automatically)
        """
        self.ipv6_multicast_ip = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_communication(self, value: Optional["EthernetCommunication"]) -> "PlatformModuleEthernetEndpointConfiguration":
        """
        Set communication and return self for chaining.
        
        Args:
            value: The communication to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_communication("value")
        """
        self.communication = value  # Use property setter (gets validation)
        return self

    def with_ipv4_multicast_ip(self, value: Optional["Ip4AddressString"]) -> "PlatformModuleEthernetEndpointConfiguration":
        """
        Set ipv4MulticastIp and return self for chaining.
        
        Args:
            value: The ipv4MulticastIp to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_ipv4_multicast_ip("value")
        """
        self.ipv4_multicast_ip = value  # Use property setter (gets validation)
        return self

    def with_ipv6_multicast_ip(self, value: Optional["Ip6AddressString"]) -> "PlatformModuleEthernetEndpointConfiguration":
        """
        Set ipv6MulticastIp and return self for chaining.
        
        Args:
            value: The ipv6MulticastIp to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_ipv6_multicast_ip("value")
        """
        self.ipv6_multicast_ip = value  # Use property setter (gets validation)
        return self
