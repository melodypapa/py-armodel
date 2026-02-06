from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
)
from armodel.v2.models.M2.MSR.Documentation.TextModel.BlockElements import (
    DocumentationBlock,
)
from armodel.v2.models.M2.MSR.Documentation.TextModel.MultilanguageData import (
    MultilanguageLongName,
)


class GeneralAnnotation(ARObject, ABC):
    def __init__(self) -> None:
        if type(self) is GeneralAnnotation:
            raise TypeError("GeneralAnnotation is an abstract class.")

        super().__init__()
        self.annotationOrigin: Union[ARLiteral, None] = None
        self.annotationText: Union[DocumentationBlock, None] = None
        self.label: Union[MultilanguageLongName, None] = None

    def getAnnotationOrigin(self) -> ARLiteral:
        return self.annotationOrigin

    def setAnnotationOrigin(self, value: ARLiteral):
        self.annotationOrigin = value
        return self

    def getAnnotationText(self) -> DocumentationBlock:
        return self.annotationText

    def setAnnotationText(self, value: DocumentationBlock):
        self.annotationText = value
        return self

    def getLabel(self) -> MultilanguageLongName:
        return self.label

    def setLabel(self, value: MultilanguageLongName):
        self.label = value
        return  self


class Annotation(GeneralAnnotation):
    def __init__(self) -> None:
        super().__init__()
