from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject import AutosarEngineeringObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable


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
        self.invocation: Optional[object] = None

    def addDeliveryArtifact(self, value: Optional[AutosarEngineeringObject]) -> "BuildActionEntity":
        """This denotes the delivery artifacts for the entity for reference purposes. A None value is a no-op and does not append anything."""
        if value is not None:
            self.deliveryArtifacts.append(value)
        return self

    def getDeliveryArtifacts(self) -> List[AutosarEngineeringObject]:
        """This denotes the delivery artifacts for the entity for reference purposes."""
        return self.deliveryArtifacts

    def getInvocation(self) -> Optional[object]:
        """This specifies how to invoke a build action in the given environment."""
        return self.invocation

    def setInvocation(self, value: Optional[object]) -> "BuildActionEntity":
        """This specifies how to invoke a build action in the given environment. A None value is a no-op and does not overwrite an existing invocation."""
        if value is not None:
            self.invocation = value
        return self
