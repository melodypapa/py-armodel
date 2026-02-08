from typing import List

from armodel.v2.models.M2.AUTOSARTemplates import (
    DiagnosticAuthentication,
    DiagnosticAuthTransmit,
)


class DiagnosticAuthTransmitCertificate(DiagnosticAuthentication):
    """
    This meta-class represents the sub-function to transmit a certificate

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::Authentication::DiagnosticAuthTransmitCertificate

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 100, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This aggregation represents a collection of certificate evaluation
        # configurations.
        self._certificate: List["DiagnosticAuthTransmit"] = []

    @property
    def certificate(self) -> List["DiagnosticAuthTransmit"]:
        """Get certificate (Pythonic accessor)."""
        return self._certificate

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCertificate(self) -> List["DiagnosticAuthTransmit"]:
        """
        AUTOSAR-compliant getter for certificate.

        Returns:
            The certificate value

        Note:
            Delegates to certificate property (CODING_RULE_V2_00017)
        """
        return self.certificate  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
