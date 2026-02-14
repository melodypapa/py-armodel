"""
AUTOSAR Package - OasisExchangeTable

Package: M2::MSR::Documentation::BlockElements::OasisExchangeTable
"""


from __future__ import annotations

from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    ARLiteral,
    Integer,
    NameToken,
    String,
)
from armodel.v2.models.M2.MSR.Documentation.BlockElements.PaginationAndView import (
    Paginateable,
)


class OrientEnum(AREnum):
    """
    Enumeration for table orientation.

    Package: M2::MSR::Documentation::BlockElements::OasisExchangeTable::OrientEnum

    Values:
        LANDSCAPE: Table in landscape orientation
        PORTRAIT: Table in portrait orientation
    """
    LANDSCAPE = "landscape"
    PORTRAIT = "portrait"


class FloatEnum(AREnum):
    """
    This enumerator specifies the policy how an objects floats on a page.

    Package: M2::MSR::Documentation::BlockElements::OasisExchangeTable::FloatEnum

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 333, Foundation
      R23-11)

    Values:
        FLOAT: A page formatter is allowed to float the table to optimize pagination
        NO_FLOAT: A page formatter is not allowed to float the object to optimize pagination
    """
    FLOAT = "float"
    NO_FLOAT = "noFloat"


class PgwideEnum(AREnum):
    """
    This enumerator specifies, if the table shall be rendered across the entire
    page, even if it is placed in side-head layouts.

    Package: M2::MSR::Documentation::BlockElements::OasisExchangeTable::PgwideEnum

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 348, Foundation
      R23-11)

    Values:
        NO_PGWIDE: The table shall be fit in the current text flow
        PGWIDE: The table may use the entire page width
    """
    NO_PGWIDE = "noPgwide"
    PGWIDE = "pgwide"


