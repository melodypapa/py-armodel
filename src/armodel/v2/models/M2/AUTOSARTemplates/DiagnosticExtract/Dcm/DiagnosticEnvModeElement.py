from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Referrable import Referrable

class DiagnosticEnvModeElement(Referrable, ABC):
    """
    All ModeDeclarations that are referenced in a DiagnosticEnvModeCondition
    shall be defined as a DiagnosticEnvModeElement of this
    DiagnosticEnvironmentalCondition. This concept keeps the ARXML clean: It
    avoids that the DiagnosticEnvConditionFormula is cluttered by lengthy
    InstanceRef definitions. Furthermore, it allows that an InstanceRef only
    needs to be defined once and can be used multiple times in the different
    DiagnosticEnvModeConditions.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::EnvironmentalCondition::DiagnosticEnvModeElement
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 89, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is DiagnosticEnvModeElement:
            raise TypeError("DiagnosticEnvModeElement is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====