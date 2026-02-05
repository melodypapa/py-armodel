from typing import Optional

from armodel.models_v2.M2.AUTOSARTemplates.BswModuleTemplate.BswOverview import (
    BswModuleDescription,
)
from armodel.models_v2.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import (
    ModeDeclaration,
)
from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class ModeInBswModuleDescriptionInstanceRef(ARObject):
    """

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 323, Classic Platform
      R23-11)
    """

    def __init__(self):
        super().__init__()

        # Stereotypes: atpDerived.
        self.bases: Optional[BswModuleDescription] = None
        # Tags: xml.
        # sequenceOffset=20.
        self.contextModes: RefType = None
        # Tags: xml.
        # sequenceOffset=30.
        self.targetModes: Optional[ModeDeclaration] = None

    def getBases(self) -> BswModuleDescription:
        return self.bases

    def setBases(
        self, value: BswModuleDescription
    ) -> "ModeInBswModuleDescriptionInstanceRef":
        self.bases = value
        return self

    def getContextModes(self) -> RefType:
        return self.contextModes

    def setContextModes(
        self, value: RefType
    ) -> "ModeInBswModuleDescriptionInstanceRef":
        self.contextModes = value
        return self

    def getTargetModes(self) -> ModeDeclaration:
        return self.targetModes

    def setTargetModes(
        self, value: ModeDeclaration
    ) -> "ModeInBswModuleDescriptionInstanceRef":
        self.targetModes = value
        return self
