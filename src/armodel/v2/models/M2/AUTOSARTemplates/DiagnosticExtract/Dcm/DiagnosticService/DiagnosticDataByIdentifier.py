from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService import (
    DiagnosticServiceInstance,
)


class DiagnosticDataByIdentifier(DiagnosticServiceInstance, ABC):
    """
    This represents an abstract base class for all diagnostic services that
    access data by identifier.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::DataByIdentifier

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 113, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is DiagnosticDataByIdentifier:
            raise TypeError("DiagnosticDataByIdentifier is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the linked DiagnosticDataIdentifier.
        self._dataIdentifier: Optional["DiagnosticAbstractData"] = None

    @property
    def data_identifier(self) -> Optional["DiagnosticAbstractData"]:
        """Get dataIdentifier (Pythonic accessor)."""
        return self._dataIdentifier

    @data_identifier.setter
    def data_identifier(self, value: Optional["DiagnosticAbstractData"]) -> None:
        """
        Set dataIdentifier with validation.

        Args:
            value: The dataIdentifier to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataIdentifier = None
            return

        if not isinstance(value, DiagnosticAbstractData):
            raise TypeError(
                f"dataIdentifier must be DiagnosticAbstractData or None, got {type(value).__name__}"
            )
        self._dataIdentifier = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataIdentifier(self) -> "DiagnosticAbstractData":
        """
        AUTOSAR-compliant getter for dataIdentifier.

        Returns:
            The dataIdentifier value

        Note:
            Delegates to data_identifier property (CODING_RULE_V2_00017)
        """
        return self.data_identifier  # Delegates to property

    def setDataIdentifier(self, value: "DiagnosticAbstractData") -> "DiagnosticDataByIdentifier":
        """
        AUTOSAR-compliant setter for dataIdentifier with method chaining.

        Args:
            value: The dataIdentifier to set

        Returns:
            self for method chaining

        Note:
            Delegates to data_identifier property setter (gets validation automatically)
        """
        self.data_identifier = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_identifier(self, value: Optional["DiagnosticAbstractData"]) -> "DiagnosticDataByIdentifier":
        """
        Set dataIdentifier and return self for chaining.

        Args:
            value: The dataIdentifier to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_identifier("value")
        """
        self.data_identifier = value  # Use property setter (gets validation)
        return self
