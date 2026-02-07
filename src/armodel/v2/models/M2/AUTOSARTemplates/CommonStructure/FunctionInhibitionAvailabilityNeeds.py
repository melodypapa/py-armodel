from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class FunctionInhibitionAvailabilityNeeds(ServiceNeeds):
    """
    Specifies the abstract needs on the configuration of the Function Inhibition
    Manager to provide the control function for one Function Identifier (FID).
    
    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::FunctionInhibitionAvailabilityNeeds
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 318, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 751, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference represents the controlled FID.
        self._controlledFid: Optional["FunctionInhibitionNeeds"] = None

    @property
    def controlled_fid(self) -> Optional["FunctionInhibitionNeeds"]:
        """Get controlledFid (Pythonic accessor)."""
        return self._controlledFid

    @controlled_fid.setter
    def controlled_fid(self, value: Optional["FunctionInhibitionNeeds"]) -> None:
        """
        Set controlledFid with validation.
        
        Args:
            value: The controlledFid to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._controlledFid = None
            return

        if not isinstance(value, FunctionInhibitionNeeds):
            raise TypeError(
                f"controlledFid must be FunctionInhibitionNeeds or None, got {type(value).__name__}"
            )
        self._controlledFid = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getControlledFid(self) -> "FunctionInhibitionNeeds":
        """
        AUTOSAR-compliant getter for controlledFid.
        
        Returns:
            The controlledFid value
        
        Note:
            Delegates to controlled_fid property (CODING_RULE_V2_00017)
        """
        return self.controlled_fid  # Delegates to property

    def setControlledFid(self, value: "FunctionInhibitionNeeds") -> "FunctionInhibitionAvailabilityNeeds":
        """
        AUTOSAR-compliant setter for controlledFid with method chaining.
        
        Args:
            value: The controlledFid to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to controlled_fid property setter (gets validation automatically)
        """
        self.controlled_fid = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_controlled_fid(self, value: Optional["FunctionInhibitionNeeds"]) -> "FunctionInhibitionAvailabilityNeeds":
        """
        Set controlledFid and return self for chaining.
        
        Args:
            value: The controlledFid to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_controlled_fid("value")
        """
        self.controlled_fid = value  # Use property setter (gets validation)
        return self