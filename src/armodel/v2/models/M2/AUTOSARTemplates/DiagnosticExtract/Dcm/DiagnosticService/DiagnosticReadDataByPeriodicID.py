from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService import (
    DiagnosticServiceInstance,
)


class DiagnosticReadDataByPeriodicID(DiagnosticServiceInstance):
    """
    This represents an instance of the "Read Data by periodic Identifier"
    diagnostic service. (cid:53) 129 of 719 Document ID 673:
    AUTOSAR_CP_TPS_DiagnosticExtractTemplate Diagnostic Extract Template AUTOSAR
    CP R23-11 (cid:52)

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::ReadDataByPeriodicID

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 129, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference substantiates that abstract reference in the serviceClass for
                # this specific concrete class.
        # reference represents the ability to access among all DiagnosticReadDataBy the
                # given context.
        self._readDataClass: Optional["DiagnosticReadDataBy"] = None

    @property
    def read_data_class(self) -> Optional["DiagnosticReadDataBy"]:
        """Get readDataClass (Pythonic accessor)."""
        return self._readDataClass

    @read_data_class.setter
    def read_data_class(self, value: Optional["DiagnosticReadDataBy"]) -> None:
        """
        Set readDataClass with validation.

        Args:
            value: The readDataClass to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._readDataClass = None
            return

        if not isinstance(value, DiagnosticReadDataBy):
            raise TypeError(
                f"readDataClass must be DiagnosticReadDataBy or None, got {type(value).__name__}"
            )
        self._readDataClass = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getReadDataClass(self) -> "DiagnosticReadDataBy":
        """
        AUTOSAR-compliant getter for readDataClass.

        Returns:
            The readDataClass value

        Note:
            Delegates to read_data_class property (CODING_RULE_V2_00017)
        """
        return self.read_data_class  # Delegates to property

    def setReadDataClass(self, value: "DiagnosticReadDataBy") -> "DiagnosticReadDataByPeriodicID":
        """
        AUTOSAR-compliant setter for readDataClass with method chaining.

        Args:
            value: The readDataClass to set

        Returns:
            self for method chaining

        Note:
            Delegates to read_data_class property setter (gets validation automatically)
        """
        self.read_data_class = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_read_data_class(self, value: Optional["DiagnosticReadDataBy"]) -> "DiagnosticReadDataByPeriodicID":
        """
        Set readDataClass and return self for chaining.

        Args:
            value: The readDataClass to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_read_data_class("value")
        """
        self.read_data_class = value  # Use property setter (gets validation)
        return self
