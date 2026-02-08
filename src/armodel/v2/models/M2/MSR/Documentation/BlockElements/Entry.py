from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class Entry(ARObject):
    """
    This represents one particular table cell.

    Package: M2::MSR::Documentation::BlockElements::OasisExchangeTable

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 336, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies how the cell ENTRY shall be horizontally is "LEFT".
        self._align: Optional["AlignEnum"] = None

    @property
    def align(self) -> Optional["AlignEnum"]:
        """Get align (Pythonic accessor)."""
        return self._align

    @align.setter
    def align(self, value: Optional["AlignEnum"]) -> None:
        """
        Set align with validation.

        Args:
            value: The align to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._align = None
            return

        if not isinstance(value, AlignEnum):
            raise TypeError(
                f"align must be AlignEnum or None, got {type(value).__name__}"
            )
        self._align = value
        # This allows to recommend a background color of the is specified bases on 6
                # digits RGB hex-code.
        # 535 Document ID 202: AUTOSAR_FO_TPS_GenericStructureTemplate Template R23-11.
        self._bgcolor: "String" = None

    @property
    def bgcolor(self) -> "String":
        """Get bgcolor (Pythonic accessor)."""
        return self._bgcolor

    @bgcolor.setter
    def bgcolor(self, value: "String") -> None:
        """
        Set bgcolor with validation.

        Args:
            value: The bgcolor to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, String):
            raise TypeError(
                f"bgcolor must be String, got {type(value).__name__}"
            )
        self._bgcolor = value
        # Indicate the name of the column, where the entry should.
        self._colname: Optional["String"] = None

    @property
    def colname(self) -> Optional["String"]:
        """Get colname (Pythonic accessor)."""
        return self._colname

    @colname.setter
    def colname(self, value: Optional["String"]) -> None:
        """
        Set colname with validation.

        Args:
            value: The colname to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._colname = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"colname must be String or None, got {type(value).__name__}"
            )
        self._colname = value
        # Indicates whether a line should be displayed end of this.
        self._colsep: Optional["TableSeparatorString"] = None

    @property
    def colsep(self) -> Optional["TableSeparatorString"]:
        """Get colsep (Pythonic accessor)."""
        return self._colsep

    @colsep.setter
    def colsep(self, value: Optional["TableSeparatorString"]) -> None:
        """
        Set colsep with validation.

        Args:
            value: The colsep to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._colsep = None
            return

        if not isinstance(value, TableSeparatorString):
            raise TypeError(
                f"colsep must be TableSeparatorString or None, got {type(value).__name__}"
            )
        self._colsep = value
        # This is the content of the TableEntry.
        self._entryContents: "DocumentationBlock" = None

    @property
    def entry_contents(self) -> "DocumentationBlock":
        """Get entryContents (Pythonic accessor)."""
        return self._entryContents

    @entry_contents.setter
    def entry_contents(self, value: "DocumentationBlock") -> None:
        """
        Set entryContents with validation.

        Args:
            value: The entryContents to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, DocumentationBlock):
            raise TypeError(
                f"entryContents must be DocumentationBlock, got {type(value).__name__}"
            )
        self._entryContents = value
        # Number of additional rows.
        # Default is "0".
        self._morerows: Optional["String"] = None

    @property
    def morerows(self) -> Optional["String"]:
        """Get morerows (Pythonic accessor)."""
        return self._morerows

    @morerows.setter
    def morerows(self, value: Optional["String"]) -> None:
        """
        Set morerows with validation.

        Args:
            value: The morerows to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._morerows = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"morerows must be String or None, got {type(value).__name__}"
            )
        self._morerows = value
        # When an entry spans multiple column this is the name of column.
        self._nameend: Optional["String"] = None

    @property
    def nameend(self) -> Optional["String"]:
        """Get nameend (Pythonic accessor)."""
        return self._nameend

    @nameend.setter
    def nameend(self, value: Optional["String"]) -> None:
        """
        Set nameend with validation.

        Args:
            value: The nameend to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nameend = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"nameend must be String or None, got {type(value).__name__}"
            )
        self._nameend = value
        # When an entry spans multiple column this is the name of column.
        self._namest: Optional["String"] = None

    @property
    def namest(self) -> Optional["String"]:
        """Get namest (Pythonic accessor)."""
        return self._namest

    @namest.setter
    def namest(self, value: Optional["String"]) -> None:
        """
        Set namest with validation.

        Args:
            value: The namest to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._namest = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"namest must be String or None, got {type(value).__name__}"
            )
        self._namest = value
        # Indicates if the cellcontent shall be rotated.
        # Default is 0; 1 the contents 90 degree counterclockwise.
        # is defined by OASIS.
        self._rotate: Optional["String"] = None

    @property
    def rotate(self) -> Optional["String"]:
        """Get rotate (Pythonic accessor)."""
        return self._rotate

    @rotate.setter
    def rotate(self, value: Optional["String"]) -> None:
        """
        Set rotate with validation.

        Args:
            value: The rotate to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rotate = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"rotate must be String or None, got {type(value).__name__}"
            )
        self._rotate = value
        # Indicates whether a line should be displayed at the of the cell.
        self._rowsep: Optional["TableSeparatorString"] = None

    @property
    def rowsep(self) -> Optional["TableSeparatorString"]:
        """Get rowsep (Pythonic accessor)."""
        return self._rowsep

    @rowsep.setter
    def rowsep(self, value: Optional["TableSeparatorString"]) -> None:
        """
        Set rowsep with validation.

        Args:
            value: The rowsep to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rowsep = None
            return

        if not isinstance(value, TableSeparatorString):
            raise TypeError(
                f"rowsep must be TableSeparatorString or None, got {type(value).__name__}"
            )
        self._rowsep = value
        # Capture the name of entry merging multiple columns.
        self._spanname: Optional["String"] = None

    @property
    def spanname(self) -> Optional["String"]:
        """Get spanname (Pythonic accessor)."""
        return self._spanname

    @spanname.setter
    def spanname(self, value: Optional["String"]) -> None:
        """
        Set spanname with validation.

        Args:
            value: The spanname to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._spanname = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"spanname must be String or None, got {type(value).__name__}"
            )
        self._spanname = value
        # Indicates how the content of the cell shall be aligned.
        # inherited from row or tbody, otherwise "TOP".
        self._valign: Optional["ValignEnum"] = None

    @property
    def valign(self) -> Optional["ValignEnum"]:
        """Get valign (Pythonic accessor)."""
        return self._valign

    @valign.setter
    def valign(self, value: Optional["ValignEnum"]) -> None:
        """
        Set valign with validation.

        Args:
            value: The valign to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._valign = None
            return

        if not isinstance(value, ValignEnum):
            raise TypeError(
                f"valign must be ValignEnum or None, got {type(value).__name__}"
            )
        self._valign = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAlign(self) -> "AlignEnum":
        """
        AUTOSAR-compliant getter for align.

        Returns:
            The align value

        Note:
            Delegates to align property (CODING_RULE_V2_00017)
        """
        return self.align  # Delegates to property

    def setAlign(self, value: "AlignEnum") -> "Entry":
        """
        AUTOSAR-compliant setter for align with method chaining.

        Args:
            value: The align to set

        Returns:
            self for method chaining

        Note:
            Delegates to align property setter (gets validation automatically)
        """
        self.align = value  # Delegates to property setter
        return self

    def getBgcolor(self) -> "String":
        """
        AUTOSAR-compliant getter for bgcolor.

        Returns:
            The bgcolor value

        Note:
            Delegates to bgcolor property (CODING_RULE_V2_00017)
        """
        return self.bgcolor  # Delegates to property

    def setBgcolor(self, value: "String") -> "Entry":
        """
        AUTOSAR-compliant setter for bgcolor with method chaining.

        Args:
            value: The bgcolor to set

        Returns:
            self for method chaining

        Note:
            Delegates to bgcolor property setter (gets validation automatically)
        """
        self.bgcolor = value  # Delegates to property setter
        return self

    def getColname(self) -> "String":
        """
        AUTOSAR-compliant getter for colname.

        Returns:
            The colname value

        Note:
            Delegates to colname property (CODING_RULE_V2_00017)
        """
        return self.colname  # Delegates to property

    def setColname(self, value: "String") -> "Entry":
        """
        AUTOSAR-compliant setter for colname with method chaining.

        Args:
            value: The colname to set

        Returns:
            self for method chaining

        Note:
            Delegates to colname property setter (gets validation automatically)
        """
        self.colname = value  # Delegates to property setter
        return self

    def getColsep(self) -> "TableSeparatorString":
        """
        AUTOSAR-compliant getter for colsep.

        Returns:
            The colsep value

        Note:
            Delegates to colsep property (CODING_RULE_V2_00017)
        """
        return self.colsep  # Delegates to property

    def setColsep(self, value: "TableSeparatorString") -> "Entry":
        """
        AUTOSAR-compliant setter for colsep with method chaining.

        Args:
            value: The colsep to set

        Returns:
            self for method chaining

        Note:
            Delegates to colsep property setter (gets validation automatically)
        """
        self.colsep = value  # Delegates to property setter
        return self

    def getEntryContents(self) -> "DocumentationBlock":
        """
        AUTOSAR-compliant getter for entryContents.

        Returns:
            The entryContents value

        Note:
            Delegates to entry_contents property (CODING_RULE_V2_00017)
        """
        return self.entry_contents  # Delegates to property

    def setEntryContents(self, value: "DocumentationBlock") -> "Entry":
        """
        AUTOSAR-compliant setter for entryContents with method chaining.

        Args:
            value: The entryContents to set

        Returns:
            self for method chaining

        Note:
            Delegates to entry_contents property setter (gets validation automatically)
        """
        self.entry_contents = value  # Delegates to property setter
        return self

    def getMorerows(self) -> "String":
        """
        AUTOSAR-compliant getter for morerows.

        Returns:
            The morerows value

        Note:
            Delegates to morerows property (CODING_RULE_V2_00017)
        """
        return self.morerows  # Delegates to property

    def setMorerows(self, value: "String") -> "Entry":
        """
        AUTOSAR-compliant setter for morerows with method chaining.

        Args:
            value: The morerows to set

        Returns:
            self for method chaining

        Note:
            Delegates to morerows property setter (gets validation automatically)
        """
        self.morerows = value  # Delegates to property setter
        return self

    def getNameend(self) -> "String":
        """
        AUTOSAR-compliant getter for nameend.

        Returns:
            The nameend value

        Note:
            Delegates to nameend property (CODING_RULE_V2_00017)
        """
        return self.nameend  # Delegates to property

    def setNameend(self, value: "String") -> "Entry":
        """
        AUTOSAR-compliant setter for nameend with method chaining.

        Args:
            value: The nameend to set

        Returns:
            self for method chaining

        Note:
            Delegates to nameend property setter (gets validation automatically)
        """
        self.nameend = value  # Delegates to property setter
        return self

    def getNamest(self) -> "String":
        """
        AUTOSAR-compliant getter for namest.

        Returns:
            The namest value

        Note:
            Delegates to namest property (CODING_RULE_V2_00017)
        """
        return self.namest  # Delegates to property

    def setNamest(self, value: "String") -> "Entry":
        """
        AUTOSAR-compliant setter for namest with method chaining.

        Args:
            value: The namest to set

        Returns:
            self for method chaining

        Note:
            Delegates to namest property setter (gets validation automatically)
        """
        self.namest = value  # Delegates to property setter
        return self

    def getRotate(self) -> "String":
        """
        AUTOSAR-compliant getter for rotate.

        Returns:
            The rotate value

        Note:
            Delegates to rotate property (CODING_RULE_V2_00017)
        """
        return self.rotate  # Delegates to property

    def setRotate(self, value: "String") -> "Entry":
        """
        AUTOSAR-compliant setter for rotate with method chaining.

        Args:
            value: The rotate to set

        Returns:
            self for method chaining

        Note:
            Delegates to rotate property setter (gets validation automatically)
        """
        self.rotate = value  # Delegates to property setter
        return self

    def getRowsep(self) -> "TableSeparatorString":
        """
        AUTOSAR-compliant getter for rowsep.

        Returns:
            The rowsep value

        Note:
            Delegates to rowsep property (CODING_RULE_V2_00017)
        """
        return self.rowsep  # Delegates to property

    def setRowsep(self, value: "TableSeparatorString") -> "Entry":
        """
        AUTOSAR-compliant setter for rowsep with method chaining.

        Args:
            value: The rowsep to set

        Returns:
            self for method chaining

        Note:
            Delegates to rowsep property setter (gets validation automatically)
        """
        self.rowsep = value  # Delegates to property setter
        return self

    def getSpanname(self) -> "String":
        """
        AUTOSAR-compliant getter for spanname.

        Returns:
            The spanname value

        Note:
            Delegates to spanname property (CODING_RULE_V2_00017)
        """
        return self.spanname  # Delegates to property

    def setSpanname(self, value: "String") -> "Entry":
        """
        AUTOSAR-compliant setter for spanname with method chaining.

        Args:
            value: The spanname to set

        Returns:
            self for method chaining

        Note:
            Delegates to spanname property setter (gets validation automatically)
        """
        self.spanname = value  # Delegates to property setter
        return self

    def getValign(self) -> "ValignEnum":
        """
        AUTOSAR-compliant getter for valign.

        Returns:
            The valign value

        Note:
            Delegates to valign property (CODING_RULE_V2_00017)
        """
        return self.valign  # Delegates to property

    def setValign(self, value: "ValignEnum") -> "Entry":
        """
        AUTOSAR-compliant setter for valign with method chaining.

        Args:
            value: The valign to set

        Returns:
            self for method chaining

        Note:
            Delegates to valign property setter (gets validation automatically)
        """
        self.valign = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_align(self, value: Optional["AlignEnum"]) -> "Entry":
        """
        Set align and return self for chaining.

        Args:
            value: The align to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_align("value")
        """
        self.align = value  # Use property setter (gets validation)
        return self

    def with_bgcolor(self, value: "String") -> "Entry":
        """
        Set bgcolor and return self for chaining.

        Args:
            value: The bgcolor to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bgcolor("value")
        """
        self.bgcolor = value  # Use property setter (gets validation)
        return self

    def with_colname(self, value: Optional["String"]) -> "Entry":
        """
        Set colname and return self for chaining.

        Args:
            value: The colname to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_colname("value")
        """
        self.colname = value  # Use property setter (gets validation)
        return self

    def with_colsep(self, value: Optional["TableSeparatorString"]) -> "Entry":
        """
        Set colsep and return self for chaining.

        Args:
            value: The colsep to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_colsep("value")
        """
        self.colsep = value  # Use property setter (gets validation)
        return self

    def with_entry_contents(self, value: "DocumentationBlock") -> "Entry":
        """
        Set entryContents and return self for chaining.

        Args:
            value: The entryContents to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_entry_contents("value")
        """
        self.entry_contents = value  # Use property setter (gets validation)
        return self

    def with_morerows(self, value: Optional["String"]) -> "Entry":
        """
        Set morerows and return self for chaining.

        Args:
            value: The morerows to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_morerows("value")
        """
        self.morerows = value  # Use property setter (gets validation)
        return self

    def with_nameend(self, value: Optional["String"]) -> "Entry":
        """
        Set nameend and return self for chaining.

        Args:
            value: The nameend to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nameend("value")
        """
        self.nameend = value  # Use property setter (gets validation)
        return self

    def with_namest(self, value: Optional["String"]) -> "Entry":
        """
        Set namest and return self for chaining.

        Args:
            value: The namest to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_namest("value")
        """
        self.namest = value  # Use property setter (gets validation)
        return self

    def with_rotate(self, value: Optional["String"]) -> "Entry":
        """
        Set rotate and return self for chaining.

        Args:
            value: The rotate to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rotate("value")
        """
        self.rotate = value  # Use property setter (gets validation)
        return self

    def with_rowsep(self, value: Optional["TableSeparatorString"]) -> "Entry":
        """
        Set rowsep and return self for chaining.

        Args:
            value: The rowsep to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rowsep("value")
        """
        self.rowsep = value  # Use property setter (gets validation)
        return self

    def with_spanname(self, value: Optional["String"]) -> "Entry":
        """
        Set spanname and return self for chaining.

        Args:
            value: The spanname to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_spanname("value")
        """
        self.spanname = value  # Use property setter (gets validation)
        return self

    def with_valign(self, value: Optional["ValignEnum"]) -> "Entry":
        """
        Set valign and return self for chaining.

        Args:
            value: The valign to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_valign("value")
        """
        self.valign = value  # Use property setter (gets validation)
        return self
