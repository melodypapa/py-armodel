from typing import Optional

from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LanguageSpecific
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable
from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView import Paginateable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject import EngineeringObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, NameToken, String


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


class AreaEnumNohref(AREnum):
    """
    This enumerator specifies the fact that the area has no reference.
    """

    # AreaEnumNohref method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.18, p.301
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on Area.nohref (NOHREF attribute)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # This indicates that the area has no active link. Tags: atp.EnumerationLiteralIndex=0
    NOHREF = "NOHREF"

    def __init__(self):
        super().__init__((AreaEnumNohref.NOHREF,))


class AreaEnumShape(AREnum):
    """
    This enumerator specifies the shape of the area.
    """

    # AreaEnumShape method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.19, p.302
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on Area.shape (SHAPE attribute)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # The shape is a circle. Tags: atp.EnumerationLiteralIndex=0
    CIRCLE = "CIRCLE"

    # This specifies the fact that the area covers the rest of the figure. Tags: atp.EnumerationLiteralIndex=1
    DEFAULT = "DEFAULT"

    # The area is specified as polygon. Tags: atp.EnumerationLiteralIndex=2
    POLY = "POLY"

    # The shape is specified as rectangle. Tags: atp.EnumerationLiteralIndex=3
    RECT = "RECT"

    def __init__(self):
        super().__init__(
            (
                AreaEnumShape.CIRCLE,
                AreaEnumShape.DEFAULT,
                AreaEnumShape.POLY,
                AreaEnumShape.RECT,
            )
        )


