from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class RelativeTolerance(ARObject):
    """
    Maximum allowable deviation
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::Timing::RelativeTolerance
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 398, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Maximum allowable deviation in percent (percent of the.
        self._relative: Optional["Integer"] = None

    @property
    def relative(self) -> Optional["Integer"]:
        """Get relative (Pythonic accessor)."""
        return self._relative

    @relative.setter
    def relative(self, value: Optional["Integer"]) -> None:
        """
        Set relative with validation.
        
        Args:
            value: The relative to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._relative = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"relative must be Integer or None, got {type(value).__name__}"
            )
        self._relative = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRelative(self) -> "Integer":
        """
        AUTOSAR-compliant getter for relative.
        
        Returns:
            The relative value
        
        Note:
            Delegates to relative property (CODING_RULE_V2_00017)
        """
        return self.relative  # Delegates to property

    def setRelative(self, value: "Integer") -> "RelativeTolerance":
        """
        AUTOSAR-compliant setter for relative with method chaining.
        
        Args:
            value: The relative to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to relative property setter (gets validation automatically)
        """
        self.relative = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_relative(self, value: Optional["Integer"]) -> "RelativeTolerance":
        """
        Set relative and return self for chaining.
        
        Args:
            value: The relative to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_relative("value")
        """
        self.relative = value  # Use property setter (gets validation)
        return self