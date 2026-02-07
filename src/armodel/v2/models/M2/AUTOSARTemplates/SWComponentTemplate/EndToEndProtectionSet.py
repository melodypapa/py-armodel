from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class EndToEndProtectionSet(ARElement):
    """
    This represents a container for collection EndToEndProtectionInformation.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::EndToEndProtection::EndToEndProtectionSet
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 214, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 383, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is one particular EndToEndProtection.
        # atpSplitable; atpVariation.
        self._endToEnd: List["EndToEndProtection"] = []

    @property
    def end_to_end(self) -> List["EndToEndProtection"]:
        """Get endToEnd (Pythonic accessor)."""
        return self._endToEnd

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEndToEnd(self) -> List["EndToEndProtection"]:
        """
        AUTOSAR-compliant getter for endToEnd.
        
        Returns:
            The endToEnd value
        
        Note:
            Delegates to end_to_end property (CODING_RULE_V2_00017)
        """
        return self.end_to_end  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====