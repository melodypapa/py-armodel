from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.MemoryByAddress import (
    DiagnosticMemoryAddressableRangeAccess,
)


class DiagnosticRequestUpload(DiagnosticMemoryAddressableRangeAccess):
    """
    This represents an instance of the "Request Upload" diagnostic service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::MemoryByAddress

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 145, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference substantiates that abstract reference in the reference
        # represents the ability to access among all DiagnosticRequestUpload in
        # context.
        self._requestUpload: Optional["DiagnosticRequest"] = None

    @property
    def request_upload(self) -> Optional["DiagnosticRequest"]:
        """Get requestUpload (Pythonic accessor)."""
        return self._requestUpload

    @request_upload.setter
    def request_upload(self, value: Optional["DiagnosticRequest"]) -> None:
        """
        Set requestUpload with validation.

        Args:
            value: The requestUpload to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._requestUpload = None
            return

        if not isinstance(value, DiagnosticRequest):
            raise TypeError(
                f"requestUpload must be DiagnosticRequest or None, got {type(value).__name__}"
            )
        self._requestUpload = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRequestUpload(self) -> "DiagnosticRequest":
        """
        AUTOSAR-compliant getter for requestUpload.

        Returns:
            The requestUpload value

        Note:
            Delegates to request_upload property (CODING_RULE_V2_00017)
        """
        return self.request_upload  # Delegates to property

    def setRequestUpload(self, value: "DiagnosticRequest") -> "DiagnosticRequestUpload":
        """
        AUTOSAR-compliant setter for requestUpload with method chaining.

        Args:
            value: The requestUpload to set

        Returns:
            self for method chaining

        Note:
            Delegates to request_upload property setter (gets validation automatically)
        """
        self.request_upload = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_request_upload(self, value: Optional["DiagnosticRequest"]) -> "DiagnosticRequestUpload":
        """
        Set requestUpload and return self for chaining.

        Args:
            value: The requestUpload to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_request_upload("value")
        """
        self.request_upload = value  # Use property setter (gets validation)
        return self
