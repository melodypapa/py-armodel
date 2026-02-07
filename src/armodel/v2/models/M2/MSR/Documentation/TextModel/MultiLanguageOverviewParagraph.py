from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class MultiLanguageOverviewParagraph(ARObject):
    """
    This is the content of a multilingual paragraph in an overview item.
    
    Package: M2::MSR::Documentation::TextModel::MultilanguageData::MultiLanguageOverviewParagraph
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 53, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 389, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 347, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 65, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        self._l2: "LOverviewParagraph" = None

    @property
    def l2(self) -> "LOverviewParagraph":
        """Get l2 (Pythonic accessor)."""
        return self._l2

    @l2.setter
    def l2(self, value: "LOverviewParagraph") -> None:
        """
        Set l2 with validation.
        
        Args:
            value: The l2 to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, LOverviewParagraph):
            raise TypeError(
                f"l2 must be LOverviewParagraph, got {type(value).__name__}"
            )
        self._l2 = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getL2(self) -> "LOverviewParagraph":
        """
        AUTOSAR-compliant getter for l2.
        
        Returns:
            The l2 value
        
        Note:
            Delegates to l2 property (CODING_RULE_V2_00017)
        """
        return self.l2  # Delegates to property

    def setL2(self, value: "LOverviewParagraph") -> "MultiLanguageOverviewParagraph":
        """
        AUTOSAR-compliant setter for l2 with method chaining.
        
        Args:
            value: The l2 to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to l2 property setter (gets validation automatically)
        """
        self.l2 = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_l2(self, value: "LOverviewParagraph") -> "MultiLanguageOverviewParagraph":
        """
        Set l2 and return self for chaining.
        
        Args:
            value: The l2 to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_l2("value")
        """
        self.l2 = value  # Use property setter (gets validation)
        return self