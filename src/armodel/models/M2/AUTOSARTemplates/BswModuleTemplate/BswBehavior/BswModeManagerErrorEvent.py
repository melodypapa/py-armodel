"""
This module defines BSW mode manager error event in AUTOSAR.
"""

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import BswEvent


class BswModeManagerErrorEvent(BswEvent):
    """
    Represents a BSW mode manager error event in AUTOSAR.
    This event occurs when a mode manager error is detected.
    """
    # BswModeManagerErrorEvent method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test


    def __init__(self):
        """
        Initializes the BswModeManagerErrorEvent with default values.
        """
        super().__init__()
