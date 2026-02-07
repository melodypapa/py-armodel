from abc import ABC


class DiagnosticSwMapping(DiagnosticMapping, ABC):
    """
    This represents the ability to define a mapping between a diagnostic
    information (at this point there is no way to become more specific about the
    semantics) to a software-component.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::DiagnosticSwMapping

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 238, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is DiagnosticSwMapping:
            raise TypeError("DiagnosticSwMapping is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
