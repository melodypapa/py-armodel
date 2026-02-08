from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.ExecutionTime import (
    ExecutionTime,
)


class SimulatedExecutionTime(ExecutionTime):
    """
    Specifies the ExecutionTime which has been gathered using simulation means.

    Package: M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::ExecutionTime

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 167, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The maximum simulated execution time.
        self._maximumExecutionTime: Optional["MultidimensionalTime"] = None

    @property
    def maximum_execution_time(self) -> Optional["MultidimensionalTime"]:
        """Get maximumExecutionTime (Pythonic accessor)."""
        return self._maximumExecutionTime

    @maximum_execution_time.setter
    def maximum_execution_time(self, value: Optional["MultidimensionalTime"]) -> None:
        """
        Set maximumExecutionTime with validation.

        Args:
            value: The maximumExecutionTime to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maximumExecutionTime = None
            return

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"maximumExecutionTime must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._maximumExecutionTime = value
        # The minimum simulated execution time.
        self._minimumExecutionTime: Optional["MultidimensionalTime"] = None

    @property
    def minimum_execution_time(self) -> Optional["MultidimensionalTime"]:
        """Get minimumExecutionTime (Pythonic accessor)."""
        return self._minimumExecutionTime

    @minimum_execution_time.setter
    def minimum_execution_time(self, value: Optional["MultidimensionalTime"]) -> None:
        """
        Set minimumExecutionTime with validation.

        Args:
            value: The minimumExecutionTime to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minimumExecutionTime = None
            return

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"minimumExecutionTime must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._minimumExecutionTime = value
        # The nominal simulated execution time.
        self._nominalExecutionTime: Optional["MultidimensionalTime"] = None

    @property
    def nominal_execution_time(self) -> Optional["MultidimensionalTime"]:
        """Get nominalExecutionTime (Pythonic accessor)."""
        return self._nominalExecutionTime

    @nominal_execution_time.setter
    def nominal_execution_time(self, value: Optional["MultidimensionalTime"]) -> None:
        """
        Set nominalExecutionTime with validation.

        Args:
            value: The nominalExecutionTime to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nominalExecutionTime = None
            return

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"nominalExecutionTime must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._nominalExecutionTime = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMaximumExecutionTime(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for maximumExecutionTime.

        Returns:
            The maximumExecutionTime value

        Note:
            Delegates to maximum_execution_time property (CODING_RULE_V2_00017)
        """
        return self.maximum_execution_time  # Delegates to property

    def setMaximumExecutionTime(self, value: "MultidimensionalTime") -> "SimulatedExecutionTime":
        """
        AUTOSAR-compliant setter for maximumExecutionTime with method chaining.

        Args:
            value: The maximumExecutionTime to set

        Returns:
            self for method chaining

        Note:
            Delegates to maximum_execution_time property setter (gets validation automatically)
        """
        self.maximum_execution_time = value  # Delegates to property setter
        return self

    def getMinimumExecutionTime(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for minimumExecutionTime.

        Returns:
            The minimumExecutionTime value

        Note:
            Delegates to minimum_execution_time property (CODING_RULE_V2_00017)
        """
        return self.minimum_execution_time  # Delegates to property

    def setMinimumExecutionTime(self, value: "MultidimensionalTime") -> "SimulatedExecutionTime":
        """
        AUTOSAR-compliant setter for minimumExecutionTime with method chaining.

        Args:
            value: The minimumExecutionTime to set

        Returns:
            self for method chaining

        Note:
            Delegates to minimum_execution_time property setter (gets validation automatically)
        """
        self.minimum_execution_time = value  # Delegates to property setter
        return self

    def getNominalExecutionTime(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for nominalExecutionTime.

        Returns:
            The nominalExecutionTime value

        Note:
            Delegates to nominal_execution_time property (CODING_RULE_V2_00017)
        """
        return self.nominal_execution_time  # Delegates to property

    def setNominalExecutionTime(self, value: "MultidimensionalTime") -> "SimulatedExecutionTime":
        """
        AUTOSAR-compliant setter for nominalExecutionTime with method chaining.

        Args:
            value: The nominalExecutionTime to set

        Returns:
            self for method chaining

        Note:
            Delegates to nominal_execution_time property setter (gets validation automatically)
        """
        self.nominal_execution_time = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_maximum_execution_time(self, value: Optional["MultidimensionalTime"]) -> "SimulatedExecutionTime":
        """
        Set maximumExecutionTime and return self for chaining.

        Args:
            value: The maximumExecutionTime to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_maximum_execution_time("value")
        """
        self.maximum_execution_time = value  # Use property setter (gets validation)
        return self

    def with_minimum_execution_time(self, value: Optional["MultidimensionalTime"]) -> "SimulatedExecutionTime":
        """
        Set minimumExecutionTime and return self for chaining.

        Args:
            value: The minimumExecutionTime to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_minimum_execution_time("value")
        """
        self.minimum_execution_time = value  # Use property setter (gets validation)
        return self

    def with_nominal_execution_time(self, value: Optional["MultidimensionalTime"]) -> "SimulatedExecutionTime":
        """
        Set nominalExecutionTime and return self for chaining.

        Args:
            value: The nominalExecutionTime to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nominal_execution_time("value")
        """
        self.nominal_execution_time = value  # Use property setter (gets validation)
        return self
