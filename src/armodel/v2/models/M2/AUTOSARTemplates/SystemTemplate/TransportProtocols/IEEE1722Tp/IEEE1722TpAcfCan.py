from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class IEEE1722TpAcfCan(IEEE1722TpAcfBus):
    """
    ACF IEEE1722Tp bus used for CAN transport.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp::IEEE1722TpAcf::IEEE1722TpAcfCan
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 661, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Definition of the ACF CAN stream message type.
        self._messageTypeMessageTypeEnum: Optional["IEEE1722TpAcfCan"] = None

    @property
    def message_type_message_type_enum(self) -> Optional["IEEE1722TpAcfCan"]:
        """Get messageTypeMessageTypeEnum (Pythonic accessor)."""
        return self._messageTypeMessageTypeEnum

    @message_type_message_type_enum.setter
    def message_type_message_type_enum(self, value: Optional["IEEE1722TpAcfCan"]) -> None:
        """
        Set messageTypeMessageTypeEnum with validation.
        
        Args:
            value: The messageTypeMessageTypeEnum to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._messageTypeMessageTypeEnum = None
            return

        if not isinstance(value, IEEE1722TpAcfCan):
            raise TypeError(
                f"messageTypeMessageTypeEnum must be IEEE1722TpAcfCan or None, got {type(value).__name__}"
            )
        self._messageTypeMessageTypeEnum = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMessageTypeMessageTypeEnum(self) -> "IEEE1722TpAcfCan":
        """
        AUTOSAR-compliant getter for messageTypeMessageTypeEnum.
        
        Returns:
            The messageTypeMessageTypeEnum value
        
        Note:
            Delegates to message_type_message_type_enum property (CODING_RULE_V2_00017)
        """
        return self.message_type_message_type_enum  # Delegates to property

    def setMessageTypeMessageTypeEnum(self, value: "IEEE1722TpAcfCan") -> "IEEE1722TpAcfCan":
        """
        AUTOSAR-compliant setter for messageTypeMessageTypeEnum with method chaining.
        
        Args:
            value: The messageTypeMessageTypeEnum to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to message_type_message_type_enum property setter (gets validation automatically)
        """
        self.message_type_message_type_enum = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_message_type_message_type_enum(self, value: Optional["IEEE1722TpAcfCan"]) -> "IEEE1722TpAcfCan":
        """
        Set messageTypeMessageTypeEnum and return self for chaining.
        
        Args:
            value: The messageTypeMessageTypeEnum to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_message_type_message_type_enum("value")
        """
        self.message_type_message_type_enum = value  # Use property setter (gets validation)
        return self