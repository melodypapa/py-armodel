"""
This module contains the AbstractBlueprintStructure package classes for AUTOSAR models.
"""

from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
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


class BlueprintPolicy(ARObject, ABC):
    """This meta-class represents the ability to indicate whether blueprintable elements will be modifiable or not modifiable."""

    # BlueprintPolicy method parity checklist:
    # Spec: R23-11/AUTOSAR_FO_TPS_StandardizationTemplate.pdf, Table C.18, p.164 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAttributeName     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setAttributeName     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self):
        if type(self) is BlueprintPolicy:
            raise TypeError("BlueprintPolicy is an abstract class.")
        super().__init__()

        # This identifies the related attribute of a BlueprintPolicy. For navigation over the model a subset of xpath expressions is used.
        self.attributeName: Optional[String] = None

    def getAttributeName(self) -> Optional[String]:
        """This identifies the related attribute of a BlueprintPolicy. For navigation over the model a subset of xpath expressions is used."""
        return self.attributeName

    def setAttributeName(self, attributeName: Optional[String]) -> "BlueprintPolicy":
        """This identifies the related attribute of a BlueprintPolicy. For navigation over the model a subset of xpath expressions is used. A None value is a no-op and is not set."""
        if attributeName is not None:
            self.attributeName = attributeName
        return self


class AtpBlueprint(Identifiable, ABC):
    """This meta-class represents the ability to act as a Blueprint. As this class is an abstract one, particular blueprint meta-classes inherit from this one."""

    # AtpBlueprint method parity checklist:
    # Spec: R23-11/AUTOSAR_FO_TPS_StandardizationTemplate.pdf, Table C.12, p.161 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addBlueprintPolicy  [x] impl  [x] docstring  [x] test  [ ] reader  [—] writer  R23-11
    # [x] getBlueprintPolicys [x] impl  [x] docstring  [x] test  [—] reader  [ ] writer  R23-11
    # Marker withheld: the blueprintPolicy aggregation's reader/writer rows stay [ ]
    # because the concrete BlueprintPolicy subclasses (BlueprintPolicyModifiable,
    # BlueprintPolicyList, BlueprintPolicyNotModifiable, BlueprintPolicySingle) are
    # not yet synced — they own the BLUEPRINT-POLICY-LIST/-NOT-MODIFIABLE/-SINGLE
    # elements (and thus the attributeName coverage). BlueprintPolicy itself is now
    # implemented (R23-11 Table C.18); only the subtypes' reader/writer blocks the stamp.

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AtpBlueprint:
            raise TypeError("AtpBlueprint is an abstract class.")
        super().__init__(parent, short_name)

        # This role indicates whether the blueprintable element will be
        # modifiable or not modifiable.
        # Spec type: BlueprintPolicy (abstract, R23-11 Table C.18). The concrete
        # subtypes (BlueprintPolicyList/NotModifiable/Single) carry the actual XML
        # elements, so the aggregation is typed with the abstract base for now.
        self.blueprintPolicys: List[BlueprintPolicy] = []

    def addBlueprintPolicy(self, value: Optional[BlueprintPolicy]) -> "AtpBlueprint":
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


__all__ = ["AtpBlueprintable", "AtpBlueprint", "AtpBlueprintMapping", "BlueprintPolicy"]
