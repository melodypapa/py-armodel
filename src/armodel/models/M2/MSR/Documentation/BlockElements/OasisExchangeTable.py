from __future__ import annotations

from typing import List, Optional, TYPE_CHECKING

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, AREnum, Integer, NameToken, String
from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView import Paginateable

if TYPE_CHECKING:
    from armodel.models.M2.MSR.Documentation.BlockElements import Caption
    from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock


class FloatEnum(AREnum):
    """
    This enumerator specifies the policy how an objects floats on a page.
    """

    # FloatEnum method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.64, p.333
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on MultiLanguageVerbatim.float / Table.float
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # This indicates that a page formatter is allowed to float the table to optimize the pagination. This is for example supported by TeX. Tags: atp.EnumerationLiteralIndex=0
    FLOAT = "float"

    # This indicates that a page formatter is not allowed to float the object to optimize the pagination. Tags: atp.EnumerationLiteralIndex=1
    NO_FLOAT = "noFloat"

    def __init__(self):
        super().__init__(
            (
                FloatEnum.FLOAT,
                FloatEnum.NO_FLOAT,
            )
        )


class FrameEnum(AREnum):
    """
    This enumerator specifies the policy, where to place a frame border around the table.
    """

    # FrameEnum method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.65, p.334
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on Table.frame / MlFigure.frame (FRAME attribute)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # Borders all around the table Tags: atp.EnumerationLiteralIndex=0
    ALL = "ALL"

    # Border at the bottom of the table Tags: atp.EnumerationLiteralIndex=1
    BOTTOM = "BOTTOM"

    # No borders around the table Tags: atp.EnumerationLiteralIndex=2
    NONE = "NONE"

    # Borders at the sides of the table Tags: atp.EnumerationLiteralIndex=3
    SIDES = "SIDES"

    # Border at the top of the table Tags: atp.EnumerationLiteralIndex=4
    TOP = "TOP"

    # Borders at the top and bottom of the table Tags: atp.EnumerationLiteralIndex=5
    TOPBOT = "TOPBOT"

    def __init__(self):
        super().__init__(
            (
                FrameEnum.ALL,
                FrameEnum.BOTTOM,
                FrameEnum.NONE,
                FrameEnum.SIDES,
                FrameEnum.TOP,
                FrameEnum.TOPBOT,
            )
        )


class AlignEnum(AREnum):
    """
    This enumerator specifies horizontal alignment.
    """

    # AlignEnum method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.67, p.335
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on Colspec.align / Entry.align / Tgroup.align (ALIGN attribute)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # The content of the table is horizontally centered. Tags: atp.EnumerationLiteralIndex=0
    CENTER = "CENTER"

    # This indicates that the content of table cell shall be justified (rendered as a block where white-space is expanded such that all lines are filled up). Tags: atp.EnumerationLiteralIndex=1
    JUSTIFY = "JUSTIFY"

    # This indicates that the content of a table cell is left justified. Tags: atp.EnumerationLiteralIndex=2
    LEFT = "LEFT"

    # This indicates that the content of a table cell is left justified. Tags: atp.EnumerationLiteralIndex=3
    RIGHT = "RIGHT"

    def __init__(self):
        super().__init__(
            (
                AlignEnum.CENTER,
                AlignEnum.JUSTIFY,
                AlignEnum.LEFT,
                AlignEnum.RIGHT,
            )
        )


class ValignEnum(AREnum):
    """
    This enumerator specifies vertical alignment.
    """

    # ValignEnum method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.69, p.336
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on Entry.valign / Row.valign / Tbody.valign (VALIGN attribute)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # The contents of the table cell is bottom aligned. Tags: atp.EnumerationLiteralIndex=0
    BOTTOM = "BOTTOM"

    # The contents of the table is vertically centered. Tags: atp.EnumerationLiteralIndex=1
    MIDDLE = "MIDDLE"

    # The contents of the table cell is top aligned. Tags: atp.EnumerationLiteralIndex=2
    TOP = "TOP"

    def __init__(self):
        super().__init__(
            (
                ValignEnum.BOTTOM,
                ValignEnum.MIDDLE,
                ValignEnum.TOP,
            )
        )


