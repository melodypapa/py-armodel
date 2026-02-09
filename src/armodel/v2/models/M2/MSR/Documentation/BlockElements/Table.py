from typing import Optional


class Table(Paginateable):
    """
    This class implements an exchange table according to OASIS Technical
    Resolution TR 9503:1995. http://www.oasis-open.org/specs/a503.htm

    Package: M2::MSR::Documentation::BlockElements::OasisExchangeTable

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 332, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Indicates if by default a line should be drawn between the this table.
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
        self._float: "FloatEnum" = None

    @property
    def float(self) -> "FloatEnum":
        """Get float (Pythonic accessor)."""
        return self._float

    @float.setter
    def float(self, value: "FloatEnum") -> None:
        """
        Set float with validation.

        Args:
            value: The float to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, FloatEnum):
            raise TypeError(
                f"float must be FloatEnum, got {type(value).__name__}"
            )
        self._float = value
        # 535 Document ID 202: AUTOSAR_FO_TPS_GenericStructureTemplate Template R23-11.
        self._frame: Optional["FrameEnum"] = None

    @property
    def frame(self) -> Optional["FrameEnum"]:
        """Get frame (Pythonic accessor)."""
        return self._frame

    @frame.setter
    def frame(self, value: Optional["FrameEnum"]) -> None:
        """
        Set frame with validation.

        Args:
            value: The frame to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._frame = None
            return

        if not isinstance(value, FrameEnum):
            raise TypeError(
                f"frame must be FrameEnum or None, got {type(value).__name__}"
            )
        self._frame = value
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
        # : landscape : portrait.
        self._orient: Optional["OrientEnum"] = None

    @property
    def orient(self) -> Optional["OrientEnum"]:
        """Get orient (Pythonic accessor)."""
        return self._orient

    @orient.setter
    def orient(self, value: Optional["OrientEnum"]) -> None:
        """
        Set orient with validation.

        Args:
            value: The orient to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._orient = None
            return

        if not isinstance(value, OrientEnum):
            raise TypeError(
                f"orient must be OrientEnum or None, got {type(value).__name__}"
            )
        self._orient = value
        # or not (value =.
        self._pgwide: Optional["NameToken"] = None

    @property
    def pgwide(self) -> Optional["NameToken"]:
        """Get pgwide (Pythonic accessor)."""
        return self._pgwide

    @pgwide.setter
    def pgwide(self, value: Optional["NameToken"]) -> None:
        """
        Set pgwide with validation.

        Args:
            value: The pgwide to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pgwide = None
            return

        if not isinstance(value, NameToken):
            raise TypeError(
                f"pgwide must be NameToken or None, got {type(value).__name__}"
            )
        self._pgwide = value
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
        self._tableCaption: Optional["Caption"] = None

    @property
    def table_caption(self) -> Optional["Caption"]:
        """Get tableCaption (Pythonic accessor)."""
        return self._tableCaption

    @table_caption.setter
    def table_caption(self, value: Optional["Caption"]) -> None:
        """
        Set tableCaption with validation.

        Args:
            value: The tableCaption to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tableCaption = None
            return

        if not isinstance(value, Caption):
            raise TypeError(
                f"tableCaption must be Caption or None, got {type(value).__name__}"
            )
        self._tableCaption = value
        # Tgroup 1.
        # * aggr A table can be built of individual segments.
        # Such a called tgroup.
        self._tabstyle: Optional["NameToken"] = None

    @property
    def tabstyle(self) -> Optional["NameToken"]:
        """Get tabstyle (Pythonic accessor)."""
        return self._tabstyle

    @tabstyle.setter
    def tabstyle(self, value: Optional["NameToken"]) -> None:
        """
        Set tabstyle with validation.

        Args:
            value: The tabstyle to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tabstyle = None
            return

        if not isinstance(value, NameToken):
            raise TypeError(
                f"tabstyle must be NameToken or None, got {type(value).__name__}"
            )
        self._tabstyle = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getColsep(self) -> "TableSeparatorString":
        """
        AUTOSAR-compliant getter for colsep.

        Returns:
            The colsep value

        Note:
            Delegates to colsep property (CODING_RULE_V2_00017)
        """
        return self.colsep  # Delegates to property

    def setColsep(self, value: "TableSeparatorString") -> "Table":
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

    def getFloat(self) -> "FloatEnum":
        """
        AUTOSAR-compliant getter for float.

        Returns:
            The float value

        Note:
            Delegates to float property (CODING_RULE_V2_00017)
        """
        return self.float  # Delegates to property

    def setFloat(self, value: "FloatEnum") -> "Table":
        """
        AUTOSAR-compliant setter for float with method chaining.

        Args:
            value: The float to set

        Returns:
            self for method chaining

        Note:
            Delegates to float property setter (gets validation automatically)
        """
        self.float = value  # Delegates to property setter
        return self

    def getFrame(self) -> "FrameEnum":
        """
        AUTOSAR-compliant getter for frame.

        Returns:
            The frame value

        Note:
            Delegates to frame property (CODING_RULE_V2_00017)
        """
        return self.frame  # Delegates to property

    def setFrame(self, value: "FrameEnum") -> "Table":
        """
        AUTOSAR-compliant setter for frame with method chaining.

        Args:
            value: The frame to set

        Returns:
            self for method chaining

        Note:
            Delegates to frame property setter (gets validation automatically)
        """
        self.frame = value  # Delegates to property setter
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

    def setHelpEntry(self, value: "String") -> "Table":
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

    def getOrient(self) -> "OrientEnum":
        """
        AUTOSAR-compliant getter for orient.

        Returns:
            The orient value

        Note:
            Delegates to orient property (CODING_RULE_V2_00017)
        """
        return self.orient  # Delegates to property

    def setOrient(self, value: "OrientEnum") -> "Table":
        """
        AUTOSAR-compliant setter for orient with method chaining.

        Args:
            value: The orient to set

        Returns:
            self for method chaining

        Note:
            Delegates to orient property setter (gets validation automatically)
        """
        self.orient = value  # Delegates to property setter
        return self

    def getPgwide(self) -> "NameToken":
        """
        AUTOSAR-compliant getter for pgwide.

        Returns:
            The pgwide value

        Note:
            Delegates to pgwide property (CODING_RULE_V2_00017)
        """
        return self.pgwide  # Delegates to property

    def setPgwide(self, value: "NameToken") -> "Table":
        """
        AUTOSAR-compliant setter for pgwide with method chaining.

        Args:
            value: The pgwide to set

        Returns:
            self for method chaining

        Note:
            Delegates to pgwide property setter (gets validation automatically)
        """
        self.pgwide = value  # Delegates to property setter
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

    def setRowsep(self, value: "TableSeparatorString") -> "Table":
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

    def getTableCaption(self) -> "Caption":
        """
        AUTOSAR-compliant getter for tableCaption.

        Returns:
            The tableCaption value

        Note:
            Delegates to table_caption property (CODING_RULE_V2_00017)
        """
        return self.table_caption  # Delegates to property

    def setTableCaption(self, value: "Caption") -> "Table":
        """
        AUTOSAR-compliant setter for tableCaption with method chaining.

        Args:
            value: The tableCaption to set

        Returns:
            self for method chaining

        Note:
            Delegates to table_caption property setter (gets validation automatically)
        """
        self.table_caption = value  # Delegates to property setter
        return self

    def getTabstyle(self) -> "NameToken":
        """
        AUTOSAR-compliant getter for tabstyle.

        Returns:
            The tabstyle value

        Note:
            Delegates to tabstyle property (CODING_RULE_V2_00017)
        """
        return self.tabstyle  # Delegates to property

    def setTabstyle(self, value: "NameToken") -> "Table":
        """
        AUTOSAR-compliant setter for tabstyle with method chaining.

        Args:
            value: The tabstyle to set

        Returns:
            self for method chaining

        Note:
            Delegates to tabstyle property setter (gets validation automatically)
        """
        self.tabstyle = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_colsep(self, value: Optional["TableSeparatorString"]) -> "Table":
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

    def with_float(self, value: "FloatEnum") -> "Table":
        """
        Set float and return self for chaining.

        Args:
            value: The float to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_float("value")
        """
        self.float = value  # Use property setter (gets validation)
        return self

    def with_frame(self, value: Optional["FrameEnum"]) -> "Table":
        """
        Set frame and return self for chaining.

        Args:
            value: The frame to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_frame("value")
        """
        self.frame = value  # Use property setter (gets validation)
        return self

    def with_help_entry(self, value: Optional["String"]) -> "Table":
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

    def with_orient(self, value: Optional["OrientEnum"]) -> "Table":
        """
        Set orient and return self for chaining.

        Args:
            value: The orient to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_orient("value")
        """
        self.orient = value  # Use property setter (gets validation)
        return self

    def with_pgwide(self, value: Optional["NameToken"]) -> "Table":
        """
        Set pgwide and return self for chaining.

        Args:
            value: The pgwide to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pgwide("value")
        """
        self.pgwide = value  # Use property setter (gets validation)
        return self

    def with_rowsep(self, value: Optional["TableSeparatorString"]) -> "Table":
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

    def with_table_caption(self, value: Optional["Caption"]) -> "Table":
        """
        Set tableCaption and return self for chaining.

        Args:
            value: The tableCaption to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_table_caption("value")
        """
        self.table_caption = value  # Use property setter (gets validation)
        return self

    def with_tabstyle(self, value: Optional["NameToken"]) -> "Table":
        """
        Set tabstyle and return self for chaining.

        Args:
            value: The tabstyle to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tabstyle("value")
        """
        self.tabstyle = value  # Use property setter (gets validation)
        return self
