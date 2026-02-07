from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class CanControllerFdConfiguration(ARObject):
    """
    Bit timing related configuration of a CAN controller for payload and CRC of
    a CAN FD frame.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanTopology::CanControllerFdConfiguration
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 66, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
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

    def getPaddingValue(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for paddingValue.
        
        Returns:
            The paddingValue value
        
        Note:
            Delegates to padding_value property (CODING_RULE_V2_00017)
        """
        return self.padding_value  # Delegates to property

    def setPaddingValue(self, value: "PositiveInteger") -> "CanControllerFdConfiguration":
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

    def getPropSeg(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for propSeg.
        
        Returns:
            The propSeg value
        
        Note:
            Delegates to prop_seg property (CODING_RULE_V2_00017)
        """
        return self.prop_seg  # Delegates to property

    def setPropSeg(self, value: "PositiveInteger") -> "CanControllerFdConfiguration":
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

    def getSspOffset(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for sspOffset.
        
        Returns:
            The sspOffset value
        
        Note:
            Delegates to ssp_offset property (CODING_RULE_V2_00017)
        """
        return self.ssp_offset  # Delegates to property

    def setSspOffset(self, value: "PositiveInteger") -> "CanControllerFdConfiguration":
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

    def setSyncJumpWidth(self, value: "PositiveInteger") -> "CanControllerFdConfiguration":
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

    def setTimeSeg1(self, value: "PositiveInteger") -> "CanControllerFdConfiguration":
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

    def setTimeSeg2(self, value: "PositiveInteger") -> "CanControllerFdConfiguration":
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

    def getTxBitRateSwitch(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for txBitRateSwitch.
        
        Returns:
            The txBitRateSwitch value
        
        Note:
            Delegates to tx_bit_rate_switch property (CODING_RULE_V2_00017)
        """
        return self.tx_bit_rate_switch  # Delegates to property

    def setTxBitRateSwitch(self, value: "Boolean") -> "CanControllerFdConfiguration":
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

    def with_padding_value(self, value: Optional["PositiveInteger"]) -> "CanControllerFdConfiguration":
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

    def with_prop_seg(self, value: Optional["PositiveInteger"]) -> "CanControllerFdConfiguration":
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

    def with_ssp_offset(self, value: Optional["PositiveInteger"]) -> "CanControllerFdConfiguration":
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

    def with_sync_jump_width(self, value: Optional["PositiveInteger"]) -> "CanControllerFdConfiguration":
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

    def with_time_seg1(self, value: Optional["PositiveInteger"]) -> "CanControllerFdConfiguration":
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

    def with_time_seg2(self, value: Optional["PositiveInteger"]) -> "CanControllerFdConfiguration":
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

    def with_tx_bit_rate_switch(self, value: Optional["Boolean"]) -> "CanControllerFdConfiguration":
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