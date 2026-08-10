from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum


class FloatEnum(AREnum):
    """
    This enumerator specifies the policy how an objects floats on a page.
    """

    # FloatEnum method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.64, p.333
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on MultiLanguageVerbatim.float / Table.float
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

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


class PgwideEnum(AREnum):
    """
    This enumerator specifies, if the table shall be rendered across the entire page, even if it is placed in side-head layouts.
    """

    # PgwideEnum method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.93, p.348
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on MlFigure.pgwide / MultiLanguageVerbatim.pgwide
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

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
