from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class DefItem(Paginateable):
    """
    This represents an entry in a definition list. The defined item is specified
    using shortName and longName.

    Package: M2::MSR::Documentation::BlockElements::ListElements::DefItem

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 298, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the definition part of the DefItem.
        # Contains the actual definition or description text for a term in a definition list.
        self._definition: "DocumentationBlock" = None

    @property
    def definition(self) -> "DocumentationBlock":
        """Get definition (Pythonic accessor) - the definition text for a definition list item."""
        return self._definition

    @definition.setter
    def definition(self, value: "DocumentationBlock") -> None:
        """
        Set definition with validation.

        Args:
            value: The definition to set (definition text block)

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, DocumentationBlock):
            raise TypeError(
                f"definition must be DocumentationBlock, got {type(value).__name__}"
            )
        self._definition = value
        # This specifies an entry point in an online help system to with the parent
                # class.
        # The syntax shall be the applied help system respectively help.
        self._helpEntry: Optional["String"] = None

    @property
    def help_entry(self) -> Optional["String"]:
        """Get helpEntry (Pythonic accessor)."""
        return self._helpEntry

    @help_entry.setter
    def help_entry(self, value: Optional["String"]) -> None:
        """
        Set helpEntry with validation.

        Args:
            value: The helpEntry to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._helpEntry = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"helpEntry must be String or None, got {type(value).__name__}"
            )
        self._helpEntry = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDef(self) -> "DocumentationBlock":
        """
        AUTOSAR-compliant getter for def.

        Returns:
            The def value (definition text block)

        Note:
            Delegates to definition property (CODING_RULE_V2_00017)
        """
        return self.definition  # Delegates to property

    def setDef(self, value: "DocumentationBlock") -> "DefItem":
        """
        AUTOSAR-compliant setter for def with method chaining.

        Args:
            value: The def to set (definition text block)

        Returns:
            self for method chaining

        Note:
            Delegates to definition property setter (gets validation automatically)
        """
        self.definition = value  # Delegates to property setter
        return self

    def getHelpEntry(self) -> "String":
        """
        AUTOSAR-compliant getter for helpEntry.

        Returns:
            The helpEntry value

        Note:
            Delegates to help_entry property (CODING_RULE_V2_00017)
        """
        return self.help_entry  # Delegates to property

    def setHelpEntry(self, value: "String") -> "DefItem":
        """
        AUTOSAR-compliant setter for helpEntry with method chaining.

        Args:
            value: The helpEntry to set

        Returns:
            self for method chaining

        Note:
            Delegates to help_entry property setter (gets validation automatically)
        """
        self.help_entry = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_def(self, value: "DocumentationBlock") -> "DefItem":
        """
        Set def and return self for chaining.

        Args:
            value: The def to set (definition text block)

        Returns:
            self for method chaining

        Example:
            >>> obj.with_def("value")
        """
        self.definition = value  # Use property setter (gets validation)
        return self

    def with_help_entry(self, value: Optional["String"]) -> "DefItem":
        """
        Set helpEntry and return self for chaining.

        Args:
            value: The helpEntry to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_help_entry("value")
        """
        self.help_entry = value  # Use property setter (gets validation)
        return self
