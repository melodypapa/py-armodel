from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import DiagnosticCommonElement
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DiagnosticMeasurementIdentifier(DiagnosticCommonElement):
    """
    This meta-class represents the ability to describe a measurement identifier.
    (cid:53) 205 of 719 Document ID 673:
    AUTOSAR_CP_TPS_DiagnosticExtractTemplate Diagnostic Extract Template AUTOSAR
    CP R23-11 (cid:52)

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticTestResult::DiagnosticMeasurementIdentifier

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 205, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the numerical measurement Id.
        self._obdMid: Optional["PositiveInteger"] = None

    @property
    def obd_mid(self) -> Optional["PositiveInteger"]:
        """Get obdMid (Pythonic accessor)."""
        return self._obdMid

    @obd_mid.setter
    def obd_mid(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set obdMid with validation.

        Args:
            value: The obdMid to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._obdMid = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"obdMid must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._obdMid = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getObdMid(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for obdMid.

        Returns:
            The obdMid value

        Note:
            Delegates to obd_mid property (CODING_RULE_V2_00017)
        """
        return self.obd_mid  # Delegates to property

    def setObdMid(self, value: "PositiveInteger") -> "DiagnosticMeasurementIdentifier":
        """
        AUTOSAR-compliant setter for obdMid with method chaining.

        Args:
            value: The obdMid to set

        Returns:
            self for method chaining

        Note:
            Delegates to obd_mid property setter (gets validation automatically)
        """
        self.obd_mid = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_obd_mid(self, value: Optional["PositiveInteger"]) -> "DiagnosticMeasurementIdentifier":
        """
        Set obdMid and return self for chaining.

        Args:
            value: The obdMid to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_obd_mid("value")
        """
        self.obd_mid = value  # Use property setter (gets validation)
        return self
