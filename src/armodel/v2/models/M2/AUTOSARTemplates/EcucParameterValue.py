from abc import ABC
from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    Annotation,
    EcucIndexableValue,
    EcucParameterDef,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class EcucParameterValue(EcucIndexableValue, ABC):
    """
    Common class to all types of configuration values.

    Package: M2::AUTOSARTemplates::ECUCDescriptionTemplate::EcucParameterValue

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 124, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 442, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 189, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is EcucParameterValue:
            raise TypeError("EcucParameterValue is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Possibility to provide additional notes while defining the Parameter Values.
        # These are not documentation but are mere design notes.
        # its sub-classes 318 Document ID 87: AUTOSAR_CP_TPS_ECUConfiguration ECU
                # Configuration R23-11.
        self._annotation: List["Annotation"] = []

    @property
    def annotation(self) -> List["Annotation"]:
        """Get annotation (Pythonic accessor)."""
        return self._annotation
        # Reference to the definition of this EcucParameterValue the ECU Configuration
        # Parameter.
        self._definition: Optional["EcucParameterDef"] = None

    @property
    def definition(self) -> Optional["EcucParameterDef"]:
        """Get definition (Pythonic accessor)."""
        return self._definition

    @definition.setter
    def definition(self, value: Optional["EcucParameterDef"]) -> None:
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

        if not isinstance(value, EcucParameterDef):
            raise TypeError(
                f"definition must be EcucParameterDef or None, got {type(value).__name__}"
            )
        self._definition = value
        # If withAuto is set to "true" for this parameter definition the be set to
                # "true".
        # If isAutoValue is set to actual value will not be considered during ECU will
                # be (re-)calculated by the code stored in the value attribute afterwards.
        # updated values might require a other modules which reference these is not
                # present the default is "false".
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

    def getDefinition(self) -> "EcucParameterDef":
        """
        AUTOSAR-compliant getter for definition.

        Returns:
            The definition value

        Note:
            Delegates to definition property (CODING_RULE_V2_00017)
        """
        return self.definition  # Delegates to property

    def setDefinition(self, value: "EcucParameterDef") -> "EcucParameterValue":
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

    def setIsAutoValue(self, value: "Boolean") -> "EcucParameterValue":
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

    def with_definition(self, value: Optional["EcucParameterDef"]) -> "EcucParameterValue":
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

    def with_is_auto_value(self, value: Optional["Boolean"]) -> "EcucParameterValue":
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
