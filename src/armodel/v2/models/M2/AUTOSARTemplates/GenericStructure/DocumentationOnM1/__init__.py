from typing import List, Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    String,
)
from armodel.v2.models.M2.MSR.Documentation.Annotation import Annotation


class StandardNameEnum(AREnum):
    """
    Enumeration of standard names for AUTOSAR documentation.

    This enumeration lists all allowed standard abbreviations used in
    AppliedStandard.appliesTo and StructuredReq.appliesTo.
    """
    DIAGNOSTIC = 'Diagnostic'
    AUTOSARAP = 'AUTOSARAP'
    CP = 'CP'
    FO = 'FO'
    TA = 'TA'
    TC = 'TC'

    def __init__(self) -> None:
        super().__init__([
            StandardNameEnum.DIAGNOSTIC,
            StandardNameEnum.AUTOSARAP,
            StandardNameEnum.CP,
            StandardNameEnum.FO,
            StandardNameEnum.TA,
            StandardNameEnum.TC,
        ])


# Use factory function to create Documentation instances
def createDocumentation(parent: ARObject, short_name: str):
    """
    Factory function to create Documentation instances.
    This avoids circular import with Identifiable module.
    """
    from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
        ARElement,
    )

    class _Documentation(ARElement):
        """
        Represents documentation in the AUTOSAR model.

        This class is used to provide documentation for AUTOSAR elements,
        including annotations and text descriptions.

        Attributes:
            annotations (List[Annotation]): A list of annotations for the documentation.
            description (String): The description text.
        """
        def __init__(self, parent: ARObject, short_name: str) -> None:
            super().__init__(parent, short_name)

            self.annotations: List[Annotation] = []
            self.description: Union[Union[String, None], None] = None

        def getAnnotations(self) -> List[Annotation]:
            return self.annotations

        def addAnnotation(self, value: Annotation):
            if value is not None:
                self.annotations.append(value)
            return self

        def getDescription(self) -> String:
            return self.description

        def setDescription(self, value: String):
            if value is not None:
                self.description = value
            return self

    return _Documentation(parent, short_name)


# Export Documentation as a class-like object that creates instances
class Documentation:
    """Factory class for creating Documentation instances."""
    def __new__(cls, parent: ARObject, short_name: str):
        return createDocumentation(parent, short_name)


__all__ = [
    'StandardNameEnum',
    'Documentation',
]
