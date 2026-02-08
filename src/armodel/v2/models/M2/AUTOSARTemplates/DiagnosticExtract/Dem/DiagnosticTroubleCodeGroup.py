from typing import List, Optional
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import DiagnosticCommonElement


class DiagnosticTroubleCodeGroup(DiagnosticCommonElement):
    """
    The diagnostic trouble code group defines the DTCs belonging together and
    thereby forming a group.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticTroubleCode::DiagnosticTroubleCodeGroup

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 177, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the collection of DiagnosticTroubleCodes this
                # DiagnosticTroubleCodeGroup.
        # atpVariation.
        self._dtc: List["DiagnosticTroubleCode"] = []

    @property
    def dtc(self) -> List["DiagnosticTroubleCode"]:
        """Get dtc (Pythonic accessor)."""
        return self._dtc
        # This represents the base number of the DTC group.
        self._groupNumber: Optional["PositiveInteger"] = None

    @property
    def group_number(self) -> Optional["PositiveInteger"]:
        """Get groupNumber (Pythonic accessor)."""
        return self._groupNumber

    @group_number.setter
    def group_number(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set groupNumber with validation.

        Args:
            value: The groupNumber to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._groupNumber = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"groupNumber must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._groupNumber = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDtc(self) -> List["DiagnosticTroubleCode"]:
        """
        AUTOSAR-compliant getter for dtc.

        Returns:
            The dtc value

        Note:
            Delegates to dtc property (CODING_RULE_V2_00017)
        """
        return self.dtc  # Delegates to property

    def getGroupNumber(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for groupNumber.

        Returns:
            The groupNumber value

        Note:
            Delegates to group_number property (CODING_RULE_V2_00017)
        """
        return self.group_number  # Delegates to property

    def setGroupNumber(self, value: "PositiveInteger") -> "DiagnosticTroubleCodeGroup":
        """
        AUTOSAR-compliant setter for groupNumber with method chaining.

        Args:
            value: The groupNumber to set

        Returns:
            self for method chaining

        Note:
            Delegates to group_number property setter (gets validation automatically)
        """
        self.group_number = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_group_number(self, value: Optional["PositiveInteger"]) -> "DiagnosticTroubleCodeGroup":
        """
        Set groupNumber and return self for chaining.

        Args:
            value: The groupNumber to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_group_number("value")
        """
        self.group_number = value  # Use property setter (gets validation)
        return self
