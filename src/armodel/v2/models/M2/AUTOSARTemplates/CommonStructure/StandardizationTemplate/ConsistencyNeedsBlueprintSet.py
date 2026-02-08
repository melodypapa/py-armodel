from typing import List

from armodel.v2.models.M2.AUTOSARTemplates import ConsistencyNeeds
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    ARElement,
)


class ConsistencyNeedsBlueprintSet(ARElement):
    """
    This meta class represents the ability to specify a set of blueprint for
    ConsistencyNeeds.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::Blueprint::ConsistencyNeedsBlueprintSet

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 179, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents a particular blueprint of consistency Note that it is
        # atpVariation.
        self._consistency: List["ConsistencyNeeds"] = []

    @property
    def consistency(self) -> List["ConsistencyNeeds"]:
        """Get consistency (Pythonic accessor)."""
        return self._consistency

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getConsistency(self) -> List["ConsistencyNeeds"]:
        """
        AUTOSAR-compliant getter for consistency.

        Returns:
            The consistency value

        Note:
            Delegates to consistency property (CODING_RULE_V2_00017)
        """
        return self.consistency  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
