from typing import List

from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.ApplicationDesign.PortInterface import Field
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import ApplicationDataType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import VariableDataPrototype
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import ClientServerOperation, PortInterface


class ApplicationDeferredDataType(ApplicationDataType):
    """A placeholder data type in which the precise application data type is deferred to a later stage."""

    # ApplicationDeferredDataType method parity checklist:
    # Spec: R23-11/AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf, Table 3.17, p.37 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class ApplicationInterface(PortInterface):
    """
    This represents the ability to define a PortInterface that consists of a composition of commands (method calls), indications (events) and attributes (fields) Tags: atp.Status=draft atp.recommendedPackage=Interfaces
    """

    # ApplicationInterface method parity checklist:
    # Spec: AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf, Table 3.7, p.28
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAttributes               [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] addAttribute                [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getCommands                 [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] addCommand                  [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getIndications              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addIndication               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the set of attributes defined in the context of an Abstract Platform ApplicationInterface. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=attribute.shortName, attribute.variation Point.shortLabel atp.Status=draft vh.latestBindingTime=blueprintDerivationTime
        self.attributes: List[Field] = []
        # This represents the collection of commands or function calls (with optional data arguments) defined in the context of an ApplicationInterface. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=command.shortName, command.variation Point.shortLabel atp.Status=draft vh.latestBindingTime=blueprintDerivationTime
        self.commands: List[ClientServerOperation] = []
        # This represents the collection of indication or events (with optional data argument) defined in the context of an ApplicationInterface. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=indication.shortName, indication.variation Point.shortLabel atp.Status=draft vh.latestBindingTime=blueprintDerivationTime
        self.indications: List[VariableDataPrototype] = []

    def getAttributes(self) -> List[Field]:
        """
        This represents the set of attributes defined in the context of an Abstract Platform ApplicationInterface. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=attribute.shortName, attribute.variation Point.shortLabel atp.Status=draft vh.latestBindingTime=blueprintDerivationTime
        """
        return self.attributes

    def setAttributes(self, value: List[Field]) -> "ApplicationInterface":
        """
        This represents the set of attributes defined in the context of an Abstract Platform ApplicationInterface. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=attribute.shortName, attribute.variation Point.shortLabel atp.Status=draft vh.latestBindingTime=blueprintDerivationTime
        """
        self.attributes = value
        return self

    def addAttribute(self, value: Field) -> "ApplicationInterface":
        """
        This represents the set of attributes defined in the context of an Abstract Platform ApplicationInterface. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=attribute.shortName, attribute.variation Point.shortLabel atp.Status=draft vh.latestBindingTime=blueprintDerivationTime
        """
        self.attributes.append(value)
        return self

    def getCommands(self) -> List[ClientServerOperation]:
        """
        This represents the collection of commands or function calls (with optional data arguments) defined in the context of an ApplicationInterface. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=command.shortName, command.variation Point.shortLabel atp.Status=draft vh.latestBindingTime=blueprintDerivationTime
        """
        return self.commands

    def setCommands(self, value: List[ClientServerOperation]) -> "ApplicationInterface":
        """
        This represents the collection of commands or function calls (with optional data arguments) defined in the context of an ApplicationInterface. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=command.shortName, command.variation Point.shortLabel atp.Status=draft vh.latestBindingTime=blueprintDerivationTime
        """
        self.commands = value
        return self

    def addCommand(self, value: ClientServerOperation) -> "ApplicationInterface":
        """
        This represents the collection of commands or function calls (with optional data arguments) defined in the context of an ApplicationInterface. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=command.shortName, command.variation Point.shortLabel atp.Status=draft vh.latestBindingTime=blueprintDerivationTime
        """
        self.commands.append(value)
        return self

    def getIndications(self) -> List[VariableDataPrototype]:
        """
        This represents the collection of indication or events (with optional data argument) defined in the context of an ApplicationInterface. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=indication.shortName, indication.variation Point.shortLabel atp.Status=draft vh.latestBindingTime=blueprintDerivationTime
        """
        return self.indications

    def setIndications(self, value: List[VariableDataPrototype]) -> "ApplicationInterface":
        """
        This represents the collection of indication or events (with optional data argument) defined in the context of an ApplicationInterface. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=indication.shortName, indication.variation Point.shortLabel atp.Status=draft vh.latestBindingTime=blueprintDerivationTime
        """
        self.indications = value
        return self

    def addIndication(self, value: VariableDataPrototype) -> "ApplicationInterface":
        """
        This represents the collection of indication or events (with optional data argument) defined in the context of an ApplicationInterface. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=indication.shortName, indication.variation Point.shortLabel atp.Status=draft vh.latestBindingTime=blueprintDerivationTime
        """
        self.indications.append(value)
        return self