class Area(ARObject):
    """
    This element specifies a region in an image map. Image maps enable authors to specify regions in an object (e.g. a graphic) and to assign a specific activity to each region (e.g. load a document, launch a program etc.). For more details refer to the specification of HTML.
    """

    # Area method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.17, p.301
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setAccesskey      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getAccesskey      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAlt            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getAlt            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setClass          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getClass          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCoords         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCoords         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setHref           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getHref           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNohref         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNohref         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setOnblur         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getOnblur         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setOnclick        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getOnclick        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setOndblclick     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getOndblclick     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setOnfocus        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getOnfocus        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setOnkeydown      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getOnkeydown      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setOnkeypress     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getOnkeypress     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setOnkeyup        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getOnkeyup        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setOnmousedown    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getOnmousedown    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setOnmousemove    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getOnmousemove    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setOnmouseout     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getOnmouseout     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setOnmouseover    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getOnmouseover    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setOnmouseup      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getOnmouseup      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setShape          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getShape          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setStyle          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getStyle          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTabindex       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTabindex       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTitle          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTitle          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()

        # This attribute assigns an access key to an element. An access key is an individual character (e.g. "B") within the document character range. If an access key with an element assigned to it is pressed, the element comes into focus. The activity performed when an element comes into focus, is dependent on the element itself Tags: xml.attribute=true
        self.accesskey: Optional[String] = None

        # This attribute specifies the text to be inserted as an alternative to illustrations, shapes or applets, where these cannot be displayed by user agents. Tags: xml.attribute=true
        self.alt: Optional[String] = None

        # Blank separated list of classes Tags: xml.attribute=true
        self.class_: Optional[String] = None

        # This attribute specifies the position and shape on the screen. The number of values and their order depend on the geometrical figure defined. Tags: xml.attribute=true
        self.coords: Optional[String] = None

        # This attribute specifies the memory location of a web resource. It is therefore able to specify a link between the current element and the target element. Tags: xml.attribute=true
        self.href: Optional[String] = None

        # If this attribute is set, the Area has no associated link. Tags: xml.attribute=true
        self.nohref: Optional[AreaEnumNohref] = None

        # The ONBLUR-Event occurs, when focus is switched away from an element. A script can be stored in this attribute to be performed in the Event. Tags: xml.attribute=true
        self.onblur: Optional[String] = None

        # The ONCLICK-Event occurs, if the current element is clicked-on. A script can be stored in this attribute to be performed in the Event. Tags: xml.attribute=true
        self.onclick: Optional[String] = None

        # The ONCLICK-Event occurs, if the current element is "double" clicked-on. A script can be stored in this attribute to be performed in the Event. Tags: xml.attribute=true
        self.ondblclick: Optional[String] = None

        # The ONFOCUS-Event occurs, if an element comes into focus (e.g., through navigation using the tab button). A script can be stored in this attribute to be performed in the Event. Tags: xml.attribute=true
        self.onfocus: Optional[String] = None

        # The ONKEYDOWN-Event occurs, if a button on the current element is pressed down. A script can be stored in this attribute to be performed in the event. Tags: xml.attribute=true
        self.onkeydown: Optional[String] = None

        # The ONKEYPRESS-Event occurs, if a button on the current element is pressed down and released. A script can be stored in this attribute to be performed in the Event. Tags: xml.attribute=true
        self.onkeypress: Optional[String] = None

        # The ONKEYUP-Event occurs, if a button on the current element is released. A script can be stored in this attribute to be performed in the Event. Tags: xml.attribute=true
        self.onkeyup: Optional[String] = None

        # The ONMOUSEDOWN-Event occurs, if the mouse button used for clicking is held down on the current element. A script can be stored in this attribute to be performed in the Event. Tags: xml.attribute=true
        self.onmousedown: Optional[String] = None

        # The ONMOUSEMOVE-Event occurs, if the mouse pointer is moved on the current element (i.e. it is located on the current element). A script can be stored in this attribute to be performed in the Event. Tags: xml.attribute=true
        self.onmousemove: Optional[String] = None

        # The ONMOUSEOUT-Event occurs, if the mouse pointer is moved from the current element. A script can be stored in this attribute to be performed in the Event. Tags: xml.attribute=true
        self.onmouseout: Optional[String] = None

        # The ONMOUSEOVER-Event occurs, if the mouse pointer is moved to the current element from another location outside it. A script can be stored in this attribute to be performed in the Event. Tags: xml.attribute=true
        self.onmouseover: Optional[String] = None

        # The ONMOUSEUP-Event occurs if the mouse button used for clicking is released on the current element. A script can be stored in this attribute to be performed in the Event. Tags: xml.attribute=true
        self.onmouseup: Optional[String] = None

        # The shape of the area. Note that in HTML this is defaulted to RECT. Tags: xml.attribute=true
        self.shape: Optional[AreaEnumShape] = None

        # Information on the associated style Tags: xml.attribute=true
        self.style: Optional[String] = None

        # This attribute specifies the position of the current element in tabbing-order for the corresponding document. The value shall lie between 0 and 32767. The Tabbing Order defines the sequence in which elements are focused on, when the user navigates using the keyboard. Tags: xml.attribute=true
        self.tabindex: Optional[String] = None

        # Title information of the Area element Tags: xml.attribute=true
        self.title: Optional[String] = None

    def setAccesskey(self, value: Optional[String]) -> "Area":
        """
        This attribute assigns an access key to an element. An access key is an individual character (e.g. "B") within the document character range. If an access key with an element assigned to it is pressed, the element comes into focus. The activity performed when an element comes into focus, is dependent on the element itself Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing accesskey.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.accesskey = value
        return self

    def getAccesskey(self) -> Optional[String]:
        """
        This attribute assigns an access key to an element. An access key is an individual character (e.g. "B") within the document character range. If an access key with an element assigned to it is pressed, the element comes into focus. The activity performed when an element comes into focus, is dependent on the element itself Tags: xml.attribute=true
        """
        return self.accesskey

    def setAlt(self, value: Optional[String]) -> "Area":
        """
        This attribute specifies the text to be inserted as an alternative to illustrations, shapes or applets, where these cannot be displayed by user agents. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing alt.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.alt = value
        return self

    def getAlt(self) -> Optional[String]:
        """
        This attribute specifies the text to be inserted as an alternative to illustrations, shapes or applets, where these cannot be displayed by user agents. Tags: xml.attribute=true
        """
        return self.alt

    def setClass(self, value: Optional[String]) -> "Area":
        """
        Blank separated list of classes Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing class.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.class_ = value
        return self

    def getClass(self) -> Optional[String]:
        """
        Blank separated list of classes Tags: xml.attribute=true
        """
        return self.class_

    def setCoords(self, value: Optional[String]) -> "Area":
        """
        This attribute specifies the position and shape on the screen. The number of values and their order depend on the geometrical figure defined. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing coords.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.coords = value
        return self

    def getCoords(self) -> Optional[String]:
        """
        This attribute specifies the position and shape on the screen. The number of values and their order depend on the geometrical figure defined. Tags: xml.attribute=true
        """
        return self.coords

    def setHref(self, value: Optional[String]) -> "Area":
        """
        This attribute specifies the memory location of a web resource. It is therefore able to specify a link between the current element and the target element. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing href.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.href = value
        return self

    def getHref(self) -> Optional[String]:
        """
        This attribute specifies the memory location of a web resource. It is therefore able to specify a link between the current element and the target element. Tags: xml.attribute=true
        """
        return self.href

    def setNohref(self, value: Optional[AreaEnumNohref]) -> "Area":
        """
        If this attribute is set, the Area has no associated link. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing nohref.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.nohref = value
        return self

    def getNohref(self) -> Optional[AreaEnumNohref]:
        """
        If this attribute is set, the Area has no associated link. Tags: xml.attribute=true
        """
        return self.nohref

    def setOnblur(self, value: Optional[String]) -> "Area":
        """
        The ONBLUR-Event occurs, when focus is switched away from an element. A script can be stored in this attribute to be performed in the Event. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing onblur.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.onblur = value
        return self

    def getOnblur(self) -> Optional[String]:
        """
        The ONBLUR-Event occurs, when focus is switched away from an element. A script can be stored in this attribute to be performed in the Event. Tags: xml.attribute=true
        """
        return self.onblur

    def setOnclick(self, value: Optional[String]) -> "Area":
        """
        The ONCLICK-Event occurs, if the current element is clicked-on. A script can be stored in this attribute to be performed in the Event. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing onclick.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.onclick = value
        return self

    def getOnclick(self) -> Optional[String]:
        """
        The ONCLICK-Event occurs, if the current element is clicked-on. A script can be stored in this attribute to be performed in the Event. Tags: xml.attribute=true
        """
        return self.onclick

    def setOndblclick(self, value: Optional[String]) -> "Area":
        """
        The ONCLICK-Event occurs, if the current element is "double" clicked-on. A script can be stored in this attribute to be performed in the Event. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing ondblclick.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.ondblclick = value
        return self

    def getOndblclick(self) -> Optional[String]:
        """
        The ONCLICK-Event occurs, if the current element is "double" clicked-on. A script can be stored in this attribute to be performed in the Event. Tags: xml.attribute=true
        """
        return self.ondblclick

    def setOnfocus(self, value: Optional[String]) -> "Area":
        """
        The ONFOCUS-Event occurs, if an element comes into focus (e.g., through navigation using the tab button). A script can be stored in this attribute to be performed in the Event. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing onfocus.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.onfocus = value
        return self

    def getOnfocus(self) -> Optional[String]:
        """
        The ONFOCUS-Event occurs, if an element comes into focus (e.g., through navigation using the tab button). A script can be stored in this attribute to be performed in the Event. Tags: xml.attribute=true
        """
        return self.onfocus

    def setOnkeydown(self, value: Optional[String]) -> "Area":
        """
        The ONKEYDOWN-Event occurs, if a button on the current element is pressed down. A script can be stored in this attribute to be performed in the event. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing onkeydown.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.onkeydown = value
        return self

    def getOnkeydown(self) -> Optional[String]:
        """
        The ONKEYDOWN-Event occurs, if a button on the current element is pressed down. A script can be stored in this attribute to be performed in the event. Tags: xml.attribute=true
        """
        return self.onkeydown

    def setOnkeypress(self, value: Optional[String]) -> "Area":
        """
        The ONKEYPRESS-Event occurs, if a button on the current element is pressed down and released. A script can be stored in this attribute to be performed in the Event. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing onkeypress.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.onkeypress = value
        return self

    def getOnkeypress(self) -> Optional[String]:
        """
        The ONKEYPRESS-Event occurs, if a button on the current element is pressed down and released. A script can be stored in this attribute to be performed in the Event. Tags: xml.attribute=true
        """
        return self.onkeypress

    def setOnkeyup(self, value: Optional[String]) -> "Area":
        """
        The ONKEYUP-Event occurs, if a button on the current element is released. A script can be stored in this attribute to be performed in the Event. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing onkeyup.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.onkeyup = value
        return self

    def getOnkeyup(self) -> Optional[String]:
        """
        The ONKEYUP-Event occurs, if a button on the current element is released. A script can be stored in this attribute to be performed in the Event. Tags: xml.attribute=true
        """
        return self.onkeyup

    def setOnmousedown(self, value: Optional[String]) -> "Area":
        """
        The ONMOUSEDOWN-Event occurs, if the mouse button used for clicking is held down on the current element. A script can be stored in this attribute to be performed in the Event. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing onmousedown.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.onmousedown = value
        return self

    def getOnmousedown(self) -> Optional[String]:
        """
        The ONMOUSEDOWN-Event occurs, if the mouse button used for clicking is held down on the current element. A script can be stored in this attribute to be performed in the Event. Tags: xml.attribute=true
        """
        return self.onmousedown

    def setOnmousemove(self, value: Optional[String]) -> "Area":
        """
        The ONMOUSEMOVE-Event occurs, if the mouse pointer is moved on the current element (i.e. it is located on the current element). A script can be stored in this attribute to be performed in the Event. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing onmousemove.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.onmousemove = value
        return self

    def getOnmousemove(self) -> Optional[String]:
        """
        The ONMOUSEMOVE-Event occurs, if the mouse pointer is moved on the current element (i.e. it is located on the current element). A script can be stored in this attribute to be performed in the Event. Tags: xml.attribute=true
        """
        return self.onmousemove

    def setOnmouseout(self, value: Optional[String]) -> "Area":
        """
        The ONMOUSEOUT-Event occurs, if the mouse pointer is moved from the current element. A script can be stored in this attribute to be performed in the Event. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing onmouseout.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.onmouseout = value
        return self

    def getOnmouseout(self) -> Optional[String]:
        """
        The ONMOUSEOUT-Event occurs, if the mouse pointer is moved from the current element. A script can be stored in this attribute to be performed in the Event. Tags: xml.attribute=true
        """
        return self.onmouseout

    def setOnmouseover(self, value: Optional[String]) -> "Area":
        """
        The ONMOUSEOVER-Event occurs, if the mouse pointer is moved to the current element from another location outside it. A script can be stored in this attribute to be performed in the Event. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing onmouseover.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.onmouseover = value
        return self

    def getOnmouseover(self) -> Optional[String]:
        """
        The ONMOUSEOVER-Event occurs, if the mouse pointer is moved to the current element from another location outside it. A script can be stored in this attribute to be performed in the Event. Tags: xml.attribute=true
        """
        return self.onmouseover

    def setOnmouseup(self, value: Optional[String]) -> "Area":
        """
        The ONMOUSEUP-Event occurs if the mouse button used for clicking is released on the current element. A script can be stored in this attribute to be performed in the Event. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing onmouseup.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.onmouseup = value
        return self

    def getOnmouseup(self) -> Optional[String]:
        """
        The ONMOUSEUP-Event occurs if the mouse button used for clicking is released on the current element. A script can be stored in this attribute to be performed in the Event. Tags: xml.attribute=true
        """
        return self.onmouseup

    def setShape(self, value: Optional[AreaEnumShape]) -> "Area":
        """
        The shape of the area. Note that in HTML this is defaulted to RECT. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing shape.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.shape = value
        return self

    def getShape(self) -> Optional[AreaEnumShape]:
        """
        The shape of the area. Note that in HTML this is defaulted to RECT. Tags: xml.attribute=true
        """
        return self.shape

    def setStyle(self, value: Optional[String]) -> "Area":
        """
        Information on the associated style Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing style.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.style = value
        return self

    def getStyle(self) -> Optional[String]:
        """
        Information on the associated style Tags: xml.attribute=true
        """
        return self.style

    def setTabindex(self, value: Optional[String]) -> "Area":
        """
        This attribute specifies the position of the current element in tabbing-order for the corresponding document. The value shall lie between 0 and 32767. The Tabbing Order defines the sequence in which elements are focused on, when the user navigates using the keyboard. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing tabindex.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.tabindex = value
        return self

    def getTabindex(self) -> Optional[String]:
        """
        This attribute specifies the position of the current element in tabbing-order for the corresponding document. The value shall lie between 0 and 32767. The Tabbing Order defines the sequence in which elements are focused on, when the user navigates using the keyboard. Tags: xml.attribute=true
        """
        return self.tabindex

    def setTitle(self, value: Optional[String]) -> "Area":
        """
        Title information of the Area element Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing title.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.title = value
        return self

    def getTitle(self) -> Optional[String]:
        """
        Title information of the Area element Tags: xml.attribute=true
        """
        return self.title


