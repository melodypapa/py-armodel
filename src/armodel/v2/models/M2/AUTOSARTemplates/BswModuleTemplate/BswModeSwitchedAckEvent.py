from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

class BswModeSwitchedAckEvent(BswScheduleEvent):
    """
    The event is raised after a switch of the referenced mode group has been
    acknowledged or an error occurs. The referenced mode group shall be provided
    by this module.
    
    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswModeSwitchedAckEvent
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 95, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # A mode group provided by this module.
        # The of a switch of this group raises this.
        self._modeGroup: RefType = None

    @property
    def mode_group(self) -> RefType:
        """Get modeGroup (Pythonic accessor)."""
        return self._modeGroup

    @mode_group.setter
    def mode_group(self, value: RefType) -> None:
        """
        Set modeGroup with validation.
        
        Args:
            value: The modeGroup to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._modeGroup = None
            return

        self._modeGroup = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getModeGroup(self) -> RefType:
        """
        AUTOSAR-compliant getter for modeGroup.
        
        Returns:
            The modeGroup value
        
        Note:
            Delegates to mode_group property (CODING_RULE_V2_00017)
        """
        return self.mode_group  # Delegates to property

    def setModeGroup(self, value: RefType) -> "BswModeSwitchedAckEvent":
        """
        AUTOSAR-compliant setter for modeGroup with method chaining.
        
        Args:
            value: The modeGroup to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to mode_group property setter (gets validation automatically)
        """
        self.mode_group = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_mode_group(self, value: Optional[RefType]) -> "BswModeSwitchedAckEvent":
        """
        Set modeGroup and return self for chaining.
        
        Args:
            value: The modeGroup to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_mode_group("value")
        """
        self.mode_group = value  # Use property setter (gets validation)
        return self