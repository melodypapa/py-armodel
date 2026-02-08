from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


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
        # This attribute represents the number of columns in the.
        self._cols: "Integer" = None

    @property
    def cols(self) -> "Integer":
        """Get cols (Pythonic accessor)."""
        return self._cols

    @cols.setter
    def cols(self, value: "Integer") -> None:
        """
        Set cols with validation.

        Args:
            value: The cols to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, Integer):
            raise TypeError(
                f"cols must be Integer, got {type(value).__name__}"
            )
        self._cols = value
        # Indicates if by default a line shall be drawn between the this table group.
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
        # This specifies one particular column specification in the There shall be one
        # entry for each column.
        self._colspec: List["Colspec"] = []

    @property
    def colspec(self) -> List["Colspec"]:
        """Get colspec (Pythonic accessor)."""
        return self._colspec
        # Indicates if by default a line shall be drawn at the bottom rows in this
        # table group.
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
        # This is the main part of the table segment, called the table 535 Document ID
        # 202: AUTOSAR_FO_TPS_GenericStructureTemplate Template R23-11.
        self._tbody: "Tbody" = None

    @property
    def tbody(self) -> "Tbody":
        """Get tbody (Pythonic accessor)."""
        return self._tbody

    @tbody.setter
    def tbody(self, value: "Tbody") -> None:
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
        # This represents the footer of the table segment.
        # This printed at the end of the table or before a.
        self._tfoot: Optional["Tbody"] = None

    @property
    def tfoot(self) -> Optional["Tbody"]:
        """Get tfoot (Pythonic accessor)."""
        return self._tfoot

    @tfoot.setter
    def tfoot(self, value: Optional["Tbody"]) -> None:
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
        # This represents the heading of the table section.
        # The usually repeated at the beginning of each new.
        self._thead: Optional["Tbody"] = None

    @property
    def thead(self) -> Optional["Tbody"]:
        """Get thead (Pythonic accessor)."""
        return self._thead

    @thead.setter
    def thead(self, value: Optional["Tbody"]) -> None:
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

    def getAlign(self) -> "AlignEnum":
        """
        AUTOSAR-compliant getter for align.

        Returns:
            The align value

        Note:
            Delegates to align property (CODING_RULE_V2_00017)
        """
        return self.align  # Delegates to property

    def setAlign(self, value: "AlignEnum") -> "Tgroup":
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

    def getCols(self) -> "Integer":
        """
        AUTOSAR-compliant getter for cols.

        Returns:
            The cols value

        Note:
            Delegates to cols property (CODING_RULE_V2_00017)
        """
        return self.cols  # Delegates to property

    def setCols(self, value: "Integer") -> "Tgroup":
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

    def getColsep(self) -> "TableSeparatorString":
        """
        AUTOSAR-compliant getter for colsep.

        Returns:
            The colsep value

        Note:
            Delegates to colsep property (CODING_RULE_V2_00017)
        """
        return self.colsep  # Delegates to property

    def setColsep(self, value: "TableSeparatorString") -> "Tgroup":
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

    def getColspec(self) -> List["Colspec"]:
        """
        AUTOSAR-compliant getter for colspec.

        Returns:
            The colspec value

        Note:
            Delegates to colspec property (CODING_RULE_V2_00017)
        """
        return self.colspec  # Delegates to property

    def getRowsep(self) -> "TableSeparatorString":
        """
        AUTOSAR-compliant getter for rowsep.

        Returns:
            The rowsep value

        Note:
            Delegates to rowsep property (CODING_RULE_V2_00017)
        """
        return self.rowsep  # Delegates to property

    def setRowsep(self, value: "TableSeparatorString") -> "Tgroup":
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

    def getTbody(self) -> "Tbody":
        """
        AUTOSAR-compliant getter for tbody.

        Returns:
            The tbody value

        Note:
            Delegates to tbody property (CODING_RULE_V2_00017)
        """
        return self.tbody  # Delegates to property

    def setTbody(self, value: "Tbody") -> "Tgroup":
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

    def getTfoot(self) -> "Tbody":
        """
        AUTOSAR-compliant getter for tfoot.

        Returns:
            The tfoot value

        Note:
            Delegates to tfoot property (CODING_RULE_V2_00017)
        """
        return self.tfoot  # Delegates to property

    def setTfoot(self, value: "Tbody") -> "Tgroup":
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

    def getThead(self) -> "Tbody":
        """
        AUTOSAR-compliant getter for thead.

        Returns:
            The thead value

        Note:
            Delegates to thead property (CODING_RULE_V2_00017)
        """
        return self.thead  # Delegates to property

    def setThead(self, value: "Tbody") -> "Tgroup":
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

    def with_align(self, value: Optional["AlignEnum"]) -> "Tgroup":
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

    def with_cols(self, value: "Integer") -> "Tgroup":
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

    def with_colsep(self, value: Optional["TableSeparatorString"]) -> "Tgroup":
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

    def with_rowsep(self, value: Optional["TableSeparatorString"]) -> "Tgroup":
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

    def with_tbody(self, value: "Tbody") -> "Tgroup":
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

    def with_tfoot(self, value: Optional["Tbody"]) -> "Tgroup":
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

    def with_thead(self, value: Optional["Tbody"]) -> "Tgroup":
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
