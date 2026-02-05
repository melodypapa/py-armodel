from typing import List

from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    ARElement,
)
from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models_v2.M2.MSR.Documentation.Annotation import Annotation



__all__ = []

class Documentation(ARElement):
    """
    Represents documentation in the AUTOSAR model.

    This class is used to provide documentation for AUTOSAR elements,
    including annotations and text descriptions.

    Attributes:
        annotations (List[Annotation]): A list of annotations for the documentation.
        description (String): The description text.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.annotations: List[Annotation] = []
        self.description: String = None

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
