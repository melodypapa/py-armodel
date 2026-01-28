"""
This module defines BSW trigger direct implementation in AUTOSAR.
"""

from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum


class BswTriggerDirectImplementation(AREnum):
    """
    Enumeration for BSW trigger direct implementation.
    """

    NOT_ALLOWED = "not-allowed"
    ALLOWED = "allowed"

    def __init__(self):
        super().__init__((
            BswTriggerDirectImplementation.NOT_ALLOWED,
            BswTriggerDirectImplementation.ALLOWED,
        ))