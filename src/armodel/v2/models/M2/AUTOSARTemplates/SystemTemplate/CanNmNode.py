from typing import Optional


class CanNmNode(NmNode):
    """
    CAN specific NM Node attributes.

    Package: M2::AUTOSARTemplates::SystemTemplate::NetworkManagement::CanNmNode

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 684, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies if Nm drops irrelevant NM PDUs.
        # Only NM PDUs with a Partial Network Information = true and containing a
                # Partial Network request ECU trigger the standard RX indication handling keep
                # the ECU awake NM PDU triggers the standard RX indication keeps the ECU awake.
        self._allNmMessages: Optional["Boolean"] = None

    @property
    def all_nm_messages(self) -> Optional["Boolean"]:
        """Get allNmMessages (Pythonic accessor)."""
        return self._allNmMessages

    @all_nm_messages.setter
    def all_nm_messages(self, value: Optional["Boolean"]) -> None:
        """
        Set allNmMessages with validation.

        Args:
            value: The allNmMessages to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._allNmMessages = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"allNmMessages must be Boolean or None, got {type(value).__name__}"
            )
        self._allNmMessages = value
        # If set to true this attribute enables the support of CarWake bit evaluation
        # in received NmPdus.
        self._nmCarWakeUp: Optional["Boolean"] = None

    @property
    def nm_car_wake_up(self) -> Optional["Boolean"]:
        """Get nmCarWakeUp (Pythonic accessor)."""
        return self._nmCarWakeUp

    @nm_car_wake_up.setter
    def nm_car_wake_up(self, value: Optional["Boolean"]) -> None:
        """
        Set nmCarWakeUp with validation.

        Args:
            value: The nmCarWakeUp to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmCarWakeUp = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"nmCarWakeUp must be Boolean or None, got {type(value).__name__}"
            )
        self._nmCarWakeUp = value
        # Node specific time offset in the periodic transmission It determines the
                # start delay of the transmission.
        # seconds.
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
        # Node specific bus cycle time in the periodic transmission with bus load
                # reduction.
        # Specified in seconds.
        self._nmMsg: Optional["TimeValue"] = None

    @property
    def nm_msg(self) -> Optional["TimeValue"]:
        """Get nmMsg (Pythonic accessor)."""
        return self._nmMsg

    @nm_msg.setter
    def nm_msg(self, value: Optional["TimeValue"]) -> None:
        """
        Set nmMsg with validation.

        Args:
            value: The nmMsg to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmMsg = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"nmMsg must be TimeValue or None, got {type(value).__name__}"
            )
        self._nmMsg = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAllNmMessages(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for allNmMessages.

        Returns:
            The allNmMessages value

        Note:
            Delegates to all_nm_messages property (CODING_RULE_V2_00017)
        """
        return self.all_nm_messages  # Delegates to property

    def setAllNmMessages(self, value: "Boolean") -> "CanNmNode":
        """
        AUTOSAR-compliant setter for allNmMessages with method chaining.

        Args:
            value: The allNmMessages to set

        Returns:
            self for method chaining

        Note:
            Delegates to all_nm_messages property setter (gets validation automatically)
        """
        self.all_nm_messages = value  # Delegates to property setter
        return self

    def getNmCarWakeUp(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for nmCarWakeUp.

        Returns:
            The nmCarWakeUp value

        Note:
            Delegates to nm_car_wake_up property (CODING_RULE_V2_00017)
        """
        return self.nm_car_wake_up  # Delegates to property

    def setNmCarWakeUp(self, value: "Boolean") -> "CanNmNode":
        """
        AUTOSAR-compliant setter for nmCarWakeUp with method chaining.

        Args:
            value: The nmCarWakeUp to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_car_wake_up property setter (gets validation automatically)
        """
        self.nm_car_wake_up = value  # Delegates to property setter
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

    def setNmMsgCycle(self, value: "TimeValue") -> "CanNmNode":
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

    def getNmMsg(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for nmMsg.

        Returns:
            The nmMsg value

        Note:
            Delegates to nm_msg property (CODING_RULE_V2_00017)
        """
        return self.nm_msg  # Delegates to property

    def setNmMsg(self, value: "TimeValue") -> "CanNmNode":
        """
        AUTOSAR-compliant setter for nmMsg with method chaining.

        Args:
            value: The nmMsg to set

        Returns:
            self for method chaining

        Note:
            Delegates to nm_msg property setter (gets validation automatically)
        """
        self.nm_msg = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_all_nm_messages(self, value: Optional["Boolean"]) -> "CanNmNode":
        """
        Set allNmMessages and return self for chaining.

        Args:
            value: The allNmMessages to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_all_nm_messages("value")
        """
        self.all_nm_messages = value  # Use property setter (gets validation)
        return self

    def with_nm_car_wake_up(self, value: Optional["Boolean"]) -> "CanNmNode":
        """
        Set nmCarWakeUp and return self for chaining.

        Args:
            value: The nmCarWakeUp to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_car_wake_up("value")
        """
        self.nm_car_wake_up = value  # Use property setter (gets validation)
        return self

    def with_nm_msg_cycle(self, value: Optional["TimeValue"]) -> "CanNmNode":
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

    def with_nm_msg(self, value: Optional["TimeValue"]) -> "CanNmNode":
        """
        Set nmMsg and return self for chaining.

        Args:
            value: The nmMsg to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_msg("value")
        """
        self.nm_msg = value  # Use property setter (gets validation)
        return self
