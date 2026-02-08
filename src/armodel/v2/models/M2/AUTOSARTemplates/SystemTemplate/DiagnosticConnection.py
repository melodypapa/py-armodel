from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement

    RefType,
)


class DiagnosticConnection(ARElement):
    """
    DiagnosticConncection that is used to describe the relationship between
    several TP connections.

    Package: M2::AUTOSARTemplates::SystemTemplate::DiagnosticConnection::DiagnosticConnection

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 60, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 632, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to functional request messages.
        # 719 Document ID 673: AUTOSAR_CP_TPS_DiagnosticExtractTemplate Template
                # R23-11.
        self._functionalRequest: List["TpConnectionIdent"] = []

    @property
    def functional_request(self) -> List["TpConnectionIdent"]:
        """Get functionalRequest (Pythonic accessor)."""
        return self._functionalRequest
        # Reference to UUDT responses.
        self._periodicResponseUudt: List[RefType] = []

    @property
    def periodic_response_uudt(self) -> List[RefType]:
        """Get periodicResponseUudt (Pythonic accessor)."""
        return self._periodicResponseUudt
        # Reference to a physical request message.
        self._physicalRequest: Optional["TpConnectionIdent"] = None

    @property
    def physical_request(self) -> Optional["TpConnectionIdent"]:
        """Get physicalRequest (Pythonic accessor)."""
        return self._physicalRequest

    @physical_request.setter
    def physical_request(self, value: Optional["TpConnectionIdent"]) -> None:
        """
        Set physicalRequest with validation.

        Args:
            value: The physicalRequest to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._physicalRequest = None
            return

        if not isinstance(value, TpConnectionIdent):
            raise TypeError(
                f"physicalRequest must be TpConnectionIdent or None, got {type(value).__name__}"
            )
        self._physicalRequest = value
        # In the vast majority of cases a response is required.
        # are also cases where providing the not possible and/or not allowed.
        self._response: Optional["TpConnectionIdent"] = None

    @property
    def response(self) -> Optional["TpConnectionIdent"]:
        """Get response (Pythonic accessor)."""
        return self._response

    @response.setter
    def response(self, value: Optional["TpConnectionIdent"]) -> None:
        """
        Set response with validation.

        Args:
            value: The response to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._response = None
            return

        if not isinstance(value, TpConnectionIdent):
            raise TypeError(
                f"response must be TpConnectionIdent or None, got {type(value).__name__}"
            )
        self._response = value
        # Reference to a ROE message.
        # atp.
        # Status=obsolete.
        self._responseOn: Optional["TpConnectionIdent"] = None

    @property
    def response_on(self) -> Optional["TpConnectionIdent"]:
        """Get responseOn (Pythonic accessor)."""
        return self._responseOn

    @response_on.setter
    def response_on(self, value: Optional["TpConnectionIdent"]) -> None:
        """
        Set responseOn with validation.

        Args:
            value: The responseOn to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._responseOn = None
            return

        if not isinstance(value, TpConnectionIdent):
            raise TypeError(
                f"responseOn must be TpConnectionIdent or None, got {type(value).__name__}"
            )
        self._responseOn = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFunctionalRequest(self) -> List["TpConnectionIdent"]:
        """
        AUTOSAR-compliant getter for functionalRequest.

        Returns:
            The functionalRequest value

        Note:
            Delegates to functional_request property (CODING_RULE_V2_00017)
        """
        return self.functional_request  # Delegates to property

    def getPeriodicResponseUudt(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for periodicResponseUudt.

        Returns:
            The periodicResponseUudt value

        Note:
            Delegates to periodic_response_uudt property (CODING_RULE_V2_00017)
        """
        return self.periodic_response_uudt  # Delegates to property

    def getPhysicalRequest(self) -> "TpConnectionIdent":
        """
        AUTOSAR-compliant getter for physicalRequest.

        Returns:
            The physicalRequest value

        Note:
            Delegates to physical_request property (CODING_RULE_V2_00017)
        """
        return self.physical_request  # Delegates to property

    def setPhysicalRequest(self, value: "TpConnectionIdent") -> "DiagnosticConnection":
        """
        AUTOSAR-compliant setter for physicalRequest with method chaining.

        Args:
            value: The physicalRequest to set

        Returns:
            self for method chaining

        Note:
            Delegates to physical_request property setter (gets validation automatically)
        """
        self.physical_request = value  # Delegates to property setter
        return self

    def getResponse(self) -> "TpConnectionIdent":
        """
        AUTOSAR-compliant getter for response.

        Returns:
            The response value

        Note:
            Delegates to response property (CODING_RULE_V2_00017)
        """
        return self.response  # Delegates to property

    def setResponse(self, value: "TpConnectionIdent") -> "DiagnosticConnection":
        """
        AUTOSAR-compliant setter for response with method chaining.

        Args:
            value: The response to set

        Returns:
            self for method chaining

        Note:
            Delegates to response property setter (gets validation automatically)
        """
        self.response = value  # Delegates to property setter
        return self

    def getResponseOn(self) -> "TpConnectionIdent":
        """
        AUTOSAR-compliant getter for responseOn.

        Returns:
            The responseOn value

        Note:
            Delegates to response_on property (CODING_RULE_V2_00017)
        """
        return self.response_on  # Delegates to property

    def setResponseOn(self, value: "TpConnectionIdent") -> "DiagnosticConnection":
        """
        AUTOSAR-compliant setter for responseOn with method chaining.

        Args:
            value: The responseOn to set

        Returns:
            self for method chaining

        Note:
            Delegates to response_on property setter (gets validation automatically)
        """
        self.response_on = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_physical_request(self, value: Optional["TpConnectionIdent"]) -> "DiagnosticConnection":
        """
        Set physicalRequest and return self for chaining.

        Args:
            value: The physicalRequest to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_physical_request("value")
        """
        self.physical_request = value  # Use property setter (gets validation)
        return self

    def with_response(self, value: Optional["TpConnectionIdent"]) -> "DiagnosticConnection":
        """
        Set response and return self for chaining.

        Args:
            value: The response to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_response("value")
        """
        self.response = value  # Use property setter (gets validation)
        return self

    def with_response_on(self, value: Optional["TpConnectionIdent"]) -> "DiagnosticConnection":
        """
        Set responseOn and return self for chaining.

        Args:
            value: The responseOn to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_response_on("value")
        """
        self.response_on = value  # Use property setter (gets validation)
        return self
