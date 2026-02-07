from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class AbstractCondition(ARObject, ABC):
    """
    A premise upon which the fulfillment of an agreement depends
    
    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Data::AbstractCondition
    
    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 102, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is AbstractCondition:
            raise TypeError("AbstractCondition is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====