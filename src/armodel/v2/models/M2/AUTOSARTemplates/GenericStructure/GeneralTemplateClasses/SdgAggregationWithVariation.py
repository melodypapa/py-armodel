from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class SdgAggregationWithVariation(SdgElementWithGid):
    """
    Describes that the Sdg may contain another Sdg. The gid of the nested Sdg is
    defined by subSdg. Represents ’sdg’.
    
    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::SpecialDataDef::SdgAggregationWithVariation
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 101, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Supported sub Sdg Class.
        self._subSdg: Optional["SdgClass"] = None

    @property
    def sub_sdg(self) -> Optional["SdgClass"]:
        """Get subSdg (Pythonic accessor)."""
        return self._subSdg

    @sub_sdg.setter
    def sub_sdg(self, value: Optional["SdgClass"]) -> None:
        """
        Set subSdg with validation.
        
        Args:
            value: The subSdg to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._subSdg = None
            return

        if not isinstance(value, SdgClass):
            raise TypeError(
                f"subSdg must be SdgClass or None, got {type(value).__name__}"
            )
        self._subSdg = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSubSdg(self) -> "SdgClass":
        """
        AUTOSAR-compliant getter for subSdg.
        
        Returns:
            The subSdg value
        
        Note:
            Delegates to sub_sdg property (CODING_RULE_V2_00017)
        """
        return self.sub_sdg  # Delegates to property

    def setSubSdg(self, value: "SdgClass") -> "SdgAggregationWithVariation":
        """
        AUTOSAR-compliant setter for subSdg with method chaining.
        
        Args:
            value: The subSdg to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sub_sdg property setter (gets validation automatically)
        """
        self.sub_sdg = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_sub_sdg(self, value: Optional["SdgClass"]) -> "SdgAggregationWithVariation":
        """
        Set subSdg and return self for chaining.
        
        Args:
            value: The subSdg to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sub_sdg("value")
        """
        self.sub_sdg = value  # Use property setter (gets validation)
        return self