from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class TopicContent(ARObject):
    """
    This meta-class represents the content of a topic. It is mainly a
    documentation block, but can also be a table.

    Package: M2::MSR::Documentation::Chapters::TopicContent

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 478, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is that part of the content which may also occur in a cell.
        self._blockLevel: "DocumentationBlock" = None

    @property
    def block_level(self) -> "DocumentationBlock":
        """Get blockLevel (Pythonic accessor)."""
        return self._blockLevel

    @block_level.setter
    def block_level(self, value: "DocumentationBlock") -> None:
        """
        Set blockLevel with validation.

        Args:
            value: The blockLevel to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, DocumentationBlock):
            raise TypeError(
                f"blockLevel must be DocumentationBlock, got {type(value).__name__}"
            )
        self._blockLevel = value
        # This represents a table within a topic.
        # atpVariation.
        self._table: Optional["Table"] = None

    @property
    def table(self) -> Optional["Table"]:
        """Get table (Pythonic accessor)."""
        return self._table

    @table.setter
    def table(self, value: Optional["Table"]) -> None:
        """
        Set table with validation.

        Args:
            value: The table to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._table = None
            return

        if not isinstance(value, Table):
            raise TypeError(
                f"table must be Table or None, got {type(value).__name__}"
            )
        self._table = value
        # This represents a traceable table within a topic.
        self._traceableTable: "TraceableTable" = None

    @property
    def traceable_table(self) -> "TraceableTable":
        """Get traceableTable (Pythonic accessor)."""
        return self._traceableTable

    @traceable_table.setter
    def traceable_table(self, value: "TraceableTable") -> None:
        """
        Set traceableTable with validation.

        Args:
            value: The traceableTable to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, TraceableTable):
            raise TypeError(
                f"traceableTable must be TraceableTable, got {type(value).__name__}"
            )
        self._traceableTable = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBlockLevel(self) -> "DocumentationBlock":
        """
        AUTOSAR-compliant getter for blockLevel.

        Returns:
            The blockLevel value

        Note:
            Delegates to block_level property (CODING_RULE_V2_00017)
        """
        return self.block_level  # Delegates to property

    def setBlockLevel(self, value: "DocumentationBlock") -> "TopicContent":
        """
        AUTOSAR-compliant setter for blockLevel with method chaining.

        Args:
            value: The blockLevel to set

        Returns:
            self for method chaining

        Note:
            Delegates to block_level property setter (gets validation automatically)
        """
        self.block_level = value  # Delegates to property setter
        return self

    def getTable(self) -> "Table":
        """
        AUTOSAR-compliant getter for table.

        Returns:
            The table value

        Note:
            Delegates to table property (CODING_RULE_V2_00017)
        """
        return self.table  # Delegates to property

    def setTable(self, value: "Table") -> "TopicContent":
        """
        AUTOSAR-compliant setter for table with method chaining.

        Args:
            value: The table to set

        Returns:
            self for method chaining

        Note:
            Delegates to table property setter (gets validation automatically)
        """
        self.table = value  # Delegates to property setter
        return self

    def getTraceableTable(self) -> "TraceableTable":
        """
        AUTOSAR-compliant getter for traceableTable.

        Returns:
            The traceableTable value

        Note:
            Delegates to traceable_table property (CODING_RULE_V2_00017)
        """
        return self.traceable_table  # Delegates to property

    def setTraceableTable(self, value: "TraceableTable") -> "TopicContent":
        """
        AUTOSAR-compliant setter for traceableTable with method chaining.

        Args:
            value: The traceableTable to set

        Returns:
            self for method chaining

        Note:
            Delegates to traceable_table property setter (gets validation automatically)
        """
        self.traceable_table = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_block_level(self, value: "DocumentationBlock") -> "TopicContent":
        """
        Set blockLevel and return self for chaining.

        Args:
            value: The blockLevel to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_block_level("value")
        """
        self.block_level = value  # Use property setter (gets validation)
        return self

    def with_table(self, value: Optional["Table"]) -> "TopicContent":
        """
        Set table and return self for chaining.

        Args:
            value: The table to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_table("value")
        """
        self.table = value  # Use property setter (gets validation)
        return self

    def with_traceable_table(self, value: "TraceableTable") -> "TopicContent":
        """
        Set traceableTable and return self for chaining.

        Args:
            value: The traceableTable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_traceable_table("value")
        """
        self.traceable_table = value  # Use property setter (gets validation)
        return self
