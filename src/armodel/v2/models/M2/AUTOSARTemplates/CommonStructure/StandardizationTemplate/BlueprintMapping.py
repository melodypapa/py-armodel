"""
AUTOSAR Package - BlueprintMapping

Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::BlueprintMapping
"""

from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)


class BlueprintMappingSet(ARElement):
    """
    This represents a container of mappings between "actual" model elements and
    the "blueprint" that has been taken for their creation.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::BlueprintMapping::BlueprintMappingSet

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 48, Foundation R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 34, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents a particular blueprint map in the set.
        self._blueprintMap: List[RefType] = []

    @property
    def blueprint_map(self) -> List[RefType]:
        """Get blueprintMap (Pythonic accessor)."""
        return self._blueprintMap

    def with_blueprint_map(self, value):
        """
        Set blueprint_map and return self for chaining.

        Args:
            value: The blueprint_map to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_blueprint_map("value")
        """
        self.blueprint_map = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBlueprintMap(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for blueprintMap.

        Returns:
            The blueprintMap value

        Note:
            Delegates to blueprint_map property (CODING_RULE_V2_00017)
        """
        return self.blueprint_map  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
