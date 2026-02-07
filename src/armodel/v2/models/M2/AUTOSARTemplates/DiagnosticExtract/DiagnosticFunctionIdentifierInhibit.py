from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class DiagnosticFunctionIdentifierInhibit(DiagnosticCommonElement):
    """
    This meta-class represents the ability to define the inhibition of a
    specific function identifier within the Fim configuration.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Fim::DiagnosticFunctionIdentifierInhibit
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 215, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the corresponding function identifier.
        self._function: Optional["DiagnosticFunction"] = None

    @property
    def function(self) -> Optional["DiagnosticFunction"]:
        """Get function (Pythonic accessor)."""
        return self._function

    @function.setter
    def function(self, value: Optional["DiagnosticFunction"]) -> None:
        """
        Set function with validation.
        
        Args:
            value: The function to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._function = None
            return

        if not isinstance(value, DiagnosticFunction):
            raise TypeError(
                f"function must be DiagnosticFunction or None, got {type(value).__name__}"
            )
        self._function = value
        # This represents the value of the inhibition mask behavior.
        self._inhibitionMask: Optional["DiagnosticInhibition"] = None

    @property
    def inhibition_mask(self) -> Optional["DiagnosticInhibition"]:
        """Get inhibitionMask (Pythonic accessor)."""
        return self._inhibitionMask

    @inhibition_mask.setter
    def inhibition_mask(self, value: Optional["DiagnosticInhibition"]) -> None:
        """
        Set inhibitionMask with validation.
        
        Args:
            value: The inhibitionMask to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._inhibitionMask = None
            return

        if not isinstance(value, DiagnosticInhibition):
            raise TypeError(
                f"inhibitionMask must be DiagnosticInhibition or None, got {type(value).__name__}"
            )
        self._inhibitionMask = value
        # This represents a collection of DiagnosticFunctionInhibit that contribute to
        # the configuration of the.
        self._inhibitSource: List["DiagnosticFunction"] = []

    @property
    def inhibit_source(self) -> List["DiagnosticFunction"]:
        """Get inhibitSource (Pythonic accessor)."""
        return self._inhibitSource

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFunction(self) -> "DiagnosticFunction":
        """
        AUTOSAR-compliant getter for function.
        
        Returns:
            The function value
        
        Note:
            Delegates to function property (CODING_RULE_V2_00017)
        """
        return self.function  # Delegates to property

    def setFunction(self, value: "DiagnosticFunction") -> "DiagnosticFunctionIdentifierInhibit":
        """
        AUTOSAR-compliant setter for function with method chaining.
        
        Args:
            value: The function to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to function property setter (gets validation automatically)
        """
        self.function = value  # Delegates to property setter
        return self

    def getInhibitionMask(self) -> "DiagnosticInhibition":
        """
        AUTOSAR-compliant getter for inhibitionMask.
        
        Returns:
            The inhibitionMask value
        
        Note:
            Delegates to inhibition_mask property (CODING_RULE_V2_00017)
        """
        return self.inhibition_mask  # Delegates to property

    def setInhibitionMask(self, value: "DiagnosticInhibition") -> "DiagnosticFunctionIdentifierInhibit":
        """
        AUTOSAR-compliant setter for inhibitionMask with method chaining.
        
        Args:
            value: The inhibitionMask to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to inhibition_mask property setter (gets validation automatically)
        """
        self.inhibition_mask = value  # Delegates to property setter
        return self

    def getInhibitSource(self) -> List["DiagnosticFunction"]:
        """
        AUTOSAR-compliant getter for inhibitSource.
        
        Returns:
            The inhibitSource value
        
        Note:
            Delegates to inhibit_source property (CODING_RULE_V2_00017)
        """
        return self.inhibit_source  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_function(self, value: Optional["DiagnosticFunction"]) -> "DiagnosticFunctionIdentifierInhibit":
        """
        Set function and return self for chaining.
        
        Args:
            value: The function to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_function("value")
        """
        self.function = value  # Use property setter (gets validation)
        return self

    def with_inhibition_mask(self, value: Optional["DiagnosticInhibition"]) -> "DiagnosticFunctionIdentifierInhibit":
        """
        Set inhibitionMask and return self for chaining.
        
        Args:
            value: The inhibitionMask to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_inhibition_mask("value")
        """
        self.inhibition_mask = value  # Use property setter (gets validation)
        return self