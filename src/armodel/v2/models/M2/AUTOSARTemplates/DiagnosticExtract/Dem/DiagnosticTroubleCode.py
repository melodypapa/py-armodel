from abc import ABC


class DiagnosticTroubleCode(DiagnosticCommonElement, ABC):
    """
    A diagnostic trouble code defines a unique identifier that is shown to the
    diagnostic tester.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticTroubleCode::DiagnosticTroubleCode

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 176, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is DiagnosticTroubleCode:
            raise TypeError("DiagnosticTroubleCode is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
