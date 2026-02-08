from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import DiagnosticMemoryByAddress


class DiagnosticDataTransfer(DiagnosticMemoryByAddress):
    """
    This represents an instance of the "Data Transfer" diagnostic service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::MemoryByAddress::DiagnosticDataTransfer

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 143, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference substantiates that abstract reference in the reference
        # represents the ability to access among all DiagnosticDataTransfer in the.
        self._dataTransfer: Optional["DiagnosticDataTransfer"] = None

    @property
    def data_transfer(self) -> Optional["DiagnosticDataTransfer"]:
        """Get dataTransfer (Pythonic accessor)."""
        return self._dataTransfer

    @data_transfer.setter
    def data_transfer(self, value: Optional["DiagnosticDataTransfer"]) -> None:
        """
        Set dataTransfer with validation.

        Args:
            value: The dataTransfer to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataTransfer = None
            return

        if not isinstance(value, DiagnosticDataTransfer):
            raise TypeError(
                f"dataTransfer must be DiagnosticDataTransfer or None, got {type(value).__name__}"
            )
        self._dataTransfer = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataTransfer(self) -> "DiagnosticDataTransfer":
        """
        AUTOSAR-compliant getter for dataTransfer.

        Returns:
            The dataTransfer value

        Note:
            Delegates to data_transfer property (CODING_RULE_V2_00017)
        """
        return self.data_transfer  # Delegates to property

    def setDataTransfer(self, value: "DiagnosticDataTransfer") -> "DiagnosticDataTransfer":
        """
        AUTOSAR-compliant setter for dataTransfer with method chaining.

        Args:
            value: The dataTransfer to set

        Returns:
            self for method chaining

        Note:
            Delegates to data_transfer property setter (gets validation automatically)
        """
        self.data_transfer = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_transfer(self, value: Optional["DiagnosticDataTransfer"]) -> "DiagnosticDataTransfer":
        """
        Set dataTransfer and return self for chaining.

        Args:
            value: The dataTransfer to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_transfer("value")
        """
        self.data_transfer = value  # Use property setter (gets validation)
        return self
