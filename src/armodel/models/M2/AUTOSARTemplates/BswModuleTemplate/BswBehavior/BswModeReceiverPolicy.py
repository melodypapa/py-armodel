"""
This module defines BSW mode receiver policy in AUTOSAR.
"""

from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum


class BswModeReceiverPolicy(AREnum):
    """
    Enumeration for BSW mode receiver policy.
    """

    NONE = "none"
    IMMEDIATE = "immediate"
    DEFERRED = "deferred"

    def __init__(self):
        super().__init__((
            BswModeReceiverPolicy.NONE,
            BswModeReceiverPolicy.IMMEDIATE,
            BswModeReceiverPolicy.DEFERRED,
        ))