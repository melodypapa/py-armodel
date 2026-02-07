from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class IdentCaption(Identifiable, ABC):
    """
    This meta-class represents the caption. This allows having some meta-classes
    optionally identifiable.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::RPTScenario::IdentCaption
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 317, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 851, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is IdentCaption:
            raise TypeError("IdentCaption is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====