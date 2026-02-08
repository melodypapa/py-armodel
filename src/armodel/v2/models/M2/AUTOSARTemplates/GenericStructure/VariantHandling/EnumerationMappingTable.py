from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PackageableElement import (
    PackageableElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class EnumerationMappingTable(PackageableElement):
    """
    that this class might be used in the extended meta-model only.

    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling::AttributeValueVariationPoints

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 444, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Key-value pair mapping enumeration values to unique.
        self._entry: List[RefType] = []

    @property
    def entry(self) -> List[RefType]:
        """Get entry (Pythonic accessor)."""
        return self._entry

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEntry(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for entry.

        Returns:
            The entry value

        Note:
            Delegates to entry property (CODING_RULE_V2_00017)
        """
        return self.entry  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
