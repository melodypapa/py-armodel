from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class DiagnosticResponseOnEvent(DiagnosticServiceInstance):
    """
    This represents an instance of the "Response on Event" diagnostic service.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::ResponseOnEvent::DiagnosticResponseOnEvent
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 132, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the applicable DiagnosticEventWindows.
        self._eventWindow: List["DiagnosticEventWindow"] = []

    @property
    def event_window(self) -> List["DiagnosticEventWindow"]:
        """Get eventWindow (Pythonic accessor)."""
        return self._eventWindow
        # This reference substantiates that abstract reference in the role serviceClass
                # for this specific concrete class.
        # reference represents the ability to access among all
                # DiagnosticResponseOnEvent given context.
        self._responseOn: Optional["DiagnosticResponseOn"] = None

    @property
    def response_on(self) -> Optional["DiagnosticResponseOn"]:
        """Get responseOn (Pythonic accessor)."""
        return self._responseOn

    @response_on.setter
    def response_on(self, value: Optional["DiagnosticResponseOn"]) -> None:
        """
        Set responseOn with validation.
        
        Args:
            value: The responseOn to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._responseOn = None
            return

        if not isinstance(value, DiagnosticResponseOn):
            raise TypeError(
                f"responseOn must be DiagnosticResponseOn or None, got {type(value).__name__}"
            )
        self._responseOn = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEventWindow(self) -> List["DiagnosticEventWindow"]:
        """
        AUTOSAR-compliant getter for eventWindow.
        
        Returns:
            The eventWindow value
        
        Note:
            Delegates to event_window property (CODING_RULE_V2_00017)
        """
        return self.event_window  # Delegates to property

    def getResponseOn(self) -> "DiagnosticResponseOn":
        """
        AUTOSAR-compliant getter for responseOn.
        
        Returns:
            The responseOn value
        
        Note:
            Delegates to response_on property (CODING_RULE_V2_00017)
        """
        return self.response_on  # Delegates to property

    def setResponseOn(self, value: "DiagnosticResponseOn") -> "DiagnosticResponseOnEvent":
        """
        AUTOSAR-compliant setter for responseOn with method chaining.
        
        Args:
            value: The responseOn to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to response_on property setter (gets validation automatically)
        """
        self.response_on = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_response_on(self, value: Optional["DiagnosticResponseOn"]) -> "DiagnosticResponseOnEvent":
        """
        Set responseOn and return self for chaining.
        
        Args:
            value: The responseOn to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_response_on("value")
        """
        self.response_on = value  # Use property setter (gets validation)
        return self