from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class CanTpConnection(TpConnection):
    """
    A connection identifies the sender and the receiver of this particular
    communication. The CanTp module routes a Pdu through this connection.
    atpVariation: Derived, because TpNode can vary.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::CanTpConnection
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 608, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Declares which communication addressing mode is supported.
        self._addressing: Optional["CanTpAddressing"] = None

    @property
    def addressing(self) -> Optional["CanTpAddressing"]:
        """Get addressing (Pythonic accessor)."""
        return self._addressing

    @addressing.setter
    def addressing(self, value: Optional["CanTpAddressing"]) -> None:
        """
        Set addressing with validation.
        
        Args:
            value: The addressing to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._addressing = None
            return

        if not isinstance(value, CanTpAddressing):
            raise TypeError(
                f"addressing must be CanTpAddressing or None, got {type(value).__name__}"
            )
        self._addressing = value
        # With this switch Tx Cancellation can be turned on or off.
        # that the Rx Cancellation is always enabled.
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
        # Reference to the CanTpChannel on which this CanTp realized.
        self._canTpChannel: Optional["CanTpChannel"] = None

    @property
    def can_tp_channel(self) -> Optional["CanTpChannel"]:
        """Get canTpChannel (Pythonic accessor)."""
        return self._canTpChannel

    @can_tp_channel.setter
    def can_tp_channel(self, value: Optional["CanTpChannel"]) -> None:
        """
        Set canTpChannel with validation.
        
        Args:
            value: The canTpChannel to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._canTpChannel = None
            return

        if not isinstance(value, CanTpChannel):
            raise TypeError(
                f"canTpChannel must be CanTpChannel or None, got {type(value).__name__}"
            )
        self._canTpChannel = value
        # Reference to an Data NPdu.
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
        self._flowControlPdu: Optional["NPdu"] = None

    @property
    def flow_control_pdu(self) -> Optional["NPdu"]:
        """Get flowControlPdu (Pythonic accessor)."""
        return self._flowControlPdu

    @flow_control_pdu.setter
    def flow_control_pdu(self, value: Optional["NPdu"]) -> None:
        """
        Set flowControlPdu with validation.
        
        Args:
            value: The flowControlPdu to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._flowControlPdu = None
            return

        if not isinstance(value, NPdu):
            raise TypeError(
                f"flowControlPdu must be NPdu or None, got {type(value).__name__}"
            )
        self._flowControlPdu = value
        # The maximum number of N-PDUs the CanTp receiver sender to send, before
                # waiting for an continue transmission of the following further details on this
                # parameter value see specification.
        # reasons of buffer length, the CAN Transport adapt the BS value within the
                # limit of this.
        self._maxBlockSize: Optional["Integer"] = None

    @property
    def max_block_size(self) -> Optional["Integer"]:
        """Get maxBlockSize (Pythonic accessor)."""
        return self._maxBlockSize

    @max_block_size.setter
    def max_block_size(self, value: Optional["Integer"]) -> None:
        """
        Set maxBlockSize with validation.
        
        Args:
            value: The maxBlockSize to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxBlockSize = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"maxBlockSize must be Integer or None, got {type(value).__name__}"
            )
        self._maxBlockSize = value
        # TP address for 1:n connections.
        self._multicast: Optional["CanTpAddress"] = None

    @property
    def multicast(self) -> Optional["CanTpAddress"]:
        """Get multicast (Pythonic accessor)."""
        return self._multicast

    @multicast.setter
    def multicast(self, value: Optional["CanTpAddress"]) -> None:
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

        if not isinstance(value, CanTpAddress):
            raise TypeError(
                f"multicast must be CanTpAddress or None, got {type(value).__name__}"
            )
        self._multicast = value
        # This specifies whether or not Sfs, FCs and the last CF be padded to 8 bytes
                # length in case it contains less N-PDU received uses padding for SF, FC and
                # CF.
        # (N-PDU length is always 8 bytes) N-PDU received does not use padding for SF,
                # the last CF.
        # (N-PDU length is dynamic).
        self._padding: Optional["Boolean"] = None

    @property
    def padding(self) -> Optional["Boolean"]:
        """Get padding (Pythonic accessor)."""
        return self._padding

    @padding.setter
    def padding(self, value: Optional["Boolean"]) -> None:
        """
        Set padding with validation.
        
        Args:
            value: The padding to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._padding = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"padding must be Boolean or None, got {type(value).__name__}"
            )
        self._padding = value
        # The target of the TP connection.
        self._receiver: List["CanTpNode"] = []

    @property
    def receiver(self) -> List["CanTpNode"]:
        """Get receiver (Pythonic accessor)."""
        return self._receiver
        # Network Target Address type.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._taTypeType: Optional["NetworkTargetAddress"] = None

    @property
    def ta_type_type(self) -> Optional["NetworkTargetAddress"]:
        """Get taTypeType (Pythonic accessor)."""
        return self._taTypeType

    @ta_type_type.setter
    def ta_type_type(self, value: Optional["NetworkTargetAddress"]) -> None:
        """
        Set taTypeType with validation.
        
        Args:
            value: The taTypeType to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._taTypeType = None
            return

        if not isinstance(value, NetworkTargetAddress):
            raise TypeError(
                f"taTypeType must be NetworkTargetAddress or None, got {type(value).__name__}"
            )
        self._taTypeType = value
        # Value in seconds of the performance requirement for (N_ N_Ar).
        # N_Br is the elapsed time between the of a FF or CF or the transmit a FC,
                # until the transmit request of the next.
        self._timeoutBr: Optional["TimeValue"] = None

    @property
    def timeout_br(self) -> Optional["TimeValue"]:
        """Get timeoutBr (Pythonic accessor)."""
        return self._timeoutBr

    @timeout_br.setter
    def timeout_br(self, value: Optional["TimeValue"]) -> None:
        """
        Set timeoutBr with validation.
        
        Args:
            value: The timeoutBr to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeoutBr = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeoutBr must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeoutBr = value
        # This parameter defines the timeout for waiting for an FC on the sender side
                # in an 1:1 connection.
        # Specified.
        self._timeoutBs: Optional["TimeValue"] = None

    @property
    def timeout_bs(self) -> Optional["TimeValue"]:
        """Get timeoutBs (Pythonic accessor)."""
        return self._timeoutBs

    @timeout_bs.setter
    def timeout_bs(self, value: Optional["TimeValue"]) -> None:
        """
        Set timeoutBs with validation.
        
        Args:
            value: The timeoutBs to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeoutBs = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeoutBs must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeoutBs = value
        # This parameter defines the timeout value for waiting for a FF-x (in case of
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
        # Reference to an IPdu that is segmented by the Transport.
        self._tpSdu: Optional["IPdu"] = None

    @property
    def tp_sdu(self) -> Optional["IPdu"]:
        """Get tpSdu (Pythonic accessor)."""
        return self._tpSdu

    @tp_sdu.setter
    def tp_sdu(self, value: Optional["IPdu"]) -> None:
        """
        Set tpSdu with validation.
        
        Args:
            value: The tpSdu to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tpSdu = None
            return

        if not isinstance(value, IPdu):
            raise TypeError(
                f"tpSdu must be IPdu or None, got {type(value).__name__}"
            )
        self._tpSdu = value
        # The source of the TP connection.
        self._transmitter: Optional["CanTpNode"] = None

    @property
    def transmitter(self) -> Optional["CanTpNode"]:
        """Get transmitter (Pythonic accessor)."""
        return self._transmitter

    @transmitter.setter
    def transmitter(self, value: Optional["CanTpNode"]) -> None:
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

        if not isinstance(value, CanTpNode):
            raise TypeError(
                f"transmitter must be CanTpNode or None, got {type(value).__name__}"
            )
        self._transmitter = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAddressing(self) -> "CanTpAddressing":
        """
        AUTOSAR-compliant getter for addressing.
        
        Returns:
            The addressing value
        
        Note:
            Delegates to addressing property (CODING_RULE_V2_00017)
        """
        return self.addressing  # Delegates to property

    def setAddressing(self, value: "CanTpAddressing") -> "CanTpConnection":
        """
        AUTOSAR-compliant setter for addressing with method chaining.
        
        Args:
            value: The addressing to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to addressing property setter (gets validation automatically)
        """
        self.addressing = value  # Delegates to property setter
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

    def setCancellation(self, value: "Boolean") -> "CanTpConnection":
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

    def getCanTpChannel(self) -> "CanTpChannel":
        """
        AUTOSAR-compliant getter for canTpChannel.
        
        Returns:
            The canTpChannel value
        
        Note:
            Delegates to can_tp_channel property (CODING_RULE_V2_00017)
        """
        return self.can_tp_channel  # Delegates to property

    def setCanTpChannel(self, value: "CanTpChannel") -> "CanTpConnection":
        """
        AUTOSAR-compliant setter for canTpChannel with method chaining.
        
        Args:
            value: The canTpChannel to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to can_tp_channel property setter (gets validation automatically)
        """
        self.can_tp_channel = value  # Delegates to property setter
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

    def setDataPdu(self, value: "NPdu") -> "CanTpConnection":
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

    def getFlowControlPdu(self) -> "NPdu":
        """
        AUTOSAR-compliant getter for flowControlPdu.
        
        Returns:
            The flowControlPdu value
        
        Note:
            Delegates to flow_control_pdu property (CODING_RULE_V2_00017)
        """
        return self.flow_control_pdu  # Delegates to property

    def setFlowControlPdu(self, value: "NPdu") -> "CanTpConnection":
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

    def getMaxBlockSize(self) -> "Integer":
        """
        AUTOSAR-compliant getter for maxBlockSize.
        
        Returns:
            The maxBlockSize value
        
        Note:
            Delegates to max_block_size property (CODING_RULE_V2_00017)
        """
        return self.max_block_size  # Delegates to property

    def setMaxBlockSize(self, value: "Integer") -> "CanTpConnection":
        """
        AUTOSAR-compliant setter for maxBlockSize with method chaining.
        
        Args:
            value: The maxBlockSize to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to max_block_size property setter (gets validation automatically)
        """
        self.max_block_size = value  # Delegates to property setter
        return self

    def getMulticast(self) -> "CanTpAddress":
        """
        AUTOSAR-compliant getter for multicast.
        
        Returns:
            The multicast value
        
        Note:
            Delegates to multicast property (CODING_RULE_V2_00017)
        """
        return self.multicast  # Delegates to property

    def setMulticast(self, value: "CanTpAddress") -> "CanTpConnection":
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

    def getPadding(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for padding.
        
        Returns:
            The padding value
        
        Note:
            Delegates to padding property (CODING_RULE_V2_00017)
        """
        return self.padding  # Delegates to property

    def setPadding(self, value: "Boolean") -> "CanTpConnection":
        """
        AUTOSAR-compliant setter for padding with method chaining.
        
        Args:
            value: The padding to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to padding property setter (gets validation automatically)
        """
        self.padding = value  # Delegates to property setter
        return self

    def getReceiver(self) -> List["CanTpNode"]:
        """
        AUTOSAR-compliant getter for receiver.
        
        Returns:
            The receiver value
        
        Note:
            Delegates to receiver property (CODING_RULE_V2_00017)
        """
        return self.receiver  # Delegates to property

    def getTaTypeType(self) -> "NetworkTargetAddress":
        """
        AUTOSAR-compliant getter for taTypeType.
        
        Returns:
            The taTypeType value
        
        Note:
            Delegates to ta_type_type property (CODING_RULE_V2_00017)
        """
        return self.ta_type_type  # Delegates to property

    def setTaTypeType(self, value: "NetworkTargetAddress") -> "CanTpConnection":
        """
        AUTOSAR-compliant setter for taTypeType with method chaining.
        
        Args:
            value: The taTypeType to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to ta_type_type property setter (gets validation automatically)
        """
        self.ta_type_type = value  # Delegates to property setter
        return self

    def getTimeoutBr(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for timeoutBr.
        
        Returns:
            The timeoutBr value
        
        Note:
            Delegates to timeout_br property (CODING_RULE_V2_00017)
        """
        return self.timeout_br  # Delegates to property

    def setTimeoutBr(self, value: "TimeValue") -> "CanTpConnection":
        """
        AUTOSAR-compliant setter for timeoutBr with method chaining.
        
        Args:
            value: The timeoutBr to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to timeout_br property setter (gets validation automatically)
        """
        self.timeout_br = value  # Delegates to property setter
        return self

    def getTimeoutBs(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for timeoutBs.
        
        Returns:
            The timeoutBs value
        
        Note:
            Delegates to timeout_bs property (CODING_RULE_V2_00017)
        """
        return self.timeout_bs  # Delegates to property

    def setTimeoutBs(self, value: "TimeValue") -> "CanTpConnection":
        """
        AUTOSAR-compliant setter for timeoutBs with method chaining.
        
        Args:
            value: The timeoutBs to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to timeout_bs property setter (gets validation automatically)
        """
        self.timeout_bs = value  # Delegates to property setter
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

    def setTimeoutCr(self, value: "TimeValue") -> "CanTpConnection":
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

    def setTimeoutCs(self, value: "TimeValue") -> "CanTpConnection":
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

    def getTpSdu(self) -> "IPdu":
        """
        AUTOSAR-compliant getter for tpSdu.
        
        Returns:
            The tpSdu value
        
        Note:
            Delegates to tp_sdu property (CODING_RULE_V2_00017)
        """
        return self.tp_sdu  # Delegates to property

    def setTpSdu(self, value: "IPdu") -> "CanTpConnection":
        """
        AUTOSAR-compliant setter for tpSdu with method chaining.
        
        Args:
            value: The tpSdu to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to tp_sdu property setter (gets validation automatically)
        """
        self.tp_sdu = value  # Delegates to property setter
        return self

    def getTransmitter(self) -> "CanTpNode":
        """
        AUTOSAR-compliant getter for transmitter.
        
        Returns:
            The transmitter value
        
        Note:
            Delegates to transmitter property (CODING_RULE_V2_00017)
        """
        return self.transmitter  # Delegates to property

    def setTransmitter(self, value: "CanTpNode") -> "CanTpConnection":
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

    def with_addressing(self, value: Optional["CanTpAddressing"]) -> "CanTpConnection":
        """
        Set addressing and return self for chaining.
        
        Args:
            value: The addressing to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_addressing("value")
        """
        self.addressing = value  # Use property setter (gets validation)
        return self

    def with_cancellation(self, value: Optional["Boolean"]) -> "CanTpConnection":
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

    def with_can_tp_channel(self, value: Optional["CanTpChannel"]) -> "CanTpConnection":
        """
        Set canTpChannel and return self for chaining.
        
        Args:
            value: The canTpChannel to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_can_tp_channel("value")
        """
        self.can_tp_channel = value  # Use property setter (gets validation)
        return self

    def with_data_pdu(self, value: Optional["NPdu"]) -> "CanTpConnection":
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

    def with_flow_control_pdu(self, value: Optional["NPdu"]) -> "CanTpConnection":
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

    def with_max_block_size(self, value: Optional["Integer"]) -> "CanTpConnection":
        """
        Set maxBlockSize and return self for chaining.
        
        Args:
            value: The maxBlockSize to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_max_block_size("value")
        """
        self.max_block_size = value  # Use property setter (gets validation)
        return self

    def with_multicast(self, value: Optional["CanTpAddress"]) -> "CanTpConnection":
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

    def with_padding(self, value: Optional["Boolean"]) -> "CanTpConnection":
        """
        Set padding and return self for chaining.
        
        Args:
            value: The padding to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_padding("value")
        """
        self.padding = value  # Use property setter (gets validation)
        return self

    def with_ta_type_type(self, value: Optional["NetworkTargetAddress"]) -> "CanTpConnection":
        """
        Set taTypeType and return self for chaining.
        
        Args:
            value: The taTypeType to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_ta_type_type("value")
        """
        self.ta_type_type = value  # Use property setter (gets validation)
        return self

    def with_timeout_br(self, value: Optional["TimeValue"]) -> "CanTpConnection":
        """
        Set timeoutBr and return self for chaining.
        
        Args:
            value: The timeoutBr to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_timeout_br("value")
        """
        self.timeout_br = value  # Use property setter (gets validation)
        return self

    def with_timeout_bs(self, value: Optional["TimeValue"]) -> "CanTpConnection":
        """
        Set timeoutBs and return self for chaining.
        
        Args:
            value: The timeoutBs to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_timeout_bs("value")
        """
        self.timeout_bs = value  # Use property setter (gets validation)
        return self

    def with_timeout_cr(self, value: Optional["TimeValue"]) -> "CanTpConnection":
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

    def with_timeout_cs(self, value: Optional["TimeValue"]) -> "CanTpConnection":
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

    def with_tp_sdu(self, value: Optional["IPdu"]) -> "CanTpConnection":
        """
        Set tpSdu and return self for chaining.
        
        Args:
            value: The tpSdu to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_tp_sdu("value")
        """
        self.tp_sdu = value  # Use property setter (gets validation)
        return self

    def with_transmitter(self, value: Optional["CanTpNode"]) -> "CanTpConnection":
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