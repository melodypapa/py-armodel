from typing import List
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import DiagnosticCommonElement


class DiagnosticFimEventGroup(DiagnosticCommonElement):
    """
    This meta-class represents the ability to model a Fim event group, also
    known as a summary event in Fim terminology. This represents a group of
    single diagnostic events.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Fim::DiagnosticFimEventGroup

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 217, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference represents the way of grouping diagnostic a summary event in
        # the context of the Fim.
        self._event: List["DiagnosticEvent"] = []

    @property
    def event(self) -> List["DiagnosticEvent"]:
        """Get event (Pythonic accessor)."""
        return self._event

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEvent(self) -> List["DiagnosticEvent"]:
        """
        AUTOSAR-compliant getter for event.

        Returns:
            The event value

        Note:
            Delegates to event property (CODING_RULE_V2_00017)
        """
        return self.event  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
