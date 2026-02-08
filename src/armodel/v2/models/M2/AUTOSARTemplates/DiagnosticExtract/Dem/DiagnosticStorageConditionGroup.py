from typing import List
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticConditionGroup import DiagnosticConditionGroup


class DiagnosticStorageConditionGroup(DiagnosticConditionGroup):
    """
    Storage condition group which includes one or several storage conditions.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticConditionGroup::DiagnosticStorageConditionGroup

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 200, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to storageConditions that are part of the StorageConditionGroup.
        # atpVariation.
        self._storage: List["DiagnosticStorage"] = []

    @property
    def storage(self) -> List["DiagnosticStorage"]:
        """Get storage (Pythonic accessor)."""
        return self._storage

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getStorage(self) -> List["DiagnosticStorage"]:
        """
        AUTOSAR-compliant getter for storage.

        Returns:
            The storage value

        Note:
            Delegates to storage property (CODING_RULE_V2_00017)
        """
        return self.storage  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
