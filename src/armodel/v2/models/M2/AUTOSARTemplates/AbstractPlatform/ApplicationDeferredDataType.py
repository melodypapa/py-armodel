from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import (
    ApplicationDataType,
)


class ApplicationDeferredDataType(ApplicationDataType):

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass    """
    A placeholder data type in which the precise application data type is
    deferred to a later stage. Tags: atp.Status=draft
    atp.recommendedPackage=ApplicationDataTypes

    Sources:
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 37, Foundation
      R23-11)
    """

    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)