class OrientEnum(AREnum):
    """
    Indicate whether a table should be represented as landscape or portrait.
    """

    # OrientEnum method parity checklist:
    # Spec: AUTOSAR_00052.xsd, simpleType ORIENT-ENUM--SIMPLE line 140997 (XSD-only; no own table in repo corpus)
    # XSD verified: AUTOSAR_00052.xsd
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on Table.orient (ORIENT attribute)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # This indicates that the table is rendered in landscape which results in turning the table 90 degree clockwise. Tags: atp.EnumerationLiteralIndex=0
    LAND = "LAND"

    # This indicates that the table is rendered in portrait, which is the regular text flow. Tags: atp.EnumerationLiteralIndex=1
    PORT = "PORT"

    def __init__(self):
        super().__init__(
            (
                OrientEnum.LAND,
                OrientEnum.PORT,
            )
        )


class PgwideEnum(AREnum):
    """
    This enumerator specifies, if the table shall be rendered across the entire page, even if it is placed in side-head layouts.
    """

    # PgwideEnum method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.93, p.348
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on MlFigure.pgwide / MultiLanguageVerbatim.pgwide
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # This indicates that the table shall be fit in the current text flow. Tags: atp.EnumerationLiteralIndex=0
    NO_PGWIDE = "noPgwide"

    # This indicates that the table may use the entire page width. This is in particular important in case of so called "side-head layouts" but also if the table is in a list or in a note. Tags: atp.EnumerationLiteralIndex=1
    PGWIDE = "pgwide"

    def __init__(self):
        super().__init__(
            (
                PgwideEnum.NO_PGWIDE,
                PgwideEnum.PGWIDE,
            )
        )


class TableSeparatorString(ARLiteral):
    """
    This represents the ability to denote a separator string within an OASIS exchange table. • 0 : no line is displayed • 1 : line is displayed

    Tags:
        * xml.xsd.customType=TABLE-SEPARATOR-STRING
        * xml.xsd.pattern=[0-1]
        * xml.xsd.type=string
    """

    # TableSeparatorString method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.72, p.337
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()


