from typing import Optional


class UdpNmCluster(NmCluster):
    """
    Udp specific NmCluster attributes

    Package: M2::AUTOSARTemplates::SystemTemplate::NetworkManagement::UdpNmCluster

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 687, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the position of the control bit vector within the Nm position).
        # If this attribute is not configured, the Vector is not used.
        self._nmCbvPosition: Optional["Integer"] = None

    @property
    def nm_cbv_position(self) -> Optional["Integer"]:
        """Get nmCbvPosition (Pythonic accessor)."""
        return self._nmCbvPosition

    @nm_cbv_position.setter
    def nm_cbv_position(self, value: Optional["Integer"]) -> None:
        """
        Set nmCbvPosition with validation.

        Args:
            value: The nmCbvPosition to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmCbvPosition = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"nmCbvPosition must be Integer or None, got {type(value).__name__}"
            )
        self._nmCbvPosition = value
        # Defines the number of immediate NmPdus which shall be If the value is zero no
                # immediate NmPdus transmitted.
        # The cycle time of immediate NmPdus is nmImmediateNmCycleTime.
        self._nmImmediate: Optional["PositiveInteger"] = None

    @property
    def nm_immediate(self) -> Optional["PositiveInteger"]:
        """Get nmImmediate (Pythonic accessor)."""
        return self._nmImmediate

    @nm_immediate.setter
    def nm_immediate(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set nmImmediate with validation.

        Args:
            value: The nmImmediate to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmImmediate = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"nmImmediate must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._nmImmediate = value
        # Timeout of a NmPdu in seconds.
        # It determines how long NM shall wait with notification of transmission
                # failure errors occur on the bus.
        self._nmMessage: Optional["TimeValue"] = None

    @property
    def nm_message(self) -> Optional["TimeValue"]:
        """Get nmMessage (Pythonic accessor)."""
        return self._nmMessage

    @nm_message.setter
    def nm_message(self, value: Optional["TimeValue"]) -> None:
        """
        Set nmMessage with validation.

        Args:
            value: The nmMessage to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmMessage = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"nmMessage must be TimeValue or None, got {type(value).__name__}"
            )
        self._nmMessage = value
        # Period of a NmPdu in seconds.
        # It determines the periodic in the periodic transmission mode with bus load is
                # the basis for transmit scheduling in the mode without bus load reduction.
        self._nmMsgCycle: Optional["TimeValue"] = None

    @property
    def nm_msg_cycle(self) -> Optional["TimeValue"]:
        """Get nmMsgCycle (Pythonic accessor)."""
        return self._nmMsgCycle

    @nm_msg_cycle.setter
    def nm_msg_cycle(self, value: Optional["TimeValue"]) -> None:
        """
        Set nmMsgCycle with validation.

        Args:
            value: The nmMsgCycle to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmMsgCycle = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"nmMsgCycle must be TimeValue or None, got {type(value).__name__}"
            )
        self._nmMsgCycle = value
        # Network Timeout for NmPdus in seconds.
        # It denotes the how long the UdpNm shall stay in the Network Mode into Prepare
                # Bus-Sleep Mode shall take.
        self._nmNetwork: Optional["TimeValue"] = None

    @property
    def nm_network(self) -> Optional["TimeValue"]:
        """Get nmNetwork (Pythonic accessor)."""
        return self._nmNetwork

    @nm_network.setter
    def nm_network(self, value: Optional["TimeValue"]) -> None:
        """
        Set nmNetwork with validation.

        Args:
            value: The nmNetwork to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmNetwork = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"nmNetwork must be TimeValue or None, got {type(value).__name__}"
            )
        self._nmNetwork = value
        # Defines the byte position of the source node identifier NmPdu.
        # If this attribute is not configured, the is not used.
        self._nmNidPosition: Optional["Integer"] = None

    @property
    def nm_nid_position(self) -> Optional["Integer"]:
        """Get nmNidPosition (Pythonic accessor)."""
        return self._nmNidPosition

    @nm_nid_position.setter
    def nm_nid_position(self, value: Optional["Integer"]) -> None:
        """
        Set nmNidPosition with validation.

        Args:
            value: The nmNidPosition to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmNidPosition = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"nmNidPosition must be Integer or None, got {type(value).__name__}"
            )
        self._nmNidPosition = value
        # Timeout for Remote Sleep Indication in seconds.
        # It the time how long it shall take to recognize that all nodes are ready to
                # sleep.
        self._nmRemote: Optional["TimeValue"] = None

    @property
    def nm_remote(self) -> Optional["TimeValue"]:
        """Get nmRemote (Pythonic accessor)."""
        return self._nmRemote

    @nm_remote.setter
    def nm_remote(self, value: Optional["TimeValue"]) -> None:
        """
        Set nmRemote with validation.

        Args:
            value: The nmRemote to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmRemote = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"nmRemote must be TimeValue or None, got {type(value).__name__}"
            )
        self._nmRemote = value
        # Timeout for Repeat Message State in seconds.
        # Defines time how long the NM shall stay in the Repeat.
        self._nmRepeat: Optional["TimeValue"] = None

    @property
    def nm_repeat(self) -> Optional["TimeValue"]:
        """Get nmRepeat (Pythonic accessor)."""
        return self._nmRepeat

    @nm_repeat.setter
    def nm_repeat(self, value: Optional["TimeValue"]) -> None:
        """
        Set nmRepeat with validation.

        Args:
            value: The nmRepeat to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmRepeat = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"nmRepeat must be TimeValue or None, got {type(value).__name__}"
            )
        self._nmRepeat = value
        # Timeout for bus calm down phase in seconds.
        # It denotes time how long the CanNm shall stay in the Prepare before
                # transition into Bus-Sleep Mode place.
        self._nmWaitBus: Optional["TimeValue"] = None

    @property
    def nm_wait_bus(self) -> Optional["TimeValue"]:
        """Get nmWaitBus (Pythonic accessor)."""
        return self._nmWaitBus

    @nm_wait_bus.setter
    def nm_wait_bus(self, value: Optional["TimeValue"]) -> None:
        """
        Set nmWaitBus with validation.

        Args:
            value: The nmWaitBus to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmWaitBus = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"nmWaitBus must be TimeValue or None, got {type(value).__name__}"
            )
        self._nmWaitBus = value
        # Reference to the vlan (represented by the Ethernet this UdpNmCluster shall
        # apply to.
        self._vlan: Optional["EthernetPhysical"] = None

    @property
    def vlan(self) -> Optional["EthernetPhysical"]:
        """Get vlan (Pythonic accessor)."""
        return self._vlan

    @vlan.setter
    def vlan(self, value: Optional["EthernetPhysical"]) -> None:
        """
        Set vlan with validation.

        Args:
            value: The vlan to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._vlan = None
            return

        if not isinstance(value, EthernetPhysical):
            raise TypeError(
                f"vlan must be EthernetPhysical or None, got {type(value).__name__}"
            )
        self._vlan = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getNmCbvPosition(self) -> "Integer":
        """
        AUTOSAR-compliant getter for nmCbvPosition.

        Returns:
            The nmCbvPosition value

        Note:
            Delegates to nm_cbv_position property (CODING_RULE_V2_00017)
        """
        return self.nm_cbv_position  # Delegates to property

    def setNmCbvPosition(self, value: "Integer") -> "UdpNmCluster":
        """
        AUTOSAR-compliant setter for nmCbvPosition with method chaining.

        Args:
            value: The nmCbvPosition to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_cbv_position property setter (gets validation automatically)
        """
        self.nm_cbv_position = value  # Delegates to property setter
        return self

    def getNmImmediate(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for nmImmediate.

        Returns:
            The nmImmediate value

        Note:
            Delegates to nm_immediate property (CODING_RULE_V2_00017)
        """
        return self.nm_immediate  # Delegates to property

    def setNmImmediate(self, value: "PositiveInteger") -> "UdpNmCluster":
        """
        AUTOSAR-compliant setter for nmImmediate with method chaining.

        Args:
            value: The nmImmediate to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_immediate property setter (gets validation automatically)
        """
        self.nm_immediate = value  # Delegates to property setter
        return self

    def getNmMessage(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for nmMessage.

        Returns:
            The nmMessage value

        Note:
            Delegates to nm_message property (CODING_RULE_V2_00017)
        """
        return self.nm_message  # Delegates to property

    def setNmMessage(self, value: "TimeValue") -> "UdpNmCluster":
        """
        AUTOSAR-compliant setter for nmMessage with method chaining.

        Args:
            value: The nmMessage to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_message property setter (gets validation automatically)
        """
        self.nm_message = value  # Delegates to property setter
        return self

    def getNmMsgCycle(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for nmMsgCycle.

        Returns:
            The nmMsgCycle value

        Note:
            Delegates to nm_msg_cycle property (CODING_RULE_V2_00017)
        """
        return self.nm_msg_cycle  # Delegates to property

    def setNmMsgCycle(self, value: "TimeValue") -> "UdpNmCluster":
        """
        AUTOSAR-compliant setter for nmMsgCycle with method chaining.

        Args:
            value: The nmMsgCycle to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_msg_cycle property setter (gets validation automatically)
        """
        self.nm_msg_cycle = value  # Delegates to property setter
        return self

    def getNmNetwork(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for nmNetwork.

        Returns:
            The nmNetwork value

        Note:
            Delegates to nm_network property (CODING_RULE_V2_00017)
        """
        return self.nm_network  # Delegates to property

    def setNmNetwork(self, value: "TimeValue") -> "UdpNmCluster":
        """
        AUTOSAR-compliant setter for nmNetwork with method chaining.

        Args:
            value: The nmNetwork to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_network property setter (gets validation automatically)
        """
        self.nm_network = value  # Delegates to property setter
        return self

    def getNmNidPosition(self) -> "Integer":
        """
        AUTOSAR-compliant getter for nmNidPosition.

        Returns:
            The nmNidPosition value

        Note:
            Delegates to nm_nid_position property (CODING_RULE_V2_00017)
        """
        return self.nm_nid_position  # Delegates to property

    def setNmNidPosition(self, value: "Integer") -> "UdpNmCluster":
        """
        AUTOSAR-compliant setter for nmNidPosition with method chaining.

        Args:
            value: The nmNidPosition to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_nid_position property setter (gets validation automatically)
        """
        self.nm_nid_position = value  # Delegates to property setter
        return self

    def getNmRemote(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for nmRemote.

        Returns:
            The nmRemote value

        Note:
            Delegates to nm_remote property (CODING_RULE_V2_00017)
        """
        return self.nm_remote  # Delegates to property

    def setNmRemote(self, value: "TimeValue") -> "UdpNmCluster":
        """
        AUTOSAR-compliant setter for nmRemote with method chaining.

        Args:
            value: The nmRemote to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_remote property setter (gets validation automatically)
        """
        self.nm_remote = value  # Delegates to property setter
        return self

    def getNmRepeat(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for nmRepeat.

        Returns:
            The nmRepeat value

        Note:
            Delegates to nm_repeat property (CODING_RULE_V2_00017)
        """
        return self.nm_repeat  # Delegates to property

    def setNmRepeat(self, value: "TimeValue") -> "UdpNmCluster":
        """
        AUTOSAR-compliant setter for nmRepeat with method chaining.

        Args:
            value: The nmRepeat to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_repeat property setter (gets validation automatically)
        """
        self.nm_repeat = value  # Delegates to property setter
        return self

    def getNmWaitBus(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for nmWaitBus.

        Returns:
            The nmWaitBus value

        Note:
            Delegates to nm_wait_bus property (CODING_RULE_V2_00017)
        """
        return self.nm_wait_bus  # Delegates to property

    def setNmWaitBus(self, value: "TimeValue") -> "UdpNmCluster":
        """
        AUTOSAR-compliant setter for nmWaitBus with method chaining.

        Args:
            value: The nmWaitBus to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_wait_bus property setter (gets validation automatically)
        """
        self.nm_wait_bus = value  # Delegates to property setter
        return self

    def getVlan(self) -> "EthernetPhysical":
        """
        AUTOSAR-compliant getter for vlan.

        Returns:
            The vlan value

        Note:
            Delegates to vlan property (CODING_RULE_V2_00017)
        """
        return self.vlan  # Delegates to property

    def setVlan(self, value: "EthernetPhysical") -> "UdpNmCluster":
        """
        AUTOSAR-compliant setter for vlan with method chaining.

        Args:
            value: The vlan to set

        Returns:
            self for method chaining

        Note:
            Delegates to vlan property setter (gets validation automatically)
        """
        self.vlan = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_nm_cbv_position(self, value: Optional["Integer"]) -> "UdpNmCluster":
        """
        Set nmCbvPosition and return self for chaining.

        Args:
            value: The nmCbvPosition to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_cbv_position("value")
        """
        self.nm_cbv_position = value  # Use property setter (gets validation)
        return self

    def with_nm_immediate(self, value: Optional["PositiveInteger"]) -> "UdpNmCluster":
        """
        Set nmImmediate and return self for chaining.

        Args:
            value: The nmImmediate to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_immediate("value")
        """
        self.nm_immediate = value  # Use property setter (gets validation)
        return self

    def with_nm_message(self, value: Optional["TimeValue"]) -> "UdpNmCluster":
        """
        Set nmMessage and return self for chaining.

        Args:
            value: The nmMessage to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_message("value")
        """
        self.nm_message = value  # Use property setter (gets validation)
        return self

    def with_nm_msg_cycle(self, value: Optional["TimeValue"]) -> "UdpNmCluster":
        """
        Set nmMsgCycle and return self for chaining.

        Args:
            value: The nmMsgCycle to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_msg_cycle("value")
        """
        self.nm_msg_cycle = value  # Use property setter (gets validation)
        return self

    def with_nm_network(self, value: Optional["TimeValue"]) -> "UdpNmCluster":
        """
        Set nmNetwork and return self for chaining.

        Args:
            value: The nmNetwork to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_network("value")
        """
        self.nm_network = value  # Use property setter (gets validation)
        return self

    def with_nm_nid_position(self, value: Optional["Integer"]) -> "UdpNmCluster":
        """
        Set nmNidPosition and return self for chaining.

        Args:
            value: The nmNidPosition to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_nid_position("value")
        """
        self.nm_nid_position = value  # Use property setter (gets validation)
        return self

    def with_nm_remote(self, value: Optional["TimeValue"]) -> "UdpNmCluster":
        """
        Set nmRemote and return self for chaining.

        Args:
            value: The nmRemote to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_remote("value")
        """
        self.nm_remote = value  # Use property setter (gets validation)
        return self

    def with_nm_repeat(self, value: Optional["TimeValue"]) -> "UdpNmCluster":
        """
        Set nmRepeat and return self for chaining.

        Args:
            value: The nmRepeat to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_repeat("value")
        """
        self.nm_repeat = value  # Use property setter (gets validation)
        return self

    def with_nm_wait_bus(self, value: Optional["TimeValue"]) -> "UdpNmCluster":
        """
        Set nmWaitBus and return self for chaining.

        Args:
            value: The nmWaitBus to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_wait_bus("value")
        """
        self.nm_wait_bus = value  # Use property setter (gets validation)
        return self

    def with_vlan(self, value: Optional["EthernetPhysical"]) -> "UdpNmCluster":
        """
        Set vlan and return self for chaining.

        Args:
            value: The vlan to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_vlan("value")
        """
        self.vlan = value  # Use property setter (gets validation)
        return self
