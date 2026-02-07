from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class EthGlobalTimeDomainProps(AbstractGlobalTimeDomainProps):
    """
    Enables the definition of Ethernet Global Time specific properties.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::GlobalTime::ETH::EthGlobalTimeDomainProps
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 867, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the fields of the message which shall be taken for CRC calculation
        # and verification.
        self._crcFlags: Optional["EthTSynCrcFlags"] = None

    @property
    def crc_flags(self) -> Optional["EthTSynCrcFlags"]:
        """Get crcFlags (Pythonic accessor)."""
        return self._crcFlags

    @crc_flags.setter
    def crc_flags(self, value: Optional["EthTSynCrcFlags"]) -> None:
        """
        Set crcFlags with validation.
        
        Args:
            value: The crcFlags to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._crcFlags = None
            return

        if not isinstance(value, EthTSynCrcFlags):
            raise TypeError(
                f"crcFlags must be EthTSynCrcFlags or None, got {type(value).__name__}"
            )
        self._crcFlags = value
        # Defines the MAC multicast address the Ethernet time messages are communicated
        # on.
        self._destination: Optional["MacAddressString"] = None

    @property
    def destination(self) -> Optional["MacAddressString"]:
        """Get destination (Pythonic accessor)."""
        return self._destination

    @destination.setter
    def destination(self, value: Optional["MacAddressString"]) -> None:
        """
        Set destination with validation.
        
        Args:
            value: The destination to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._destination = None
            return

        if not isinstance(value, MacAddressString):
            raise TypeError(
                f"destination must be MacAddressString or None, got {type(value).__name__}"
            )
        self._destination = value
        self._fupDataIDList: "PositiveInteger" = None

    @property
    def fup_data_id_list(self) -> "PositiveInteger":
        """Get fupDataIDList (Pythonic accessor)."""
        return self._fupDataIDList

    @fup_data_id_list.setter
    def fup_data_id_list(self, value: "PositiveInteger") -> None:
        """
        Set fupDataIDList with validation.
        
        Args:
            value: The fupDataIDList to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"fupDataIDList must be PositiveInteger, got {type(value).__name__}"
            )
        self._fupDataIDList = value
        # Collection of CouplingPorts which are managed in the scope of this Ethernet
        # GlobalTimeDomain.
        self._managed: List["EthGlobalTime"] = []

    @property
    def managed(self) -> List["EthGlobalTime"]:
        """Get managed (Pythonic accessor)."""
        return self._managed
        # Defines the compliance of the Ethernet time sync messages to specific
        # standards.
        self._message: Optional["EthGlobalTimeMessage"] = None

    @property
    def message(self) -> Optional["EthGlobalTimeMessage"]:
        """Get message (Pythonic accessor)."""
        return self._message

    @message.setter
    def message(self, value: Optional["EthGlobalTimeMessage"]) -> None:
        """
        Set message with validation.
        
        Args:
            value: The message to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._message = None
            return

        if not isinstance(value, EthGlobalTimeMessage):
            raise TypeError(
                f"message must be EthGlobalTimeMessage or None, got {type(value).__name__}"
            )
        self._message = value
        # Defines which VLAN priority shall be assigned to a time in case the message
        # is sent using a VLAN.
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

    def getCrcFlags(self) -> "EthTSynCrcFlags":
        """
        AUTOSAR-compliant getter for crcFlags.
        
        Returns:
            The crcFlags value
        
        Note:
            Delegates to crc_flags property (CODING_RULE_V2_00017)
        """
        return self.crc_flags  # Delegates to property

    def setCrcFlags(self, value: "EthTSynCrcFlags") -> "EthGlobalTimeDomainProps":
        """
        AUTOSAR-compliant setter for crcFlags with method chaining.
        
        Args:
            value: The crcFlags to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to crc_flags property setter (gets validation automatically)
        """
        self.crc_flags = value  # Delegates to property setter
        return self

    def getDestination(self) -> "MacAddressString":
        """
        AUTOSAR-compliant getter for destination.
        
        Returns:
            The destination value
        
        Note:
            Delegates to destination property (CODING_RULE_V2_00017)
        """
        return self.destination  # Delegates to property

    def setDestination(self, value: "MacAddressString") -> "EthGlobalTimeDomainProps":
        """
        AUTOSAR-compliant setter for destination with method chaining.
        
        Args:
            value: The destination to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to destination property setter (gets validation automatically)
        """
        self.destination = value  # Delegates to property setter
        return self

    def getFupDataIDList(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for fupDataIDList.
        
        Returns:
            The fupDataIDList value
        
        Note:
            Delegates to fup_data_id_list property (CODING_RULE_V2_00017)
        """
        return self.fup_data_id_list  # Delegates to property

    def setFupDataIDList(self, value: "PositiveInteger") -> "EthGlobalTimeDomainProps":
        """
        AUTOSAR-compliant setter for fupDataIDList with method chaining.
        
        Args:
            value: The fupDataIDList to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to fup_data_id_list property setter (gets validation automatically)
        """
        self.fup_data_id_list = value  # Delegates to property setter
        return self

    def getManaged(self) -> List["EthGlobalTime"]:
        """
        AUTOSAR-compliant getter for managed.
        
        Returns:
            The managed value
        
        Note:
            Delegates to managed property (CODING_RULE_V2_00017)
        """
        return self.managed  # Delegates to property

    def getMessage(self) -> "EthGlobalTimeMessage":
        """
        AUTOSAR-compliant getter for message.
        
        Returns:
            The message value
        
        Note:
            Delegates to message property (CODING_RULE_V2_00017)
        """
        return self.message  # Delegates to property

    def setMessage(self, value: "EthGlobalTimeMessage") -> "EthGlobalTimeDomainProps":
        """
        AUTOSAR-compliant setter for message with method chaining.
        
        Args:
            value: The message to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to message property setter (gets validation automatically)
        """
        self.message = value  # Delegates to property setter
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

    def setVlanPriority(self, value: "PositiveInteger") -> "EthGlobalTimeDomainProps":
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

    def with_crc_flags(self, value: Optional["EthTSynCrcFlags"]) -> "EthGlobalTimeDomainProps":
        """
        Set crcFlags and return self for chaining.
        
        Args:
            value: The crcFlags to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_crc_flags("value")
        """
        self.crc_flags = value  # Use property setter (gets validation)
        return self

    def with_destination(self, value: Optional["MacAddressString"]) -> "EthGlobalTimeDomainProps":
        """
        Set destination and return self for chaining.
        
        Args:
            value: The destination to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_destination("value")
        """
        self.destination = value  # Use property setter (gets validation)
        return self

    def with_fup_data_id_list(self, value: "PositiveInteger") -> "EthGlobalTimeDomainProps":
        """
        Set fupDataIDList and return self for chaining.
        
        Args:
            value: The fupDataIDList to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_fup_data_id_list("value")
        """
        self.fup_data_id_list = value  # Use property setter (gets validation)
        return self

    def with_message(self, value: Optional["EthGlobalTimeMessage"]) -> "EthGlobalTimeDomainProps":
        """
        Set message and return self for chaining.
        
        Args:
            value: The message to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_message("value")
        """
        self.message = value  # Use property setter (gets validation)
        return self

    def with_vlan_priority(self, value: Optional["PositiveInteger"]) -> "EthGlobalTimeDomainProps":
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