from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class EcucContainerValue(Identifiable):
    """
    Represents a Container definition in the ECU Configuration Description.

    Package: M2::AUTOSARTemplates::ECUCDescriptionTemplate

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 119, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2021, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 439, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 185, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the definition of this Container in the ECU Definition.
        self._definition: Optional["EcucContainerDef"] = None

    @property
    def definition(self) -> Optional["EcucContainerDef"]:
        """Get definition (Pythonic accessor)."""
        return self._definition

    @definition.setter
    def definition(self, value: Optional["EcucContainerDef"]) -> None:
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

        if not isinstance(value, EcucContainerDef):
            raise TypeError(
                f"definition must be EcucContainerDef or None, got {type(value).__name__}"
            )
        self._definition = value
        # Aggregates all ECU Configuration Values within this atpVariation.
        self._parameterValue: List["EcucParameterValue"] = []

    @property
    def parameter_value(self) -> List["EcucParameterValue"]:
        """Get parameterValue (Pythonic accessor)."""
        return self._parameterValue
        # Aggregates all References with this container.
        # [RS_ECUC_00079] atpVariation.
        self._referenceValue: List[RefType] = []

    @property
    def reference_value(self) -> List[RefType]:
        """Get referenceValue (Pythonic accessor)."""
        return self._referenceValue
        # Aggregates all sub-containers within this container.
        # atpVariation.
        self._subContainer: List["EcucContainerValue"] = []

    @property
    def sub_container(self) -> List["EcucContainerValue"]:
        """Get subContainer (Pythonic accessor)."""
        return self._subContainer

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDefinition(self) -> "EcucContainerDef":
        """
        AUTOSAR-compliant getter for definition.

        Returns:
            The definition value

        Note:
            Delegates to definition property (CODING_RULE_V2_00017)
        """
        return self.definition  # Delegates to property

    def setDefinition(self, value: "EcucContainerDef") -> "EcucContainerValue":
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

    def getParameterValue(self) -> List["EcucParameterValue"]:
        """
        AUTOSAR-compliant getter for parameterValue.

        Returns:
            The parameterValue value

        Note:
            Delegates to parameter_value property (CODING_RULE_V2_00017)
        """
        return self.parameter_value  # Delegates to property

    def getReferenceValue(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for referenceValue.

        Returns:
            The referenceValue value

        Note:
            Delegates to reference_value property (CODING_RULE_V2_00017)
        """
        return self.reference_value  # Delegates to property

    def getSubContainer(self) -> List["EcucContainerValue"]:
        """
        AUTOSAR-compliant getter for subContainer.

        Returns:
            The subContainer value

        Note:
            Delegates to sub_container property (CODING_RULE_V2_00017)
        """
        return self.sub_container  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_definition(self, value: Optional["EcucContainerDef"]) -> "EcucContainerValue":
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
