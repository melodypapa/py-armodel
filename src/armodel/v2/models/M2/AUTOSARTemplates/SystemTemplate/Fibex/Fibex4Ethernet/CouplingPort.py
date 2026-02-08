from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class CouplingPort(Identifiable):
    """
    A CouplingPort is used to connect a CouplingElement with an EcuInstance or
    two CouplingElements with each other via a CouplingPortConnection.
    Optionally, the CouplingPort may also have a reference to a
    macMulticastGroup and a defaultVLAN.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::CouplingPort

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 109, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies the connection negotiation of the CouplingPort.
        self._connection: Optional["EthernetConnection"] = None

    @property
    def connection(self) -> Optional["EthernetConnection"]:
        """Get connection (Pythonic accessor)."""
        return self._connection

    @connection.setter
    def connection(self, value: Optional["EthernetConnection"]) -> None:
        """
        Set connection with validation.

        Args:
            value: The connection to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._connection = None
            return

        if not isinstance(value, EthernetConnection):
            raise TypeError(
                f"connection must be EthernetConnection or None, got {type(value).__name__}"
            )
        self._connection = value
        # Defines the role this CouplingPort takes in the context of CouplingElement.
        self._couplingPort: Optional["CouplingPortRoleEnum"] = None

    @property
    def coupling_port(self) -> Optional["CouplingPortRoleEnum"]:
        """Get couplingPort (Pythonic accessor)."""
        return self._couplingPort

    @coupling_port.setter
    def coupling_port(self, value: Optional["CouplingPortRoleEnum"]) -> None:
        """
        Set couplingPort with validation.

        Args:
            value: The couplingPort to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._couplingPort = None
            return

        if not isinstance(value, CouplingPortRoleEnum):
            raise TypeError(
                f"couplingPort must be CouplingPortRoleEnum or None, got {type(value).__name__}"
            )
        self._couplingPort = value
        # The vLanIdentifier of the referenced VLAN is the (port VLAN ID).
        # A Port VLAN ID is a default that is assigned to an access CouplingPort to
                # VLAN segment to which this port is if a CouplingPort has not been any VLAN
                # memberships, the virtual VLAN ID (pvid) becomes the default VLAN the ports
                # connection.
        # is added for incoming untagged the port (ingress tagging).
        # For outgoing this identifier, the tag is removed at the untagging, depending
                # on the Vlan.
        self._defaultVlan: Optional["EthernetPhysical"] = None

    @property
    def default_vlan(self) -> Optional["EthernetPhysical"]:
        """Get defaultVlan (Pythonic accessor)."""
        return self._defaultVlan

    @default_vlan.setter
    def default_vlan(self, value: Optional["EthernetPhysical"]) -> None:
        """
        Set defaultVlan with validation.

        Args:
            value: The defaultVlan to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._defaultVlan = None
            return

        if not isinstance(value, EthernetPhysical):
            raise TypeError(
                f"defaultVlan must be EthernetPhysical or None, got {type(value).__name__}"
            )
        self._defaultVlan = value
        # Specifies the mac layer type of the CouplingPort.
        self._macLayerTypeEnum: Optional["EthernetMacLayerType"] = None

    @property
    def mac_layer_type_enum(self) -> Optional["EthernetMacLayerType"]:
        """Get macLayerTypeEnum (Pythonic accessor)."""
        return self._macLayerTypeEnum

    @mac_layer_type_enum.setter
    def mac_layer_type_enum(self, value: Optional["EthernetMacLayerType"]) -> None:
        """
        Set macLayerTypeEnum with validation.

        Args:
            value: The macLayerTypeEnum to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._macLayerTypeEnum = None
            return

        if not isinstance(value, EthernetMacLayerType):
            raise TypeError(
                f"macLayerTypeEnum must be EthernetMacLayerType or None, got {type(value).__name__}"
            )
        self._macLayerTypeEnum = value
        # Assigns a set of MAC-Multicast-Addresses which are via this CouplingPort.
        # This is a static further addresses may be learned.
        self._macMulticast: List[RefType] = []

    @property
    def mac_multicast(self) -> List[RefType]:
        """Get macMulticast (Pythonic accessor)."""
        return self._macMulticast
        # Properties to configure MACsec (Media access control the MKA (MACsec Key
        # Agreement) for the.
        self._macSecProps: List["MacSecProps"] = []

    @property
    def mac_sec_props(self) -> List["MacSecProps"]:
        """Get macSecProps (Pythonic accessor)."""
        return self._macSecProps
        # Specifies the physical layer type of the CouplingPort.
        self._physicalLayer: Optional["EthernetPhysicalLayer"] = None

    @property
    def physical_layer(self) -> Optional["EthernetPhysicalLayer"]:
        """Get physicalLayer (Pythonic accessor)."""
        return self._physicalLayer

    @physical_layer.setter
    def physical_layer(self, value: Optional["EthernetPhysicalLayer"]) -> None:
        """
        Set physicalLayer with validation.

        Args:
            value: The physicalLayer to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._physicalLayer = None
            return

        if not isinstance(value, EthernetPhysicalLayer):
            raise TypeError(
                f"physicalLayer must be EthernetPhysicalLayer or None, got {type(value).__name__}"
            )
        self._physicalLayer = value
        # Optional properties for configuration of PLCA (Physical Avoidance) in case
        # 10-BASE-T1S used and PLCA is enabled on the Coupling.
        self._plcaProps: Optional["PlcaProps"] = None

    @property
    def plca_props(self) -> Optional["PlcaProps"]:
        """Get plcaProps (Pythonic accessor)."""
        return self._plcaProps

    @plca_props.setter
    def plca_props(self, value: Optional["PlcaProps"]) -> None:
        """
        Set plcaProps with validation.

        Args:
            value: The plcaProps to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._plcaProps = None
            return

        if not isinstance(value, PlcaProps):
            raise TypeError(
                f"plcaProps must be PlcaProps or None, got {type(value).__name__}"
            )
        self._plcaProps = value
        # Reference to the partial networks this CouplingPort.
        self._pncMapping: List[RefType] = []

    @property
    def pnc_mapping(self) -> List[RefType]:
        """Get pncMapping (Pythonic accessor)."""
        return self._pncMapping
        # Defines the handling of frames at the ingress port.
        self._receiveActivity: Optional["EthernetSwitchVlan"] = None

    @property
    def receive_activity(self) -> Optional["EthernetSwitchVlan"]:
        """Get receiveActivity (Pythonic accessor)."""
        return self._receiveActivity

    @receive_activity.setter
    def receive_activity(self, value: Optional["EthernetSwitchVlan"]) -> None:
        """
        Set receiveActivity with validation.

        Args:
            value: The receiveActivity to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._receiveActivity = None
            return

        if not isinstance(value, EthernetSwitchVlan):
            raise TypeError(
                f"receiveActivity must be EthernetSwitchVlan or None, got {type(value).__name__}"
            )
        self._receiveActivity = value
        # Messages of VLANs that are defined here can be via the CouplingPort.
        self._vlan: List["VlanMembership"] = []

    @property
    def vlan(self) -> List["VlanMembership"]:
        """Get vlan (Pythonic accessor)."""
        return self._vlan
        # All incoming messages at this CouplingPort shall be with this VLAN Id.
        # This tagging is performed the message already has a VLAN tag untagged, an
                # existing VLAN tag will be overwritten.
        # is XOR with CoupligPort.
        # defaultVlan.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._vlanModifier: Optional["EthernetPhysical"] = None

    @property
    def vlan_modifier(self) -> Optional["EthernetPhysical"]:
        """Get vlanModifier (Pythonic accessor)."""
        return self._vlanModifier

    @vlan_modifier.setter
    def vlan_modifier(self, value: Optional["EthernetPhysical"]) -> None:
        """
        Set vlanModifier with validation.

        Args:
            value: The vlanModifier to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._vlanModifier = None
            return

        if not isinstance(value, EthernetPhysical):
            raise TypeError(
                f"vlanModifier must be EthernetPhysical or None, got {type(value).__name__}"
            )
        self._vlanModifier = value
        # Optional reference to EthernetWakeupSleepOnDataline Config.
        self._wakeupSleep: Optional["EthernetWakeupSleep"] = None

    @property
    def wakeup_sleep(self) -> Optional["EthernetWakeupSleep"]:
        """Get wakeupSleep (Pythonic accessor)."""
        return self._wakeupSleep

    @wakeup_sleep.setter
    def wakeup_sleep(self, value: Optional["EthernetWakeupSleep"]) -> None:
        """
        Set wakeupSleep with validation.

        Args:
            value: The wakeupSleep to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._wakeupSleep = None
            return

        if not isinstance(value, EthernetWakeupSleep):
            raise TypeError(
                f"wakeupSleep must be EthernetWakeupSleep or None, got {type(value).__name__}"
            )
        self._wakeupSleep = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getConnection(self) -> "EthernetConnection":
        """
        AUTOSAR-compliant getter for connection.

        Returns:
            The connection value

        Note:
            Delegates to connection property (CODING_RULE_V2_00017)
        """
        return self.connection  # Delegates to property

    def setConnection(self, value: "EthernetConnection") -> "CouplingPort":
        """
        AUTOSAR-compliant setter for connection with method chaining.

        Args:
            value: The connection to set

        Returns:
            self for method chaining

        Note:
            Delegates to connection property setter (gets validation automatically)
        """
        self.connection = value  # Delegates to property setter
        return self

    def getCouplingPort(self) -> "CouplingPortRoleEnum":
        """
        AUTOSAR-compliant getter for couplingPort.

        Returns:
            The couplingPort value

        Note:
            Delegates to coupling_port property (CODING_RULE_V2_00017)
        """
        return self.coupling_port  # Delegates to property

    def setCouplingPort(self, value: "CouplingPortRoleEnum") -> "CouplingPort":
        """
        AUTOSAR-compliant setter for couplingPort with method chaining.

        Args:
            value: The couplingPort to set

        Returns:
            self for method chaining

        Note:
            Delegates to coupling_port property setter (gets validation automatically)
        """
        self.coupling_port = value  # Delegates to property setter
        return self

    def getDefaultVlan(self) -> "EthernetPhysical":
        """
        AUTOSAR-compliant getter for defaultVlan.

        Returns:
            The defaultVlan value

        Note:
            Delegates to default_vlan property (CODING_RULE_V2_00017)
        """
        return self.default_vlan  # Delegates to property

    def setDefaultVlan(self, value: "EthernetPhysical") -> "CouplingPort":
        """
        AUTOSAR-compliant setter for defaultVlan with method chaining.

        Args:
            value: The defaultVlan to set

        Returns:
            self for method chaining

        Note:
            Delegates to default_vlan property setter (gets validation automatically)
        """
        self.default_vlan = value  # Delegates to property setter
        return self

    def getMacLayerTypeEnum(self) -> "EthernetMacLayerType":
        """
        AUTOSAR-compliant getter for macLayerTypeEnum.

        Returns:
            The macLayerTypeEnum value

        Note:
            Delegates to mac_layer_type_enum property (CODING_RULE_V2_00017)
        """
        return self.mac_layer_type_enum  # Delegates to property

    def setMacLayerTypeEnum(self, value: "EthernetMacLayerType") -> "CouplingPort":
        """
        AUTOSAR-compliant setter for macLayerTypeEnum with method chaining.

        Args:
            value: The macLayerTypeEnum to set

        Returns:
            self for method chaining

        Note:
            Delegates to mac_layer_type_enum property setter (gets validation automatically)
        """
        self.mac_layer_type_enum = value  # Delegates to property setter
        return self

    def getMacMulticast(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for macMulticast.

        Returns:
            The macMulticast value

        Note:
            Delegates to mac_multicast property (CODING_RULE_V2_00017)
        """
        return self.mac_multicast  # Delegates to property

    def getMacSecProps(self) -> List["MacSecProps"]:
        """
        AUTOSAR-compliant getter for macSecProps.

        Returns:
            The macSecProps value

        Note:
            Delegates to mac_sec_props property (CODING_RULE_V2_00017)
        """
        return self.mac_sec_props  # Delegates to property

    def getPhysicalLayer(self) -> "EthernetPhysicalLayer":
        """
        AUTOSAR-compliant getter for physicalLayer.

        Returns:
            The physicalLayer value

        Note:
            Delegates to physical_layer property (CODING_RULE_V2_00017)
        """
        return self.physical_layer  # Delegates to property

    def setPhysicalLayer(self, value: "EthernetPhysicalLayer") -> "CouplingPort":
        """
        AUTOSAR-compliant setter for physicalLayer with method chaining.

        Args:
            value: The physicalLayer to set

        Returns:
            self for method chaining

        Note:
            Delegates to physical_layer property setter (gets validation automatically)
        """
        self.physical_layer = value  # Delegates to property setter
        return self

    def getPlcaProps(self) -> "PlcaProps":
        """
        AUTOSAR-compliant getter for plcaProps.

        Returns:
            The plcaProps value

        Note:
            Delegates to plca_props property (CODING_RULE_V2_00017)
        """
        return self.plca_props  # Delegates to property

    def setPlcaProps(self, value: "PlcaProps") -> "CouplingPort":
        """
        AUTOSAR-compliant setter for plcaProps with method chaining.

        Args:
            value: The plcaProps to set

        Returns:
            self for method chaining

        Note:
            Delegates to plca_props property setter (gets validation automatically)
        """
        self.plca_props = value  # Delegates to property setter
        return self

    def getPncMapping(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for pncMapping.

        Returns:
            The pncMapping value

        Note:
            Delegates to pnc_mapping property (CODING_RULE_V2_00017)
        """
        return self.pnc_mapping  # Delegates to property

    def getReceiveActivity(self) -> "EthernetSwitchVlan":
        """
        AUTOSAR-compliant getter for receiveActivity.

        Returns:
            The receiveActivity value

        Note:
            Delegates to receive_activity property (CODING_RULE_V2_00017)
        """
        return self.receive_activity  # Delegates to property

    def setReceiveActivity(self, value: "EthernetSwitchVlan") -> "CouplingPort":
        """
        AUTOSAR-compliant setter for receiveActivity with method chaining.

        Args:
            value: The receiveActivity to set

        Returns:
            self for method chaining

        Note:
            Delegates to receive_activity property setter (gets validation automatically)
        """
        self.receive_activity = value  # Delegates to property setter
        return self

    def getVlan(self) -> List["VlanMembership"]:
        """
        AUTOSAR-compliant getter for vlan.

        Returns:
            The vlan value

        Note:
            Delegates to vlan property (CODING_RULE_V2_00017)
        """
        return self.vlan  # Delegates to property

    def getVlanModifier(self) -> "EthernetPhysical":
        """
        AUTOSAR-compliant getter for vlanModifier.

        Returns:
            The vlanModifier value

        Note:
            Delegates to vlan_modifier property (CODING_RULE_V2_00017)
        """
        return self.vlan_modifier  # Delegates to property

    def setVlanModifier(self, value: "EthernetPhysical") -> "CouplingPort":
        """
        AUTOSAR-compliant setter for vlanModifier with method chaining.

        Args:
            value: The vlanModifier to set

        Returns:
            self for method chaining

        Note:
            Delegates to vlan_modifier property setter (gets validation automatically)
        """
        self.vlan_modifier = value  # Delegates to property setter
        return self

    def getWakeupSleep(self) -> "EthernetWakeupSleep":
        """
        AUTOSAR-compliant getter for wakeupSleep.

        Returns:
            The wakeupSleep value

        Note:
            Delegates to wakeup_sleep property (CODING_RULE_V2_00017)
        """
        return self.wakeup_sleep  # Delegates to property

    def setWakeupSleep(self, value: "EthernetWakeupSleep") -> "CouplingPort":
        """
        AUTOSAR-compliant setter for wakeupSleep with method chaining.

        Args:
            value: The wakeupSleep to set

        Returns:
            self for method chaining

        Note:
            Delegates to wakeup_sleep property setter (gets validation automatically)
        """
        self.wakeup_sleep = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_connection(self, value: Optional["EthernetConnection"]) -> "CouplingPort":
        """
        Set connection and return self for chaining.

        Args:
            value: The connection to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_connection("value")
        """
        self.connection = value  # Use property setter (gets validation)
        return self

    def with_coupling_port(self, value: Optional["CouplingPortRoleEnum"]) -> "CouplingPort":
        """
        Set couplingPort and return self for chaining.

        Args:
            value: The couplingPort to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_coupling_port("value")
        """
        self.coupling_port = value  # Use property setter (gets validation)
        return self

    def with_default_vlan(self, value: Optional["EthernetPhysical"]) -> "CouplingPort":
        """
        Set defaultVlan and return self for chaining.

        Args:
            value: The defaultVlan to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_default_vlan("value")
        """
        self.default_vlan = value  # Use property setter (gets validation)
        return self

    def with_mac_layer_type_enum(self, value: Optional["EthernetMacLayerType"]) -> "CouplingPort":
        """
        Set macLayerTypeEnum and return self for chaining.

        Args:
            value: The macLayerTypeEnum to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mac_layer_type_enum("value")
        """
        self.mac_layer_type_enum = value  # Use property setter (gets validation)
        return self

    def with_physical_layer(self, value: Optional["EthernetPhysicalLayer"]) -> "CouplingPort":
        """
        Set physicalLayer and return self for chaining.

        Args:
            value: The physicalLayer to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_physical_layer("value")
        """
        self.physical_layer = value  # Use property setter (gets validation)
        return self

    def with_plca_props(self, value: Optional["PlcaProps"]) -> "CouplingPort":
        """
        Set plcaProps and return self for chaining.

        Args:
            value: The plcaProps to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_plca_props("value")
        """
        self.plca_props = value  # Use property setter (gets validation)
        return self

    def with_receive_activity(self, value: Optional["EthernetSwitchVlan"]) -> "CouplingPort":
        """
        Set receiveActivity and return self for chaining.

        Args:
            value: The receiveActivity to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_receive_activity("value")
        """
        self.receive_activity = value  # Use property setter (gets validation)
        return self

    def with_vlan_modifier(self, value: Optional["EthernetPhysical"]) -> "CouplingPort":
        """
        Set vlanModifier and return self for chaining.

        Args:
            value: The vlanModifier to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_vlan_modifier("value")
        """
        self.vlan_modifier = value  # Use property setter (gets validation)
        return self

    def with_wakeup_sleep(self, value: Optional["EthernetWakeupSleep"]) -> "CouplingPort":
        """
        Set wakeupSleep and return self for chaining.

        Args:
            value: The wakeupSleep to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_wakeup_sleep("value")
        """
        self.wakeup_sleep = value  # Use property setter (gets validation)
        return self
