from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    CryptoService,
    DiagnosticAuthTransmit,
    DiagnosticMapping,
)


class DiagnosticAuthTransmitCertificateMapping(DiagnosticMapping):
    """
    This meta-class represents the ability to associate a
    CryptoServiceCertificate with a DiagnosticAuth CertificateEvaluation with
    the purpose to configure the evaluation of the certificate.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::DiagnosticAuthTransmitCertificateMapping

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 242, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference identifies the description of the applicable crypto
        # certificate.
        self._cryptoService: List["CryptoService"] = []

    @property
    def crypto_service(self) -> List["CryptoService"]:
        """Get cryptoService (Pythonic accessor)."""
        return self._cryptoService
        # This reference identifies the applicable DiagnosticAuth service instance (via
        # the aggregation role certificateEvaluation).
        self._serviceInstance: Optional["DiagnosticAuthTransmit"] = None

    @property
    def service_instance(self) -> Optional["DiagnosticAuthTransmit"]:
        """Get serviceInstance (Pythonic accessor)."""
        return self._serviceInstance

    @service_instance.setter
    def service_instance(self, value: Optional["DiagnosticAuthTransmit"]) -> None:
        """
        Set serviceInstance with validation.

        Args:
            value: The serviceInstance to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._serviceInstance = None
            return

        if not isinstance(value, DiagnosticAuthTransmit):
            raise TypeError(
                f"serviceInstance must be DiagnosticAuthTransmit or None, got {type(value).__name__}"
            )
        self._serviceInstance = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCryptoService(self) -> List["CryptoService"]:
        """
        AUTOSAR-compliant getter for cryptoService.

        Returns:
            The cryptoService value

        Note:
            Delegates to crypto_service property (CODING_RULE_V2_00017)
        """
        return self.crypto_service  # Delegates to property

    def getServiceInstance(self) -> "DiagnosticAuthTransmit":
        """
        AUTOSAR-compliant getter for serviceInstance.

        Returns:
            The serviceInstance value

        Note:
            Delegates to service_instance property (CODING_RULE_V2_00017)
        """
        return self.service_instance  # Delegates to property

    def setServiceInstance(self, value: "DiagnosticAuthTransmit") -> "DiagnosticAuthTransmitCertificateMapping":
        """
        AUTOSAR-compliant setter for serviceInstance with method chaining.

        Args:
            value: The serviceInstance to set

        Returns:
            self for method chaining

        Note:
            Delegates to service_instance property setter (gets validation automatically)
        """
        self.service_instance = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_service_instance(self, value: Optional["DiagnosticAuthTransmit"]) -> "DiagnosticAuthTransmitCertificateMapping":
        """
        Set serviceInstance and return self for chaining.

        Args:
            value: The serviceInstance to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_service_instance("value")
        """
        self.service_instance = value  # Use property setter (gets validation)
        return self
