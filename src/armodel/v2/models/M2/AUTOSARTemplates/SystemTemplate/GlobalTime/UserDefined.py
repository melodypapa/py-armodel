"""
AUTOSAR Package - UserDefined

Package: M2::AUTOSARTemplates::SystemTemplate::GlobalTime::UserDefined
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.__init__ import (
    GlobalTimeMaster,
    GlobalTimeSlave,
)




class UserDefinedGlobalTimeMaster(GlobalTimeMaster):
    """
    This represents the specialization of the GlobalTimeMaster for user defined
    communication.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::GlobalTime::UserDefined::UserDefinedGlobalTimeMaster
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 879, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class UserDefinedGlobalTimeSlave(GlobalTimeSlave):
    """
    This represents the specialization of the GlobalTimeSlave for user defined
    communication.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::GlobalTime::UserDefined::UserDefinedGlobalTimeSlave
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 879, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====