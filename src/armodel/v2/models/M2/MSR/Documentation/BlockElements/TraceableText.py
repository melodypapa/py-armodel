from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class TraceableText(Paginateable):
    """
    This meta-class represents the ability to denote a traceable text item such
    as requirements etc. The following approach applies: • shortName represents
    the tag for tracing • longName represents the head line • category
    represents the kind of the tagged text (see [constr_2540])
    
    Package: M2::MSR::Documentation::BlockElements::RequirementsTracing::TraceableText
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 178, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 313, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 222, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the text to which the tag applies.
        self._text: "DocumentationBlock" = None

    @property
    def text(self) -> "DocumentationBlock":
        """Get text (Pythonic accessor)."""
        return self._text

    @text.setter
    def text(self, value: "DocumentationBlock") -> None:
        """
        Set text with validation.
        
        Args:
            value: The text to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, DocumentationBlock):
            raise TypeError(
                f"text must be DocumentationBlock, got {type(value).__name__}"
            )
        self._text = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getText(self) -> "DocumentationBlock":
        """
        AUTOSAR-compliant getter for text.
        
        Returns:
            The text value
        
        Note:
            Delegates to text property (CODING_RULE_V2_00017)
        """
        return self.text  # Delegates to property

    def setText(self, value: "DocumentationBlock") -> "TraceableText":
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

    def with_text(self, value: "DocumentationBlock") -> "TraceableText":
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