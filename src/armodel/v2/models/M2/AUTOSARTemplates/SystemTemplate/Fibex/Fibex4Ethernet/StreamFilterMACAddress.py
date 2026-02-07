from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class StreamFilterMACAddress(ARObject):
    """
    Configuration of filter rules on the DataLink layer
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::StreamFilterMACAddress
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 137, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Filter to match packets with the MAC address range.
        # atp.
        # Status=candidate.
        self._macAddress: Optional["MacAddressString"] = None

    @property
    def mac_address(self) -> Optional["MacAddressString"]:
        """Get macAddress (Pythonic accessor)."""
        return self._macAddress

    @mac_address.setter
    def mac_address(self, value: Optional["MacAddressString"]) -> None:
        """
        Set macAddress with validation.
        
        Args:
            value: The macAddress to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._macAddress = None
            return

        if not isinstance(value, MacAddressString):
            raise TypeError(
                f"macAddress must be MacAddressString or None, got {type(value).__name__}"
            )
        self._macAddress = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMacAddress(self) -> "MacAddressString":
        """
        AUTOSAR-compliant getter for macAddress.
        
        Returns:
            The macAddress value
        
        Note:
            Delegates to mac_address property (CODING_RULE_V2_00017)
        """
        return self.mac_address  # Delegates to property

    def setMacAddress(self, value: "MacAddressString") -> "StreamFilterMACAddress":
        """
        AUTOSAR-compliant setter for macAddress with method chaining.
        
        Args:
            value: The macAddress to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to mac_address property setter (gets validation automatically)
        """
        self.mac_address = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_mac_address(self, value: Optional["MacAddressString"]) -> "StreamFilterMACAddress":
        """
        Set macAddress and return self for chaining.
        
        Args:
            value: The macAddress to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_mac_address("value")
        """
        self.mac_address = value  # Use property setter (gets validation)
        return self