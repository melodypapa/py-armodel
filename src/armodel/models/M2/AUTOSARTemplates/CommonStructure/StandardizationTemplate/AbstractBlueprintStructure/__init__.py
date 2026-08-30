"""
This module contains the AbstractBlueprintStructure package classes for AUTOSAR models.
"""

from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import PackageableElement


class AtpBlueprintable(PackageableElement, ABC):
    """
    Abstract base class for AUTOSAR Template (ATP) blueprintable elements.

    AtpBlueprintable represents elements that can be used as blueprints in the AUTOSAR
    template system. These elements provide reusable definitions that can be instantiated
    or referenced in the model.

    This class extends Identifiable with blueprint-specific functionality for managing
    template-based elements in AUTOSAR models.

    Note:
        This is an abstract class and cannot be instantiated directly.
        Concrete implementations include BswModuleEntry, CompuMethod, DataConstr,
        and other blueprintable AUTOSAR elements.
    """

    # AtpBlueprintable method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AtpBlueprintable:
            raise TypeError("AtpBlueprintable is an abstract class.")
        super().__init__(parent, short_name)


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


class AtpBlueprintMapping(ARObject, ABC):
    """
    Abstract base class for AUTOSAR Template (ATP) blueprint mapping elements.

    AtpBlueprintMapping represents mapping elements in the AUTOSAR system that
    define relationships between blueprints and their implementations or instances.
    Mappings provide the mechanism to connect abstract blueprint definitions
    with concrete implementations.

    This class extends ARObject with mapping-specific functionality for managing
    blueprint mapping relationships.

    Note:
        This is an abstract class and cannot be instantiated directly.
        AtpBlueprintMapping is the parent of various AUTOSAR mapping elements:
        - BlueprintMapping (generic blueprint to implementation mapping)

    Attributes:
        Inherits all attributes from ARObject including uuid and adminData.
    """

    # AtpBlueprintMapping method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        if type(self) is AtpBlueprintMapping:
            raise TypeError("AtpBlueprintMapping is an abstract class.")
        super().__init__()


__all__ = ["AtpBlueprintable", "AtpBlueprint", "AtpBlueprintMapping"]
