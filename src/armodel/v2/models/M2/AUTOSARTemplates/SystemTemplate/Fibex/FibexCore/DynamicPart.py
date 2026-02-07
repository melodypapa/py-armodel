from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class DynamicPart(MultiplexedPart):
    """
    Dynamic part of a multiplexed I-Pdu. Reserved space which is used to
    transport varying SignalIPdus at the same position, controlled by the
    corresponding selectorFieldCode.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::DynamicPart
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 410, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Com IPdu alternatives that are transmitted in the Dynamic of the
        # MultiplexedIPdu.
        self._dynamicPart: List["DynamicPartAlternative"] = []

    @property
    def dynamic_part(self) -> List["DynamicPartAlternative"]:
        """Get dynamicPart (Pythonic accessor)."""
        return self._dynamicPart

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDynamicPart(self) -> List["DynamicPartAlternative"]:
        """
        AUTOSAR-compliant getter for dynamicPart.
        
        Returns:
            The dynamicPart value
        
        Note:
            Delegates to dynamic_part property (CODING_RULE_V2_00017)
        """
        return self.dynamic_part  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====