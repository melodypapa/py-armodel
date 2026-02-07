from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class FlexrayArTpChannel(ARObject):
    """
    A channel is a group of connections sharing several properties. The FlexRay
    AutosarTransport Layer supports several channels. These channels can work
    concurrently, thus each of them requires its own state machine and
    management data structures and its own PDU-IDs.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::FlexrayArTpChannel

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 600, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Type of Acknowledgement.
        self._ackType: Optional["FrArTpAckType"] = None

    @property
    def ack_type(self) -> Optional["FrArTpAckType"]:
        """Get ackType (Pythonic accessor)."""
        return self._ackType

    @ack_type.setter
    def ack_type(self, value: Optional["FrArTpAckType"]) -> None:
        """
        Set ackType with validation.

        Args:
            value: The ackType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ackType = None
            return

        if not isinstance(value, FrArTpAckType):
            raise TypeError(
                f"ackType must be FrArTpAckType or None, got {type(value).__name__}"
            )
        self._ackType = value
        # With this switch Tx and Rx Cancellation can be turned on.
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
        # Adressing Type of this connection: Two Bytes Byte.
        self._extended: Optional["Boolean"] = None

    @property
    def extended(self) -> Optional["Boolean"]:
        """Get extended (Pythonic accessor)."""
        return self._extended

    @extended.setter
    def extended(self, value: Optional["Boolean"]) -> None:
        """
        Set extended with validation.

        Args:
            value: The extended to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._extended = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"extended must be Boolean or None, got {type(value).__name__}"
            )
        self._extended = value
        # This attribute defines the maximum number of trying to frame when a TIMEOUT
        # AR occurs (depending retry is configured).
        self._maxAr: Optional["Integer"] = None

    @property
    def max_ar(self) -> Optional["Integer"]:
        """Get maxAr (Pythonic accessor)."""
        return self._maxAr

    @max_ar.setter
    def max_ar(self, value: Optional["Integer"]) -> None:
        """
        Set maxAr with validation.

        Args:
            value: The maxAr to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxAr = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"maxAr must be Integer or None, got {type(value).__name__}"
            )
        self._maxAr = value
        # This attribute defines the maximum number of trying to frame when a TIMEOUT
        # AS occurs (depending on is configured).
        self._maxAs: Optional["Integer"] = None

    @property
    def max_as(self) -> Optional["Integer"]:
        """Get maxAs (Pythonic accessor)."""
        return self._maxAs

    @max_as.setter
    def max_as(self, value: Optional["Integer"]) -> None:
        """
        Set maxAs with validation.

        Args:
            value: The maxAs to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxAs = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"maxAs must be Integer or None, got {type(value).__name__}"
            )
        self._maxAs = value
        # This attribute defines the number of consecutive CFs FCs (block size).
        # Valid values are 1.
        # 16 is activated, and 0.
        # 255 otherwise.
        self._maxBs: Optional["Integer"] = None

    @property
    def max_bs(self) -> Optional["Integer"]:
        """Get maxBs (Pythonic accessor)."""
        return self._maxBs

    @max_bs.setter
    def max_bs(self, value: Optional["Integer"]) -> None:
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

        if not isinstance(value, Integer):
            raise TypeError(
                f"maxBs must be Integer or None, got {type(value).__name__}"
            )
        self._maxBs = value
        # This attribute defines the maximal number of wait frames sent for a pending
                # connection.
        # Range is 0.
        # 255.
        self._maxFcWait: Optional["PositiveInteger"] = None

    @property
    def max_fc_wait(self) -> Optional["PositiveInteger"]:
        """Get maxFcWait (Pythonic accessor)."""
        return self._maxFcWait

    @max_fc_wait.setter
    def max_fc_wait(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxFcWait with validation.

        Args:
            value: The maxFcWait to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxFcWait = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"maxFcWait must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._maxFcWait = value
        # This specifies the maximum message length for the particular channel.
        self._maximum: Optional["MaximumMessage"] = None

    @property
    def maximum(self) -> Optional["MaximumMessage"]:
        """Get maximum (Pythonic accessor)."""
        return self._maximum

    @maximum.setter
    def maximum(self, value: Optional["MaximumMessage"]) -> None:
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

        if not isinstance(value, MaximumMessage):
            raise TypeError(
                f"maximum must be MaximumMessage or None, got {type(value).__name__}"
            )
        self._maximum = value
        # This attribute defines the maximum number of retries (if configured for the
                # particular channel).
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._maxRetries: Optional["Integer"] = None

    @property
    def max_retries(self) -> Optional["Integer"]:
        """Get maxRetries (Pythonic accessor)."""
        return self._maxRetries

    @max_retries.setter
    def max_retries(self, value: Optional["Integer"]) -> None:
        """
        Set maxRetries with validation.

        Args:
            value: The maxRetries to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxRetries = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"maxRetries must be Integer or None, got {type(value).__name__}"
            )
        self._maxRetries = value
        # This attribute defines the minimum amount of time two succeeding CFs of a 1:1
                # segmented seconds.
        # Valid values are 0, 100µs, 200µs 1ms, 2ms.
        # 127ms.
        # The value can be changed using the FrArTp_ChangeParameter interface.
        # shall be an integer multiple cycle length multiplied with the multiplexing
                # factor, = n * cycle * m, where n is >=0, cycle is FlexrayCluster.
        # cycle, and m is the of those cycles where PDUs of the PDU scheduled.
        # Due to the scheduling strategies of FrTp, only be kept to a degree the
                # maximum temporal distance of the PDUs PDU pool within one FlexRay cycle.
        # 0.
        # 127.
        self._minimum: Optional["TimeValue"] = None

    @property
    def minimum(self) -> Optional["TimeValue"]:
        """Get minimum (Pythonic accessor)."""
        return self._minimum

    @minimum.setter
    def minimum(self, value: Optional["TimeValue"]) -> None:
        """
        Set minimum with validation.

        Args:
            value: The minimum to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minimum = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"minimum must be TimeValue or None, got {type(value).__name__}"
            )
        self._minimum = value
        # This attribute defines whether segmentation within a 1:n is allowed or not.
        self._multicast: Optional["Boolean"] = None

    @property
    def multicast(self) -> Optional["Boolean"]:
        """Get multicast (Pythonic accessor)."""
        return self._multicast

    @multicast.setter
    def multicast(self, value: Optional["Boolean"]) -> None:
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

        if not isinstance(value, Boolean):
            raise TypeError(
                f"multicast must be Boolean or None, got {type(value).__name__}"
            )
        self._multicast = value
        # A FlexRayTpChannel references a set of NPdus.
        # These logically assembled into a pool of Rx NPdus pool of Tx NPdus.
        # It shall be ensured that a either references all NPdus of such a none.
        self._nPdu: List["NPdu"] = []

    @property
    def n_pdu(self) -> List["NPdu"]:
        """Get nPdu (Pythonic accessor)."""
        return self._nPdu
        # This attribute defines the time in seconds between last CF of a block or an
        # FF-x (or SF-x) and an FC or AF.
        self._timeBr: Optional["TimeValue"] = None

    @property
    def time_br(self) -> Optional["TimeValue"]:
        """Get timeBr (Pythonic accessor)."""
        return self._timeBr

    @time_br.setter
    def time_br(self, value: Optional["TimeValue"]) -> None:
        """
        Set timeBr with validation.

        Args:
            value: The timeBr to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeBr = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeBr must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeBr = value
        # This attribute defines the time in seconds between the two consecutive frames
        # or between a and a flow control (for Transmit between reception of an flow
        # control or and sending of the next or a flow control (for Transmit.
        self._timeCs: Optional["TimeValue"] = None

    @property
    def time_cs(self) -> Optional["TimeValue"]:
        """Get timeCs (Pythonic accessor)."""
        return self._timeCs

    @time_cs.setter
    def time_cs(self, value: Optional["TimeValue"]) -> None:
        """
        Set timeCs with validation.

        Args:
            value: The timeCs to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeCs = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeCs must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeCs = value
        # This attribute states the timeout in seconds between the request of the
                # Transport Layer to the Flex and the corresponding confirmation of the on the
                # receiver side (for FC or AF).
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._timeoutAr: Optional["TimeValue"] = None

    @property
    def timeout_ar(self) -> Optional["TimeValue"]:
        """Get timeoutAr (Pythonic accessor)."""
        return self._timeoutAr

    @timeout_ar.setter
    def timeout_ar(self, value: Optional["TimeValue"]) -> None:
        """
        Set timeoutAr with validation.

        Args:
            value: The timeoutAr to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeoutAr = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeoutAr must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeoutAr = value
        # This attribute states the timeout in seconds between the request for the
        # first PDU of the group used current connection of the Transport Layer to the
        # and the corresponding confirmation of Interface (when having sent the last
        # PDU of used in this connection) on the sender side CF).
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
        # This attribute defines the timeout in seconds for waiting FC or AF on the
        # sender side in a 1:1 connection.
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
        # This attribute defines the timeout value in seconds for a CF or FF-x (in case
        # of retry) after receiving CF or after sending an FC or AF on the receiver.
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
        # Group of connections that can be used in this channel.
        self._tpConnection: List["FlexrayArTpConnection"] = []

    @property
    def tp_connection(self) -> List["FlexrayArTpConnection"]:
        """Get tpConnection (Pythonic accessor)."""
        return self._tpConnection

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAckType(self) -> "FrArTpAckType":
        """
        AUTOSAR-compliant getter for ackType.

        Returns:
            The ackType value

        Note:
            Delegates to ack_type property (CODING_RULE_V2_00017)
        """
        return self.ack_type  # Delegates to property

    def setAckType(self, value: "FrArTpAckType") -> "FlexrayArTpChannel":
        """
        AUTOSAR-compliant setter for ackType with method chaining.

        Args:
            value: The ackType to set

        Returns:
            self for method chaining

        Note:
            Delegates to ack_type property setter (gets validation automatically)
        """
        self.ack_type = value  # Delegates to property setter
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

    def setCancellation(self, value: "Boolean") -> "FlexrayArTpChannel":
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

    def getExtended(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for extended.

        Returns:
            The extended value

        Note:
            Delegates to extended property (CODING_RULE_V2_00017)
        """
        return self.extended  # Delegates to property

    def setExtended(self, value: "Boolean") -> "FlexrayArTpChannel":
        """
        AUTOSAR-compliant setter for extended with method chaining.

        Args:
            value: The extended to set

        Returns:
            self for method chaining

        Note:
            Delegates to extended property setter (gets validation automatically)
        """
        self.extended = value  # Delegates to property setter
        return self

    def getMaxAr(self) -> "Integer":
        """
        AUTOSAR-compliant getter for maxAr.

        Returns:
            The maxAr value

        Note:
            Delegates to max_ar property (CODING_RULE_V2_00017)
        """
        return self.max_ar  # Delegates to property

    def setMaxAr(self, value: "Integer") -> "FlexrayArTpChannel":
        """
        AUTOSAR-compliant setter for maxAr with method chaining.

        Args:
            value: The maxAr to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_ar property setter (gets validation automatically)
        """
        self.max_ar = value  # Delegates to property setter
        return self

    def getMaxAs(self) -> "Integer":
        """
        AUTOSAR-compliant getter for maxAs.

        Returns:
            The maxAs value

        Note:
            Delegates to max_as property (CODING_RULE_V2_00017)
        """
        return self.max_as  # Delegates to property

    def setMaxAs(self, value: "Integer") -> "FlexrayArTpChannel":
        """
        AUTOSAR-compliant setter for maxAs with method chaining.

        Args:
            value: The maxAs to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_as property setter (gets validation automatically)
        """
        self.max_as = value  # Delegates to property setter
        return self

    def getMaxBs(self) -> "Integer":
        """
        AUTOSAR-compliant getter for maxBs.

        Returns:
            The maxBs value

        Note:
            Delegates to max_bs property (CODING_RULE_V2_00017)
        """
        return self.max_bs  # Delegates to property

    def setMaxBs(self, value: "Integer") -> "FlexrayArTpChannel":
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

    def getMaxFcWait(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxFcWait.

        Returns:
            The maxFcWait value

        Note:
            Delegates to max_fc_wait property (CODING_RULE_V2_00017)
        """
        return self.max_fc_wait  # Delegates to property

    def setMaxFcWait(self, value: "PositiveInteger") -> "FlexrayArTpChannel":
        """
        AUTOSAR-compliant setter for maxFcWait with method chaining.

        Args:
            value: The maxFcWait to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_fc_wait property setter (gets validation automatically)
        """
        self.max_fc_wait = value  # Delegates to property setter
        return self

    def getMaximum(self) -> "MaximumMessage":
        """
        AUTOSAR-compliant getter for maximum.

        Returns:
            The maximum value

        Note:
            Delegates to maximum property (CODING_RULE_V2_00017)
        """
        return self.maximum  # Delegates to property

    def setMaximum(self, value: "MaximumMessage") -> "FlexrayArTpChannel":
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

    def getMaxRetries(self) -> "Integer":
        """
        AUTOSAR-compliant getter for maxRetries.

        Returns:
            The maxRetries value

        Note:
            Delegates to max_retries property (CODING_RULE_V2_00017)
        """
        return self.max_retries  # Delegates to property

    def setMaxRetries(self, value: "Integer") -> "FlexrayArTpChannel":
        """
        AUTOSAR-compliant setter for maxRetries with method chaining.

        Args:
            value: The maxRetries to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_retries property setter (gets validation automatically)
        """
        self.max_retries = value  # Delegates to property setter
        return self

    def getMinimum(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for minimum.

        Returns:
            The minimum value

        Note:
            Delegates to minimum property (CODING_RULE_V2_00017)
        """
        return self.minimum  # Delegates to property

    def setMinimum(self, value: "TimeValue") -> "FlexrayArTpChannel":
        """
        AUTOSAR-compliant setter for minimum with method chaining.

        Args:
            value: The minimum to set

        Returns:
            self for method chaining

        Note:
            Delegates to minimum property setter (gets validation automatically)
        """
        self.minimum = value  # Delegates to property setter
        return self

    def getMulticast(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for multicast.

        Returns:
            The multicast value

        Note:
            Delegates to multicast property (CODING_RULE_V2_00017)
        """
        return self.multicast  # Delegates to property

    def setMulticast(self, value: "Boolean") -> "FlexrayArTpChannel":
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

    def getNPdu(self) -> List["NPdu"]:
        """
        AUTOSAR-compliant getter for nPdu.

        Returns:
            The nPdu value

        Note:
            Delegates to n_pdu property (CODING_RULE_V2_00017)
        """
        return self.n_pdu  # Delegates to property

    def getTimeBr(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for timeBr.

        Returns:
            The timeBr value

        Note:
            Delegates to time_br property (CODING_RULE_V2_00017)
        """
        return self.time_br  # Delegates to property

    def setTimeBr(self, value: "TimeValue") -> "FlexrayArTpChannel":
        """
        AUTOSAR-compliant setter for timeBr with method chaining.

        Args:
            value: The timeBr to set

        Returns:
            self for method chaining

        Note:
            Delegates to time_br property setter (gets validation automatically)
        """
        self.time_br = value  # Delegates to property setter
        return self

    def getTimeCs(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for timeCs.

        Returns:
            The timeCs value

        Note:
            Delegates to time_cs property (CODING_RULE_V2_00017)
        """
        return self.time_cs  # Delegates to property

    def setTimeCs(self, value: "TimeValue") -> "FlexrayArTpChannel":
        """
        AUTOSAR-compliant setter for timeCs with method chaining.

        Args:
            value: The timeCs to set

        Returns:
            self for method chaining

        Note:
            Delegates to time_cs property setter (gets validation automatically)
        """
        self.time_cs = value  # Delegates to property setter
        return self

    def getTimeoutAr(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for timeoutAr.

        Returns:
            The timeoutAr value

        Note:
            Delegates to timeout_ar property (CODING_RULE_V2_00017)
        """
        return self.timeout_ar  # Delegates to property

    def setTimeoutAr(self, value: "TimeValue") -> "FlexrayArTpChannel":
        """
        AUTOSAR-compliant setter for timeoutAr with method chaining.

        Args:
            value: The timeoutAr to set

        Returns:
            self for method chaining

        Note:
            Delegates to timeout_ar property setter (gets validation automatically)
        """
        self.timeout_ar = value  # Delegates to property setter
        return self

    def getTimeoutAs(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for timeoutAs.

        Returns:
            The timeoutAs value

        Note:
            Delegates to timeout_as property (CODING_RULE_V2_00017)
        """
        return self.timeout_as  # Delegates to property

    def setTimeoutAs(self, value: "TimeValue") -> "FlexrayArTpChannel":
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

    def getTimeoutBs(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for timeoutBs.

        Returns:
            The timeoutBs value

        Note:
            Delegates to timeout_bs property (CODING_RULE_V2_00017)
        """
        return self.timeout_bs  # Delegates to property

    def setTimeoutBs(self, value: "TimeValue") -> "FlexrayArTpChannel":
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

    def setTimeoutCr(self, value: "TimeValue") -> "FlexrayArTpChannel":
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

    def getTpConnection(self) -> List["FlexrayArTpConnection"]:
        """
        AUTOSAR-compliant getter for tpConnection.

        Returns:
            The tpConnection value

        Note:
            Delegates to tp_connection property (CODING_RULE_V2_00017)
        """
        return self.tp_connection  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ack_type(self, value: Optional["FrArTpAckType"]) -> "FlexrayArTpChannel":
        """
        Set ackType and return self for chaining.

        Args:
            value: The ackType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ack_type("value")
        """
        self.ack_type = value  # Use property setter (gets validation)
        return self

    def with_cancellation(self, value: Optional["Boolean"]) -> "FlexrayArTpChannel":
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

    def with_extended(self, value: Optional["Boolean"]) -> "FlexrayArTpChannel":
        """
        Set extended and return self for chaining.

        Args:
            value: The extended to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_extended("value")
        """
        self.extended = value  # Use property setter (gets validation)
        return self

    def with_max_ar(self, value: Optional["Integer"]) -> "FlexrayArTpChannel":
        """
        Set maxAr and return self for chaining.

        Args:
            value: The maxAr to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_ar("value")
        """
        self.max_ar = value  # Use property setter (gets validation)
        return self

    def with_max_as(self, value: Optional["Integer"]) -> "FlexrayArTpChannel":
        """
        Set maxAs and return self for chaining.

        Args:
            value: The maxAs to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_as("value")
        """
        self.max_as = value  # Use property setter (gets validation)
        return self

    def with_max_bs(self, value: Optional["Integer"]) -> "FlexrayArTpChannel":
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

    def with_max_fc_wait(self, value: Optional["PositiveInteger"]) -> "FlexrayArTpChannel":
        """
        Set maxFcWait and return self for chaining.

        Args:
            value: The maxFcWait to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_fc_wait("value")
        """
        self.max_fc_wait = value  # Use property setter (gets validation)
        return self

    def with_maximum(self, value: Optional["MaximumMessage"]) -> "FlexrayArTpChannel":
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

    def with_max_retries(self, value: Optional["Integer"]) -> "FlexrayArTpChannel":
        """
        Set maxRetries and return self for chaining.

        Args:
            value: The maxRetries to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_retries("value")
        """
        self.max_retries = value  # Use property setter (gets validation)
        return self

    def with_minimum(self, value: Optional["TimeValue"]) -> "FlexrayArTpChannel":
        """
        Set minimum and return self for chaining.

        Args:
            value: The minimum to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_minimum("value")
        """
        self.minimum = value  # Use property setter (gets validation)
        return self

    def with_multicast(self, value: Optional["Boolean"]) -> "FlexrayArTpChannel":
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

    def with_time_br(self, value: Optional["TimeValue"]) -> "FlexrayArTpChannel":
        """
        Set timeBr and return self for chaining.

        Args:
            value: The timeBr to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_time_br("value")
        """
        self.time_br = value  # Use property setter (gets validation)
        return self

    def with_time_cs(self, value: Optional["TimeValue"]) -> "FlexrayArTpChannel":
        """
        Set timeCs and return self for chaining.

        Args:
            value: The timeCs to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_time_cs("value")
        """
        self.time_cs = value  # Use property setter (gets validation)
        return self

    def with_timeout_ar(self, value: Optional["TimeValue"]) -> "FlexrayArTpChannel":
        """
        Set timeoutAr and return self for chaining.

        Args:
            value: The timeoutAr to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_timeout_ar("value")
        """
        self.timeout_ar = value  # Use property setter (gets validation)
        return self

    def with_timeout_as(self, value: Optional["TimeValue"]) -> "FlexrayArTpChannel":
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

    def with_timeout_bs(self, value: Optional["TimeValue"]) -> "FlexrayArTpChannel":
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

    def with_timeout_cr(self, value: Optional["TimeValue"]) -> "FlexrayArTpChannel":
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
