"""
AUTOSAR Package - RequestFileTransfer

Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::RequestFileTransfer
"""

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService import (
    DiagnosticServiceClass,
    DiagnosticServiceInstance,
)


class DiagnosticRequestFileTransfer(DiagnosticServiceInstance):
    """
    This diagnostic service instance implements the UDS service 0x38. (cid:53)
    146 of 719 Document ID 673: AUTOSAR_CP_TPS_DiagnosticExtractTemplate
    Diagnostic Extract Template AUTOSAR CP R23-11 (cid:52)

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::RequestFileTransfer::DiagnosticRequestFileTransfer

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 146, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference substantiates that abstract reference in the role serviceClass
                # for this specific concrete class.
        # reference represents the ability to access among all DiagnosticRequestFile
                # the given context.
        self._requestFile: Optional["DiagnosticRequestFile"] = None

    @property
    def request_file(self) -> Optional["DiagnosticRequestFile"]:
        """Get requestFile (Pythonic accessor)."""
        return self._requestFile

    @request_file.setter
    def request_file(self, value: Optional["DiagnosticRequestFile"]) -> None:
        """
        Set requestFile with validation.

        Args:
            value: The requestFile to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._requestFile = None
            return

        if not isinstance(value, DiagnosticRequestFile):
            raise TypeError(
                f"requestFile must be DiagnosticRequestFile or None, got {type(value).__name__}"
            )
        self._requestFile = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRequestFile(self) -> "DiagnosticRequestFile":
        """
        AUTOSAR-compliant getter for requestFile.

        Returns:
            The requestFile value

        Note:
            Delegates to request_file property (CODING_RULE_V2_00017)
        """
        return self.request_file  # Delegates to property

    def setRequestFile(self, value: "DiagnosticRequestFile") -> "DiagnosticRequestFileTransfer":
        """
        AUTOSAR-compliant setter for requestFile with method chaining.

        Args:
            value: The requestFile to set

        Returns:
            self for method chaining

        Note:
            Delegates to request_file property setter (gets validation automatically)
        """
        self.request_file = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_request_file(self, value: Optional["DiagnosticRequestFile"]) -> "DiagnosticRequestFileTransfer":
        """
        Set requestFile and return self for chaining.

        Args:
            value: The requestFile to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_request_file("value")
        """
        self.request_file = value  # Use property setter (gets validation)
        return self



class DiagnosticRequestFileTransferClass(DiagnosticServiceClass):
    """
    This meta-class contains attributes shared by all instances of the "Request
    File transfer" diagnostic service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::RequestFileTransfer::DiagnosticRequestFileTransferClass

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 147, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