class Colspec(ARObject):
    """
    This meta-class represents the ability to specify the properties of a column in a table.
    """

    # Colspec method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table E.20, p.433
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAlign   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAlign   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getColname [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setColname [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getColnum  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setColnum  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getColsep  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setColsep  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getColwidth [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setColwidth [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRowsep  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRowsep  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()
        # Specifies how the cell entries shall be horizontally aligned within the specified column. Default is "LEFT" Tags: xml.attribute=true
        self.align: Optional[AlignEnum] = None

        # Specifies the name of the column. Tags: xml.attribute=true
        self.colname: Optional[String] = None

        # column number (allows to sort the columns). Tags: xml.attribute=true
        self.colnum: Optional[String] = None

        # Indicates whether a line should be displayed right of this column in the column specification. Tags: xml.attribute=true
        self.colsep: Optional[TableSeparatorString] = None

        # Width of the column. You can enter absolute values such as 4 cm, or relative values marked with * (e.g., 2* for column widths double those of other columns with 1*). The unit can be added to the number in the string. Possible units are: cm, mm, px, pt. Tags: xml.attribute=true
        self.colwidth: Optional[String] = None

        # Indicates whether a line should be displayed at the bottom end of the cells of the column defined in the Colspec. Tags: xml.attribute=true
        self.rowsep: Optional[TableSeparatorString] = None

    def getAlign(self) -> Optional[AlignEnum]:
        """
        Specifies how the cell entries shall be horizontally aligned within the specified column. Default is "LEFT" Tags: xml.attribute=true
        """
        return self.align

    def setAlign(self, value: Optional[AlignEnum]) -> Colspec:
        """
        Specifies how the cell entries shall be horizontally aligned within the specified column. Default is "LEFT" Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing align.
        """
        if value is not None:
            self.align = value
        return self

    def getColname(self) -> Optional[String]:
        """
        Specifies the name of the column. Tags: xml.attribute=true
        """
        return self.colname

    def setColname(self, value: Optional[String]) -> Colspec:
        """
        Specifies the name of the column. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing colname.
        """
        if value is not None:
            self.colname = value
        return self

    def getColnum(self) -> Optional[String]:
        """
        column number (allows to sort the columns). Tags: xml.attribute=true
        """
        return self.colnum

    def setColnum(self, value: Optional[String]) -> Colspec:
        """
        column number (allows to sort the columns). Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing colnum.
        """
        if value is not None:
            self.colnum = value
        return self

    def getColsep(self) -> Optional[TableSeparatorString]:
        """
        Indicates whether a line should be displayed right of this column in the column specification. Tags: xml.attribute=true
        """
        return self.colsep

    def setColsep(self, value: Optional[TableSeparatorString]) -> Colspec:
        """
        Indicates whether a line should be displayed right of this column in the column specification. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing colsep.
        """
        if value is not None:
            self.colsep = value
        return self

    def getColwidth(self) -> Optional[String]:
        """
        Width of the column. You can enter absolute values such as 4 cm, or relative values marked with * (e.g., 2* for column widths double those of other columns with 1*). The unit can be added to the number in the string. Possible units are: cm, mm, px, pt. Tags: xml.attribute=true
        """
        return self.colwidth

    def setColwidth(self, value: Optional[String]) -> Colspec:
        """
        Width of the column. You can enter absolute values such as 4 cm, or relative values marked with * (e.g., 2* for column widths double those of other columns with 1*). The unit can be added to the number in the string. Possible units are: cm, mm, px, pt. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing colwidth.
        """
        if value is not None:
            self.colwidth = value
        return self

    def getRowsep(self) -> Optional[TableSeparatorString]:
        """
        Indicates whether a line should be displayed at the bottom end of the cells of the column defined in the Colspec. Tags: xml.attribute=true
        """
        return self.rowsep

    def setRowsep(self, value: Optional[TableSeparatorString]) -> Colspec:
        """
        Indicates whether a line should be displayed at the bottom end of the cells of the column defined in the Colspec. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing rowsep.
        """
        if value is not None:
            self.rowsep = value
        return self


class Entry(ARObject):
    """
    This represents one particular table cell.
    """

    # Entry method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.71, p.337
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAlign           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAlign           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getBgcolor         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setBgcolor         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getColname         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setColname         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getColsep          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setColsep          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getEntryContents   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setEntryContents   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMorerows        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMorerows        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNameend         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNameend         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNamest          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setNamest          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRotate          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRotate          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRowsep          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRowsep          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSpanname        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSpanname        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getValign          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setValign          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Specifies how the cell ENTRY shall be horizontally aligned. Default is "LEFT" Tags: xml.attribute=true
        self.align: Optional[AlignEnum] = None

        # This allows to recommend a background color of the entry. It is specified bases on 6 digits RGB hex-code. Tags: xml.attribute=true
        self.bgcolor: Optional[String] = None

        # Indicate the name of the column, where the entry should appear. Tags: xml.attribute=true
        self.colname: Optional[String] = None

        # Indicates whether a line should be displayed end of this entry. Tags: xml.attribute=true
        self.colsep: Optional[TableSeparatorString] = None

        # This is the content of the TableEntry Tags: xml.roleElement=false xml.roleWrapperElement=false xml.typeElement=false xml.typeWrapperElement=false
        self.entryContents: Optional["DocumentationBlock"] = None

        # Number of additional rows. Default is "0" Tags: xml.attribute=true
        self.morerows: Optional[String] = None

        # When an entry spans multiple column this is the name of the last column. Tags: xml.attribute=true
        self.nameend: Optional[String] = None

        # When an entry spans multiple column this is the name of the first column. Tags: xml.attribute=true
        self.namest: Optional[String] = None

        # Indicates if the cellcontent shall be rotated. Default is 0; 1 would rotate the contents 90 degree counterclockwise. This attribute is defined by OASIS. Tags: xml.attribute=true
        self.rotate: Optional[String] = None

        # Indicates whether a line should be displayed at the bottom end of the cell. Tags: xml.attribute=true
        self.rowsep: Optional[TableSeparatorString] = None

        # Capture the name of entry merging multiple columns. Tags: xml.attribute=true
        self.spanname: Optional[String] = None

        # Indicates how the content of the cell shall be aligned. Default is inherited from row or tbody, otherwise "TOP" Tags: xml.attribute=true
        self.valign: Optional[ValignEnum] = None

    def getAlign(self) -> Optional[AlignEnum]:
        """
        Specifies how the cell ENTRY shall be horizontally aligned. Default is "LEFT" Tags: xml.attribute=true
        """
        return self.align

    def setAlign(self, value: Optional[AlignEnum]) -> Entry:
        """
        Specifies how the cell ENTRY shall be horizontally aligned. Default is "LEFT" Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing align.
        """
        if value is not None:
            self.align = value
        return self

    def getBgcolor(self) -> Optional[String]:
        """
        This allows to recommend a background color of the entry. It is specified bases on 6 digits RGB hex-code. Tags: xml.attribute=true
        """
        return self.bgcolor

    def setBgcolor(self, value: Optional[String]) -> Entry:
        """
        This allows to recommend a background color of the entry. It is specified bases on 6 digits RGB hex-code. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing bgcolor.
        """
        if value is not None:
            self.bgcolor = value
        return self

    def getColname(self) -> Optional[String]:
        """
        Indicate the name of the column, where the entry should appear. Tags: xml.attribute=true
        """
        return self.colname

    def setColname(self, value: Optional[String]) -> Entry:
        """
        Indicate the name of the column, where the entry should appear. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing colname.
        """
        if value is not None:
            self.colname = value
        return self

    def getColsep(self) -> Optional[TableSeparatorString]:
        """
        Indicates whether a line should be displayed end of this entry. Tags: xml.attribute=true
        """
        return self.colsep

    def setColsep(self, value: Optional[TableSeparatorString]) -> Entry:
        """
        Indicates whether a line should be displayed end of this entry. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing colsep.
        """
        if value is not None:
            self.colsep = value
        return self

    def getEntryContents(self) -> Optional["DocumentationBlock"]:
        """
        This is the content of the TableEntry Tags: xml.roleElement=false xml.roleWrapperElement=false xml.typeElement=false xml.typeWrapperElement=false
        """
        return self.entryContents

    def setEntryContents(self, value: Optional["DocumentationBlock"]) -> Entry:
        """
        This is the content of the TableEntry Tags: xml.roleElement=false xml.roleWrapperElement=false xml.typeElement=false xml.typeWrapperElement=false. A None value is a no-op and does not overwrite an existing entryContents.
        """
        if value is not None:
            self.entryContents = value
        return self

    def getMorerows(self) -> Optional[String]:
        """
        Number of additional rows. Default is "0" Tags: xml.attribute=true
        """
        return self.morerows

    def setMorerows(self, value: Optional[String]) -> Entry:
        """
        Number of additional rows. Default is "0" Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing morerows.
        """
        if value is not None:
            self.morerows = value
        return self

    def getNameend(self) -> Optional[String]:
        """
        When an entry spans multiple column this is the name of the last column. Tags: xml.attribute=true
        """
        return self.nameend

    def setNameend(self, value: Optional[String]) -> Entry:
        """
        When an entry spans multiple column this is the name of the last column. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing nameend.
        """
        if value is not None:
            self.nameend = value
        return self

    def getNamest(self) -> Optional[String]:
        """
        When an entry spans multiple column this is the name of the first column. Tags: xml.attribute=true
        """
        return self.namest

    def setNamest(self, value: Optional[String]) -> Entry:
        """
        When an entry spans multiple column this is the name of the first column. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing namest.
        """
        if value is not None:
            self.namest = value
        return self

    def getRotate(self) -> Optional[String]:
        """
        Indicates if the cellcontent shall be rotated. Default is 0; 1 would rotate the contents 90 degree counterclockwise. This attribute is defined by OASIS. Tags: xml.attribute=true
        """
        return self.rotate

    def setRotate(self, value: Optional[String]) -> Entry:
        """
        Indicates if the cellcontent shall be rotated. Default is 0; 1 would rotate the contents 90 degree counterclockwise. This attribute is defined by OASIS. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing rotate.
        """
        if value is not None:
            self.rotate = value
        return self

    def getRowsep(self) -> Optional[TableSeparatorString]:
        """
        Indicates whether a line should be displayed at the bottom end of the cell. Tags: xml.attribute=true
        """
        return self.rowsep

    def setRowsep(self, value: Optional[TableSeparatorString]) -> Entry:
        """
        Indicates whether a line should be displayed at the bottom end of the cell. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing rowsep.
        """
        if value is not None:
            self.rowsep = value
        return self

    def getSpanname(self) -> Optional[String]:
        """
        Capture the name of entry merging multiple columns. Tags: xml.attribute=true
        """
        return self.spanname

    def setSpanname(self, value: Optional[String]) -> Entry:
        """
        Capture the name of entry merging multiple columns. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing spanname.
        """
        if value is not None:
            self.spanname = value
        return self

    def getValign(self) -> Optional[ValignEnum]:
        """
        Indicates how the content of the cell shall be aligned. Default is inherited from row or tbody, otherwise "TOP" Tags: xml.attribute=true
        """
        return self.valign

    def setValign(self, value: Optional[ValignEnum]) -> Entry:
        """
        Indicates how the content of the cell shall be aligned. Default is inherited from row or tbody, otherwise "TOP" Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing valign.
        """
        if value is not None:
            self.valign = value
        return self


class Row(Paginateable):
    """
    This meta-class represents the ability to express one row in a table.
    """

    # Row method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.70, p.336
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addEntry     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getEntries   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getRowsep    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRowsep    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getValign    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setValign    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()
        # This represents one particular table cell. It is an entry in the table. Tags: xml.roleElement=true xml.roleWrapperElement=false xml.sequenceOffset=20 xml.typeElement=false xml.typeWrapperElement=false
        self.entries: List[Entry] = []

        # Indicates if by default a line should be displayed below the row. Tags: xml.attribute=true
        self.rowsep: Optional[TableSeparatorString] = None

        # Indicates how the cells in the rows shall be aligned. Default is inherited from tbody, otherwise it is "TOP" Tags: xml.attribute=true
        self.valign: Optional[ValignEnum] = None

    def addEntry(self, value: Entry) -> Row:
        """
        This represents one particular table cell. It is an entry in the table. Tags: xml.roleElement=true xml.roleWrapperElement=false xml.sequenceOffset=20 xml.typeElement=false xml.typeWrapperElement=false
        """
        self.entries.append(value)
        return self

    def getEntries(self) -> List[Entry]:
        """
        This represents one particular table cell. It is an entry in the table. Tags: xml.roleElement=true xml.roleWrapperElement=false xml.sequenceOffset=20 xml.typeElement=false xml.typeWrapperElement=false
        """
        return self.entries

    def getRowsep(self) -> Optional[TableSeparatorString]:
        """
        Indicates if by default a line should be displayed below the row. Tags: xml.attribute=true
        """
        return self.rowsep

    def setRowsep(self, value: Optional[TableSeparatorString]) -> Row:
        """
        Indicates if by default a line should be displayed below the row. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing rowsep.
        """
        if value is not None:
            self.rowsep = value
        return self

    def getValign(self) -> Optional[ValignEnum]:
        """
        Indicates how the cells in the rows shall be aligned. Default is inherited from tbody, otherwise it is "TOP" Tags: xml.attribute=true
        """
        return self.valign

    def setValign(self, value: Optional[ValignEnum]) -> Row:
        """
        Indicates how the cells in the rows shall be aligned. Default is inherited from tbody, otherwise it is "TOP" Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing valign.
        """
        if value is not None:
            self.valign = value
        return self


class Tbody(ARObject):
    """
    This meta-class represents a part within a table group. Such a part can be the table head, the table body or the table foot.
    """

    # Tbody method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.68, p.335
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addRow    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRows   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getValign [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setValign [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This is a particular row in a table. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=row, row.variationPoint.shortLabel vh.latestBindingTime=postBuild xml.roleElement=true xml.roleWrapperElement=false xml.sequenceOffset=20 xml.typeElement=false xml.typeWrapperElement=false
        self.rows: List[Row] = []

        # Indicates how the cells in the rows shall be aligned. Default is inherited from tbody, otherwise it is "TOP" Tags: xml.attribute=true
        self.valign: Optional[ValignEnum] = None

    def addRow(self, value: Row) -> Tbody:
        """
        This is a particular row in a table. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=row, row.variationPoint.shortLabel vh.latestBindingTime=postBuild xml.roleElement=true xml.roleWrapperElement=false xml.sequenceOffset=20 xml.typeElement=false xml.typeWrapperElement=false
        """
        self.rows.append(value)
        return self

    def getRows(self) -> List[Row]:
        """
        This is a particular row in a table. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=row, row.variationPoint.shortLabel vh.latestBindingTime=postBuild xml.roleElement=true xml.roleWrapperElement=false xml.sequenceOffset=20 xml.typeElement=false xml.typeWrapperElement=false
        """
        return self.rows

    def getValign(self) -> Optional[ValignEnum]:
        """
        Indicates how the cells in the rows shall be aligned. Default is inherited from tbody, otherwise it is "TOP" Tags: xml.attribute=true
        """
        return self.valign

    def setValign(self, value: Optional[ValignEnum]) -> Tbody:
        """
        Indicates how the cells in the rows shall be aligned. Default is inherited from tbody, otherwise it is "TOP" Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing valign.
        """
        if value is not None:
            self.valign = value
        return self


class Tgroup(ARObject):
    """
    This meta-class represents the ability to denote a table section.
    """

    # Tgroup method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.66, p.335
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAlign    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAlign    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCols     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCols     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getColsep   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setColsep   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addColspec  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getColspecs [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getRowsep   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRowsep   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTbody    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTbody    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTfoot    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTfoot    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getThead    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setThead    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Specifies how the cell entries shall be horizontally aligned within the specified TGROUP. Default is "LEFT" Tags: xml.attribute=true
        self.align: Optional[AlignEnum] = None

        # This attribute represents the number of columns in the table. Tags: xml.attribute=true
        self.cols: Optional[Integer] = None

        # Indicates if by default a line shall be drawn between the columns of this table group. Tags: xml.attribute=true
        self.colsep: Optional[TableSeparatorString] = None

        # This specifies one particular column specification in the table. There shall be one entry for each column. Tags: xml.roleElement=true xml.roleWrapperElement=false xml.sequenceOffset=20 xml.typeElement=false xml.typeWrapperElement=false
        self.colspecs: List[Colspec] = []

        # Indicates if by default a line shall be drawn at the bottom of the rows in this table group. Tags: xml.attribute=true
        self.rowsep: Optional[TableSeparatorString] = None

        # This is the main part of the table segment, called the table body. Tags: xml.sequenceOffset=60
        self.tbody: Optional[Tbody] = None

        # This represents the footer of the table segment. This segment is printed at the end of the table or before a page break. Tags: xml.sequenceOffset=50
        self.tfoot: Optional[Tbody] = None

        # This represents the heading of the table section. The heading is usually repeated at the beginning of each new page. Tags: xml.sequenceOffset=40
        self.thead: Optional[Tbody] = None

    def addColspec(self, value: Colspec) -> Tgroup:
        """
        This specifies one particular column specification in the table. There shall be one entry for each column. Tags: xml.roleElement=true xml.roleWrapperElement=false xml.sequenceOffset=20 xml.typeElement=false xml.typeWrapperElement=false
        """
        self.colspecs.append(value)
        return self

    def getColspecs(self) -> List[Colspec]:
        """
        This specifies one particular column specification in the table. There shall be one entry for each column. Tags: xml.roleElement=true xml.roleWrapperElement=false xml.sequenceOffset=20 xml.typeElement=false xml.typeWrapperElement=false
        """
        return self.colspecs

    def getAlign(self) -> Optional[AlignEnum]:
        """
        Specifies how the cell entries shall be horizontally aligned within the specified TGROUP. Default is "LEFT" Tags: xml.attribute=true
        """
        return self.align

    def setAlign(self, value: Optional[AlignEnum]) -> Tgroup:
        """
        Specifies how the cell entries shall be horizontally aligned within the specified TGROUP. Default is "LEFT" Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing align.
        """
        if value is not None:
            self.align = value
        return self

    def getCols(self) -> Optional[Integer]:
        """
        This attribute represents the number of columns in the table. Tags: xml.attribute=true
        """
        return self.cols

    def setCols(self, value: Optional[Integer]) -> Tgroup:
        """
        This attribute represents the number of columns in the table. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing cols.
        """
        if value is not None:
            self.cols = value
        return self

    def getColsep(self) -> Optional[TableSeparatorString]:
        """
        Indicates if by default a line shall be drawn between the columns of this table group. Tags: xml.attribute=true
        """
        return self.colsep

    def setColsep(self, value: Optional[TableSeparatorString]) -> Tgroup:
        """
        Indicates if by default a line shall be drawn between the columns of this table group. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing colsep.
        """
        if value is not None:
            self.colsep = value
        return self

    def getRowsep(self) -> Optional[TableSeparatorString]:
        """
        Indicates if by default a line shall be drawn at the bottom of the rows in this table group. Tags: xml.attribute=true
        """
        return self.rowsep

    def setRowsep(self, value: Optional[TableSeparatorString]) -> Tgroup:
        """
        Indicates if by default a line shall be drawn at the bottom of the rows in this table group. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing rowsep.
        """
        if value is not None:
            self.rowsep = value
        return self

    def getTbody(self) -> Optional[Tbody]:
        """
        This is the main part of the table segment, called the table body. Tags: xml.sequenceOffset=60
        """
        return self.tbody

    def setTbody(self, value: Optional[Tbody]) -> Tgroup:
        """
        This is the main part of the table segment, called the table body. Tags: xml.sequenceOffset=60. A None value is a no-op and does not overwrite an existing tbody.
        """
        if value is not None:
            self.tbody = value
        return self

    def getTfoot(self) -> Optional[Tbody]:
        """
        This represents the footer of the table segment. This segment is printed at the end of the table or before a page break. Tags: xml.sequenceOffset=50
        """
        return self.tfoot

    def setTfoot(self, value: Optional[Tbody]) -> Tgroup:
        """
        This represents the footer of the table segment. This segment is printed at the end of the table or before a page break. Tags: xml.sequenceOffset=50. A None value is a no-op and does not overwrite an existing tfoot.
        """
        if value is not None:
            self.tfoot = value
        return self

    def getThead(self) -> Optional[Tbody]:
        """
        This represents the heading of the table section. The heading is usually repeated at the beginning of each new page. Tags: xml.sequenceOffset=40
        """
        return self.thead

    def setThead(self, value: Optional[Tbody]) -> Tgroup:
        """
        This represents the heading of the table section. The heading is usually repeated at the beginning of each new page. Tags: xml.sequenceOffset=40. A None value is a no-op and does not overwrite an existing thead.
        """
        if value is not None:
            self.thead = value
        return self


class Table(Paginateable):
    """
    This class implements an exchange table according to OASIS Technical Resolution TR 9503:1995. http://www.oasis-open.org/specs/a503.htm
    """

    # Table method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.63, p.333
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getColsep      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setColsep      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getFloat       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFloat       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getFrame       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFrame       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getHelpEntry   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setHelpEntry   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getOrient      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setOrient      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPgwide      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPgwide      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRowsep      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRowsep      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTableCaption [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTableCaption [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTabstyle    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTabstyle    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addTgroup      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTgroups     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()

        # Indicates if by default a line should be drawn between the columns of this table. Tags: xml.attribute=true
        self.colsep: Optional[TableSeparatorString] = None

        # Indicate whether it is allowed to break the element. Tags: xml.attribute=true
        self.float: Optional[FloatEnum] = None

        # Used to defined the frame line around a table. Tags: xml.attribute=true
        self.frame: Optional[FrameEnum] = None

        # This specifies an entry point in an online help system to be linked with the parent class. The syntax shall be defined by the applied help system respectively help system generator. Tags: xml.attribute=true
        self.helpEntry: Optional[String] = None

        # Indicate whether a table should be represented as landscape or portrait. • land : landscape • port : portrait Tags: xml.attribute=true
        self.orient: Optional[OrientEnum] = None

        # Used to indicate whether the figure should take the complete page width (value = "pgwide") or not (value = "noPgwide"). Tags: xml.attribute=true
        self.pgwide: Optional[NameToken] = None

        # Indicates if by default a line should be drawn at the bottom of table rows. Tags: xml.attribute=true
        self.rowsep: Optional[TableSeparatorString] = None

        # This element specifies the table heading. Tags: xml.sequenceOffset=20
        self.tableCaption: Optional[Caption] = None

        # Indicates an external table style. Tags: xml.attribute=true
        self.tabstyle: Optional[NameToken] = None

        # A table can be built of individual segments. Such a segment is called tgroup. Tags: xml.roleElement=true xml.roleWrapperElement=false xml.sequenceOffset=30 xml.typeElement=false xml.typeWrapperElement=false
        self.tgroups: List[Tgroup] = []

    def addTgroup(self, value: Tgroup) -> Table:
        """
        A table can be built of individual segments. Such a segment is called tgroup. Tags: xml.roleElement=true xml.roleWrapperElement=false xml.sequenceOffset=30 xml.typeElement=false xml.typeWrapperElement=false
        """
        self.tgroups.append(value)
        return self

    def getTgroups(self) -> List[Tgroup]:
        """
        A table can be built of individual segments. Such a segment is called tgroup. Tags: xml.roleElement=true xml.roleWrapperElement=false xml.sequenceOffset=30 xml.typeElement=false xml.typeWrapperElement=false
        """
        return self.tgroups

    def getColsep(self) -> Optional[TableSeparatorString]:
        """
        Indicates if by default a line should be drawn between the columns of this table. Tags: xml.attribute=true
        """
        return self.colsep

    def setColsep(self, value: Optional[TableSeparatorString]) -> Table:
        """
        Indicates if by default a line should be drawn between the columns of this table. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing colsep.
        """
        if value is not None:
            self.colsep = value
        return self

    def getFloat(self) -> Optional[FloatEnum]:
        """
        Indicate whether it is allowed to break the element. Tags: xml.attribute=true
        """
        return self.float

    def setFloat(self, value: Optional[FloatEnum]) -> Table:
        """
        Indicate whether it is allowed to break the element. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing float.
        """
        if value is not None:
            self.float = value
        return self

    def getFrame(self) -> Optional[FrameEnum]:
        """
        Used to defined the frame line around a table. Tags: xml.attribute=true
        """
        return self.frame

    def setFrame(self, value: Optional[FrameEnum]) -> Table:
        """
        Used to defined the frame line around a table. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing frame.
        """
        if value is not None:
            self.frame = value
        return self

    def getHelpEntry(self) -> Optional[String]:
        """
        This specifies an entry point in an online help system to be linked with the parent class. The syntax shall be defined by the applied help system respectively help system generator. Tags: xml.attribute=true
        """
        return self.helpEntry

    def setHelpEntry(self, value: Optional[String]) -> Table:
        """
        This specifies an entry point in an online help system to be linked with the parent class. The syntax shall be defined by the applied help system respectively help system generator. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing helpEntry.
        """
        if value is not None:
            self.helpEntry = value
        return self

    def getOrient(self) -> Optional[OrientEnum]:
        """
        Indicate whether a table should be represented as landscape or portrait. • land : landscape • port : portrait Tags: xml.attribute=true
        """
        return self.orient

    def setOrient(self, value: Optional[OrientEnum]) -> Table:
        """
        Indicate whether a table should be represented as landscape or portrait. • land : landscape • port : portrait Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing orient.
        """
        if value is not None:
            self.orient = value
        return self

    def getPgwide(self) -> Optional[NameToken]:
        """
        Used to indicate whether the figure should take the complete page width (value = "pgwide") or not (value = "noPgwide"). Tags: xml.attribute=true
        """
        return self.pgwide

    def setPgwide(self, value: Optional[NameToken]) -> Table:
        """
        Used to indicate whether the figure should take the complete page width (value = "pgwide") or not (value = "noPgwide"). Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing pgwide.
        """
        if value is not None:
            self.pgwide = value
        return self

    def getRowsep(self) -> Optional[TableSeparatorString]:
        """
        Indicates if by default a line should be drawn at the bottom of table rows. Tags: xml.attribute=true
        """
        return self.rowsep

    def setRowsep(self, value: Optional[TableSeparatorString]) -> Table:
        """
        Indicates if by default a line should be drawn at the bottom of table rows. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing rowsep.
        """
        if value is not None:
            self.rowsep = value
        return self

    def getTableCaption(self) -> Optional[Caption]:
        """
        This element specifies the table heading. Tags: xml.sequenceOffset=20
        """
        return self.tableCaption

    def setTableCaption(self, value: Optional[Caption]) -> Table:
        """
        This element specifies the table heading. Tags: xml.sequenceOffset=20. A None value is a no-op and does not overwrite an existing tableCaption.
        """
        if value is not None:
            self.tableCaption = value
        return self

    def getTabstyle(self) -> Optional[NameToken]:
        """
        Indicates an external table style. Tags: xml.attribute=true
        """
        return self.tabstyle

    def setTabstyle(self, value: Optional[NameToken]) -> Table:
        """
        Indicates an external table style. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing tabstyle.
        """
        if value is not None:
            self.tabstyle = value
        return self
