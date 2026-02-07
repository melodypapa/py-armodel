from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class BlueprintFormula(ARObject):
    """
    This class express the extension of the Formula Language to provide
    formalized blueprint-Value resp. blueprintCondition.
    
    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::BlueprintFormula::BlueprintFormula
    
    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 163, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The EcucDefinitionElement serves as a argument for the.
        self._ecuc: "EcucDefinitionElement" = None

    @property
    def ecuc(self) -> "EcucDefinitionElement":
        """Get ecuc (Pythonic accessor)."""
        return self._ecuc

    @ecuc.setter
    def ecuc(self, value: "EcucDefinitionElement") -> None:
        """
        Set ecuc with validation.
        
        Args:
            value: The ecuc to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, EcucDefinitionElement):
            raise TypeError(
                f"ecuc must be EcucDefinitionElement, got {type(value).__name__}"
            )
        self._ecuc = value
        # This represents an informal term in the expression as Note that the result of
        # this is same as "undefined".
        self._verbatim: "MultiLanguageVerbatim" = None

    @property
    def verbatim(self) -> "MultiLanguageVerbatim":
        """Get verbatim (Pythonic accessor)."""
        return self._verbatim

    @verbatim.setter
    def verbatim(self, value: "MultiLanguageVerbatim") -> None:
        """
        Set verbatim with validation.
        
        Args:
            value: The verbatim to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, MultiLanguageVerbatim):
            raise TypeError(
                f"verbatim must be MultiLanguageVerbatim, got {type(value).__name__}"
            )
        self._verbatim = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEcuc(self) -> "EcucDefinitionElement":
        """
        AUTOSAR-compliant getter for ecuc.
        
        Returns:
            The ecuc value
        
        Note:
            Delegates to ecuc property (CODING_RULE_V2_00017)
        """
        return self.ecuc  # Delegates to property

    def setEcuc(self, value: "EcucDefinitionElement") -> "BlueprintFormula":
        """
        AUTOSAR-compliant setter for ecuc with method chaining.
        
        Args:
            value: The ecuc to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to ecuc property setter (gets validation automatically)
        """
        self.ecuc = value  # Delegates to property setter
        return self

    def getVerbatim(self) -> "MultiLanguageVerbatim":
        """
        AUTOSAR-compliant getter for verbatim.
        
        Returns:
            The verbatim value
        
        Note:
            Delegates to verbatim property (CODING_RULE_V2_00017)
        """
        return self.verbatim  # Delegates to property

    def setVerbatim(self, value: "MultiLanguageVerbatim") -> "BlueprintFormula":
        """
        AUTOSAR-compliant setter for verbatim with method chaining.
        
        Args:
            value: The verbatim to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to verbatim property setter (gets validation automatically)
        """
        self.verbatim = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ecuc(self, value: "EcucDefinitionElement") -> "BlueprintFormula":
        """
        Set ecuc and return self for chaining.
        
        Args:
            value: The ecuc to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_ecuc("value")
        """
        self.ecuc = value  # Use property setter (gets validation)
        return self

    def with_verbatim(self, value: "MultiLanguageVerbatim") -> "BlueprintFormula":
        """
        Set verbatim and return self for chaining.
        
        Args:
            value: The verbatim to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_verbatim("value")
        """
        self.verbatim = value  # Use property setter (gets validation)
        return self