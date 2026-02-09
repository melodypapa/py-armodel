"""
AUTOSAR Package - ExecutionTimeConstraint

Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::ExecutionTimeConstraint
"""

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.__init__ import (
    TimingConstraint,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)


class ExecutionTimeConstraint(TimingConstraint):
    """
    Constrains the execution time of the referenced executable in component
    between a minimum and maximum interval. The time to execute the executable
    including interruptions by other entities and including external calls is
    commonly called "response time". The TimingExtensions provide the concept of
    event chains and latency constraints for that purpose. An event chain from
    the start of the entity to the termination of the entity with according
    latency constraint represents a response time constraint for that executable
    entity.
    
    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::ExecutionTimeConstraint::ExecutionTimeConstraint
    
    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 130, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # for the ExecutionTimeConstraint.
        # If the entity is in a module no component shall be provided.
        # by: ComponentIn.
        self._component: Optional["SwComponent"] = None

    @property
    def component(self) -> Optional["SwComponent"]:
        """Get component (Pythonic accessor)."""
        return self._component

    @component.setter
    def component(self, value: Optional["SwComponent"]) -> None:
        """
        Set component with validation.
        
        Args:
            value: The component to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._component = None
            return

        if not isinstance(value, SwComponent):
            raise TypeError(
                f"component must be SwComponent or None, got {type(value).__name__}"
            )
        self._component = value
        self._executable: Optional["ExecutableEntity"] = None

    @property
    def executable(self) -> Optional["ExecutableEntity"]:
        """Get executable (Pythonic accessor)."""
        return self._executable

    @executable.setter
    def executable(self, value: Optional["ExecutableEntity"]) -> None:
        """
        Set executable with validation.
        
        Args:
            value: The executable to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._executable = None
            return

        if not isinstance(value, ExecutableEntity):
            raise TypeError(
                f"executable must be ExecutableEntity or None, got {type(value).__name__}"
            )
        self._executable = value
        # ExecutionTimeConstraint,.
        self._executionTime: Optional["ExecutionTimeType"] = None

    @property
    def execution_time(self) -> Optional["ExecutionTimeType"]:
        """Get executionTime (Pythonic accessor)."""
        return self._executionTime

    @execution_time.setter
    def execution_time(self, value: Optional["ExecutionTimeType"]) -> None:
        """
        Set executionTime with validation.
        
        Args:
            value: The executionTime to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._executionTime = None
            return

        if not isinstance(value, ExecutionTimeType):
            raise TypeError(
                f"executionTime must be ExecutionTimeType or None, got {type(value).__name__}"
            )
        self._executionTime = value
        self._maximum: Optional["MultidimensionalTime"] = None

    @property
    def maximum(self) -> Optional["MultidimensionalTime"]:
        """Get maximum (Pythonic accessor)."""
        return self._maximum

    @maximum.setter
    def maximum(self, value: Optional["MultidimensionalTime"]) -> None:
        """
        Set maximum with validation.
        
        Args:
            value: The maximum to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maximum = None
            return

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"maximum must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._maximum = value
        self._minimum: Optional["MultidimensionalTime"] = None

    @property
    def minimum(self) -> Optional["MultidimensionalTime"]:
        """Get minimum (Pythonic accessor)."""
        return self._minimum

    @minimum.setter
    def minimum(self, value: Optional["MultidimensionalTime"]) -> None:
        """
        Set minimum with validation.
        
        Args:
            value: The minimum to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minimum = None
            return

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"minimum must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._minimum = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getComponent(self) -> "SwComponent":
        """
        AUTOSAR-compliant getter for component.
        
        Returns:
            The component value
        
        Note:
            Delegates to component property (CODING_RULE_V2_00017)
        """
        return self.component  # Delegates to property

    def setComponent(self, value: "SwComponent") -> "ExecutionTimeConstraint":
        """
        AUTOSAR-compliant setter for component with method chaining.
        
        Args:
            value: The component to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to component property setter (gets validation automatically)
        """
        self.component = value  # Delegates to property setter
        return self

    def getExecutable(self) -> "ExecutableEntity":
        """
        AUTOSAR-compliant getter for executable.
        
        Returns:
            The executable value
        
        Note:
            Delegates to executable property (CODING_RULE_V2_00017)
        """
        return self.executable  # Delegates to property

    def setExecutable(self, value: "ExecutableEntity") -> "ExecutionTimeConstraint":
        """
        AUTOSAR-compliant setter for executable with method chaining.
        
        Args:
            value: The executable to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to executable property setter (gets validation automatically)
        """
        self.executable = value  # Delegates to property setter
        return self

    def getExecutionTime(self) -> "ExecutionTimeType":
        """
        AUTOSAR-compliant getter for executionTime.
        
        Returns:
            The executionTime value
        
        Note:
            Delegates to execution_time property (CODING_RULE_V2_00017)
        """
        return self.execution_time  # Delegates to property

    def setExecutionTime(self, value: "ExecutionTimeType") -> "ExecutionTimeConstraint":
        """
        AUTOSAR-compliant setter for executionTime with method chaining.
        
        Args:
            value: The executionTime to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to execution_time property setter (gets validation automatically)
        """
        self.execution_time = value  # Delegates to property setter
        return self

    def getMaximum(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for maximum.
        
        Returns:
            The maximum value
        
        Note:
            Delegates to maximum property (CODING_RULE_V2_00017)
        """
        return self.maximum  # Delegates to property

    def setMaximum(self, value: "MultidimensionalTime") -> "ExecutionTimeConstraint":
        """
        AUTOSAR-compliant setter for maximum with method chaining.
        
        Args:
            value: The maximum to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to maximum property setter (gets validation automatically)
        """
        self.maximum = value  # Delegates to property setter
        return self

    def getMinimum(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for minimum.
        
        Returns:
            The minimum value
        
        Note:
            Delegates to minimum property (CODING_RULE_V2_00017)
        """
        return self.minimum  # Delegates to property

    def setMinimum(self, value: "MultidimensionalTime") -> "ExecutionTimeConstraint":
        """
        AUTOSAR-compliant setter for minimum with method chaining.
        
        Args:
            value: The minimum to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to minimum property setter (gets validation automatically)
        """
        self.minimum = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_component(self, value: Optional["SwComponent"]) -> "ExecutionTimeConstraint":
        """
        Set component and return self for chaining.
        
        Args:
            value: The component to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_component("value")
        """
        self.component = value  # Use property setter (gets validation)
        return self

    def with_executable(self, value: Optional["ExecutableEntity"]) -> "ExecutionTimeConstraint":
        """
        Set executable and return self for chaining.
        
        Args:
            value: The executable to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_executable("value")
        """
        self.executable = value  # Use property setter (gets validation)
        return self

    def with_execution_time(self, value: Optional["ExecutionTimeType"]) -> "ExecutionTimeConstraint":
        """
        Set executionTime and return self for chaining.
        
        Args:
            value: The executionTime to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_execution_time("value")
        """
        self.execution_time = value  # Use property setter (gets validation)
        return self

    def with_maximum(self, value: Optional["MultidimensionalTime"]) -> "ExecutionTimeConstraint":
        """
        Set maximum and return self for chaining.
        
        Args:
            value: The maximum to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_maximum("value")
        """
        self.maximum = value  # Use property setter (gets validation)
        return self

    def with_minimum(self, value: Optional["MultidimensionalTime"]) -> "ExecutionTimeConstraint":
        """
        Set minimum and return self for chaining.
        
        Args:
            value: The minimum to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_minimum("value")
        """
        self.minimum = value  # Use property setter (gets validation)
        return self


class ExecutionTimeTypeEnum(AREnum):
    """
    ExecutionTimeTypeEnum enumeration

Specifies the type of the executionTimeType for a ExecutionTimeConstraint. Aggregated by ExecutionTimeConstraint.executionTimeType (cid:53) 130 of 277 Document ID 411: AUTOSAR_CP_TPS_TimingExtensions Specification of Timing Extensions for Classic Platform AUTOSAR CP R23-11 (cid:52)

Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::ExecutionTimeConstraint
    """
    # Indicates that the given execution time is the time used to execute the executable WITHOUT any interruption and WITH external calls.
    gross = "0"

    # Indicates that the given execution time is the time used to execute the executable WITHOUT any interruption and WITHOUT any external calls.
    net = "1"
