from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class Colspec(ARObject):
    """
    This meta-class represents the ability to specify the properties of a column
    in a table.

    Package: M2::MSR::Documentation::BlockElements::OasisExchangeTable

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
        self._colnum: Optional["String"] = None

    @property
    def colnum(self) -> Optional["String"]:
        """Get colnum (Pythonic accessor)."""
        return self._colnum

    @colnum.setter
    def colnum(self, value: Optional["String"]) -> None:
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

        if not isinstance(value, String):
            raise TypeError(
                f"colnum must be String or None, got {type(value).__name__}"
            )
        self._colnum = value
                # specification.
        # 535 Document ID 202: AUTOSAR_FO_TPS_GenericStructureTemplate Template R23-11.
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
        # You can enter absolute values such cm, or relative values marked with * (e.
        # g.
        # , 2* for double those of other columns with 1*).
        # can be added to the number in the string.
        # are: cm, mm, px, pt.
        self._colwidth: Optional["String"] = None

    @property
    def colwidth(self) -> Optional["String"]:
        """Get colwidth (Pythonic accessor)."""
        return self._colwidth

    @colwidth.setter
    def colwidth(self, value: Optional["String"]) -> None:
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

        if not isinstance(value, String):
            raise TypeError(
                f"colwidth must be String or None, got {type(value).__name__}"
            )
        self._colwidth = value
        # column defined in the Colspec.
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

    def setAlign(self, value: "AlignEnum") -> "Colspec":
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

    def getColname(self) -> "String":
        """
        AUTOSAR-compliant getter for colname.

        Returns:
            The colname value

        Note:
            Delegates to colname property (CODING_RULE_V2_00017)
        """
        return self.colname  # Delegates to property

    def setColname(self, value: "String") -> "Colspec":
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

    def getColnum(self) -> "String":
        """
        AUTOSAR-compliant getter for colnum.

        Returns:
            The colnum value

        Note:
            Delegates to colnum property (CODING_RULE_V2_00017)
        """
        return self.colnum  # Delegates to property

    def setColnum(self, value: "String") -> "Colspec":
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

    def getColsep(self) -> "TableSeparatorString":
        """
        AUTOSAR-compliant getter for colsep.

        Returns:
            The colsep value

        Note:
            Delegates to colsep property (CODING_RULE_V2_00017)
        """
        return self.colsep  # Delegates to property

    def setColsep(self, value: "TableSeparatorString") -> "Colspec":
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

    def getColwidth(self) -> "String":
        """
        AUTOSAR-compliant getter for colwidth.

        Returns:
            The colwidth value

        Note:
            Delegates to colwidth property (CODING_RULE_V2_00017)
        """
        return self.colwidth  # Delegates to property

    def setColwidth(self, value: "String") -> "Colspec":
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

    def getRowsep(self) -> "TableSeparatorString":
        """
        AUTOSAR-compliant getter for rowsep.

        Returns:
            The rowsep value

        Note:
            Delegates to rowsep property (CODING_RULE_V2_00017)
        """
        return self.rowsep  # Delegates to property

    def setRowsep(self, value: "TableSeparatorString") -> "Colspec":
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

    def with_align(self, value: Optional["AlignEnum"]) -> "Colspec":
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

    def with_colname(self, value: Optional["String"]) -> "Colspec":
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

    def with_colnum(self, value: Optional["String"]) -> "Colspec":
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

    def with_colsep(self, value: Optional["TableSeparatorString"]) -> "Colspec":
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

    def with_colwidth(self, value: Optional["String"]) -> "Colspec":
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

    def with_rowsep(self, value: Optional["TableSeparatorString"]) -> "Colspec":
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