class Table(Paginateable):
    """
    This class implements an exchange table according to OASIS Technical
    Resolution TR 9503:1995. http://www.oasis-open.org/specs/a503.htm

    Package: M2::MSR::Documentation::BlockElements::OasisExchangeTable::Table

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 332, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Indicates if by default a line should be drawn between the this table.
        self._colsep: Optional[TableSeparatorString] = None

    @property
    def colsep(self) -> Optional[TableSeparatorString]:
        """Get colsep (Pythonic accessor)."""
        return self._colsep

    @colsep.setter
    def colsep(self, value: Optional[TableSeparatorString]) -> None:
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
        self._float: FloatEnum = None

    @property
    def float(self) -> FloatEnum:
        """Get float (Pythonic accessor)."""
        return self._float

    @float.setter
    def float(self, value: FloatEnum) -> None:
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
        self._frame: Optional[FrameEnum] = None

    @property
    def frame(self) -> Optional[FrameEnum]:
        """Get frame (Pythonic accessor)."""
        return self._frame

    @frame.setter
    def frame(self, value: Optional[FrameEnum]) -> None:
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
        self._helpEntry: Optional[String] = None

    @property
    def help_entry(self) -> Optional[String]:
        """Get helpEntry (Pythonic accessor)."""
        return self._helpEntry

    @help_entry.setter
    def help_entry(self, value: Optional[String]) -> None:
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
        # : landscape : portrait.
        self._orient: Optional[OrientEnum] = None

    @property
    def orient(self) -> Optional[OrientEnum]:
        """Get orient (Pythonic accessor)."""
        return self._orient

    @orient.setter
    def orient(self, value: Optional[OrientEnum]) -> None:
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
        self._pgwide: Optional[NameToken] = None

    @property
    def pgwide(self) -> Optional[NameToken]:
        """Get pgwide (Pythonic accessor)."""
        return self._pgwide

    @pgwide.setter
    def pgwide(self, value: Optional[NameToken]) -> None:
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

        if not isinstance(value, (NameToken, str)):
            raise TypeError(
                f"pgwide must be NameToken or str or None, got {type(value).__name__}"
            )
        self._pgwide = value
        self._rowsep: Optional[TableSeparatorString] = None

    @property
    def rowsep(self) -> Optional[TableSeparatorString]:
        """Get rowsep (Pythonic accessor)."""
        return self._rowsep

    @rowsep.setter
    def rowsep(self, value: Optional[TableSeparatorString]) -> None:
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
        self._tableCaption: Optional[Caption] = None

    @property
    def table_caption(self) -> Optional[Caption]:
        """Get tableCaption (Pythonic accessor)."""
        return self._tableCaption

    @table_caption.setter
    def table_caption(self, value: Optional[Caption]) -> None:
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
        self._tabstyle: Optional[NameToken] = None

    @property
    def tabstyle(self) -> Optional[NameToken]:
        """Get tabstyle (Pythonic accessor)."""
        return self._tabstyle

    @tabstyle.setter
    def tabstyle(self, value: Optional[NameToken]) -> None:
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

        if not isinstance(value, (NameToken, str)):
            raise TypeError(
                f"tabstyle must be NameToken or str or None, got {type(value).__name__}"
            )
        self._tabstyle = value

    def with_colspec(self, value):
        """
        Set colspec and return self for chaining.

        Args:
            value: The colspec to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_colspec("value")
        """
        self.colspec = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getColsep(self) -> TableSeparatorString:
        """
        AUTOSAR-compliant getter for colsep.

        Returns:
            The colsep value

        Note:
            Delegates to colsep property (CODING_RULE_V2_00017)
        """
        return self.colsep  # Delegates to property

    def setColsep(self, value: TableSeparatorString) -> Table:
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

    def getFloat(self) -> FloatEnum:
        """
        AUTOSAR-compliant getter for float.

        Returns:
            The float value

        Note:
            Delegates to float property (CODING_RULE_V2_00017)
        """
        return self.float  # Delegates to property

    def setFloat(self, value: FloatEnum) -> Table:
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

    def getFrame(self) -> FrameEnum:
        """
        AUTOSAR-compliant getter for frame.

        Returns:
            The frame value

        Note:
            Delegates to frame property (CODING_RULE_V2_00017)
        """
        return self.frame  # Delegates to property

    def setFrame(self, value: FrameEnum) -> Table:
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

    def getHelpEntry(self) -> String:
        """
        AUTOSAR-compliant getter for helpEntry.

        Returns:
            The helpEntry value

        Note:
            Delegates to help_entry property (CODING_RULE_V2_00017)
        """
        return self.help_entry  # Delegates to property

    def setHelpEntry(self, value: String) -> Table:
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

    def getOrient(self) -> OrientEnum:
        """
        AUTOSAR-compliant getter for orient.

        Returns:
            The orient value

        Note:
            Delegates to orient property (CODING_RULE_V2_00017)
        """
        return self.orient  # Delegates to property

    def setOrient(self, value: OrientEnum) -> Table:
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

    def getPgwide(self) -> NameToken:
        """
        AUTOSAR-compliant getter for pgwide.

        Returns:
            The pgwide value

        Note:
            Delegates to pgwide property (CODING_RULE_V2_00017)
        """
        return self.pgwide  # Delegates to property

    def setPgwide(self, value: NameToken) -> Table:
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

    def getRowsep(self) -> TableSeparatorString:
        """
        AUTOSAR-compliant getter for rowsep.

        Returns:
            The rowsep value

        Note:
            Delegates to rowsep property (CODING_RULE_V2_00017)
        """
        return self.rowsep  # Delegates to property

    def setRowsep(self, value: TableSeparatorString) -> Table:
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

    def getTableCaption(self) -> Caption:
        """
        AUTOSAR-compliant getter for tableCaption.

        Returns:
            The tableCaption value

        Note:
            Delegates to table_caption property (CODING_RULE_V2_00017)
        """
        return self.table_caption  # Delegates to property

    def setTableCaption(self, value: Caption) -> Table:
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

    def getTabstyle(self) -> NameToken:
        """
        AUTOSAR-compliant getter for tabstyle.

        Returns:
            The tabstyle value

        Note:
            Delegates to tabstyle property (CODING_RULE_V2_00017)
        """
        return self.tabstyle  # Delegates to property

    def setTabstyle(self, value: NameToken) -> Table:
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

    def with_colsep(self, value: Optional[TableSeparatorString]) -> Table:
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

    def with_float(self, value: FloatEnum) -> Table:
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

    def with_frame(self, value: Optional[FrameEnum]) -> Table:
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

    def with_help_entry(self, value: Optional[String]) -> Table:
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

    def with_orient(self, value: Optional[OrientEnum]) -> Table:
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

    def with_pgwide(self, value: Optional[NameToken]) -> Table:
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

    def with_rowsep(self, value: Optional[TableSeparatorString]) -> Table:
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

    def with_table_caption(self, value: Optional[Caption]) -> Table:
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

    def with_tabstyle(self, value: Optional[NameToken]) -> Table:
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



class Tgroup(ARObject):
    """
    This meta-class represents the ability to denote a table section.

    Package: M2::MSR::Documentation::BlockElements::OasisExchangeTable::Tgroup

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 334, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies how the cell entries shall be horizontally aligned specified
                # TGROUP.
        # Default is "LEFT".
        self._align: Optional[AlignEnum] = None

    @property
    def align(self) -> Optional[AlignEnum]:
        """Get align (Pythonic accessor)."""
        return self._align

    @align.setter
    def align(self, value: Optional[AlignEnum]) -> None:
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
        self._cols: Integer = None

    @property
    def cols(self) -> Integer:
        """Get cols (Pythonic accessor)."""
        return self._cols

    @cols.setter
    def cols(self, value: Integer) -> None:
        """
        Set cols with validation.

        Args:
            value: The cols to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"cols must be Integer or int, got {type(value).__name__}"
            )
        self._cols = value
        self._colsep: Optional[TableSeparatorString] = None

    @property
    def colsep(self) -> Optional[TableSeparatorString]:
        """Get colsep (Pythonic accessor)."""
        return self._colsep

    @colsep.setter
    def colsep(self, value: Optional[TableSeparatorString]) -> None:
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
        # entry for each column.
        self._colspec: List[Colspec] = []

    @property
    def colspec(self) -> List[Colspec]:
        """Get colspec (Pythonic accessor)."""
        return self._colspec
        # Indicates if by default a line shall be drawn at the bottom rows in this
        # table group.
        self._rowsep: Optional[TableSeparatorString] = None

    @property
    def rowsep(self) -> Optional[TableSeparatorString]:
        """Get rowsep (Pythonic accessor)."""
        return self._rowsep

    @rowsep.setter
    def rowsep(self, value: Optional[TableSeparatorString]) -> None:
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
        # 202: AUTOSAR_FO_TPS_GenericStructureTemplate Template R23-11.
        self._tbody: Tbody = None

    @property
    def tbody(self) -> Tbody:
        """Get tbody (Pythonic accessor)."""
        return self._tbody

    @tbody.setter
    def tbody(self, value: Tbody) -> None:
        """
        Set tbody with validation.

        Args:
            value: The tbody to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, Tbody):
            raise TypeError(
                f"tbody must be Tbody, got {type(value).__name__}"
            )
        self._tbody = value
        # This printed at the end of the table or before a.
        self._tfoot: Optional[Tbody] = None

    @property
    def tfoot(self) -> Optional[Tbody]:
        """Get tfoot (Pythonic accessor)."""
        return self._tfoot

    @tfoot.setter
    def tfoot(self, value: Optional[Tbody]) -> None:
        """
        Set tfoot with validation.

        Args:
            value: The tfoot to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tfoot = None
            return

        if not isinstance(value, Tbody):
            raise TypeError(
                f"tfoot must be Tbody or None, got {type(value).__name__}"
            )
        self._tfoot = value
        # The usually repeated at the beginning of each new.
        self._thead: Optional[Tbody] = None

    @property
    def thead(self) -> Optional[Tbody]:
        """Get thead (Pythonic accessor)."""
        return self._thead

    @thead.setter
    def thead(self, value: Optional[Tbody]) -> None:
        """
        Set thead with validation.

        Args:
            value: The thead to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._thead = None
            return

        if not isinstance(value, Tbody):
            raise TypeError(
                f"thead must be Tbody or None, got {type(value).__name__}"
            )
        self._thead = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAlign(self) -> AlignEnum:
        """
        AUTOSAR-compliant getter for align.

        Returns:
            The align value

        Note:
            Delegates to align property (CODING_RULE_V2_00017)
        """
        return self.align  # Delegates to property

    def setAlign(self, value: AlignEnum) -> Tgroup:
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

    def getCols(self) -> Integer:
        """
        AUTOSAR-compliant getter for cols.

        Returns:
            The cols value

        Note:
            Delegates to cols property (CODING_RULE_V2_00017)
        """
        return self.cols  # Delegates to property

    def setCols(self, value: Integer) -> Tgroup:
        """
        AUTOSAR-compliant setter for cols with method chaining.

        Args:
            value: The cols to set

        Returns:
            self for method chaining

        Note:
            Delegates to cols property setter (gets validation automatically)
        """
        self.cols = value  # Delegates to property setter
        return self

    def getColsep(self) -> TableSeparatorString:
        """
        AUTOSAR-compliant getter for colsep.

        Returns:
            The colsep value

        Note:
            Delegates to colsep property (CODING_RULE_V2_00017)
        """
        return self.colsep  # Delegates to property

    def setColsep(self, value: TableSeparatorString) -> Tgroup:
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

    def getColspec(self) -> List[Colspec]:
        """
        AUTOSAR-compliant getter for colspec.

        Returns:
            The colspec value

        Note:
            Delegates to colspec property (CODING_RULE_V2_00017)
        """
        return self.colspec  # Delegates to property

    def getRowsep(self) -> TableSeparatorString:
        """
        AUTOSAR-compliant getter for rowsep.

        Returns:
            The rowsep value

        Note:
            Delegates to rowsep property (CODING_RULE_V2_00017)
        """
        return self.rowsep  # Delegates to property

    def setRowsep(self, value: TableSeparatorString) -> Tgroup:
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

    def getTbody(self) -> Tbody:
        """
        AUTOSAR-compliant getter for tbody.

        Returns:
            The tbody value

        Note:
            Delegates to tbody property (CODING_RULE_V2_00017)
        """
        return self.tbody  # Delegates to property

    def setTbody(self, value: Tbody) -> Tgroup:
        """
        AUTOSAR-compliant setter for tbody with method chaining.

        Args:
            value: The tbody to set

        Returns:
            self for method chaining

        Note:
            Delegates to tbody property setter (gets validation automatically)
        """
        self.tbody = value  # Delegates to property setter
        return self

    def getTfoot(self) -> Tbody:
        """
        AUTOSAR-compliant getter for tfoot.

        Returns:
            The tfoot value

        Note:
            Delegates to tfoot property (CODING_RULE_V2_00017)
        """
        return self.tfoot  # Delegates to property

    def setTfoot(self, value: Tbody) -> Tgroup:
        """
        AUTOSAR-compliant setter for tfoot with method chaining.

        Args:
            value: The tfoot to set

        Returns:
            self for method chaining

        Note:
            Delegates to tfoot property setter (gets validation automatically)
        """
        self.tfoot = value  # Delegates to property setter
        return self

    def getThead(self) -> Tbody:
        """
        AUTOSAR-compliant getter for thead.

        Returns:
            The thead value

        Note:
            Delegates to thead property (CODING_RULE_V2_00017)
        """
        return self.thead  # Delegates to property

    def setThead(self, value: Tbody) -> Tgroup:
        """
        AUTOSAR-compliant setter for thead with method chaining.

        Args:
            value: The thead to set

        Returns:
            self for method chaining

        Note:
            Delegates to thead property setter (gets validation automatically)
        """
        self.thead = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_align(self, value: Optional[AlignEnum]) -> Tgroup:
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

    def with_cols(self, value: Integer) -> Tgroup:
        """
        Set cols and return self for chaining.

        Args:
            value: The cols to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_cols("value")
        """
        self.cols = value  # Use property setter (gets validation)
        return self

    def with_colsep(self, value: Optional[TableSeparatorString]) -> Tgroup:
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

    def with_rowsep(self, value: Optional[TableSeparatorString]) -> Tgroup:
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

    def with_tbody(self, value: Tbody) -> Tgroup:
        """
        Set tbody and return self for chaining.

        Args:
            value: The tbody to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tbody("value")
        """
        self.tbody = value  # Use property setter (gets validation)
        return self

    def with_tfoot(self, value: Optional[Tbody]) -> Tgroup:
        """
        Set tfoot and return self for chaining.

        Args:
            value: The tfoot to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tfoot("value")
        """
        self.tfoot = value  # Use property setter (gets validation)
        return self

    def with_thead(self, value: Optional[Tbody]) -> Tgroup:
        """
        Set thead and return self for chaining.

        Args:
            value: The thead to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_thead("value")
        """
        self.thead = value  # Use property setter (gets validation)
        return self



