from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class IEEE1722TpConnection(ARElement, ABC):
    """
    Definition of the IEEE1722Tp protocol.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp::IEEE1722TpConnection
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 637, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is IEEE1722TpConnection:
            raise TypeError("IEEE1722TpConnection is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Optional definition of the destination MAC address for this If no given then
        # macAddressStreamId is used as address.
        self._destinationMac: Optional["MacAddressString"] = None

    @property
    def destination_mac(self) -> Optional["MacAddressString"]:
        """Get destinationMac (Pythonic accessor)."""
        return self._destinationMac

    @destination_mac.setter
    def destination_mac(self, value: Optional["MacAddressString"]) -> None:
        """
        Set destinationMac with validation.
        
        Args:
            value: The destinationMac to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._destinationMac = None
            return

        if not isinstance(value, MacAddressString):
            raise TypeError(
                f"destinationMac must be MacAddressString or None, got {type(value).__name__}"
            )
        self._destinationMac = value
        # MAC Address part of the Stream Id.
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
        # Reference to the lower layer Pdu used for the transport.
        self._pdu: RefType = None

    @property
    def pdu(self) -> RefType:
        """Get pdu (Pythonic accessor)."""
        return self._pdu

    @pdu.setter
    def pdu(self, value: RefType) -> None:
        """
        Set pdu with validation.
        
        Args:
            value: The pdu to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pdu = None
            return

        self._pdu = value
        # Unique Id part of the Stream Id.
        self._uniqueStreamId: Optional["PositiveInteger"] = None

    @property
    def unique_stream_id(self) -> Optional["PositiveInteger"]:
        """Get uniqueStreamId (Pythonic accessor)."""
        return self._uniqueStreamId

    @unique_stream_id.setter
    def unique_stream_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set uniqueStreamId with validation.
        
        Args:
            value: The uniqueStreamId to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._uniqueStreamId = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"uniqueStreamId must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._uniqueStreamId = value
        # Version of the IEEE1722TP stream.
        self._version: Optional["PositiveInteger"] = None

    @property
    def version(self) -> Optional["PositiveInteger"]:
        """Get version (Pythonic accessor)."""
        return self._version

    @version.setter
    def version(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set version with validation.
        
        Args:
            value: The version to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._version = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"version must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._version = value
        # Optional definition of the VLAN priority for this stream.
        self._vlanPriority: Optional["PositiveInteger"] = None

    @property
    def vlan_priority(self) -> Optional["PositiveInteger"]:
        """Get vlanPriority (Pythonic accessor)."""
        return self._vlanPriority

    @vlan_priority.setter
    def vlan_priority(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set vlanPriority with validation.
        
        Args:
            value: The vlanPriority to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._vlanPriority = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"vlanPriority must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._vlanPriority = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDestinationMac(self) -> "MacAddressString":
        """
        AUTOSAR-compliant getter for destinationMac.
        
        Returns:
            The destinationMac value
        
        Note:
            Delegates to destination_mac property (CODING_RULE_V2_00017)
        """
        return self.destination_mac  # Delegates to property

    def setDestinationMac(self, value: "MacAddressString") -> "IEEE1722TpConnection":
        """
        AUTOSAR-compliant setter for destinationMac with method chaining.
        
        Args:
            value: The destinationMac to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to destination_mac property setter (gets validation automatically)
        """
        self.destination_mac = value  # Delegates to property setter
        return self

    def getMacAddress(self) -> "MacAddressString":
        """
        AUTOSAR-compliant getter for macAddress.
        
        Returns:
            The macAddress value
        
        Note:
            Delegates to mac_address property (CODING_RULE_V2_00017)
        """
        return self.mac_address  # Delegates to property

    def setMacAddress(self, value: "MacAddressString") -> "IEEE1722TpConnection":
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

    def getPdu(self) -> RefType:
        """
        AUTOSAR-compliant getter for pdu.
        
        Returns:
            The pdu value
        
        Note:
            Delegates to pdu property (CODING_RULE_V2_00017)
        """
        return self.pdu  # Delegates to property

    def setPdu(self, value: RefType) -> "IEEE1722TpConnection":
        """
        AUTOSAR-compliant setter for pdu with method chaining.
        
        Args:
            value: The pdu to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to pdu property setter (gets validation automatically)
        """
        self.pdu = value  # Delegates to property setter
        return self

    def getUniqueStreamId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for uniqueStreamId.
        
        Returns:
            The uniqueStreamId value
        
        Note:
            Delegates to unique_stream_id property (CODING_RULE_V2_00017)
        """
        return self.unique_stream_id  # Delegates to property

    def setUniqueStreamId(self, value: "PositiveInteger") -> "IEEE1722TpConnection":
        """
        AUTOSAR-compliant setter for uniqueStreamId with method chaining.
        
        Args:
            value: The uniqueStreamId to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to unique_stream_id property setter (gets validation automatically)
        """
        self.unique_stream_id = value  # Delegates to property setter
        return self

    def getVersion(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for version.
        
        Returns:
            The version value
        
        Note:
            Delegates to version property (CODING_RULE_V2_00017)
        """
        return self.version  # Delegates to property

    def setVersion(self, value: "PositiveInteger") -> "IEEE1722TpConnection":
        """
        AUTOSAR-compliant setter for version with method chaining.
        
        Args:
            value: The version to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to version property setter (gets validation automatically)
        """
        self.version = value  # Delegates to property setter
        return self

    def getVlanPriority(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for vlanPriority.
        
        Returns:
            The vlanPriority value
        
        Note:
            Delegates to vlan_priority property (CODING_RULE_V2_00017)
        """
        return self.vlan_priority  # Delegates to property

    def setVlanPriority(self, value: "PositiveInteger") -> "IEEE1722TpConnection":
        """
        AUTOSAR-compliant setter for vlanPriority with method chaining.
        
        Args:
            value: The vlanPriority to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to vlan_priority property setter (gets validation automatically)
        """
        self.vlan_priority = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_destination_mac(self, value: Optional["MacAddressString"]) -> "IEEE1722TpConnection":
        """
        Set destinationMac and return self for chaining.
        
        Args:
            value: The destinationMac to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_destination_mac("value")
        """
        self.destination_mac = value  # Use property setter (gets validation)
        return self

    def with_mac_address(self, value: Optional["MacAddressString"]) -> "IEEE1722TpConnection":
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

    def with_pdu(self, value: Optional[RefType]) -> "IEEE1722TpConnection":
        """
        Set pdu and return self for chaining.
        
        Args:
            value: The pdu to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_pdu("value")
        """
        self.pdu = value  # Use property setter (gets validation)
        return self

    def with_unique_stream_id(self, value: Optional["PositiveInteger"]) -> "IEEE1722TpConnection":
        """
        Set uniqueStreamId and return self for chaining.
        
        Args:
            value: The uniqueStreamId to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_unique_stream_id("value")
        """
        self.unique_stream_id = value  # Use property setter (gets validation)
        return self

    def with_version(self, value: Optional["PositiveInteger"]) -> "IEEE1722TpConnection":
        """
        Set version and return self for chaining.
        
        Args:
            value: The version to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_version("value")
        """
        self.version = value  # Use property setter (gets validation)
        return self

    def with_vlan_priority(self, value: Optional["PositiveInteger"]) -> "IEEE1722TpConnection":
        """
        Set vlanPriority and return self for chaining.
        
        Args:
            value: The vlanPriority to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_vlan_priority("value")
        """
        self.vlan_priority = value  # Use property setter (gets validation)
        return self