from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class FlexrayTpConnectionControl(Identifiable):
    """
    Configuration parameters to control a FlexRay TP connection.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::FlexrayTpConnectionControl

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 593, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This parameter defines the type of acknowledgement used for the specific
        # channel.
        self._ackType: Optional["TpAckType"] = None

    @property
    def ack_type(self) -> Optional["TpAckType"]:
        """Get ackType (Pythonic accessor)."""
        return self._ackType

    @ack_type.setter
    def ack_type(self, value: Optional["TpAckType"]) -> None:
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

        if not isinstance(value, TpAckType):
            raise TypeError(
                f"ackType must be TpAckType or None, got {type(value).__name__}"
            )
        self._ackType = value
        # This attribute defines the maximum number of Flow with FlowState "WAIT".
        self._maxFcWait: Optional["Integer"] = None

    @property
    def max_fc_wait(self) -> Optional["Integer"]:
        """Get maxFcWait (Pythonic accessor)."""
        return self._maxFcWait

    @max_fc_wait.setter
    def max_fc_wait(self, value: Optional["Integer"]) -> None:
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

        if not isinstance(value, Integer):
            raise TypeError(
                f"maxFcWait must be Integer or None, got {type(value).__name__}"
            )
        self._maxFcWait = value
        # This parameter limits the number of N-Pdus the sender is to transmit within a
        # FlexRay cycle.
        self._maxNumberOf: Optional["Integer"] = None

    @property
    def max_number_of(self) -> Optional["Integer"]:
        """Get maxNumberOf (Pythonic accessor)."""
        return self._maxNumberOf

    @max_number_of.setter
    def max_number_of(self, value: Optional["Integer"]) -> None:
        """
        Set maxNumberOf with validation.

        Args:
            value: The maxNumberOf to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxNumberOf = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"maxNumberOf must be Integer or None, got {type(value).__name__}"
            )
        self._maxNumberOf = value
        # This parameter defines the maximum number of retries (if configured for the
        # particular channel).
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
        # Exponent to calculate the minimum number of Cycles" the sender has to wait
        # for the next an FrTp N-Pdu.
        self._separationCycle: Optional["Integer"] = None

    @property
    def separation_cycle(self) -> Optional["Integer"]:
        """Get separationCycle (Pythonic accessor)."""
        return self._separationCycle

    @separation_cycle.setter
    def separation_cycle(self, value: Optional["Integer"]) -> None:
        """
        Set separationCycle with validation.

        Args:
            value: The separationCycle to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._separationCycle = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"separationCycle must be Integer or None, got {type(value).__name__}"
            )
        self._separationCycle = value
        # Time (in seconds) until transmission of the next Flow.
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
        # This parameter defines the time of waiting for the next try a Tx or Rx
                # buffer.
        # is equivalent to the temporal distance FC.
        # WT N-Pdus in case the buffer request seconds.
        self._timeBuffer: Optional["TimeValue"] = None

    @property
    def time_buffer(self) -> Optional["TimeValue"]:
        """Get timeBuffer (Pythonic accessor)."""
        return self._timeBuffer

    @time_buffer.setter
    def time_buffer(self, value: Optional["TimeValue"]) -> None:
        """
        Set timeBuffer with validation.

        Args:
            value: The timeBuffer to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeBuffer = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeBuffer must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeBuffer = value
        # Time (in seconds) until transmission of the next / LastFrame NPdu.
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
        # This parameter states the timeout between the PDU of the Transport Layer to
                # the FlexRay the corresponding confirmation of the Flex on the receiver side
                # (for FC or AF).
        # seconds.
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
        # This attribute states the timeout between the PDU for the first PDU of the
                # group used in the of the Transport Layer to the FlexRay the corresponding
                # confirmation of the Flex (when having sent the last PDU of the in this
                # connection) on the sender side (SF-x, or FC (in case of Transmit
                # Cancellation)).
        # seconds.
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
        # This parameter defines the timeout in seconds for waiting FC or AF on the
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
        # This parameter defines the timeout value in seconds for a CF or FF-x (in case
        # of retry) after receiving CF or after sending an FC or AF on the receiver in
        # seconds.
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

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAckType(self) -> "TpAckType":
        """
        AUTOSAR-compliant getter for ackType.

        Returns:
            The ackType value

        Note:
            Delegates to ack_type property (CODING_RULE_V2_00017)
        """
        return self.ack_type  # Delegates to property

    def setAckType(self, value: "TpAckType") -> "FlexrayTpConnectionControl":
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

    def getMaxFcWait(self) -> "Integer":
        """
        AUTOSAR-compliant getter for maxFcWait.

        Returns:
            The maxFcWait value

        Note:
            Delegates to max_fc_wait property (CODING_RULE_V2_00017)
        """
        return self.max_fc_wait  # Delegates to property

    def setMaxFcWait(self, value: "Integer") -> "FlexrayTpConnectionControl":
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

    def getMaxNumberOf(self) -> "Integer":
        """
        AUTOSAR-compliant getter for maxNumberOf.

        Returns:
            The maxNumberOf value

        Note:
            Delegates to max_number_of property (CODING_RULE_V2_00017)
        """
        return self.max_number_of  # Delegates to property

    def setMaxNumberOf(self, value: "Integer") -> "FlexrayTpConnectionControl":
        """
        AUTOSAR-compliant setter for maxNumberOf with method chaining.

        Args:
            value: The maxNumberOf to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_number_of property setter (gets validation automatically)
        """
        self.max_number_of = value  # Delegates to property setter
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

    def setMaxRetries(self, value: "Integer") -> "FlexrayTpConnectionControl":
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

    def getSeparationCycle(self) -> "Integer":
        """
        AUTOSAR-compliant getter for separationCycle.

        Returns:
            The separationCycle value

        Note:
            Delegates to separation_cycle property (CODING_RULE_V2_00017)
        """
        return self.separation_cycle  # Delegates to property

    def setSeparationCycle(self, value: "Integer") -> "FlexrayTpConnectionControl":
        """
        AUTOSAR-compliant setter for separationCycle with method chaining.

        Args:
            value: The separationCycle to set

        Returns:
            self for method chaining

        Note:
            Delegates to separation_cycle property setter (gets validation automatically)
        """
        self.separation_cycle = value  # Delegates to property setter
        return self

    def getTimeBr(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for timeBr.

        Returns:
            The timeBr value

        Note:
            Delegates to time_br property (CODING_RULE_V2_00017)
        """
        return self.time_br  # Delegates to property

    def setTimeBr(self, value: "TimeValue") -> "FlexrayTpConnectionControl":
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

    def getTimeBuffer(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for timeBuffer.

        Returns:
            The timeBuffer value

        Note:
            Delegates to time_buffer property (CODING_RULE_V2_00017)
        """
        return self.time_buffer  # Delegates to property

    def setTimeBuffer(self, value: "TimeValue") -> "FlexrayTpConnectionControl":
        """
        AUTOSAR-compliant setter for timeBuffer with method chaining.

        Args:
            value: The timeBuffer to set

        Returns:
            self for method chaining

        Note:
            Delegates to time_buffer property setter (gets validation automatically)
        """
        self.time_buffer = value  # Delegates to property setter
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

    def setTimeCs(self, value: "TimeValue") -> "FlexrayTpConnectionControl":
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

    def setTimeoutAr(self, value: "TimeValue") -> "FlexrayTpConnectionControl":
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

    def setTimeoutAs(self, value: "TimeValue") -> "FlexrayTpConnectionControl":
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

    def setTimeoutBs(self, value: "TimeValue") -> "FlexrayTpConnectionControl":
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

    def setTimeoutCr(self, value: "TimeValue") -> "FlexrayTpConnectionControl":
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ack_type(self, value: Optional["TpAckType"]) -> "FlexrayTpConnectionControl":
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

    def with_max_fc_wait(self, value: Optional["Integer"]) -> "FlexrayTpConnectionControl":
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

    def with_max_number_of(self, value: Optional["Integer"]) -> "FlexrayTpConnectionControl":
        """
        Set maxNumberOf and return self for chaining.

        Args:
            value: The maxNumberOf to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_number_of("value")
        """
        self.max_number_of = value  # Use property setter (gets validation)
        return self

    def with_max_retries(self, value: Optional["Integer"]) -> "FlexrayTpConnectionControl":
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

    def with_separation_cycle(self, value: Optional["Integer"]) -> "FlexrayTpConnectionControl":
        """
        Set separationCycle and return self for chaining.

        Args:
            value: The separationCycle to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_separation_cycle("value")
        """
        self.separation_cycle = value  # Use property setter (gets validation)
        return self

    def with_time_br(self, value: Optional["TimeValue"]) -> "FlexrayTpConnectionControl":
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

    def with_time_buffer(self, value: Optional["TimeValue"]) -> "FlexrayTpConnectionControl":
        """
        Set timeBuffer and return self for chaining.

        Args:
            value: The timeBuffer to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_time_buffer("value")
        """
        self.time_buffer = value  # Use property setter (gets validation)
        return self

    def with_time_cs(self, value: Optional["TimeValue"]) -> "FlexrayTpConnectionControl":
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

    def with_timeout_ar(self, value: Optional["TimeValue"]) -> "FlexrayTpConnectionControl":
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

    def with_timeout_as(self, value: Optional["TimeValue"]) -> "FlexrayTpConnectionControl":
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

    def with_timeout_bs(self, value: Optional["TimeValue"]) -> "FlexrayTpConnectionControl":
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

    def with_timeout_cr(self, value: Optional["TimeValue"]) -> "FlexrayTpConnectionControl":
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
