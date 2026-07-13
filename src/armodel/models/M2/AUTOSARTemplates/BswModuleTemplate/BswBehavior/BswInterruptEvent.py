"""
This module defines BSW interrupt event in AUTOSAR.
"""

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import BswEvent


class BswInterruptEvent(BswEvent):
    """
    Represents a BSW interrupt event in AUTOSAR.
    This event occurs when an interrupt is triggered.
    """
    # BswInterruptEvent method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test


    def __init__(self):
        """
        Initializes the BswInterruptEvent with default values.
        """
        super().__init__()
