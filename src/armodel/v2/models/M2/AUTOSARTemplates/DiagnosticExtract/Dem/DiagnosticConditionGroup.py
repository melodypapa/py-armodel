from abc import ABC


class DiagnosticConditionGroup(DiagnosticCommonElement, ABC):
    """
    Abstract element for StorageConditionGroups and EnableConditionGroups.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticConditionGroup::DiagnosticConditionGroup

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 200, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is DiagnosticConditionGroup:
            raise TypeError("DiagnosticConditionGroup is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
