from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class TDEventBsw(TimingDescriptionEvent, ABC):
    """
    This is used to describe timing events related to BSW modules.
    
    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription::TDEventBsw
    
    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 251, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is TDEventBsw:
            raise TypeError("TDEventBsw is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The scope of this timing event.
        self._bswModuleDescription: Optional["BswModuleDescription"] = None

    @property
    def bsw_module_description(self) -> Optional["BswModuleDescription"]:
        """Get bswModuleDescription (Pythonic accessor)."""
        return self._bswModuleDescription

    @bsw_module_description.setter
    def bsw_module_description(self, value: Optional["BswModuleDescription"]) -> None:
        """
        Set bswModuleDescription with validation.
        
        Args:
            value: The bswModuleDescription to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._bswModuleDescription = None
            return

        if not isinstance(value, BswModuleDescription):
            raise TypeError(
                f"bswModuleDescription must be BswModuleDescription or None, got {type(value).__name__}"
            )
        self._bswModuleDescription = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBswModuleDescription(self) -> "BswModuleDescription":
        """
        AUTOSAR-compliant getter for bswModuleDescription.
        
        Returns:
            The bswModuleDescription value
        
        Note:
            Delegates to bsw_module_description property (CODING_RULE_V2_00017)
        """
        return self.bsw_module_description  # Delegates to property

    def setBswModuleDescription(self, value: "BswModuleDescription") -> "TDEventBsw":
        """
        AUTOSAR-compliant setter for bswModuleDescription with method chaining.
        
        Args:
            value: The bswModuleDescription to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to bsw_module_description property setter (gets validation automatically)
        """
        self.bsw_module_description = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bsw_module_description(self, value: Optional["BswModuleDescription"]) -> "TDEventBsw":
        """
        Set bswModuleDescription and return self for chaining.
        
        Args:
            value: The bswModuleDescription to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_bsw_module_description("value")
        """
        self.bsw_module_description = value  # Use property setter (gets validation)
        return self