from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class GlobalSupervisionNeeds(ServiceNeeds):
    """
    Specifies the abstract needs on the configuration of the Watchdog Manager to
    get access on the Global Supervision control and status interface.
    
    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::GlobalSupervisionNeeds
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 318, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 709, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====