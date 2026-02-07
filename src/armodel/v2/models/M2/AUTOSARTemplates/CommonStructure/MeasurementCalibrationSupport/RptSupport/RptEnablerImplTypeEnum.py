from enum import Enum


class RptEnablerImplTypeEnum(Enum):

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass    """
    Enumeration for RPT enabler implementation types in AUTOSAR.
    Defines different implementation approaches for RPT enablers.
    """

    ENUM_EXTERNAL = "external"
    ENUM_INTERNAL = "internal"
