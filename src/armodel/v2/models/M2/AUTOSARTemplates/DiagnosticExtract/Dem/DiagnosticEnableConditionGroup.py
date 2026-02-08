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
