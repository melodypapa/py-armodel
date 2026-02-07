from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class J1939DcmIPdu(IPdu):
    """
    Represents the IPdus handled by J1939Dcm.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::J1939DcmIPdu
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 321, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 344, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute is used to identify the actual DMx message,.
        self._diagnostic: Optional["PositiveInteger"] = None

    @property
    def diagnostic(self) -> Optional["PositiveInteger"]:
        """Get diagnostic (Pythonic accessor)."""
        return self._diagnostic

    @diagnostic.setter
    def diagnostic(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set diagnostic with validation.
        
        Args:
            value: The diagnostic to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._diagnostic = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"diagnostic must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._diagnostic = value
        self._MessageType: "e.g" = None

    @property
    def message_type(self) -> "e.g":
        """Get MessageType (Pythonic accessor)."""
        return self._MessageType

    @message_type.setter
    def message_type(self, value: "e.g") -> None:
        """
        Set MessageType with validation.
        
        Args:
            value: The MessageType to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, e.g):
            raise TypeError(
                f"MessageType must be e.g, got {type(value).__name__}"
            )
        self._MessageType = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDiagnostic(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for diagnostic.
        
        Returns:
            The diagnostic value
        
        Note:
            Delegates to diagnostic property (CODING_RULE_V2_00017)
        """
        return self.diagnostic  # Delegates to property

    def setDiagnostic(self, value: "PositiveInteger") -> "J1939DcmIPdu":
        """
        AUTOSAR-compliant setter for diagnostic with method chaining.
        
        Args:
            value: The diagnostic to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to diagnostic property setter (gets validation automatically)
        """
        self.diagnostic = value  # Delegates to property setter
        return self

    def getMessageType(self) -> "e.g":
        """
        AUTOSAR-compliant getter for MessageType.
        
        Returns:
            The MessageType value
        
        Note:
            Delegates to message_type property (CODING_RULE_V2_00017)
        """
        return self.message_type  # Delegates to property

    def setMessageType(self, value: "e.g") -> "J1939DcmIPdu":
        """
        AUTOSAR-compliant setter for MessageType with method chaining.
        
        Args:
            value: The MessageType to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to message_type property setter (gets validation automatically)
        """
        self.message_type = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_diagnostic(self, value: Optional["PositiveInteger"]) -> "J1939DcmIPdu":
        """
        Set diagnostic and return self for chaining.
        
        Args:
            value: The diagnostic to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_diagnostic("value")
        """
        self.diagnostic = value  # Use property setter (gets validation)
        return self

    def with_message_type(self, value: "e.g") -> "J1939DcmIPdu":
        """
        Set MessageType and return self for chaining.
        
        Args:
            value: The MessageType to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_message_type("value")
        """
        self.message_type = value  # Use property setter (gets validation)
        return self