from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import (
    DiagnosticCommonElement,
)


class DiagnosticTestRoutineIdentifier(DiagnosticCommonElement):
    """
    This represents the test id of the DiagnosticTestIdentifier.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::ObdService::Mode_0x08_RequestControlOfOnBoard

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 158, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the numerical id of the DiagnosticTest SAE J1979-DA).
        self._id: Optional["PositiveInteger"] = None

    @property
    def id(self) -> Optional["PositiveInteger"]:
        """Get id (Pythonic accessor)."""
        return self._id

    @id.setter
    def id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set id with validation.

        Args:
            value: The id to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._id = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"id must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._id = value
        # This represents the specified data size for the request Unit: byte.
        self._requestData: Optional["PositiveInteger"] = None

    @property
    def request_data(self) -> Optional["PositiveInteger"]:
        """Get requestData (Pythonic accessor)."""
        return self._requestData

    @request_data.setter
    def request_data(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set requestData with validation.

        Args:
            value: The requestData to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._requestData = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"requestData must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._requestData = value
        # This represents the specified data size for the response Unit:byte.
        self._responseData: Optional["PositiveInteger"] = None

    @property
    def response_data(self) -> Optional["PositiveInteger"]:
        """Get responseData (Pythonic accessor)."""
        return self._responseData

    @response_data.setter
    def response_data(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set responseData with validation.

        Args:
            value: The responseData to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._responseData = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"responseData must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._responseData = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for id.

        Returns:
            The id value

        Note:
            Delegates to id property (CODING_RULE_V2_00017)
        """
        return self.id  # Delegates to property

    def setId(self, value: "PositiveInteger") -> "DiagnosticTestRoutineIdentifier":
        """
        AUTOSAR-compliant setter for id with method chaining.

        Args:
            value: The id to set

        Returns:
            self for method chaining

        Note:
            Delegates to id property setter (gets validation automatically)
        """
        self.id = value  # Delegates to property setter
        return self

    def getRequestData(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for requestData.

        Returns:
            The requestData value

        Note:
            Delegates to request_data property (CODING_RULE_V2_00017)
        """
        return self.request_data  # Delegates to property

    def setRequestData(self, value: "PositiveInteger") -> "DiagnosticTestRoutineIdentifier":
        """
        AUTOSAR-compliant setter for requestData with method chaining.

        Args:
            value: The requestData to set

        Returns:
            self for method chaining

        Note:
            Delegates to request_data property setter (gets validation automatically)
        """
        self.request_data = value  # Delegates to property setter
        return self

    def getResponseData(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for responseData.

        Returns:
            The responseData value

        Note:
            Delegates to response_data property (CODING_RULE_V2_00017)
        """
        return self.response_data  # Delegates to property

    def setResponseData(self, value: "PositiveInteger") -> "DiagnosticTestRoutineIdentifier":
        """
        AUTOSAR-compliant setter for responseData with method chaining.

        Args:
            value: The responseData to set

        Returns:
            self for method chaining

        Note:
            Delegates to response_data property setter (gets validation automatically)
        """
        self.response_data = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_id(self, value: Optional["PositiveInteger"]) -> "DiagnosticTestRoutineIdentifier":
        """
        Set id and return self for chaining.

        Args:
            value: The id to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_id("value")
        """
        self.id = value  # Use property setter (gets validation)
        return self

    def with_request_data(self, value: Optional["PositiveInteger"]) -> "DiagnosticTestRoutineIdentifier":
        """
        Set requestData and return self for chaining.

        Args:
            value: The requestData to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_request_data("value")
        """
        self.request_data = value  # Use property setter (gets validation)
        return self

    def with_response_data(self, value: Optional["PositiveInteger"]) -> "DiagnosticTestRoutineIdentifier":
        """
        Set responseData and return self for chaining.

        Args:
            value: The responseData to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_response_data("value")
        """
        self.response_data = value  # Use property setter (gets validation)
        return self
