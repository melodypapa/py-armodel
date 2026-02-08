from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class List(Paginateable):
    """
    This meta-class represents the ability to express a list. The kind of list
    is specified in the attribute.

    Package: M2::MSR::Documentation::BlockElements::ListElements

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 295, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # block.
        # Therefore lists can be arbitrarily is discouraged to have a very deep
                # nesting.
        # atpVariation.
        self._item: "Item" = None

    @property
    def item(self) -> "Item":
        """Get item (Pythonic accessor)."""
        return self._item

    @item.setter
    def item(self, value: "Item") -> None:
        """
        Set item with validation.

        Args:
            value: The item to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, Item):
            raise TypeError(
                f"item must be Item, got {type(value).__name__}"
            )
        self._item = value
        # The type of the list.
        # Default is "UNNUMBER".
        self._type: RefType = None

    @property
    def type(self) -> RefType:
        """Get type (Pythonic accessor)."""
        return self._type

    @type.setter
    def type(self, value: RefType) -> None:
        """
        Set type with validation.

        Args:
            value: The type to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._type = None
            return

        self._type = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getItem(self) -> "Item":
        """
        AUTOSAR-compliant getter for item.

        Returns:
            The item value

        Note:
            Delegates to item property (CODING_RULE_V2_00017)
        """
        return self.item  # Delegates to property

    def setItem(self, value: "Item") -> "List":
        """
        AUTOSAR-compliant setter for item with method chaining.

        Args:
            value: The item to set

        Returns:
            self for method chaining

        Note:
            Delegates to item property setter (gets validation automatically)
        """
        self.item = value  # Delegates to property setter
        return self

    def getType(self) -> RefType:
        """
        AUTOSAR-compliant getter for type.

        Returns:
            The type value

        Note:
            Delegates to type property (CODING_RULE_V2_00017)
        """
        return self.type  # Delegates to property

    def setType(self, value: RefType) -> "List":
        """
        AUTOSAR-compliant setter for type with method chaining.

        Args:
            value: The type to set

        Returns:
            self for method chaining

        Note:
            Delegates to type property setter (gets validation automatically)
        """
        self.type = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_item(self, value: "Item") -> "List":
        """
        Set item and return self for chaining.

        Args:
            value: The item to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_item("value")
        """
        self.item = value  # Use property setter (gets validation)
        return self

    def with_type(self, value: Optional[RefType]) -> "List":
        """
        Set type and return self for chaining.

        Args:
            value: The type to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_type("value")
        """
        self.type = value  # Use property setter (gets validation)
        return self
