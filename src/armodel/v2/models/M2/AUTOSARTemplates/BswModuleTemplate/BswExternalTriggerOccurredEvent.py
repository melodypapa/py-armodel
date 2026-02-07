from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

class BswExternalTriggerOccurredEvent(BswScheduleEvent):
    """
    A BswEvent resulting from a trigger released by another module or cluster.
    
    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswExternalTriggerOccurredEvent
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 91, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The trigger associated with this event.
        # The trigger is this module.
        self._trigger: RefType = None

    @property
    def trigger(self) -> RefType:
        """Get trigger (Pythonic accessor)."""
        return self._trigger

    @trigger.setter
    def trigger(self, value: RefType) -> None:
        """
        Set trigger with validation.
        
        Args:
            value: The trigger to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._trigger = None
            return

        self._trigger = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTrigger(self) -> RefType:
        """
        AUTOSAR-compliant getter for trigger.
        
        Returns:
            The trigger value
        
        Note:
            Delegates to trigger property (CODING_RULE_V2_00017)
        """
        return self.trigger  # Delegates to property

    def setTrigger(self, value: RefType) -> "BswExternalTriggerOccurredEvent":
        """
        AUTOSAR-compliant setter for trigger with method chaining.
        
        Args:
            value: The trigger to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to trigger property setter (gets validation automatically)
        """
        self.trigger = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_trigger(self, value: Optional[RefType]) -> "BswExternalTriggerOccurredEvent":
        """
        Set trigger and return self for chaining.
        
        Args:
            value: The trigger to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_trigger("value")
        """
        self.trigger = value  # Use property setter (gets validation)
        return self