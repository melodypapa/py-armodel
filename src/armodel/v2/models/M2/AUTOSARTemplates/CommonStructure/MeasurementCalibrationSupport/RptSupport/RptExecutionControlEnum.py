from enum import Enum


class RptExecutionControlEnum(Enum):

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass    """
    Enumeration for RPT execution control types in AUTOSAR.
    Defines different execution control modes for RPT functionality.
    """

    ENUM_ASYNCHRONOUS = "asynchronous"
    ENUM_SYNCHRONOUS = "synchronous"