class Tbody(ARObject):
    """
    This meta-class represents a part within a table group. Such a part can be
    the table head, the table body or the table foot.

    Package: M2::MSR::Documentation::BlockElements::OasisExchangeTable::Tbody

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 335, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Indicates how the cells in the rows shall be aligned.
        # inherited from tbody, otherwise it is "TOP".
        self._valign: Optional[ValignEnum] = None

    @property
    def valign(self) -> Optional[ValignEnum]:
        """Get valign (Pythonic accessor)."""
        return self._valign

    @valign.setter
    def valign(self, value: Optional[ValignEnum]) -> None:
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

    def getValign(self) -> ValignEnum:
        """
        AUTOSAR-compliant getter for valign.

        Returns:
            The valign value

        Note:
            Delegates to valign property (CODING_RULE_V2_00017)
        """
        return self.valign  # Delegates to property

    def setValign(self, value: ValignEnum) -> Tbody:
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

    def with_valign(self, value: Optional[ValignEnum]) -> Tbody:
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



class Row(Paginateable):
    """
    This meta-class represents the ability to express one row in a table.

    Package: M2::MSR::Documentation::BlockElements::OasisExchangeTable::Row

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 336, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Indicates if by default a line should be displayed below the.
        self._rowsep: Optional[TableSeparatorString] = None

    @property
    def rowsep(self) -> Optional[TableSeparatorString]:
        """Get rowsep (Pythonic accessor)."""
        return self._rowsep

    @rowsep.setter
    def rowsep(self, value: Optional[TableSeparatorString]) -> None:
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
        # inherited from tbody, otherwise it is "TOP".
        self._valign: Optional[ValignEnum] = None

    @property
    def valign(self) -> Optional[ValignEnum]:
        """Get valign (Pythonic accessor)."""
        return self._valign

    @valign.setter
    def valign(self, value: Optional[ValignEnum]) -> None:
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

    def getRowsep(self) -> TableSeparatorString:
        """
        AUTOSAR-compliant getter for rowsep.

        Returns:
            The rowsep value

        Note:
            Delegates to rowsep property (CODING_RULE_V2_00017)
        """
        return self.rowsep  # Delegates to property

    def setRowsep(self, value: TableSeparatorString) -> Row:
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

    def getValign(self) -> ValignEnum:
        """
        AUTOSAR-compliant getter for valign.

        Returns:
            The valign value

        Note:
            Delegates to valign property (CODING_RULE_V2_00017)
        """
        return self.valign  # Delegates to property

    def setValign(self, value: ValignEnum) -> Row:
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

    def with_rowsep(self, value: Optional[TableSeparatorString]) -> Row:
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

    def with_valign(self, value: Optional[ValignEnum]) -> Row:
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



