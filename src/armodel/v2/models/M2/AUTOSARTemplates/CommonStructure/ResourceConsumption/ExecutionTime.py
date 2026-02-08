from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class MemorySectionLocation(ARObject):
    """
    Specifies in which hardware ProvidedMemorySegment the softwareMemorySection
    is located.

    Package: M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::ExecutionTime

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 162, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the hardware ProvidedMemorySegment.
        self._providedMemory: Optional["HwElement"] = None

    @property
    def provided_memory(self) -> Optional["HwElement"]:
        """Get providedMemory (Pythonic accessor)."""
        return self._providedMemory

    @provided_memory.setter
    def provided_memory(self, value: Optional["HwElement"]) -> None:
        """
        Set providedMemory with validation.

        Args:
            value: The providedMemory to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._providedMemory = None
            return

        if not isinstance(value, HwElement):
            raise TypeError(
                f"providedMemory must be HwElement or None, got {type(value).__name__}"
            )
        self._providedMemory = value
        # Reference to the MemorySection which is mapped on a hardware memory segment.
        self._software: Optional["MemorySection"] = None

    @property
    def software(self) -> Optional["MemorySection"]:
        """Get software (Pythonic accessor)."""
        return self._software

    @software.setter
    def software(self, value: Optional["MemorySection"]) -> None:
        """
        Set software with validation.

        Args:
            value: The software to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._software = None
            return

        if not isinstance(value, MemorySection):
            raise TypeError(
                f"software must be MemorySection or None, got {type(value).__name__}"
            )
        self._software = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getProvidedMemory(self) -> "HwElement":
        """
        AUTOSAR-compliant getter for providedMemory.

        Returns:
            The providedMemory value

        Note:
            Delegates to provided_memory property (CODING_RULE_V2_00017)
        """
        return self.provided_memory  # Delegates to property

    def setProvidedMemory(self, value: "HwElement") -> "MemorySectionLocation":
        """
        AUTOSAR-compliant setter for providedMemory with method chaining.

        Args:
            value: The providedMemory to set

        Returns:
            self for method chaining

        Note:
            Delegates to provided_memory property setter (gets validation automatically)
        """
        self.provided_memory = value  # Delegates to property setter
        return self

    def getSoftware(self) -> "MemorySection":
        """
        AUTOSAR-compliant getter for software.

        Returns:
            The software value

        Note:
            Delegates to software property (CODING_RULE_V2_00017)
        """
        return self.software  # Delegates to property

    def setSoftware(self, value: "MemorySection") -> "MemorySectionLocation":
        """
        AUTOSAR-compliant setter for software with method chaining.

        Args:
            value: The software to set

        Returns:
            self for method chaining

        Note:
            Delegates to software property setter (gets validation automatically)
        """
        self.software = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_provided_memory(self, value: Optional["HwElement"]) -> "MemorySectionLocation":
        """
        Set providedMemory and return self for chaining.

        Args:
            value: The providedMemory to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_provided_memory("value")
        """
        self.provided_memory = value  # Use property setter (gets validation)
        return self

    def with_software(self, value: Optional["MemorySection"]) -> "MemorySectionLocation":
        """
        Set software and return self for chaining.

        Args:
            value: The software to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_software("value")
        """
        self.software = value  # Use property setter (gets validation)
        return self

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.ExecutionTime import (
    ExecutionTime,
)


class AnalyzedExecutionTime(ExecutionTime):
    """
    AnalyzedExecutionTime provides an analytic method for specifying the best
    and worst case execution time.

    Package: M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::ExecutionTime

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

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.ExecutionTime import (
    ExecutionTime,
)


