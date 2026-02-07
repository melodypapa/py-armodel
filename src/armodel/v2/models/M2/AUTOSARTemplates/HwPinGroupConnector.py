from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class HwPinGroupConnector(Describable):
    """
    This meta-class represents the ability to connect two pin groups.
    
    Package: M2::AUTOSARTemplates::EcuResourceTemplate::HwPinGroupConnector
    
    Sources:
      - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (Page 22, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents one particular connection between two pins.
        # The connected pins shall match the by the parent hwPinGroup atpVariation.
        self._hwPin: List["HwPinConnector"] = []

    @property
    def hw_pin(self) -> List["HwPinConnector"]:
        """Get hwPin (Pythonic accessor)."""
        return self._hwPin
        # This association connects two hardware pin groups.
        self._hwPinGroup: List[RefType] = []

    @property
    def hw_pin_group(self) -> List[RefType]:
        """Get hwPinGroup (Pythonic accessor)."""
        return self._hwPinGroup

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getHwPin(self) -> List["HwPinConnector"]:
        """
        AUTOSAR-compliant getter for hwPin.
        
        Returns:
            The hwPin value
        
        Note:
            Delegates to hw_pin property (CODING_RULE_V2_00017)
        """
        return self.hw_pin  # Delegates to property

    def getHwPinGroup(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for hwPinGroup.
        
        Returns:
            The hwPinGroup value
        
        Note:
            Delegates to hw_pin_group property (CODING_RULE_V2_00017)
        """
        return self.hw_pin_group  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====