class Entry(ARObject):
    """
    This represents one particular table cell.

    Package: M2::MSR::Documentation::BlockElements::OasisExchangeTable::Entry

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 336, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies how the cell ENTRY shall be horizontally is "LEFT".
        self._align: Optional[AlignEnum] = None

    @property
    def align(self) -> Optional[AlignEnum]:
        """Get align (Pythonic accessor)."""
        return self._align

    @align.setter
    def align(self, value: Optional[AlignEnum]) -> None:
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
                # digits RGB hex-code.
        # 535 Document ID 202: AUTOSAR_FO_TPS_GenericStructureTemplate Template R23-11.
        self._bgcolor: String = None

    @property
    def bgcolor(self) -> String:
        """Get bgcolor (Pythonic accessor)."""
        return self._bgcolor

    @bgcolor.setter
    def bgcolor(self, value: String) -> None:
        """
        Set bgcolor with validation.

        Args:
            value: The bgcolor to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, (String, str)):
            raise TypeError(
                f"bgcolor must be String or str, got {type(value).__name__}"
            )
        self._bgcolor = value
        self._colname: Optional[String] = None

    @property
    def colname(self) -> Optional[String]:
        """Get colname (Pythonic accessor)."""
        return self._colname

    @colname.setter
    def colname(self, value: Optional[String]) -> None:
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

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"colname must be String or str or None, got {type(value).__name__}"
            )
        self._colname = value
        self._colsep: Optional[TableSeparatorString] = None

    @property
    def colsep(self) -> Optional[TableSeparatorString]:
        """Get colsep (Pythonic accessor)."""
        return self._colsep

    @colsep.setter
    def colsep(self, value: Optional[TableSeparatorString]) -> None:
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
        self._entryContents: DocumentationBlock = None

    @property
    def entry_contents(self) -> DocumentationBlock:
        """Get entryContents (Pythonic accessor)."""
        return self._entryContents

    @entry_contents.setter
    def entry_contents(self, value: DocumentationBlock) -> None:
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
        # Default is "0".
        self._morerows: Optional[String] = None

    @property
    def morerows(self) -> Optional[String]:
        """Get morerows (Pythonic accessor)."""
        return self._morerows

    @morerows.setter
    def morerows(self, value: Optional[String]) -> None:
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

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"morerows must be String or str or None, got {type(value).__name__}"
            )
        self._morerows = value
        self._nameend: Optional[String] = None

    @property
    def nameend(self) -> Optional[String]:
        """Get nameend (Pythonic accessor)."""
        return self._nameend

    @nameend.setter
    def nameend(self, value: Optional[String]) -> None:
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

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"nameend must be String or str or None, got {type(value).__name__}"
            )
        self._nameend = value
        self._namest: Optional[String] = None

    @property
    def namest(self) -> Optional[String]:
        """Get namest (Pythonic accessor)."""
        return self._namest

    @namest.setter
    def namest(self, value: Optional[String]) -> None:
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

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"namest must be String or str or None, got {type(value).__name__}"
            )
        self._namest = value
        # Default is 0; 1 the contents 90 degree counterclockwise.
        # is defined by OASIS.
        self._rotate: Optional[String] = None

    @property
    def rotate(self) -> Optional[String]:
        """Get rotate (Pythonic accessor)."""
        return self._rotate

    @rotate.setter
    def rotate(self, value: Optional[String]) -> None:
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

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"rotate must be String or str or None, got {type(value).__name__}"
            )
        self._rotate = value
        self._rowsep: Optional[TableSeparatorString] = None

    @property
    def rowsep(self) -> Optional[TableSeparatorString]:
        """Get rowsep (Pythonic accessor)."""
        return self._rowsep

    @rowsep.setter
    def rowsep(self, value: Optional[TableSeparatorString]) -> None:
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
        self._spanname: Optional[String] = None

    @property
    def spanname(self) -> Optional[String]:
        """Get spanname (Pythonic accessor)."""
        return self._spanname

    @spanname.setter
    def spanname(self, value: Optional[String]) -> None:
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

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"spanname must be String or str or None, got {type(value).__name__}"
            )
        self._spanname = value
        # inherited from row or tbody, otherwise "TOP".
        self._valign: Optional[ValignEnum] = None

    @property
    def valign(self) -> Optional[ValignEnum]:
        """Get valign (Pythonic accessor)."""
        return self._valign

    @valign.setter
    def valign(self, value: Optional[ValignEnum]) -> None:
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

    def getAlign(self) -> AlignEnum:
        """
        AUTOSAR-compliant getter for align.

        Returns:
            The align value

        Note:
            Delegates to align property (CODING_RULE_V2_00017)
        """
        return self.align  # Delegates to property

    def setAlign(self, value: AlignEnum) -> Entry:
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

    def getBgcolor(self) -> String:
        """
        AUTOSAR-compliant getter for bgcolor.

        Returns:
            The bgcolor value

        Note:
            Delegates to bgcolor property (CODING_RULE_V2_00017)
        """
        return self.bgcolor  # Delegates to property

    def setBgcolor(self, value: String) -> Entry:
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

    def getColname(self) -> String:
        """
        AUTOSAR-compliant getter for colname.

        Returns:
            The colname value

        Note:
            Delegates to colname property (CODING_RULE_V2_00017)
        """
        return self.colname  # Delegates to property

    def setColname(self, value: String) -> Entry:
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

    def getColsep(self) -> TableSeparatorString:
        """
        AUTOSAR-compliant getter for colsep.

        Returns:
            The colsep value

        Note:
            Delegates to colsep property (CODING_RULE_V2_00017)
        """
        return self.colsep  # Delegates to property

    def setColsep(self, value: TableSeparatorString) -> Entry:
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

    def getEntryContents(self) -> DocumentationBlock:
        """
        AUTOSAR-compliant getter for entryContents.

        Returns:
            The entryContents value

        Note:
            Delegates to entry_contents property (CODING_RULE_V2_00017)
        """
        return self.entry_contents  # Delegates to property

    def setEntryContents(self, value: DocumentationBlock) -> Entry:
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

    def getMorerows(self) -> String:
        """
        AUTOSAR-compliant getter for morerows.

        Returns:
            The morerows value

        Note:
            Delegates to morerows property (CODING_RULE_V2_00017)
        """
        return self.morerows  # Delegates to property

    def setMorerows(self, value: String) -> Entry:
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

    def getNameend(self) -> String:
        """
        AUTOSAR-compliant getter for nameend.

        Returns:
            The nameend value

        Note:
            Delegates to nameend property (CODING_RULE_V2_00017)
        """
        return self.nameend  # Delegates to property

    def setNameend(self, value: String) -> Entry:
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

    def getNamest(self) -> String:
        """
        AUTOSAR-compliant getter for namest.

        Returns:
            The namest value

        Note:
            Delegates to namest property (CODING_RULE_V2_00017)
        """
        return self.namest  # Delegates to property

    def setNamest(self, value: String) -> Entry:
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

    def getRotate(self) -> String:
        """
        AUTOSAR-compliant getter for rotate.

        Returns:
            The rotate value

        Note:
            Delegates to rotate property (CODING_RULE_V2_00017)
        """
        return self.rotate  # Delegates to property

    def setRotate(self, value: String) -> Entry:
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

    def getRowsep(self) -> TableSeparatorString:
        """
        AUTOSAR-compliant getter for rowsep.

        Returns:
            The rowsep value

        Note:
            Delegates to rowsep property (CODING_RULE_V2_00017)
        """
        return self.rowsep  # Delegates to property

    def setRowsep(self, value: TableSeparatorString) -> Entry:
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

    def getSpanname(self) -> String:
        """
        AUTOSAR-compliant getter for spanname.

        Returns:
            The spanname value

        Note:
            Delegates to spanname property (CODING_RULE_V2_00017)
        """
        return self.spanname  # Delegates to property

    def setSpanname(self, value: String) -> Entry:
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

    def getValign(self) -> ValignEnum:
        """
        AUTOSAR-compliant getter for valign.

        Returns:
            The valign value

        Note:
            Delegates to valign property (CODING_RULE_V2_00017)
        """
        return self.valign  # Delegates to property

    def setValign(self, value: ValignEnum) -> Entry:
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

    def with_align(self, value: Optional[AlignEnum]) -> Entry:
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

    def with_bgcolor(self, value: String) -> Entry:
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

    def with_colname(self, value: Optional[String]) -> Entry:
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

    def with_colsep(self, value: Optional[TableSeparatorString]) -> Entry:
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

    def with_entry_contents(self, value: DocumentationBlock) -> Entry:
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

    def with_morerows(self, value: Optional[String]) -> Entry:
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

    def with_nameend(self, value: Optional[String]) -> Entry:
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

    def with_namest(self, value: Optional[String]) -> Entry:
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

    def with_rotate(self, value: Optional[String]) -> Entry:
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

    def with_rowsep(self, value: Optional[TableSeparatorString]) -> Entry:
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

    def with_spanname(self, value: Optional[String]) -> Entry:
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

    def with_valign(self, value: Optional[ValignEnum]) -> Entry:
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



