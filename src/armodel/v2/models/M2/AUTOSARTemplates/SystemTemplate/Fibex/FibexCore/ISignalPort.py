from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommConnectorPort


class ISignalPort(CommConnectorPort):
    """
    Connectors reception or send port on the referenced channel referenced by an
    ISignalTriggering. If different timeouts or DataFilters for ISignals need to
    be specified several ISignalPorts may be created.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::ISignalPort

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 305, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Optional specification of a signal COM filter at the in case that the System
        # Description doesn’t complete Software Component Description (VFB supports the
        # inclusion of legacy system a full DataMapping exist for the SystemSignal may
        # be available from a configured this case the ReceiverComSpec optional
        # specification.
        self._dataFilter: Optional["DataFilter"] = None

    @property
    def data_filter(self) -> Optional["DataFilter"]:
        """Get dataFilter (Pythonic accessor)."""
        return self._dataFilter

    @data_filter.setter
    def data_filter(self, value: Optional["DataFilter"]) -> None:
        """
        Set dataFilter with validation.

        Args:
            value: The dataFilter to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataFilter = None
            return

        if not isinstance(value, DataFilter):
            raise TypeError(
                f"dataFilter must be DataFilter or None, got {type(value).__name__}"
            )
        self._dataFilter = value
        # Reference to the DDS Qos profile used for this ISignal.
        self._ddsQosProfile: Optional["DdsCpQosProfile"] = None

    @property
    def dds_qos_profile(self) -> Optional["DdsCpQosProfile"]:
        """Get ddsQosProfile (Pythonic accessor)."""
        return self._ddsQosProfile

    @dds_qos_profile.setter
    def dds_qos_profile(self, value: Optional["DdsCpQosProfile"]) -> None:
        """
        Set ddsQosProfile with validation.

        Args:
            value: The ddsQosProfile to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ddsQosProfile = None
            return

        if not isinstance(value, DdsCpQosProfile):
            raise TypeError(
                f"ddsQosProfile must be DdsCpQosProfile or None, got {type(value).__name__}"
            )
        self._ddsQosProfile = value
        # • ISignalPort with communicationDirection = in: timeout value in seconds for
        # the reception of with communicationDirection = out: timeout value in seconds
        # for transmission.
        self._firstTimeout: Optional["TimeValue"] = None

    @property
    def first_timeout(self) -> Optional["TimeValue"]:
        """Get firstTimeout (Pythonic accessor)."""
        return self._firstTimeout

    @first_timeout.setter
    def first_timeout(self, value: Optional["TimeValue"]) -> None:
        """
        Set firstTimeout with validation.

        Args:
            value: The firstTimeout to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._firstTimeout = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"firstTimeout must be TimeValue or None, got {type(value).__name__}"
            )
        self._firstTimeout = value
        # This attribute defines how invalidation is applied to the in the context of
                # this ISignalPort.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._handleInvalid: Optional["HandleInvalidEnum"] = None

    @property
    def handle_invalid(self) -> Optional["HandleInvalidEnum"]:
        """Get handleInvalid (Pythonic accessor)."""
        return self._handleInvalid

    @handle_invalid.setter
    def handle_invalid(self, value: Optional["HandleInvalidEnum"]) -> None:
        """
        Set handleInvalid with validation.

        Args:
            value: The handleInvalid to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._handleInvalid = None
            return

        if not isinstance(value, HandleInvalidEnum):
            raise TypeError(
                f"handleInvalid must be HandleInvalidEnum or None, got {type(value).__name__}"
            )
        self._handleInvalid = value
        # • ISignalPort with communicationDirection = in: value in seconds for the
                # reception of the attribute value is used to configure the Com the COM module.
        # The RTE ignores this timeout can also be specified with the If a exists for
                # the SystemSignal and the available in the configured ReceiverComSpec, timeout
                # value in the ReceiverComSpec overrides timeout specification during the
                # creation of Ecu Configuration of the COM module.
        # with communicationDirection = out: value in seconds for the transmission of
                # The attribute value is used to configure the the COM module.
        # The RTE ignores this timeout can also be specified with the ender If
                # DataMapping exists for the SystemSignal and the available in the configured
                # SenderComSpec, then value in the SenderComSpec overrides this specification
                # during the creation of the can be used in the following cases: signal where
                # the System Description doesn’t complete Software Component Description (VFB
                # where the DataMapping is missing.
        # monitoring use cases in which the DataMapping is.
        self._timeout: Optional["TimeValue"] = None

    @property
    def timeout(self) -> Optional["TimeValue"]:
        """Get timeout (Pythonic accessor)."""
        return self._timeout

    @timeout.setter
    def timeout(self, value: Optional["TimeValue"]) -> None:
        """
        Set timeout with validation.

        Args:
            value: The timeout to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeout = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeout must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeout = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataFilter(self) -> "DataFilter":
        """
        AUTOSAR-compliant getter for dataFilter.

        Returns:
            The dataFilter value

        Note:
            Delegates to data_filter property (CODING_RULE_V2_00017)
        """
        return self.data_filter  # Delegates to property

    def setDataFilter(self, value: "DataFilter") -> "ISignalPort":
        """
        AUTOSAR-compliant setter for dataFilter with method chaining.

        Args:
            value: The dataFilter to set

        Returns:
            self for method chaining

        Note:
            Delegates to data_filter property setter (gets validation automatically)
        """
        self.data_filter = value  # Delegates to property setter
        return self

    def getDdsQosProfile(self) -> "DdsCpQosProfile":
        """
        AUTOSAR-compliant getter for ddsQosProfile.

        Returns:
            The ddsQosProfile value

        Note:
            Delegates to dds_qos_profile property (CODING_RULE_V2_00017)
        """
        return self.dds_qos_profile  # Delegates to property

    def setDdsQosProfile(self, value: "DdsCpQosProfile") -> "ISignalPort":
        """
        AUTOSAR-compliant setter for ddsQosProfile with method chaining.

        Args:
            value: The ddsQosProfile to set

        Returns:
            self for method chaining

        Note:
            Delegates to dds_qos_profile property setter (gets validation automatically)
        """
        self.dds_qos_profile = value  # Delegates to property setter
        return self

    def getFirstTimeout(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for firstTimeout.

        Returns:
            The firstTimeout value

        Note:
            Delegates to first_timeout property (CODING_RULE_V2_00017)
        """
        return self.first_timeout  # Delegates to property

    def setFirstTimeout(self, value: "TimeValue") -> "ISignalPort":
        """
        AUTOSAR-compliant setter for firstTimeout with method chaining.

        Args:
            value: The firstTimeout to set

        Returns:
            self for method chaining

        Note:
            Delegates to first_timeout property setter (gets validation automatically)
        """
        self.first_timeout = value  # Delegates to property setter
        return self

    def getHandleInvalid(self) -> "HandleInvalidEnum":
        """
        AUTOSAR-compliant getter for handleInvalid.

        Returns:
            The handleInvalid value

        Note:
            Delegates to handle_invalid property (CODING_RULE_V2_00017)
        """
        return self.handle_invalid  # Delegates to property

    def setHandleInvalid(self, value: "HandleInvalidEnum") -> "ISignalPort":
        """
        AUTOSAR-compliant setter for handleInvalid with method chaining.

        Args:
            value: The handleInvalid to set

        Returns:
            self for method chaining

        Note:
            Delegates to handle_invalid property setter (gets validation automatically)
        """
        self.handle_invalid = value  # Delegates to property setter
        return self

    def getTimeout(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for timeout.

        Returns:
            The timeout value

        Note:
            Delegates to timeout property (CODING_RULE_V2_00017)
        """
        return self.timeout  # Delegates to property

    def setTimeout(self, value: "TimeValue") -> "ISignalPort":
        """
        AUTOSAR-compliant setter for timeout with method chaining.

        Args:
            value: The timeout to set

        Returns:
            self for method chaining

        Note:
            Delegates to timeout property setter (gets validation automatically)
        """
        self.timeout = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_filter(self, value: Optional["DataFilter"]) -> "ISignalPort":
        """
        Set dataFilter and return self for chaining.

        Args:
            value: The dataFilter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_filter("value")
        """
        self.data_filter = value  # Use property setter (gets validation)
        return self

    def with_dds_qos_profile(self, value: Optional["DdsCpQosProfile"]) -> "ISignalPort":
        """
        Set ddsQosProfile and return self for chaining.

        Args:
            value: The ddsQosProfile to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dds_qos_profile("value")
        """
        self.dds_qos_profile = value  # Use property setter (gets validation)
        return self

    def with_first_timeout(self, value: Optional["TimeValue"]) -> "ISignalPort":
        """
        Set firstTimeout and return self for chaining.

        Args:
            value: The firstTimeout to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_first_timeout("value")
        """
        self.first_timeout = value  # Use property setter (gets validation)
        return self

    def with_handle_invalid(self, value: Optional["HandleInvalidEnum"]) -> "ISignalPort":
        """
        Set handleInvalid and return self for chaining.

        Args:
            value: The handleInvalid to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_handle_invalid("value")
        """
        self.handle_invalid = value  # Use property setter (gets validation)
        return self

    def with_timeout(self, value: Optional["TimeValue"]) -> "ISignalPort":
        """
        Set timeout and return self for chaining.

        Args:
            value: The timeout to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_timeout("value")
        """
        self.timeout = value  # Use property setter (gets validation)
        return self
