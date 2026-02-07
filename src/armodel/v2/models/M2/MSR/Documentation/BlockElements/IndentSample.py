from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

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
        self._l2: "LOverviewParagraph" = None

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