class Colspec(ARObject):
    """
    This meta-class represents the ability to specify the properties of a column
    in a table.

    Package: M2::MSR::Documentation::BlockElements::OasisExchangeTable::Colspec

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 433, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies how the cell entries shall be horizontally aligned specified
                # column.
        # Default is "LEFT".
        self._align: Optional[AlignEnum] = None

    @property
    def align(self) -> Optional[AlignEnum]:
        """Get align (Pythonic accessor)."""
        return self._align

    @align.setter
    def align(self, value: Optional[AlignEnum]) -> None:
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
        self._colname: Optional[String] = None

    @property
    def colname(self) -> Optional[String]:
        """Get colname (Pythonic accessor)."""
        return self._colname

    @colname.setter
    def colname(self, value: Optional[String]) -> None:
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

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"colname must be String or str or None, got {type(value).__name__}"
            )
        self._colname = value
        self._colnum: Optional[String] = None

    @property
    def colnum(self) -> Optional[String]:
        """Get colnum (Pythonic accessor)."""
        return self._colnum

    @colnum.setter
    def colnum(self, value: Optional[String]) -> None:
        """
        Set colnum with validation.

        Args:
            value: The colnum to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._colnum = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"colnum must be String or str or None, got {type(value).__name__}"
            )
        self._colnum = value
                # specification.
        # 535 Document ID 202: AUTOSAR_FO_TPS_GenericStructureTemplate Template R23-11.
        self._colsep: Optional[TableSeparatorString] = None

    @property
    def colsep(self) -> Optional[TableSeparatorString]:
        """Get colsep (Pythonic accessor)."""
        return self._colsep

    @colsep.setter
    def colsep(self, value: Optional[TableSeparatorString]) -> None:
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
        # You can enter absolute values such cm, or relative values marked with * (e.
        # g.
        # , 2* for double those of other columns with 1*).
        # can be added to the number in the string.
        # are: cm, mm, px, pt.
        self._colwidth: Optional[String] = None

    @property
    def colwidth(self) -> Optional[String]:
        """Get colwidth (Pythonic accessor)."""
        return self._colwidth

    @colwidth.setter
    def colwidth(self, value: Optional[String]) -> None:
        """
        Set colwidth with validation.

        Args:
            value: The colwidth to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._colwidth = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"colwidth must be String or str or None, got {type(value).__name__}"
            )
        self._colwidth = value
        # column defined in the Colspec.
        self._rowsep: Optional[TableSeparatorString] = None

    @property
    def rowsep(self) -> Optional[TableSeparatorString]:
        """Get rowsep (Pythonic accessor)."""
        return self._rowsep

    @rowsep.setter
    def rowsep(self, value: Optional[TableSeparatorString]) -> None:
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

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAlign(self) -> AlignEnum:
        """
        AUTOSAR-compliant getter for align.

        Returns:
            The align value

        Note:
            Delegates to align property (CODING_RULE_V2_00017)
        """
        return self.align  # Delegates to property

    def setAlign(self, value: AlignEnum) -> Colspec:
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

    def getColname(self) -> String:
        """
        AUTOSAR-compliant getter for colname.

        Returns:
            The colname value

        Note:
            Delegates to colname property (CODING_RULE_V2_00017)
        """
        return self.colname  # Delegates to property

    def setColname(self, value: String) -> Colspec:
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

    def getColnum(self) -> String:
        """
        AUTOSAR-compliant getter for colnum.

        Returns:
            The colnum value

        Note:
            Delegates to colnum property (CODING_RULE_V2_00017)
        """
        return self.colnum  # Delegates to property

    def setColnum(self, value: String) -> Colspec:
        """
        AUTOSAR-compliant setter for colnum with method chaining.

        Args:
            value: The colnum to set

        Returns:
            self for method chaining

        Note:
            Delegates to colnum property setter (gets validation automatically)
        """
        self.colnum = value  # Delegates to property setter
        return self

    def getColsep(self) -> TableSeparatorString:
        """
        AUTOSAR-compliant getter for colsep.

        Returns:
            The colsep value

        Note:
            Delegates to colsep property (CODING_RULE_V2_00017)
        """
        return self.colsep  # Delegates to property

    def setColsep(self, value: TableSeparatorString) -> Colspec:
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

    def getColwidth(self) -> String:
        """
        AUTOSAR-compliant getter for colwidth.

        Returns:
            The colwidth value

        Note:
            Delegates to colwidth property (CODING_RULE_V2_00017)
        """
        return self.colwidth  # Delegates to property

    def setColwidth(self, value: String) -> Colspec:
        """
        AUTOSAR-compliant setter for colwidth with method chaining.

        Args:
            value: The colwidth to set

        Returns:
            self for method chaining

        Note:
            Delegates to colwidth property setter (gets validation automatically)
        """
        self.colwidth = value  # Delegates to property setter
        return self

    def getRowsep(self) -> TableSeparatorString:
        """
        AUTOSAR-compliant getter for rowsep.

        Returns:
            The rowsep value

        Note:
            Delegates to rowsep property (CODING_RULE_V2_00017)
        """
        return self.rowsep  # Delegates to property

    def setRowsep(self, value: TableSeparatorString) -> Colspec:
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_align(self, value: Optional[AlignEnum]) -> Colspec:
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

    def with_colname(self, value: Optional[String]) -> Colspec:
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

    def with_colnum(self, value: Optional[String]) -> Colspec:
        """
        Set colnum and return self for chaining.

        Args:
            value: The colnum to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_colnum("value")
        """
        self.colnum = value  # Use property setter (gets validation)
        return self

    def with_colsep(self, value: Optional[TableSeparatorString]) -> Colspec:
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

    def with_colwidth(self, value: Optional[String]) -> Colspec:
        """
        Set colwidth and return self for chaining.

        Args:
            value: The colwidth to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_colwidth("value")
        """
        self.colwidth = value  # Use property setter (gets validation)
        return self

    def with_rowsep(self, value: Optional[TableSeparatorString]) -> Colspec:
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


class FrameEnum(AREnum):
    """
    FrameEnum enumeration

