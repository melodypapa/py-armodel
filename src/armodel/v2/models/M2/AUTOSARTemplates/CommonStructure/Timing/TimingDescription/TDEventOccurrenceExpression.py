from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    AutosarOperation,
    AutosarVariable,
    TDEventOccurrence,
    TimingModeInstance,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class TDEventOccurrenceExpression(ARObject):
    """
    This is used to specify a filter on the occurrences of
    TimingDescriptionEvents by means of a TDEventOccurrenceExpressionFormula.
    Filter criteria can be variable and argument values, i.e. the timing event
    only occurs for specific values, as well as the temporal characteristics of
    the occurrences of arbitrary timing events.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription::TDEventOccurrenceExpression

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 84, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # An occurrence expression can reference an arbitrary of
        # OperationArgumentPrototypes in its association aggregates instance
        # OperationArgumentPrototypes which can in the expression.
        self._argument: List["AutosarOperation"] = []

    @property
    def argument(self) -> List["AutosarOperation"]:
        """Get argument (Pythonic accessor)."""
        return self._argument
        # This is the expression formula which is used to describe occurrence
        # expression.
        self._formula: Optional["TDEventOccurrence"] = None

    @property
    def formula(self) -> Optional["TDEventOccurrence"]:
        """Get formula (Pythonic accessor)."""
        return self._formula

    @formula.setter
    def formula(self, value: Optional["TDEventOccurrence"]) -> None:
        """
        Set formula with validation.

        Args:
            value: The formula to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._formula = None
            return

        if not isinstance(value, TDEventOccurrence):
            raise TypeError(
                f"formula must be TDEventOccurrence or None, got {type(value).__name__}"
            )
        self._formula = value
        # An occurrence expression can reference an arbitrary TimingModeInstances in
                # its expression.
        # This instance references to Mode can be referenced in the expression.
        self._mode: List["TimingModeInstance"] = []

    @property
    def mode(self) -> List["TimingModeInstance"]:
        """Get mode (Pythonic accessor)."""
        return self._mode
        # An occurrence expression can reference an arbitrary of VariableDataPrototypes
                # in its expression.
        # This instance references to Variable can be referenced in the.
        self._variable: List["AutosarVariable"] = []

    @property
    def variable(self) -> List["AutosarVariable"]:
        """Get variable (Pythonic accessor)."""
        return self._variable

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getArgument(self) -> List["AutosarOperation"]:
        """
        AUTOSAR-compliant getter for argument.

        Returns:
            The argument value

        Note:
            Delegates to argument property (CODING_RULE_V2_00017)
        """
        return self.argument  # Delegates to property

    def getFormula(self) -> "TDEventOccurrence":
        """
        AUTOSAR-compliant getter for formula.

        Returns:
            The formula value

        Note:
            Delegates to formula property (CODING_RULE_V2_00017)
        """
        return self.formula  # Delegates to property

    def setFormula(self, value: "TDEventOccurrence") -> "TDEventOccurrenceExpression":
        """
        AUTOSAR-compliant setter for formula with method chaining.

        Args:
            value: The formula to set

        Returns:
            self for method chaining

        Note:
            Delegates to formula property setter (gets validation automatically)
        """
        self.formula = value  # Delegates to property setter
        return self

    def getMode(self) -> List["TimingModeInstance"]:
        """
        AUTOSAR-compliant getter for mode.

        Returns:
            The mode value

        Note:
            Delegates to mode property (CODING_RULE_V2_00017)
        """
        return self.mode  # Delegates to property

    def getVariable(self) -> List["AutosarVariable"]:
        """
        AUTOSAR-compliant getter for variable.

        Returns:
            The variable value

        Note:
            Delegates to variable property (CODING_RULE_V2_00017)
        """
        return self.variable  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_formula(self, value: Optional["TDEventOccurrence"]) -> "TDEventOccurrenceExpression":
        """
        Set formula and return self for chaining.

        Args:
            value: The formula to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_formula("value")
        """
        self.formula = value  # Use property setter (gets validation)
        return self
