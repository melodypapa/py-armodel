from typing import List

from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.ApplicationDesign.PortInterface.Field import (
    Field,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
    ClientServerOperation,
    PortInterface,
)


class ApplicationInterface(PortInterface):
    """
    This represents the ability to define a PortInterface that consists of a
    composition of commands (method calls), indications (events) and attributes
    (fields) Tags: atp.Status=draft atp.recommendedPackage=Interfaces

    Sources:
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 28, Foundation
      R23-11)
    """

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the set of attributes defined in the context Abstract
        # Platform ApplicationInterface.
        # atpVariation.
        self.attributes: List[Field] = []
        # This represents the collection of commands or function optional data
        # arguments) defined in the context ApplicationInterface.
        # atpVariation.
        self.commands: List[ClientServerOperation] = []
        # This represents the collection of indication or events (with argument)
        # defined in the context of an atpVariation.
        self.indications: List[RefType] = []

    def getAttributes(self) -> List[Field]:
        return self.attributes

    def setAttributes(self, value: List[Field]) -> "ApplicationInterface":
        self.attributes = value
        return self

    def addAttribute(self, value: Field) -> "ApplicationInterface":
        """Adds a value to the attributes list."""
        self.attributes.append(value)
        return self

    def getCommands(self) -> List[ClientServerOperation]:
        return self.commands

    def setCommands(self, value: List[ClientServerOperation]) -> "ApplicationInterface":
        self.commands = value
        return self

    def addCommand(self, value: ClientServerOperation) -> "ApplicationInterface":
        """Adds a value to the commands list."""
        self.commands.append(value)
        return self

    def getIndications(self) -> List[RefType]:
        return self.indications

    def setIndications(self, value: List[RefType]) -> "ApplicationInterface":
        self.indications = value
        return self

    def addIndication(self, value: RefType) -> "ApplicationInterface":
        """Adds a value to the indications list."""
        self.indications.append(value)
        return self
