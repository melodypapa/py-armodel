"""
This module contains the AtpBlueprint abstract class for AUTOSAR models
in the CommonStructure module.
"""

from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


def _get_identifiable_base():
    """Lazy import of Identifiable to avoid circular import."""
    from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
        Identifiable,
    )
    return Identifiable


# Create a base class dynamically to avoid circular import at definition time
_Identifiable = cast(type, None)


class AtpBlueprintable(ABC):
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

    def __init__(self, parent: ARObject, short_name: str) -> None:
        if type(self) is AtpBlueprintable:
            raise TypeError("AtpBlueprintable is an abstract class.")
        # Lazy import to avoid circular dependency
        Identifiable = _get_identifiable_base()
        Identifiable.__init__(self, parent, short_name)


class AtpBlueprint(ABC):
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

    def __init__(self, parent, short_name: str) -> None:
        if type(self) is AtpBlueprint:
            raise TypeError("AtpBlueprint is an abstract class.")
        # Lazy import to avoid circular dependency
        Identifiable = _get_identifiable_base()
        Identifiable.__init__(self, parent, short_name)


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

    def __init__(self) -> None:
        if type(self) is AtpBlueprintMapping:
            raise TypeError("AtpBlueprintMapping is an abstract class.")
        super().__init__()
