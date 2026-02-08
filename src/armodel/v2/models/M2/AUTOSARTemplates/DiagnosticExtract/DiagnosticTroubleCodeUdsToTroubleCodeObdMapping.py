from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping import DiagnosticMapping


class DiagnosticTroubleCodeUdsToTroubleCodeObdMapping(DiagnosticMapping):
    """
    This meta-class represents the ability to associate a UDS trouble code to an
    OBD trouble code.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::DiagnosticTroubleCodeUdsToTroubleCodeObdMapping

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 188, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the OBD DTC referenced in the mapping between UDS and OBD
        # DTCs.
        self._troubleCode: Optional["DiagnosticTroubleCode"] = None

    @property
    def trouble_code(self) -> Optional["DiagnosticTroubleCode"]:
        """Get troubleCode (Pythonic accessor)."""
        return self._troubleCode

    @trouble_code.setter
    def trouble_code(self, value: Optional["DiagnosticTroubleCode"]) -> None:
        """
        Set troubleCode with validation.

        Args:
            value: The troubleCode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._troubleCode = None
            return

        if not isinstance(value, DiagnosticTroubleCode):
            raise TypeError(
                f"troubleCode must be DiagnosticTroubleCode or None, got {type(value).__name__}"
            )
        self._troubleCode = value
        # This represents the UDS DTC referenced in the mapping UDS and OBD DTCs.
        self._troubleCodeUds: Optional["DiagnosticTroubleCode"] = None

    @property
    def trouble_code_uds(self) -> Optional["DiagnosticTroubleCode"]:
        """Get troubleCodeUds (Pythonic accessor)."""
        return self._troubleCodeUds

    @trouble_code_uds.setter
    def trouble_code_uds(self, value: Optional["DiagnosticTroubleCode"]) -> None:
        """
        Set troubleCodeUds with validation.

        Args:
            value: The troubleCodeUds to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._troubleCodeUds = None
            return

        if not isinstance(value, DiagnosticTroubleCode):
            raise TypeError(
                f"troubleCodeUds must be DiagnosticTroubleCode or None, got {type(value).__name__}"
            )
        self._troubleCodeUds = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTroubleCode(self) -> "DiagnosticTroubleCode":
        """
        AUTOSAR-compliant getter for troubleCode.

        Returns:
            The troubleCode value

        Note:
            Delegates to trouble_code property (CODING_RULE_V2_00017)
        """
        return self.trouble_code  # Delegates to property

    def setTroubleCode(self, value: "DiagnosticTroubleCode") -> "DiagnosticTroubleCodeUdsToTroubleCodeObdMapping":
        """
        AUTOSAR-compliant setter for troubleCode with method chaining.

        Args:
            value: The troubleCode to set

        Returns:
            self for method chaining

        Note:
            Delegates to trouble_code property setter (gets validation automatically)
        """
        self.trouble_code = value  # Delegates to property setter
        return self

    def getTroubleCodeUds(self) -> "DiagnosticTroubleCode":
        """
        AUTOSAR-compliant getter for troubleCodeUds.

        Returns:
            The troubleCodeUds value

        Note:
            Delegates to trouble_code_uds property (CODING_RULE_V2_00017)
        """
        return self.trouble_code_uds  # Delegates to property

    def setTroubleCodeUds(self, value: "DiagnosticTroubleCode") -> "DiagnosticTroubleCodeUdsToTroubleCodeObdMapping":
        """
        AUTOSAR-compliant setter for troubleCodeUds with method chaining.

        Args:
            value: The troubleCodeUds to set

        Returns:
            self for method chaining

        Note:
            Delegates to trouble_code_uds property setter (gets validation automatically)
        """
        self.trouble_code_uds = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_trouble_code(self, value: Optional["DiagnosticTroubleCode"]) -> "DiagnosticTroubleCodeUdsToTroubleCodeObdMapping":
        """
        Set troubleCode and return self for chaining.

        Args:
            value: The troubleCode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_trouble_code("value")
        """
        self.trouble_code = value  # Use property setter (gets validation)
        return self

    def with_trouble_code_uds(self, value: Optional["DiagnosticTroubleCode"]) -> "DiagnosticTroubleCodeUdsToTroubleCodeObdMapping":
        """
        Set troubleCodeUds and return self for chaining.

        Args:
            value: The troubleCodeUds to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_trouble_code_uds("value")
        """
        self.trouble_code_uds = value  # Use property setter (gets validation)
        return self
