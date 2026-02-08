from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import BswEvent


class BswOperationInvokedEvent(BswEvent):
    """
    this event is not needed in case of direct function calls.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswOperationInvokedEvent

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 97, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The providedClientServerEntry invoked by this event.
        self._entry: Optional["BswModuleClientServer"] = None

    @property
    def entry(self) -> Optional["BswModuleClientServer"]:
        """Get entry (Pythonic accessor)."""
        return self._entry

    @entry.setter
    def entry(self, value: Optional["BswModuleClientServer"]) -> None:
        """
        Set entry with validation.

        Args:
            value: The entry to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._entry = None
            return

        if not isinstance(value, BswModuleClientServer):
            raise TypeError(
                f"entry must be BswModuleClientServer or None, got {type(value).__name__}"
            )
        self._entry = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEntry(self) -> "BswModuleClientServer":
        """
        AUTOSAR-compliant getter for entry.

        Returns:
            The entry value

        Note:
            Delegates to entry property (CODING_RULE_V2_00017)
        """
        return self.entry  # Delegates to property

    def setEntry(self, value: "BswModuleClientServer") -> "BswOperationInvokedEvent":
        """
        AUTOSAR-compliant setter for entry with method chaining.

        Args:
            value: The entry to set

        Returns:
            self for method chaining

        Note:
            Delegates to entry property setter (gets validation automatically)
        """
        self.entry = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_entry(self, value: Optional["BswModuleClientServer"]) -> "BswOperationInvokedEvent":
        """
        Set entry and return self for chaining.

        Args:
            value: The entry to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_entry("value")
        """
        self.entry = value  # Use property setter (gets validation)
        return self
