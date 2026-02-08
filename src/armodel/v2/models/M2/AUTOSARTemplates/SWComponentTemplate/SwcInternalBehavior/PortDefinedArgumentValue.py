from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    ImplementationData,
    ValueSpecification,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class PortDefinedArgumentValue(ARObject):
    """
    A PortDefinedArgumentValue is passed to a RunnableEntity dealing with the
    ClientServerOperations provided by a given PortPrototype. Note that this is
    restricted to PPortPrototypes of a ClientServer Interface.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::PortAPIOptions::PortDefinedArgumentValue

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 326, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 593, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 199, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies the actual value.
        self._value: Optional["ValueSpecification"] = None

    @property
    def value(self) -> Optional["ValueSpecification"]:
        """Get value (Pythonic accessor)."""
        return self._value

    @value.setter
    def value(self, value: Optional["ValueSpecification"]) -> None:
        """
        Set value with validation.

        Args:
            value: The value to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._value = None
            return

        if not isinstance(value, ValueSpecification):
            raise TypeError(
                f"value must be ValueSpecification or None, got {type(value).__name__}"
            )
        self._value = value
        # be composite type or a pointer.
        self._valueType: Optional["ImplementationData"] = None

    @property
    def value_type(self) -> Optional["ImplementationData"]:
        """Get valueType (Pythonic accessor)."""
        return self._valueType

    @value_type.setter
    def value_type(self, value: Optional["ImplementationData"]) -> None:
        """
        Set valueType with validation.

        Args:
            value: The valueType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._valueType = None
            return

        if not isinstance(value, ImplementationData):
            raise TypeError(
                f"valueType must be ImplementationData or None, got {type(value).__name__}"
            )
        self._valueType = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getValue(self) -> "ValueSpecification":
        """
        AUTOSAR-compliant getter for value.

        Returns:
            The value value

        Note:
            Delegates to value property (CODING_RULE_V2_00017)
        """
        return self.value  # Delegates to property

    def setValue(self, value: "ValueSpecification") -> "PortDefinedArgumentValue":
        """
        AUTOSAR-compliant setter for value with method chaining.

        Args:
            value: The value to set

        Returns:
            self for method chaining

        Note:
            Delegates to value property setter (gets validation automatically)
        """
        self.value = value  # Delegates to property setter
        return self

    def getValueType(self) -> "ImplementationData":
        """
        AUTOSAR-compliant getter for valueType.

        Returns:
            The valueType value

        Note:
            Delegates to value_type property (CODING_RULE_V2_00017)
        """
        return self.value_type  # Delegates to property

    def setValueType(self, value: "ImplementationData") -> "PortDefinedArgumentValue":
        """
        AUTOSAR-compliant setter for valueType with method chaining.

        Args:
            value: The valueType to set

        Returns:
            self for method chaining

        Note:
            Delegates to value_type property setter (gets validation automatically)
        """
        self.value_type = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_value(self, value: Optional["ValueSpecification"]) -> "PortDefinedArgumentValue":
        """
        Set value and return self for chaining.

        Args:
            value: The value to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_value("value")
        """
        self.value = value  # Use property setter (gets validation)
        return self

    def with_value_type(self, value: Optional["ImplementationData"]) -> "PortDefinedArgumentValue":
        """
        Set valueType and return self for chaining.

        Args:
            value: The valueType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_value_type("value")
        """
        self.value_type = value  # Use property setter (gets validation)
        return self
