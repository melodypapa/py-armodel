from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    DiagnosticResponseTo,
    DiagnosticServiceClass,
)


class DiagnosticEcuResetClass(DiagnosticServiceClass):
    """
    This meta-class contains attributes shared by all instances of the "Ecu
    Reset" diagnostic service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::EcuReset::DiagnosticEcuResetClass

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 102, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines whether the response to the Ecu Reset service shall be
        # transmitted before or after the.
        self._respondTo: Optional["DiagnosticResponseTo"] = None

    @property
    def respond_to(self) -> Optional["DiagnosticResponseTo"]:
        """Get respondTo (Pythonic accessor)."""
        return self._respondTo

    @respond_to.setter
    def respond_to(self, value: Optional["DiagnosticResponseTo"]) -> None:
        """
        Set respondTo with validation.

        Args:
            value: The respondTo to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._respondTo = None
            return

        if not isinstance(value, DiagnosticResponseTo):
            raise TypeError(
                f"respondTo must be DiagnosticResponseTo or None, got {type(value).__name__}"
            )
        self._respondTo = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRespondTo(self) -> "DiagnosticResponseTo":
        """
        AUTOSAR-compliant getter for respondTo.

        Returns:
            The respondTo value

        Note:
            Delegates to respond_to property (CODING_RULE_V2_00017)
        """
        return self.respond_to  # Delegates to property

    def setRespondTo(self, value: "DiagnosticResponseTo") -> "DiagnosticEcuResetClass":
        """
        AUTOSAR-compliant setter for respondTo with method chaining.

        Args:
            value: The respondTo to set

        Returns:
            self for method chaining

        Note:
            Delegates to respond_to property setter (gets validation automatically)
        """
        self.respond_to = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_respond_to(self, value: Optional["DiagnosticResponseTo"]) -> "DiagnosticEcuResetClass":
        """
        Set respondTo and return self for chaining.

        Args:
            value: The respondTo to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_respond_to("value")
        """
        self.respond_to = value  # Use property setter (gets validation)
        return self
