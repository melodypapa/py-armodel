from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class DiagnosticEventToTroubleCodeJ1939Mapping(DiagnosticMapping):
    """
    By means of this meta-class it is possible to associate a DiagnosticEvent to
    a DiagnosticTroubleCode J1939.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::DiagnosticJ1939Mapping::DiagnosticEventToTroubleCodeJ1939Mapping
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 269, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to a DiagnosticEvent to which a J1939 Code is assigned.
        self._diagnosticEvent: Optional["DiagnosticEvent"] = None

    @property
    def diagnostic_event(self) -> Optional["DiagnosticEvent"]:
        """Get diagnosticEvent (Pythonic accessor)."""
        return self._diagnosticEvent

    @diagnostic_event.setter
    def diagnostic_event(self, value: Optional["DiagnosticEvent"]) -> None:
        """
        Set diagnosticEvent with validation.
        
        Args:
            value: The diagnosticEvent to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._diagnosticEvent = None
            return

        if not isinstance(value, DiagnosticEvent):
            raise TypeError(
                f"diagnosticEvent must be DiagnosticEvent or None, got {type(value).__name__}"
            )
        self._diagnosticEvent = value
        # Reference to a J1939 Diagnostic Trouble Code to which a DiagnosticEvent is
        # assigned.
        self._troubleCode: Optional["DiagnosticTroubleCode"] = None

    @property
    def trouble_code(self) -> Optional["DiagnosticTroubleCode"]:
        """Get troubleCode (Pythonic accessor)."""
        return self._troubleCode

    @trouble_code.setter
    def trouble_code(self, value: Optional["DiagnosticTroubleCode"]) -> None:
        """
        Set troubleCode with validation.
        
        Args:
            value: The troubleCode to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._troubleCode = None
            return

        if not isinstance(value, DiagnosticTroubleCode):
            raise TypeError(
                f"troubleCode must be DiagnosticTroubleCode or None, got {type(value).__name__}"
            )
        self._troubleCode = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDiagnosticEvent(self) -> "DiagnosticEvent":
        """
        AUTOSAR-compliant getter for diagnosticEvent.
        
        Returns:
            The diagnosticEvent value
        
        Note:
            Delegates to diagnostic_event property (CODING_RULE_V2_00017)
        """
        return self.diagnostic_event  # Delegates to property

    def setDiagnosticEvent(self, value: "DiagnosticEvent") -> "DiagnosticEventToTroubleCodeJ1939Mapping":
        """
        AUTOSAR-compliant setter for diagnosticEvent with method chaining.
        
        Args:
            value: The diagnosticEvent to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to diagnostic_event property setter (gets validation automatically)
        """
        self.diagnostic_event = value  # Delegates to property setter
        return self

    def getTroubleCode(self) -> "DiagnosticTroubleCode":
        """
        AUTOSAR-compliant getter for troubleCode.
        
        Returns:
            The troubleCode value
        
        Note:
            Delegates to trouble_code property (CODING_RULE_V2_00017)
        """
        return self.trouble_code  # Delegates to property

    def setTroubleCode(self, value: "DiagnosticTroubleCode") -> "DiagnosticEventToTroubleCodeJ1939Mapping":
        """
        AUTOSAR-compliant setter for troubleCode with method chaining.
        
        Args:
            value: The troubleCode to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to trouble_code property setter (gets validation automatically)
        """
        self.trouble_code = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_diagnostic_event(self, value: Optional["DiagnosticEvent"]) -> "DiagnosticEventToTroubleCodeJ1939Mapping":
        """
        Set diagnosticEvent and return self for chaining.
        
        Args:
            value: The diagnosticEvent to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_diagnostic_event("value")
        """
        self.diagnostic_event = value  # Use property setter (gets validation)
        return self

    def with_trouble_code(self, value: Optional["DiagnosticTroubleCode"]) -> "DiagnosticEventToTroubleCodeJ1939Mapping":
        """
        Set troubleCode and return self for chaining.
        
        Args:
            value: The troubleCode to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_trouble_code("value")
        """
        self.trouble_code = value  # Use property setter (gets validation)
        return self