from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.Authentication import (
    DiagnosticAuthentication,
)


class DiagnosticVerifyCertificateBidirectional(DiagnosticAuthentication):
    """
    This meta-class represents the subfunction to do a bidirectional
    verification of the certificate.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::Authentication

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 99, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
