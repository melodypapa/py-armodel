from abc import ABC
from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    Annotation,
    EcucIndexableValue,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    RefType,
)


class EcucAbstractReferenceValue(EcucIndexableValue, ABC):
    """
    Abstract class to be used as common parent for all reference values in the
    ECU Configuration Description.

    Package: M2::AUTOSARTemplates::ECUCDescriptionTemplate::EcucAbstractReferenceValue

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 131, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is EcucAbstractReferenceValue:
            raise TypeError("EcucAbstractReferenceValue is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Possibility to provide additional notes while defining a (e.
        # g.
        # the ECU Configuration Parameter are not intended as documentation but design
                # notes.
        self._annotation: List["Annotation"] = []

    @property
    def annotation(self) -> List["Annotation"]:
        """Get annotation (Pythonic accessor)."""
        return self._annotation
        # Reference to the definition of this EcucAbstractReference subclasses in the
        # ECU Configuration Parameter.
        self._definition: RefType = None

    @property
    def definition(self) -> RefType:
        """Get definition (Pythonic accessor)."""
        return self._definition

    @definition.setter
    def definition(self, value: RefType) -> None:
        """
        Set definition with validation.

        Args:
            value: The definition to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._definition = None
            return

        self._definition = value
        # If withAuto is set to "true" for this parameter definition the be set to
                # "true".
        # is set to "true" the actual value will not be ECU Configuration but will be
                # the code generator and stored in the afterwards.
        # These implicit updated values a re-generation of other modules which values.
        # is not present the default is "false".
        self._isAutoValue: Optional["Boolean"] = None

    @property
    def is_auto_value(self) -> Optional["Boolean"]:
        """Get isAutoValue (Pythonic accessor)."""
        return self._isAutoValue

    @is_auto_value.setter
    def is_auto_value(self, value: Optional["Boolean"]) -> None:
        """
        Set isAutoValue with validation.

        Args:
            value: The isAutoValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._isAutoValue = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"isAutoValue must be Boolean or None, got {type(value).__name__}"
            )
        self._isAutoValue = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAnnotation(self) -> List["Annotation"]:
        """
        AUTOSAR-compliant getter for annotation.

        Returns:
            The annotation value

        Note:
            Delegates to annotation property (CODING_RULE_V2_00017)
        """
        return self.annotation  # Delegates to property

    def getDefinition(self) -> RefType:
        """
        AUTOSAR-compliant getter for definition.

        Returns:
            The definition value

        Note:
            Delegates to definition property (CODING_RULE_V2_00017)
        """
        return self.definition  # Delegates to property

    def setDefinition(self, value: RefType) -> "EcucAbstractReferenceValue":
        """
        AUTOSAR-compliant setter for definition with method chaining.

        Args:
            value: The definition to set

        Returns:
            self for method chaining

        Note:
            Delegates to definition property setter (gets validation automatically)
        """
        self.definition = value  # Delegates to property setter
        return self

    def getIsAutoValue(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for isAutoValue.

        Returns:
            The isAutoValue value

        Note:
            Delegates to is_auto_value property (CODING_RULE_V2_00017)
        """
        return self.is_auto_value  # Delegates to property

    def setIsAutoValue(self, value: "Boolean") -> "EcucAbstractReferenceValue":
        """
        AUTOSAR-compliant setter for isAutoValue with method chaining.

        Args:
            value: The isAutoValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to is_auto_value property setter (gets validation automatically)
        """
        self.is_auto_value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_definition(self, value: Optional[RefType]) -> "EcucAbstractReferenceValue":
        """
        Set definition and return self for chaining.

        Args:
            value: The definition to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_definition("value")
        """
        self.definition = value  # Use property setter (gets validation)
        return self

    def with_is_auto_value(self, value: Optional["Boolean"]) -> "EcucAbstractReferenceValue":
        """
        Set isAutoValue and return self for chaining.

        Args:
            value: The isAutoValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_is_auto_value("value")
        """
        self.is_auto_value = value  # Use property setter (gets validation)
        return self
