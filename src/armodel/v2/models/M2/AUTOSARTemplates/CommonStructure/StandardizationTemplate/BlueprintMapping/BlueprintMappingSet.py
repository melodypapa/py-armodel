from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class BlueprintMappingSet(ARObject):
    """
    Represents a set of blueprint mappings in AUTOSAR.
    Defines a collection of blueprint mappings.
    """

    def __init__(self):
        """
        Initializes the BlueprintMappingSet with default values.
        """
        super().__init__()
        self.mappings: List[str] = []

    def addMapping(self, mapping: str):
        """
        Adds a mapping to this set.

        Args:
            mapping: The mapping to add

        Returns:
            self for method chaining
        """
        self.mappings.append(mapping)
        return self

    def getMappings(self) -> List[str]:
        """
        Gets the list of mappings.

        Returns:
            List of mappings
        """
        return self.mappings
