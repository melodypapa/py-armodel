from typing import List

from armodel.v2.models.M2.AUTOSARTemplates import (
    Annotation,
    Integer,
    PostBuildVariant,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class PostBuildVariantCriterionValue(ARObject):
    """
    This class specifies the value which shall be assigned to a particular
    variant criterion in order to bind the variation point. If multiple
    criterion/value pairs are specified, they all shall match to bind the
    variation point.

    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling::PostBuildVariantCriterionValue

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 305, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 77, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 258, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This provides the ability to add information why the value like it is.
        self._annotation: List["Annotation"] = []

    @property
    def annotation(self) -> List["Annotation"]:
        """Get annotation (Pythonic accessor)."""
        return self._annotation
        # This is the particular value of the post-build variant.
        self._value: "Integer" = None

    @property
    def value(self) -> "Integer":
        """Get value (Pythonic accessor)."""
        return self._value

    @value.setter
    def value(self, value: "Integer") -> None:
        """
        Set value with validation.

        Args:
            value: The value to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, Integer):
            raise TypeError(
                f"value must be Integer, got {type(value).__name__}"
            )
        self._value = value
        # This association selects the variant criterion whose value specified.
        self._variantCriterion: "PostBuildVariant" = None

    @property
    def variant_criterion(self) -> "PostBuildVariant":
        """Get variantCriterion (Pythonic accessor)."""
        return self._variantCriterion

    @variant_criterion.setter
    def variant_criterion(self, value: "PostBuildVariant") -> None:
        """
        Set variantCriterion with validation.

        Args:
            value: The variantCriterion to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, PostBuildVariant):
            raise TypeError(
                f"variantCriterion must be PostBuildVariant, got {type(value).__name__}"
            )
        self._variantCriterion = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAnnotation(self) -> List["Annotation"]:
        """
        AUTOSAR-compliant getter for annotation.

        Returns:
            The annotation value

        Note:
            Delegates to annotation property (CODING_RULE_V2_00017)
        """
        return self.annotation  # Delegates to property

    def getValue(self) -> "Integer":
        """
        AUTOSAR-compliant getter for value.

        Returns:
            The value value

        Note:
            Delegates to value property (CODING_RULE_V2_00017)
        """
        return self.value  # Delegates to property

    def setValue(self, value: "Integer") -> "PostBuildVariantCriterionValue":
        """
        AUTOSAR-compliant setter for value with method chaining.

        Args:
            value: The value to set

        Returns:
            self for method chaining

        Note:
            Delegates to value property setter (gets validation automatically)
        """
        self.value = value  # Delegates to property setter
        return self

    def getVariantCriterion(self) -> "PostBuildVariant":
        """
        AUTOSAR-compliant getter for variantCriterion.

        Returns:
            The variantCriterion value

        Note:
            Delegates to variant_criterion property (CODING_RULE_V2_00017)
        """
        return self.variant_criterion  # Delegates to property

    def setVariantCriterion(self, value: "PostBuildVariant") -> "PostBuildVariantCriterionValue":
        """
        AUTOSAR-compliant setter for variantCriterion with method chaining.

        Args:
            value: The variantCriterion to set

        Returns:
            self for method chaining

        Note:
            Delegates to variant_criterion property setter (gets validation automatically)
        """
        self.variant_criterion = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_value(self, value: "Integer") -> "PostBuildVariantCriterionValue":
        """
        Set value and return self for chaining.

        Args:
            value: The value to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_value("value")
        """
        self.value = value  # Use property setter (gets validation)
        return self

    def with_variant_criterion(self, value: "PostBuildVariant") -> "PostBuildVariantCriterionValue":
        """
        Set variantCriterion and return self for chaining.

        Args:
            value: The variantCriterion to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_variant_criterion("value")
        """
        self.variant_criterion = value  # Use property setter (gets validation)
        return self
