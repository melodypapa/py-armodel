from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data import (
    AttributeCondition,
)


class AggregationCondition(AttributeCondition):
    """
    The AggregationCondition evaluates to true, if the referenced aggregation is
    accepted by all rules of this condition.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Data

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 102, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The aggregation that has to be accepted by the this AggregationCondition.
        self._aggregation: "AggregationTailoring" = None

    @property
    def aggregation(self) -> "AggregationTailoring":
        """Get aggregation (Pythonic accessor)."""
        return self._aggregation

    @aggregation.setter
    def aggregation(self, value: "AggregationTailoring") -> None:
        """
        Set aggregation with validation.

        Args:
            value: The aggregation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, AggregationTailoring):
            raise TypeError(
                f"aggregation must be AggregationTailoring, got {type(value).__name__}"
            )
        self._aggregation = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAggregation(self) -> "AggregationTailoring":
        """
        AUTOSAR-compliant getter for aggregation.

        Returns:
            The aggregation value

        Note:
            Delegates to aggregation property (CODING_RULE_V2_00017)
        """
        return self.aggregation  # Delegates to property

    def setAggregation(self, value: "AggregationTailoring") -> "AggregationCondition":
        """
        AUTOSAR-compliant setter for aggregation with method chaining.

        Args:
            value: The aggregation to set

        Returns:
            self for method chaining

        Note:
            Delegates to aggregation property setter (gets validation automatically)
        """
        self.aggregation = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_aggregation(self, value: "AggregationTailoring") -> "AggregationCondition":
        """
        Set aggregation and return self for chaining.

        Args:
            value: The aggregation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_aggregation("value")
        """
        self.aggregation = value  # Use property setter (gets validation)
        return self
