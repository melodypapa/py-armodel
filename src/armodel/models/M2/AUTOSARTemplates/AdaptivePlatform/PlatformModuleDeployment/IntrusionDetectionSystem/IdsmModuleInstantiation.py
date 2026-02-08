from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.IntrusionDetectionSystem.IdsPlatformInstantiation import (
    IdsPlatformInstantiation,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class IdsmModuleInstantiation(IdsPlatformInstantiation):
    """
    This meta-class defines the attributes for the IdsM configuration on a
    specific machine. Tags: atp.Status=candidate

    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 63, Foundation R23-11)
    """

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
