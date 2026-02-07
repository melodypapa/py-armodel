from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class EnumerationMappingEntry(ARObject):
    """
    that this class might be used in the extended meta-model only.
    
    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling::AttributeValueVariationPoints::EnumerationMappingEntry
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 443, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute specifies the symbolic value (e.
        # g.
        # in, out) of enumeration entry.
        self._enumerator: "NameToken" = None

    @property
    def enumerator(self) -> "NameToken":
        """Get enumerator (Pythonic accessor)."""
        return self._enumerator

    @enumerator.setter
    def enumerator(self, value: "NameToken") -> None:
        """
        Set enumerator with validation.
        
        Args:
            value: The enumerator to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, NameToken):
            raise TypeError(
                f"enumerator must be NameToken, got {type(value).__name__}"
            )
        self._enumerator = value
        # This attribute specifies the numerical value (e.
        # g.
        # 0, 1) of entry.
        # The numericalValue marks an M2 level.
        # It is not used in C-Code or at runtime.
        # is only given to be able to calculate a represents the enumerator literal in
                # a numerical.
        self._numericalValue: "PositiveInteger" = None

    @property
    def numerical_value(self) -> "PositiveInteger":
        """Get numericalValue (Pythonic accessor)."""
        return self._numericalValue

    @numerical_value.setter
    def numerical_value(self, value: "PositiveInteger") -> None:
        """
        Set numericalValue with validation.
        
        Args:
            value: The numericalValue to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"numericalValue must be PositiveInteger, got {type(value).__name__}"
            )
        self._numericalValue = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEnumerator(self) -> "NameToken":
        """
        AUTOSAR-compliant getter for enumerator.
        
        Returns:
            The enumerator value
        
        Note:
            Delegates to enumerator property (CODING_RULE_V2_00017)
        """
        return self.enumerator  # Delegates to property

    def setEnumerator(self, value: "NameToken") -> "EnumerationMappingEntry":
        """
        AUTOSAR-compliant setter for enumerator with method chaining.
        
        Args:
            value: The enumerator to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to enumerator property setter (gets validation automatically)
        """
        self.enumerator = value  # Delegates to property setter
        return self

    def getNumericalValue(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for numericalValue.
        
        Returns:
            The numericalValue value
        
        Note:
            Delegates to numerical_value property (CODING_RULE_V2_00017)
        """
        return self.numerical_value  # Delegates to property

    def setNumericalValue(self, value: "PositiveInteger") -> "EnumerationMappingEntry":
        """
        AUTOSAR-compliant setter for numericalValue with method chaining.
        
        Args:
            value: The numericalValue to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to numerical_value property setter (gets validation automatically)
        """
        self.numerical_value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_enumerator(self, value: "NameToken") -> "EnumerationMappingEntry":
        """
        Set enumerator and return self for chaining.
        
        Args:
            value: The enumerator to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_enumerator("value")
        """
        self.enumerator = value  # Use property setter (gets validation)
        return self

    def with_numerical_value(self, value: "PositiveInteger") -> "EnumerationMappingEntry":
        """
        Set numericalValue and return self for chaining.
        
        Args:
            value: The numericalValue to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_numerical_value("value")
        """
        self.numerical_value = value  # Use property setter (gets validation)
        return self