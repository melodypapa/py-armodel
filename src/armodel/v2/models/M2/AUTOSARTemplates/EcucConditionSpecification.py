from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class EcucConditionSpecification(ARObject):
    """
    Allows to define existence dependencies based on the value of parameter
    values.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 100, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Definition of the formula used to define existence.
        self._condition: Optional["EcucConditionFormula"] = None

    @property
    def condition(self) -> Optional["EcucConditionFormula"]:
        """Get condition (Pythonic accessor)."""
        return self._condition

    @condition.setter
    def condition(self, value: Optional["EcucConditionFormula"]) -> None:
        """
        Set condition with validation.

        Args:
            value: The condition to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._condition = None
            return

        if not isinstance(value, EcucConditionFormula):
            raise TypeError(
                f"condition must be EcucConditionFormula or None, got {type(value).__name__}"
            )
        self._condition = value
        # Query to the ECU Configuration Description.
        self._ecucQuery: List["EcucQuery"] = []

    @property
    def ecuc_query(self) -> List["EcucQuery"]:
        """Get ecucQuery (Pythonic accessor)."""
        return self._ecucQuery
        # Informal description of the condition used to to define.
        self._informalFormula: Optional["MlFormula"] = None

    @property
    def informal_formula(self) -> Optional["MlFormula"]:
        """Get informalFormula (Pythonic accessor)."""
        return self._informalFormula

    @informal_formula.setter
    def informal_formula(self, value: Optional["MlFormula"]) -> None:
        """
        Set informalFormula with validation.

        Args:
            value: The informalFormula to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._informalFormula = None
            return

        if not isinstance(value, MlFormula):
            raise TypeError(
                f"informalFormula must be MlFormula or None, got {type(value).__name__}"
            )
        self._informalFormula = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCondition(self) -> "EcucConditionFormula":
        """
        AUTOSAR-compliant getter for condition.

        Returns:
            The condition value

        Note:
            Delegates to condition property (CODING_RULE_V2_00017)
        """
        return self.condition  # Delegates to property

    def setCondition(self, value: "EcucConditionFormula") -> "EcucConditionSpecification":
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

    def getEcucQuery(self) -> List["EcucQuery"]:
        """
        AUTOSAR-compliant getter for ecucQuery.

        Returns:
            The ecucQuery value

        Note:
            Delegates to ecuc_query property (CODING_RULE_V2_00017)
        """
        return self.ecuc_query  # Delegates to property

    def getInformalFormula(self) -> "MlFormula":
        """
        AUTOSAR-compliant getter for informalFormula.

        Returns:
            The informalFormula value

        Note:
            Delegates to informal_formula property (CODING_RULE_V2_00017)
        """
        return self.informal_formula  # Delegates to property

    def setInformalFormula(self, value: "MlFormula") -> "EcucConditionSpecification":
        """
        AUTOSAR-compliant setter for informalFormula with method chaining.

        Args:
            value: The informalFormula to set

        Returns:
            self for method chaining

        Note:
            Delegates to informal_formula property setter (gets validation automatically)
        """
        self.informal_formula = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_condition(self, value: Optional["EcucConditionFormula"]) -> "EcucConditionSpecification":
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

    def with_informal_formula(self, value: Optional["MlFormula"]) -> "EcucConditionSpecification":
        """
        Set informalFormula and return self for chaining.

        Args:
            value: The informalFormula to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_informal_formula("value")
        """
        self.informal_formula = value  # Use property setter (gets validation)
        return self
