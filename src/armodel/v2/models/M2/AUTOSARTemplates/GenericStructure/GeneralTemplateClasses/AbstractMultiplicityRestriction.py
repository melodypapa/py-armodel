from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class AbstractMultiplicityRestriction(ARObject, ABC):
    """
    Restriction that specifies the valid number of occurrences of an element in
    the current context.

    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ModelRestrictionTypes

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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"lowerMultiplicity must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._lowerMultiplicity = value
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

        if not isinstance(value, Boolean):
            raise TypeError(
                f"upperMultiplicity must be Boolean or None, got {type(value).__name__}"
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
