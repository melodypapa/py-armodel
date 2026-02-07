from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class EthernetCommunicationController(ARObject):
    """
    Ethernet specific communication port attributes.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::EthernetCommunicationController
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 115, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # If the Ethernet frames handled by this Ethernet are to be tunneled through
        # XL, then this reference shall refer to the Abstract aggregates the Can the
        # physical CAN XL channel used for tunneling.
        self._canXlConfig: Optional["AbstractCan"] = None

    @property
    def can_xl_config(self) -> Optional["AbstractCan"]:
        """Get canXlConfig (Pythonic accessor)."""
        return self._canXlConfig

    @can_xl_config.setter
    def can_xl_config(self, value: Optional["AbstractCan"]) -> None:
        """
        Set canXlConfig with validation.
        
        Args:
            value: The canXlConfig to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._canXlConfig = None
            return

        if not isinstance(value, AbstractCan):
            raise TypeError(
                f"canXlConfig must be AbstractCan or None, got {type(value).__name__}"
            )
        self._canXlConfig = value
        # Optional CouplingPort that can be used to connect the a CouplingElement (e.
        # g.
        # a switch).
        self._couplingPort: List["CouplingPort"] = []

    @property
    def coupling_port(self) -> List["CouplingPort"]:
        """Get couplingPort (Pythonic accessor)."""
        return self._couplingPort
        # Specifies the mac layer type of the ethernet controller.
        self._macLayerType: Optional["EthernetMacLayerType"] = None

    @property
    def mac_layer_type(self) -> Optional["EthernetMacLayerType"]:
        """Get macLayerType (Pythonic accessor)."""
        return self._macLayerType

    @mac_layer_type.setter
    def mac_layer_type(self, value: Optional["EthernetMacLayerType"]) -> None:
        """
        Set macLayerType with validation.
        
        Args:
            value: The macLayerType to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._macLayerType = None
            return

        if not isinstance(value, EthernetMacLayerType):
            raise TypeError(
                f"macLayerType must be EthernetMacLayerType or None, got {type(value).__name__}"
            )
        self._macLayerType = value
        # Media Access Control address (MAC address) that identifies each
        # EthernetCommunication the network.
        self._macUnicast: Optional["MacAddressString"] = None

    @property
    def mac_unicast(self) -> Optional["MacAddressString"]:
        """Get macUnicast (Pythonic accessor)."""
        return self._macUnicast

    @mac_unicast.setter
    def mac_unicast(self, value: Optional["MacAddressString"]) -> None:
        """
        Set macUnicast with validation.
        
        Args:
            value: The macUnicast to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._macUnicast = None
            return

        if not isinstance(value, MacAddressString):
            raise TypeError(
                f"macUnicast must be MacAddressString or None, got {type(value).__name__}"
            )
        self._macUnicast = value
        # Determines the maximum transmit buffer length (frame in bytes.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._maximum: Optional["Integer"] = None

    @property
    def maximum(self) -> Optional["Integer"]:
        """Get maximum (Pythonic accessor)."""
        return self._maximum

    @maximum.setter
    def maximum(self, value: Optional["Integer"]) -> None:
        """
        Set maximum with validation.
        
        Args:
            value: The maximum to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maximum = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"maximum must be Integer or None, got {type(value).__name__}"
            )
        self._maximum = value
        # This attribute specifies if the EcuInstance is acting as a communication
                # slave on the connected Physical This is used for EthernetCommunication that
                # use Ethernet hardware which supports sleep on the network (e.
        # g.
        # Open Alliance Ethernet hardware).
        self._slaveActAs: Optional["Boolean"] = None

    @property
    def slave_act_as(self) -> Optional["Boolean"]:
        """Get slaveActAs (Pythonic accessor)."""
        return self._slaveActAs

    @slave_act_as.setter
    def slave_act_as(self, value: Optional["Boolean"]) -> None:
        """
        Set slaveActAs with validation.
        
        Args:
            value: The slaveActAs to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._slaveActAs = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"slaveActAs must be Boolean or None, got {type(value).__name__}"
            )
        self._slaveActAs = value
        # This attribute specifies time when an unexpected link is evaluated as link
        # down and indicated to the communication stack.
        self._slaveQualified: Optional["TimeValue"] = None

    @property
    def slave_qualified(self) -> Optional["TimeValue"]:
        """Get slaveQualified (Pythonic accessor)."""
        return self._slaveQualified

    @slave_qualified.setter
    def slave_qualified(self, value: Optional["TimeValue"]) -> None:
        """
        Set slaveQualified with validation.
        
        Args:
            value: The slaveQualified to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._slaveQualified = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"slaveQualified must be TimeValue or None, got {type(value).__name__}"
            )
        self._slaveQualified = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCanXlConfig(self) -> "AbstractCan":
        """
        AUTOSAR-compliant getter for canXlConfig.
        
        Returns:
            The canXlConfig value
        
        Note:
            Delegates to can_xl_config property (CODING_RULE_V2_00017)
        """
        return self.can_xl_config  # Delegates to property

    def setCanXlConfig(self, value: "AbstractCan") -> "EthernetCommunicationController":
        """
        AUTOSAR-compliant setter for canXlConfig with method chaining.
        
        Args:
            value: The canXlConfig to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to can_xl_config property setter (gets validation automatically)
        """
        self.can_xl_config = value  # Delegates to property setter
        return self

    def getCouplingPort(self) -> List["CouplingPort"]:
        """
        AUTOSAR-compliant getter for couplingPort.
        
        Returns:
            The couplingPort value
        
        Note:
            Delegates to coupling_port property (CODING_RULE_V2_00017)
        """
        return self.coupling_port  # Delegates to property

    def getMacLayerType(self) -> "EthernetMacLayerType":
        """
        AUTOSAR-compliant getter for macLayerType.
        
        Returns:
            The macLayerType value
        
        Note:
            Delegates to mac_layer_type property (CODING_RULE_V2_00017)
        """
        return self.mac_layer_type  # Delegates to property

    def setMacLayerType(self, value: "EthernetMacLayerType") -> "EthernetCommunicationController":
        """
        AUTOSAR-compliant setter for macLayerType with method chaining.
        
        Args:
            value: The macLayerType to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to mac_layer_type property setter (gets validation automatically)
        """
        self.mac_layer_type = value  # Delegates to property setter
        return self

    def getMacUnicast(self) -> "MacAddressString":
        """
        AUTOSAR-compliant getter for macUnicast.
        
        Returns:
            The macUnicast value
        
        Note:
            Delegates to mac_unicast property (CODING_RULE_V2_00017)
        """
        return self.mac_unicast  # Delegates to property

    def setMacUnicast(self, value: "MacAddressString") -> "EthernetCommunicationController":
        """
        AUTOSAR-compliant setter for macUnicast with method chaining.
        
        Args:
            value: The macUnicast to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to mac_unicast property setter (gets validation automatically)
        """
        self.mac_unicast = value  # Delegates to property setter
        return self

    def getMaximum(self) -> "Integer":
        """
        AUTOSAR-compliant getter for maximum.
        
        Returns:
            The maximum value
        
        Note:
            Delegates to maximum property (CODING_RULE_V2_00017)
        """
        return self.maximum  # Delegates to property

    def setMaximum(self, value: "Integer") -> "EthernetCommunicationController":
        """
        AUTOSAR-compliant setter for maximum with method chaining.
        
        Args:
            value: The maximum to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to maximum property setter (gets validation automatically)
        """
        self.maximum = value  # Delegates to property setter
        return self

    def getSlaveActAs(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for slaveActAs.
        
        Returns:
            The slaveActAs value
        
        Note:
            Delegates to slave_act_as property (CODING_RULE_V2_00017)
        """
        return self.slave_act_as  # Delegates to property

    def setSlaveActAs(self, value: "Boolean") -> "EthernetCommunicationController":
        """
        AUTOSAR-compliant setter for slaveActAs with method chaining.
        
        Args:
            value: The slaveActAs to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to slave_act_as property setter (gets validation automatically)
        """
        self.slave_act_as = value  # Delegates to property setter
        return self

    def getSlaveQualified(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for slaveQualified.
        
        Returns:
            The slaveQualified value
        
        Note:
            Delegates to slave_qualified property (CODING_RULE_V2_00017)
        """
        return self.slave_qualified  # Delegates to property

    def setSlaveQualified(self, value: "TimeValue") -> "EthernetCommunicationController":
        """
        AUTOSAR-compliant setter for slaveQualified with method chaining.
        
        Args:
            value: The slaveQualified to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to slave_qualified property setter (gets validation automatically)
        """
        self.slave_qualified = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_can_xl_config(self, value: Optional["AbstractCan"]) -> "EthernetCommunicationController":
        """
        Set canXlConfig and return self for chaining.
        
        Args:
            value: The canXlConfig to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_can_xl_config("value")
        """
        self.can_xl_config = value  # Use property setter (gets validation)
        return self

    def with_mac_layer_type(self, value: Optional["EthernetMacLayerType"]) -> "EthernetCommunicationController":
        """
        Set macLayerType and return self for chaining.
        
        Args:
            value: The macLayerType to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_mac_layer_type("value")
        """
        self.mac_layer_type = value  # Use property setter (gets validation)
        return self

    def with_mac_unicast(self, value: Optional["MacAddressString"]) -> "EthernetCommunicationController":
        """
        Set macUnicast and return self for chaining.
        
        Args:
            value: The macUnicast to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_mac_unicast("value")
        """
        self.mac_unicast = value  # Use property setter (gets validation)
        return self

    def with_maximum(self, value: Optional["Integer"]) -> "EthernetCommunicationController":
        """
        Set maximum and return self for chaining.
        
        Args:
            value: The maximum to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_maximum("value")
        """
        self.maximum = value  # Use property setter (gets validation)
        return self

    def with_slave_act_as(self, value: Optional["Boolean"]) -> "EthernetCommunicationController":
        """
        Set slaveActAs and return self for chaining.
        
        Args:
            value: The slaveActAs to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_slave_act_as("value")
        """
        self.slave_act_as = value  # Use property setter (gets validation)
        return self

    def with_slave_qualified(self, value: Optional["TimeValue"]) -> "EthernetCommunicationController":
        """
        Set slaveQualified and return self for chaining.
        
        Args:
            value: The slaveQualified to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_slave_qualified("value")
        """
        self.slave_qualified = value  # Use property setter (gets validation)
        return self