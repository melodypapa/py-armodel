from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultilanguageLongName
from abc import ABC


class GeneralAnnotation(ARObject, ABC):
    """
    Abstract base class for annotations including origin, text, and label.
    """

    # GeneralAnnotation method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getAnnotationOrigin          [x] impl  [ ] docstring  [ ] test
    # [ ] setAnnotationOrigin          [x] impl  [ ] docstring  [ ] test
    # [ ] getAnnotationText            [x] impl  [ ] docstring  [ ] test
    # [ ] setAnnotationText            [x] impl  [ ] docstring  [ ] test
    # [ ] getLabel                     [x] impl  [ ] docstring  [ ] test
    # [ ] setLabel                     [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        if type(self) is GeneralAnnotation:
            raise TypeError("GeneralAnnotation is an abstract class.")

        super().__init__()
        self.annotationOrigin = None  # type: ARLiteral
        self.annotationText = None  # type: DocumentationBlock
        self.label = None  # type: MultilanguageLongName

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
        return self


class Annotation(GeneralAnnotation):
    """
    This is a plain annotation which does not have further formal data.
    """

    # Annotation method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.72, p.163
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no own attributes)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self):
        super().__init__()
