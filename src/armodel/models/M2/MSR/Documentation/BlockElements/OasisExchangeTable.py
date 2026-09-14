from __future__ import annotations

from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, AREnum, String


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

    def setAlign(self, value: Optional[AlignEnum]) -> "Colspec":
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

    def setColname(self, value: Optional[String]) -> "Colspec":
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

    def setColnum(self, value: Optional[String]) -> "Colspec":
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

    def setColsep(self, value: Optional[TableSeparatorString]) -> "Colspec":
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

    def setColwidth(self, value: Optional[String]) -> "Colspec":
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

    def setRowsep(self, value: Optional[TableSeparatorString]) -> "Colspec":
        """
        Indicates whether a line should be displayed at the bottom end of the cells of the column defined in the Colspec. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing rowsep.
        """
        if value is not None:
            self.rowsep = value
        return self
