from typing import List


class DiagnosticIumprDenominatorGroup(DiagnosticCommonElement):
    """
    This meta-class represents the ability to model a IUMPR denominator groups.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticEvent::DiagnosticIumprDenominatorGroup

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 211, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference collects DiagnosticIumpr to a Diagnostic.
        self._iumpr: List["DiagnosticIumpr"] = []

    @property
    def iumpr(self) -> List["DiagnosticIumpr"]:
        """Get iumpr (Pythonic accessor)."""
        return self._iumpr

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIumpr(self) -> List["DiagnosticIumpr"]:
        """
        AUTOSAR-compliant getter for iumpr.

        Returns:
            The iumpr value

        Note:
            Delegates to iumpr property (CODING_RULE_V2_00017)
        """
        return self.iumpr  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
