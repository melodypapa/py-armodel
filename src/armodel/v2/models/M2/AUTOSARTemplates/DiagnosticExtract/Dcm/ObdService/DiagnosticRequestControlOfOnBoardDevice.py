from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    DiagnosticRequest,
    DiagnosticServiceInstance,
    DiagnosticTestRoutine,
)


class DiagnosticRequestControlOfOnBoardDevice(DiagnosticServiceInstance):
    """
    This meta-class represents the ability to model an instance of the OBD mode
    0x08 service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::ObdService::Mode_0x08_RequestControlOfOnBoard::DiagnosticRequestControlOfOnBoardDevice

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 157, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference substantiates that abstract reference in the role serviceClass
                # for this specific concrete class.
        # Thereby, the reference represents the ability to access among all
                # DiagnosticRequestControlOf the given context.
        self._requestControl: Optional["DiagnosticRequest"] = None

    @property
    def request_control(self) -> Optional["DiagnosticRequest"]:
        """Get requestControl (Pythonic accessor)."""
        return self._requestControl

    @request_control.setter
    def request_control(self, value: Optional["DiagnosticRequest"]) -> None:
        """
        Set requestControl with validation.

        Args:
            value: The requestControl to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._requestControl = None
            return

        if not isinstance(value, DiagnosticRequest):
            raise TypeError(
                f"requestControl must be DiagnosticRequest or None, got {type(value).__name__}"
            )
        self._requestControl = value
        # This represents the test Id for the mode 0x08.
        self._testIdIdentifier: Optional["DiagnosticTestRoutine"] = None

    @property
    def test_id_identifier(self) -> Optional["DiagnosticTestRoutine"]:
        """Get testIdIdentifier (Pythonic accessor)."""
        return self._testIdIdentifier

    @test_id_identifier.setter
    def test_id_identifier(self, value: Optional["DiagnosticTestRoutine"]) -> None:
        """
        Set testIdIdentifier with validation.

        Args:
            value: The testIdIdentifier to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._testIdIdentifier = None
            return

        if not isinstance(value, DiagnosticTestRoutine):
            raise TypeError(
                f"testIdIdentifier must be DiagnosticTestRoutine or None, got {type(value).__name__}"
            )
        self._testIdIdentifier = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRequestControl(self) -> "DiagnosticRequest":
        """
        AUTOSAR-compliant getter for requestControl.

        Returns:
            The requestControl value

        Note:
            Delegates to request_control property (CODING_RULE_V2_00017)
        """
        return self.request_control  # Delegates to property

    def setRequestControl(self, value: "DiagnosticRequest") -> "DiagnosticRequestControlOfOnBoardDevice":
        """
        AUTOSAR-compliant setter for requestControl with method chaining.

        Args:
            value: The requestControl to set

        Returns:
            self for method chaining

        Note:
            Delegates to request_control property setter (gets validation automatically)
        """
        self.request_control = value  # Delegates to property setter
        return self

    def getTestIdIdentifier(self) -> "DiagnosticTestRoutine":
        """
        AUTOSAR-compliant getter for testIdIdentifier.

        Returns:
            The testIdIdentifier value

        Note:
            Delegates to test_id_identifier property (CODING_RULE_V2_00017)
        """
        return self.test_id_identifier  # Delegates to property

    def setTestIdIdentifier(self, value: "DiagnosticTestRoutine") -> "DiagnosticRequestControlOfOnBoardDevice":
        """
        AUTOSAR-compliant setter for testIdIdentifier with method chaining.

        Args:
            value: The testIdIdentifier to set

        Returns:
            self for method chaining

        Note:
            Delegates to test_id_identifier property setter (gets validation automatically)
        """
        self.test_id_identifier = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_request_control(self, value: Optional["DiagnosticRequest"]) -> "DiagnosticRequestControlOfOnBoardDevice":
        """
        Set requestControl and return self for chaining.

        Args:
            value: The requestControl to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_request_control("value")
        """
        self.request_control = value  # Use property setter (gets validation)
        return self

    def with_test_id_identifier(self, value: Optional["DiagnosticTestRoutine"]) -> "DiagnosticRequestControlOfOnBoardDevice":
        """
        Set testIdIdentifier and return self for chaining.

        Args:
            value: The testIdIdentifier to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_test_id_identifier("value")
        """
        self.test_id_identifier = value  # Use property setter (gets validation)
        return self
