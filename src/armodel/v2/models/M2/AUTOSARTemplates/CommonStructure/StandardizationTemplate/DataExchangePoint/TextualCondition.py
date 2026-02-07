from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class TextualCondition(AbstractCondition):
    """
    Specifies additional conditions for one or more model elements. The
    condition is described using human language.
    
    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Data::TextualCondition
    
    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 105, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Human language description of the condition.
        self._text: "String" = None

    @property
    def text(self) -> "String":
        """Get text (Pythonic accessor)."""
        return self._text

    @text.setter
    def text(self, value: "String") -> None:
        """
        Set text with validation.
        
        Args:
            value: The text to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, String):
            raise TypeError(
                f"text must be String, got {type(value).__name__}"
            )
        self._text = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getText(self) -> "String":
        """
        AUTOSAR-compliant getter for text.
        
        Returns:
            The text value
        
        Note:
            Delegates to text property (CODING_RULE_V2_00017)
        """
        return self.text  # Delegates to property

    def setText(self, value: "String") -> "TextualCondition":
        """
        AUTOSAR-compliant setter for text with method chaining.
        
        Args:
            value: The text to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to text property setter (gets validation automatically)
        """
        self.text = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_text(self, value: "String") -> "TextualCondition":
        """
        Set text and return self for chaining.
        
        Args:
            value: The text to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_text("value")
        """
        self.text = value  # Use property setter (gets validation)
        return self