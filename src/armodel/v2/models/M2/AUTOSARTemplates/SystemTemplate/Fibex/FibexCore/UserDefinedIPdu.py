from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class UserDefinedIPdu(IPdu):
    """
    UserDefinedIPdu allows to describe PDU-based communication over Complex
    Drivers. If a new BSW module is added above the PduR (e.g. a Diagnostic
    Service ) then this IPdu element shall be used to describe the
    communication.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::UserDefinedIPdu
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 346, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines the CDD that transmits or receives If several CDDs are
        # defined this used to distinguish between them.
        self._cddType: Optional["String"] = None

    @property
    def cdd_type(self) -> Optional["String"]:
        """Get cddType (Pythonic accessor)."""
        return self._cddType

    @cdd_type.setter
    def cdd_type(self, value: Optional["String"]) -> None:
        """
        Set cddType with validation.
        
        Args:
            value: The cddType to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._cddType = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"cddType must be String or None, got {type(value).__name__}"
            )
        self._cddType = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCddType(self) -> "String":
        """
        AUTOSAR-compliant getter for cddType.
        
        Returns:
            The cddType value
        
        Note:
            Delegates to cdd_type property (CODING_RULE_V2_00017)
        """
        return self.cdd_type  # Delegates to property

    def setCddType(self, value: "String") -> "UserDefinedIPdu":
        """
        AUTOSAR-compliant setter for cddType with method chaining.
        
        Args:
            value: The cddType to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to cdd_type property setter (gets validation automatically)
        """
        self.cdd_type = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_cdd_type(self, value: Optional["String"]) -> "UserDefinedIPdu":
        """
        Set cddType and return self for chaining.
        
        Args:
            value: The cddType to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_cdd_type("value")
        """
        self.cdd_type = value  # Use property setter (gets validation)
        return self