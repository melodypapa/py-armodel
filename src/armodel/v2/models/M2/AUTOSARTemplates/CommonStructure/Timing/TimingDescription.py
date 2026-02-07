from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class TimingDescription(Identifiable, ABC):
    """
    The abstract parent class of the model elements that are used to define the
    scope of a timing constraint.
    
    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription
    
    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 253, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is TimingDescription:
            raise TypeError("TimingDescription is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====