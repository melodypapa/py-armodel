from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class AbstractValueRestriction(ARObject, ABC):
    """
    Restricts primitive values. A value is valid if all rules that are defined
    by this restriction evaluate to true.
    
    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ModelRestrictionTypes::AbstractValueRestriction
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 103, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 87, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is AbstractValueRestriction:
            raise TypeError("AbstractValueRestriction is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies the upper bounds for numeric values.
        self._max: Optional["Limit"] = None

    @property
    def max(self) -> Optional["Limit"]:
        """Get max (Pythonic accessor)."""
        return self._max

    @max.setter
    def max(self, value: Optional["Limit"]) -> None:
        """
        Set max with validation.
        
        Args:
            value: The max to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._max = None
            return

        if not isinstance(value, Limit):
            raise TypeError(
                f"max must be Limit or None, got {type(value).__name__}"
            )
        self._max = value
        # Specifies the maximum number of characters of textual.
        self._maxLength: Optional["PositiveInteger"] = None

    @property
    def max_length(self) -> Optional["PositiveInteger"]:
        """Get maxLength (Pythonic accessor)."""
        return self._maxLength

    @max_length.setter
    def max_length(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxLength with validation.
        
        Args:
            value: The maxLength to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxLength = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"maxLength must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._maxLength = value
        # Specifies the lower bounds for numeric values.
        self._min: Optional["Limit"] = None

    @property
    def min(self) -> Optional["Limit"]:
        """Get min (Pythonic accessor)."""
        return self._min

    @min.setter
    def min(self, value: Optional["Limit"]) -> None:
        """
        Set min with validation.
        
        Args:
            value: The min to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._min = None
            return

        if not isinstance(value, Limit):
            raise TypeError(
                f"min must be Limit or None, got {type(value).__name__}"
            )
        self._min = value
        # Specifies the minimal number of characters of textual.
        self._minLength: Optional["PositiveInteger"] = None

    @property
    def min_length(self) -> Optional["PositiveInteger"]:
        """Get minLength (Pythonic accessor)."""
        return self._minLength

    @min_length.setter
    def min_length(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set minLength with validation.
        
        Args:
            value: The minLength to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minLength = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"minLength must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._minLength = value
        # Defines the exact sequence of characters that are.
        self._pattern: Optional["RegularExpression"] = None

    @property
    def pattern(self) -> Optional["RegularExpression"]:
        """Get pattern (Pythonic accessor)."""
        return self._pattern

    @pattern.setter
    def pattern(self, value: Optional["RegularExpression"]) -> None:
        """
        Set pattern with validation.
        
        Args:
            value: The pattern to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pattern = None
            return

        if not isinstance(value, RegularExpression):
            raise TypeError(
                f"pattern must be RegularExpression or None, got {type(value).__name__}"
            )
        self._pattern = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMax(self) -> "Limit":
        """
        AUTOSAR-compliant getter for max.
        
        Returns:
            The max value
        
        Note:
            Delegates to max property (CODING_RULE_V2_00017)
        """
        return self.max  # Delegates to property

    def setMax(self, value: "Limit") -> "AbstractValueRestriction":
        """
        AUTOSAR-compliant setter for max with method chaining.
        
        Args:
            value: The max to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to max property setter (gets validation automatically)
        """
        self.max = value  # Delegates to property setter
        return self

    def getMaxLength(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxLength.
        
        Returns:
            The maxLength value
        
        Note:
            Delegates to max_length property (CODING_RULE_V2_00017)
        """
        return self.max_length  # Delegates to property

    def setMaxLength(self, value: "PositiveInteger") -> "AbstractValueRestriction":
        """
        AUTOSAR-compliant setter for maxLength with method chaining.
        
        Args:
            value: The maxLength to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to max_length property setter (gets validation automatically)
        """
        self.max_length = value  # Delegates to property setter
        return self

    def getMin(self) -> "Limit":
        """
        AUTOSAR-compliant getter for min.
        
        Returns:
            The min value
        
        Note:
            Delegates to min property (CODING_RULE_V2_00017)
        """
        return self.min  # Delegates to property

    def setMin(self, value: "Limit") -> "AbstractValueRestriction":
        """
        AUTOSAR-compliant setter for min with method chaining.
        
        Args:
            value: The min to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to min property setter (gets validation automatically)
        """
        self.min = value  # Delegates to property setter
        return self

    def getMinLength(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for minLength.
        
        Returns:
            The minLength value
        
        Note:
            Delegates to min_length property (CODING_RULE_V2_00017)
        """
        return self.min_length  # Delegates to property

    def setMinLength(self, value: "PositiveInteger") -> "AbstractValueRestriction":
        """
        AUTOSAR-compliant setter for minLength with method chaining.
        
        Args:
            value: The minLength to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to min_length property setter (gets validation automatically)
        """
        self.min_length = value  # Delegates to property setter
        return self

    def getPattern(self) -> "RegularExpression":
        """
        AUTOSAR-compliant getter for pattern.
        
        Returns:
            The pattern value
        
        Note:
            Delegates to pattern property (CODING_RULE_V2_00017)
        """
        return self.pattern  # Delegates to property

    def setPattern(self, value: "RegularExpression") -> "AbstractValueRestriction":
        """
        AUTOSAR-compliant setter for pattern with method chaining.
        
        Args:
            value: The pattern to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to pattern property setter (gets validation automatically)
        """
        self.pattern = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_max(self, value: Optional["Limit"]) -> "AbstractValueRestriction":
        """
        Set max and return self for chaining.
        
        Args:
            value: The max to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_max("value")
        """
        self.max = value  # Use property setter (gets validation)
        return self

    def with_max_length(self, value: Optional["PositiveInteger"]) -> "AbstractValueRestriction":
        """
        Set maxLength and return self for chaining.
        
        Args:
            value: The maxLength to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_max_length("value")
        """
        self.max_length = value  # Use property setter (gets validation)
        return self

    def with_min(self, value: Optional["Limit"]) -> "AbstractValueRestriction":
        """
        Set min and return self for chaining.
        
        Args:
            value: The min to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_min("value")
        """
        self.min = value  # Use property setter (gets validation)
        return self

    def with_min_length(self, value: Optional["PositiveInteger"]) -> "AbstractValueRestriction":
        """
        Set minLength and return self for chaining.
        
        Args:
            value: The minLength to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_min_length("value")
        """
        self.min_length = value  # Use property setter (gets validation)
        return self

    def with_pattern(self, value: Optional["RegularExpression"]) -> "AbstractValueRestriction":
        """
        Set pattern and return self for chaining.
        
        Args:
            value: The pattern to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_pattern("value")
        """
        self.pattern = value  # Use property setter (gets validation)
        return self