
from abc import ABCMeta

from .M2.MSR.documentation.block_elements import DocumentationBlock
from .multilanguage_data import MultilanguageLongName
from .ar_object import ARLiteral, ARObject


class GeneralAnnotation(ARObject, metaclass=ABCMeta):
    def __init__(self):
        if type(self) == ARObject:
            raise NotImplementedError("GeneralAnnotation is an abstract class.")
        
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

