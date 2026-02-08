from abc import ABC
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import DiagnosticCommonElement


class DiagnosticAbstractAliasEvent(DiagnosticCommonElement, ABC):
    """
    This meta-class represents an abstract base class for all diagnostic alias
    events.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticEvent::DiagnosticAbstractAliasEvent

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 214, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is DiagnosticAbstractAliasEvent:
            raise TypeError("DiagnosticAbstractAliasEvent is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
