from armodel.models_v2.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral
from armodel.models_v2.M2.MSR.Documentation.TextModel.MultilanguageData import MultilanguageLongName
from abc import ABC

class GeneralAnnotation(ARObject, ABC):
    def __init__(self):
        if type(self) is GeneralAnnotation:
            raise TypeError("GeneralAnnotation is an abstract class.")

        super().__init__()
        self.annotationOrigin = None        # type: ARLiteral
        self.annotationText = None          # type: DocumentationBlock
        self.label = None                   # type: MultilanguageLongName

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
    def __init__(self):
        super().__init__()