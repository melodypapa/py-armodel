"""
This module defines BSW entry relationship in AUTOSAR.
"""

from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class BswEntryRelationship(ARObject):
    """
    Represents a BSW entry relationship in AUTOSAR.
    This class defines relationships between BSW entries.
    """

    def __init__(self):
        """
        Initializes the BswEntryRelationship with default values.
        """
        super().__init__()
        self.relationType: str = None

    def getRelationType(self):
        return self.relationType

    def setRelationType(self, value):
        self.relationType = value
        return self