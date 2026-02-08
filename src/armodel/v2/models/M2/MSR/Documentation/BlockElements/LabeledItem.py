from typing import Optional


class LabeledItem(Paginateable):
    """
    this represents an item of a labeled list.

    Package: M2::MSR::Documentation::BlockElements::ListElements::LabeledItem

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 296, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
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
        # This represents the actual content of the item.
        # It is a DocumentationBlock.
        # This way it is use simple paragraphs to nested lists, or notes.
        self._itemContents: Optional["DocumentationBlock"] = None

    @property
    def item_contents(self) -> Optional["DocumentationBlock"]:
        """Get itemContents (Pythonic accessor)."""
        return self._itemContents

    @item_contents.setter
    def item_contents(self, value: Optional["DocumentationBlock"]) -> None:
        """
        Set itemContents with validation.

        Args:
            value: The itemContents to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._itemContents = None
            return

        if not isinstance(value, DocumentationBlock):
            raise TypeError(
                f"itemContents must be DocumentationBlock or None, got {type(value).__name__}"
            )
        self._itemContents = value
        # This is the label of the item.
        # xml.
        # sequenceOffset=20.
        self._itemLabel: "MultiLanguageOverview" = None

    @property
    def item_label(self) -> "MultiLanguageOverview":
        """Get itemLabel (Pythonic accessor)."""
        return self._itemLabel

    @item_label.setter
    def item_label(self, value: "MultiLanguageOverview") -> None:
        """
        Set itemLabel with validation.

        Args:
            value: The itemLabel to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, MultiLanguageOverview):
            raise TypeError(
                f"itemLabel must be MultiLanguageOverview, got {type(value).__name__}"
            )
        self._itemLabel = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getHelpEntry(self) -> "String":
        """
        AUTOSAR-compliant getter for helpEntry.

        Returns:
            The helpEntry value

        Note:
            Delegates to help_entry property (CODING_RULE_V2_00017)
        """
        return self.help_entry  # Delegates to property

    def setHelpEntry(self, value: "String") -> "LabeledItem":
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

    def getItemContents(self) -> "DocumentationBlock":
        """
        AUTOSAR-compliant getter for itemContents.

        Returns:
            The itemContents value

        Note:
            Delegates to item_contents property (CODING_RULE_V2_00017)
        """
        return self.item_contents  # Delegates to property

    def setItemContents(self, value: "DocumentationBlock") -> "LabeledItem":
        """
        AUTOSAR-compliant setter for itemContents with method chaining.

        Args:
            value: The itemContents to set

        Returns:
            self for method chaining

        Note:
            Delegates to item_contents property setter (gets validation automatically)
        """
        self.item_contents = value  # Delegates to property setter
        return self

    def getItemLabel(self) -> "MultiLanguageOverview":
        """
        AUTOSAR-compliant getter for itemLabel.

        Returns:
            The itemLabel value

        Note:
            Delegates to item_label property (CODING_RULE_V2_00017)
        """
        return self.item_label  # Delegates to property

    def setItemLabel(self, value: "MultiLanguageOverview") -> "LabeledItem":
        """
        AUTOSAR-compliant setter for itemLabel with method chaining.

        Args:
            value: The itemLabel to set

        Returns:
            self for method chaining

        Note:
            Delegates to item_label property setter (gets validation automatically)
        """
        self.item_label = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_help_entry(self, value: Optional["String"]) -> "LabeledItem":
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

    def with_item_contents(self, value: Optional["DocumentationBlock"]) -> "LabeledItem":
        """
        Set itemContents and return self for chaining.

        Args:
            value: The itemContents to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_item_contents("value")
        """
        self.item_contents = value  # Use property setter (gets validation)
        return self

    def with_item_label(self, value: "MultiLanguageOverview") -> "LabeledItem":
        """
        Set itemLabel and return self for chaining.

        Args:
            value: The itemLabel to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_item_label("value")
        """
        self.item_label = value  # Use property setter (gets validation)
        return self
