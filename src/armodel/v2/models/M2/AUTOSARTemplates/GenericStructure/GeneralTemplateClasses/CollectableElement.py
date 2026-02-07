from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class CollectableElement(Identifiable, ABC):
    """
    This meta-class specifies the ability to be part of a specific AUTOSAR
    collection of ARPackages or ARElements. The scope of collection has been
    extended beyond CollectableElement with Revision 4.0.3. For compatibility
    reasons the name of this meta Class was not changed.
    
    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ElementCollection::CollectableElement
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 399, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is CollectableElement:
            raise TypeError("CollectableElement is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====