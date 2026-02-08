from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService import DiagnosticServiceClass


class DiagnosticReadDataByIdentifierClass(DiagnosticServiceClass):
    """
    This meta-class contains attributes shared by all instances of the "Read
    Data by Identifier" diagnostic service. (cid:53) 113 of 719 Document ID 673:
    AUTOSAR_CP_TPS_DiagnosticExtractTemplate Diagnostic Extract Template AUTOSAR
    CP R23-11 (cid:52)

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::DataByIdentifier::DiagnosticReadDataByIdentifierClass

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 113, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute represents the maximum number of allowed a single instance of
        # DiagnosticReadDataBy.
        self._maxDidToRead: Optional["PositiveInteger"] = None

    @property
    def max_did_to_read(self) -> Optional["PositiveInteger"]:
        """Get maxDidToRead (Pythonic accessor)."""
        return self._maxDidToRead

    @max_did_to_read.setter
    def max_did_to_read(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxDidToRead with validation.

        Args:
            value: The maxDidToRead to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxDidToRead = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"maxDidToRead must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._maxDidToRead = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMaxDidToRead(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxDidToRead.

        Returns:
            The maxDidToRead value

        Note:
            Delegates to max_did_to_read property (CODING_RULE_V2_00017)
        """
        return self.max_did_to_read  # Delegates to property

    def setMaxDidToRead(self, value: "PositiveInteger") -> "DiagnosticReadDataByIdentifierClass":
        """
        AUTOSAR-compliant setter for maxDidToRead with method chaining.

        Args:
            value: The maxDidToRead to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_did_to_read property setter (gets validation automatically)
        """
        self.max_did_to_read = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_max_did_to_read(self, value: Optional["PositiveInteger"]) -> "DiagnosticReadDataByIdentifierClass":
        """
        Set maxDidToRead and return self for chaining.

        Args:
            value: The maxDidToRead to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_did_to_read("value")
        """
        self.max_did_to_read = value  # Use property setter (gets validation)
        return self
