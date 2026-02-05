from enum import Enum


class SignalServiceTranslationControlEnum(Enum):
    """
    Enumeration for signal service translation control types in AUTOSAR.
    Defines different control modes for signal service translation.
    """

    ENUM_AUTOMATIC = "automatic"
    ENUM_MANUAL = "manual"