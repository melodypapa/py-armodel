from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticMemoryDestination import (
    DiagnosticMemoryDestination,
)


class DiagnosticMemoryDestinationPrimary(DiagnosticMemoryDestination):
    """
    This represents a primary memory for a diagnostic event.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticMemoryDestination

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 184, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines the format returned by Dem_Dcm GetTranslationType and
        # does not relate to/influence the functionality.
        self._typeOfDtc: Optional["DiagnosticTypeOfDtc"] = None

    @property
    def type_of_dtc(self) -> Optional["DiagnosticTypeOfDtc"]:
        """Get typeOfDtc (Pythonic accessor)."""
        return self._typeOfDtc

    @type_of_dtc.setter
    def type_of_dtc(self, value: Optional["DiagnosticTypeOfDtc"]) -> None:
        """
        Set typeOfDtc with validation.

        Args:
            value: The typeOfDtc to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._typeOfDtc = None
            return

        if not isinstance(value, DiagnosticTypeOfDtc):
            raise TypeError(
                f"typeOfDtc must be DiagnosticTypeOfDtc or None, got {type(value).__name__}"
            )
        self._typeOfDtc = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTypeOfDtc(self) -> "DiagnosticTypeOfDtc":
        """
        AUTOSAR-compliant getter for typeOfDtc.

        Returns:
            The typeOfDtc value

        Note:
            Delegates to type_of_dtc property (CODING_RULE_V2_00017)
        """
        return self.type_of_dtc  # Delegates to property

    def setTypeOfDtc(self, value: "DiagnosticTypeOfDtc") -> "DiagnosticMemoryDestinationPrimary":
        """
        AUTOSAR-compliant setter for typeOfDtc with method chaining.

        Args:
            value: The typeOfDtc to set

        Returns:
            self for method chaining

        Note:
            Delegates to type_of_dtc property setter (gets validation automatically)
        """
        self.type_of_dtc = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_type_of_dtc(self, value: Optional["DiagnosticTypeOfDtc"]) -> "DiagnosticMemoryDestinationPrimary":
        """
        Set typeOfDtc and return self for chaining.

        Args:
            value: The typeOfDtc to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_type_of_dtc("value")
        """
        self.type_of_dtc = value  # Use property setter (gets validation)
        return self
