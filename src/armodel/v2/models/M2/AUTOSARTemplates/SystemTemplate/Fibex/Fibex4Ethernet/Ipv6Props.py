from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class Ipv6Props(ARObject):
    """
    This meta-class specifies the configuration options for IPv6.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::Ipv6Props
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 147, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Configuration properties for DHCPv6.
        self._dhcpProps: Optional["Dhcpv6Props"] = None

    @property
    def dhcp_props(self) -> Optional["Dhcpv6Props"]:
        """Get dhcpProps (Pythonic accessor)."""
        return self._dhcpProps

    @dhcp_props.setter
    def dhcp_props(self, value: Optional["Dhcpv6Props"]) -> None:
        """
        Set dhcpProps with validation.
        
        Args:
            value: The dhcpProps to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dhcpProps = None
            return

        if not isinstance(value, Dhcpv6Props):
            raise TypeError(
                f"dhcpProps must be Dhcpv6Props or None, got {type(value).__name__}"
            )
        self._dhcpProps = value
        # Configuration properties for IPv6 packet fragmentation/ reassembly.
        self._fragmentation: Optional["Ipv6Fragmentation"] = None

    @property
    def fragmentation(self) -> Optional["Ipv6Fragmentation"]:
        """Get fragmentation (Pythonic accessor)."""
        return self._fragmentation

    @fragmentation.setter
    def fragmentation(self, value: Optional["Ipv6Fragmentation"]) -> None:
        """
        Set fragmentation with validation.
        
        Args:
            value: The fragmentation to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._fragmentation = None
            return

        if not isinstance(value, Ipv6Fragmentation):
            raise TypeError(
                f"fragmentation must be Ipv6Fragmentation or None, got {type(value).__name__}"
            )
        self._fragmentation = value
        # Configuration properties for the Neighbor Discovery IPv6.
        self._ndpProps: Optional["Ipv6NdpProps"] = None

    @property
    def ndp_props(self) -> Optional["Ipv6NdpProps"]:
        """Get ndpProps (Pythonic accessor)."""
        return self._ndpProps

    @ndp_props.setter
    def ndp_props(self, value: Optional["Ipv6NdpProps"]) -> None:
        """
        Set ndpProps with validation.
        
        Args:
            value: The ndpProps to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ndpProps = None
            return

        if not isinstance(value, Ipv6NdpProps):
            raise TypeError(
                f"ndpProps must be Ipv6NdpProps or None, got {type(value).__name__}"
            )
        self._ndpProps = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDhcpProps(self) -> "Dhcpv6Props":
        """
        AUTOSAR-compliant getter for dhcpProps.
        
        Returns:
            The dhcpProps value
        
        Note:
            Delegates to dhcp_props property (CODING_RULE_V2_00017)
        """
        return self.dhcp_props  # Delegates to property

    def setDhcpProps(self, value: "Dhcpv6Props") -> "Ipv6Props":
        """
        AUTOSAR-compliant setter for dhcpProps with method chaining.
        
        Args:
            value: The dhcpProps to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to dhcp_props property setter (gets validation automatically)
        """
        self.dhcp_props = value  # Delegates to property setter
        return self

    def getFragmentation(self) -> "Ipv6Fragmentation":
        """
        AUTOSAR-compliant getter for fragmentation.
        
        Returns:
            The fragmentation value
        
        Note:
            Delegates to fragmentation property (CODING_RULE_V2_00017)
        """
        return self.fragmentation  # Delegates to property

    def setFragmentation(self, value: "Ipv6Fragmentation") -> "Ipv6Props":
        """
        AUTOSAR-compliant setter for fragmentation with method chaining.
        
        Args:
            value: The fragmentation to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to fragmentation property setter (gets validation automatically)
        """
        self.fragmentation = value  # Delegates to property setter
        return self

    def getNdpProps(self) -> "Ipv6NdpProps":
        """
        AUTOSAR-compliant getter for ndpProps.
        
        Returns:
            The ndpProps value
        
        Note:
            Delegates to ndp_props property (CODING_RULE_V2_00017)
        """
        return self.ndp_props  # Delegates to property

    def setNdpProps(self, value: "Ipv6NdpProps") -> "Ipv6Props":
        """
        AUTOSAR-compliant setter for ndpProps with method chaining.
        
        Args:
            value: The ndpProps to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to ndp_props property setter (gets validation automatically)
        """
        self.ndp_props = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_dhcp_props(self, value: Optional["Dhcpv6Props"]) -> "Ipv6Props":
        """
        Set dhcpProps and return self for chaining.
        
        Args:
            value: The dhcpProps to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_dhcp_props("value")
        """
        self.dhcp_props = value  # Use property setter (gets validation)
        return self

    def with_fragmentation(self, value: Optional["Ipv6Fragmentation"]) -> "Ipv6Props":
        """
        Set fragmentation and return self for chaining.
        
        Args:
            value: The fragmentation to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_fragmentation("value")
        """
        self.fragmentation = value  # Use property setter (gets validation)
        return self

    def with_ndp_props(self, value: Optional["Ipv6NdpProps"]) -> "Ipv6Props":
        """
        Set ndpProps and return self for chaining.
        
        Args:
            value: The ndpProps to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_ndp_props("value")
        """
        self.ndp_props = value  # Use property setter (gets validation)
        return self