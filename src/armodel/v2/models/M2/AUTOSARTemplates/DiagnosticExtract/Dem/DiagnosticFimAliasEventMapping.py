from typing import Optional


class DiagnosticFimAliasEventMapping(DiagnosticMapping):
    """
    This meta-class represents the ability to model the mapping of a
    DiagnosticEvent to a DiagnosticAlias Event. By this means the "preliminary"
    modeling by way of a DiagnosticAliasEvent is further substantiated.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticEvent::DiagnosticFimAliasEventMapping

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 262, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the reference to the actual diagnostic.
        self._actualEvent: Optional["DiagnosticEvent"] = None

    @property
    def actual_event(self) -> Optional["DiagnosticEvent"]:
        """Get actualEvent (Pythonic accessor)."""
        return self._actualEvent

    @actual_event.setter
    def actual_event(self, value: Optional["DiagnosticEvent"]) -> None:
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

        if not isinstance(value, DiagnosticEvent):
            raise TypeError(
                f"actualEvent must be DiagnosticEvent or None, got {type(value).__name__}"
            )
        self._actualEvent = value
        # This represents the reference to the alias event.
        self._aliasEventEvent: Optional["DiagnosticFimAlias"] = None

    @property
    def alias_event_event(self) -> Optional["DiagnosticFimAlias"]:
        """Get aliasEventEvent (Pythonic accessor)."""
        return self._aliasEventEvent

    @alias_event_event.setter
    def alias_event_event(self, value: Optional["DiagnosticFimAlias"]) -> None:
        """
        Set aliasEventEvent with validation.

        Args:
            value: The aliasEventEvent to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._aliasEventEvent = None
            return

        if not isinstance(value, DiagnosticFimAlias):
            raise TypeError(
                f"aliasEventEvent must be DiagnosticFimAlias or None, got {type(value).__name__}"
            )
        self._aliasEventEvent = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getActualEvent(self) -> "DiagnosticEvent":
        """
        AUTOSAR-compliant getter for actualEvent.

        Returns:
            The actualEvent value

        Note:
            Delegates to actual_event property (CODING_RULE_V2_00017)
        """
        return self.actual_event  # Delegates to property

    def setActualEvent(self, value: "DiagnosticEvent") -> "DiagnosticFimAliasEventMapping":
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

    def getAliasEventEvent(self) -> "DiagnosticFimAlias":
        """
        AUTOSAR-compliant getter for aliasEventEvent.

        Returns:
            The aliasEventEvent value

        Note:
            Delegates to alias_event_event property (CODING_RULE_V2_00017)
        """
        return self.alias_event_event  # Delegates to property

    def setAliasEventEvent(self, value: "DiagnosticFimAlias") -> "DiagnosticFimAliasEventMapping":
        """
        AUTOSAR-compliant setter for aliasEventEvent with method chaining.

        Args:
            value: The aliasEventEvent to set

        Returns:
            self for method chaining

        Note:
            Delegates to alias_event_event property setter (gets validation automatically)
        """
        self.alias_event_event = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_actual_event(self, value: Optional["DiagnosticEvent"]) -> "DiagnosticFimAliasEventMapping":
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

    def with_alias_event_event(self, value: Optional["DiagnosticFimAlias"]) -> "DiagnosticFimAliasEventMapping":
        """
        Set aliasEventEvent and return self for chaining.

        Args:
            value: The aliasEventEvent to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_alias_event_event("value")
        """
        self.alias_event_event = value  # Use property setter (gets validation)
        return self
