from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class DiagnosticFimAliasEventGroupMapping(DiagnosticMapping):
    """
    This meta-class represents the ability to map a DiagnosticFimEventGroup to a
    DiagnosticFimAliasEvent Group. By this means the "preliminary" modeling by
    way of a DiagnosticFimAliasEventGroup is further substantiated.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::FimMapping::DiagnosticFimAliasEventGroupMapping
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 263, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the reference to the actual summary.
        self._actualEvent: Optional["DiagnosticFimEvent"] = None

    @property
    def actual_event(self) -> Optional["DiagnosticFimEvent"]:
        """Get actualEvent (Pythonic accessor)."""
        return self._actualEvent

    @actual_event.setter
    def actual_event(self, value: Optional["DiagnosticFimEvent"]) -> None:
        """
        Set actualEvent with validation.
        
        Args:
            value: The actualEvent to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._actualEvent = None
            return

        if not isinstance(value, DiagnosticFimEvent):
            raise TypeError(
                f"actualEvent must be DiagnosticFimEvent or None, got {type(value).__name__}"
            )
        self._actualEvent = value
        # This represents the reference to the alias summary event.
        self._aliasEvent: Optional["DiagnosticFimAlias"] = None

    @property
    def alias_event(self) -> Optional["DiagnosticFimAlias"]:
        """Get aliasEvent (Pythonic accessor)."""
        return self._aliasEvent

    @alias_event.setter
    def alias_event(self, value: Optional["DiagnosticFimAlias"]) -> None:
        """
        Set aliasEvent with validation.
        
        Args:
            value: The aliasEvent to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._aliasEvent = None
            return

        if not isinstance(value, DiagnosticFimAlias):
            raise TypeError(
                f"aliasEvent must be DiagnosticFimAlias or None, got {type(value).__name__}"
            )
        self._aliasEvent = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getActualEvent(self) -> "DiagnosticFimEvent":
        """
        AUTOSAR-compliant getter for actualEvent.
        
        Returns:
            The actualEvent value
        
        Note:
            Delegates to actual_event property (CODING_RULE_V2_00017)
        """
        return self.actual_event  # Delegates to property

    def setActualEvent(self, value: "DiagnosticFimEvent") -> "DiagnosticFimAliasEventGroupMapping":
        """
        AUTOSAR-compliant setter for actualEvent with method chaining.
        
        Args:
            value: The actualEvent to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to actual_event property setter (gets validation automatically)
        """
        self.actual_event = value  # Delegates to property setter
        return self

    def getAliasEvent(self) -> "DiagnosticFimAlias":
        """
        AUTOSAR-compliant getter for aliasEvent.
        
        Returns:
            The aliasEvent value
        
        Note:
            Delegates to alias_event property (CODING_RULE_V2_00017)
        """
        return self.alias_event  # Delegates to property

    def setAliasEvent(self, value: "DiagnosticFimAlias") -> "DiagnosticFimAliasEventGroupMapping":
        """
        AUTOSAR-compliant setter for aliasEvent with method chaining.
        
        Args:
            value: The aliasEvent to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to alias_event property setter (gets validation automatically)
        """
        self.alias_event = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_actual_event(self, value: Optional["DiagnosticFimEvent"]) -> "DiagnosticFimAliasEventGroupMapping":
        """
        Set actualEvent and return self for chaining.
        
        Args:
            value: The actualEvent to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_actual_event("value")
        """
        self.actual_event = value  # Use property setter (gets validation)
        return self

    def with_alias_event(self, value: Optional["DiagnosticFimAlias"]) -> "DiagnosticFimAliasEventGroupMapping":
        """
        Set aliasEvent and return self for chaining.
        
        Args:
            value: The aliasEvent to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_alias_event("value")
        """
        self.alias_event = value  # Use property setter (gets validation)
        return self