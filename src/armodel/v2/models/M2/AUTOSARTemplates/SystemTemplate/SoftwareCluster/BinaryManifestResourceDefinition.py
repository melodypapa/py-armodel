from typing import List

from armodel.v2.models.M2.AUTOSARTemplates import BinaryManifestItem
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class BinaryManifestResourceDefinition(Identifiable):
    """
    This meta-class represents the ability to specify a resource definition that
    provides information that can be shared by all resources that refer to the
    respective resource definition.

    Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster::BinaryManifest::BinaryManifestResourceDefinition

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 917, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This aggregation specifies the collection of handle definitions in the
        # context of the enclosing binary manifest.
        self._itemDefinition: List["BinaryManifestItem"] = []

    @property
    def item_definition(self) -> List["BinaryManifestItem"]:
        """Get itemDefinition (Pythonic accessor)."""
        return self._itemDefinition

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getItemDefinition(self) -> List["BinaryManifestItem"]:
        """
        AUTOSAR-compliant getter for itemDefinition.

        Returns:
            The itemDefinition value

        Note:
            Delegates to item_definition property (CODING_RULE_V2_00017)
        """
        return self.item_definition  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
