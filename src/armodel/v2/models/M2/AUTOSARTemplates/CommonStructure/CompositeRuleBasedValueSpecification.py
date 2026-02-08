from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    AbstractRuleBasedValueSpecification,
    CompositeRuleBased,
    CompositeValue,
    Identifier,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class CompositeRuleBasedValueSpecification(AbstractRuleBasedValueSpecification):
    """
    This meta-class represents rule-based values for DataPrototypes typed by
    composite AutosarDataTypes.

    Package: M2::AUTOSARTemplates::CommonStructure::Constants::CompositeRuleBasedValueSpecification

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 471, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the collection of aggregated Value Specifications.
        # The last ValueSpecification in the be taken to execute the filling rule.
        self._argument: List["CompositeValue"] = []

    @property
    def argument(self) -> List["CompositeValue"]:
        """Get argument (Pythonic accessor)."""
        return self._argument
        # This represents the collection of aggregated Value in the collection shall be
        # taken to the filling rule.
        self._compound: List["CompositeRuleBased"] = []

    @property
    def compound(self) -> List["CompositeRuleBased"]:
        """Get compound (Pythonic accessor)."""
        return self._compound
        # If a rule is chosen which does not fill until the end, this which size the
        # rule shall fill the values.
        self._maxSizeToFill: Optional["PositiveInteger"] = None

    @property
    def max_size_to_fill(self) -> Optional["PositiveInteger"]:
        """Get maxSizeToFill (Pythonic accessor)."""
        return self._maxSizeToFill

    @max_size_to_fill.setter
    def max_size_to_fill(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxSizeToFill with validation.

        Args:
            value: The maxSizeToFill to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxSizeToFill = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"maxSizeToFill must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._maxSizeToFill = value
        # This denotes the name of the rule of the RuleBasedValue rule determines the
        # calculation which the arguments are used to values.
        self._rule: Optional["Identifier"] = None

    @property
    def rule(self) -> Optional["Identifier"]:
        """Get rule (Pythonic accessor)."""
        return self._rule

    @rule.setter
    def rule(self, value: Optional["Identifier"]) -> None:
        """
        Set rule with validation.

        Args:
            value: The rule to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rule = None
            return

        if not isinstance(value, Identifier):
            raise TypeError(
                f"rule must be Identifier or None, got {type(value).__name__}"
            )
        self._rule = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getArgument(self) -> List["CompositeValue"]:
        """
        AUTOSAR-compliant getter for argument.

        Returns:
            The argument value

        Note:
            Delegates to argument property (CODING_RULE_V2_00017)
        """
        return self.argument  # Delegates to property

    def getCompound(self) -> List["CompositeRuleBased"]:
        """
        AUTOSAR-compliant getter for compound.

        Returns:
            The compound value

        Note:
            Delegates to compound property (CODING_RULE_V2_00017)
        """
        return self.compound  # Delegates to property

    def getMaxSizeToFill(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxSizeToFill.

        Returns:
            The maxSizeToFill value

        Note:
            Delegates to max_size_to_fill property (CODING_RULE_V2_00017)
        """
        return self.max_size_to_fill  # Delegates to property

    def setMaxSizeToFill(self, value: "PositiveInteger") -> "CompositeRuleBasedValueSpecification":
        """
        AUTOSAR-compliant setter for maxSizeToFill with method chaining.

        Args:
            value: The maxSizeToFill to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_size_to_fill property setter (gets validation automatically)
        """
        self.max_size_to_fill = value  # Delegates to property setter
        return self

    def getRule(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for rule.

        Returns:
            The rule value

        Note:
            Delegates to rule property (CODING_RULE_V2_00017)
        """
        return self.rule  # Delegates to property

    def setRule(self, value: "Identifier") -> "CompositeRuleBasedValueSpecification":
        """
        AUTOSAR-compliant setter for rule with method chaining.

        Args:
            value: The rule to set

        Returns:
            self for method chaining

        Note:
            Delegates to rule property setter (gets validation automatically)
        """
        self.rule = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_max_size_to_fill(self, value: Optional["PositiveInteger"]) -> "CompositeRuleBasedValueSpecification":
        """
        Set maxSizeToFill and return self for chaining.

        Args:
            value: The maxSizeToFill to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_size_to_fill("value")
        """
        self.max_size_to_fill = value  # Use property setter (gets validation)
        return self

    def with_rule(self, value: Optional["Identifier"]) -> "CompositeRuleBasedValueSpecification":
        """
        Set rule and return self for chaining.

        Args:
            value: The rule to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rule("value")
        """
        self.rule = value  # Use property setter (gets validation)
        return self
