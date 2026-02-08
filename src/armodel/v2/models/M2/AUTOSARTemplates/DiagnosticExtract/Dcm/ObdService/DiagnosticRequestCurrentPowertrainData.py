from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService import DiagnosticServiceInstance


class DiagnosticRequestCurrentPowertrainData(DiagnosticServiceInstance):
    """
    This meta-class represents the ability to model an instance of the OBD mode
    0x01 service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::ObdService::Mode_0x01_RequestCurrentPowertrain::DiagnosticRequestCurrentPowertrainData

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 150, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the PID associated with this instance of OBD mode 0x01
        # service.
        self._pid: Optional["DiagnosticParameter"] = None

    @property
    def pid(self) -> Optional["DiagnosticParameter"]:
        """Get pid (Pythonic accessor)."""
        return self._pid

    @pid.setter
    def pid(self, value: Optional["DiagnosticParameter"]) -> None:
        """
        Set pid with validation.

        Args:
            value: The pid to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pid = None
            return

        if not isinstance(value, DiagnosticParameter):
            raise TypeError(
                f"pid must be DiagnosticParameter or None, got {type(value).__name__}"
            )
        self._pid = value
        # This reference substantiates that abstract reference in the role serviceClass
                # for this specific concrete class.
        # Thereby, the reference represents the ability to access Class shared
                # attributes among all DiagnosticRequestCurrent the given context.
        self._requestCurrent: Optional["DiagnosticRequest"] = None

    @property
    def request_current(self) -> Optional["DiagnosticRequest"]:
        """Get requestCurrent (Pythonic accessor)."""
        return self._requestCurrent

    @request_current.setter
    def request_current(self, value: Optional["DiagnosticRequest"]) -> None:
        """
        Set requestCurrent with validation.

        Args:
            value: The requestCurrent to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._requestCurrent = None
            return

        if not isinstance(value, DiagnosticRequest):
            raise TypeError(
                f"requestCurrent must be DiagnosticRequest or None, got {type(value).__name__}"
            )
        self._requestCurrent = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getPid(self) -> "DiagnosticParameter":
        """
        AUTOSAR-compliant getter for pid.

        Returns:
            The pid value

        Note:
            Delegates to pid property (CODING_RULE_V2_00017)
        """
        return self.pid  # Delegates to property

    def setPid(self, value: "DiagnosticParameter") -> "DiagnosticRequestCurrentPowertrainData":
        """
        AUTOSAR-compliant setter for pid with method chaining.

        Args:
            value: The pid to set

        Returns:
            self for method chaining

        Note:
            Delegates to pid property setter (gets validation automatically)
        """
        self.pid = value  # Delegates to property setter
        return self

    def getRequestCurrent(self) -> "DiagnosticRequest":
        """
        AUTOSAR-compliant getter for requestCurrent.

        Returns:
            The requestCurrent value

        Note:
            Delegates to request_current property (CODING_RULE_V2_00017)
        """
        return self.request_current  # Delegates to property

    def setRequestCurrent(self, value: "DiagnosticRequest") -> "DiagnosticRequestCurrentPowertrainData":
        """
        AUTOSAR-compliant setter for requestCurrent with method chaining.

        Args:
            value: The requestCurrent to set

        Returns:
            self for method chaining

        Note:
            Delegates to request_current property setter (gets validation automatically)
        """
        self.request_current = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_pid(self, value: Optional["DiagnosticParameter"]) -> "DiagnosticRequestCurrentPowertrainData":
        """
        Set pid and return self for chaining.

        Args:
            value: The pid to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pid("value")
        """
        self.pid = value  # Use property setter (gets validation)
        return self

    def with_request_current(self, value: Optional["DiagnosticRequest"]) -> "DiagnosticRequestCurrentPowertrainData":
        """
        Set requestCurrent and return self for chaining.

        Args:
            value: The requestCurrent to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_request_current("value")
        """
        self.request_current = value  # Use property setter (gets validation)
        return self
