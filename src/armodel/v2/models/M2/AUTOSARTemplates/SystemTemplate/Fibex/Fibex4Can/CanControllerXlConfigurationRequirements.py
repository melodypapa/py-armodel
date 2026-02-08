from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class CanControllerXlConfigurationRequirements(ARObject):
    """
    This element allows the specification of ranges for the CAN XL configuration
    parameters. These ranges are taken as requirements and have to be respected
    by the ECU developer.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanTopology

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 71, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies if error signaling shall be enabled.
        # This is not when the transceiver is switched to PWM mode to TRUE).
        # signaling shall be enabled.
        # signaling shall be disabled.
        self._errorSignaling: Optional["Boolean"] = None

    @property
    def error_signaling(self) -> Optional["Boolean"]:
        """Get errorSignaling (Pythonic accessor)."""
        return self._errorSignaling

    @error_signaling.setter
    def error_signaling(self, value: Optional["Boolean"]) -> None:
        """
        Set errorSignaling with validation.

        Args:
            value: The errorSignaling to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._errorSignaling = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"errorSignaling must be Boolean or None, got {type(value).__name__}"
            )
        self._errorSignaling = value
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
        # Specifies the maximum PWM long phase length.
        self._maxPwmL: Optional["PositiveInteger"] = None

    @property
    def max_pwm_l(self) -> Optional["PositiveInteger"]:
        """Get maxPwmL (Pythonic accessor)."""
        return self._maxPwmL

    @max_pwm_l.setter
    def max_pwm_l(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxPwmL with validation.

        Args:
            value: The maxPwmL to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxPwmL = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"maxPwmL must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._maxPwmL = value
        # Specifies the minimum PWM time offset.
        self._maxPwmO: Optional["PositiveInteger"] = None

    @property
    def max_pwm_o(self) -> Optional["PositiveInteger"]:
        """Get maxPwmO (Pythonic accessor)."""
        return self._maxPwmO

    @max_pwm_o.setter
    def max_pwm_o(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxPwmO with validation.

        Args:
            value: The maxPwmO to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxPwmO = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"maxPwmO must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._maxPwmO = value
        # Specifies the maximum PWM short phase length.
        self._maxPwmS: Optional["PositiveInteger"] = None

    @property
    def max_pwm_s(self) -> Optional["PositiveInteger"]:
        """Get maxPwmS (Pythonic accessor)."""
        return self._maxPwmS

    @max_pwm_s.setter
    def max_pwm_s(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxPwmS with validation.

        Args:
            value: The maxPwmS to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxPwmS = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"maxPwmS must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._maxPwmS = value
        # The max.
        # value of the sample point as a percentage of total bit time.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
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
        # Specifies the minimum PWM long phase length.
        self._minPwmL: Optional["PositiveInteger"] = None

    @property
    def min_pwm_l(self) -> Optional["PositiveInteger"]:
        """Get minPwmL (Pythonic accessor)."""
        return self._minPwmL

    @min_pwm_l.setter
    def min_pwm_l(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set minPwmL with validation.

        Args:
            value: The minPwmL to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minPwmL = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"minPwmL must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._minPwmL = value
        # Specifies the maximum PWM time offset.
        self._minPwmO: Optional["PositiveInteger"] = None

    @property
    def min_pwm_o(self) -> Optional["PositiveInteger"]:
        """Get minPwmO (Pythonic accessor)."""
        return self._minPwmO

    @min_pwm_o.setter
    def min_pwm_o(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set minPwmO with validation.

        Args:
            value: The minPwmO to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minPwmO = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"minPwmO must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._minPwmO = value
        # Specifies the minimum PWM short phase length.
        self._minPwmS: Optional["PositiveInteger"] = None

    @property
    def min_pwm_s(self) -> Optional["PositiveInteger"]:
        """Get minPwmS (Pythonic accessor)."""
        return self._minPwmS

    @min_pwm_s.setter
    def min_pwm_s(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set minPwmS with validation.

        Args:
            value: The minPwmS to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minPwmS = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"minPwmS must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._minPwmS = value
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
        # Specifies if the transceiver shall be set to the PWM mode.
        # The transceiver shall be switched to PWM mode.
        # transceiver shall work in classic CAN mode.
        self._trcvPwmMode: Optional["Boolean"] = None

    @property
    def trcv_pwm_mode(self) -> Optional["Boolean"]:
        """Get trcvPwmMode (Pythonic accessor)."""
        return self._trcvPwmMode

    @trcv_pwm_mode.setter
    def trcv_pwm_mode(self, value: Optional["Boolean"]) -> None:
        """
        Set trcvPwmMode with validation.

        Args:
            value: The trcvPwmMode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._trcvPwmMode = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"trcvPwmMode must be Boolean or None, got {type(value).__name__}"
            )
        self._trcvPwmMode = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getErrorSignaling(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for errorSignaling.

        Returns:
            The errorSignaling value

        Note:
            Delegates to error_signaling property (CODING_RULE_V2_00017)
        """
        return self.error_signaling  # Delegates to property

    def setErrorSignaling(self, value: "Boolean") -> "CanControllerXlConfigurationRequirements":
        """
        AUTOSAR-compliant setter for errorSignaling with method chaining.

        Args:
            value: The errorSignaling to set

        Returns:
            self for method chaining

        Note:
            Delegates to error_signaling property setter (gets validation automatically)
        """
        self.error_signaling = value  # Delegates to property setter
        return self

    def getMaxNumberOfTimeQuantaPerBit(self) -> "Integer":
        """
        AUTOSAR-compliant getter for maxNumberOfTimeQuantaPerBit.

        Returns:
            The maxNumberOfTimeQuantaPerBit value

        Note:
            Delegates to max_number_of_time_quanta_per_bit property (CODING_RULE_V2_00017)
        """
        return self.max_number_of_time_quanta_per_bit  # Delegates to property

    def setMaxNumberOfTimeQuantaPerBit(self, value: "Integer") -> "CanControllerXlConfigurationRequirements":
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

    def getMaxPwmL(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxPwmL.

        Returns:
            The maxPwmL value

        Note:
            Delegates to max_pwm_l property (CODING_RULE_V2_00017)
        """
        return self.max_pwm_l  # Delegates to property

    def setMaxPwmL(self, value: "PositiveInteger") -> "CanControllerXlConfigurationRequirements":
        """
        AUTOSAR-compliant setter for maxPwmL with method chaining.

        Args:
            value: The maxPwmL to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_pwm_l property setter (gets validation automatically)
        """
        self.max_pwm_l = value  # Delegates to property setter
        return self

    def getMaxPwmO(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxPwmO.

        Returns:
            The maxPwmO value

        Note:
            Delegates to max_pwm_o property (CODING_RULE_V2_00017)
        """
        return self.max_pwm_o  # Delegates to property

    def setMaxPwmO(self, value: "PositiveInteger") -> "CanControllerXlConfigurationRequirements":
        """
        AUTOSAR-compliant setter for maxPwmO with method chaining.

        Args:
            value: The maxPwmO to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_pwm_o property setter (gets validation automatically)
        """
        self.max_pwm_o = value  # Delegates to property setter
        return self

    def getMaxPwmS(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxPwmS.

        Returns:
            The maxPwmS value

        Note:
            Delegates to max_pwm_s property (CODING_RULE_V2_00017)
        """
        return self.max_pwm_s  # Delegates to property

    def setMaxPwmS(self, value: "PositiveInteger") -> "CanControllerXlConfigurationRequirements":
        """
        AUTOSAR-compliant setter for maxPwmS with method chaining.

        Args:
            value: The maxPwmS to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_pwm_s property setter (gets validation automatically)
        """
        self.max_pwm_s = value  # Delegates to property setter
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

    def setMaxSample(self, value: "Float") -> "CanControllerXlConfigurationRequirements":
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

    def setMaxSyncJump(self, value: "Float") -> "CanControllerXlConfigurationRequirements":
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

    def setMaxTrcvDelay(self, value: "TimeValue") -> "CanControllerXlConfigurationRequirements":
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

    def setMinNumberOfTimeQuantaPerBit(self, value: "Integer") -> "CanControllerXlConfigurationRequirements":
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

    def getMinPwmL(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for minPwmL.

        Returns:
            The minPwmL value

        Note:
            Delegates to min_pwm_l property (CODING_RULE_V2_00017)
        """
        return self.min_pwm_l  # Delegates to property

    def setMinPwmL(self, value: "PositiveInteger") -> "CanControllerXlConfigurationRequirements":
        """
        AUTOSAR-compliant setter for minPwmL with method chaining.

        Args:
            value: The minPwmL to set

        Returns:
            self for method chaining

        Note:
            Delegates to min_pwm_l property setter (gets validation automatically)
        """
        self.min_pwm_l = value  # Delegates to property setter
        return self

    def getMinPwmO(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for minPwmO.

        Returns:
            The minPwmO value

        Note:
            Delegates to min_pwm_o property (CODING_RULE_V2_00017)
        """
        return self.min_pwm_o  # Delegates to property

    def setMinPwmO(self, value: "PositiveInteger") -> "CanControllerXlConfigurationRequirements":
        """
        AUTOSAR-compliant setter for minPwmO with method chaining.

        Args:
            value: The minPwmO to set

        Returns:
            self for method chaining

        Note:
            Delegates to min_pwm_o property setter (gets validation automatically)
        """
        self.min_pwm_o = value  # Delegates to property setter
        return self

    def getMinPwmS(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for minPwmS.

        Returns:
            The minPwmS value

        Note:
            Delegates to min_pwm_s property (CODING_RULE_V2_00017)
        """
        return self.min_pwm_s  # Delegates to property

    def setMinPwmS(self, value: "PositiveInteger") -> "CanControllerXlConfigurationRequirements":
        """
        AUTOSAR-compliant setter for minPwmS with method chaining.

        Args:
            value: The minPwmS to set

        Returns:
            self for method chaining

        Note:
            Delegates to min_pwm_s property setter (gets validation automatically)
        """
        self.min_pwm_s = value  # Delegates to property setter
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

    def setMinSamplePoint(self, value: "Float") -> "CanControllerXlConfigurationRequirements":
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

    def setMinSyncJump(self, value: "Float") -> "CanControllerXlConfigurationRequirements":
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

    def setMinTrcvDelay(self, value: "TimeValue") -> "CanControllerXlConfigurationRequirements":
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

    def getTrcvPwmMode(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for trcvPwmMode.

        Returns:
            The trcvPwmMode value

        Note:
            Delegates to trcv_pwm_mode property (CODING_RULE_V2_00017)
        """
        return self.trcv_pwm_mode  # Delegates to property

    def setTrcvPwmMode(self, value: "Boolean") -> "CanControllerXlConfigurationRequirements":
        """
        AUTOSAR-compliant setter for trcvPwmMode with method chaining.

        Args:
            value: The trcvPwmMode to set

        Returns:
            self for method chaining

        Note:
            Delegates to trcv_pwm_mode property setter (gets validation automatically)
        """
        self.trcv_pwm_mode = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_error_signaling(self, value: Optional["Boolean"]) -> "CanControllerXlConfigurationRequirements":
        """
        Set errorSignaling and return self for chaining.

        Args:
            value: The errorSignaling to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_error_signaling("value")
        """
        self.error_signaling = value  # Use property setter (gets validation)
        return self

    def with_max_number_of_time_quanta_per_bit(self, value: Optional["Integer"]) -> "CanControllerXlConfigurationRequirements":
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

    def with_max_pwm_l(self, value: Optional["PositiveInteger"]) -> "CanControllerXlConfigurationRequirements":
        """
        Set maxPwmL and return self for chaining.

        Args:
            value: The maxPwmL to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_pwm_l("value")
        """
        self.max_pwm_l = value  # Use property setter (gets validation)
        return self

    def with_max_pwm_o(self, value: Optional["PositiveInteger"]) -> "CanControllerXlConfigurationRequirements":
        """
        Set maxPwmO and return self for chaining.

        Args:
            value: The maxPwmO to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_pwm_o("value")
        """
        self.max_pwm_o = value  # Use property setter (gets validation)
        return self

    def with_max_pwm_s(self, value: Optional["PositiveInteger"]) -> "CanControllerXlConfigurationRequirements":
        """
        Set maxPwmS and return self for chaining.

        Args:
            value: The maxPwmS to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_pwm_s("value")
        """
        self.max_pwm_s = value  # Use property setter (gets validation)
        return self

    def with_max_sample(self, value: Optional["Float"]) -> "CanControllerXlConfigurationRequirements":
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

    def with_max_sync_jump(self, value: Optional["Float"]) -> "CanControllerXlConfigurationRequirements":
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

    def with_max_trcv_delay(self, value: Optional["TimeValue"]) -> "CanControllerXlConfigurationRequirements":
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

    def with_min_number_of_time_quanta_per_bit(self, value: Optional["Integer"]) -> "CanControllerXlConfigurationRequirements":
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

    def with_min_pwm_l(self, value: Optional["PositiveInteger"]) -> "CanControllerXlConfigurationRequirements":
        """
        Set minPwmL and return self for chaining.

        Args:
            value: The minPwmL to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_min_pwm_l("value")
        """
        self.min_pwm_l = value  # Use property setter (gets validation)
        return self

    def with_min_pwm_o(self, value: Optional["PositiveInteger"]) -> "CanControllerXlConfigurationRequirements":
        """
        Set minPwmO and return self for chaining.

        Args:
            value: The minPwmO to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_min_pwm_o("value")
        """
        self.min_pwm_o = value  # Use property setter (gets validation)
        return self

    def with_min_pwm_s(self, value: Optional["PositiveInteger"]) -> "CanControllerXlConfigurationRequirements":
        """
        Set minPwmS and return self for chaining.

        Args:
            value: The minPwmS to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_min_pwm_s("value")
        """
        self.min_pwm_s = value  # Use property setter (gets validation)
        return self

    def with_min_sample_point(self, value: Optional["Float"]) -> "CanControllerXlConfigurationRequirements":
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

    def with_min_sync_jump(self, value: Optional["Float"]) -> "CanControllerXlConfigurationRequirements":
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

    def with_min_trcv_delay(self, value: Optional["TimeValue"]) -> "CanControllerXlConfigurationRequirements":
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

    def with_trcv_pwm_mode(self, value: Optional["Boolean"]) -> "CanControllerXlConfigurationRequirements":
        """
        Set trcvPwmMode and return self for chaining.

        Args:
            value: The trcvPwmMode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_trcv_pwm_mode("value")
        """
        self.trcv_pwm_mode = value  # Use property setter (gets validation)
        return self
