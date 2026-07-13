from enum import Enum


class RptAccessEnum(Enum):
    """
    Enumeration for RPT (Read-Protect-Transform) access types in AUTOSAR.
    Defines different access modes for read-protect-transform functionality.
    """
    # RptAccessEnum method parity checklist:
    # (no methods)


    ENUM_READ = "read"
    ENUM_READ_WRITE = "read-write"
    ENUM_WRITE = "write"
