from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class PduMappingDefaultValue(ARObject):
    """
    Default Value which will be distributed if no I-Pdu has been received since
    last sending.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Multiplatform::PduMappingDefaultValue
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 841, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The default value consists of a number of elements.
        # Each value element is represented by the element and in an array.
        self._defaultValue: List["DefaultValueElement"] = []

    @property
    def default_value(self) -> List["DefaultValueElement"]:
        """Get defaultValue (Pythonic accessor)."""
        return self._defaultValue

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDefaultValue(self) -> List["DefaultValueElement"]:
        """
        AUTOSAR-compliant getter for defaultValue.
        
        Returns:
            The defaultValue value
        
        Note:
            Delegates to default_value property (CODING_RULE_V2_00017)
        """
        return self.default_value  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====