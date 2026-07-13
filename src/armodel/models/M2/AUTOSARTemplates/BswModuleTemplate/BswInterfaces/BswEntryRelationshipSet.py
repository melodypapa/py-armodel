"""
This module defines BSW entry relationship set in AUTOSAR.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class BswEntryRelationshipSet(ARObject):
    """
    Represents a set of BSW entry relationships in AUTOSAR.
    """
    # BswEntryRelationshipSet method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test
    # [ ] addRelationship              [x] impl  [ ] docstring  [ ] test
    # [ ] getRelationships             [x] impl  [ ] docstring  [ ] test


    def __init__(self):
        """
        Initializes the BswEntryRelationshipSet with default values.
        """
        super().__init__()
        self.relationships = []

    def addRelationship(self, relationship):
        self.relationships.append(relationship)

    def getRelationships(self):
        return self.relationships
