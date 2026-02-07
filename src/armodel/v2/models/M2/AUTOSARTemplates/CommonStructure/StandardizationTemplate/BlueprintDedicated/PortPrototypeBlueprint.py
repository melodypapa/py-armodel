"""
This module defines classes for port prototype blueprints in AUTOSAR standardization templates.

Port prototype blueprints provide a way to define standard templates for port prototypes
that can be reused across different AUTOSAR software components. This is particularly useful
for standardization and blueprint-based development approaches in AUTOSAR architecture.

Classes:
    PortPrototypeBlueprintInitValue: Represents initial value specifications for port prototype blueprints
    PortPrototypeBlueprint: Defines a blueprint for port prototypes with communication specifications
"""

from typing import List, Union

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Constants import (
    ValueSpecification,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import (
    AtpStructureElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import (
    PPortComSpec,
    RPortComSpec,
)


class PortPrototypeBlueprintInitValue(ARObject):
    """
    Represents an initial value specification for a port prototype blueprint.
    This class defines the initial value and associated data prototype reference
    for a specific port prototype blueprint element.
    """

    def __init__(self) -> None:
        super().__init__()

        self.dataPrototypeRef: Union[Union[RefType, None] , None] = None
        self.value: Union[Union[ValueSpecification, None] , None] = None

    def getDataPrototypeRef(self) -> Union[RefType, None]:
        """
        Gets the data prototype reference for this initial value specification.

        Returns:
            Reference to the data prototype
        """
        return self.dataPrototypeRef

    def setDataPrototypeRef(self, value: RefType) -> "PortPrototypeBlueprintInitValue":
        """
        Sets the data prototype reference for this initial value specification.

        Args:
            value: Reference to the data prototype

        Returns:
            Self instance for method chaining
        """
        if value is not None:
            self.dataPrototypeRef = value
        return self

    def getValue(self) -> ValueSpecification:
        """
        Gets the value specification for this initial value.

        Returns:
            The value specification
        """
        return self.value

    def setValue(self, value: ValueSpecification):
        """
        Sets the value specification for this initial value.

        Args:
            value: The value specification

        Returns:
            Self instance for method chaining
        """
        if value is not None:
            self.value = value
        return self


class PortPrototypeBlueprint(AtpStructureElement):
    """
    Defines a blueprint for port prototypes in AUTOSAR standardization templates.
    This class provides a template for defining port prototypes that can be reused
    across different software components, helping to standardize port configurations.
    """
    def __init__(self, parent, short_name) -> None:
        super().__init__(parent, short_name)

        self.initValues: List[PortPrototypeBlueprintInitValue] = []
        self.interfaceRef: Union[Union[RefType, None] , None] = None
        self.providedComSpecs: List[PPortComSpec] = []
        self.requiredComSpecs: List[RPortComSpec] = []

    def getInitValues(self) -> List[PortPrototypeBlueprintInitValue]:
        """
        Gets the list of initial value specifications for this port prototype blueprint.

        Returns:
            List of initial value specifications
        """
        return self.initValues

    def setInitValues(self, value: List[PortPrototypeBlueprintInitValue]):
        """
        Sets the list of initial value specifications for this port prototype blueprint.

        Args:
            value: List of initial value specifications

        Returns:
            Self instance for method chaining
        """
        if value is not None:
            self.initValues = value
        return self

    def getInterfaceRef(self) -> Union[RefType, None]:
        """
        Gets the interface reference for this port prototype blueprint.

        Returns:
            Reference to the interface
        """
        return self.interfaceRef

    def setInterfaceRef(self, value: RefType) -> "PortPrototypeBlueprint":
        """
        Sets the interface reference for this port prototype blueprint.

        Args:
            value: Reference to the interface

        Returns:
            Self instance for method chaining
        """
        if value is not None:
            self.interfaceRef = value
        return self

    def getProvidedComSpecs(self) -> List[PPortComSpec]:
        """
        Gets the list of provided communication specifications for this port prototype blueprint.

        Returns:
            List of provided communication specifications
        """
        return self.providedComSpecs

    def setProvidedComSpecs(self, value: List[PPortComSpec]):
        """
        Sets the list of provided communication specifications for this port prototype blueprint.

        Args:
            value: List of provided communication specifications

        Returns:
            Self instance for method chaining
        """
        if value is not None:
            self.providedComSpecs = value
        return self

    def getRequiredComSpecs(self) -> List[RPortComSpec]:
        """
        Gets the list of required communication specifications for this port prototype blueprint.

        Returns:
            List of required communication specifications
        """
        return self.requiredComSpecs

    def setRequiredComSpecs(self, value: List[RPortComSpec]):
        """
        Sets the list of required communication specifications for this port prototype blueprint.

        Args:
            value: List of required communication specifications

        Returns:
            Self instance for method chaining
        """
        if value is not None:
            self.requiredComSpecs = value
        return self
