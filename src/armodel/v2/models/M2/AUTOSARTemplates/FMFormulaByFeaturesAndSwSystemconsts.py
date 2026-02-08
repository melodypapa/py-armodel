from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class FMFormulaByFeaturesAndSwSystemconsts(ARObject, ABC):
    """
    An expression that has the syntax of the AUTOSAR formula language and may
    use references to features or system constants as operands.

    Package: M2::AUTOSARTemplates::FeatureModelTemplate

    Sources:
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 63, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is FMFormulaByFeaturesAndSwSystemconsts:
            raise TypeError("FMFormulaByFeaturesAndSwSystemconsts is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # An expression of type FMFormulaByFeaturesAndSw refer to FMFeatures.
        self._feature: Optional["FMFeature"] = None

    @property
    def feature(self) -> Optional["FMFeature"]:
        """Get feature (Pythonic accessor)."""
        return self._feature

    @feature.setter
    def feature(self, value: Optional["FMFeature"]) -> None:
        """
        Set feature with validation.

        Args:
            value: The feature to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._feature = None
            return

        if not isinstance(value, FMFeature):
            raise TypeError(
                f"feature must be FMFeature or None, got {type(value).__name__}"
            )
        self._feature = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFeature(self) -> "FMFeature":
        """
        AUTOSAR-compliant getter for feature.

        Returns:
            The feature value

        Note:
            Delegates to feature property (CODING_RULE_V2_00017)
        """
        return self.feature  # Delegates to property

    def setFeature(self, value: "FMFeature") -> "FMFormulaByFeaturesAndSwSystemconsts":
        """
        AUTOSAR-compliant setter for feature with method chaining.

        Args:
            value: The feature to set

        Returns:
            self for method chaining

        Note:
            Delegates to feature property setter (gets validation automatically)
        """
        self.feature = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_feature(self, value: Optional["FMFeature"]) -> "FMFormulaByFeaturesAndSwSystemconsts":
        """
        Set feature and return self for chaining.

        Args:
            value: The feature to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_feature("value")
        """
        self.feature = value  # Use property setter (gets validation)
        return self
