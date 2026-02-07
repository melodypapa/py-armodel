from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class CompositeRuleBasedValueArgument(ARObject, ABC):
    """
    This meta-class has the ability to serve as the abstract base class for
    ValueSpecifications that can be used for compound primitive data types.
    
    Package: M2::AUTOSARTemplates::CommonStructure::Constants::CompositeRuleBasedValueArgument
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 473, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is CompositeRuleBasedValueArgument:
            raise TypeError("CompositeRuleBasedValueArgument is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====