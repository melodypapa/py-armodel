
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject import (
    EngineeringObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)
from armodel.v2.models.M2.MSR.Documentation.TextModel.BlockElements.PaginationAndView import (
    Paginateable,
)
from armodel.v2.models.M2.MSR.Documentation.TextModel.LanguageDataModel import (
    LanguageSpecific,
)


class GraphicFitEnum(AREnum):
    def __init__(self, enum_values) -> None:
        super().__init__([

        ])


class Graphic(EngineeringObject):
    def __init__(self) -> None:
        super().__init__()

        self.editfit: Union[GraphicFitEnum, None] = None
        self.editHeight: Union[String, None] = None
        self.editscale: Union[String, None] = None
        self.editWidth: Union[String, None] = None
        self.filename: Union[String, None] = None
        self.fit: Union[GraphicFitEnum, None] = None

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

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        super().__init__()


class LGraphic(LanguageSpecific):
    def __init__(self) -> None:
        super().__init__()

        self.l: Union[str, None] = None                         # noqa E741
        self.graphic: Union[Graphic, None] = None
        self.map: Union[Map, None] = None

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
    def __init__(self) -> None:
        super().__init__()

        self.figureCaption: Union[Caption, None] = None
        self.helpEntry: Union[String, None] = None
        self.lGraphics = []                                     # type: List[LGraphic]
        self.pgwide: Union[PgwideEnum, None] = None
        self.verbatim: Union[MultiLanguageVerbatim, None] = None

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
