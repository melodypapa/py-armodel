from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class TimingConstraint(Traceable, ABC):
    """
    The abstract parent class of different timing constraints supported by the
    Timing extension. A concrete timing constraint is used to bound the timing
    behavior of the model elements in its scope.
    
    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::TimingConstraint
    
    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 253, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is TimingConstraint:
            raise TypeError("TimingConstraint is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # A timing condition the timing constraint depends on.
        # In it specifies the condition the timing constraint.
        self._timingCondition: Optional["TimingCondition"] = None

    @property
    def timing_condition(self) -> Optional["TimingCondition"]:
        """Get timingCondition (Pythonic accessor)."""
        return self._timingCondition

    @timing_condition.setter
    def timing_condition(self, value: Optional["TimingCondition"]) -> None:
        """
        Set timingCondition with validation.
        
        Args:
            value: The timingCondition to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timingCondition = None
            return

        if not isinstance(value, TimingCondition):
            raise TypeError(
                f"timingCondition must be TimingCondition or None, got {type(value).__name__}"
            )
        self._timingCondition = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTimingCondition(self) -> "TimingCondition":
        """
        AUTOSAR-compliant getter for timingCondition.
        
        Returns:
            The timingCondition value
        
        Note:
            Delegates to timing_condition property (CODING_RULE_V2_00017)
        """
        return self.timing_condition  # Delegates to property

    def setTimingCondition(self, value: "TimingCondition") -> "TimingConstraint":
        """
        AUTOSAR-compliant setter for timingCondition with method chaining.
        
        Args:
            value: The timingCondition to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to timing_condition property setter (gets validation automatically)
        """
        self.timing_condition = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_timing_condition(self, value: Optional["TimingCondition"]) -> "TimingConstraint":
        """
        Set timingCondition and return self for chaining.
        
        Args:
            value: The timingCondition to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_timing_condition("value")
        """
        self.timing_condition = value  # Use property setter (gets validation)
        return self