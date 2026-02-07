from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class FlexrayFrameTriggering(FrameTriggering):
    """
    FlexRay specific attributes to the FrameTriggering
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Flexray::FlexrayCommunication::FlexrayFrameTriggering
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 422, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specification of a sending behaviour where the exact time for the frames
        # transmission is guaranteed.
        self._absolutely: List["FlexrayAbsolutely"] = []

    @property
    def absolutely(self) -> List["FlexrayAbsolutely"]:
        """Get absolutely (Pythonic accessor)."""
        return self._absolutely
        # Allows L-PDU length reduction and indicates that the CC buffer has to be
                # reconfigured for the actual Header-CRC before transmission of the attribute
                # is set to true than the referenced Frame defines the max.
        # length.
        self._allowDynamic: Optional["Boolean"] = None

    @property
    def allow_dynamic(self) -> Optional["Boolean"]:
        """Get allowDynamic (Pythonic accessor)."""
        return self._allowDynamic

    @allow_dynamic.setter
    def allow_dynamic(self, value: Optional["Boolean"]) -> None:
        """
        Set allowDynamic with validation.
        
        Args:
            value: The allowDynamic to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._allowDynamic = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"allowDynamic must be Boolean or None, got {type(value).__name__}"
            )
        self._allowDynamic = value
        # The first two bytes of the payload segment of the FlexRay for frames
        # transmitted in the dynamic be used as receiver filterable data called the.
        self._messageId: Optional["PositiveInteger"] = None

    @property
    def message_id(self) -> Optional["PositiveInteger"]:
        """Get messageId (Pythonic accessor)."""
        return self._messageId

    @message_id.setter
    def message_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set messageId with validation.
        
        Args:
            value: The messageId to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._messageId = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"messageId must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._messageId = value
        # Switching the Payload Preamble bit.
        self._payloadPreambleIndicator: Optional["Boolean"] = None

    @property
    def payload_preamble_indicator(self) -> Optional["Boolean"]:
        """Get payloadPreambleIndicator (Pythonic accessor)."""
        return self._payloadPreambleIndicator

    @payload_preamble_indicator.setter
    def payload_preamble_indicator(self, value: Optional["Boolean"]) -> None:
        """
        Set payloadPreambleIndicator with validation.
        
        Args:
            value: The payloadPreambleIndicator to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._payloadPreambleIndicator = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"payloadPreambleIndicator must be Boolean or None, got {type(value).__name__}"
            )
        self._payloadPreambleIndicator = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAbsolutely(self) -> List["FlexrayAbsolutely"]:
        """
        AUTOSAR-compliant getter for absolutely.
        
        Returns:
            The absolutely value
        
        Note:
            Delegates to absolutely property (CODING_RULE_V2_00017)
        """
        return self.absolutely  # Delegates to property

    def getAllowDynamic(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for allowDynamic.
        
        Returns:
            The allowDynamic value
        
        Note:
            Delegates to allow_dynamic property (CODING_RULE_V2_00017)
        """
        return self.allow_dynamic  # Delegates to property

    def setAllowDynamic(self, value: "Boolean") -> "FlexrayFrameTriggering":
        """
        AUTOSAR-compliant setter for allowDynamic with method chaining.
        
        Args:
            value: The allowDynamic to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to allow_dynamic property setter (gets validation automatically)
        """
        self.allow_dynamic = value  # Delegates to property setter
        return self

    def getMessageId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for messageId.
        
        Returns:
            The messageId value
        
        Note:
            Delegates to message_id property (CODING_RULE_V2_00017)
        """
        return self.message_id  # Delegates to property

    def setMessageId(self, value: "PositiveInteger") -> "FlexrayFrameTriggering":
        """
        AUTOSAR-compliant setter for messageId with method chaining.
        
        Args:
            value: The messageId to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to message_id property setter (gets validation automatically)
        """
        self.message_id = value  # Delegates to property setter
        return self

    def getPayloadPreambleIndicator(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for payloadPreambleIndicator.
        
        Returns:
            The payloadPreambleIndicator value
        
        Note:
            Delegates to payload_preamble_indicator property (CODING_RULE_V2_00017)
        """
        return self.payload_preamble_indicator  # Delegates to property

    def setPayloadPreambleIndicator(self, value: "Boolean") -> "FlexrayFrameTriggering":
        """
        AUTOSAR-compliant setter for payloadPreambleIndicator with method chaining.
        
        Args:
            value: The payloadPreambleIndicator to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to payload_preamble_indicator property setter (gets validation automatically)
        """
        self.payload_preamble_indicator = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_allow_dynamic(self, value: Optional["Boolean"]) -> "FlexrayFrameTriggering":
        """
        Set allowDynamic and return self for chaining.
        
        Args:
            value: The allowDynamic to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_allow_dynamic("value")
        """
        self.allow_dynamic = value  # Use property setter (gets validation)
        return self

    def with_message_id(self, value: Optional["PositiveInteger"]) -> "FlexrayFrameTriggering":
        """
        Set messageId and return self for chaining.
        
        Args:
            value: The messageId to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_message_id("value")
        """
        self.message_id = value  # Use property setter (gets validation)
        return self

    def with_payload_preamble_indicator(self, value: Optional["Boolean"]) -> "FlexrayFrameTriggering":
        """
        Set payloadPreambleIndicator and return self for chaining.
        
        Args:
            value: The payloadPreambleIndicator to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_payload_preamble_indicator("value")
        """
        self.payload_preamble_indicator = value  # Use property setter (gets validation)
        return self