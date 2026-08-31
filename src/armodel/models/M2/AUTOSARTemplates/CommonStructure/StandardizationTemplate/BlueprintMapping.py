from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import (
    AtpBlueprintMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

__all__ = ["BlueprintMappingSet", "BlueprintMapping"]


class BlueprintMapping(AtpBlueprintMapping):
    """
    This meta-class represents the ability to map two an object and its blueprint.
    """

    def __init__(self):
        super().__init__()


class BlueprintMappingSet(ARElement):
    """
    This represents a container of mappings between "actual" model elements and the "blueprint" that has been taken for their creation.
    """

    # BlueprintMappingSet method parity checklist:
    # Spec: R23-11/AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 3.1, p.48 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addBlueprintMap      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getBlueprintMaps     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents a particular blueprint map in the set.
        self.blueprintMaps: List[AtpBlueprintMapping] = []

    def addBlueprintMap(self, value: Optional[AtpBlueprintMapping]) -> "BlueprintMappingSet":
        """
        This represents a particular blueprint map in the set. A None value is a no-op and is not added.
        """
        if value is not None:
            self.blueprintMaps.append(value)
        return self

    def getBlueprintMaps(self) -> List[AtpBlueprintMapping]:
        """
        This represents a particular blueprint map in the set.
        """
        return self.blueprintMaps
