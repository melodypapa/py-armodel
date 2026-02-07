from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class AtpBlueprintable(Identifiable, ABC):
    """
    This meta-class represents the ability to be derived from a Blueprint. As
    this class is an abstract one, particular blueprintable meta-classes inherit
    from this one.
    
    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::AbstractBlueprintStructure::AtpBlueprintable
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 424, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 162, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is AtpBlueprintable:
            raise TypeError("AtpBlueprintable is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====