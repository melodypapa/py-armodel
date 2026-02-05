from enum import Enum


class RptPreparationEnum(Enum):
    """
    Enumeration for RPT preparation types in AUTOSAR.
    Defines different preparation modes for RPT functionality.
    """

    ENUM_PREPARED = "prepared"
    ENUM_UNPREPARED = "unprepared"
