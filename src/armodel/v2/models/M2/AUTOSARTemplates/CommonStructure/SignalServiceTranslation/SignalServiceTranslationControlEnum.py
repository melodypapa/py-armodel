from enum import Enum


class SignalServiceTranslationControlEnum(Enum):

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass    """
    Enumeration for signal service translation control types in AUTOSAR.
    Defines different control modes for signal service translation.
    """

    ENUM_AUTOMATIC = "automatic"
    ENUM_MANUAL = "manual"
