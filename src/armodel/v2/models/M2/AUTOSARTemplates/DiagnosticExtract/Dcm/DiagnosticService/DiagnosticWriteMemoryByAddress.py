from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class DiagnosticWriteMemoryByAddress(DiagnosticMemoryAddressableRangeAccess):
    """
    This represents an instance of the "Write Memory by Address" diagnostic
    service.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::MemoryByAddress::DiagnosticWriteMemoryByAddress
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 140, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference substantiates that abstract reference in the serviceClass for
                # this specific concrete class.
        # reference represents the ability to access among all DiagnosticWritememoryBy
                # the given context.
        self._writeClass: Optional["DiagnosticWriteMemory"] = None

    @property
    def write_class(self) -> Optional["DiagnosticWriteMemory"]:
        """Get writeClass (Pythonic accessor)."""
        return self._writeClass

    @write_class.setter
    def write_class(self, value: Optional["DiagnosticWriteMemory"]) -> None:
        """
        Set writeClass with validation.
        
        Args:
            value: The writeClass to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._writeClass = None
            return

        if not isinstance(value, DiagnosticWriteMemory):
            raise TypeError(
                f"writeClass must be DiagnosticWriteMemory or None, got {type(value).__name__}"
            )
        self._writeClass = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getWriteClass(self) -> "DiagnosticWriteMemory":
        """
        AUTOSAR-compliant getter for writeClass.
        
        Returns:
            The writeClass value
        
        Note:
            Delegates to write_class property (CODING_RULE_V2_00017)
        """
        return self.write_class  # Delegates to property

    def setWriteClass(self, value: "DiagnosticWriteMemory") -> "DiagnosticWriteMemoryByAddress":
        """
        AUTOSAR-compliant setter for writeClass with method chaining.
        
        Args:
            value: The writeClass to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to write_class property setter (gets validation automatically)
        """
        self.write_class = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_write_class(self, value: Optional["DiagnosticWriteMemory"]) -> "DiagnosticWriteMemoryByAddress":
        """
        Set writeClass and return self for chaining.
        
        Args:
            value: The writeClass to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_write_class("value")
        """
        self.write_class = value  # Use property setter (gets validation)
        return self