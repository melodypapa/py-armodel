from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LanguageSpecific
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable
from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView import Paginateable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject import EngineeringObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum


class GraphicFitEnum(AREnum):
    """
    This enumerator specifies the policy how to place and scale the figure on the page.
    """

    # GraphicFitEnum method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.21, p.304
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on Graphic.editfit/fit/htmlFit (EDITFIT/FIT/HTML-FIT attributes)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # This indicates that the image shall be incorporated as is without scaling, rotation etc. Tags: atp.EnumerationLiteralIndex=0
    ASIS = "AS-IS"

    # Fit to the page Tags: atp.EnumerationLiteralIndex=1
    FIT_TO_PAGE = "FIT-TO-PAGE"

    # fit to the text containing the graphic. Tags: atp.EnumerationLiteralIndex=2
    FIT_TO_TEXT = "FIT-TO-TEXT"

    # This indicates that the width of the graphic shall be limited to the page width . The image shall not be scaled down but cropped. Tags: atp.EnumerationLiteralIndex=3
    LIMIT_TO_PAGE = "LIMIT-TO-PAGE"

    # This indicates that the width of the graphic shall be limited to the width of the current text flow . The image shall not be scaled down but cropped. Tags: atp.EnumerationLiteralIndex=4
    LIMIT_TO_TEXT = "LIMIT-TO-TEXT"

    # Rotate 180 degree Tags: atp.EnumerationLiteralIndex=5
    ROTATE_180 = "ROTATE-180"

    # Rotate 180 degree Tags: atp.EnumerationLiteralIndex=6
    ROTATE_180_LIMIT_TO_TEXT = "ROTATE-180-LIMIT-TO-TEXT"

    # Rotate 90 degree counter clockwise Tags: atp.EnumerationLiteralIndex=7
    ROTATE_90CCW = "ROTATE-90-CCW"

    # Rotate by 90 degree counter clock wise and then fit to text Tags: atp.EnumerationLiteralIndex=8
    ROTATE_90CCW_FIT_TO_TEXT = "ROTATE-90-CCW-FIT-TO-TEXT"

    # Rotate by 90 degree counter clock wise and then fit to text Tags: atp.EnumerationLiteralIndex=9
    ROTATE_90CCW_LIMIT_TO_TEXT = "ROTATE-90-CCW-LIMIT-TO-TEXT"

    # Rotate 90 degree clockwise Tags: atp.EnumerationLiteralIndex=10
    ROTATE_90CW = "ROTATE-90-CW"

    # Rotate by 90 degree and then fit to text Tags: atp.EnumerationLiteralIndex=11
    ROTATE_90CW_FIT_TO_TEXT = "ROTATE-90-CW-FIT-TO-TEXT"

    # Rotate by 90 degree and then fit to text Tags: atp.EnumerationLiteralIndex=12
    ROTATE_90CW_LIMIT_TO_TEXT = "ROTATE-90-CW-LIMIT-TO-TEXT"

    def __init__(self):
        super().__init__(
            (
                GraphicFitEnum.ASIS,
                GraphicFitEnum.FIT_TO_PAGE,
                GraphicFitEnum.FIT_TO_TEXT,
                GraphicFitEnum.LIMIT_TO_PAGE,
                GraphicFitEnum.LIMIT_TO_TEXT,
                GraphicFitEnum.ROTATE_180,
                GraphicFitEnum.ROTATE_180_LIMIT_TO_TEXT,
                GraphicFitEnum.ROTATE_90CCW,
                GraphicFitEnum.ROTATE_90CCW_FIT_TO_TEXT,
                GraphicFitEnum.ROTATE_90CCW_LIMIT_TO_TEXT,
                GraphicFitEnum.ROTATE_90CW,
                GraphicFitEnum.ROTATE_90CW_FIT_TO_TEXT,
                GraphicFitEnum.ROTATE_90CW_LIMIT_TO_TEXT,
            )
        )


class GraphicNotationEnum(AREnum):
    """
    This enumerator specifies the various notations (finally file types) used to represent the figure.
    """

    # GraphicNotationEnum method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.22, p.305
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on Graphic.notation (NOTATION attribute)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # bitmap image Tags: atp.EnumerationLiteralIndex=0
    BMP = "BMP"

    # Encapsulated Postscript Tags: atp.EnumerationLiteralIndex=1
    EPS = "EPS"

    # Graphics Interchange Format Tags: atp.EnumerationLiteralIndex=2
    GIF = "GIF"

    # "Joint Photographic Experts Group" format Tags: atp.EnumerationLiteralIndex=3
    JPG = "JPG"

    # Portable Document Format Tags: atp.EnumerationLiteralIndex=4
    PDF = "PDF"

    # Portable Network Graphics Tags: atp.EnumerationLiteralIndex=5
    PNG = "PNG"

    # scalable vector graphic Tags: atp.EnumerationLiteralIndex=6
    SVG = "SVG"

    # Tagged Image File Format Tags: atp.EnumerationLiteralIndex=7
    TIFF = "TIFF"

    def __init__(self):
        super().__init__(
            (
                GraphicNotationEnum.BMP,
                GraphicNotationEnum.EPS,
                GraphicNotationEnum.GIF,
                GraphicNotationEnum.JPG,
                GraphicNotationEnum.PDF,
                GraphicNotationEnum.PNG,
                GraphicNotationEnum.SVG,
                GraphicNotationEnum.TIFF,
            )
        )


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
