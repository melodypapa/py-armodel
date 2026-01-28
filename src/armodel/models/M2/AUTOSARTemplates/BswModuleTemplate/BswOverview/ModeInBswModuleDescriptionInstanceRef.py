"""
This module defines mode in BSW module description instance reference in AUTOSAR.
"""

from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class ModeInBswModuleDescriptionInstanceRef(RefType):
    """
    Represents a reference to a mode in BSW module description.
    """

    def __init__(self):
        """
        Initializes the ModeInBswModuleDescriptionInstanceRef.
        """
        super().__init__()