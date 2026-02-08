from armodel.v2.models.M2.AUTOSARTemplates import AbstractCondition


class InvertCondition(AbstractCondition):
    """
    inverts the nested condition

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Data::InvertCondition

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 104, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The inverted condition.
        self._condition: "AbstractCondition" = None

    @property
    def condition(self) -> "AbstractCondition":
        """Get condition (Pythonic accessor)."""
        return self._condition

    @condition.setter
    def condition(self, value: "AbstractCondition") -> None:
        """
        Set condition with validation.

        Args:
            value: The condition to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, AbstractCondition):
            raise TypeError(
                f"condition must be AbstractCondition, got {type(value).__name__}"
            )
        self._condition = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCondition(self) -> "AbstractCondition":
        """
        AUTOSAR-compliant getter for condition.

        Returns:
            The condition value

        Note:
            Delegates to condition property (CODING_RULE_V2_00017)
        """
        return self.condition  # Delegates to property

    def setCondition(self, value: "AbstractCondition") -> "InvertCondition":
        """
        AUTOSAR-compliant setter for condition with method chaining.

        Args:
            value: The condition to set

        Returns:
            self for method chaining

        Note:
            Delegates to condition property setter (gets validation automatically)
        """
        self.condition = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_condition(self, value: "AbstractCondition") -> "InvertCondition":
        """
        Set condition and return self for chaining.

        Args:
            value: The condition to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_condition("value")
        """
        self.condition = value  # Use property setter (gets validation)
        return self