class Graphic(EngineeringObject):
    """
    This class represents an artifact containing the image to be inserted in the document
    """

    # Graphic method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.20, p.303
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getEditfit        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setEditfit        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getEditHeight     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setEditHeight     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getEditscale      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setEditscale      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getEditWidth      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setEditWidth      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getFilename       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFilename       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getFit            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFit            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getGenerator      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setGenerator      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getHeight         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setHeight         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getHtmlFit        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setHtmlFit        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getHtmlHeight     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setHtmlHeight     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getHtmlScale      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setHtmlScale      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getHtmlWidth      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setHtmlWidth      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNotation       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNotation       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getScale          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setScale          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getWidth          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setWidth          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Specifies how the graphic shall be displayed in an editor. If the attribute is missing, Tags: xml.attribute=true
        self.editfit: Optional[GraphicFitEnum] = None

        # Specifies the height of the graphic when it is displayed in an editor. The unit can be added to the number in the string. Possible units are: cm, mm, px, pt. The default unit is px. Tags: xml.attribute=true
        self.editHeight: Optional[String] = None

        # Set the proportional scale when displayed in an editor. Tags: xml.attribute=true
        self.editscale: Optional[String] = None

        # Specifies the width of the graphic when it is displayed in an editor. The unit can be added to the number in the string. Possible units are: cm, mm, px, pt. The default unit is px. Tags: xml.attribute=true
        self.editWidth: Optional[String] = None

        # Name of the file that should be displayed. This attribute is supported in ASAM FSX and kept in AUTOSAR in order to support cut and paste. Tags: xml.attribute=true
        self.filename: Optional[String] = None

        # It determines the way in which the graphic should be inserted. Enter the attribute value "AS-IS" , to insert a graphic in its original dimensions. The graphic is adapted, if it is too big for the space for which it was intended. Default is "AS-IS" Tags: xml.attribute=true
        self.fit: Optional[GraphicFitEnum] = None

        # This attribute specifies the generator which is used to generate the image. Use case is that when editing a documentation, a figure (to be delivered by the modeling tool) is inserted by the authoring tool as reference (this is the role of graphic). But the real figure maybe injected during document processing. To be able to recognize this situation, this attribute can be applied. Tags: xml.attribute=true
        self.generator: Optional[NameToken] = None

        # Define the displayed height of the figure. The unit can be added to the number in the string. Possible units are: cm, mm, px, pt. The default unit is px. Tags: xml.attribute=true
        self.height: Optional[String] = None

        # How to fit the graphic in an online media. Default is AS-IS. Tags: xml.attribute=true
        self.htmlFit: Optional[GraphicFitEnum] = None

        # Specifies the height of the graphic when it is displayed online. The unit can be added to the number in the string. Possible units are: cm, mm, px, pt. The default unit is px. Tags: xml.attribute=true
        self.htmlHeight: Optional[String] = None

        # Set the proportional scale when displayed online. Tags: xml.attribute=true
        self.htmlScale: Optional[String] = None

        # Specifies the width of the graphic when it is displayed online. The unit can be added to the number in the string. Possible units are: cm, mm, px, pt. The default unit is px. Tags: xml.attribute=true
        self.htmlWidth: Optional[String] = None

        # This attribute captures the format used to represent the graphic. Tags: xml.attribute=true
        self.notation: Optional[GraphicNotationEnum] = None

        # In this element the dimensions of the graphic can be altered proportionally. Tags: xml.attribute=true
        self.scale: Optional[String] = None

        # Define the displayed width of the figure. The unit can be added to the number in the string. Possible units are: cm, mm, px, pt. The default unit is px. Tags: xml.attribute=true
        self.width: Optional[String] = None

    def getEditfit(self) -> Optional[GraphicFitEnum]:
        """
        Specifies how the graphic shall be displayed in an editor. If the attribute is missing, Tags: xml.attribute=true
        """
        return self.editfit

    def setEditfit(self, value: Optional[GraphicFitEnum]) -> "Graphic":
        """
        Specifies how the graphic shall be displayed in an editor. If the attribute is missing, Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing editfit.
        """
        if value is not None:
            self.editfit = value
        return self

    def getEditHeight(self) -> Optional[String]:
        """
        Specifies the height of the graphic when it is displayed in an editor. The unit can be added to the number in the string. Possible units are: cm, mm, px, pt. The default unit is px. Tags: xml.attribute=true
        """
        return self.editHeight

    def setEditHeight(self, value: Optional[String]) -> "Graphic":
        """
        Specifies the height of the graphic when it is displayed in an editor. The unit can be added to the number in the string. Possible units are: cm, mm, px, pt. The default unit is px. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing editHeight.
        """
        if value is not None:
            self.editHeight = value
        return self

    def getEditscale(self) -> Optional[String]:
        """
        Set the proportional scale when displayed in an editor. Tags: xml.attribute=true
        """
        return self.editscale

    def setEditscale(self, value: Optional[String]) -> "Graphic":
        """
        Set the proportional scale when displayed in an editor. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing editscale.
        """
        if value is not None:
            self.editscale = value
        return self

    def getEditWidth(self) -> Optional[String]:
        """
        Specifies the width of the graphic when it is displayed in an editor. The unit can be added to the number in the string. Possible units are: cm, mm, px, pt. The default unit is px. Tags: xml.attribute=true
        """
        return self.editWidth

    def setEditWidth(self, value: Optional[String]) -> "Graphic":
        """
        Specifies the width of the graphic when it is displayed in an editor. The unit can be added to the number in the string. Possible units are: cm, mm, px, pt. The default unit is px. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing editWidth.
        """
        if value is not None:
            self.editWidth = value
        return self

    def getFilename(self) -> Optional[String]:
        """
        Name of the file that should be displayed. This attribute is supported in ASAM FSX and kept in AUTOSAR in order to support cut and paste. Tags: xml.attribute=true
        """
        return self.filename

    def setFilename(self, value: Optional[String]) -> "Graphic":
        """
        Name of the file that should be displayed. This attribute is supported in ASAM FSX and kept in AUTOSAR in order to support cut and paste. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing filename.
        """
        if value is not None:
            self.filename = value
        return self

    def getFit(self) -> Optional[GraphicFitEnum]:
        """
        It determines the way in which the graphic should be inserted. Enter the attribute value "AS-IS" , to insert a graphic in its original dimensions. The graphic is adapted, if it is too big for the space for which it was intended. Default is "AS-IS" Tags: xml.attribute=true
        """
        return self.fit

    def setFit(self, value: Optional[GraphicFitEnum]) -> "Graphic":
        """
        It determines the way in which the graphic should be inserted. Enter the attribute value "AS-IS" , to insert a graphic in its original dimensions. The graphic is adapted, if it is too big for the space for which it was intended. Default is "AS-IS" Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing fit.
        """
        if value is not None:
            self.fit = value
        return self

    def getGenerator(self) -> Optional[NameToken]:
        """
        This attribute specifies the generator which is used to generate the image. Use case is that when editing a documentation, a figure (to be delivered by the modeling tool) is inserted by the authoring tool as reference (this is the role of graphic). But the real figure maybe injected during document processing. To be able to recognize this situation, this attribute can be applied. Tags: xml.attribute=true
        """
        return self.generator

    def setGenerator(self, value: Optional[NameToken]) -> "Graphic":
        """
        This attribute specifies the generator which is used to generate the image. Use case is that when editing a documentation, a figure (to be delivered by the modeling tool) is inserted by the authoring tool as reference (this is the role of graphic). But the real figure maybe injected during document processing. To be able to recognize this situation, this attribute can be applied. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing generator.
        """
        if value is not None:
            self.generator = value
        return self

    def getHeight(self) -> Optional[String]:
        """
        Define the displayed height of the figure. The unit can be added to the number in the string. Possible units are: cm, mm, px, pt. The default unit is px. Tags: xml.attribute=true
        """
        return self.height

    def setHeight(self, value: Optional[String]) -> "Graphic":
        """
        Define the displayed height of the figure. The unit can be added to the number in the string. Possible units are: cm, mm, px, pt. The default unit is px. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing height.
        """
        if value is not None:
            self.height = value
        return self

    def getHtmlFit(self) -> Optional[GraphicFitEnum]:
        """
        How to fit the graphic in an online media. Default is AS-IS. Tags: xml.attribute=true
        """
        return self.htmlFit

    def setHtmlFit(self, value: Optional[GraphicFitEnum]) -> "Graphic":
        """
        How to fit the graphic in an online media. Default is AS-IS. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing htmlFit.
        """
        if value is not None:
            self.htmlFit = value
        return self

    def getHtmlHeight(self) -> Optional[String]:
        """
        Specifies the height of the graphic when it is displayed online. The unit can be added to the number in the string. Possible units are: cm, mm, px, pt. The default unit is px. Tags: xml.attribute=true
        """
        return self.htmlHeight

    def setHtmlHeight(self, value: Optional[String]) -> "Graphic":
        """
        Specifies the height of the graphic when it is displayed online. The unit can be added to the number in the string. Possible units are: cm, mm, px, pt. The default unit is px. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing htmlHeight.
        """
        if value is not None:
            self.htmlHeight = value
        return self

    def getHtmlScale(self) -> Optional[String]:
        """
        Set the proportional scale when displayed online. Tags: xml.attribute=true
        """
        return self.htmlScale

    def setHtmlScale(self, value: Optional[String]) -> "Graphic":
        """
        Set the proportional scale when displayed online. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing htmlScale.
        """
        if value is not None:
            self.htmlScale = value
        return self

    def getHtmlWidth(self) -> Optional[String]:
        """
        Specifies the width of the graphic when it is displayed online. The unit can be added to the number in the string. Possible units are: cm, mm, px, pt. The default unit is px. Tags: xml.attribute=true
        """
        return self.htmlWidth

    def setHtmlWidth(self, value: Optional[String]) -> "Graphic":
        """
        Specifies the width of the graphic when it is displayed online. The unit can be added to the number in the string. Possible units are: cm, mm, px, pt. The default unit is px. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing htmlWidth.
        """
        if value is not None:
            self.htmlWidth = value
        return self

    def getNotation(self) -> Optional[GraphicNotationEnum]:
        """
        This attribute captures the format used to represent the graphic. Tags: xml.attribute=true
        """
        return self.notation

    def setNotation(self, value: Optional[GraphicNotationEnum]) -> "Graphic":
        """
        This attribute captures the format used to represent the graphic. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing notation.
        """
        if value is not None:
            self.notation = value
        return self

    def getScale(self) -> Optional[String]:
        """
        In this element the dimensions of the graphic can be altered proportionally. Tags: xml.attribute=true
        """
        return self.scale

    def setScale(self, value: Optional[String]) -> "Graphic":
        """
        In this element the dimensions of the graphic can be altered proportionally. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing scale.
        """
        if value is not None:
            self.scale = value
        return self

    def getWidth(self) -> Optional[String]:
        """
        Define the displayed width of the figure. The unit can be added to the number in the string. Possible units are: cm, mm, px, pt. The default unit is px. Tags: xml.attribute=true
        """
        return self.width

    def setWidth(self, value: Optional[String]) -> "Graphic":
        """
        Define the displayed width of the figure. The unit can be added to the number in the string. Possible units are: cm, mm, px, pt. The default unit is px. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing width.
        """
        if value is not None:
            self.width = value
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
