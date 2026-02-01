"""
This module contains the AtpBlueprint abstract class for AUTOSAR models
in the CommonStructure module.
"""

from abc import ABC
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable


class AtpBlueprint(Identifiable, ABC):
    """
    Abstract base class for AUTOSAR Template (ATP) blueprint elements.
    
    AtpBlueprint represents blueprint elements in the AUTOSAR system. Blueprints
    provide reusable definitions that can be used as templates for creating
    specific instances or mappings in AUTOSAR models.
    
    This class extends Identifiable with blueprint-specific functionality for
    managing template-based elements.
    
    Note:
        This is an abstract class and cannot be instantiated directly.
        Concrete implementations include ClientServerInterfaceToBswModuleEntryBlueprintMapping.
    
    Attributes:
        Inherits all attributes from Identifiable including shortName and adminData.
    """
    
    def __init__(self, parent, short_name: str):
        if type(self) is AtpBlueprint:
            raise TypeError("AtpBlueprint is an abstract class.")
        super().__init__(parent, short_name)