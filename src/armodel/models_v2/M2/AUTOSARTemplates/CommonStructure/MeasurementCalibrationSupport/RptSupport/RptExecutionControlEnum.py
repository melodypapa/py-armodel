from enum import Enum


class RptExecutionControlEnum(Enum):
    """
    Enumeration for RPT execution control types in AUTOSAR.
    Defines different execution control modes for RPT functionality.
    """

    ENUM_ASYNCHRONOUS = "asynchronous"
    ENUM_SYNCHRONOUS = "synchronous"