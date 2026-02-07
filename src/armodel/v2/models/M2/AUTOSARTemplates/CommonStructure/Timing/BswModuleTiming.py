from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class BswModuleTiming(TimingExtension):
    """
    A model element used to define timing descriptions and constraints for the
    BswInternalBehavior of one BSW Module. Thereby, for each BswInternalBehavior
    a separate timing can be specified. A constraint defined at this level holds
    true for all Implementations of that BswInternalBehavior. TimingDescriptions
    aggregated by BswModuleTiming are restricted to event chains referring to
    events which are derived from the class TDEventBswInternalBehavior.
    
    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingExtensions::BswModuleTiming
    
    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 28, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This defines the scope of a BswModuleTiming.
        # All descriptions and constraints shall within this scope.
        self._behavior: Optional["BswInternalBehavior"] = None

    @property
    def behavior(self) -> Optional["BswInternalBehavior"]:
        """Get behavior (Pythonic accessor)."""
        return self._behavior

    @behavior.setter
    def behavior(self, value: Optional["BswInternalBehavior"]) -> None:
        """
        Set behavior with validation.
        
        Args:
            value: The behavior to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._behavior = None
            return

        if not isinstance(value, BswInternalBehavior):
            raise TypeError(
                f"behavior must be BswInternalBehavior or None, got {type(value).__name__}"
            )
        self._behavior = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBehavior(self) -> "BswInternalBehavior":
        """
        AUTOSAR-compliant getter for behavior.
        
        Returns:
            The behavior value
        
        Note:
            Delegates to behavior property (CODING_RULE_V2_00017)
        """
        return self.behavior  # Delegates to property

    def setBehavior(self, value: "BswInternalBehavior") -> "BswModuleTiming":
        """
        AUTOSAR-compliant setter for behavior with method chaining.
        
        Args:
            value: The behavior to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to behavior property setter (gets validation automatically)
        """
        self.behavior = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_behavior(self, value: Optional["BswInternalBehavior"]) -> "BswModuleTiming":
        """
        Set behavior and return self for chaining.
        
        Args:
            value: The behavior to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_behavior("value")
        """
        self.behavior = value  # Use property setter (gets validation)
        return self