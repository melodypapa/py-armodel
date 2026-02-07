from enum import Enum


class RptPreparationEnum(Enum):

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass    """
    Enumeration for RPT preparation types in AUTOSAR.
    Defines different preparation modes for RPT functionality.
    """

    ENUM_PREPARED = "prepared"
    ENUM_UNPREPARED = "unprepared"
