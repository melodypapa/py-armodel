from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService import (
    DiagnosticServiceClass,
)


class DiagnosticCustomServiceClass(DiagnosticServiceClass):
    """
    This represents the ability to define a custom diagnostic service class and
    assign an ID to it. Further configuration is not foreseen from the point of
    view of the diagnostic extract and consequently needs to be done on the
    level of ECUC.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::CommonService

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 71, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute may only be used for the definition of services.
        # The values shall not overlap with service IDs.
        self._customService: Optional["PositiveInteger"] = None

    @property
    def custom_service(self) -> Optional["PositiveInteger"]:
        """Get customService (Pythonic accessor)."""
        return self._customService

    @custom_service.setter
    def custom_service(self, value: Optional["PositiveInteger"]) -> None:
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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"customService must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._customService = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCustomService(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for customService.

        Returns:
            The customService value

        Note:
            Delegates to custom_service property (CODING_RULE_V2_00017)
        """
        return self.custom_service  # Delegates to property

    def setCustomService(self, value: "PositiveInteger") -> "DiagnosticCustomServiceClass":
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

    def with_custom_service(self, value: Optional["PositiveInteger"]) -> "DiagnosticCustomServiceClass":
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
