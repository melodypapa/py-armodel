from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.MSR.Documentation.BlockElements.Figure import (
    MlFigure,
)
from armodel.v2.models.M2.MSR.Documentation.TextModel.BlockElements.ListElements import (
    ARList,
    Item,
    ListEnum,
)
from armodel.v2.models.M2.MSR.Documentation.TextModel.BlockElements.PaginationAndView import (
    DocumentViewSelectable,
    Paginateable,
)

# DocumentationBlock is defined in this file below
from armodel.v2.models.M2.MSR.Documentation.TextModel.MultilanguageData import (
    MultiLanguageParagraph,
)


class DocumentationBlock(ARObject):

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        super().__init__()

        self.defList: Union[DefList, None] = None
        self.figures = []                           # type: List[MlFigure]
        self.formula = None                         # type：MlFormula
        self.labeledList: Union[LabeledList, None] = None
        self.lists = []                             # type: List[ARList]
        self.msrQueryP2: Union[MsrQueryP2, None] = None
        self.note: Union[Note, None] = None
        self.ps = []                                # type: List[MultiLanguageParagraph]
        self.structuredReq: Union[StructuredReq, None] = None
        self.trace: Union[TraceableText, None] = None
        self.verbatim: Union[MultiLanguageVerbatim, None] = None

    def getDefList(self):
        return self.defList

    def setDefList(self, value):
        if value is not None:
            self.defList = value
        return self

    def getFigures(self):
        return self.figures

    def addFigure(self, value):
        if value is not None:
            self.figures.append(value)
        return self

    def getFormula(self):
        return self.formula

    def setFormula(self, value):
        if value is not None:
            self.formula = value
        return self

    def getLabeledList(self):
        return self.labeledList

    def setLabeledList(self, value):
        if value is not None:
            self.labeledList = value
        return self

    def getLists(self):
        return self.lists

    def addList(self, value):
        if value is not None:
            self.lists.append(value)
        return self

    def getMsrQueryP2(self):
        return self.msrQueryP2

    def setMsrQueryP2(self, value):
        if value is not None:
            self.msrQueryP2 = value
        return self

    def getNote(self):
        return self.note

    def setNote(self, value):
        if value is not None:
            self.note = value
        return self

    def getPs(self) -> List[MultiLanguageParagraph]:
        return self.ps

    def addP(self, value):
        if value is not None:
            self.ps.append(value)
        return self

    def getStructuredReq(self):
        return self.structuredReq

    def setStructuredReq(self, value):
        if value is not None:
            self.structuredReq = value
        return self

    def getTrace(self):
        return self.trace

    def setTrace(self, value):
        if value is not None:
            self.trace = value
        return self

    def getVerbatim(self):
        return self.verbatim

    def setVerbatim(self, value):
        if value is not None:
            self.verbatim = value
        return self


__all__ = [
    'ARList',
    'DocumentViewSelectable',
    'DocumentationBlock',
    'Item',
    'ListEnum',
    'MlFigure',
    'Paginateable',
]
