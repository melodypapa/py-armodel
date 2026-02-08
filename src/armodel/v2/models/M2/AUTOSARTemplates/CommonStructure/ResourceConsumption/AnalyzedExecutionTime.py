from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    ExecutionTime,
    MultidimensionalTime,
)


class AnalyzedExecutionTime(ExecutionTime):
    """
    AnalyzedExecutionTime provides an analytic method for specifying the best
    and worst case execution time.

    Package: M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::ExecutionTime::AnalyzedExecutionTime

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 164, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The best case execution time (BCET) defines the amount of time the related
        # executable entity its execution.
        self._bestCase: Optional["MultidimensionalTime"] = None

    @property
    def best_case(self) -> Optional["MultidimensionalTime"]:
        """Get bestCase (Pythonic accessor)."""
        return self._bestCase

    @best_case.setter
    def best_case(self, value: Optional["MultidimensionalTime"]) -> None:
        """
        Set bestCase with validation.

        Args:
            value: The bestCase to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._bestCase = None
            return

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"bestCase must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._bestCase = value
        # The worst case execution time (WCET) defines the amount of time the related
        # executable entity its execution.
        self._worstCase: Optional["MultidimensionalTime"] = None

    @property
    def worst_case(self) -> Optional["MultidimensionalTime"]:
        """Get worstCase (Pythonic accessor)."""
        return self._worstCase

    @worst_case.setter
    def worst_case(self, value: Optional["MultidimensionalTime"]) -> None:
        """
        Set worstCase with validation.

        Args:
            value: The worstCase to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._worstCase = None
            return

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"worstCase must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._worstCase = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBestCase(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for bestCase.

        Returns:
            The bestCase value

        Note:
            Delegates to best_case property (CODING_RULE_V2_00017)
        """
        return self.best_case  # Delegates to property

    def setBestCase(self, value: "MultidimensionalTime") -> "AnalyzedExecutionTime":
        """
        AUTOSAR-compliant setter for bestCase with method chaining.

        Args:
            value: The bestCase to set

        Returns:
            self for method chaining

        Note:
            Delegates to best_case property setter (gets validation automatically)
        """
        self.best_case = value  # Delegates to property setter
        return self

    def getWorstCase(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for worstCase.

        Returns:
            The worstCase value

        Note:
            Delegates to worst_case property (CODING_RULE_V2_00017)
        """
        return self.worst_case  # Delegates to property

    def setWorstCase(self, value: "MultidimensionalTime") -> "AnalyzedExecutionTime":
        """
        AUTOSAR-compliant setter for worstCase with method chaining.

        Args:
            value: The worstCase to set

        Returns:
            self for method chaining

        Note:
            Delegates to worst_case property setter (gets validation automatically)
        """
        self.worst_case = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_best_case(self, value: Optional["MultidimensionalTime"]) -> "AnalyzedExecutionTime":
        """
        Set bestCase and return self for chaining.

        Args:
            value: The bestCase to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_best_case("value")
        """
        self.best_case = value  # Use property setter (gets validation)
        return self

    def with_worst_case(self, value: Optional["MultidimensionalTime"]) -> "AnalyzedExecutionTime":
        """
        Set worstCase and return self for chaining.

        Args:
            value: The worstCase to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_worst_case("value")
        """
        self.worst_case = value  # Use property setter (gets validation)
        return self
