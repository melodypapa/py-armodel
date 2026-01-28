"""
This module defines BSW exclusive area policy in AUTOSAR.
"""

from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum


class BswExclusiveAreaPolicy(AREnum):
    """
    Enumeration for BSW exclusive area policy.
    """

    NONE = "none"
    INTERNAL = "internal"
    EXTERNAL = "external"

    def __init__(self):
        super().__init__((
            BswExclusiveAreaPolicy.NONE,
            BswExclusiveAreaPolicy.INTERNAL,
            BswExclusiveAreaPolicy.EXTERNAL,
        ))