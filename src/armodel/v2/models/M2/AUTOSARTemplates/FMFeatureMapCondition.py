from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import FMConditionByFeatures
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class FMFeatureMapCondition(Identifiable):
    """
    Defines a condition which needs to be fulfilled for this mapping to become
    active. The condition is implemented as formula that is based on features
    and attributes and is defined by fmCond.

    Package: M2::AUTOSARTemplates::FeatureModelTemplate::FMFeatureMapCondition

    Sources:
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 55, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The formula that implements the condition.
        self._fmCondAndAttributes: Optional["FMConditionByFeatures"] = None

    @property
    def fm_cond_and_attributes(self) -> Optional["FMConditionByFeatures"]:
        """Get fmCondAndAttributes (Pythonic accessor)."""
        return self._fmCondAndAttributes

    @fm_cond_and_attributes.setter
    def fm_cond_and_attributes(self, value: Optional["FMConditionByFeatures"]) -> None:
        """
        Set fmCondAndAttributes with validation.

        Args:
            value: The fmCondAndAttributes to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._fmCondAndAttributes = None
            return

        if not isinstance(value, FMConditionByFeatures):
            raise TypeError(
                f"fmCondAndAttributes must be FMConditionByFeatures or None, got {type(value).__name__}"
            )
        self._fmCondAndAttributes = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFmCondAndAttributes(self) -> "FMConditionByFeatures":
        """
        AUTOSAR-compliant getter for fmCondAndAttributes.

        Returns:
            The fmCondAndAttributes value

        Note:
            Delegates to fm_cond_and_attributes property (CODING_RULE_V2_00017)
        """
        return self.fm_cond_and_attributes  # Delegates to property

    def setFmCondAndAttributes(self, value: "FMConditionByFeatures") -> "FMFeatureMapCondition":
        """
        AUTOSAR-compliant setter for fmCondAndAttributes with method chaining.

        Args:
            value: The fmCondAndAttributes to set

        Returns:
            self for method chaining

        Note:
            Delegates to fm_cond_and_attributes property setter (gets validation automatically)
        """
        self.fm_cond_and_attributes = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_fm_cond_and_attributes(self, value: Optional["FMConditionByFeatures"]) -> "FMFeatureMapCondition":
        """
        Set fmCondAndAttributes and return self for chaining.

        Args:
            value: The fmCondAndAttributes to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_fm_cond_and_attributes("value")
        """
        self.fm_cond_and_attributes = value  # Use property setter (gets validation)
        return self
