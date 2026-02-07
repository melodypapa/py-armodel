from abc import ABC
from typing import TYPE_CHECKING, Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
)
from armodel.v2.models.M2.MSR.Documentation.TextModel.MultilanguageData import (
    MultilanguageLongName,
)

if TYPE_CHECKING:
    from armodel.v2.models.M2.MSR.Documentation.TextModel.BlockElements import (
        DocumentationBlock,
    )


class GeneralAnnotation(ARObject, ABC):
    def __init__(self) -> None:
        if type(self) is GeneralAnnotation:
            raise TypeError("GeneralAnnotation is an abstract class.")

        super().__init__()
        self.annotationOrigin: Union[ARLiteral, None] = None
        self.annotationText: Union["DocumentationBlock", None] = None
        self.label: Union[MultilanguageLongName, None] = None

    def getAnnotationOrigin(self) -> Union[ARLiteral, None]:
        return self.annotationOrigin

    def setAnnotationOrigin(self, value: ARLiteral) -> "GeneralAnnotation":
        self.annotationOrigin = value
        return self

    def getAnnotationText(self) -> Union["DocumentationBlock", None]:
        return self.annotationText

    def setAnnotationText(self, value: "DocumentationBlock") -> "GeneralAnnotation":
        self.annotationText = value
        return self

    def getLabel(self) -> Union[MultilanguageLongName, None]:
        return self.label

    def setLabel(self, value: MultilanguageLongName) -> "GeneralAnnotation":
        self.label = value
        return  self


class Annotation(GeneralAnnotation):
    def __init__(self) -> None:
        super().__init__()
