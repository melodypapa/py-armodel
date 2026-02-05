"""
This module contains enumeration classes for AUTOSAR models
in the GenericStructure module. These enumerations are used to specify
various configuration and behavior options throughout the AUTOSAR model.
"""

from enum import Enum


class AutoCollectEnum(Enum):
    """
    Enumeration for auto-collect settings in AUTOSAR collections.
    This enum defines the different auto-collection behaviors that can be applied to collections.
    """
    AUTO_COLLECT_OFF = "OFF"
    AUTO_COLLECT_ON = "ON"
    AUTO_COLLECT_AUTO = "AUTO"
