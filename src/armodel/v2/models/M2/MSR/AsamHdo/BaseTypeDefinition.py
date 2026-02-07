from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class BaseTypeDefinition(ARObject, ABC):
    """
    This meta-class represents the ability to define a basetype.
    
    Package: M2::MSR::AsamHdo::BaseTypes::BaseTypeDefinition
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 290, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is BaseTypeDefinition:
            raise TypeError("BaseTypeDefinition is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====