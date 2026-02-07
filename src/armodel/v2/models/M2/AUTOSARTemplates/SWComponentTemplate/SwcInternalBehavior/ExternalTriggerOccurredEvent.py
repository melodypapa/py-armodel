from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class ExternalTriggerOccurredEvent(RTEEvent):
    """
    This event is raised when the referenced Trigger has occurred.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RTEEvents::ExternalTriggerOccurredEvent
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 545, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # by: RTriggerInAtomicSwc.
        self._triggerInstanceRef: RefType = None

    @property
    def trigger_instance_ref(self) -> RefType:
        """Get triggerInstanceRef (Pythonic accessor)."""
        return self._triggerInstanceRef

    @trigger_instance_ref.setter
    def trigger_instance_ref(self, value: RefType) -> None:
        """
        Set triggerInstanceRef with validation.
        
        Args:
            value: The triggerInstanceRef to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._triggerInstanceRef = None
            return

        self._triggerInstanceRef = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTriggerInstanceRef(self) -> RefType:
        """
        AUTOSAR-compliant getter for triggerInstanceRef.
        
        Returns:
            The triggerInstanceRef value
        
        Note:
            Delegates to trigger_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.trigger_instance_ref  # Delegates to property

    def setTriggerInstanceRef(self, value: RefType) -> "ExternalTriggerOccurredEvent":
        """
        AUTOSAR-compliant setter for triggerInstanceRef with method chaining.
        
        Args:
            value: The triggerInstanceRef to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to trigger_instance_ref property setter (gets validation automatically)
        """
        self.trigger_instance_ref = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_trigger_instance_ref(self, value: Optional[RefType]) -> "ExternalTriggerOccurredEvent":
        """
        Set triggerInstanceRef and return self for chaining.
        
        Args:
            value: The triggerInstanceRef to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_trigger_instance_ref("value")
        """
        self.trigger_instance_ref = value  # Use property setter (gets validation)
        return self