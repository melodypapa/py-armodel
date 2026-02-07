from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class RoughEstimateOfExecutionTime(ExecutionTime):
    """
    Provides a description of a rough estimate on the ExecutionTime.
    
    Package: M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::ExecutionTime::RoughEstimateOfExecutionTime
    
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