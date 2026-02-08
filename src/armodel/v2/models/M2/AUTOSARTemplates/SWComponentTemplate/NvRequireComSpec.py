from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import RPortComSpec

    RefType,
)


class NvRequireComSpec(RPortComSpec):
    """
    Communication attributes of RPortPrototypes with respect to Nv data
    communication on the required side.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication::NvRequireComSpec

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 194, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The initial value owned by the NvComSpec.
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
        # The VariableDataPrototype the ComSpec applies for.
        self._variable: RefType = None

    @property
    def variable(self) -> RefType:
        """Get variable (Pythonic accessor)."""
        return self._variable

    @variable.setter
    def variable(self, value: RefType) -> None:
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

        self._variable = value

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

    def setInitValue(self, value: "ValueSpecification") -> "NvRequireComSpec":
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

    def getVariable(self) -> RefType:
        """
        AUTOSAR-compliant getter for variable.

        Returns:
            The variable value

        Note:
            Delegates to variable property (CODING_RULE_V2_00017)
        """
        return self.variable  # Delegates to property

    def setVariable(self, value: RefType) -> "NvRequireComSpec":
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

    def with_init_value(self, value: Optional["ValueSpecification"]) -> "NvRequireComSpec":
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

    def with_variable(self, value: Optional[RefType]) -> "NvRequireComSpec":
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
