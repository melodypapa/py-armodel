from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class CanControllerFdConfigurationRequirements(ARObject):
    """
    This element allows the specification of ranges for the CanFD bit timing
    configuration parameters. These ranges are taken as requirements and shall
    be respected by the ECU developer.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanTopology

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 66, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Maximum number of time quanta in the bit time.
        self._maxNumberOfTimeQuantaPerBit: Optional["Integer"] = None

    @property
    def max_number_of_time_quanta_per_bit(self) -> Optional["Integer"]:
        """Get maxNumberOfTimeQuantaPerBit (Pythonic accessor)."""
        return self._maxNumberOfTimeQuantaPerBit

    @max_number_of_time_quanta_per_bit.setter
    def max_number_of_time_quanta_per_bit(self, value: Optional["Integer"]) -> None:
        """
        Set maxNumberOfTimeQuantaPerBit with validation.

        Args:
            value: The maxNumberOfTimeQuantaPerBit to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxNumberOfTimeQuantaPerBit = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"maxNumberOfTimeQuantaPerBit must be Integer or None, got {type(value).__name__}"
            )
        self._maxNumberOfTimeQuantaPerBit = value
        # The max.
        # value of the sample point as a percentage of total bit time.
        self._maxSample: Optional["Float"] = None

    @property
    def max_sample(self) -> Optional["Float"]:
        """Get maxSample (Pythonic accessor)."""
        return self._maxSample

    @max_sample.setter
    def max_sample(self, value: Optional["Float"]) -> None:
        """
        Set maxSample with validation.

        Args:
            value: The maxSample to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxSample = None
            return

        if not isinstance(value, Float):
            raise TypeError(
                f"maxSample must be Float or None, got {type(value).__name__}"
            )
        self._maxSample = value
        # The max.
        # Synchronization Jump Width value as a of the total bit time.
        # The (Re-)Synchronization (SJW) defines how far a resynchronization the Sample
                # Point inside the limits defined by Buffer Segments to compensate for edge.
        self._maxSyncJump: Optional["Float"] = None

    @property
    def max_sync_jump(self) -> Optional["Float"]:
        """Get maxSyncJump (Pythonic accessor)."""
        return self._maxSyncJump

    @max_sync_jump.setter
    def max_sync_jump(self, value: Optional["Float"]) -> None:
        """
        Set maxSyncJump with validation.

        Args:
            value: The maxSyncJump to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxSyncJump = None
            return

        if not isinstance(value, Float):
            raise TypeError(
                f"maxSyncJump must be Float or None, got {type(value).__name__}"
            )
        self._maxSyncJump = value
        # Specifies the maximum Transceiver Delay Compensation in seconds.
        # If not specified Transceiver Delay is disabled.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._maxTrcvDelay: Optional["TimeValue"] = None

    @property
    def max_trcv_delay(self) -> Optional["TimeValue"]:
        """Get maxTrcvDelay (Pythonic accessor)."""
        return self._maxTrcvDelay

    @max_trcv_delay.setter
    def max_trcv_delay(self, value: Optional["TimeValue"]) -> None:
        """
        Set maxTrcvDelay with validation.

        Args:
            value: The maxTrcvDelay to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxTrcvDelay = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"maxTrcvDelay must be TimeValue or None, got {type(value).__name__}"
            )
        self._maxTrcvDelay = value
        # Minimum number of time quanta in the bit time.
        self._minNumberOfTimeQuantaPerBit: Optional["Integer"] = None

    @property
    def min_number_of_time_quanta_per_bit(self) -> Optional["Integer"]:
        """Get minNumberOfTimeQuantaPerBit (Pythonic accessor)."""
        return self._minNumberOfTimeQuantaPerBit

    @min_number_of_time_quanta_per_bit.setter
    def min_number_of_time_quanta_per_bit(self, value: Optional["Integer"]) -> None:
        """
        Set minNumberOfTimeQuantaPerBit with validation.

        Args:
            value: The minNumberOfTimeQuantaPerBit to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minNumberOfTimeQuantaPerBit = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"minNumberOfTimeQuantaPerBit must be Integer or None, got {type(value).__name__}"
            )
        self._minNumberOfTimeQuantaPerBit = value
        # The min.
        # value of the sample point as a percentage of the time.
        self._minSamplePoint: Optional["Float"] = None

    @property
    def min_sample_point(self) -> Optional["Float"]:
        """Get minSamplePoint (Pythonic accessor)."""
        return self._minSamplePoint

    @min_sample_point.setter
    def min_sample_point(self, value: Optional["Float"]) -> None:
        """
        Set minSamplePoint with validation.

        Args:
            value: The minSamplePoint to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minSamplePoint = None
            return

        if not isinstance(value, Float):
            raise TypeError(
                f"minSamplePoint must be Float or None, got {type(value).__name__}"
            )
        self._minSamplePoint = value
        # The min.
        # Synchronization Jump Width value as a of the total bit time.
        # The (Re-)Synchronization (SJW) defines how far a resynchronization the Sample
                # Point inside the limits defined by Buffer Segments to compensate for edge.
        self._minSyncJump: Optional["Float"] = None

    @property
    def min_sync_jump(self) -> Optional["Float"]:
        """Get minSyncJump (Pythonic accessor)."""
        return self._minSyncJump

    @min_sync_jump.setter
    def min_sync_jump(self, value: Optional["Float"]) -> None:
        """
        Set minSyncJump with validation.

        Args:
            value: The minSyncJump to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minSyncJump = None
            return

        if not isinstance(value, Float):
            raise TypeError(
                f"minSyncJump must be Float or None, got {type(value).__name__}"
            )
        self._minSyncJump = value
        # Specifies the minimum Transceiver Delay Compensation in seconds.
        # If not specified Transceiver Delay is disabled.
        self._minTrcvDelay: Optional["TimeValue"] = None

    @property
    def min_trcv_delay(self) -> Optional["TimeValue"]:
        """Get minTrcvDelay (Pythonic accessor)."""
        return self._minTrcvDelay

    @min_trcv_delay.setter
    def min_trcv_delay(self, value: Optional["TimeValue"]) -> None:
        """
        Set minTrcvDelay with validation.

        Args:
            value: The minTrcvDelay to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minTrcvDelay = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"minTrcvDelay must be TimeValue or None, got {type(value).__name__}"
            )
        self._minTrcvDelay = value
        # Specifies the value which is used to pad unused data in frames which are
        # bigger than 8 byte if the length Pdu which was requested to be sent does not
        # match DLC values of CAN FD.
        self._paddingValue: Optional["PositiveInteger"] = None

    @property
    def padding_value(self) -> Optional["PositiveInteger"]:
        """Get paddingValue (Pythonic accessor)."""
        return self._paddingValue

    @padding_value.setter
    def padding_value(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set paddingValue with validation.

        Args:
            value: The paddingValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._paddingValue = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"paddingValue must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._paddingValue = value
        # Specifies if the bit rate switching shall be used for FD frames shall be sent
        # with bit rate FD frames shall be sent without bit rate.
        self._txBitRateSwitch: Optional["Boolean"] = None

    @property
    def tx_bit_rate_switch(self) -> Optional["Boolean"]:
        """Get txBitRateSwitch (Pythonic accessor)."""
        return self._txBitRateSwitch

    @tx_bit_rate_switch.setter
    def tx_bit_rate_switch(self, value: Optional["Boolean"]) -> None:
        """
        Set txBitRateSwitch with validation.

        Args:
            value: The txBitRateSwitch to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._txBitRateSwitch = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"txBitRateSwitch must be Boolean or None, got {type(value).__name__}"
            )
        self._txBitRateSwitch = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMaxNumberOfTimeQuantaPerBit(self) -> "Integer":
        """
        AUTOSAR-compliant getter for maxNumberOfTimeQuantaPerBit.

        Returns:
            The maxNumberOfTimeQuantaPerBit value

        Note:
            Delegates to max_number_of_time_quanta_per_bit property (CODING_RULE_V2_00017)
        """
        return self.max_number_of_time_quanta_per_bit  # Delegates to property

    def setMaxNumberOfTimeQuantaPerBit(self, value: "Integer") -> "CanControllerFdConfigurationRequirements":
        """
        AUTOSAR-compliant setter for maxNumberOfTimeQuantaPerBit with method chaining.

        Args:
            value: The maxNumberOfTimeQuantaPerBit to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_number_of_time_quanta_per_bit property setter (gets validation automatically)
        """
        self.max_number_of_time_quanta_per_bit = value  # Delegates to property setter
        return self

    def getMaxSample(self) -> "Float":
        """
        AUTOSAR-compliant getter for maxSample.

        Returns:
            The maxSample value

        Note:
            Delegates to max_sample property (CODING_RULE_V2_00017)
        """
        return self.max_sample  # Delegates to property

    def setMaxSample(self, value: "Float") -> "CanControllerFdConfigurationRequirements":
        """
        AUTOSAR-compliant setter for maxSample with method chaining.

        Args:
            value: The maxSample to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_sample property setter (gets validation automatically)
        """
        self.max_sample = value  # Delegates to property setter
        return self

    def getMaxSyncJump(self) -> "Float":
        """
        AUTOSAR-compliant getter for maxSyncJump.

        Returns:
            The maxSyncJump value

        Note:
            Delegates to max_sync_jump property (CODING_RULE_V2_00017)
        """
        return self.max_sync_jump  # Delegates to property

    def setMaxSyncJump(self, value: "Float") -> "CanControllerFdConfigurationRequirements":
        """
        AUTOSAR-compliant setter for maxSyncJump with method chaining.

        Args:
            value: The maxSyncJump to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_sync_jump property setter (gets validation automatically)
        """
        self.max_sync_jump = value  # Delegates to property setter
        return self

    def getMaxTrcvDelay(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for maxTrcvDelay.

        Returns:
            The maxTrcvDelay value

        Note:
            Delegates to max_trcv_delay property (CODING_RULE_V2_00017)
        """
        return self.max_trcv_delay  # Delegates to property

    def setMaxTrcvDelay(self, value: "TimeValue") -> "CanControllerFdConfigurationRequirements":
        """
        AUTOSAR-compliant setter for maxTrcvDelay with method chaining.

        Args:
            value: The maxTrcvDelay to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_trcv_delay property setter (gets validation automatically)
        """
        self.max_trcv_delay = value  # Delegates to property setter
        return self

    def getMinNumberOfTimeQuantaPerBit(self) -> "Integer":
        """
        AUTOSAR-compliant getter for minNumberOfTimeQuantaPerBit.

        Returns:
            The minNumberOfTimeQuantaPerBit value

        Note:
            Delegates to min_number_of_time_quanta_per_bit property (CODING_RULE_V2_00017)
        """
        return self.min_number_of_time_quanta_per_bit  # Delegates to property

    def setMinNumberOfTimeQuantaPerBit(self, value: "Integer") -> "CanControllerFdConfigurationRequirements":
        """
        AUTOSAR-compliant setter for minNumberOfTimeQuantaPerBit with method chaining.

        Args:
            value: The minNumberOfTimeQuantaPerBit to set

        Returns:
            self for method chaining

        Note:
            Delegates to min_number_of_time_quanta_per_bit property setter (gets validation automatically)
        """
        self.min_number_of_time_quanta_per_bit = value  # Delegates to property setter
        return self

    def getMinSamplePoint(self) -> "Float":
        """
        AUTOSAR-compliant getter for minSamplePoint.

        Returns:
            The minSamplePoint value

        Note:
            Delegates to min_sample_point property (CODING_RULE_V2_00017)
        """
        return self.min_sample_point  # Delegates to property

    def setMinSamplePoint(self, value: "Float") -> "CanControllerFdConfigurationRequirements":
        """
        AUTOSAR-compliant setter for minSamplePoint with method chaining.

        Args:
            value: The minSamplePoint to set

        Returns:
            self for method chaining

        Note:
            Delegates to min_sample_point property setter (gets validation automatically)
        """
        self.min_sample_point = value  # Delegates to property setter
        return self

    def getMinSyncJump(self) -> "Float":
        """
        AUTOSAR-compliant getter for minSyncJump.

        Returns:
            The minSyncJump value

        Note:
            Delegates to min_sync_jump property (CODING_RULE_V2_00017)
        """
        return self.min_sync_jump  # Delegates to property

    def setMinSyncJump(self, value: "Float") -> "CanControllerFdConfigurationRequirements":
        """
        AUTOSAR-compliant setter for minSyncJump with method chaining.

        Args:
            value: The minSyncJump to set

        Returns:
            self for method chaining

        Note:
            Delegates to min_sync_jump property setter (gets validation automatically)
        """
        self.min_sync_jump = value  # Delegates to property setter
        return self

    def getMinTrcvDelay(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for minTrcvDelay.

        Returns:
            The minTrcvDelay value

        Note:
            Delegates to min_trcv_delay property (CODING_RULE_V2_00017)
        """
        return self.min_trcv_delay  # Delegates to property

    def setMinTrcvDelay(self, value: "TimeValue") -> "CanControllerFdConfigurationRequirements":
        """
        AUTOSAR-compliant setter for minTrcvDelay with method chaining.

        Args:
            value: The minTrcvDelay to set

        Returns:
            self for method chaining

        Note:
            Delegates to min_trcv_delay property setter (gets validation automatically)
        """
        self.min_trcv_delay = value  # Delegates to property setter
        return self

    def getPaddingValue(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for paddingValue.

        Returns:
            The paddingValue value

        Note:
            Delegates to padding_value property (CODING_RULE_V2_00017)
        """
        return self.padding_value  # Delegates to property

    def setPaddingValue(self, value: "PositiveInteger") -> "CanControllerFdConfigurationRequirements":
        """
        AUTOSAR-compliant setter for paddingValue with method chaining.

        Args:
            value: The paddingValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to padding_value property setter (gets validation automatically)
        """
        self.padding_value = value  # Delegates to property setter
        return self

    def getTxBitRateSwitch(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for txBitRateSwitch.

        Returns:
            The txBitRateSwitch value

        Note:
            Delegates to tx_bit_rate_switch property (CODING_RULE_V2_00017)
        """
        return self.tx_bit_rate_switch  # Delegates to property

    def setTxBitRateSwitch(self, value: "Boolean") -> "CanControllerFdConfigurationRequirements":
        """
        AUTOSAR-compliant setter for txBitRateSwitch with method chaining.

        Args:
            value: The txBitRateSwitch to set

        Returns:
            self for method chaining

        Note:
            Delegates to tx_bit_rate_switch property setter (gets validation automatically)
        """
        self.tx_bit_rate_switch = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_max_number_of_time_quanta_per_bit(self, value: Optional["Integer"]) -> "CanControllerFdConfigurationRequirements":
        """
        Set maxNumberOfTimeQuantaPerBit and return self for chaining.

        Args:
            value: The maxNumberOfTimeQuantaPerBit to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_number_of_time_quanta_per_bit("value")
        """
        self.max_number_of_time_quanta_per_bit = value  # Use property setter (gets validation)
        return self

    def with_max_sample(self, value: Optional["Float"]) -> "CanControllerFdConfigurationRequirements":
        """
        Set maxSample and return self for chaining.

        Args:
            value: The maxSample to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_sample("value")
        """
        self.max_sample = value  # Use property setter (gets validation)
        return self

    def with_max_sync_jump(self, value: Optional["Float"]) -> "CanControllerFdConfigurationRequirements":
        """
        Set maxSyncJump and return self for chaining.

        Args:
            value: The maxSyncJump to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_sync_jump("value")
        """
        self.max_sync_jump = value  # Use property setter (gets validation)
        return self

    def with_max_trcv_delay(self, value: Optional["TimeValue"]) -> "CanControllerFdConfigurationRequirements":
        """
        Set maxTrcvDelay and return self for chaining.

        Args:
            value: The maxTrcvDelay to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_trcv_delay("value")
        """
        self.max_trcv_delay = value  # Use property setter (gets validation)
        return self

    def with_min_number_of_time_quanta_per_bit(self, value: Optional["Integer"]) -> "CanControllerFdConfigurationRequirements":
        """
        Set minNumberOfTimeQuantaPerBit and return self for chaining.

        Args:
            value: The minNumberOfTimeQuantaPerBit to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_min_number_of_time_quanta_per_bit("value")
        """
        self.min_number_of_time_quanta_per_bit = value  # Use property setter (gets validation)
        return self

    def with_min_sample_point(self, value: Optional["Float"]) -> "CanControllerFdConfigurationRequirements":
        """
        Set minSamplePoint and return self for chaining.

        Args:
            value: The minSamplePoint to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_min_sample_point("value")
        """
        self.min_sample_point = value  # Use property setter (gets validation)
        return self

    def with_min_sync_jump(self, value: Optional["Float"]) -> "CanControllerFdConfigurationRequirements":
        """
        Set minSyncJump and return self for chaining.

        Args:
            value: The minSyncJump to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_min_sync_jump("value")
        """
        self.min_sync_jump = value  # Use property setter (gets validation)
        return self

    def with_min_trcv_delay(self, value: Optional["TimeValue"]) -> "CanControllerFdConfigurationRequirements":
        """
        Set minTrcvDelay and return self for chaining.

        Args:
            value: The minTrcvDelay to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_min_trcv_delay("value")
        """
        self.min_trcv_delay = value  # Use property setter (gets validation)
        return self

    def with_padding_value(self, value: Optional["PositiveInteger"]) -> "CanControllerFdConfigurationRequirements":
        """
        Set paddingValue and return self for chaining.

        Args:
            value: The paddingValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_padding_value("value")
        """
        self.padding_value = value  # Use property setter (gets validation)
        return self

    def with_tx_bit_rate_switch(self, value: Optional["Boolean"]) -> "CanControllerFdConfigurationRequirements":
        """
        Set txBitRateSwitch and return self for chaining.

        Args:
            value: The txBitRateSwitch to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tx_bit_rate_switch("value")
        """
        self.tx_bit_rate_switch = value  # Use property setter (gets validation)
        return self
