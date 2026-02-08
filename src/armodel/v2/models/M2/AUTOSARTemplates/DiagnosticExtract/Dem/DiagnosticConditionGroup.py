from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticConditionGroup import (
    DiagnosticConditionGroup,
)


class DiagnosticEnableConditionGroup(DiagnosticConditionGroup):
    """
    Enable condition group which includes one or several enable conditions.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticConditionGroup

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 200, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to enableConditions that are part of the Enable atpVariation.
        self._enableCondition: List["DiagnosticEnable"] = []

    @property
    def enable_condition(self) -> List["DiagnosticEnable"]:
        """Get enableCondition (Pythonic accessor)."""
        return self._enableCondition

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEnableCondition(self) -> List["DiagnosticEnable"]:
        """
        AUTOSAR-compliant getter for enableCondition.

        Returns:
            The enableCondition value

        Note:
            Delegates to enable_condition property (CODING_RULE_V2_00017)
        """
        return self.enable_condition  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticConditionGroup import (
    DiagnosticConditionGroup,
)


class DiagnosticStorageConditionGroup(DiagnosticConditionGroup):
    """
    Storage condition group which includes one or several storage conditions.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticConditionGroup

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
