from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class MultilanguageLongName(ARObject):
    """
    This meta-class represents the ability to specify a long name which acts in
    the role of a headline. It is intended for human readers. Per language it
    should be around max 80 characters.
    
    Package: M2::MSR::Documentation::TextModel::MultilanguageData::MultilanguageLongName
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 179, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 163, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 62, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        self._l4: "LLongName" = None

    @property
    def l4(self) -> "LLongName":
        """Get l4 (Pythonic accessor)."""
        return self._l4

    @l4.setter
    def l4(self, value: "LLongName") -> None:
        """
        Set l4 with validation.
        
        Args:
            value: The l4 to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, LLongName):
            raise TypeError(
                f"l4 must be LLongName, got {type(value).__name__}"
            )
        self._l4 = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getL4(self) -> "LLongName":
        """
        AUTOSAR-compliant getter for l4.
        
        Returns:
            The l4 value
        
        Note:
            Delegates to l4 property (CODING_RULE_V2_00017)
        """
        return self.l4  # Delegates to property

    def setL4(self, value: "LLongName") -> "MultilanguageLongName":
        """
        AUTOSAR-compliant setter for l4 with method chaining.
        
        Args:
            value: The l4 to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to l4 property setter (gets validation automatically)
        """
        self.l4 = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_l4(self, value: "LLongName") -> "MultilanguageLongName":
        """
        Set l4 and return self for chaining.
        
        Args:
            value: The l4 to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_l4("value")
        """
        self.l4 = value  # Use property setter (gets validation)
        return self