from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class CryptoKeySlotContent(Identifiable):
    """
    This meta-class represents the restriction of allowed usage of a key stored
    to the slot. Tags: atp.Status=candidate

    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 57, Foundation R23-11)
    """

    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)
