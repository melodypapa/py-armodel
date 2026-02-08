from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class FMFeatureRestriction(Identifiable):
    """
    Defines restrictions for FMFeatures. A FMFeature can only be part of a
    FMFeatureSelectionSet if at least one of its restrictions evaluate to true.

    Package: M2::AUTOSARTemplates::FeatureModelTemplate::FMFeatureRestriction

    Sources:
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 32, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # A formula that contains the actual restriction.
        self._restrictionAndAttributes: Optional["FMConditionByFeatures"] = None

    @property
    def restriction_and_attributes(self) -> Optional["FMConditionByFeatures"]:
        """Get restrictionAndAttributes (Pythonic accessor)."""
        return self._restrictionAndAttributes

    @restriction_and_attributes.setter
    def restriction_and_attributes(self, value: Optional["FMConditionByFeatures"]) -> None:
        """
        Set restrictionAndAttributes with validation.

        Args:
            value: The restrictionAndAttributes to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._restrictionAndAttributes = None
            return

        if not isinstance(value, FMConditionByFeatures):
            raise TypeError(
                f"restrictionAndAttributes must be FMConditionByFeatures or None, got {type(value).__name__}"
            )
        self._restrictionAndAttributes = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRestrictionAndAttributes(self) -> "FMConditionByFeatures":
        """
        AUTOSAR-compliant getter for restrictionAndAttributes.

        Returns:
            The restrictionAndAttributes value

        Note:
            Delegates to restriction_and_attributes property (CODING_RULE_V2_00017)
        """
        return self.restriction_and_attributes  # Delegates to property

    def setRestrictionAndAttributes(self, value: "FMConditionByFeatures") -> "FMFeatureRestriction":
        """
        AUTOSAR-compliant setter for restrictionAndAttributes with method chaining.

        Args:
            value: The restrictionAndAttributes to set

        Returns:
            self for method chaining

        Note:
            Delegates to restriction_and_attributes property setter (gets validation automatically)
        """
        self.restriction_and_attributes = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_restriction_and_attributes(self, value: Optional["FMConditionByFeatures"]) -> "FMFeatureRestriction":
        """
        Set restrictionAndAttributes and return self for chaining.

        Args:
            value: The restrictionAndAttributes to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_restriction_and_attributes("value")
        """
        self.restriction_and_attributes = value  # Use property setter (gets validation)
        return self
