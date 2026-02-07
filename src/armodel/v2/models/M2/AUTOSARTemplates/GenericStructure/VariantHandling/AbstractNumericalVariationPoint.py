from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class AbstractNumericalVariationPoint(ARObject, ABC):
    """
    This is an abstract NumericalValueVariationPoint. It is introduced to
    support the case that additional attributes are required for particular
    purposes.
    
    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling::AttributeValueVariationPoints::AbstractNumericalVariationPoint
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 969, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 240, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is AbstractNumericalVariationPoint:
            raise TypeError("AbstractNumericalVariationPoint is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====