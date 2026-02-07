from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultilanguageReferrable import MultilanguageReferrable
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Referrable import Referrable

class SdgCaption(MultilanguageReferrable):
    """
    This meta-class represents the caption of a special data group. This allows
    to have some parts of special data as identifiable.
    
    Package: M2::MSR::AsamHdo::SpecialData::SdgCaption
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 91, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents a general but brief (one paragraph) what the special data in
                # question is about.
        # It is paragraph! Desc is intended to be collected into This property helps a
                # human reader to special data in question.
        self._desc: Optional["MultiLanguageOverview"] = None

    @property
    def desc(self) -> Optional["MultiLanguageOverview"]:
        """Get desc (Pythonic accessor)."""
        return self._desc

    @desc.setter
    def desc(self, value: Optional["MultiLanguageOverview"]) -> None:
        """
        Set desc with validation.
        
        Args:
            value: The desc to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._desc = None
            return

        if not isinstance(value, MultiLanguageOverview):
            raise TypeError(
                f"desc must be MultiLanguageOverview or None, got {type(value).__name__}"
            )
        self._desc = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDesc(self) -> "MultiLanguageOverview":
        """
        AUTOSAR-compliant getter for desc.
        
        Returns:
            The desc value
        
        Note:
            Delegates to desc property (CODING_RULE_V2_00017)
        """
        return self.desc  # Delegates to property

    def setDesc(self, value: "MultiLanguageOverview") -> "SdgCaption":
        """
        AUTOSAR-compliant setter for desc with method chaining.
        
        Args:
            value: The desc to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to desc property setter (gets validation automatically)
        """
        self.desc = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_desc(self, value: Optional["MultiLanguageOverview"]) -> "SdgCaption":
        """
        Set desc and return self for chaining.
        
        Args:
            value: The desc to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_desc("value")
        """
        self.desc = value  # Use property setter (gets validation)
        return self