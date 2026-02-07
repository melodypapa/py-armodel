from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class PostBuildVariantCriterion(ARElement):
    """
    This class specifies one particular PostBuildVariantSelector.
    
    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling::PostBuildVariantCriterion
    
    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 304, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 614, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 76, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 232, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The compuMethod specifies the possible values for the serving as an
        # enumerator.
        self._compuMethod: "CompuMethod" = None

    @property
    def compu_method(self) -> "CompuMethod":
        """Get compuMethod (Pythonic accessor)."""
        return self._compuMethod

    @compu_method.setter
    def compu_method(self, value: "CompuMethod") -> None:
        """
        Set compuMethod with validation.
        
        Args:
            value: The compuMethod to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, CompuMethod):
            raise TypeError(
                f"compuMethod must be CompuMethod, got {type(value).__name__}"
            )
        self._compuMethod = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCompuMethod(self) -> "CompuMethod":
        """
        AUTOSAR-compliant getter for compuMethod.
        
        Returns:
            The compuMethod value
        
        Note:
            Delegates to compu_method property (CODING_RULE_V2_00017)
        """
        return self.compu_method  # Delegates to property

    def setCompuMethod(self, value: "CompuMethod") -> "PostBuildVariantCriterion":
        """
        AUTOSAR-compliant setter for compuMethod with method chaining.
        
        Args:
            value: The compuMethod to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to compu_method property setter (gets validation automatically)
        """
        self.compu_method = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_compu_method(self, value: "CompuMethod") -> "PostBuildVariantCriterion":
        """
        Set compuMethod and return self for chaining.
        
        Args:
            value: The compuMethod to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_compu_method("value")
        """
        self.compu_method = value  # Use property setter (gets validation)
        return self