from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject import AutosarEngineeringObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import VerbatimString
from armodel.models.M2.MSR.AsamHdo.SpecialData import Sdg


class BuildActionEntity(Identifiable):
    """
    This meta-class represents the ability to describe a build action entity which might be specialized to environments as well as to individual build actions.
    """

    # BuildActionEntity method parity checklist:
    # Spec: R23-11/AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 10.5, p.371 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addDeliveryArtifact [x] impl  [x] docstring  [x] test  [ ] reader  [ ] writer  R23-11
    # [x] getDeliveryArtifacts [x] impl  [x] docstring  [x] test  [ ] reader  [ ] writer  R23-11
    # [x] getInvocation     [x] impl  [x] docstring  [x] test  [ ] reader  [ ] writer  R23-11
    # [x] setInvocation     [x] impl  [x] docstring  [x] test  [ ] reader  [ ] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is BuildActionEntity:
            raise TypeError("BuildActionEntity is an abstract class.")

        super().__init__(parent, short_name)

        # This denotes the delivery artifacts for the entity for reference purposes.
        self.deliveryArtifacts: List[AutosarEngineeringObject] = []

        # This specifies how to invoke a build action in the given environment.
        self.invocation: Optional[BuildActionInvocator] = None

    def addDeliveryArtifact(self, value: Optional[AutosarEngineeringObject]) -> "BuildActionEntity":
        """This denotes the delivery artifacts for the entity for reference purposes. A None value is a no-op and does not append anything."""
        if value is not None:
            self.deliveryArtifacts.append(value)
        return self

    def getDeliveryArtifacts(self) -> List[AutosarEngineeringObject]:
        """This denotes the delivery artifacts for the entity for reference purposes."""
        return self.deliveryArtifacts

    def getInvocation(self) -> Optional["BuildActionInvocator"]:
        """This specifies how to invoke a build action in the given environment."""
        return self.invocation

    def setInvocation(self, value: Optional["BuildActionInvocator"]) -> "BuildActionEntity":
        """This specifies how to invoke a build action in the given environment. A None value is a no-op and does not overwrite an existing invocation."""
        if value is not None:
            self.invocation = value
        return self


class BuildActionInvocator(ARObject):
    """
    This meta-class represents the ability to specify the invocation of a task in a build action.
    """

    # BuildActionInvocator method parity checklist:
    # Spec: R23-11/AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 10.6, p.372 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCommand   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCommand   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSdgs      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addSdg       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This represents the command to invocate the processor. Note that this is a generic string which can be interpreted properly in the processor environment. Note that it is optional due to the fact that some actions are hardwired in the environment and do not need an explicit command. On the other hand the properties of an invocator can be complex and not standardized.
        self.command: Optional[VerbatimString] = None

        # This represents a general data structure intended to denote parameters for the BuildAction.
        self.sdgs: List[Sdg] = []

    def getCommand(self) -> Optional[VerbatimString]:
        """This represents the command to invocate the processor. Note that this is a generic string which can be interpreted properly in the processor environment. Note that it is optional due to the fact that some actions are hardwired in the environment and do not need an explicit command. On the other hand the properties of an invocator can be complex and not standardized."""
        return self.command

    def setCommand(self, value: Optional[VerbatimString]) -> "BuildActionInvocator":
        """This represents the command to invocate the processor. Note that this is a generic string which can be interpreted properly in the processor environment. Note that it is optional due to the fact that some actions are hardwired in the environment and do not need an explicit command. On the other hand the properties of an invocator can be complex and not standardized. A None value is a no-op and does not overwrite an existing command."""
        if value is not None:
            self.command = value
        return self

    def getSdgs(self) -> List[Sdg]:
        """This represents a general data structure intended to denote parameters for the BuildAction."""
        return self.sdgs

    def addSdg(self, value: Optional[Sdg]) -> "BuildActionInvocator":
        """This represents a general data structure intended to denote parameters for the BuildAction. A None value is a no-op and does not append anything."""
        if value is not None:
            self.sdgs.append(value)
        return self
