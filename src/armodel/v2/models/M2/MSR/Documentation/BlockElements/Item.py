from armodel.v2.models.M2.MSR.Documentation.DocumentationBlock import (
    DocumentationBlock,
)


class Item(Paginateable):
    """
    This meta-class represents one particular item in a list.

    Package: M2::MSR::Documentation::BlockElements::ListElements

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 295, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # this represents the actual content of the item.
        # It is a DocumentationBlock.
        # This way it is use simple paragraphs to nested lists, or notes.
        self._itemContents: "DocumentationBlock" = None

    @property
    def item_contents(self) -> "DocumentationBlock":
        """Get itemContents (Pythonic accessor)."""
        return self._itemContents

    @item_contents.setter
    def item_contents(self, value: "DocumentationBlock") -> None:
        """
        Set itemContents with validation.

        Args:
            value: The itemContents to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, DocumentationBlock):
            raise TypeError(
                f"itemContents must be DocumentationBlock, got {type(value).__name__}"
            )
        self._itemContents = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getItemContents(self) -> "DocumentationBlock":
        """
        AUTOSAR-compliant getter for itemContents.

        Returns:
            The itemContents value

        Note:
            Delegates to item_contents property (CODING_RULE_V2_00017)
        """
        return self.item_contents  # Delegates to property

    def setItemContents(self, value: "DocumentationBlock") -> "Item":
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_item_contents(self, value: "DocumentationBlock") -> "Item":
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
