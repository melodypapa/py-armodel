from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class LimitValueVariationPoint(ARObject):
    """
    that the xml.name is "LIMIT" for backward compatibility reasons.

    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling::AttributeValueVariationPoints

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 241, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This specifies the type of the interval.
        # If the attribute is interval shall be considered as "CLOSED".
        self._intervalType: Optional["IntervalTypeEnum"] = None

    @property
    def interval_type(self) -> Optional["IntervalTypeEnum"]:
        """Get intervalType (Pythonic accessor)."""
        return self._intervalType

    @interval_type.setter
    def interval_type(self, value: Optional["IntervalTypeEnum"]) -> None:
        """
        Set intervalType with validation.

        Args:
            value: The intervalType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._intervalType = None
            return

        if not isinstance(value, IntervalTypeEnum):
            raise TypeError(
                f"intervalType must be IntervalTypeEnum or None, got {type(value).__name__}"
            )
        self._intervalType = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIntervalType(self) -> "IntervalTypeEnum":
        """
        AUTOSAR-compliant getter for intervalType.

        Returns:
            The intervalType value

        Note:
            Delegates to interval_type property (CODING_RULE_V2_00017)
        """
        return self.interval_type  # Delegates to property

    def setIntervalType(self, value: "IntervalTypeEnum") -> "LimitValueVariationPoint":
        """
        AUTOSAR-compliant setter for intervalType with method chaining.

        Args:
            value: The intervalType to set

        Returns:
            self for method chaining

        Note:
            Delegates to interval_type property setter (gets validation automatically)
        """
        self.interval_type = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_interval_type(self, value: Optional["IntervalTypeEnum"]) -> "LimitValueVariationPoint":
        """
        Set intervalType and return self for chaining.

        Args:
            value: The intervalType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_interval_type("value")
        """
        self.interval_type = value  # Use property setter (gets validation)
        return self
