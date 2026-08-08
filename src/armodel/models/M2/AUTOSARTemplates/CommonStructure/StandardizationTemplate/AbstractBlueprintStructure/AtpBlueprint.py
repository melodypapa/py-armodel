"""
This module contains the AtpBlueprint abstract class for AUTOSAR models
in the CommonStructure module.
"""

from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable


class AtpBlueprint(Identifiable, ABC):
    """
    This meta-class represents the ability to act as a Blueprint. As this
    class is an abstract one, particular blueprint meta-classes inherit from
    this one.
    """

    # AtpBlueprint method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table D.11, p.305
    # [ ] __init__                     [ ] impl  [ ] docstring  [ ] test
    # [ ] addBlueprintPolicy           [ ] impl  [ ] docstring  [ ] test
    # [ ] getBlueprintPolicys          [ ] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AtpBlueprint:
            raise TypeError("AtpBlueprint is an abstract class.")
        super().__init__(parent, short_name)

        # This role indicates whether the blueprintable element will be
        # modifiable or not modifiable.
        # Spec type: BlueprintPolicy (abstract, not yet implemented); carried
        # as a List[ARObject] placeholder. See deviation tracker "class not
        # yet implemented".
        self.blueprintPolicys: List[ARObject] = []

    def addBlueprintPolicy(self, value: Optional[ARObject]) -> "AtpBlueprint":
        """
        Adds a BlueprintPolicy (spec type, not yet implemented; carried as an
        ARObject placeholder) that indicates whether the blueprintable
        element will be modifiable or not modifiable. A None value is a no-op
        and does not append to blueprintPolicys.
        """
        if value is not None:
            self.blueprintPolicys.append(value)
        return self

    def getBlueprintPolicys(self) -> List[ARObject]:
        """
        Gets the BlueprintPolicys (spec type, not yet implemented; carried as
        ARObject placeholders) that indicate whether the blueprintable
        elements will be modifiable or not modifiable.
        """
        return self.blueprintPolicys
