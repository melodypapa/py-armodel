from typing import List, Optional
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection import TpConnection


class J1939TpConnection(TpConnection):
    """
    A J1939TpConnection represents an internal path for the transmission or
    reception of a Pdu via J1939Tp and describes the sender and the receiver of
    this particular communication. The J1939Tp module routes a Pdu (J1939 PGN)
    through the connection.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::J1939TpConnection

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 624, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # BAM (Broadcast Announce Message) is a broadcast this attribute is set to true
                # broadcast is used.
        # FF is the only broadcast address, there’s to configure it.
        self._broadcast: Optional["Boolean"] = None

    @property
    def broadcast(self) -> Optional["Boolean"]:
        """Get broadcast (Pythonic accessor)."""
        return self._broadcast

    @broadcast.setter
    def broadcast(self, value: Optional["Boolean"]) -> None:
        """
        Set broadcast with validation.

        Args:
            value: The broadcast to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._broadcast = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"broadcast must be Boolean or None, got {type(value).__name__}"
            )
        self._broadcast = value
        # Defines usage of available data for dynamic block size protocol retry is
                # enabled.
        # This attribute percent of available buffer that shall be used.
        self._bufferRatio: Optional["PositiveInteger"] = None

    @property
    def buffer_ratio(self) -> Optional["PositiveInteger"]:
        """Get bufferRatio (Pythonic accessor)."""
        return self._bufferRatio

    @buffer_ratio.setter
    def buffer_ratio(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set bufferRatio with validation.

        Args:
            value: The bufferRatio to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._bufferRatio = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"bufferRatio must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._bufferRatio = value
        # Enable support for Tx/Rx cancellation.
        self._cancellation: Optional["Boolean"] = None

    @property
    def cancellation(self) -> Optional["Boolean"]:
        """Get cancellation (Pythonic accessor)."""
        return self._cancellation

    @cancellation.setter
    def cancellation(self, value: Optional["Boolean"]) -> None:
        """
        Set cancellation with validation.

        Args:
            value: The cancellation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._cancellation = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"cancellation must be Boolean or None, got {type(value).__name__}"
            )
        self._cancellation = value
        # Data Message (TP.
        # DT) used by CMDT and BAM.
        # has a fixed length of 8 bytes.
        self._dataPdu: Optional["NPdu"] = None

    @property
    def data_pdu(self) -> Optional["NPdu"]:
        """Get dataPdu (Pythonic accessor)."""
        return self._dataPdu

    @data_pdu.setter
    def data_pdu(self, value: Optional["NPdu"]) -> None:
        """
        Set dataPdu with validation.

        Args:
            value: The dataPdu to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataPdu = None
            return

        if not isinstance(value, NPdu):
            raise TypeError(
                f"dataPdu must be NPdu or None, got {type(value).__name__}"
            )
        self._dataPdu = value
        # Enable support for dynamic block size calculation.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._dynamicBs: Optional["Boolean"] = None

    @property
    def dynamic_bs(self) -> Optional["Boolean"]:
        """Get dynamicBs (Pythonic accessor)."""
        return self._dynamicBs

    @dynamic_bs.setter
    def dynamic_bs(self, value: Optional["Boolean"]) -> None:
        """
        Set dynamicBs with validation.

        Args:
            value: The dynamicBs to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dynamicBs = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"dynamicBs must be Boolean or None, got {type(value).__name__}"
            )
        self._dynamicBs = value
        # CMDT (Connection Mode Data Transfer) in both one TP.
        # CM (Transport Protocol Command).
        # has a fixed length of 8 bytes.
        # that the role name "flowControlIPdu" is is kept for backward compatibilty
                # reasons.
        self._flowControlPdu: "NPdu" = None

    @property
    def flow_control_pdu(self) -> "NPdu":
        """Get flowControlPdu (Pythonic accessor)."""
        return self._flowControlPdu

    @flow_control_pdu.setter
    def flow_control_pdu(self, value: "NPdu") -> None:
        """
        Set flowControlPdu with validation.

        Args:
            value: The flowControlPdu to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, NPdu):
            raise TypeError(
                f"flowControlPdu must be NPdu, got {type(value).__name__}"
            )
        self._flowControlPdu = value
        # Set maximum block size (number of packets in TP.
        # CM_.
        self._maxBs: Optional["PositiveInteger"] = None

    @property
    def max_bs(self) -> Optional["PositiveInteger"]:
        """Get maxBs (Pythonic accessor)."""
        return self._maxBs

    @max_bs.setter
    def max_bs(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxBs with validation.

        Args:
            value: The maxBs to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxBs = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"maxBs must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._maxBs = value
        # Set maximum for expected block size (maximum number in TP.
        # CM_RTS).
        self._maxExpBs: Optional["PositiveInteger"] = None

    @property
    def max_exp_bs(self) -> Optional["PositiveInteger"]:
        """Get maxExpBs (Pythonic accessor)."""
        return self._maxExpBs

    @max_exp_bs.setter
    def max_exp_bs(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxExpBs with validation.

        Args:
            value: The maxExpBs to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxExpBs = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"maxExpBs must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._maxExpBs = value
        # The target of the TP connection.
        self._receiver: List["J1939TpNode"] = []

    @property
    def receiver(self) -> List["J1939TpNode"]:
        """Get receiver (Pythonic accessor)."""
        return self._receiver
        # Enable support for protocol retry.
        self._retry: Optional["Boolean"] = None

    @property
    def retry(self) -> Optional["Boolean"]:
        """Get retry (Pythonic accessor)."""
        return self._retry

    @retry.setter
    def retry(self, value: Optional["Boolean"]) -> None:
        """
        Set retry with validation.

        Args:
            value: The retry to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._retry = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"retry must be Boolean or None, got {type(value).__name__}"
            )
        self._retry = value
        # J1939 messages (parameter groups, PGs) that can be this connection.
        self._tpPg: List["J1939TpPg"] = []

    @property
    def tp_pg(self) -> List["J1939TpPg"]:
        """Get tpPg (Pythonic accessor)."""
        return self._tpPg
        # The source of the TP connection.
        self._transmitter: Optional["J1939TpNode"] = None

    @property
    def transmitter(self) -> Optional["J1939TpNode"]:
        """Get transmitter (Pythonic accessor)."""
        return self._transmitter

    @transmitter.setter
    def transmitter(self, value: Optional["J1939TpNode"]) -> None:
        """
        Set transmitter with validation.

        Args:
            value: The transmitter to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._transmitter = None
            return

        if not isinstance(value, J1939TpNode):
            raise TypeError(
                f"transmitter must be J1939TpNode or None, got {type(value).__name__}"
            )
        self._transmitter = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBroadcast(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for broadcast.

        Returns:
            The broadcast value

        Note:
            Delegates to broadcast property (CODING_RULE_V2_00017)
        """
        return self.broadcast  # Delegates to property

    def setBroadcast(self, value: "Boolean") -> "J1939TpConnection":
        """
        AUTOSAR-compliant setter for broadcast with method chaining.

        Args:
            value: The broadcast to set

        Returns:
            self for method chaining

        Note:
            Delegates to broadcast property setter (gets validation automatically)
        """
        self.broadcast = value  # Delegates to property setter
        return self

    def getBufferRatio(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for bufferRatio.

        Returns:
            The bufferRatio value

        Note:
            Delegates to buffer_ratio property (CODING_RULE_V2_00017)
        """
        return self.buffer_ratio  # Delegates to property

    def setBufferRatio(self, value: "PositiveInteger") -> "J1939TpConnection":
        """
        AUTOSAR-compliant setter for bufferRatio with method chaining.

        Args:
            value: The bufferRatio to set

        Returns:
            self for method chaining

        Note:
            Delegates to buffer_ratio property setter (gets validation automatically)
        """
        self.buffer_ratio = value  # Delegates to property setter
        return self

    def getCancellation(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for cancellation.

        Returns:
            The cancellation value

        Note:
            Delegates to cancellation property (CODING_RULE_V2_00017)
        """
        return self.cancellation  # Delegates to property

    def setCancellation(self, value: "Boolean") -> "J1939TpConnection":
        """
        AUTOSAR-compliant setter for cancellation with method chaining.

        Args:
            value: The cancellation to set

        Returns:
            self for method chaining

        Note:
            Delegates to cancellation property setter (gets validation automatically)
        """
        self.cancellation = value  # Delegates to property setter
        return self

    def getDataPdu(self) -> "NPdu":
        """
        AUTOSAR-compliant getter for dataPdu.

        Returns:
            The dataPdu value

        Note:
            Delegates to data_pdu property (CODING_RULE_V2_00017)
        """
        return self.data_pdu  # Delegates to property

    def setDataPdu(self, value: "NPdu") -> "J1939TpConnection":
        """
        AUTOSAR-compliant setter for dataPdu with method chaining.

        Args:
            value: The dataPdu to set

        Returns:
            self for method chaining

        Note:
            Delegates to data_pdu property setter (gets validation automatically)
        """
        self.data_pdu = value  # Delegates to property setter
        return self

    def getDynamicBs(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for dynamicBs.

        Returns:
            The dynamicBs value

        Note:
            Delegates to dynamic_bs property (CODING_RULE_V2_00017)
        """
        return self.dynamic_bs  # Delegates to property

    def setDynamicBs(self, value: "Boolean") -> "J1939TpConnection":
        """
        AUTOSAR-compliant setter for dynamicBs with method chaining.

        Args:
            value: The dynamicBs to set

        Returns:
            self for method chaining

        Note:
            Delegates to dynamic_bs property setter (gets validation automatically)
        """
        self.dynamic_bs = value  # Delegates to property setter
        return self

    def getFlowControlPdu(self) -> "NPdu":
        """
        AUTOSAR-compliant getter for flowControlPdu.

        Returns:
            The flowControlPdu value

        Note:
            Delegates to flow_control_pdu property (CODING_RULE_V2_00017)
        """
        return self.flow_control_pdu  # Delegates to property

    def setFlowControlPdu(self, value: "NPdu") -> "J1939TpConnection":
        """
        AUTOSAR-compliant setter for flowControlPdu with method chaining.

        Args:
            value: The flowControlPdu to set

        Returns:
            self for method chaining

        Note:
            Delegates to flow_control_pdu property setter (gets validation automatically)
        """
        self.flow_control_pdu = value  # Delegates to property setter
        return self

    def getMaxBs(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxBs.

        Returns:
            The maxBs value

        Note:
            Delegates to max_bs property (CODING_RULE_V2_00017)
        """
        return self.max_bs  # Delegates to property

    def setMaxBs(self, value: "PositiveInteger") -> "J1939TpConnection":
        """
        AUTOSAR-compliant setter for maxBs with method chaining.

        Args:
            value: The maxBs to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_bs property setter (gets validation automatically)
        """
        self.max_bs = value  # Delegates to property setter
        return self

    def getMaxExpBs(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxExpBs.

        Returns:
            The maxExpBs value

        Note:
            Delegates to max_exp_bs property (CODING_RULE_V2_00017)
        """
        return self.max_exp_bs  # Delegates to property

    def setMaxExpBs(self, value: "PositiveInteger") -> "J1939TpConnection":
        """
        AUTOSAR-compliant setter for maxExpBs with method chaining.

        Args:
            value: The maxExpBs to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_exp_bs property setter (gets validation automatically)
        """
        self.max_exp_bs = value  # Delegates to property setter
        return self

    def getReceiver(self) -> List["J1939TpNode"]:
        """
        AUTOSAR-compliant getter for receiver.

        Returns:
            The receiver value

        Note:
            Delegates to receiver property (CODING_RULE_V2_00017)
        """
        return self.receiver  # Delegates to property

    def getRetry(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for retry.

        Returns:
            The retry value

        Note:
            Delegates to retry property (CODING_RULE_V2_00017)
        """
        return self.retry  # Delegates to property

    def setRetry(self, value: "Boolean") -> "J1939TpConnection":
        """
        AUTOSAR-compliant setter for retry with method chaining.

        Args:
            value: The retry to set

        Returns:
            self for method chaining

        Note:
            Delegates to retry property setter (gets validation automatically)
        """
        self.retry = value  # Delegates to property setter
        return self

    def getTpPg(self) -> List["J1939TpPg"]:
        """
        AUTOSAR-compliant getter for tpPg.

        Returns:
            The tpPg value

        Note:
            Delegates to tp_pg property (CODING_RULE_V2_00017)
        """
        return self.tp_pg  # Delegates to property

    def getTransmitter(self) -> "J1939TpNode":
        """
        AUTOSAR-compliant getter for transmitter.

        Returns:
            The transmitter value

        Note:
            Delegates to transmitter property (CODING_RULE_V2_00017)
        """
        return self.transmitter  # Delegates to property

    def setTransmitter(self, value: "J1939TpNode") -> "J1939TpConnection":
        """
        AUTOSAR-compliant setter for transmitter with method chaining.

        Args:
            value: The transmitter to set

        Returns:
            self for method chaining

        Note:
            Delegates to transmitter property setter (gets validation automatically)
        """
        self.transmitter = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_broadcast(self, value: Optional["Boolean"]) -> "J1939TpConnection":
        """
        Set broadcast and return self for chaining.

        Args:
            value: The broadcast to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_broadcast("value")
        """
        self.broadcast = value  # Use property setter (gets validation)
        return self

    def with_buffer_ratio(self, value: Optional["PositiveInteger"]) -> "J1939TpConnection":
        """
        Set bufferRatio and return self for chaining.

        Args:
            value: The bufferRatio to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_buffer_ratio("value")
        """
        self.buffer_ratio = value  # Use property setter (gets validation)
        return self

    def with_cancellation(self, value: Optional["Boolean"]) -> "J1939TpConnection":
        """
        Set cancellation and return self for chaining.

        Args:
            value: The cancellation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_cancellation("value")
        """
        self.cancellation = value  # Use property setter (gets validation)
        return self

    def with_data_pdu(self, value: Optional["NPdu"]) -> "J1939TpConnection":
        """
        Set dataPdu and return self for chaining.

        Args:
            value: The dataPdu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_pdu("value")
        """
        self.data_pdu = value  # Use property setter (gets validation)
        return self

    def with_dynamic_bs(self, value: Optional["Boolean"]) -> "J1939TpConnection":
        """
        Set dynamicBs and return self for chaining.

        Args:
            value: The dynamicBs to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dynamic_bs("value")
        """
        self.dynamic_bs = value  # Use property setter (gets validation)
        return self

    def with_flow_control_pdu(self, value: "NPdu") -> "J1939TpConnection":
        """
        Set flowControlPdu and return self for chaining.

        Args:
            value: The flowControlPdu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_flow_control_pdu("value")
        """
        self.flow_control_pdu = value  # Use property setter (gets validation)
        return self

    def with_max_bs(self, value: Optional["PositiveInteger"]) -> "J1939TpConnection":
        """
        Set maxBs and return self for chaining.

        Args:
            value: The maxBs to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_bs("value")
        """
        self.max_bs = value  # Use property setter (gets validation)
        return self

    def with_max_exp_bs(self, value: Optional["PositiveInteger"]) -> "J1939TpConnection":
        """
        Set maxExpBs and return self for chaining.

        Args:
            value: The maxExpBs to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_exp_bs("value")
        """
        self.max_exp_bs = value  # Use property setter (gets validation)
        return self

    def with_retry(self, value: Optional["Boolean"]) -> "J1939TpConnection":
        """
        Set retry and return self for chaining.

        Args:
            value: The retry to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_retry("value")
        """
        self.retry = value  # Use property setter (gets validation)
        return self

    def with_transmitter(self, value: Optional["J1939TpNode"]) -> "J1939TpConnection":
        """
        Set transmitter and return self for chaining.

        Args:
            value: The transmitter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_transmitter("value")
        """
        self.transmitter = value  # Use property setter (gets validation)
        return self
