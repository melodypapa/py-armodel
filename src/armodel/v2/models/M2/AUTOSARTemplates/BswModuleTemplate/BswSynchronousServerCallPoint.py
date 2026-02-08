from typing import Optional


class BswSynchronousServerCallPoint(BswModuleCallPoint):
    """
    Represents a synchronous procedure call point via the BSW Scheduler.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswSynchronousServerCallPoint

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 79, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The entry to be called.
        self._calledEntryEntry: Optional["BswModuleClientServer"] = None

    @property
    def called_entry_entry(self) -> Optional["BswModuleClientServer"]:
        """Get calledEntryEntry (Pythonic accessor)."""
        return self._calledEntryEntry

    @called_entry_entry.setter
    def called_entry_entry(self, value: Optional["BswModuleClientServer"]) -> None:
        """
        Set calledEntryEntry with validation.

        Args:
            value: The calledEntryEntry to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._calledEntryEntry = None
            return

        if not isinstance(value, BswModuleClientServer):
            raise TypeError(
                f"calledEntryEntry must be BswModuleClientServer or None, got {type(value).__name__}"
            )
        self._calledEntryEntry = value
        # This indicates that the call point is located at the deepest level inside one
        # or more ExclusiveAreas that are nested the given order.
        self._calledFrom: Optional["ExclusiveAreaNesting"] = None

    @property
    def called_from(self) -> Optional["ExclusiveAreaNesting"]:
        """Get calledFrom (Pythonic accessor)."""
        return self._calledFrom

    @called_from.setter
    def called_from(self, value: Optional["ExclusiveAreaNesting"]) -> None:
        """
        Set calledFrom with validation.

        Args:
            value: The calledFrom to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._calledFrom = None
            return

        if not isinstance(value, ExclusiveAreaNesting):
            raise TypeError(
                f"calledFrom must be ExclusiveAreaNesting or None, got {type(value).__name__}"
            )
        self._calledFrom = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCalledEntryEntry(self) -> "BswModuleClientServer":
        """
        AUTOSAR-compliant getter for calledEntryEntry.

        Returns:
            The calledEntryEntry value

        Note:
            Delegates to called_entry_entry property (CODING_RULE_V2_00017)
        """
        return self.called_entry_entry  # Delegates to property

    def setCalledEntryEntry(self, value: "BswModuleClientServer") -> "BswSynchronousServerCallPoint":
        """
        AUTOSAR-compliant setter for calledEntryEntry with method chaining.

        Args:
            value: The calledEntryEntry to set

        Returns:
            self for method chaining

        Note:
            Delegates to called_entry_entry property setter (gets validation automatically)
        """
        self.called_entry_entry = value  # Delegates to property setter
        return self

    def getCalledFrom(self) -> "ExclusiveAreaNesting":
        """
        AUTOSAR-compliant getter for calledFrom.

        Returns:
            The calledFrom value

        Note:
            Delegates to called_from property (CODING_RULE_V2_00017)
        """
        return self.called_from  # Delegates to property

    def setCalledFrom(self, value: "ExclusiveAreaNesting") -> "BswSynchronousServerCallPoint":
        """
        AUTOSAR-compliant setter for calledFrom with method chaining.

        Args:
            value: The calledFrom to set

        Returns:
            self for method chaining

        Note:
            Delegates to called_from property setter (gets validation automatically)
        """
        self.called_from = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_called_entry_entry(self, value: Optional["BswModuleClientServer"]) -> "BswSynchronousServerCallPoint":
        """
        Set calledEntryEntry and return self for chaining.

        Args:
            value: The calledEntryEntry to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_called_entry_entry("value")
        """
        self.called_entry_entry = value  # Use property setter (gets validation)
        return self

    def with_called_from(self, value: Optional["ExclusiveAreaNesting"]) -> "BswSynchronousServerCallPoint":
        """
        Set calledFrom and return self for chaining.

        Args:
            value: The calledFrom to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_called_from("value")
        """
        self.called_from = value  # Use property setter (gets validation)
        return self
