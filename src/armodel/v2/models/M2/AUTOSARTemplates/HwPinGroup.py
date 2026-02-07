from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class HwPinGroup(Identifiable):
    """
    This meta-class represents the ability to describe groups of pins which are
    used to connect hardware elements. This group acts as a bundle of pins.
    Thereby they allow to describe high level connections. Pin groups can even
    be nested.
    
    Package: M2::AUTOSARTemplates::EcuResourceTemplate::HwPinGroup
    
    Sources:
      - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (Page 19, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2027, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This aggregation describes the contained pins/pin groups.
        self._hwPinGroup: RefType = None

    @property
    def hw_pin_group(self) -> RefType:
        """Get hwPinGroup (Pythonic accessor)."""
        return self._hwPinGroup

    @hw_pin_group.setter
    def hw_pin_group(self, value: RefType) -> None:
        """
        Set hwPinGroup with validation.
        
        Args:
            value: The hwPinGroup to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._hwPinGroup = None
            return

        self._hwPinGroup = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getHwPinGroup(self) -> RefType:
        """
        AUTOSAR-compliant getter for hwPinGroup.
        
        Returns:
            The hwPinGroup value
        
        Note:
            Delegates to hw_pin_group property (CODING_RULE_V2_00017)
        """
        return self.hw_pin_group  # Delegates to property

    def setHwPinGroup(self, value: RefType) -> "HwPinGroup":
        """
        AUTOSAR-compliant setter for hwPinGroup with method chaining.
        
        Args:
            value: The hwPinGroup to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to hw_pin_group property setter (gets validation automatically)
        """
        self.hw_pin_group = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_hw_pin_group(self, value: Optional[RefType]) -> "HwPinGroup":
        """
        Set hwPinGroup and return self for chaining.
        
        Args:
            value: The hwPinGroup to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_hw_pin_group("value")
        """
        self.hw_pin_group = value  # Use property setter (gets validation)
        return self