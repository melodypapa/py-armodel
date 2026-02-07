from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class CanTpNode(Identifiable):
    """
    TP Node (Sender or Receiver) provides the TP Address and the connection to
    the Topology description.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::CanTpNode

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 611, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Association to a CommunicationConnector in the description.
        # In a System Description this mandatory.
        # In an ECU Extract this reference (references to ECUs that are not part of the
                # shall be avoided).
        self._connector: Optional["Communication"] = None

    @property
    def connector(self) -> Optional["Communication"]:
        """Get connector (Pythonic accessor)."""
        return self._connector

    @connector.setter
    def connector(self, value: Optional["Communication"]) -> None:
        """
        Set connector with validation.

        Args:
            value: The connector to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._connector = None
            return

        if not isinstance(value, Communication):
            raise TypeError(
                f"connector must be Communication or None, got {type(value).__name__}"
            )
        self._connector = value
        # This attribute defines the maximum number of flow control can be
        # consecutively be transmitted by a.
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
        # Sets the duration of the minimum time the CanTp sender between the
        # transmissions of two CF N-PDUs.
        self._stMin: Optional["TimeValue"] = None

    @property
    def st_min(self) -> Optional["TimeValue"]:
        """Get stMin (Pythonic accessor)."""
        return self._stMin

    @st_min.setter
    def st_min(self, value: Optional["TimeValue"]) -> None:
        """
        Set stMin with validation.

        Args:
            value: The stMin to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._stMin = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"stMin must be TimeValue or None, got {type(value).__name__}"
            )
        self._stMin = value
        # This attribute states the timeout between the PDU of the Transport Layer to
                # the Can the corresponding confirmation of the Can the receiver side (for FC
                # or AF).
        # Specified in.
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
                # group used in the of the Transport Layer to the Can the corresponding
                # confirmation of the Can having sent the last PDU of the group this
                # connection) on the sender side (SF-x, FF-x, FC (in case of Transmit
                # Cancellation)).
        # Specified in.
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
        # Reference to the TP Address that is used by the TpNode.
        # is optional in case that the multicast TP used (reference from TpConnection).
        self._tpAddress: Optional["CanTpAddress"] = None

    @property
    def tp_address(self) -> Optional["CanTpAddress"]:
        """Get tpAddress (Pythonic accessor)."""
        return self._tpAddress

    @tp_address.setter
    def tp_address(self, value: Optional["CanTpAddress"]) -> None:
        """
        Set tpAddress with validation.

        Args:
            value: The tpAddress to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tpAddress = None
            return

        if not isinstance(value, CanTpAddress):
            raise TypeError(
                f"tpAddress must be CanTpAddress or None, got {type(value).__name__}"
            )
        self._tpAddress = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getConnector(self) -> "Communication":
        """
        AUTOSAR-compliant getter for connector.

        Returns:
            The connector value

        Note:
            Delegates to connector property (CODING_RULE_V2_00017)
        """
        return self.connector  # Delegates to property

    def setConnector(self, value: "Communication") -> "CanTpNode":
        """
        AUTOSAR-compliant setter for connector with method chaining.

        Args:
            value: The connector to set

        Returns:
            self for method chaining

        Note:
            Delegates to connector property setter (gets validation automatically)
        """
        self.connector = value  # Delegates to property setter
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

    def setMaxFcWait(self, value: "Integer") -> "CanTpNode":
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

    def getStMin(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for stMin.

        Returns:
            The stMin value

        Note:
            Delegates to st_min property (CODING_RULE_V2_00017)
        """
        return self.st_min  # Delegates to property

    def setStMin(self, value: "TimeValue") -> "CanTpNode":
        """
        AUTOSAR-compliant setter for stMin with method chaining.

        Args:
            value: The stMin to set

        Returns:
            self for method chaining

        Note:
            Delegates to st_min property setter (gets validation automatically)
        """
        self.st_min = value  # Delegates to property setter
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

    def setTimeoutAr(self, value: "TimeValue") -> "CanTpNode":
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

    def setTimeoutAs(self, value: "TimeValue") -> "CanTpNode":
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

    def getTpAddress(self) -> "CanTpAddress":
        """
        AUTOSAR-compliant getter for tpAddress.

        Returns:
            The tpAddress value

        Note:
            Delegates to tp_address property (CODING_RULE_V2_00017)
        """
        return self.tp_address  # Delegates to property

    def setTpAddress(self, value: "CanTpAddress") -> "CanTpNode":
        """
        AUTOSAR-compliant setter for tpAddress with method chaining.

        Args:
            value: The tpAddress to set

        Returns:
            self for method chaining

        Note:
            Delegates to tp_address property setter (gets validation automatically)
        """
        self.tp_address = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_connector(self, value: Optional["Communication"]) -> "CanTpNode":
        """
        Set connector and return self for chaining.

        Args:
            value: The connector to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_connector("value")
        """
        self.connector = value  # Use property setter (gets validation)
        return self

    def with_max_fc_wait(self, value: Optional["Integer"]) -> "CanTpNode":
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

    def with_st_min(self, value: Optional["TimeValue"]) -> "CanTpNode":
        """
        Set stMin and return self for chaining.

        Args:
            value: The stMin to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_st_min("value")
        """
        self.st_min = value  # Use property setter (gets validation)
        return self

    def with_timeout_ar(self, value: Optional["TimeValue"]) -> "CanTpNode":
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

    def with_timeout_as(self, value: Optional["TimeValue"]) -> "CanTpNode":
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

    def with_tp_address(self, value: Optional["CanTpAddress"]) -> "CanTpNode":
        """
        Set tpAddress and return self for chaining.

        Args:
            value: The tpAddress to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tp_address("value")
        """
        self.tp_address = value  # Use property setter (gets validation)
        return self
