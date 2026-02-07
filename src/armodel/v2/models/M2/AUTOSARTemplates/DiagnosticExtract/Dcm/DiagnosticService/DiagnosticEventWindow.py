from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class DiagnosticEventWindow(ARObject):
    """
    This represents the ability to define the characteristics of the applicable
    event window
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::ResponseOnEvent::DiagnosticEventWindow
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 133, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute clarifies the validity of the eventWindow.
        self._eventWindow: Optional["DiagnosticEventWindow"] = None

    @property
    def event_window(self) -> Optional["DiagnosticEventWindow"]:
        """Get eventWindow (Pythonic accessor)."""
        return self._eventWindow

    @event_window.setter
    def event_window(self, value: Optional["DiagnosticEventWindow"]) -> None:
        """
        Set eventWindow with validation.
        
        Args:
            value: The eventWindow to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._eventWindow = None
            return

        if not isinstance(value, DiagnosticEventWindow):
            raise TypeError(
                f"eventWindow must be DiagnosticEventWindow or None, got {type(value).__name__}"
            )
        self._eventWindow = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEventWindow(self) -> "DiagnosticEventWindow":
        """
        AUTOSAR-compliant getter for eventWindow.
        
        Returns:
            The eventWindow value
        
        Note:
            Delegates to event_window property (CODING_RULE_V2_00017)
        """
        return self.event_window  # Delegates to property

    def setEventWindow(self, value: "DiagnosticEventWindow") -> "DiagnosticEventWindow":
        """
        AUTOSAR-compliant setter for eventWindow with method chaining.
        
        Args:
            value: The eventWindow to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to event_window property setter (gets validation automatically)
        """
        self.event_window = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_event_window(self, value: Optional["DiagnosticEventWindow"]) -> "DiagnosticEventWindow":
        """
        Set eventWindow and return self for chaining.
        
        Args:
            value: The eventWindow to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_event_window("value")
        """
        self.event_window = value  # Use property setter (gets validation)
        return self