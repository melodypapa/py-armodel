from typing import Optional

from armodel.v2.models.M2.MSR.Documentation.BlockElements.PaginationAndView import (
    Paginateable,
)


class Row(Paginateable):
    """
    This meta-class represents the ability to express one row in a table.

    Package: M2::MSR::Documentation::BlockElements::OasisExchangeTable

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 336, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Indicates if by default a line should be displayed below the.
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
        # inherited from tbody, otherwise it is "TOP".
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

    def getRowsep(self) -> "TableSeparatorString":
        """
        AUTOSAR-compliant getter for rowsep.

        Returns:
            The rowsep value

        Note:
            Delegates to rowsep property (CODING_RULE_V2_00017)
        """
        return self.rowsep  # Delegates to property

    def setRowsep(self, value: "TableSeparatorString") -> "Row":
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

    def getValign(self) -> "ValignEnum":
        """
        AUTOSAR-compliant getter for valign.

        Returns:
            The valign value

        Note:
            Delegates to valign property (CODING_RULE_V2_00017)
        """
        return self.valign  # Delegates to property

    def setValign(self, value: "ValignEnum") -> "Row":
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

    def with_rowsep(self, value: Optional["TableSeparatorString"]) -> "Row":
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

    def with_valign(self, value: Optional["ValignEnum"]) -> "Row":
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
