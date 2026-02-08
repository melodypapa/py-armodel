from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Constants import AbstractRuleBasedValueSpecification


class NumericalRuleBasedValueSpecification(AbstractRuleBasedValueSpecification):
    """
    This meta-class is used to support a rule-based initialization approach for
    data types with an array-nature (ImplementationDataType of category ARRAY).

    Package: M2::AUTOSARTemplates::CommonStructure::Constants::NumericalRuleBasedValueSpecification

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 467, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the rule based value specification for the array.
        self._ruleBased: Optional["RuleBasedValue"] = None

    @property
    def rule_based(self) -> Optional["RuleBasedValue"]:
        """Get ruleBased (Pythonic accessor)."""
        return self._ruleBased

    @rule_based.setter
    def rule_based(self, value: Optional["RuleBasedValue"]) -> None:
        """
        Set ruleBased with validation.

        Args:
            value: The ruleBased to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ruleBased = None
            return

        if not isinstance(value, RuleBasedValue):
            raise TypeError(
                f"ruleBased must be RuleBasedValue or None, got {type(value).__name__}"
            )
        self._ruleBased = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRuleBased(self) -> "RuleBasedValue":
        """
        AUTOSAR-compliant getter for ruleBased.

        Returns:
            The ruleBased value

        Note:
            Delegates to rule_based property (CODING_RULE_V2_00017)
        """
        return self.rule_based  # Delegates to property

    def setRuleBased(self, value: "RuleBasedValue") -> "NumericalRuleBasedValueSpecification":
        """
        AUTOSAR-compliant setter for ruleBased with method chaining.

        Args:
            value: The ruleBased to set

        Returns:
            self for method chaining

        Note:
            Delegates to rule_based property setter (gets validation automatically)
        """
        self.rule_based = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_rule_based(self, value: Optional["RuleBasedValue"]) -> "NumericalRuleBasedValueSpecification":
        """
        Set ruleBased and return self for chaining.

        Args:
            value: The ruleBased to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rule_based("value")
        """
        self.rule_based = value  # Use property setter (gets validation)
        return self
