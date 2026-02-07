from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class LLongName(ARObject):
    """
    MixedContentForLongNames in one particular language. The language is denoted
    in the attribute l.
    
    Package: M2::MSR::Documentation::TextModel::LanguageDataModel::LLongName
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 179, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 62, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents a description that documents how the be defined when deriving
        # objects from the.
        self._blueprintValue: Optional["String"] = None

    @property
    def blueprint_value(self) -> Optional["String"]:
        """Get blueprintValue (Pythonic accessor)."""
        return self._blueprintValue

    @blueprint_value.setter
    def blueprint_value(self, value: Optional["String"]) -> None:
        """
        Set blueprintValue with validation.
        
        Args:
            value: The blueprintValue to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._blueprintValue = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"blueprintValue must be String or None, got {type(value).__name__}"
            )
        self._blueprintValue = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBlueprintValue(self) -> "String":
        """
        AUTOSAR-compliant getter for blueprintValue.
        
        Returns:
            The blueprintValue value
        
        Note:
            Delegates to blueprint_value property (CODING_RULE_V2_00017)
        """
        return self.blueprint_value  # Delegates to property

    def setBlueprintValue(self, value: "String") -> "LLongName":
        """
        AUTOSAR-compliant setter for blueprintValue with method chaining.
        
        Args:
            value: The blueprintValue to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to blueprint_value property setter (gets validation automatically)
        """
        self.blueprint_value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_blueprint_value(self, value: Optional["String"]) -> "LLongName":
        """
        Set blueprintValue and return self for chaining.
        
        Args:
            value: The blueprintValue to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_blueprint_value("value")
        """
        self.blueprint_value = value  # Use property setter (gets validation)
        return self