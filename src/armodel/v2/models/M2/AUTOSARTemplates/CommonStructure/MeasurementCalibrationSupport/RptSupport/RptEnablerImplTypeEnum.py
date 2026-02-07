from enum import Enum


class RptEnablerImplTypeEnum(Enum):
    """
    Enumeration for RPT enabler implementation types in AUTOSAR.
    Defines different implementation approaches for RPT enablers.
    """

    ENUM_EXTERNAL = "external"
    ENUM_INTERNAL = "internal"
