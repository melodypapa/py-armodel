from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class DiagnosticFunctionInhibitSource(Identifiable):
    """
    This meta-class represents the ability to define an inhibition source in the
    context of the Fim configuration.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Fim::DiagnosticFunctionInhibitSource
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 216, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the alias event applicable for the inhibition source.
        self._event: Optional["DiagnosticFimAlias"] = None

    @property
    def event(self) -> Optional["DiagnosticFimAlias"]:
        """Get event (Pythonic accessor)."""
        return self._event

    @event.setter
    def event(self, value: Optional["DiagnosticFimAlias"]) -> None:
        """
        Set event with validation.
        
        Args:
            value: The event to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._event = None
            return

        if not isinstance(value, DiagnosticFimAlias):
            raise TypeError(
                f"event must be DiagnosticFimAlias or None, got {type(value).__name__}"
            )
        self._event = value
        # This represents the event group applicable for the inhibition source.
        self._eventGroup: Optional["DiagnosticFimAlias"] = None

    @property
    def event_group(self) -> Optional["DiagnosticFimAlias"]:
        """Get eventGroup (Pythonic accessor)."""
        return self._eventGroup

    @event_group.setter
    def event_group(self, value: Optional["DiagnosticFimAlias"]) -> None:
        """
        Set eventGroup with validation.
        
        Args:
            value: The eventGroup to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._eventGroup = None
            return

        if not isinstance(value, DiagnosticFimAlias):
            raise TypeError(
                f"eventGroup must be DiagnosticFimAlias or None, got {type(value).__name__}"
            )
        self._eventGroup = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEvent(self) -> "DiagnosticFimAlias":
        """
        AUTOSAR-compliant getter for event.
        
        Returns:
            The event value
        
        Note:
            Delegates to event property (CODING_RULE_V2_00017)
        """
        return self.event  # Delegates to property

    def setEvent(self, value: "DiagnosticFimAlias") -> "DiagnosticFunctionInhibitSource":
        """
        AUTOSAR-compliant setter for event with method chaining.
        
        Args:
            value: The event to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to event property setter (gets validation automatically)
        """
        self.event = value  # Delegates to property setter
        return self

    def getEventGroup(self) -> "DiagnosticFimAlias":
        """
        AUTOSAR-compliant getter for eventGroup.
        
        Returns:
            The eventGroup value
        
        Note:
            Delegates to event_group property (CODING_RULE_V2_00017)
        """
        return self.event_group  # Delegates to property

    def setEventGroup(self, value: "DiagnosticFimAlias") -> "DiagnosticFunctionInhibitSource":
        """
        AUTOSAR-compliant setter for eventGroup with method chaining.
        
        Args:
            value: The eventGroup to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to event_group property setter (gets validation automatically)
        """
        self.event_group = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_event(self, value: Optional["DiagnosticFimAlias"]) -> "DiagnosticFunctionInhibitSource":
        """
        Set event and return self for chaining.
        
        Args:
            value: The event to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_event("value")
        """
        self.event = value  # Use property setter (gets validation)
        return self

    def with_event_group(self, value: Optional["DiagnosticFimAlias"]) -> "DiagnosticFunctionInhibitSource":
        """
        Set eventGroup and return self for chaining.
        
        Args:
            value: The eventGroup to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_event_group("value")
        """
        self.event_group = value  # Use property setter (gets validation)
        return self