class MeasuredExecutionTime(ExecutionTime):
    """
    Specifies the ExecutionTime which has been gathered using measurement means.

    Package: M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::ExecutionTime

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 166, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The maximum measured execution time.
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
        # The minimum measured execution time.
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
        # The nominal measured execution time.
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

    def setMaximumExecutionTime(self, value: "MultidimensionalTime") -> "MeasuredExecutionTime":
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

    def setMinimumExecutionTime(self, value: "MultidimensionalTime") -> "MeasuredExecutionTime":
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

    def setNominalExecutionTime(self, value: "MultidimensionalTime") -> "MeasuredExecutionTime":
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

    def with_maximum_execution_time(self, value: Optional["MultidimensionalTime"]) -> "MeasuredExecutionTime":
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

    def with_minimum_execution_time(self, value: Optional["MultidimensionalTime"]) -> "MeasuredExecutionTime":
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

    def with_nominal_execution_time(self, value: Optional["MultidimensionalTime"]) -> "MeasuredExecutionTime":
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

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.ExecutionTime import (
    ExecutionTime,
)


class RoughEstimateOfExecutionTime(ExecutionTime):
    """
    Provides a description of a rough estimate on the ExecutionTime.

    Package: M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::ExecutionTime

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 167, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Provides description on the rough estimate of the.
        self._additional: Optional["String"] = None

    @property
    def additional(self) -> Optional["String"]:
        """Get additional (Pythonic accessor)."""
        return self._additional

    @additional.setter
    def additional(self, value: Optional["String"]) -> None:
        """
        Set additional with validation.

        Args:
            value: The additional to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._additional = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"additional must be String or None, got {type(value).__name__}"
            )
        self._additional = value
        # The estimated execution time.
        self._estimatedExecutionTime: Optional["MultidimensionalTime"] = None

    @property
    def estimated_execution_time(self) -> Optional["MultidimensionalTime"]:
        """Get estimatedExecutionTime (Pythonic accessor)."""
        return self._estimatedExecutionTime

    @estimated_execution_time.setter
    def estimated_execution_time(self, value: Optional["MultidimensionalTime"]) -> None:
        """
        Set estimatedExecutionTime with validation.

        Args:
            value: The estimatedExecutionTime to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._estimatedExecutionTime = None
            return

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"estimatedExecutionTime must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._estimatedExecutionTime = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAdditional(self) -> "String":
        """
        AUTOSAR-compliant getter for additional.

        Returns:
            The additional value

        Note:
            Delegates to additional property (CODING_RULE_V2_00017)
        """
        return self.additional  # Delegates to property

    def setAdditional(self, value: "String") -> "RoughEstimateOfExecutionTime":
        """
        AUTOSAR-compliant setter for additional with method chaining.

        Args:
            value: The additional to set

        Returns:
            self for method chaining

        Note:
            Delegates to additional property setter (gets validation automatically)
        """
        self.additional = value  # Delegates to property setter
        return self

    def getEstimatedExecutionTime(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for estimatedExecutionTime.

        Returns:
            The estimatedExecutionTime value

        Note:
            Delegates to estimated_execution_time property (CODING_RULE_V2_00017)
        """
        return self.estimated_execution_time  # Delegates to property

    def setEstimatedExecutionTime(self, value: "MultidimensionalTime") -> "RoughEstimateOfExecutionTime":
        """
        AUTOSAR-compliant setter for estimatedExecutionTime with method chaining.

        Args:
            value: The estimatedExecutionTime to set

        Returns:
            self for method chaining

        Note:
            Delegates to estimated_execution_time property setter (gets validation automatically)
        """
        self.estimated_execution_time = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_additional(self, value: Optional["String"]) -> "RoughEstimateOfExecutionTime":
        """
        Set additional and return self for chaining.

        Args:
            value: The additional to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_additional("value")
        """
        self.additional = value  # Use property setter (gets validation)
        return self

    def with_estimated_execution_time(self, value: Optional["MultidimensionalTime"]) -> "RoughEstimateOfExecutionTime":
        """
        Set estimatedExecutionTime and return self for chaining.

        Args:
            value: The estimatedExecutionTime to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_estimated_execution_time("value")
        """
        self.estimated_execution_time = value  # Use property setter (gets validation)
        return self
