from typing import Optional


class DiagnosticRequestEmissionRelatedDTCPermanentStatus(DiagnosticServiceInstance):
    """
    This meta-class represents the ability to model an instance of the OBD mode
    0x0A service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::ObdService::Mode_0x0A_RequestEmissionRelated::DiagnosticRequestEmissionRelatedDTCPermanentStatus

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 161, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference substantiates that abstract reference in the role serviceClass
                # for this specific concrete class.
        # Thereby, the reference represents the ability to access Class shared
                # attributes among all DiagnosticRequestEmission Permanent
                # RelatedDTCPermanentStatus in the given context.
        # Status.
        self._request: Optional["DiagnosticRequest"] = None

    @property
    def request(self) -> Optional["DiagnosticRequest"]:
        """Get request (Pythonic accessor)."""
        return self._request

    @request.setter
    def request(self, value: Optional["DiagnosticRequest"]) -> None:
        """
        Set request with validation.

        Args:
            value: The request to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._request = None
            return

        if not isinstance(value, DiagnosticRequest):
            raise TypeError(
                f"request must be DiagnosticRequest or None, got {type(value).__name__}"
            )
        self._request = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRequest(self) -> "DiagnosticRequest":
        """
        AUTOSAR-compliant getter for request.

        Returns:
            The request value

        Note:
            Delegates to request property (CODING_RULE_V2_00017)
        """
        return self.request  # Delegates to property

    def setRequest(self, value: "DiagnosticRequest") -> "DiagnosticRequestEmissionRelatedDTCPermanentStatus":
        """
        AUTOSAR-compliant setter for request with method chaining.

        Args:
            value: The request to set

        Returns:
            self for method chaining

        Note:
            Delegates to request property setter (gets validation automatically)
        """
        self.request = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_request(self, value: Optional["DiagnosticRequest"]) -> "DiagnosticRequestEmissionRelatedDTCPermanentStatus":
        """
        Set request and return self for chaining.

        Args:
            value: The request to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_request("value")
        """
        self.request = value  # Use property setter (gets validation)
        return self
