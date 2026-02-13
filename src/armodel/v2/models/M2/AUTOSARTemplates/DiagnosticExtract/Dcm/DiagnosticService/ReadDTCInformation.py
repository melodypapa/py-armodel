"""
AUTOSAR Package - ReadDTCInformation

Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::ReadDTCInformation
"""


from __future__ import annotations

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService import (
    DiagnosticServiceClass,
    DiagnosticServiceInstance,
)


class DiagnosticReadDTCInformation(DiagnosticServiceInstance):
    """
    This represents an instance of the "Read DTC Information" diagnostic
    service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::ReadDTCInformation::DiagnosticReadDTCInformation

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 136, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference substantiates that abstract reference in the role serviceClass
                # for this specific concrete class.
        # among all DiagnosticRead the given context.
        self._read: Optional["DiagnosticReadDTC"] = None

    @property
    def read(self) -> Optional["DiagnosticReadDTC"]:
        """Get read (Pythonic accessor)."""
        return self._read

    @read.setter
    def read(self, value: Optional["DiagnosticReadDTC"]) -> None:
        """
        Set read with validation.

        Args:
            value: The read to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._read = None
            return

        if not isinstance(value, DiagnosticReadDTC):
            raise TypeError(
                f"read must be DiagnosticReadDTC or None, got {type(value).__name__}"
            )
        self._read = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRead(self) -> "DiagnosticReadDTC":
        """
        AUTOSAR-compliant getter for read.

        Returns:
            The read value

        Note:
            Delegates to read property (CODING_RULE_V2_00017)
        """
        return self.read  # Delegates to property

    def setRead(self, value: "DiagnosticReadDTC") -> DiagnosticReadDTCInformation:
        """
        AUTOSAR-compliant setter for read with method chaining.

        Args:
            value: The read to set

        Returns:
            self for method chaining

        Note:
            Delegates to read property setter (gets validation automatically)
        """
        self.read = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_read(self, value: Optional["DiagnosticReadDTC"]) -> DiagnosticReadDTCInformation:
        """
        Set read and return self for chaining.

        Args:
            value: The read to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_read("value")
        """
        self.read = value  # Use property setter (gets validation)
        return self



class DiagnosticReadDTCInformationClass(DiagnosticServiceClass):
    """
    This meta-class contains attributes shared by all instances of the
    "ReadDTCInformation" diagnostic service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::ReadDTCInformation::DiagnosticReadDTCInformationClass

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 136, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
