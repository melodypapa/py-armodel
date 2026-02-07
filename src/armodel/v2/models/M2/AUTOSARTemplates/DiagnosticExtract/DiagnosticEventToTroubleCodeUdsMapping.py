from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class DiagnosticEventToTroubleCodeUdsMapping(DiagnosticMapping):
    """
    Defines which UDS Diagnostic Trouble Code is applicable for a
    DiagnosticEvent.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::DiagnosticEventToTroubleCodeUdsMapping
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 245, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to a DiagnosticEvent to which a UDS Code is assigned.
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
        # Reference to an UDS Diagnostic Trouble Code assigned a DiagnosticEvent.
        self._troubleCodeUds: Optional["DiagnosticTroubleCode"] = None

    @property
    def trouble_code_uds(self) -> Optional["DiagnosticTroubleCode"]:
        """Get troubleCodeUds (Pythonic accessor)."""
        return self._troubleCodeUds

    @trouble_code_uds.setter
    def trouble_code_uds(self, value: Optional["DiagnosticTroubleCode"]) -> None:
        """
        Set troubleCodeUds with validation.
        
        Args:
            value: The troubleCodeUds to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._troubleCodeUds = None
            return

        if not isinstance(value, DiagnosticTroubleCode):
            raise TypeError(
                f"troubleCodeUds must be DiagnosticTroubleCode or None, got {type(value).__name__}"
            )
        self._troubleCodeUds = value

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

    def setDiagnosticEvent(self, value: "DiagnosticEvent") -> "DiagnosticEventToTroubleCodeUdsMapping":
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

    def getTroubleCodeUds(self) -> "DiagnosticTroubleCode":
        """
        AUTOSAR-compliant getter for troubleCodeUds.
        
        Returns:
            The troubleCodeUds value
        
        Note:
            Delegates to trouble_code_uds property (CODING_RULE_V2_00017)
        """
        return self.trouble_code_uds  # Delegates to property

    def setTroubleCodeUds(self, value: "DiagnosticTroubleCode") -> "DiagnosticEventToTroubleCodeUdsMapping":
        """
        AUTOSAR-compliant setter for troubleCodeUds with method chaining.
        
        Args:
            value: The troubleCodeUds to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to trouble_code_uds property setter (gets validation automatically)
        """
        self.trouble_code_uds = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_diagnostic_event(self, value: Optional["DiagnosticEvent"]) -> "DiagnosticEventToTroubleCodeUdsMapping":
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

    def with_trouble_code_uds(self, value: Optional["DiagnosticTroubleCode"]) -> "DiagnosticEventToTroubleCodeUdsMapping":
        """
        Set troubleCodeUds and return self for chaining.
        
        Args:
            value: The troubleCodeUds to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_trouble_code_uds("value")
        """
        self.trouble_code_uds = value  # Use property setter (gets validation)
        return self