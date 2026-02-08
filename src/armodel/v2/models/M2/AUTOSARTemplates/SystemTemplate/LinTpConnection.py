from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection import (
    TpConnection,
)


class LinTpConnection(TpConnection):
    """
    A LinTP channel represents an internal path for the transmission or
    reception of a Pdu via LinTp and describes the sender and the receiver of
    this particular communication. LinTp supports (per Lin Cluster) the
    configuration of one Rx Tp-SDU and one Tx Tp-SDU per NAD the LinMaster uses
    to address one or more of its Lin Slaves. To support this an arbitrary
    number of LinTp Connections shall be described.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 615, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to an NPdu (Single Frame, First Frame or Frame network protocol
                # data unit (SF N_PDU) sent out by the sending network entity and can by one or
                # multiple receiving network entities.
        # Frame (SF N_PDU) shall be sent out to service data unit that can be
                # transferred via a request to the data link layer.
        # This network unit shall be sent to transfer unsegmented Frame network
                # protocol data unit (FF N_PDU) first network protocol data unit (N_PDU) of a
                # transmitted by a network sending received by a receiving network entity.
        # Frame network protocol data unit (CF segments (N_Data) of the service data
                # data (<MessageData>).
        # All network units (N_PDUs) transmitted by the sending the First Frame network
                # protocol data unit (FF be encoded as Consecutive Frames data units (CF
                # N_PDUs).
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
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
        # Reference to the Flow Control NPdu.
        # Control network protocol data unit (FC N_PDU) by the Flow Control protocol
                # control N_PCI).
        # The Flow Control network unit (FC N_PDU) instructs a sending to start, stop
                # or resume transmission of CF Flow Control network protocol data unit sent by
                # the receiving network layer entity to the layer entity, when ready to receive
                # more correct reception of: Frame network protocol data unit (FF N_PDU) last
                # Consecutive Frame network protocol data unit of a block of Consecutive Frames
                # (CF N_ further Consecutive Frame network protocol data N_PDU) need(s) to be
                # sent.
        self._flowControl: Optional["NPdu"] = None

    @property
    def flow_control(self) -> Optional["NPdu"]:
        """Get flowControl (Pythonic accessor)."""
        return self._flowControl

    @flow_control.setter
    def flow_control(self, value: Optional["NPdu"]) -> None:
        """
        Set flowControl with validation.

        Args:
            value: The flowControl to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._flowControl = None
            return

        if not isinstance(value, NPdu):
            raise TypeError(
                f"flowControl must be NPdu or None, got {type(value).__name__}"
            )
        self._flowControl = value
        # Reference to the IPdu that is segmented by the Transport.
        self._linTpNSdu: Optional["IPdu"] = None

    @property
    def lin_tp_n_sdu(self) -> Optional["IPdu"]:
        """Get linTpNSdu (Pythonic accessor)."""
        return self._linTpNSdu

    @lin_tp_n_sdu.setter
    def lin_tp_n_sdu(self, value: Optional["IPdu"]) -> None:
        """
        Set linTpNSdu with validation.

        Args:
            value: The linTpNSdu to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._linTpNSdu = None
            return

        if not isinstance(value, IPdu):
            raise TypeError(
                f"linTpNSdu must be IPdu or None, got {type(value).__name__}"
            )
        self._linTpNSdu = value
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
        self._receiver: List["LinTpNode"] = []

    @property
    def receiver(self) -> List["LinTpNode"]:
        """Get receiver (Pythonic accessor)."""
        return self._receiver
        # Time for transmission of the LIN frame (any N-PDU) on side.
        # Specified in seconds.
        self._timeoutAs: Optional["TimeValue"] = None

    @property
    def timeout_as(self) -> Optional["TimeValue"]:
        """Get timeoutAs (Pythonic accessor)."""
        return self._timeoutAs

    @timeout_as.setter
    def timeout_as(self, value: Optional["TimeValue"]) -> None:
        """
        Set timeoutAs with validation.

        Args:
            value: The timeoutAs to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeoutAs = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeoutAs must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeoutAs = value
        # This attribute defines the timeout value for waiting for a FF-x (in case of
                # retry) after receiving the last CF or an FC or AF on the receiver side.
        # Specified.
        self._timeoutCr: Optional["TimeValue"] = None

    @property
    def timeout_cr(self) -> Optional["TimeValue"]:
        """Get timeoutCr (Pythonic accessor)."""
        return self._timeoutCr

    @timeout_cr.setter
    def timeout_cr(self, value: Optional["TimeValue"]) -> None:
        """
        Set timeoutCr with validation.

        Args:
            value: The timeoutCr to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeoutCr = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeoutCr must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeoutCr = value
        # The attribute timeoutCs represents the time (in seconds) between the transmit
        # request of a CF the transmit request of the next CF N-PDU.
        self._timeoutCs: Optional["TimeValue"] = None

    @property
    def timeout_cs(self) -> Optional["TimeValue"]:
        """Get timeoutCs (Pythonic accessor)."""
        return self._timeoutCs

    @timeout_cs.setter
    def timeout_cs(self, value: Optional["TimeValue"]) -> None:
        """
        Set timeoutCs with validation.

        Args:
            value: The timeoutCs to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeoutCs = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeoutCs must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeoutCs = value
        # The source of the TP connection.
        self._transmitter: Optional["LinTpNode"] = None

    @property
    def transmitter(self) -> Optional["LinTpNode"]:
        """Get transmitter (Pythonic accessor)."""
        return self._transmitter

    @transmitter.setter
    def transmitter(self, value: Optional["LinTpNode"]) -> None:
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

        if not isinstance(value, LinTpNode):
            raise TypeError(
                f"transmitter must be LinTpNode or None, got {type(value).__name__}"
            )
        self._transmitter = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataPdu(self) -> "NPdu":
        """
        AUTOSAR-compliant getter for dataPdu.

        Returns:
            The dataPdu value

        Note:
            Delegates to data_pdu property (CODING_RULE_V2_00017)
        """
        return self.data_pdu  # Delegates to property

    def setDataPdu(self, value: "NPdu") -> "LinTpConnection":
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

    def getFlowControl(self) -> "NPdu":
        """
        AUTOSAR-compliant getter for flowControl.

        Returns:
            The flowControl value

        Note:
            Delegates to flow_control property (CODING_RULE_V2_00017)
        """
        return self.flow_control  # Delegates to property

    def setFlowControl(self, value: "NPdu") -> "LinTpConnection":
        """
        AUTOSAR-compliant setter for flowControl with method chaining.

        Args:
            value: The flowControl to set

        Returns:
            self for method chaining

        Note:
            Delegates to flow_control property setter (gets validation automatically)
        """
        self.flow_control = value  # Delegates to property setter
        return self

    def getLinTpNSdu(self) -> "IPdu":
        """
        AUTOSAR-compliant getter for linTpNSdu.

        Returns:
            The linTpNSdu value

        Note:
            Delegates to lin_tp_n_sdu property (CODING_RULE_V2_00017)
        """
        return self.lin_tp_n_sdu  # Delegates to property

    def setLinTpNSdu(self, value: "IPdu") -> "LinTpConnection":
        """
        AUTOSAR-compliant setter for linTpNSdu with method chaining.

        Args:
            value: The linTpNSdu to set

        Returns:
            self for method chaining

        Note:
            Delegates to lin_tp_n_sdu property setter (gets validation automatically)
        """
        self.lin_tp_n_sdu = value  # Delegates to property setter
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

    def setMulticast(self, value: "TpAddress") -> "LinTpConnection":
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

    def getReceiver(self) -> List["LinTpNode"]:
        """
        AUTOSAR-compliant getter for receiver.

        Returns:
            The receiver value

        Note:
            Delegates to receiver property (CODING_RULE_V2_00017)
        """
        return self.receiver  # Delegates to property

    def getTimeoutAs(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for timeoutAs.

        Returns:
            The timeoutAs value

        Note:
            Delegates to timeout_as property (CODING_RULE_V2_00017)
        """
        return self.timeout_as  # Delegates to property

    def setTimeoutAs(self, value: "TimeValue") -> "LinTpConnection":
        """
        AUTOSAR-compliant setter for timeoutAs with method chaining.

        Args:
            value: The timeoutAs to set

        Returns:
            self for method chaining

        Note:
            Delegates to timeout_as property setter (gets validation automatically)
        """
        self.timeout_as = value  # Delegates to property setter
        return self

    def getTimeoutCr(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for timeoutCr.

        Returns:
            The timeoutCr value

        Note:
            Delegates to timeout_cr property (CODING_RULE_V2_00017)
        """
        return self.timeout_cr  # Delegates to property

    def setTimeoutCr(self, value: "TimeValue") -> "LinTpConnection":
        """
        AUTOSAR-compliant setter for timeoutCr with method chaining.

        Args:
            value: The timeoutCr to set

        Returns:
            self for method chaining

        Note:
            Delegates to timeout_cr property setter (gets validation automatically)
        """
        self.timeout_cr = value  # Delegates to property setter
        return self

    def getTimeoutCs(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for timeoutCs.

        Returns:
            The timeoutCs value

        Note:
            Delegates to timeout_cs property (CODING_RULE_V2_00017)
        """
        return self.timeout_cs  # Delegates to property

    def setTimeoutCs(self, value: "TimeValue") -> "LinTpConnection":
        """
        AUTOSAR-compliant setter for timeoutCs with method chaining.

        Args:
            value: The timeoutCs to set

        Returns:
            self for method chaining

        Note:
            Delegates to timeout_cs property setter (gets validation automatically)
        """
        self.timeout_cs = value  # Delegates to property setter
        return self

    def getTransmitter(self) -> "LinTpNode":
        """
        AUTOSAR-compliant getter for transmitter.

        Returns:
            The transmitter value

        Note:
            Delegates to transmitter property (CODING_RULE_V2_00017)
        """
        return self.transmitter  # Delegates to property

    def setTransmitter(self, value: "LinTpNode") -> "LinTpConnection":
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

    def with_data_pdu(self, value: Optional["NPdu"]) -> "LinTpConnection":
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

    def with_flow_control(self, value: Optional["NPdu"]) -> "LinTpConnection":
        """
        Set flowControl and return self for chaining.

        Args:
            value: The flowControl to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_flow_control("value")
        """
        self.flow_control = value  # Use property setter (gets validation)
        return self

    def with_lin_tp_n_sdu(self, value: Optional["IPdu"]) -> "LinTpConnection":
        """
        Set linTpNSdu and return self for chaining.

        Args:
            value: The linTpNSdu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_lin_tp_n_sdu("value")
        """
        self.lin_tp_n_sdu = value  # Use property setter (gets validation)
        return self

    def with_multicast(self, value: Optional["TpAddress"]) -> "LinTpConnection":
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

    def with_timeout_as(self, value: Optional["TimeValue"]) -> "LinTpConnection":
        """
        Set timeoutAs and return self for chaining.

        Args:
            value: The timeoutAs to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_timeout_as("value")
        """
        self.timeout_as = value  # Use property setter (gets validation)
        return self

    def with_timeout_cr(self, value: Optional["TimeValue"]) -> "LinTpConnection":
        """
        Set timeoutCr and return self for chaining.

        Args:
            value: The timeoutCr to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_timeout_cr("value")
        """
        self.timeout_cr = value  # Use property setter (gets validation)
        return self

    def with_timeout_cs(self, value: Optional["TimeValue"]) -> "LinTpConnection":
        """
        Set timeoutCs and return self for chaining.

        Args:
            value: The timeoutCs to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_timeout_cs("value")
        """
        self.timeout_cs = value  # Use property setter (gets validation)
        return self

    def with_transmitter(self, value: Optional["LinTpNode"]) -> "LinTpConnection":
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
