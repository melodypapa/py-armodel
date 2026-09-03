from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LanguageSpecific
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable
from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView import Paginateable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject import EngineeringObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum


class GraphicFitEnum(AREnum):
    """
    Enumeration for graphic fitting modes.
    """

    # GraphicFitEnum method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self, enum_values):
        super().__init__([])


class Graphic(EngineeringObject):
    """
    Graphic element with filename, dimensions, and fit properties.
    """

    # Graphic method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getEditfit                   [x] impl  [ ] docstring  [ ] test
    # [ ] setEditfit                   [x] impl  [ ] docstring  [ ] test
    # [ ] getEditHeight                [x] impl  [ ] docstring  [ ] test
    # [ ] setEditHeight                [x] impl  [ ] docstring  [ ] test
    # [ ] getEditscale                 [x] impl  [ ] docstring  [ ] test
    # [ ] setEditscale                 [x] impl  [ ] docstring  [ ] test
    # [ ] getEditWidth                 [x] impl  [ ] docstring  [ ] test
    # [ ] setEditWidth                 [x] impl  [ ] docstring  [ ] test
    # [ ] getFilename                  [x] impl  [ ] docstring  [ ] test
    # [ ] setFilename                  [x] impl  [ ] docstring  [ ] test
    # [ ] getFit                       [x] impl  [ ] docstring  [ ] test
    # [ ] setFit                       [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.editfit = None  # type: GraphicFitEnum
        self.editHeight = None  # type: String
        self.editscale = None  # type: String
        self.editWidth = None  # type: String
        self.filename = None  # type: String
        self.fit = None  # type: GraphicFitEnum

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
    """
    Image map definition for clickable regions within a graphic.
    """

    # Map method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()


class LGraphic(LanguageSpecific):
    """
    This meta-class represents the figure in one particular language.
    """

    # LGraphic method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.25, p.308
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getGraphic   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setGraphic   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMap       [x] impl  [x] docstring  [x] test  [ ] reader  [ ] writer
    # [x] setMap       [x] impl  [x] docstring  [x] test  [ ] reader  [ ] writer

    def __init__(self):
        super().__init__()

        # Reference to the actual graphic represented in the figure. Tags: xml.sequenceOffset=20
        self.graphic = None  # type: Graphic

        # Image maps enable authors to specify regions of an image or object and assign a specific action to each region. Tags: xml.sequenceOffset=30
        self.map = None  # type: Map

    def getGraphic(self):
        """
        Reference to the actual graphic represented in the figure. Tags: xml.sequenceOffset=20

        Returns:
            The graphic represented in the figure
        """
        return self.graphic

    def setGraphic(self, value):
        """
        Reference to the actual graphic represented in the figure. Tags: xml.sequenceOffset=20. A None value is a no-op and does not overwrite an existing graphic.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.graphic = value
        return self

    def getMap(self):
        """
        Image maps enable authors to specify regions of an image or object and assign a specific action to each region. Tags: xml.sequenceOffset=30

        Returns:
            The image map of the figure
        """
        return self.map

    def setMap(self, value):
        """
        Image maps enable authors to specify regions of an image or object and assign a specific action to each region. Tags: xml.sequenceOffset=30. A None value is a no-op and does not overwrite an existing map.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.map = value
        return self


class MlFigure(Paginateable, VariationPointCapable):
    """
    Multi-language figure with caption, graphics, and optional verbatim
    content.
    """

    # MlFigure method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getFigureCaption             [x] impl  [ ] docstring  [ ] test
    # [ ] setFigureCaption             [x] impl  [ ] docstring  [ ] test
    # [ ] getHelpEntry                 [x] impl  [ ] docstring  [ ] test
    # [ ] setHelpEntry                 [x] impl  [ ] docstring  [ ] test
    # [ ] getLGraphics                 [x] impl  [ ] docstring  [ ] test
    # [ ] addLGraphics                 [x] impl  [ ] docstring  [ ] test
    # [ ] getPgwide                    [x] impl  [ ] docstring  [ ] test
    # [ ] setPgwide                    [x] impl  [ ] docstring  [ ] test
    # [ ] getVerbatim                  [x] impl  [ ] docstring  [ ] test
    # [ ] setVerbatim                  [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.figureCaption = None  # type: Caption
        self.helpEntry = None  # type: String
        self.lGraphics = []  # type: List[LGraphic]
        self.pgwide = None  # type: PgwideEnum
        self.verbatim = None  # type: MultiLanguageVerbatim

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
