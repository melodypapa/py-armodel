from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class RuleBasedValueSpecification(ARObject):
    """
    This meta-class is used to support a rule-based initialization approach for
    data types with an array-nature (ApplicationArrayDataType and
    ImplementationDataType of category ARRAY) or a compound Application
    PrimitiveDataType (which also boils down to an array-nature).

    Package: M2::AUTOSARTemplates::CommonStructure::Constants

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 331, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 469, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the arguments for the RuleBasedValue atpVariation.
        self._arguments: Optional["RuleArguments"] = None

    @property
    def arguments(self) -> Optional["RuleArguments"]:
        """Get arguments (Pythonic accessor)."""
        return self._arguments

    @arguments.setter
    def arguments(self, value: Optional["RuleArguments"]) -> None:
        """
        Set arguments with validation.

        Args:
            value: The arguments to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._arguments = None
            return

        if not isinstance(value, RuleArguments):
            raise TypeError(
                f"arguments must be RuleArguments or None, got {type(value).__name__}"
            )
        self._arguments = value
        # If a rule is chosen which does not fill until the end, this which size the
        # rule shall fill the values.
        self._maxSizeToFill: Optional["Integer"] = None

    @property
    def max_size_to_fill(self) -> Optional["Integer"]:
        """Get maxSizeToFill (Pythonic accessor)."""
        return self._maxSizeToFill

    @max_size_to_fill.setter
    def max_size_to_fill(self, value: Optional["Integer"]) -> None:
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

        if not isinstance(value, Integer):
            raise TypeError(
                f"maxSizeToFill must be Integer or None, got {type(value).__name__}"
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

    def getArguments(self) -> "RuleArguments":
        """
        AUTOSAR-compliant getter for arguments.

        Returns:
            The arguments value

        Note:
            Delegates to arguments property (CODING_RULE_V2_00017)
        """
        return self.arguments  # Delegates to property

    def setArguments(self, value: "RuleArguments") -> "RuleBasedValueSpecification":
        """
        AUTOSAR-compliant setter for arguments with method chaining.

        Args:
            value: The arguments to set

        Returns:
            self for method chaining

        Note:
            Delegates to arguments property setter (gets validation automatically)
        """
        self.arguments = value  # Delegates to property setter
        return self

    def getMaxSizeToFill(self) -> "Integer":
        """
        AUTOSAR-compliant getter for maxSizeToFill.

        Returns:
            The maxSizeToFill value

        Note:
            Delegates to max_size_to_fill property (CODING_RULE_V2_00017)
        """
        return self.max_size_to_fill  # Delegates to property

    def setMaxSizeToFill(self, value: "Integer") -> "RuleBasedValueSpecification":
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

    def setRule(self, value: "Identifier") -> "RuleBasedValueSpecification":
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

    def with_arguments(self, value: Optional["RuleArguments"]) -> "RuleBasedValueSpecification":
        """
        Set arguments and return self for chaining.

        Args:
            value: The arguments to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_arguments("value")
        """
        self.arguments = value  # Use property setter (gets validation)
        return self

    def with_max_size_to_fill(self, value: Optional["Integer"]) -> "RuleBasedValueSpecification":
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

    def with_rule(self, value: Optional["Identifier"]) -> "RuleBasedValueSpecification":
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
