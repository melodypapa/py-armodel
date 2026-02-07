from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class TimingModeInstance(Identifiable):
    """
    This class specifies the mode declaration to be checked in a specific
    instance of a mode declaration group. This is used in a timing condition
    formula as an operand of the unary timing function TIMEX_mode Active to
    check whether the mode declaration is active at the point in time this
    expression is evaluated.
    
    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingCondition::TimingModeInstance
    
    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 37, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This refers to a specific mode declaration in the given.
        self._modeInstance: Optional["ModeInSwcBsw"] = None

    @property
    def mode_instance(self) -> Optional["ModeInSwcBsw"]:
        """Get modeInstance (Pythonic accessor)."""
        return self._modeInstance

    @mode_instance.setter
    def mode_instance(self, value: Optional["ModeInSwcBsw"]) -> None:
        """
        Set modeInstance with validation.
        
        Args:
            value: The modeInstance to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._modeInstance = None
            return

        if not isinstance(value, ModeInSwcBsw):
            raise TypeError(
                f"modeInstance must be ModeInSwcBsw or None, got {type(value).__name__}"
            )
        self._modeInstance = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getModeInstance(self) -> "ModeInSwcBsw":
        """
        AUTOSAR-compliant getter for modeInstance.
        
        Returns:
            The modeInstance value
        
        Note:
            Delegates to mode_instance property (CODING_RULE_V2_00017)
        """
        return self.mode_instance  # Delegates to property

    def setModeInstance(self, value: "ModeInSwcBsw") -> "TimingModeInstance":
        """
        AUTOSAR-compliant setter for modeInstance with method chaining.
        
        Args:
            value: The modeInstance to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to mode_instance property setter (gets validation automatically)
        """
        self.mode_instance = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_mode_instance(self, value: Optional["ModeInSwcBsw"]) -> "TimingModeInstance":
        """
        Set modeInstance and return self for chaining.
        
        Args:
            value: The modeInstance to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_mode_instance("value")
        """
        self.mode_instance = value  # Use property setter (gets validation)
        return self