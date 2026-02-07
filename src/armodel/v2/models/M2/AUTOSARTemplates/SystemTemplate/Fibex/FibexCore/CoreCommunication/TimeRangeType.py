from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class TimeRangeType(ARObject):
    """
    The timeRange can be specified with the value attribute. Optionally a
    tolerance can be defined.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::Timing::TimeRangeType
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 398, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Optional specification of a tolerance.
        self._toleranceTolerance: Optional["TimeRangeType"] = None

    @property
    def tolerance_tolerance(self) -> Optional["TimeRangeType"]:
        """Get toleranceTolerance (Pythonic accessor)."""
        return self._toleranceTolerance

    @tolerance_tolerance.setter
    def tolerance_tolerance(self, value: Optional["TimeRangeType"]) -> None:
        """
        Set toleranceTolerance with validation.
        
        Args:
            value: The toleranceTolerance to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._toleranceTolerance = None
            return

        if not isinstance(value, TimeRangeType):
            raise TypeError(
                f"toleranceTolerance must be TimeRangeType or None, got {type(value).__name__}"
            )
        self._toleranceTolerance = value
        # Average value of a date (in seconds).
        self._value: Optional["TimeValue"] = None

    @property
    def value(self) -> Optional["TimeValue"]:
        """Get value (Pythonic accessor)."""
        return self._value

    @value.setter
    def value(self, value: Optional["TimeValue"]) -> None:
        """
        Set value with validation.
        
        Args:
            value: The value to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._value = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"value must be TimeValue or None, got {type(value).__name__}"
            )
        self._value = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getToleranceTolerance(self) -> "TimeRangeType":
        """
        AUTOSAR-compliant getter for toleranceTolerance.
        
        Returns:
            The toleranceTolerance value
        
        Note:
            Delegates to tolerance_tolerance property (CODING_RULE_V2_00017)
        """
        return self.tolerance_tolerance  # Delegates to property

    def setToleranceTolerance(self, value: "TimeRangeType") -> "TimeRangeType":
        """
        AUTOSAR-compliant setter for toleranceTolerance with method chaining.
        
        Args:
            value: The toleranceTolerance to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to tolerance_tolerance property setter (gets validation automatically)
        """
        self.tolerance_tolerance = value  # Delegates to property setter
        return self

    def getValue(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for value.
        
        Returns:
            The value value
        
        Note:
            Delegates to value property (CODING_RULE_V2_00017)
        """
        return self.value  # Delegates to property

    def setValue(self, value: "TimeValue") -> "TimeRangeType":
        """
        AUTOSAR-compliant setter for value with method chaining.
        
        Args:
            value: The value to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to value property setter (gets validation automatically)
        """
        self.value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_tolerance_tolerance(self, value: Optional["TimeRangeType"]) -> "TimeRangeType":
        """
        Set toleranceTolerance and return self for chaining.
        
        Args:
            value: The toleranceTolerance to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_tolerance_tolerance("value")
        """
        self.tolerance_tolerance = value  # Use property setter (gets validation)
        return self

    def with_value(self, value: Optional["TimeValue"]) -> "TimeRangeType":
        """
        Set value and return self for chaining.
        
        Args:
            value: The value to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_value("value")
        """
        self.value = value  # Use property setter (gets validation)
        return self