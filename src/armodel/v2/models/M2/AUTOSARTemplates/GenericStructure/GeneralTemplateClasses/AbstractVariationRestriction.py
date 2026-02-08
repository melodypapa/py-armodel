from abc import ABC
from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class AbstractVariationRestriction(ARObject, ABC):
    """
    Defines constraints on the usage of variation and on the valid binding
    times.

    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ModelRestrictionTypes

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

        if not isinstance(value, Boolean):
            raise TypeError(
                f"variation must be Boolean or None, got {type(value).__name__}"
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
