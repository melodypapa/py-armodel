
from .....M2.MSR.Documentation.TextModel.LanguageDataModel import LanguageSpecific
from .....M2.MSR.Documentation.TextModel.BlockElements.PaginationAndView import Paginateable
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject import EngineeringObject
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum


class GraphicFitEnum(AREnum):
    def __init__(self, enum_values):
        super().__init__([

        ])


class Graphic(EngineeringObject):
    def __init__(self):
        super().__init__()

        self.editfit = None                                     # type: GraphicFitEnum
        self.editHeight = None                                  # type: String
        self.editscale = None                                   # type: String
        self.editWidth = None                                   # type: String
        self.filename = None                                    # type: String
        self.fit = None                                         # type: GraphicFitEnum

    def getEditfit(self):
        return self.editfit

    def setEditfit(self, value):
        if value is not None:
            self.editfit = value
        return self

    def getEditHeight(self):
        return self.editHeight

    def setEditHeight(self, value):
        if value is not None:
            self.editHeight = value
        return self

    def getEditscale(self):
        return self.editscale

    def setEditscale(self, value):
        if value is not None:
            self.editscale = value
        return self

    def getEditWidth(self):
        return self.editWidth

    def setEditWidth(self, value):
        if value is not None:
            self.editWidth = value
        return self

    def getFilename(self):
        return self.filename

    def setFilename(self, value):
        if value is not None:
            self.filename = value
        return self

    def getFit(self):
        return self.fit

    def setFit(self, value):
        if value is not None:
            self.fit = value
        return self
    

class Map(ARObject):
    def __init__(self):
        super().__init__()
    

class LGraphic(LanguageSpecific):
    def __init__(self):
        super().__init__()

        self.l = None                                           # type: str                         # noqa E741
        self.graphic = None                                     # type: Graphic
        self.map = None                                         # type: Map

    def getL(self):
        return self.l

    def setL(self, value):
        if value is not None:
            self.l = value                                                                          # noqa E741
        return self

    def getGraphic(self):
        return self.graphic

    def setGraphic(self, value):
        if value is not None:
            self.graphic = value
        return self

    def getMap(self):
        return self.map

    def setMap(self, value):
        if value is not None:
            self.map = value
        return self


class MlFigure(Paginateable):
    def __init__(self):
        super().__init__()

        self.figureCaption = None                               # type: Caption
        self.helpEntry = None                                   # type: String
        self.lGraphics = []                                     # type: List[LGraphic]
        self.pgwide = None                                      # type: PgwideEnum
        self.verbatim = None                                    # type: MultiLanguageVerbatim

    def getFigureCaption(self):
        return self.figureCaption

    def setFigureCaption(self, value):
        if value is not None:
            self.figureCaption = value
        return self

    def getHelpEntry(self):
        return self.helpEntry

    def setHelpEntry(self, value):
        if value is not None:
            self.helpEntry = value
        return self

    def getLGraphics(self):
        return self.lGraphics

    def addLGraphics(self, value):
        if value is not None:
            self.lGraphics.append(value)
        return self

    def getPgwide(self):
        return self.pgwide

    def setPgwide(self, value):
        if value is not None:
            self.pgwide = value
        return self

    def getVerbatim(self):
        return self.verbatim

    def setVerbatim(self, value):
        if value is not None:
            self.verbatim = value
        return self
