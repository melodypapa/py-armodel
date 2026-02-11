from armodel.v2.models.M2.MSR.Documentation.BlockElements.PaginationAndView import (
    Paginateable,
)
from typing import Optional


class LabeledList(Paginateable):
    """
    This meta-class represents a labeled list, in which items have a label and a
    content. The policy how to render such items is specified in the labeled
    list.

    Package: M2::MSR::Documentation::BlockElements::ListElements

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
