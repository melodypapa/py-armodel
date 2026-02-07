from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class SdgTailoring(RestrictionWithSeverity):
    """
    Describes if the referenced Sdg may be attached to the current class.
    
    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Data::SdgTailoring
    
    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 118, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specification of the structure of the Special Data Group.
        self._sdgClass: Optional["SdgClass"] = None

    @property
    def sdg_class(self) -> Optional["SdgClass"]:
        """Get sdgClass (Pythonic accessor)."""
        return self._sdgClass

    @sdg_class.setter
    def sdg_class(self, value: Optional["SdgClass"]) -> None:
        """
        Set sdgClass with validation.
        
        Args:
            value: The sdgClass to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sdgClass = None
            return

        if not isinstance(value, SdgClass):
            raise TypeError(
                f"sdgClass must be SdgClass or None, got {type(value).__name__}"
            )
        self._sdgClass = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSdgClass(self) -> "SdgClass":
        """
        AUTOSAR-compliant getter for sdgClass.
        
        Returns:
            The sdgClass value
        
        Note:
            Delegates to sdg_class property (CODING_RULE_V2_00017)
        """
        return self.sdg_class  # Delegates to property

    def setSdgClass(self, value: "SdgClass") -> "SdgTailoring":
        """
        AUTOSAR-compliant setter for sdgClass with method chaining.
        
        Args:
            value: The sdgClass to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sdg_class property setter (gets validation automatically)
        """
        self.sdg_class = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_sdg_class(self, value: Optional["SdgClass"]) -> "SdgTailoring":
        """
        Set sdgClass and return self for chaining.
        
        Args:
            value: The sdgClass to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sdg_class("value")
        """
        self.sdg_class = value  # Use property setter (gets validation)
        return self