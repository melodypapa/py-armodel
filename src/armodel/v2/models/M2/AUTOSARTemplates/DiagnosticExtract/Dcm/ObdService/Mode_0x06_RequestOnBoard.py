"""
AUTOSAR Package - Mode_0x06_RequestOnBoard

Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::ObdService::Mode_0x06_RequestOnBoard
"""

from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService import (
    DiagnosticServiceClass,
    DiagnosticServiceInstance,
)


class DiagnosticRequestOnBoardMonitoringTestResults(DiagnosticServiceInstance):
    """
    This meta-class represents the ability to model an instance of the OBD mode
    0x06 service.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::ObdService::Mode_0x06_RequestOnBoard::DiagnosticRequestOnBoardMonitoringTestResults
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 156, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference identifies the applicable collection of test for setting up a
        # request message for mode.
        self._diagnosticTest: List["DiagnosticTestResult"] = []

    @property
    def diagnostic_test(self) -> List["DiagnosticTestResult"]:
        """Get diagnosticTest (Pythonic accessor)."""
        return self._diagnosticTest
        # This reference substantiates that abstract reference in the role serviceClass
                # for this specific concrete class.
        # Thereby, the reference represents the ability to access ResultsClass shared
                # attributes among all DiagnosticRequestOnBoard the given context.
        self._requestOn: Optional["DiagnosticRequestOn"] = None

    @property
    def request_on(self) -> Optional["DiagnosticRequestOn"]:
        """Get requestOn (Pythonic accessor)."""
        return self._requestOn

    @request_on.setter
    def request_on(self, value: Optional["DiagnosticRequestOn"]) -> None:
        """
        Set requestOn with validation.
        
        Args:
            value: The requestOn to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._requestOn = None
            return

        if not isinstance(value, DiagnosticRequestOn):
            raise TypeError(
                f"requestOn must be DiagnosticRequestOn or None, got {type(value).__name__}"
            )
        self._requestOn = value

    def with_diagnostic_test(self, value):
        """
        Set diagnostic_test and return self for chaining.

        Args:
            value: The diagnostic_test to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_diagnostic_test("value")
        """
        self.diagnostic_test = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDiagnosticTest(self) -> List["DiagnosticTestResult"]:
        """
        AUTOSAR-compliant getter for diagnosticTest.
        
        Returns:
            The diagnosticTest value
        
        Note:
            Delegates to diagnostic_test property (CODING_RULE_V2_00017)
        """
        return self.diagnostic_test  # Delegates to property

    def getRequestOn(self) -> "DiagnosticRequestOn":
        """
        AUTOSAR-compliant getter for requestOn.
        
        Returns:
            The requestOn value
        
        Note:
            Delegates to request_on property (CODING_RULE_V2_00017)
        """
        return self.request_on  # Delegates to property

    def setRequestOn(self, value: "DiagnosticRequestOn") -> "DiagnosticRequestOnBoardMonitoringTestResults":
        """
        AUTOSAR-compliant setter for requestOn with method chaining.
        
        Args:
            value: The requestOn to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to request_on property setter (gets validation automatically)
        """
        self.request_on = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_request_on(self, value: Optional["DiagnosticRequestOn"]) -> "DiagnosticRequestOnBoardMonitoringTestResults":
        """
        Set requestOn and return self for chaining.
        
        Args:
            value: The requestOn to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_request_on("value")
        """
        self.request_on = value  # Use property setter (gets validation)
        return self



class DiagnosticRequestOnBoardMonitoringTestResultsClass(DiagnosticServiceClass):
    """
    This meta-class represents the ability to define common properties for all
    instances of the "Request On-Board Monitoring Test Results" OBD diagnostic
    service.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::ObdService::Mode_0x06_RequestOnBoard::DiagnosticRequestOnBoardMonitoringTestResultsClass
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 156, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
