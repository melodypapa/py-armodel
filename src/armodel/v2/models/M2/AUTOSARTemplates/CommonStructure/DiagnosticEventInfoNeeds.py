from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import DiagnosticCapabilityElement


class DiagnosticEventInfoNeeds(DiagnosticCapabilityElement):
    """
    This meta-class represents the needs of a software-component interested to
    get information regarding specific DTCs.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::DiagnosticEventInfoNeeds

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 312, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 760, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents a reasonable Diagnostic Trouble Code.
        # to predefine the Diagnostic Trouble Code, e.
        # g.
        # function developer has received a particular the OEM or from a
                # standardization applies for the OBD diagnostics use case.
        self._obdDtcNumber: Optional["PositiveInteger"] = None

    @property
    def obd_dtc_number(self) -> Optional["PositiveInteger"]:
        """Get obdDtcNumber (Pythonic accessor)."""
        return self._obdDtcNumber

    @obd_dtc_number.setter
    def obd_dtc_number(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set obdDtcNumber with validation.

        Args:
            value: The obdDtcNumber to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._obdDtcNumber = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"obdDtcNumber must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._obdDtcNumber = value
        # This represents a reasonable Diagnostic Trouble Code.
        # to predefine the Diagnostic Trouble Code, e.
        # g.
        # function developer has received a particular the OEM or from a
                # standardization applies for the UDS diagnostics use case.
        self._udsDtcNumber: Optional["PositiveInteger"] = None

    @property
    def uds_dtc_number(self) -> Optional["PositiveInteger"]:
        """Get udsDtcNumber (Pythonic accessor)."""
        return self._udsDtcNumber

    @uds_dtc_number.setter
    def uds_dtc_number(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set udsDtcNumber with validation.

        Args:
            value: The udsDtcNumber to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._udsDtcNumber = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"udsDtcNumber must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._udsDtcNumber = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getObdDtcNumber(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for obdDtcNumber.

        Returns:
            The obdDtcNumber value

        Note:
            Delegates to obd_dtc_number property (CODING_RULE_V2_00017)
        """
        return self.obd_dtc_number  # Delegates to property

    def setObdDtcNumber(self, value: "PositiveInteger") -> "DiagnosticEventInfoNeeds":
        """
        AUTOSAR-compliant setter for obdDtcNumber with method chaining.

        Args:
            value: The obdDtcNumber to set

        Returns:
            self for method chaining

        Note:
            Delegates to obd_dtc_number property setter (gets validation automatically)
        """
        self.obd_dtc_number = value  # Delegates to property setter
        return self

    def getUdsDtcNumber(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for udsDtcNumber.

        Returns:
            The udsDtcNumber value

        Note:
            Delegates to uds_dtc_number property (CODING_RULE_V2_00017)
        """
        return self.uds_dtc_number  # Delegates to property

    def setUdsDtcNumber(self, value: "PositiveInteger") -> "DiagnosticEventInfoNeeds":
        """
        AUTOSAR-compliant setter for udsDtcNumber with method chaining.

        Args:
            value: The udsDtcNumber to set

        Returns:
            self for method chaining

        Note:
            Delegates to uds_dtc_number property setter (gets validation automatically)
        """
        self.uds_dtc_number = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_obd_dtc_number(self, value: Optional["PositiveInteger"]) -> "DiagnosticEventInfoNeeds":
        """
        Set obdDtcNumber and return self for chaining.

        Args:
            value: The obdDtcNumber to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_obd_dtc_number("value")
        """
        self.obd_dtc_number = value  # Use property setter (gets validation)
        return self

    def with_uds_dtc_number(self, value: Optional["PositiveInteger"]) -> "DiagnosticEventInfoNeeds":
        """
        Set udsDtcNumber and return self for chaining.

        Args:
            value: The udsDtcNumber to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_uds_dtc_number("value")
        """
        self.uds_dtc_number = value  # Use property setter (gets validation)
        return self
