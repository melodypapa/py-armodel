from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class DiagnosticEnvConditionFormulaPart(ARObject, ABC):
    """
    A DiagnosticEnvConditionFormulaPart can either be a atomic condition, e.g. a
    DiagnosticEnvCompare Condition, or a DiagnosticEnvConditionFormula, again,
    which allows arbitrary nesting.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::EnvironmentalCondition::DiagnosticEnvConditionFormulaPart
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 80, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is DiagnosticEnvConditionFormulaPart:
            raise TypeError("DiagnosticEnvConditionFormulaPart is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====