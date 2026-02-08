from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService import DiagnosticServiceInstance


class DiagnosticClearResetEmissionRelatedInfo(DiagnosticServiceInstance):
    """
    This meta-class represents the ability to model an instance of the OBD mode
    0x04 service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::ObdService::Mode_0x04_ClearResetEmission::DiagnosticClearResetEmissionRelatedInfo

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 154, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference substantiates that abstract reference in the role serviceClass
                # for this specific concrete class.
        # Thereby, the reference represents the ability to access DiagnosticInfo shared
                # attributes among all DiagnosticClearReste Class EmissionRelatedInfo in the
                # given context.
        self._clearReset: Optional["DiagnosticClearReset"] = None

    @property
    def clear_reset(self) -> Optional["DiagnosticClearReset"]:
        """Get clearReset (Pythonic accessor)."""
        return self._clearReset

    @clear_reset.setter
    def clear_reset(self, value: Optional["DiagnosticClearReset"]) -> None:
        """
        Set clearReset with validation.

        Args:
            value: The clearReset to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._clearReset = None
            return

        if not isinstance(value, DiagnosticClearReset):
            raise TypeError(
                f"clearReset must be DiagnosticClearReset or None, got {type(value).__name__}"
            )
        self._clearReset = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getClearReset(self) -> "DiagnosticClearReset":
        """
        AUTOSAR-compliant getter for clearReset.

        Returns:
            The clearReset value

        Note:
            Delegates to clear_reset property (CODING_RULE_V2_00017)
        """
        return self.clear_reset  # Delegates to property

    def setClearReset(self, value: "DiagnosticClearReset") -> "DiagnosticClearResetEmissionRelatedInfo":
        """
        AUTOSAR-compliant setter for clearReset with method chaining.

        Args:
            value: The clearReset to set

        Returns:
            self for method chaining

        Note:
            Delegates to clear_reset property setter (gets validation automatically)
        """
        self.clear_reset = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_clear_reset(self, value: Optional["DiagnosticClearReset"]) -> "DiagnosticClearResetEmissionRelatedInfo":
        """
        Set clearReset and return self for chaining.

        Args:
            value: The clearReset to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_clear_reset("value")
        """
        self.clear_reset = value  # Use property setter (gets validation)
        return self
