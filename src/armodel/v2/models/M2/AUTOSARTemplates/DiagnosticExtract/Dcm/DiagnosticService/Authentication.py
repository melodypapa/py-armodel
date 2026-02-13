"""
AUTOSAR Package - Authentication

Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::Authentication
"""


from __future__ import annotations
from abc import ABC
from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService import (
    DiagnosticServiceClass,
    DiagnosticServiceInstance,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class DiagnosticAuthentication(DiagnosticServiceInstance, ABC):
    """
    This meta-class represents the ability to configure the usage of the UDS
    service Authentication in the Diagnostic extract.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::Authentication::DiagnosticAuthentication

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 98, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is DiagnosticAuthentication:
            raise TypeError("DiagnosticAuthentication is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the corresponding "class", i.
        # e.
        # this applicable sub-classes of DiagnosticService that affected by this
                # pattern implement the applicable "class"-role that substantiate reference.
        self._authentication: Optional["Diagnostic"] = None

    @property
    def authentication(self) -> Optional["Diagnostic"]:
        """Get authentication (Pythonic accessor)."""
        return self._authentication

    @authentication.setter
    def authentication(self, value: Optional["Diagnostic"]) -> None:
        """
        Set authentication with validation.

        Args:
            value: The authentication to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._authentication = None
            return

        if not isinstance(value, Diagnostic):
            raise TypeError(
                f"authentication must be Diagnostic or None, got {type(value).__name__}"
            )
        self._authentication = value

    def with_certificate(self, value):
        """
        Set certificate and return self for chaining.

        Args:
            value: The certificate to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_certificate("value")
        """
        self.certificate = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAuthentication(self) -> "Diagnostic":
        """
        AUTOSAR-compliant getter for authentication.

        Returns:
            The authentication value

        Note:
            Delegates to authentication property (CODING_RULE_V2_00017)
        """
        return self.authentication  # Delegates to property

    def setAuthentication(self, value: "Diagnostic") -> DiagnosticAuthentication:
        """
        AUTOSAR-compliant setter for authentication with method chaining.

        Args:
            value: The authentication to set

        Returns:
            self for method chaining

        Note:
            Delegates to authentication property setter (gets validation automatically)
        """
        self.authentication = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_authentication(self, value: Optional["Diagnostic"]) -> DiagnosticAuthentication:
        """
        Set authentication and return self for chaining.

        Args:
            value: The authentication to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_authentication("value")
        """
        self.authentication = value  # Use property setter (gets validation)
        return self



class DiagnosticAuthenticationClass(DiagnosticServiceClass):
    """
    This meta-class contains configuration shared by all instances of the
    Authentication diagnostic service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::Authentication::DiagnosticAuthenticationClass

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 99, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DiagnosticAuthTransmitCertificateEvaluation(Identifiable):
    """
    This meta-class represents the ability to configure a certificate evaluation
    in the context of a diagnostic authentication.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::Authentication::DiagnosticAuthTransmitCertificateEvaluation

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 101, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attributes represents the ID of the certificate.
        self._evaluationId: Optional[PositiveInteger] = None

    @property
    def evaluation_id(self) -> Optional[PositiveInteger]:
        """Get evaluationId (Pythonic accessor)."""
        return self._evaluationId

    @evaluation_id.setter
    def evaluation_id(self, value: Optional[PositiveInteger]) -> None:
        """
        Set evaluationId with validation.

        Args:
            value: The evaluationId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._evaluationId = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"evaluationId must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._evaluationId = value
        # evaluation ID.
        self._function: Optional[String] = None

    @property
    def function(self) -> Optional[String]:
        """Get function (Pythonic accessor)."""
        return self._function

    @function.setter
    def function(self, value: Optional[String]) -> None:
        """
        Set function with validation.

        Args:
            value: The function to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._function = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"function must be String or str or None, got {type(value).__name__}"
            )
        self._function = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEvaluationId(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for evaluationId.

        Returns:
            The evaluationId value

        Note:
            Delegates to evaluation_id property (CODING_RULE_V2_00017)
        """
        return self.evaluation_id  # Delegates to property

    def setEvaluationId(self, value: PositiveInteger) -> DiagnosticAuthTransmitCertificateEvaluation:
        """
        AUTOSAR-compliant setter for evaluationId with method chaining.

        Args:
            value: The evaluationId to set

        Returns:
            self for method chaining

        Note:
            Delegates to evaluation_id property setter (gets validation automatically)
        """
        self.evaluation_id = value  # Delegates to property setter
        return self

    def getFunction(self) -> String:
        """
        AUTOSAR-compliant getter for function.

        Returns:
            The function value

        Note:
            Delegates to function property (CODING_RULE_V2_00017)
        """
        return self.function  # Delegates to property

    def setFunction(self, value: String) -> DiagnosticAuthTransmitCertificateEvaluation:
        """
        AUTOSAR-compliant setter for function with method chaining.

        Args:
            value: The function to set

        Returns:
            self for method chaining

        Note:
            Delegates to function property setter (gets validation automatically)
        """
        self.function = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_evaluation_id(self, value: Optional[PositiveInteger]) -> DiagnosticAuthTransmitCertificateEvaluation:
        """
        Set evaluationId and return self for chaining.

        Args:
            value: The evaluationId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_evaluation_id("value")
        """
        self.evaluation_id = value  # Use property setter (gets validation)
        return self

    def with_function(self, value: Optional[String]) -> DiagnosticAuthTransmitCertificateEvaluation:
        """
        Set function and return self for chaining.

        Args:
            value: The function to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_function("value")
        """
        self.function = value  # Use property setter (gets validation)
        return self



class DiagnosticAuthenticationConfiguration(DiagnosticAuthentication):
    """
    This meta-class represents the subfunction to configure the authentication.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::Authentication::DiagnosticAuthenticationConfiguration

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 99, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DiagnosticVerifyCertificateBidirectional(DiagnosticAuthentication):
    """
    This meta-class represents the subfunction to do a bidirectional
    verification of the certificate.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::Authentication::DiagnosticVerifyCertificateBidirectional

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 99, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DiagnosticVerifyCertificateUnidirectional(DiagnosticAuthentication):
    """
    This meta-class represents the subfunction to do a unidirectional
    verification of the certificate.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::Authentication::DiagnosticVerifyCertificateUnidirectional

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 100, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DiagnosticDeAuthentication(DiagnosticAuthentication):
    """
    This meta-class represents the subfunction to remove the authentication

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::Authentication::DiagnosticDeAuthentication

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 100, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DiagnosticProofOfOwnership(DiagnosticAuthentication):
    """
    This meta-class represents the subfunction to provide proof of ownership.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::Authentication::DiagnosticProofOfOwnership

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 100, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



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
