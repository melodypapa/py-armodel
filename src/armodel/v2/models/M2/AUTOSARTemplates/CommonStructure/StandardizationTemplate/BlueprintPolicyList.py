from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class BlueprintPolicyList(BlueprintPolicy):
    """
    The class represents that the related attribute is modifiable during the
    blueprinting. It applies only to attribute with upper multiplicity greater
    than 1.
    
    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::AbstractBlueprintStructure::BlueprintPolicyList
    
    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 164, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Maximum number of elements in list.
        # If the maximum is not constraint it shall be set to "undefined".
        self._maxNumberOf: "PositiveInteger" = None

    @property
    def max_number_of(self) -> "PositiveInteger":
        """Get maxNumberOf (Pythonic accessor)."""
        return self._maxNumberOf

    @max_number_of.setter
    def max_number_of(self, value: "PositiveInteger") -> None:
        """
        Set maxNumberOf with validation.
        
        Args:
            value: The maxNumberOf to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"maxNumberOf must be PositiveInteger, got {type(value).__name__}"
            )
        self._maxNumberOf = value
        # Minimum number of elements in the list.
        # If the minimum is not constraint it shall be set to "undefined".
        self._minNumberOf: "PositiveInteger" = None

    @property
    def min_number_of(self) -> "PositiveInteger":
        """Get minNumberOf (Pythonic accessor)."""
        return self._minNumberOf

    @min_number_of.setter
    def min_number_of(self, value: "PositiveInteger") -> None:
        """
        Set minNumberOf with validation.
        
        Args:
            value: The minNumberOf to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"minNumberOf must be PositiveInteger, got {type(value).__name__}"
            )
        self._minNumberOf = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMaxNumberOf(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxNumberOf.
        
        Returns:
            The maxNumberOf value
        
        Note:
            Delegates to max_number_of property (CODING_RULE_V2_00017)
        """
        return self.max_number_of  # Delegates to property

    def setMaxNumberOf(self, value: "PositiveInteger") -> "BlueprintPolicyList":
        """
        AUTOSAR-compliant setter for maxNumberOf with method chaining.
        
        Args:
            value: The maxNumberOf to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to max_number_of property setter (gets validation automatically)
        """
        self.max_number_of = value  # Delegates to property setter
        return self

    def getMinNumberOf(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for minNumberOf.
        
        Returns:
            The minNumberOf value
        
        Note:
            Delegates to min_number_of property (CODING_RULE_V2_00017)
        """
        return self.min_number_of  # Delegates to property

    def setMinNumberOf(self, value: "PositiveInteger") -> "BlueprintPolicyList":
        """
        AUTOSAR-compliant setter for minNumberOf with method chaining.
        
        Args:
            value: The minNumberOf to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to min_number_of property setter (gets validation automatically)
        """
        self.min_number_of = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_max_number_of(self, value: "PositiveInteger") -> "BlueprintPolicyList":
        """
        Set maxNumberOf and return self for chaining.
        
        Args:
            value: The maxNumberOf to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_max_number_of("value")
        """
        self.max_number_of = value  # Use property setter (gets validation)
        return self

    def with_min_number_of(self, value: "PositiveInteger") -> "BlueprintPolicyList":
        """
        Set minNumberOf and return self for chaining.
        
        Args:
            value: The minNumberOf to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_min_number_of("value")
        """
        self.min_number_of = value  # Use property setter (gets validation)
        return self