from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum


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
