from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class CanControllerXlConfiguration(ARObject):
    """
    This meta-class represents the CAN XL-specific controller attributes.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanTopology::CanControllerXlConfiguration
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 70, Classic Platform R23-11)
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
        # Specifies propagation delay in time quantas.
        self._propSeg: Optional["PositiveInteger"] = None

    @property
    def prop_seg(self) -> Optional["PositiveInteger"]:
        """Get propSeg (Pythonic accessor)."""
        return self._propSeg

    @prop_seg.setter
    def prop_seg(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set propSeg with validation.
        
        Args:
            value: The propSeg to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._propSeg = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"propSeg must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._propSeg = value
        # Specifies the PWM long phase length.
        self._pwmL: Optional["PositiveInteger"] = None

    @property
    def pwm_l(self) -> Optional["PositiveInteger"]:
        """Get pwmL (Pythonic accessor)."""
        return self._pwmL

    @pwm_l.setter
    def pwm_l(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set pwmL with validation.
        
        Args:
            value: The pwmL to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pwmL = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"pwmL must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._pwmL = value
        # Specifies the PWM time offset.
        self._pwmO: Optional["PositiveInteger"] = None

    @property
    def pwm_o(self) -> Optional["PositiveInteger"]:
        """Get pwmO (Pythonic accessor)."""
        return self._pwmO

    @pwm_o.setter
    def pwm_o(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set pwmO with validation.
        
        Args:
            value: The pwmO to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pwmO = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"pwmO must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._pwmO = value
        # Specifies the PWM short phase length.
        self._pwmS: Optional["PositiveInteger"] = None

    @property
    def pwm_s(self) -> Optional["PositiveInteger"]:
        """Get pwmS (Pythonic accessor)."""
        return self._pwmS

    @pwm_s.setter
    def pwm_s(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set pwmS with validation.
        
        Args:
            value: The pwmS to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pwmS = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"pwmS must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._pwmS = value
        # Specifies the Transmitter Delay Compensation Offset in quanta.
        # Transmitter Delay Compensation used to adjust the position of the Secondary
                # (SSP), relative to the beginning of the If this parameter is configured, the
                # Compensation is done by the CAN controller.
        # If not specified Compensation is disabled.
        self._sspOffset: Optional["PositiveInteger"] = None

    @property
    def ssp_offset(self) -> Optional["PositiveInteger"]:
        """Get sspOffset (Pythonic accessor)."""
        return self._sspOffset

    @ssp_offset.setter
    def ssp_offset(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set sspOffset with validation.
        
        Args:
            value: The sspOffset to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sspOffset = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"sspOffset must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._sspOffset = value
        # Specifies the synchronization jump width for the controller quantas.
        self._syncJumpWidth: Optional["PositiveInteger"] = None

    @property
    def sync_jump_width(self) -> Optional["PositiveInteger"]:
        """Get syncJumpWidth (Pythonic accessor)."""
        return self._syncJumpWidth

    @sync_jump_width.setter
    def sync_jump_width(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set syncJumpWidth with validation.
        
        Args:
            value: The syncJumpWidth to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._syncJumpWidth = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"syncJumpWidth must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._syncJumpWidth = value
        # Specifies phase segment 1 in time quantas.
        self._timeSeg1: Optional["PositiveInteger"] = None

    @property
    def time_seg1(self) -> Optional["PositiveInteger"]:
        """Get timeSeg1 (Pythonic accessor)."""
        return self._timeSeg1

    @time_seg1.setter
    def time_seg1(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set timeSeg1 with validation.
        
        Args:
            value: The timeSeg1 to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeSeg1 = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"timeSeg1 must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._timeSeg1 = value
        # Specifies phase segment 2 in time quantas.
        self._timeSeg2: Optional["PositiveInteger"] = None

    @property
    def time_seg2(self) -> Optional["PositiveInteger"]:
        """Get timeSeg2 (Pythonic accessor)."""
        return self._timeSeg2

    @time_seg2.setter
    def time_seg2(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set timeSeg2 with validation.
        
        Args:
            value: The timeSeg2 to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeSeg2 = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"timeSeg2 must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._timeSeg2 = value
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

    def setErrorSignaling(self, value: "Boolean") -> "CanControllerXlConfiguration":
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

    def getPropSeg(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for propSeg.
        
        Returns:
            The propSeg value
        
        Note:
            Delegates to prop_seg property (CODING_RULE_V2_00017)
        """
        return self.prop_seg  # Delegates to property

    def setPropSeg(self, value: "PositiveInteger") -> "CanControllerXlConfiguration":
        """
        AUTOSAR-compliant setter for propSeg with method chaining.
        
        Args:
            value: The propSeg to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to prop_seg property setter (gets validation automatically)
        """
        self.prop_seg = value  # Delegates to property setter
        return self

    def getPwmL(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for pwmL.
        
        Returns:
            The pwmL value
        
        Note:
            Delegates to pwm_l property (CODING_RULE_V2_00017)
        """
        return self.pwm_l  # Delegates to property

    def setPwmL(self, value: "PositiveInteger") -> "CanControllerXlConfiguration":
        """
        AUTOSAR-compliant setter for pwmL with method chaining.
        
        Args:
            value: The pwmL to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to pwm_l property setter (gets validation automatically)
        """
        self.pwm_l = value  # Delegates to property setter
        return self

    def getPwmO(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for pwmO.
        
        Returns:
            The pwmO value
        
        Note:
            Delegates to pwm_o property (CODING_RULE_V2_00017)
        """
        return self.pwm_o  # Delegates to property

    def setPwmO(self, value: "PositiveInteger") -> "CanControllerXlConfiguration":
        """
        AUTOSAR-compliant setter for pwmO with method chaining.
        
        Args:
            value: The pwmO to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to pwm_o property setter (gets validation automatically)
        """
        self.pwm_o = value  # Delegates to property setter
        return self

    def getPwmS(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for pwmS.
        
        Returns:
            The pwmS value
        
        Note:
            Delegates to pwm_s property (CODING_RULE_V2_00017)
        """
        return self.pwm_s  # Delegates to property

    def setPwmS(self, value: "PositiveInteger") -> "CanControllerXlConfiguration":
        """
        AUTOSAR-compliant setter for pwmS with method chaining.
        
        Args:
            value: The pwmS to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to pwm_s property setter (gets validation automatically)
        """
        self.pwm_s = value  # Delegates to property setter
        return self

    def getSspOffset(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for sspOffset.
        
        Returns:
            The sspOffset value
        
        Note:
            Delegates to ssp_offset property (CODING_RULE_V2_00017)
        """
        return self.ssp_offset  # Delegates to property

    def setSspOffset(self, value: "PositiveInteger") -> "CanControllerXlConfiguration":
        """
        AUTOSAR-compliant setter for sspOffset with method chaining.
        
        Args:
            value: The sspOffset to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to ssp_offset property setter (gets validation automatically)
        """
        self.ssp_offset = value  # Delegates to property setter
        return self

    def getSyncJumpWidth(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for syncJumpWidth.
        
        Returns:
            The syncJumpWidth value
        
        Note:
            Delegates to sync_jump_width property (CODING_RULE_V2_00017)
        """
        return self.sync_jump_width  # Delegates to property

    def setSyncJumpWidth(self, value: "PositiveInteger") -> "CanControllerXlConfiguration":
        """
        AUTOSAR-compliant setter for syncJumpWidth with method chaining.
        
        Args:
            value: The syncJumpWidth to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sync_jump_width property setter (gets validation automatically)
        """
        self.sync_jump_width = value  # Delegates to property setter
        return self

    def getTimeSeg1(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for timeSeg1.
        
        Returns:
            The timeSeg1 value
        
        Note:
            Delegates to time_seg1 property (CODING_RULE_V2_00017)
        """
        return self.time_seg1  # Delegates to property

    def setTimeSeg1(self, value: "PositiveInteger") -> "CanControllerXlConfiguration":
        """
        AUTOSAR-compliant setter for timeSeg1 with method chaining.
        
        Args:
            value: The timeSeg1 to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to time_seg1 property setter (gets validation automatically)
        """
        self.time_seg1 = value  # Delegates to property setter
        return self

    def getTimeSeg2(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for timeSeg2.
        
        Returns:
            The timeSeg2 value
        
        Note:
            Delegates to time_seg2 property (CODING_RULE_V2_00017)
        """
        return self.time_seg2  # Delegates to property

    def setTimeSeg2(self, value: "PositiveInteger") -> "CanControllerXlConfiguration":
        """
        AUTOSAR-compliant setter for timeSeg2 with method chaining.
        
        Args:
            value: The timeSeg2 to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to time_seg2 property setter (gets validation automatically)
        """
        self.time_seg2 = value  # Delegates to property setter
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

    def setTrcvPwmMode(self, value: "Boolean") -> "CanControllerXlConfiguration":
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

    def with_error_signaling(self, value: Optional["Boolean"]) -> "CanControllerXlConfiguration":
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

    def with_prop_seg(self, value: Optional["PositiveInteger"]) -> "CanControllerXlConfiguration":
        """
        Set propSeg and return self for chaining.
        
        Args:
            value: The propSeg to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_prop_seg("value")
        """
        self.prop_seg = value  # Use property setter (gets validation)
        return self

    def with_pwm_l(self, value: Optional["PositiveInteger"]) -> "CanControllerXlConfiguration":
        """
        Set pwmL and return self for chaining.
        
        Args:
            value: The pwmL to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_pwm_l("value")
        """
        self.pwm_l = value  # Use property setter (gets validation)
        return self

    def with_pwm_o(self, value: Optional["PositiveInteger"]) -> "CanControllerXlConfiguration":
        """
        Set pwmO and return self for chaining.
        
        Args:
            value: The pwmO to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_pwm_o("value")
        """
        self.pwm_o = value  # Use property setter (gets validation)
        return self

    def with_pwm_s(self, value: Optional["PositiveInteger"]) -> "CanControllerXlConfiguration":
        """
        Set pwmS and return self for chaining.
        
        Args:
            value: The pwmS to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_pwm_s("value")
        """
        self.pwm_s = value  # Use property setter (gets validation)
        return self

    def with_ssp_offset(self, value: Optional["PositiveInteger"]) -> "CanControllerXlConfiguration":
        """
        Set sspOffset and return self for chaining.
        
        Args:
            value: The sspOffset to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_ssp_offset("value")
        """
        self.ssp_offset = value  # Use property setter (gets validation)
        return self

    def with_sync_jump_width(self, value: Optional["PositiveInteger"]) -> "CanControllerXlConfiguration":
        """
        Set syncJumpWidth and return self for chaining.
        
        Args:
            value: The syncJumpWidth to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sync_jump_width("value")
        """
        self.sync_jump_width = value  # Use property setter (gets validation)
        return self

    def with_time_seg1(self, value: Optional["PositiveInteger"]) -> "CanControllerXlConfiguration":
        """
        Set timeSeg1 and return self for chaining.
        
        Args:
            value: The timeSeg1 to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_time_seg1("value")
        """
        self.time_seg1 = value  # Use property setter (gets validation)
        return self

    def with_time_seg2(self, value: Optional["PositiveInteger"]) -> "CanControllerXlConfiguration":
        """
        Set timeSeg2 and return self for chaining.
        
        Args:
            value: The timeSeg2 to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_time_seg2("value")
        """
        self.time_seg2 = value  # Use property setter (gets validation)
        return self

    def with_trcv_pwm_mode(self, value: Optional["Boolean"]) -> "CanControllerXlConfiguration":
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