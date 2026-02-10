"""
AUTOSAR Package - ListElements

Package: M2::MSR::Documentation::BlockElements::ListElements
"""

from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
    String,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)
from armodel.v2.models.M2.MSR.Documentation.BlockElements.PaginationAndView import (
    Paginateable,
)


class List(Paginateable):
    """
    This meta-class represents the ability to express a list. The kind of list
    is specified in the attribute.
    
    Package: M2::MSR::Documentation::BlockElements::ListElements::List
    
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
        # Default is "UNNUMBER".
        self._type: Optional["RefType"] = None

    @property
    def type(self) -> Optional["RefType"]:
        """Get type (Pythonic accessor)."""
        return self._type

    @type.setter
    def type(self, value: Optional["RefType"]) -> None:
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

    def getType(self) -> "RefType":
        """
        AUTOSAR-compliant getter for type.
        
        Returns:
            The type value
        
        Note:
            Delegates to type property (CODING_RULE_V2_00017)
        """
        return self.type  # Delegates to property

    def setType(self, value: "RefType") -> "List":
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



class Item(Paginateable):
    """
    This meta-class represents one particular item in a list.
    
    Package: M2::MSR::Documentation::BlockElements::ListElements::Item
    
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



class LabeledList(Paginateable):
    """
    This meta-class represents a labeled list, in which items have a label and a
    content. The policy how to render such items is specified in the labeled
    list.
    
    Package: M2::MSR::Documentation::BlockElements::ListElements::LabeledList
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 296, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is a sample item.
        # This sample is used by a rendering measure out the width of indentation.
        # Since this the particular fontsize etc.
        # the indentation specified e.
        # g.
        # in mm.
        self._indentSample: Optional["IndentSample"] = None

    @property
    def indent_sample(self) -> Optional["IndentSample"]:
        """Get indentSample (Pythonic accessor)."""
        return self._indentSample

    @indent_sample.setter
    def indent_sample(self, value: Optional["IndentSample"]) -> None:
        """
        Set indentSample with validation.
        
        Args:
            value: The indentSample to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._indentSample = None
            return

        if not isinstance(value, IndentSample):
            raise TypeError(
                f"indentSample must be IndentSample or None, got {type(value).__name__}"
            )
        self._indentSample = value
        self._labeledItemLabel: "LabeledItem" = None

    @property
    def labeled_item_label(self) -> "LabeledItem":
        """Get labeledItemLabel (Pythonic accessor)."""
        return self._labeledItemLabel

    @labeled_item_label.setter
    def labeled_item_label(self, value: "LabeledItem") -> None:
        """
        Set labeledItemLabel with validation.
        
        Args:
            value: The labeledItemLabel to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, LabeledItem):
            raise TypeError(
                f"labeledItemLabel must be LabeledItem, got {type(value).__name__}"
            )
        self._labeledItemLabel = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIndentSample(self) -> "IndentSample":
        """
        AUTOSAR-compliant getter for indentSample.
        
        Returns:
            The indentSample value
        
        Note:
            Delegates to indent_sample property (CODING_RULE_V2_00017)
        """
        return self.indent_sample  # Delegates to property

    def setIndentSample(self, value: "IndentSample") -> "LabeledList":
        """
        AUTOSAR-compliant setter for indentSample with method chaining.
        
        Args:
            value: The indentSample to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to indent_sample property setter (gets validation automatically)
        """
        self.indent_sample = value  # Delegates to property setter
        return self

    def getLabeledItemLabel(self) -> "LabeledItem":
        """
        AUTOSAR-compliant getter for labeledItemLabel.
        
        Returns:
            The labeledItemLabel value
        
        Note:
            Delegates to labeled_item_label property (CODING_RULE_V2_00017)
        """
        return self.labeled_item_label  # Delegates to property

    def setLabeledItemLabel(self, value: "LabeledItem") -> "LabeledList":
        """
        AUTOSAR-compliant setter for labeledItemLabel with method chaining.
        
        Args:
            value: The labeledItemLabel to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to labeled_item_label property setter (gets validation automatically)
        """
        self.labeled_item_label = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_indent_sample(self, value: Optional["IndentSample"]) -> "LabeledList":
        """
        Set indentSample and return self for chaining.
        
        Args:
            value: The indentSample to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_indent_sample("value")
        """
        self.indent_sample = value  # Use property setter (gets validation)
        return self

    def with_labeled_item_label(self, value: "LabeledItem") -> "LabeledList":
        """
        Set labeledItemLabel and return self for chaining.
        
        Args:
            value: The labeledItemLabel to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_labeled_item_label("value")
        """
        self.labeled_item_label = value  # Use property setter (gets validation)
        return self



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

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"helpEntry must be String or str or None, got {type(value).__name__}"
            )
        self._helpEntry = value
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



class IndentSample(ARObject):
    """
    This represents the ability to specify indentation of a labeled list by
    providing a sample content. This content can be measured by the rendering
    system in order to determine the width of indentation.
    
    Package: M2::MSR::Documentation::BlockElements::ListElements::IndentSample
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 297, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The position of the label in case the label is too long.
        # The "NO-NEWLINE".
        self._itemLabelPos: Optional["ItemLabelPosEnum"] = None

    @property
    def item_label_pos(self) -> Optional["ItemLabelPosEnum"]:
        """Get itemLabelPos (Pythonic accessor)."""
        return self._itemLabelPos

    @item_label_pos.setter
    def item_label_pos(self, value: Optional["ItemLabelPosEnum"]) -> None:
        """
        Set itemLabelPos with validation.
        
        Args:
            value: The itemLabelPos to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._itemLabelPos = None
            return

        if not isinstance(value, ItemLabelPosEnum):
            raise TypeError(
                f"itemLabelPos must be ItemLabelPosEnum or None, got {type(value).__name__}"
            )
        self._itemLabelPos = value

    @property
    def l2(self) -> "LOverviewParagraph":
        """Get l2 (Pythonic accessor)."""
        return self._l2

    @l2.setter
    def l2(self, value: "LOverviewParagraph") -> None:
        """
        Set l2 with validation.
        
        Args:
            value: The l2 to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, LOverviewParagraph):
            raise TypeError(
                f"l2 must be LOverviewParagraph, got {type(value).__name__}"
            )
        self._l2 = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getItemLabelPos(self) -> "ItemLabelPosEnum":
        """
        AUTOSAR-compliant getter for itemLabelPos.
        
        Returns:
            The itemLabelPos value
        
        Note:
            Delegates to item_label_pos property (CODING_RULE_V2_00017)
        """
        return self.item_label_pos  # Delegates to property

    def setItemLabelPos(self, value: "ItemLabelPosEnum") -> "IndentSample":
        """
        AUTOSAR-compliant setter for itemLabelPos with method chaining.
        
        Args:
            value: The itemLabelPos to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to item_label_pos property setter (gets validation automatically)
        """
        self.item_label_pos = value  # Delegates to property setter
        return self

    def getL2(self) -> "LOverviewParagraph":
        """
        AUTOSAR-compliant getter for l2.
        
        Returns:
            The l2 value
        
        Note:
            Delegates to l2 property (CODING_RULE_V2_00017)
        """
        return self.l2  # Delegates to property

    def setL2(self, value: "LOverviewParagraph") -> "IndentSample":
        """
        AUTOSAR-compliant setter for l2 with method chaining.
        
        Args:
            value: The l2 to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to l2 property setter (gets validation automatically)
        """
        self.l2 = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_item_label_pos(self, value: Optional["ItemLabelPosEnum"]) -> "IndentSample":
        """
        Set itemLabelPos and return self for chaining.
        
        Args:
            value: The itemLabelPos to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_item_label_pos("value")
        """
        self.item_label_pos = value  # Use property setter (gets validation)
        return self

    def with_l2(self, value: "LOverviewParagraph") -> "IndentSample":
        """
        Set l2 and return self for chaining.
        
        Args:
            value: The l2 to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_l2("value")
        """
        self.l2 = value  # Use property setter (gets validation)
        return self



