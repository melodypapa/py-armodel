from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class AggregationTailoring(AttributeTailoring):
    """
    Tailoring of aggregations in the AUTOSAR meta-model
    
    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Data::AggregationTailoring
    
    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 113, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Local class tailoring which is applied if the content is this aggregation.
        self._typeTailoring: List["ClassTailoring"] = []

    @property
    def type_tailoring(self) -> List["ClassTailoring"]:
        """Get typeTailoring (Pythonic accessor)."""
        return self._typeTailoring

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTypeTailoring(self) -> List["ClassTailoring"]:
        """
        AUTOSAR-compliant getter for typeTailoring.
        
        Returns:
            The typeTailoring value
        
        Note:
            Delegates to type_tailoring property (CODING_RULE_V2_00017)
        """
        return self.type_tailoring  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====