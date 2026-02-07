from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

class TriggerInterface(PortInterface):
    """
    A trigger interface declares a number of triggers that can be sent by an
    trigger source.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::TriggerInterface
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 109, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2076, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The Trigger of this trigger interface.
        self._trigger: List[RefType] = []

    @property
    def trigger(self) -> List[RefType]:
        """Get trigger (Pythonic accessor)."""
        return self._trigger

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTrigger(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for trigger.
        
        Returns:
            The trigger value
        
        Note:
            Delegates to trigger property (CODING_RULE_V2_00017)
        """
        return self.trigger  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====