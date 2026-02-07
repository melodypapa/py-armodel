from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class DiagnosticEventToSecurityEventMapping(DiagnosticMapping):
    """
    This meta-class represents the ability to map a security event that is
    defined in the context of the Security Extract to a diagnostic event defined
    on the context of the DiagnosticExtract.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::DiagnosticEventToSecurityEventMapping
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 257, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference identifies the applicable diagnostic event.
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
        # This reference identifies the qualification of the applicable security event.
        self._securityEvent: Optional["SecurityEventContext"] = None

    @property
    def security_event(self) -> Optional["SecurityEventContext"]:
        """Get securityEvent (Pythonic accessor)."""
        return self._securityEvent

    @security_event.setter
    def security_event(self, value: Optional["SecurityEventContext"]) -> None:
        """
        Set securityEvent with validation.
        
        Args:
            value: The securityEvent to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._securityEvent = None
            return

        if not isinstance(value, SecurityEventContext):
            raise TypeError(
                f"securityEvent must be SecurityEventContext or None, got {type(value).__name__}"
            )
        self._securityEvent = value

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

    def setDiagnosticEvent(self, value: "DiagnosticEvent") -> "DiagnosticEventToSecurityEventMapping":
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

    def getSecurityEvent(self) -> "SecurityEventContext":
        """
        AUTOSAR-compliant getter for securityEvent.
        
        Returns:
            The securityEvent value
        
        Note:
            Delegates to security_event property (CODING_RULE_V2_00017)
        """
        return self.security_event  # Delegates to property

    def setSecurityEvent(self, value: "SecurityEventContext") -> "DiagnosticEventToSecurityEventMapping":
        """
        AUTOSAR-compliant setter for securityEvent with method chaining.
        
        Args:
            value: The securityEvent to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to security_event property setter (gets validation automatically)
        """
        self.security_event = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_diagnostic_event(self, value: Optional["DiagnosticEvent"]) -> "DiagnosticEventToSecurityEventMapping":
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

    def with_security_event(self, value: Optional["SecurityEventContext"]) -> "DiagnosticEventToSecurityEventMapping":
        """
        Set securityEvent and return self for chaining.
        
        Args:
            value: The securityEvent to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_security_event("value")
        """
        self.security_event = value  # Use property setter (gets validation)
        return self