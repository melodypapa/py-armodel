from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PackageableElement import PackageableElement

class FibexElement(PackageableElement, ABC):
    """
    ASAM FIBEX elements specifying Communication and Topology.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::FibexElement
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2026, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 445, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is FibexElement:
            raise TypeError("FibexElement is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====