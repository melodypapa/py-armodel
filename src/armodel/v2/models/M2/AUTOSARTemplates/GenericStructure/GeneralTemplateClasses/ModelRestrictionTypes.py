"""
AUTOSAR Package - ModelRestrictionTypes

Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ModelRestrictionTypes
"""

from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)


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

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"maxLength must be PositiveInteger or str or None, got {type(value).__name__}"
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

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"minLength must be PositiveInteger or str or None, got {type(value).__name__}"
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

    def with_valid_binding(self, value):
        """
        Set valid_binding and return self for chaining.

        Args:
            value: The valid_binding to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_valid_binding("value")
        """
        self.valid_binding = value  # Use property setter (gets validation)
        return self

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



class AbstractVariationRestriction(ARObject, ABC):
    """
    Defines constraints on the usage of variation and on the valid binding
    times.
    
    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ModelRestrictionTypes::AbstractVariationRestriction
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 104, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 88, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is AbstractVariationRestriction:
            raise TypeError("AbstractVariationRestriction is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # List of valid binding times.
        # xml.
        # sequenceOffset=20.
        self._validBinding: List["FullBindingTimeEnum"] = []

    @property
    def valid_binding(self) -> List["FullBindingTimeEnum"]:
        """Get validBinding (Pythonic accessor)."""
        return self._validBinding
        # Defines if the AUTOSAR model may define a Variation this location.
        self._variation: Optional["Boolean"] = None

    @property
    def variation(self) -> Optional["Boolean"]:
        """Get variation (Pythonic accessor)."""
        return self._variation

    @variation.setter
    def variation(self, value: Optional["Boolean"]) -> None:
        """
        Set variation with validation.
        
        Args:
            value: The variation to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._variation = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"variation must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._variation = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getValidBinding(self) -> List["FullBindingTimeEnum"]:
        """
        AUTOSAR-compliant getter for validBinding.
        
        Returns:
            The validBinding value
        
        Note:
            Delegates to valid_binding property (CODING_RULE_V2_00017)
        """
        return self.valid_binding  # Delegates to property

    def getVariation(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for variation.
        
        Returns:
            The variation value
        
        Note:
            Delegates to variation property (CODING_RULE_V2_00017)
        """
        return self.variation  # Delegates to property

    def setVariation(self, value: "Boolean") -> "AbstractVariationRestriction":
        """
        AUTOSAR-compliant setter for variation with method chaining.
        
        Args:
            value: The variation to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to variation property setter (gets validation automatically)
        """
        self.variation = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_variation(self, value: Optional["Boolean"]) -> "AbstractVariationRestriction":
        """
        Set variation and return self for chaining.
        
        Args:
            value: The variation to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_variation("value")
        """
        self.variation = value  # Use property setter (gets validation)
        return self



class AbstractMultiplicityRestriction(ARObject, ABC):
    """
    Restriction that specifies the valid number of occurrences of an element in
    the current context.
    
    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ModelRestrictionTypes::AbstractMultiplicityRestriction
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 422, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 88, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is AbstractMultiplicityRestriction:
            raise TypeError("AbstractMultiplicityRestriction is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies the minimal number of times an object shall this primitive
        # attribute is not set, then the object.
        self._lowerMultiplicity: Optional["PositiveInteger"] = None

    @property
    def lower_multiplicity(self) -> Optional["PositiveInteger"]:
        """Get lowerMultiplicity (Pythonic accessor)."""
        return self._lowerMultiplicity

    @lower_multiplicity.setter
    def lower_multiplicity(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set lowerMultiplicity with validation.
        
        Args:
            value: The lowerMultiplicity to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._lowerMultiplicity = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"lowerMultiplicity must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._lowerMultiplicity = value
        # This explicitly specifies, that the upper multiplicity is NOT Note: The use
        # of ’upperMultiplicityInfinite’ and mutual exclusive.
        self._upperMultiplicity: Optional["Boolean"] = None

    @property
    def upper_multiplicity(self) -> Optional["Boolean"]:
        """Get upperMultiplicity (Pythonic accessor)."""
        return self._upperMultiplicity

    @upper_multiplicity.setter
    def upper_multiplicity(self, value: Optional["Boolean"]) -> None:
        """
        Set upperMultiplicity with validation.
        
        Args:
            value: The upperMultiplicity to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._upperMultiplicity = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"upperMultiplicity must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._upperMultiplicity = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getLowerMultiplicity(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for lowerMultiplicity.
        
        Returns:
            The lowerMultiplicity value
        
        Note:
            Delegates to lower_multiplicity property (CODING_RULE_V2_00017)
        """
        return self.lower_multiplicity  # Delegates to property

    def setLowerMultiplicity(self, value: "PositiveInteger") -> "AbstractMultiplicityRestriction":
        """
        AUTOSAR-compliant setter for lowerMultiplicity with method chaining.
        
        Args:
            value: The lowerMultiplicity to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to lower_multiplicity property setter (gets validation automatically)
        """
        self.lower_multiplicity = value  # Delegates to property setter
        return self

    def getUpperMultiplicity(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for upperMultiplicity.
        
        Returns:
            The upperMultiplicity value
        
        Note:
            Delegates to upper_multiplicity property (CODING_RULE_V2_00017)
        """
        return self.upper_multiplicity  # Delegates to property

    def setUpperMultiplicity(self, value: "Boolean") -> "AbstractMultiplicityRestriction":
        """
        AUTOSAR-compliant setter for upperMultiplicity with method chaining.
        
        Args:
            value: The upperMultiplicity to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to upper_multiplicity property setter (gets validation automatically)
        """
        self.upper_multiplicity = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_lower_multiplicity(self, value: Optional["PositiveInteger"]) -> "AbstractMultiplicityRestriction":
        """
        Set lowerMultiplicity and return self for chaining.
        
        Args:
            value: The lowerMultiplicity to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_lower_multiplicity("value")
        """
        self.lower_multiplicity = value  # Use property setter (gets validation)
        return self

    def with_upper_multiplicity(self, value: Optional["Boolean"]) -> "AbstractMultiplicityRestriction":
        """
        Set upperMultiplicity and return self for chaining.
        
        Args:
            value: The upperMultiplicity to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_upper_multiplicity("value")
        """
        self.upper_multiplicity = value  # Use property setter (gets validation)
        return self


class FullBindingTimeEnum(AREnum):
    """
    FullBindingTimeEnum enumeration

This enumeration specifies the BindingTimes that can be used in AUTOSAR models. Aggregated by AbstractVariationRestriction.validBindingTime (cid:53) 104 of 535 Document ID 202: AUTOSAR_FO_TPS_GenericStructureTemplate Generic Structure Template AUTOSAR FO R23-11 (cid:52)

Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ModelRestrictionTypes
    """
    # The point in time when an object is created from a blueprint.
    blueprintDerivationTime = "0"

    # • Coding by hand, based on requirements document.
    codeGenerationTime = "2"

    # Configure what is included in object code, and what is omitted Based on which variant(s) are selected
    linkTime = "4"

    # PostBuild is the binding time which is bound latest at startup of the ECU. In other words this is everything between creation of the executable program and startup of the ECU.
    postBuild = "5"

    # This is typically the C-Preprocessor. Exclude parts of the code from the compilation process, e.g., because they are not required for the selected variant, because they are incompatible with the selected variant, because they require resources that are not present in the selected variant. Object code is only generated for the selected variant(s). The code that is excluded at this stage code will not be available at later stages.
    preCompileTime = "3"

    # • Designing the VFB.
    systemDesignTime = "1"
