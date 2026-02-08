from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection import (
    TpConnection,
)


class FlexrayTpConnection(TpConnection):
    """
    A connection identifies the sender and the receiver of this particular
    communication. The FlexRayTp module routes a Pdu through this connection. In
    a System Description the references to the PduPools are mandatory. In an ECU
    Extract these references can be optional: On unicast connections these
    references are always mandatory. On multicast the txPduPool is mandatory on
    the sender side. The rxPduPool is mandatory on the receiver side. On Gateway
    ECUs both references are mandatory.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 594, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies whether the connection requires a bandwidth or not.
        self._bandwidth: Optional["Boolean"] = None

    @property
    def bandwidth(self) -> Optional["Boolean"]:
        """Get bandwidth (Pythonic accessor)."""
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, value: Optional["Boolean"]) -> None:
        """
        Set bandwidth with validation.

        Args:
            value: The bandwidth to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._bandwidth = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"bandwidth must be Boolean or None, got {type(value).__name__}"
            )
        self._bandwidth = value
        # Reference to the IPdu that is segmented by the Transport.
        self._directTpSdu: Optional["IPdu"] = None

    @property
    def direct_tp_sdu(self) -> Optional["IPdu"]:
        """Get directTpSdu (Pythonic accessor)."""
        return self._directTpSdu

    @direct_tp_sdu.setter
    def direct_tp_sdu(self, value: Optional["IPdu"]) -> None:
        """
        Set directTpSdu with validation.

        Args:
            value: The directTpSdu to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._directTpSdu = None
            return

        if not isinstance(value, IPdu):
            raise TypeError(
                f"directTpSdu must be IPdu or None, got {type(value).__name__}"
            )
        self._directTpSdu = value
        # TP address for 1:n connections.
        self._multicast: Optional["TpAddress"] = None

    @property
    def multicast(self) -> Optional["TpAddress"]:
        """Get multicast (Pythonic accessor)."""
        return self._multicast

    @multicast.setter
    def multicast(self, value: Optional["TpAddress"]) -> None:
        """
        Set multicast with validation.

        Args:
            value: The multicast to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._multicast = None
            return

        if not isinstance(value, TpAddress):
            raise TypeError(
                f"multicast must be TpAddress or None, got {type(value).__name__}"
            )
        self._multicast = value
        # The target of the TP connection.
        self._receiver: List["FlexrayTpNode"] = []

    @property
    def receiver(self) -> List["FlexrayTpNode"]:
        """Get receiver (Pythonic accessor)."""
        return self._receiver
        # Reference to the IPdu that is segmented by the Transport support of both
        # sending and receiving is used, references the IPdu used for the direction.
        self._reversedTpSdu: Optional["IPdu"] = None

    @property
    def reversed_tp_sdu(self) -> Optional["IPdu"]:
        """Get reversedTpSdu (Pythonic accessor)."""
        return self._reversedTpSdu

    @reversed_tp_sdu.setter
    def reversed_tp_sdu(self, value: Optional["IPdu"]) -> None:
        """
        Set reversedTpSdu with validation.

        Args:
            value: The reversedTpSdu to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._reversedTpSdu = None
            return

        if not isinstance(value, IPdu):
            raise TypeError(
                f"reversedTpSdu must be IPdu or None, got {type(value).__name__}"
            )
        self._reversedTpSdu = value
        # A connection has a reference to a set of NPdus (FrTpRx are defined for
        # receiving data via this constraint is valid only for the System In case this
        # connection is applied to the rxPduPool holds the actually received case this
        # connection is applied to the receiver holds the actually sent NPdus.
        self._rxPduPool: Optional["FlexrayTpPduPool"] = None

    @property
    def rx_pdu_pool(self) -> Optional["FlexrayTpPduPool"]:
        """Get rxPduPool (Pythonic accessor)."""
        return self._rxPduPool

    @rx_pdu_pool.setter
    def rx_pdu_pool(self, value: Optional["FlexrayTpPduPool"]) -> None:
        """
        Set rxPduPool with validation.

        Args:
            value: The rxPduPool to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rxPduPool = None
            return

        if not isinstance(value, FlexrayTpPduPool):
            raise TypeError(
                f"rxPduPool must be FlexrayTpPduPool or None, got {type(value).__name__}"
            )
        self._rxPduPool = value
        # Reference to the connection control.
        self._tpConnection: Optional["FlexrayTpConnection"] = None

    @property
    def tp_connection(self) -> Optional["FlexrayTpConnection"]:
        """Get tpConnection (Pythonic accessor)."""
        return self._tpConnection

    @tp_connection.setter
    def tp_connection(self, value: Optional["FlexrayTpConnection"]) -> None:
        """
        Set tpConnection with validation.

        Args:
            value: The tpConnection to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tpConnection = None
            return

        if not isinstance(value, FlexrayTpConnection):
            raise TypeError(
                f"tpConnection must be FlexrayTpConnection or None, got {type(value).__name__}"
            )
        self._tpConnection = value
        # The source of the TP connection.
        self._transmitter: Optional["FlexrayTpNode"] = None

    @property
    def transmitter(self) -> Optional["FlexrayTpNode"]:
        """Get transmitter (Pythonic accessor)."""
        return self._transmitter

    @transmitter.setter
    def transmitter(self, value: Optional["FlexrayTpNode"]) -> None:
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

        if not isinstance(value, FlexrayTpNode):
            raise TypeError(
                f"transmitter must be FlexrayTpNode or None, got {type(value).__name__}"
            )
        self._transmitter = value
        # A connection has a reference to a set of NPdus (FrTpTx are defined for
        # sending data via this constraint is valid only for the System In case this
        # connection is applied to the txPduPool holds the actually sent case this
        # connection is applied to the receiver holds the actually received NPdus.
        self._txPduPool: Optional["FlexrayTpPduPool"] = None

    @property
    def tx_pdu_pool(self) -> Optional["FlexrayTpPduPool"]:
        """Get txPduPool (Pythonic accessor)."""
        return self._txPduPool

    @tx_pdu_pool.setter
    def tx_pdu_pool(self, value: Optional["FlexrayTpPduPool"]) -> None:
        """
        Set txPduPool with validation.

        Args:
            value: The txPduPool to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._txPduPool = None
            return

        if not isinstance(value, FlexrayTpPduPool):
            raise TypeError(
                f"txPduPool must be FlexrayTpPduPool or None, got {type(value).__name__}"
            )
        self._txPduPool = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBandwidth(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for bandwidth.

        Returns:
            The bandwidth value

        Note:
            Delegates to bandwidth property (CODING_RULE_V2_00017)
        """
        return self.bandwidth  # Delegates to property

    def setBandwidth(self, value: "Boolean") -> "FlexrayTpConnection":
        """
        AUTOSAR-compliant setter for bandwidth with method chaining.

        Args:
            value: The bandwidth to set

        Returns:
            self for method chaining

        Note:
            Delegates to bandwidth property setter (gets validation automatically)
        """
        self.bandwidth = value  # Delegates to property setter
        return self

    def getDirectTpSdu(self) -> "IPdu":
        """
        AUTOSAR-compliant getter for directTpSdu.

        Returns:
            The directTpSdu value

        Note:
            Delegates to direct_tp_sdu property (CODING_RULE_V2_00017)
        """
        return self.direct_tp_sdu  # Delegates to property

    def setDirectTpSdu(self, value: "IPdu") -> "FlexrayTpConnection":
        """
        AUTOSAR-compliant setter for directTpSdu with method chaining.

        Args:
            value: The directTpSdu to set

        Returns:
            self for method chaining

        Note:
            Delegates to direct_tp_sdu property setter (gets validation automatically)
        """
        self.direct_tp_sdu = value  # Delegates to property setter
        return self

    def getMulticast(self) -> "TpAddress":
        """
        AUTOSAR-compliant getter for multicast.

        Returns:
            The multicast value

        Note:
            Delegates to multicast property (CODING_RULE_V2_00017)
        """
        return self.multicast  # Delegates to property

    def setMulticast(self, value: "TpAddress") -> "FlexrayTpConnection":
        """
        AUTOSAR-compliant setter for multicast with method chaining.

        Args:
            value: The multicast to set

        Returns:
            self for method chaining

        Note:
            Delegates to multicast property setter (gets validation automatically)
        """
        self.multicast = value  # Delegates to property setter
        return self

    def getReceiver(self) -> List["FlexrayTpNode"]:
        """
        AUTOSAR-compliant getter for receiver.

        Returns:
            The receiver value

        Note:
            Delegates to receiver property (CODING_RULE_V2_00017)
        """
        return self.receiver  # Delegates to property

    def getReversedTpSdu(self) -> "IPdu":
        """
        AUTOSAR-compliant getter for reversedTpSdu.

        Returns:
            The reversedTpSdu value

        Note:
            Delegates to reversed_tp_sdu property (CODING_RULE_V2_00017)
        """
        return self.reversed_tp_sdu  # Delegates to property

    def setReversedTpSdu(self, value: "IPdu") -> "FlexrayTpConnection":
        """
        AUTOSAR-compliant setter for reversedTpSdu with method chaining.

        Args:
            value: The reversedTpSdu to set

        Returns:
            self for method chaining

        Note:
            Delegates to reversed_tp_sdu property setter (gets validation automatically)
        """
        self.reversed_tp_sdu = value  # Delegates to property setter
        return self

    def getRxPduPool(self) -> "FlexrayTpPduPool":
        """
        AUTOSAR-compliant getter for rxPduPool.

        Returns:
            The rxPduPool value

        Note:
            Delegates to rx_pdu_pool property (CODING_RULE_V2_00017)
        """
        return self.rx_pdu_pool  # Delegates to property

    def setRxPduPool(self, value: "FlexrayTpPduPool") -> "FlexrayTpConnection":
        """
        AUTOSAR-compliant setter for rxPduPool with method chaining.

        Args:
            value: The rxPduPool to set

        Returns:
            self for method chaining

        Note:
            Delegates to rx_pdu_pool property setter (gets validation automatically)
        """
        self.rx_pdu_pool = value  # Delegates to property setter
        return self

    def getTpConnection(self) -> "FlexrayTpConnection":
        """
        AUTOSAR-compliant getter for tpConnection.

        Returns:
            The tpConnection value

        Note:
            Delegates to tp_connection property (CODING_RULE_V2_00017)
        """
        return self.tp_connection  # Delegates to property

    def setTpConnection(self, value: "FlexrayTpConnection") -> "FlexrayTpConnection":
        """
        AUTOSAR-compliant setter for tpConnection with method chaining.

        Args:
            value: The tpConnection to set

        Returns:
            self for method chaining

        Note:
            Delegates to tp_connection property setter (gets validation automatically)
        """
        self.tp_connection = value  # Delegates to property setter
        return self

    def getTransmitter(self) -> "FlexrayTpNode":
        """
        AUTOSAR-compliant getter for transmitter.

        Returns:
            The transmitter value

        Note:
            Delegates to transmitter property (CODING_RULE_V2_00017)
        """
        return self.transmitter  # Delegates to property

    def setTransmitter(self, value: "FlexrayTpNode") -> "FlexrayTpConnection":
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

    def getTxPduPool(self) -> "FlexrayTpPduPool":
        """
        AUTOSAR-compliant getter for txPduPool.

        Returns:
            The txPduPool value

        Note:
            Delegates to tx_pdu_pool property (CODING_RULE_V2_00017)
        """
        return self.tx_pdu_pool  # Delegates to property

    def setTxPduPool(self, value: "FlexrayTpPduPool") -> "FlexrayTpConnection":
        """
        AUTOSAR-compliant setter for txPduPool with method chaining.

        Args:
            value: The txPduPool to set

        Returns:
            self for method chaining

        Note:
            Delegates to tx_pdu_pool property setter (gets validation automatically)
        """
        self.tx_pdu_pool = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bandwidth(self, value: Optional["Boolean"]) -> "FlexrayTpConnection":
        """
        Set bandwidth and return self for chaining.

        Args:
            value: The bandwidth to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bandwidth("value")
        """
        self.bandwidth = value  # Use property setter (gets validation)
        return self

    def with_direct_tp_sdu(self, value: Optional["IPdu"]) -> "FlexrayTpConnection":
        """
        Set directTpSdu and return self for chaining.

        Args:
            value: The directTpSdu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_direct_tp_sdu("value")
        """
        self.direct_tp_sdu = value  # Use property setter (gets validation)
        return self

    def with_multicast(self, value: Optional["TpAddress"]) -> "FlexrayTpConnection":
        """
        Set multicast and return self for chaining.

        Args:
            value: The multicast to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_multicast("value")
        """
        self.multicast = value  # Use property setter (gets validation)
        return self

    def with_reversed_tp_sdu(self, value: Optional["IPdu"]) -> "FlexrayTpConnection":
        """
        Set reversedTpSdu and return self for chaining.

        Args:
            value: The reversedTpSdu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_reversed_tp_sdu("value")
        """
        self.reversed_tp_sdu = value  # Use property setter (gets validation)
        return self

    def with_rx_pdu_pool(self, value: Optional["FlexrayTpPduPool"]) -> "FlexrayTpConnection":
        """
        Set rxPduPool and return self for chaining.

        Args:
            value: The rxPduPool to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rx_pdu_pool("value")
        """
        self.rx_pdu_pool = value  # Use property setter (gets validation)
        return self

    def with_tp_connection(self, value: Optional["FlexrayTpConnection"]) -> "FlexrayTpConnection":
        """
        Set tpConnection and return self for chaining.

        Args:
            value: The tpConnection to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tp_connection("value")
        """
        self.tp_connection = value  # Use property setter (gets validation)
        return self

    def with_transmitter(self, value: Optional["FlexrayTpNode"]) -> "FlexrayTpConnection":
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

    def with_tx_pdu_pool(self, value: Optional["FlexrayTpPduPool"]) -> "FlexrayTpConnection":
        """
        Set txPduPool and return self for chaining.

        Args:
            value: The txPduPool to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tx_pdu_pool("value")
        """
        self.tx_pdu_pool = value  # Use property setter (gets validation)
        return self
