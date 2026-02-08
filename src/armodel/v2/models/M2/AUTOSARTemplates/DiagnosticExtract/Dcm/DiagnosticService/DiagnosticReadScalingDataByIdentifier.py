from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.DataByIdentifier import (
    DiagnosticDataByIdentifier,
)


class DiagnosticReadScalingDataByIdentifier(DiagnosticDataByIdentifier):
    """
    This represents an instance of the "Read Scaling Data by Identifier"
    diagnostic service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::DataByIdentifier

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 116, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference substantiates that abstract reference in the role serviceClass
                # for this specific concrete class.
        # reference represents the ability to access among all
                # DiagnosticReadScalingData the given context.
        self._readScaling: Optional["DiagnosticReadScaling"] = None

    @property
    def read_scaling(self) -> Optional["DiagnosticReadScaling"]:
        """Get readScaling (Pythonic accessor)."""
        return self._readScaling

    @read_scaling.setter
    def read_scaling(self, value: Optional["DiagnosticReadScaling"]) -> None:
        """
        Set readScaling with validation.

        Args:
            value: The readScaling to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._readScaling = None
            return

        if not isinstance(value, DiagnosticReadScaling):
            raise TypeError(
                f"readScaling must be DiagnosticReadScaling or None, got {type(value).__name__}"
            )
        self._readScaling = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getReadScaling(self) -> "DiagnosticReadScaling":
        """
        AUTOSAR-compliant getter for readScaling.

        Returns:
            The readScaling value

        Note:
            Delegates to read_scaling property (CODING_RULE_V2_00017)
        """
        return self.read_scaling  # Delegates to property

    def setReadScaling(self, value: "DiagnosticReadScaling") -> "DiagnosticReadScalingDataByIdentifier":
        """
        AUTOSAR-compliant setter for readScaling with method chaining.

        Args:
            value: The readScaling to set

        Returns:
            self for method chaining

        Note:
            Delegates to read_scaling property setter (gets validation automatically)
        """
        self.read_scaling = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_read_scaling(self, value: Optional["DiagnosticReadScaling"]) -> "DiagnosticReadScalingDataByIdentifier":
        """
        Set readScaling and return self for chaining.

        Args:
            value: The readScaling to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_read_scaling("value")
        """
        self.read_scaling = value  # Use property setter (gets validation)
        return self
