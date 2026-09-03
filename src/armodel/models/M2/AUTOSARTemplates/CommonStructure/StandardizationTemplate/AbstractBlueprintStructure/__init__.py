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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import PackageableElement


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
    """This meta-class represents the ability to act as a Blueprint. As this class is an abstract one, particular blueprint meta-classes inherit from this one."""

    # AtpBlueprint method parity checklist:
    # Spec: R23-11/AUTOSAR_FO_TPS_StandardizationTemplate.pdf, Table C.12, p.161 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addBlueprintPolicy  [x] impl  [x] docstring  [x] test  [ ] reader  [—] writer  R23-11
    # [x] getBlueprintPolicys [x] impl  [x] docstring  [x] test  [—] reader  [ ] writer  R23-11
    # Marker withheld: BlueprintPolicy (member type, `*` aggr) is a Rule 0001.10 referenced-class
    # placeholder — not implemented in this repo — so the blueprintPolicy aggregation's reader/writer
    # (deferred, rows stay [ ]) and the `# Spec verified:` stamp are withheld until BlueprintPolicy lands.

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
        """This role indicates whether the blueprintable element will be modifiable or not modifiable. A None value is a no-op and does not append to blueprintPolicys."""
        if value is not None:
            self.blueprintPolicys.append(value)
        return self

    def getBlueprintPolicys(self) -> List[ARObject]:
        """This role indicates whether the blueprintable element will be modifiable or not modifiable."""
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
        Inherits all attributes from ARObject; uuid (Table 4.4) and adminData come from Identifiable.
    """

    # AtpBlueprintMapping method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        if type(self) is AtpBlueprintMapping:
            raise TypeError("AtpBlueprintMapping is an abstract class.")
        super().__init__()


__all__ = ["AtpBlueprintable", "AtpBlueprint", "AtpBlueprintMapping"]
