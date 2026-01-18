from typing import List
from armodel.models.M2.MSR.Documentation.Annotation import Annotation
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String


class Documentation(ARObject):
    """
    Represents documentation in the AUTOSAR model.

    This class is used to provide documentation for AUTOSAR elements,
    including annotations and text descriptions.

    Attributes:
        annotations (List[Annotation]): A list of annotations for the documentation.
        description (String): The description text.
    """
    def __init__(self):
        super().__init__()

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