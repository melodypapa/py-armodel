from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class PhysicalDimensionMapping(ARObject):
    """
    This class represents a specific mapping between two PhysicalDimensions.
    
    Package: M2::MSR::AsamHdo::Units::PhysicalDimensionMapping
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 399, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the first PhysicalDimension of the PhysicalDimensionMapping.
        self._firstPhysical: Optional["PhysicalDimension"] = None

    @property
    def first_physical(self) -> Optional["PhysicalDimension"]:
        """Get firstPhysical (Pythonic accessor)."""
        return self._firstPhysical

    @first_physical.setter
    def first_physical(self, value: Optional["PhysicalDimension"]) -> None:
        """
        Set firstPhysical with validation.
        
        Args:
            value: The firstPhysical to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._firstPhysical = None
            return

        if not isinstance(value, PhysicalDimension):
            raise TypeError(
                f"firstPhysical must be PhysicalDimension or None, got {type(value).__name__}"
            )
        self._firstPhysical = value
        # This represents the first PhysicalDimension of the PhysicalDimensionMapping.
        self._secondPhysical: Optional["PhysicalDimension"] = None

    @property
    def second_physical(self) -> Optional["PhysicalDimension"]:
        """Get secondPhysical (Pythonic accessor)."""
        return self._secondPhysical

    @second_physical.setter
    def second_physical(self, value: Optional["PhysicalDimension"]) -> None:
        """
        Set secondPhysical with validation.
        
        Args:
            value: The secondPhysical to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._secondPhysical = None
            return

        if not isinstance(value, PhysicalDimension):
            raise TypeError(
                f"secondPhysical must be PhysicalDimension or None, got {type(value).__name__}"
            )
        self._secondPhysical = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFirstPhysical(self) -> "PhysicalDimension":
        """
        AUTOSAR-compliant getter for firstPhysical.
        
        Returns:
            The firstPhysical value
        
        Note:
            Delegates to first_physical property (CODING_RULE_V2_00017)
        """
        return self.first_physical  # Delegates to property

    def setFirstPhysical(self, value: "PhysicalDimension") -> "PhysicalDimensionMapping":
        """
        AUTOSAR-compliant setter for firstPhysical with method chaining.
        
        Args:
            value: The firstPhysical to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to first_physical property setter (gets validation automatically)
        """
        self.first_physical = value  # Delegates to property setter
        return self

    def getSecondPhysical(self) -> "PhysicalDimension":
        """
        AUTOSAR-compliant getter for secondPhysical.
        
        Returns:
            The secondPhysical value
        
        Note:
            Delegates to second_physical property (CODING_RULE_V2_00017)
        """
        return self.second_physical  # Delegates to property

    def setSecondPhysical(self, value: "PhysicalDimension") -> "PhysicalDimensionMapping":
        """
        AUTOSAR-compliant setter for secondPhysical with method chaining.
        
        Args:
            value: The secondPhysical to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to second_physical property setter (gets validation automatically)
        """
        self.second_physical = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_first_physical(self, value: Optional["PhysicalDimension"]) -> "PhysicalDimensionMapping":
        """
        Set firstPhysical and return self for chaining.
        
        Args:
            value: The firstPhysical to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_first_physical("value")
        """
        self.first_physical = value  # Use property setter (gets validation)
        return self

    def with_second_physical(self, value: Optional["PhysicalDimension"]) -> "PhysicalDimensionMapping":
        """
        Set secondPhysical and return self for chaining.
        
        Args:
            value: The secondPhysical to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_second_physical("value")
        """
        self.second_physical = value  # Use property setter (gets validation)
        return self