class DefList(Paginateable):
    """
    This meta-class represents the ability to express a list of definitions.
    Note that a definition list might be rendered similar to a labeled list but
    has a particular semantics to denote definitions.
    
    Package: M2::MSR::Documentation::BlockElements::ListElements::DefList
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 297, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # atpVariation.
        self._defItem: "DefItem" = None

    @property
    def def_item(self) -> "DefItem":
        """Get defItem (Pythonic accessor)."""
        return self._defItem

    @def_item.setter
    def def_item(self, value: "DefItem") -> None:
        """
        Set defItem with validation.
        
        Args:
            value: The defItem to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, DefItem):
            raise TypeError(
                f"defItem must be DefItem, got {type(value).__name__}"
            )
        self._defItem = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDefItem(self) -> "DefItem":
        """
        AUTOSAR-compliant getter for defItem.
        
        Returns:
            The defItem value
        
        Note:
            Delegates to def_item property (CODING_RULE_V2_00017)
        """
        return self.def_item  # Delegates to property

    def setDefItem(self, value: "DefItem") -> "DefList":
        """
        AUTOSAR-compliant setter for defItem with method chaining.
        
        Args:
            value: The defItem to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to def_item property setter (gets validation automatically)
        """
        self.def_item = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_def_item(self, value: "DefItem") -> "DefList":
        """
        Set defItem and return self for chaining.
        
        Args:
            value: The defItem to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_def_item("value")
        """
        self.def_item = value  # Use property setter (gets validation)
        return self



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
        self._definition: "DocumentationBlock" = None

    @property
    def definition(self) -> "DocumentationBlock":
        """Get definition (Pythonic accessor)."""
        return self._definition

    @definition.setter
    def definition(self, value: "DocumentationBlock") -> None:
        """
        Set definition with validation.
        
        Args:
            value: The definition to set
        
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

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"helpEntry must be String or str or None, got {type(value).__name__}"
            )
        self._helpEntry = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDef(self) -> "DocumentationBlock":
        """
        AUTOSAR-compliant getter for def.
        
        Returns:
            The definition value
        
        Note:
            Delegates to definition property (CODING_RULE_V2_00017)
        """
        return self.definition  # Delegates to property

    def setDefinition(self, value: "DocumentationBlock") -> "DefItem":
        """
        AUTOSAR-compliant setter for definition with method chaining.
        
        Args:
            value: The definition to set
        
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
            value: The def to set
        
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


class ListEnum(AREnum):
    """
    ListEnum enumeration

This meta-class represents the notation of the various types of lists. Aggregated by List.type

Package: M2::MSR::Documentation::BlockElements::ListElements
    """
    # This indicates that the list is an numerated list.
    number = "0"

    # This indicates that it is an enumeration (bulleted list)
    unnumber = "1"



class ItemLabelPosEnum(AREnum):
    """
    ItemLabelPosEnum enumeration

This enumerator specifies, how the label of a labeled list shall be rendered. Aggregated by IndentSample.itemLabelPos

Package: M2::MSR::Documentation::BlockElements::ListElements
    """
    # The label is renders in a new line.
    newline = "0"

    # The label is rendered in a new line if it is longer than the indentation.
    newlineIfNecessary = "1"

    # The label is rendered in one line with the item even if it is longer than the indentation.
    noNewline = "2"
