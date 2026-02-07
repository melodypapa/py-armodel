from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class TDEventOccurrenceExpressionFormula(ARObject):
    """
    This is an extension of the FormulaExpression for the AUTOSAR Timing
    Extensions. A TDEventOccurrenceExpressionFormula provides the means to
    express the temporal characteristics of timing event occurrences in
    correlation with specific variable and argument values. The formal
    definition of the extended functions (ExtUnaryFunctions) is described in
    detail in the AUTOSAR Timing Extensions.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription::TDEventOccurrenceExpressionFormula

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 84, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is one particular argument value used in the formula.
        self._argument: Optional["AutosarOperation"] = None

    @property
    def argument(self) -> Optional["AutosarOperation"]:
        """Get argument (Pythonic accessor)."""
        return self._argument

    @argument.setter
    def argument(self, value: Optional["AutosarOperation"]) -> None:
        """
        Set argument with validation.

        Args:
            value: The argument to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._argument = None
            return

        if not isinstance(value, AutosarOperation):
            raise TypeError(
                f"argument must be AutosarOperation or None, got {type(value).__name__}"
            )
        self._argument = value
        # This is one particular timing description event used in the.
        self._event: Optional["TimingDescriptionEvent"] = None

    @property
    def event(self) -> Optional["TimingDescriptionEvent"]:
        """Get event (Pythonic accessor)."""
        return self._event

    @event.setter
    def event(self, value: Optional["TimingDescriptionEvent"]) -> None:
        """
        Set event with validation.

        Args:
            value: The event to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._event = None
            return

        if not isinstance(value, TimingDescriptionEvent):
            raise TypeError(
                f"event must be TimingDescriptionEvent or None, got {type(value).__name__}"
            )
        self._event = value
        # This is one particular mode used in the expression.
        self._mode: Optional["TimingModeInstance"] = None

    @property
    def mode(self) -> Optional["TimingModeInstance"]:
        """Get mode (Pythonic accessor)."""
        return self._mode

    @mode.setter
    def mode(self, value: Optional["TimingModeInstance"]) -> None:
        """
        Set mode with validation.

        Args:
            value: The mode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mode = None
            return

        if not isinstance(value, TimingModeInstance):
            raise TypeError(
                f"mode must be TimingModeInstance or None, got {type(value).__name__}"
            )
        self._mode = value
        # This is one particular variable value used in the formula.
        self._variable: Optional["AutosarVariable"] = None

    @property
    def variable(self) -> Optional["AutosarVariable"]:
        """Get variable (Pythonic accessor)."""
        return self._variable

    @variable.setter
    def variable(self, value: Optional["AutosarVariable"]) -> None:
        """
        Set variable with validation.

        Args:
            value: The variable to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._variable = None
            return

        if not isinstance(value, AutosarVariable):
            raise TypeError(
                f"variable must be AutosarVariable or None, got {type(value).__name__}"
            )
        self._variable = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getArgument(self) -> "AutosarOperation":
        """
        AUTOSAR-compliant getter for argument.

        Returns:
            The argument value

        Note:
            Delegates to argument property (CODING_RULE_V2_00017)
        """
        return self.argument  # Delegates to property

    def setArgument(self, value: "AutosarOperation") -> "TDEventOccurrenceExpressionFormula":
        """
        AUTOSAR-compliant setter for argument with method chaining.

        Args:
            value: The argument to set

        Returns:
            self for method chaining

        Note:
            Delegates to argument property setter (gets validation automatically)
        """
        self.argument = value  # Delegates to property setter
        return self

    def getEvent(self) -> "TimingDescriptionEvent":
        """
        AUTOSAR-compliant getter for event.

        Returns:
            The event value

        Note:
            Delegates to event property (CODING_RULE_V2_00017)
        """
        return self.event  # Delegates to property

    def setEvent(self, value: "TimingDescriptionEvent") -> "TDEventOccurrenceExpressionFormula":
        """
        AUTOSAR-compliant setter for event with method chaining.

        Args:
            value: The event to set

        Returns:
            self for method chaining

        Note:
            Delegates to event property setter (gets validation automatically)
        """
        self.event = value  # Delegates to property setter
        return self

    def getMode(self) -> "TimingModeInstance":
        """
        AUTOSAR-compliant getter for mode.

        Returns:
            The mode value

        Note:
            Delegates to mode property (CODING_RULE_V2_00017)
        """
        return self.mode  # Delegates to property

    def setMode(self, value: "TimingModeInstance") -> "TDEventOccurrenceExpressionFormula":
        """
        AUTOSAR-compliant setter for mode with method chaining.

        Args:
            value: The mode to set

        Returns:
            self for method chaining

        Note:
            Delegates to mode property setter (gets validation automatically)
        """
        self.mode = value  # Delegates to property setter
        return self

    def getVariable(self) -> "AutosarVariable":
        """
        AUTOSAR-compliant getter for variable.

        Returns:
            The variable value

        Note:
            Delegates to variable property (CODING_RULE_V2_00017)
        """
        return self.variable  # Delegates to property

    def setVariable(self, value: "AutosarVariable") -> "TDEventOccurrenceExpressionFormula":
        """
        AUTOSAR-compliant setter for variable with method chaining.

        Args:
            value: The variable to set

        Returns:
            self for method chaining

        Note:
            Delegates to variable property setter (gets validation automatically)
        """
        self.variable = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_argument(self, value: Optional["AutosarOperation"]) -> "TDEventOccurrenceExpressionFormula":
        """
        Set argument and return self for chaining.

        Args:
            value: The argument to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_argument("value")
        """
        self.argument = value  # Use property setter (gets validation)
        return self

    def with_event(self, value: Optional["TimingDescriptionEvent"]) -> "TDEventOccurrenceExpressionFormula":
        """
        Set event and return self for chaining.

        Args:
            value: The event to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_event("value")
        """
        self.event = value  # Use property setter (gets validation)
        return self

    def with_mode(self, value: Optional["TimingModeInstance"]) -> "TDEventOccurrenceExpressionFormula":
        """
        Set mode and return self for chaining.

        Args:
            value: The mode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mode("value")
        """
        self.mode = value  # Use property setter (gets validation)
        return self

    def with_variable(self, value: Optional["AutosarVariable"]) -> "TDEventOccurrenceExpressionFormula":
        """
        Set variable and return self for chaining.

        Args:
            value: The variable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_variable("value")
        """
        self.variable = value  # Use property setter (gets validation)
        return self
