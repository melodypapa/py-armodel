"""
This module defines BSW mode manager error event in AUTOSAR.
"""

from .BswEvent import BswEvent


class BswModeManagerErrorEvent(BswEvent):
    """
    Represents a BSW mode manager error event in AUTOSAR.
    This event occurs when a mode manager error is detected.
    """

    def __init__(self):
        """
        Initializes the BswModeManagerErrorEvent with default values.
        """
        super().__init__()