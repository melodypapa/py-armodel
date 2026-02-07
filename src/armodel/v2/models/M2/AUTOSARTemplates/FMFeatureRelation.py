from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class FMFeatureRelation(Identifiable):
    """
    Defines relations for FMFeatures, for example dependencies on other
    FMFeatures, or conflicts with other FMFeatures. A FMFeature can only be part
    of a FMFeatureSelectionSet if all its relations are fulfilled.

    Package: M2::AUTOSARTemplates::FeatureModelTemplate::FMFeatureRelation

    Sources:
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 34, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The FMFeature that is targeted by this FMFeature.
        self._feature: List["FMFeature"] = []

    @property
    def feature(self) -> List["FMFeature"]:
        """Get feature (Pythonic accessor)."""
        return self._feature
        # If given, the condition shall evaluate to true, in order for
        # FMFeatureRelation to be active.
        self._restriction: Optional["FMConditionByFeatures"] = None

    @property
    def restriction(self) -> Optional["FMConditionByFeatures"]:
        """Get restriction (Pythonic accessor)."""
        return self._restriction

    @restriction.setter
    def restriction(self, value: Optional["FMConditionByFeatures"]) -> None:
        """
        Set restriction with validation.

        Args:
            value: The restriction to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._restriction = None
            return

        if not isinstance(value, FMConditionByFeatures):
            raise TypeError(
                f"restriction must be FMConditionByFeatures or None, got {type(value).__name__}"
            )
        self._restriction = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFeature(self) -> List["FMFeature"]:
        """
        AUTOSAR-compliant getter for feature.

        Returns:
            The feature value

        Note:
            Delegates to feature property (CODING_RULE_V2_00017)
        """
        return self.feature  # Delegates to property

    def getRestriction(self) -> "FMConditionByFeatures":
        """
        AUTOSAR-compliant getter for restriction.

        Returns:
            The restriction value

        Note:
            Delegates to restriction property (CODING_RULE_V2_00017)
        """
        return self.restriction  # Delegates to property

    def setRestriction(self, value: "FMConditionByFeatures") -> "FMFeatureRelation":
        """
        AUTOSAR-compliant setter for restriction with method chaining.

        Args:
            value: The restriction to set

        Returns:
            self for method chaining

        Note:
            Delegates to restriction property setter (gets validation automatically)
        """
        self.restriction = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_restriction(self, value: Optional["FMConditionByFeatures"]) -> "FMFeatureRelation":
        """
        Set restriction and return self for chaining.

        Args:
            value: The restriction to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_restriction("value")
        """
        self.restriction = value  # Use property setter (gets validation)
        return self
