from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    BswModuleCallPoint,
    BswModuleClientServer,
)


class BswAsynchronousServerCallPoint(BswModuleCallPoint):
    """
    Represents an asynchronous procedure call point via the BSW Scheduler.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswAsynchronousServerCallPoint

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 80, Classic
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

    def setCalledEntryEntry(self, value: "BswModuleClientServer") -> "BswAsynchronousServerCallPoint":
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_called_entry_entry(self, value: Optional["BswModuleClientServer"]) -> "BswAsynchronousServerCallPoint":
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
