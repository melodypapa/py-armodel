from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class TimingCondition(Identifiable):
    """
    A TimingCondition describes a dependency on a specific condition. The
    element owns an expression which describes the timing condition dependency.
    
    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingCondition::TimingCondition
    
    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 35, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the expression describing the dependency on a specific condition.
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

    def setTimingCondition(self, value: "TimingCondition") -> "TimingCondition":
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

    def with_timing_condition(self, value: Optional["TimingCondition"]) -> "TimingCondition":
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