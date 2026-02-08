from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService import DiagnosticServiceInstance


class DiagnosticCustomServiceInstance(DiagnosticServiceInstance):
    """
    This meta-class has the ability to define an instance of a custom diagnostic
    service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::CustomServiceInstance::DiagnosticCustomServiceInstance

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 70, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the corresponding DiagnosticCustom.
        self._customService: Optional["DiagnosticCustom"] = None

    @property
    def custom_service(self) -> Optional["DiagnosticCustom"]:
        """Get customService (Pythonic accessor)."""
        return self._customService

    @custom_service.setter
    def custom_service(self, value: Optional["DiagnosticCustom"]) -> None:
        """
        Set customService with validation.

        Args:
            value: The customService to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._customService = None
            return

        if not isinstance(value, DiagnosticCustom):
            raise TypeError(
                f"customService must be DiagnosticCustom or None, got {type(value).__name__}"
            )
        self._customService = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCustomService(self) -> "DiagnosticCustom":
        """
        AUTOSAR-compliant getter for customService.

        Returns:
            The customService value

        Note:
            Delegates to custom_service property (CODING_RULE_V2_00017)
        """
        return self.custom_service  # Delegates to property

    def setCustomService(self, value: "DiagnosticCustom") -> "DiagnosticCustomServiceInstance":
        """
        AUTOSAR-compliant setter for customService with method chaining.

        Args:
            value: The customService to set

        Returns:
            self for method chaining

        Note:
            Delegates to custom_service property setter (gets validation automatically)
        """
        self.custom_service = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_custom_service(self, value: Optional["DiagnosticCustom"]) -> "DiagnosticCustomServiceInstance":
        """
        Set customService and return self for chaining.

        Args:
            value: The customService to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_custom_service("value")
        """
        self.custom_service = value  # Use property setter (gets validation)
        return self
