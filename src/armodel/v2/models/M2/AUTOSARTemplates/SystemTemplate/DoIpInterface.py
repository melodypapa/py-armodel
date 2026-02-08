from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class DoIpInterface(Identifiable):
    """
    A logical interface over which the DoIP Node is able to communicate via DoIP
    independently from other existing DoIpInterfaces.

    Package: M2::AUTOSARTemplates::SystemTemplate::DoIP

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 551, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines the timeout in seconds for waiting response to an
                # Alive Check request before the is considered to be disconnected.
        # Represents of ISO 13400-2:2012.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._aliveCheck: Optional["TimeValue"] = None

    @property
    def alive_check(self) -> Optional["TimeValue"]:
        """Get aliveCheck (Pythonic accessor)."""
        return self._aliveCheck

    @alive_check.setter
    def alive_check(self, value: Optional["TimeValue"]) -> None:
        """
        Set aliveCheck with validation.

        Args:
            value: The aliveCheck to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._aliveCheck = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"aliveCheck must be TimeValue or None, got {type(value).__name__}"
            )
        self._aliveCheck = value
        # Configuration of DoIPChannels available in an DoIp Each DoIPChannel describes
        # a connection doIpSourceAddress and a doIpTargetAddress exchange of DcmIPdus
        # between the PduR and DoIP channel is constituted by the set of all DoIp via
        # which the configured Ecu or receives SDUs that are sharing the diagnosis
        # address and tester address.
        self._doipChannel: Optional["DoIpTpConfig"] = None

    @property
    def doip_channel(self) -> Optional["DoIpTpConfig"]:
        """Get doipChannel (Pythonic accessor)."""
        return self._doipChannel

    @doip_channel.setter
    def doip_channel(self, value: Optional["DoIpTpConfig"]) -> None:
        """
        Set doipChannel with validation.

        Args:
            value: The doipChannel to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._doipChannel = None
            return

        if not isinstance(value, DoIpTpConfig):
            raise TypeError(
                f"doipChannel must be DoIpTpConfig or None, got {type(value).__name__}"
            )
        self._doipChannel = value
        # DoIP Connections in the DoIpInterface that define the Do Pdus that are sent
        # and received via SoAd over TCP or.
        self._doipConnection: List["SocketConnection"] = []

    @property
    def doip_connection(self) -> List["SocketConnection"]:
        """Get doipConnection (Pythonic accessor)."""
        return self._doipConnection
        # Collection of DoIpRoutingActivation possibilities defined the DoIpInterface.
        self._doIpRouting: List["DoIpRoutingActivation"] = []

    @property
    def do_ip_routing(self) -> List["DoIpRoutingActivation"]:
        """Get doIpRouting (Pythonic accessor)."""
        return self._doIpRouting
        # This attribute defines the timeout in seconds for maximum of a TCP socket
                # connection before the DoIP close the according socket connection.
        # T_TCP_General_Inactivity of ISO.
        self._generalInactivity: Optional["TimeValue"] = None

    @property
    def general_inactivity(self) -> Optional["TimeValue"]:
        """Get generalInactivity (Pythonic accessor)."""
        return self._generalInactivity

    @general_inactivity.setter
    def general_inactivity(self, value: Optional["TimeValue"]) -> None:
        """
        Set generalInactivity with validation.

        Args:
            value: The generalInactivity to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._generalInactivity = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"generalInactivity must be TimeValue or None, got {type(value).__name__}"
            )
        self._generalInactivity = value
        # This attribute defines the timeout in seconds used for inactivity of a
                # connected TCP socket connection socket connection.
        # Represents parameter ISO 13400-2:2012.
        self._initialInactivity: Optional["TimeValue"] = None

    @property
    def initial_inactivity(self) -> Optional["TimeValue"]:
        """Get initialInactivity (Pythonic accessor)."""
        return self._initialInactivity

    @initial_inactivity.setter
    def initial_inactivity(self, value: Optional["TimeValue"]) -> None:
        """
        Set initialInactivity with validation.

        Args:
            value: The initialInactivity to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._initialInactivity = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"initialInactivity must be TimeValue or None, got {type(value).__name__}"
            )
        self._initialInactivity = value
        # This attribute defines the waiting time in seconds for first vehicle
                # announcement message after IP assignment.
        # Represents parameter A_DoIP_ ISO 13400-2:2012.
        self._initialVehicle: Optional["TimeValue"] = None

    @property
    def initial_vehicle(self) -> Optional["TimeValue"]:
        """Get initialVehicle (Pythonic accessor)."""
        return self._initialVehicle

    @initial_vehicle.setter
    def initial_vehicle(self, value: Optional["TimeValue"]) -> None:
        """
        Set initialVehicle with validation.

        Args:
            value: The initialVehicle to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._initialVehicle = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"initialVehicle must be TimeValue or None, got {type(value).__name__}"
            )
        self._initialVehicle = value
        # This attribute defines whether the network interface is started "on-demand"
        # when an activation line is always available.
        self._isActivationLine: Optional["Boolean"] = None

    @property
    def is_activation_line(self) -> Optional["Boolean"]:
        """Get isActivationLine (Pythonic accessor)."""
        return self._isActivationLine

    @is_activation_line.setter
    def is_activation_line(self, value: Optional["Boolean"]) -> None:
        """
        Set isActivationLine with validation.

        Args:
            value: The isActivationLine to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._isActivationLine = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"isActivationLine must be Boolean or None, got {type(value).__name__}"
            )
        self._isActivationLine = value
        # Maximum amount of tester connections that shall be at one time before alive
        # check is performed.
        self._maxTester: Optional["PositiveInteger"] = None

    @property
    def max_tester(self) -> Optional["PositiveInteger"]:
        """Get maxTester (Pythonic accessor)."""
        return self._maxTester

    @max_tester.setter
    def max_tester(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxTester with validation.

        Args:
            value: The maxTester to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxTester = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"maxTester must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._maxTester = value
        # DoIP Connections in the DoIpInterface that define the Do Pdus that are sent
        # and received via SoAd over TCP or.
        self._socket: List["StaticSocketConnection"] = []

    @property
    def socket(self) -> List["StaticSocketConnection"]:
        """Get socket (Pythonic accessor)."""
        return self._socket
        # This attribute defines whether a configured EID at vehicle response/vehicle
                # announcement is used or address.
        # TRUE: Use MAC Address instead of Vehicle identification/announcement.
        # FALSE: Use for vehicle identification/announcement.
        self._useMacAddress: Optional["Boolean"] = None

    @property
    def use_mac_address(self) -> Optional["Boolean"]:
        """Get useMacAddress (Pythonic accessor)."""
        return self._useMacAddress

    @use_mac_address.setter
    def use_mac_address(self, value: Optional["Boolean"]) -> None:
        """
        Set useMacAddress with validation.

        Args:
            value: The useMacAddress to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._useMacAddress = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"useMacAddress must be Boolean or None, got {type(value).__name__}"
            )
        self._useMacAddress = value
        # This attribute defines if the optional VIN/GID status is used additionally in
        # the vehicle.
        self._useVehicle: Optional["Boolean"] = None

    @property
    def use_vehicle(self) -> Optional["Boolean"]:
        """Get useVehicle (Pythonic accessor)."""
        return self._useVehicle

    @use_vehicle.setter
    def use_vehicle(self, value: Optional["Boolean"]) -> None:
        """
        Set useVehicle with validation.

        Args:
            value: The useVehicle to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._useVehicle = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"useVehicle must be Boolean or None, got {type(value).__name__}"
            )
        self._useVehicle = value
        # This attribute defines the waiting time in seconds for subsequent vehicle
                # announcement messages.
        # parameter A_DoIP_Announce_Interval of.
        self._vehicle: Optional["TimeValue"] = None

    @property
    def vehicle(self) -> Optional["TimeValue"]:
        """Get vehicle (Pythonic accessor)."""
        return self._vehicle

    @vehicle.setter
    def vehicle(self, value: Optional["TimeValue"]) -> None:
        """
        Set vehicle with validation.

        Args:
            value: The vehicle to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._vehicle = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"vehicle must be TimeValue or None, got {type(value).__name__}"
            )
        self._vehicle = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAliveCheck(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for aliveCheck.

        Returns:
            The aliveCheck value

        Note:
            Delegates to alive_check property (CODING_RULE_V2_00017)
        """
        return self.alive_check  # Delegates to property

    def setAliveCheck(self, value: "TimeValue") -> "DoIpInterface":
        """
        AUTOSAR-compliant setter for aliveCheck with method chaining.

        Args:
            value: The aliveCheck to set

        Returns:
            self for method chaining

        Note:
            Delegates to alive_check property setter (gets validation automatically)
        """
        self.alive_check = value  # Delegates to property setter
        return self

    def getDoipChannel(self) -> "DoIpTpConfig":
        """
        AUTOSAR-compliant getter for doipChannel.

        Returns:
            The doipChannel value

        Note:
            Delegates to doip_channel property (CODING_RULE_V2_00017)
        """
        return self.doip_channel  # Delegates to property

    def setDoipChannel(self, value: "DoIpTpConfig") -> "DoIpInterface":
        """
        AUTOSAR-compliant setter for doipChannel with method chaining.

        Args:
            value: The doipChannel to set

        Returns:
            self for method chaining

        Note:
            Delegates to doip_channel property setter (gets validation automatically)
        """
        self.doip_channel = value  # Delegates to property setter
        return self

    def getDoipConnection(self) -> List["SocketConnection"]:
        """
        AUTOSAR-compliant getter for doipConnection.

        Returns:
            The doipConnection value

        Note:
            Delegates to doip_connection property (CODING_RULE_V2_00017)
        """
        return self.doip_connection  # Delegates to property

    def getDoIpRouting(self) -> List["DoIpRoutingActivation"]:
        """
        AUTOSAR-compliant getter for doIpRouting.

        Returns:
            The doIpRouting value

        Note:
            Delegates to do_ip_routing property (CODING_RULE_V2_00017)
        """
        return self.do_ip_routing  # Delegates to property

    def getGeneralInactivity(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for generalInactivity.

        Returns:
            The generalInactivity value

        Note:
            Delegates to general_inactivity property (CODING_RULE_V2_00017)
        """
        return self.general_inactivity  # Delegates to property

    def setGeneralInactivity(self, value: "TimeValue") -> "DoIpInterface":
        """
        AUTOSAR-compliant setter for generalInactivity with method chaining.

        Args:
            value: The generalInactivity to set

        Returns:
            self for method chaining

        Note:
            Delegates to general_inactivity property setter (gets validation automatically)
        """
        self.general_inactivity = value  # Delegates to property setter
        return self

    def getInitialInactivity(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for initialInactivity.

        Returns:
            The initialInactivity value

        Note:
            Delegates to initial_inactivity property (CODING_RULE_V2_00017)
        """
        return self.initial_inactivity  # Delegates to property

    def setInitialInactivity(self, value: "TimeValue") -> "DoIpInterface":
        """
        AUTOSAR-compliant setter for initialInactivity with method chaining.

        Args:
            value: The initialInactivity to set

        Returns:
            self for method chaining

        Note:
            Delegates to initial_inactivity property setter (gets validation automatically)
        """
        self.initial_inactivity = value  # Delegates to property setter
        return self

    def getInitialVehicle(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for initialVehicle.

        Returns:
            The initialVehicle value

        Note:
            Delegates to initial_vehicle property (CODING_RULE_V2_00017)
        """
        return self.initial_vehicle  # Delegates to property

    def setInitialVehicle(self, value: "TimeValue") -> "DoIpInterface":
        """
        AUTOSAR-compliant setter for initialVehicle with method chaining.

        Args:
            value: The initialVehicle to set

        Returns:
            self for method chaining

        Note:
            Delegates to initial_vehicle property setter (gets validation automatically)
        """
        self.initial_vehicle = value  # Delegates to property setter
        return self

    def getIsActivationLine(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for isActivationLine.

        Returns:
            The isActivationLine value

        Note:
            Delegates to is_activation_line property (CODING_RULE_V2_00017)
        """
        return self.is_activation_line  # Delegates to property

    def setIsActivationLine(self, value: "Boolean") -> "DoIpInterface":
        """
        AUTOSAR-compliant setter for isActivationLine with method chaining.

        Args:
            value: The isActivationLine to set

        Returns:
            self for method chaining

        Note:
            Delegates to is_activation_line property setter (gets validation automatically)
        """
        self.is_activation_line = value  # Delegates to property setter
        return self

    def getMaxTester(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxTester.

        Returns:
            The maxTester value

        Note:
            Delegates to max_tester property (CODING_RULE_V2_00017)
        """
        return self.max_tester  # Delegates to property

    def setMaxTester(self, value: "PositiveInteger") -> "DoIpInterface":
        """
        AUTOSAR-compliant setter for maxTester with method chaining.

        Args:
            value: The maxTester to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_tester property setter (gets validation automatically)
        """
        self.max_tester = value  # Delegates to property setter
        return self

    def getSocket(self) -> List["StaticSocketConnection"]:
        """
        AUTOSAR-compliant getter for socket.

        Returns:
            The socket value

        Note:
            Delegates to socket property (CODING_RULE_V2_00017)
        """
        return self.socket  # Delegates to property

    def getUseMacAddress(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for useMacAddress.

        Returns:
            The useMacAddress value

        Note:
            Delegates to use_mac_address property (CODING_RULE_V2_00017)
        """
        return self.use_mac_address  # Delegates to property

    def setUseMacAddress(self, value: "Boolean") -> "DoIpInterface":
        """
        AUTOSAR-compliant setter for useMacAddress with method chaining.

        Args:
            value: The useMacAddress to set

        Returns:
            self for method chaining

        Note:
            Delegates to use_mac_address property setter (gets validation automatically)
        """
        self.use_mac_address = value  # Delegates to property setter
        return self

    def getUseVehicle(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for useVehicle.

        Returns:
            The useVehicle value

        Note:
            Delegates to use_vehicle property (CODING_RULE_V2_00017)
        """
        return self.use_vehicle  # Delegates to property

    def setUseVehicle(self, value: "Boolean") -> "DoIpInterface":
        """
        AUTOSAR-compliant setter for useVehicle with method chaining.

        Args:
            value: The useVehicle to set

        Returns:
            self for method chaining

        Note:
            Delegates to use_vehicle property setter (gets validation automatically)
        """
        self.use_vehicle = value  # Delegates to property setter
        return self

    def getVehicle(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for vehicle.

        Returns:
            The vehicle value

        Note:
            Delegates to vehicle property (CODING_RULE_V2_00017)
        """
        return self.vehicle  # Delegates to property

    def setVehicle(self, value: "TimeValue") -> "DoIpInterface":
        """
        AUTOSAR-compliant setter for vehicle with method chaining.

        Args:
            value: The vehicle to set

        Returns:
            self for method chaining

        Note:
            Delegates to vehicle property setter (gets validation automatically)
        """
        self.vehicle = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_alive_check(self, value: Optional["TimeValue"]) -> "DoIpInterface":
        """
        Set aliveCheck and return self for chaining.

        Args:
            value: The aliveCheck to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_alive_check("value")
        """
        self.alive_check = value  # Use property setter (gets validation)
        return self

    def with_doip_channel(self, value: Optional["DoIpTpConfig"]) -> "DoIpInterface":
        """
        Set doipChannel and return self for chaining.

        Args:
            value: The doipChannel to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_doip_channel("value")
        """
        self.doip_channel = value  # Use property setter (gets validation)
        return self

    def with_general_inactivity(self, value: Optional["TimeValue"]) -> "DoIpInterface":
        """
        Set generalInactivity and return self for chaining.

        Args:
            value: The generalInactivity to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_general_inactivity("value")
        """
        self.general_inactivity = value  # Use property setter (gets validation)
        return self

    def with_initial_inactivity(self, value: Optional["TimeValue"]) -> "DoIpInterface":
        """
        Set initialInactivity and return self for chaining.

        Args:
            value: The initialInactivity to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_initial_inactivity("value")
        """
        self.initial_inactivity = value  # Use property setter (gets validation)
        return self

    def with_initial_vehicle(self, value: Optional["TimeValue"]) -> "DoIpInterface":
        """
        Set initialVehicle and return self for chaining.

        Args:
            value: The initialVehicle to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_initial_vehicle("value")
        """
        self.initial_vehicle = value  # Use property setter (gets validation)
        return self

    def with_is_activation_line(self, value: Optional["Boolean"]) -> "DoIpInterface":
        """
        Set isActivationLine and return self for chaining.

        Args:
            value: The isActivationLine to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_is_activation_line("value")
        """
        self.is_activation_line = value  # Use property setter (gets validation)
        return self

    def with_max_tester(self, value: Optional["PositiveInteger"]) -> "DoIpInterface":
        """
        Set maxTester and return self for chaining.

        Args:
            value: The maxTester to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_tester("value")
        """
        self.max_tester = value  # Use property setter (gets validation)
        return self

    def with_use_mac_address(self, value: Optional["Boolean"]) -> "DoIpInterface":
        """
        Set useMacAddress and return self for chaining.

        Args:
            value: The useMacAddress to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_use_mac_address("value")
        """
        self.use_mac_address = value  # Use property setter (gets validation)
        return self

    def with_use_vehicle(self, value: Optional["Boolean"]) -> "DoIpInterface":
        """
        Set useVehicle and return self for chaining.

        Args:
            value: The useVehicle to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_use_vehicle("value")
        """
        self.use_vehicle = value  # Use property setter (gets validation)
        return self

    def with_vehicle(self, value: Optional["TimeValue"]) -> "DoIpInterface":
        """
        Set vehicle and return self for chaining.

        Args:
            value: The vehicle to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_vehicle("value")
        """
        self.vehicle = value  # Use property setter (gets validation)
        return self
