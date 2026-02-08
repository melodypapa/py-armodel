from abc import ABC
from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class AtpBlueprint(Identifiable, ABC):
    """
    This meta-class represents the ability to act as a Blueprint. As this class
    is an abstract one, particular blueprint meta-classes inherit from this one.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::AbstractBlueprintStructure

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 305, Classic
      Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 424, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 161, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is AtpBlueprint:
            raise TypeError("AtpBlueprint is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This role indicates whether the blueprintable element will or not modifiable.
        self._blueprintPolicy: List["BlueprintPolicy"] = []

    @property
    def blueprint_policy(self) -> List["BlueprintPolicy"]:
        """Get blueprintPolicy (Pythonic accessor)."""
        return self._blueprintPolicy

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBlueprintPolicy(self) -> List["BlueprintPolicy"]:
        """
        AUTOSAR-compliant getter for blueprintPolicy.

        Returns:
            The blueprintPolicy value

        Note:
            Delegates to blueprint_policy property (CODING_RULE_V2_00017)
        """
        return self.blueprint_policy  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
