from typing import List
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement


class BswEntryRelationshipSet(ARElement):
    """
    Describes a set of relationships between two BswModuleEntrys.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces::BswEntryRelationshipSet

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 51, Classic
      Platform R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 51, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Relationship between two BswModuleEntrys.
        self._bswEntryRelationship: List["BswEntryRelationship"] = []

    @property
    def bsw_entry_relationship(self) -> List["BswEntryRelationship"]:
        """Get bswEntryRelationship (Pythonic accessor)."""
        return self._bswEntryRelationship

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBswEntryRelationship(self) -> List["BswEntryRelationship"]:
        """
        AUTOSAR-compliant getter for bswEntryRelationship.

        Returns:
            The bswEntryRelationship value

        Note:
            Delegates to bsw_entry_relationship property (CODING_RULE_V2_00017)
        """
        return self.bsw_entry_relationship  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
