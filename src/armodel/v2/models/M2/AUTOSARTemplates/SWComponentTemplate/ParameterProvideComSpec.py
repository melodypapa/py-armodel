from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import (
    PPortComSpec,
)


class ParameterProvideComSpec(PPortComSpec):
    """
    "Communication" specification that applies to parameters on the provided
    side of a connection.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 192, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The initial value applicable for the corresponding.
        self._initValue: Optional["ValueSpecification"] = None

    @property
    def init_value(self) -> Optional["ValueSpecification"]:
        """Get initValue (Pythonic accessor)."""
        return self._initValue

    @init_value.setter
    def init_value(self, value: Optional["ValueSpecification"]) -> None:
        """
        Set initValue with validation.

        Args:
            value: The initValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._initValue = None
            return

        if not isinstance(value, ValueSpecification):
            raise TypeError(
                f"initValue must be ValueSpecification or None, got {type(value).__name__}"
            )
        self._initValue = value
        # The ParameterDataPrototype to which the Parameter applies.
        self._parameter: Optional["ParameterData"] = None

    @property
    def parameter(self) -> Optional["ParameterData"]:
        """Get parameter (Pythonic accessor)."""
        return self._parameter

    @parameter.setter
    def parameter(self, value: Optional["ParameterData"]) -> None:
        """
        Set parameter with validation.

        Args:
            value: The parameter to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._parameter = None
            return

        if not isinstance(value, ParameterData):
            raise TypeError(
                f"parameter must be ParameterData or None, got {type(value).__name__}"
            )
        self._parameter = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getInitValue(self) -> "ValueSpecification":
        """
        AUTOSAR-compliant getter for initValue.

        Returns:
            The initValue value

        Note:
            Delegates to init_value property (CODING_RULE_V2_00017)
        """
        return self.init_value  # Delegates to property

    def setInitValue(self, value: "ValueSpecification") -> "ParameterProvideComSpec":
        """
        AUTOSAR-compliant setter for initValue with method chaining.

        Args:
            value: The initValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to init_value property setter (gets validation automatically)
        """
        self.init_value = value  # Delegates to property setter
        return self

    def getParameter(self) -> "ParameterData":
        """
        AUTOSAR-compliant getter for parameter.

        Returns:
            The parameter value

        Note:
            Delegates to parameter property (CODING_RULE_V2_00017)
        """
        return self.parameter  # Delegates to property

    def setParameter(self, value: "ParameterData") -> "ParameterProvideComSpec":
        """
        AUTOSAR-compliant setter for parameter with method chaining.

        Args:
            value: The parameter to set

        Returns:
            self for method chaining

        Note:
            Delegates to parameter property setter (gets validation automatically)
        """
        self.parameter = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_init_value(self, value: Optional["ValueSpecification"]) -> "ParameterProvideComSpec":
        """
        Set initValue and return self for chaining.

        Args:
            value: The initValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_init_value("value")
        """
        self.init_value = value  # Use property setter (gets validation)
        return self

    def with_parameter(self, value: Optional["ParameterData"]) -> "ParameterProvideComSpec":
        """
        Set parameter and return self for chaining.

        Args:
            value: The parameter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_parameter("value")
        """
        self.parameter = value  # Use property setter (gets validation)
        return self