This enumerator specifies the policy, where to place a frame border around the table. Aggregated by MlFigure.frame, Table.frame

Package: M2::MSR::Documentation::BlockElements::OasisExchangeTable
    """
    # Borders all around the table
    all = "0"

    # Border at the bottom of the table
    bottom = "1"

    # No borders around the table
    none = "2"

    # Borders at the sides of the table
    sides = "3"

    # Border at the top of the table
    top = "4"

    # Borders at the top and bottom of the table
    topbot = "5"



class AlignEnum(AREnum):
    """
    AlignEnum enumeration

This enumerator specifies horizontal alignment. Aggregated by Colspec.align, Entry.align, Tgroup.align

Package: M2::MSR::Documentation::BlockElements::OasisExchangeTable
    """
    # The content of the table is horizontally centered.
    center = "0"

    # This indicates that the content of table cell shall be justified (rendered as a block where white-space is expanded such that all lines are filled up).
    justify = "1"

    # This indicates that the content of a table cell is left justified.
    leftright = "3"



class ValignEnum(AREnum):
    """
    ValignEnum enumeration

This enumerator specifies vertical alignment. Aggregated by Entry.valign, Row.valign, Tbody.valign

Package: M2::MSR::Documentation::BlockElements::OasisExchangeTable
    """
    # The contents of the table cell is bottom aligned.
    bottom = "0"

    # The contents of the table is vertically centered.
    middle = "1"

    # The contents of the table cell is top aligned.
    top = "2"



class TableSeparatorString(ARLiteral):
    """
    TableSeparatorString primitive type

This represents the ability to denote a separator string within an OASIS exchange table. • 0: no line is displayed • 1: line is displayed Tags: xml.xsd.customType=TABLE-SEPARATOR-STRING xml.xsd.pattern=[0-1] xml.xsd.type=string Table 9.72: TableSeparatorString 337 of 535 Document ID 202: AUTOSAR_FO_TPS_GenericStructureTemplate Generic Structure Template AUTOSAR FO R23-11 9.3.4 Topics in Documentation [TPS_GST_00332] Topics in Documentation (cid:100)A topic (Topic1)7 is a logical unit, which subdivides a content of a chapter mainly by providing intermediate head lines.

Package: M2::MSR::Documentation::BlockElements::OasisExchangeTable
    """
    pass


