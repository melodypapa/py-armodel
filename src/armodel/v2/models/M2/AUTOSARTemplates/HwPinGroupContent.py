from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class HwPinGroupContent(ARObject):
    """
    This meta-class specifies a mixture of hwPins and hwPinGroups.
    
    Package: M2::AUTOSARTemplates::EcuResourceTemplate::HwPinGroupContent
    
    Sources:
      - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (Page 20, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This aggregation represents a hardware pin in a hardware atpVariation.
        self._hwPin: Optional["HwPin"] = None

    @property
    def hw_pin(self) -> Optional["HwPin"]:
        """Get hwPin (Pythonic accessor)."""
        return self._hwPin

    @hw_pin.setter
    def hw_pin(self, value: Optional["HwPin"]) -> None:
        """
        Set hwPin with validation.
        
        Args:
            value: The hwPin to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._hwPin = None
            return

        if not isinstance(value, HwPin):
            raise TypeError(
                f"hwPin must be HwPin or None, got {type(value).__name__}"
            )
        self._hwPin = value
        # This aggregation represents a nested hardware pin group.
        # atpVariation.
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

    def getHwPin(self) -> "HwPin":
        """
        AUTOSAR-compliant getter for hwPin.
        
        Returns:
            The hwPin value
        
        Note:
            Delegates to hw_pin property (CODING_RULE_V2_00017)
        """
        return self.hw_pin  # Delegates to property

    def setHwPin(self, value: "HwPin") -> "HwPinGroupContent":
        """
        AUTOSAR-compliant setter for hwPin with method chaining.
        
        Args:
            value: The hwPin to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to hw_pin property setter (gets validation automatically)
        """
        self.hw_pin = value  # Delegates to property setter
        return self

    def getHwPinGroup(self) -> RefType:
        """
        AUTOSAR-compliant getter for hwPinGroup.
        
        Returns:
            The hwPinGroup value
        
        Note:
            Delegates to hw_pin_group property (CODING_RULE_V2_00017)
        """
        return self.hw_pin_group  # Delegates to property

    def setHwPinGroup(self, value: RefType) -> "HwPinGroupContent":
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

    def with_hw_pin(self, value: Optional["HwPin"]) -> "HwPinGroupContent":
        """
        Set hwPin and return self for chaining.
        
        Args:
            value: The hwPin to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_hw_pin("value")
        """
        self.hw_pin = value  # Use property setter (gets validation)
        return self

    def with_hw_pin_group(self, value: Optional[RefType]) -> "HwPinGroupContent":
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