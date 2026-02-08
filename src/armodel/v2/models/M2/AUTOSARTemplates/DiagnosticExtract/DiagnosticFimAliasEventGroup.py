from typing import List
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent import DiagnosticAbstractAliasEvent


class DiagnosticFimAliasEventGroup(DiagnosticAbstractAliasEvent):
    """
    This meta-class represents the ability to define an alias for a Fim
    summarized event. This alias can be used in early phases of the
    configuration process until a further refinement is possible.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Fim::DiagnosticFimAliasEventGroup

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 263, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # By means of this reference the grouping of Diagnostic AliasEvents within the
        # DiagnosticFimSummaryEvent can.
        self._groupedAlias: List["DiagnosticFimAlias"] = []

    @property
    def grouped_alias(self) -> List["DiagnosticFimAlias"]:
        """Get groupedAlias (Pythonic accessor)."""
        return self._groupedAlias

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getGroupedAlias(self) -> List["DiagnosticFimAlias"]:
        """
        AUTOSAR-compliant getter for groupedAlias.

        Returns:
            The groupedAlias value

        Note:
            Delegates to grouped_alias property (CODING_RULE_V2_00017)
        """
        return self.grouped_alias  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
