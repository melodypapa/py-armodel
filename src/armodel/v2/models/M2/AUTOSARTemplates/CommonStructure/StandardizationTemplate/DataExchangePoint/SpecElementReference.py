from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class SpecElementReference(Identifiable, ABC):
    """
    This is a reference to a specification element in the Autosar standard.
    
    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Common::SpecElementReference
    
    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 82, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is SpecElementReference:
            raise TypeError("SpecElementReference is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Alternative name of a specification element if its name fit into the
                # shortName.
        # E.
        # g.
        # because the name.
        self._alternative: Optional["String"] = None

    @property
    def alternative(self) -> Optional["String"]:
        """Get alternative (Pythonic accessor)."""
        return self._alternative

    @alternative.setter
    def alternative(self, value: Optional["String"]) -> None:
        """
        Set alternative with validation.
        
        Args:
            value: The alternative to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._alternative = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"alternative must be String or None, got {type(value).__name__}"
            )
        self._alternative = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAlternative(self) -> "String":
        """
        AUTOSAR-compliant getter for alternative.
        
        Returns:
            The alternative value
        
        Note:
            Delegates to alternative property (CODING_RULE_V2_00017)
        """
        return self.alternative  # Delegates to property

    def setAlternative(self, value: "String") -> "SpecElementReference":
        """
        AUTOSAR-compliant setter for alternative with method chaining.
        
        Args:
            value: The alternative to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to alternative property setter (gets validation automatically)
        """
        self.alternative = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_alternative(self, value: Optional["String"]) -> "SpecElementReference":
        """
        Set alternative and return self for chaining.
        
        Args:
            value: The alternative to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_alternative("value")
        """
        self.alternative = value  # Use property setter (gets validation)
        return self