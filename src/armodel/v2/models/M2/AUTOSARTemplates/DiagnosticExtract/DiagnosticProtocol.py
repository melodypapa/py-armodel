from typing import List, Optional
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import DiagnosticCommonElement


class DiagnosticProtocol(DiagnosticCommonElement):
    """
    This meta-class represents the ability to define a diagnostic protocol.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticContribution::DiagnosticProtocol

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 58, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the collection of applicable Diagnostic for this
                # DiagnosticProtocol.
        # atpVariation.
        self._diagnostic: List["DiagnosticConnection"] = []

    @property
    def diagnostic(self) -> List["DiagnosticConnection"]:
        """Get diagnostic (Pythonic accessor)."""
        return self._diagnostic
        # This represents the priority of the diagnostic protocol in other diagnostic
                # protocols.
        # Lower numeric higher protocol priority: - Highest protocol priority - Lowest
                # protocol priority.
        self._priority: Optional["PositiveInteger"] = None

    @property
    def priority(self) -> Optional["PositiveInteger"]:
        """Get priority (Pythonic accessor)."""
        return self._priority

    @priority.setter
    def priority(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set priority with validation.

        Args:
            value: The priority to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._priority = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"priority must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._priority = value
        # This identifies the applicable protocol.
        self._protocolKind: Optional["NameToken"] = None

    @property
    def protocol_kind(self) -> Optional["NameToken"]:
        """Get protocolKind (Pythonic accessor)."""
        return self._protocolKind

    @protocol_kind.setter
    def protocol_kind(self, value: Optional["NameToken"]) -> None:
        """
        Set protocolKind with validation.

        Args:
            value: The protocolKind to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._protocolKind = None
            return

        if not isinstance(value, NameToken):
            raise TypeError(
                f"protocolKind must be NameToken or None, got {type(value).__name__}"
            )
        self._protocolKind = value
        # The purpose of this attribute is to define whether or not ECU should send a
        # NRC 0x78 (response pending) to the bootloader (in this case the be set to
        # "true") or if the transition shall be sending NRC 0x78 (in this case the be
        # set to "false").
        self._sendRespPend: Optional["Boolean"] = None

    @property
    def send_resp_pend(self) -> Optional["Boolean"]:
        """Get sendRespPend (Pythonic accessor)."""
        return self._sendRespPend

    @send_resp_pend.setter
    def send_resp_pend(self, value: Optional["Boolean"]) -> None:
        """
        Set sendRespPend with validation.

        Args:
            value: The sendRespPend to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sendRespPend = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"sendRespPend must be Boolean or None, got {type(value).__name__}"
            )
        self._sendRespPend = value
        # This represents the service table applicable for the given atpVariation.
        self._serviceTable: Optional["DiagnosticServiceTable"] = None

    @property
    def service_table(self) -> Optional["DiagnosticServiceTable"]:
        """Get serviceTable (Pythonic accessor)."""
        return self._serviceTable

    @service_table.setter
    def service_table(self, value: Optional["DiagnosticServiceTable"]) -> None:
        """
        Set serviceTable with validation.

        Args:
            value: The serviceTable to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._serviceTable = None
            return

        if not isinstance(value, DiagnosticServiceTable):
            raise TypeError(
                f"serviceTable must be DiagnosticServiceTable or None, got {type(value).__name__}"
            )
        self._serviceTable = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDiagnostic(self) -> List["DiagnosticConnection"]:
        """
        AUTOSAR-compliant getter for diagnostic.

        Returns:
            The diagnostic value

        Note:
            Delegates to diagnostic property (CODING_RULE_V2_00017)
        """
        return self.diagnostic  # Delegates to property

    def getPriority(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for priority.

        Returns:
            The priority value

        Note:
            Delegates to priority property (CODING_RULE_V2_00017)
        """
        return self.priority  # Delegates to property

    def setPriority(self, value: "PositiveInteger") -> "DiagnosticProtocol":
        """
        AUTOSAR-compliant setter for priority with method chaining.

        Args:
            value: The priority to set

        Returns:
            self for method chaining

        Note:
            Delegates to priority property setter (gets validation automatically)
        """
        self.priority = value  # Delegates to property setter
        return self

    def getProtocolKind(self) -> "NameToken":
        """
        AUTOSAR-compliant getter for protocolKind.

        Returns:
            The protocolKind value

        Note:
            Delegates to protocol_kind property (CODING_RULE_V2_00017)
        """
        return self.protocol_kind  # Delegates to property

    def setProtocolKind(self, value: "NameToken") -> "DiagnosticProtocol":
        """
        AUTOSAR-compliant setter for protocolKind with method chaining.

        Args:
            value: The protocolKind to set

        Returns:
            self for method chaining

        Note:
            Delegates to protocol_kind property setter (gets validation automatically)
        """
        self.protocol_kind = value  # Delegates to property setter
        return self

    def getSendRespPend(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for sendRespPend.

        Returns:
            The sendRespPend value

        Note:
            Delegates to send_resp_pend property (CODING_RULE_V2_00017)
        """
        return self.send_resp_pend  # Delegates to property

    def setSendRespPend(self, value: "Boolean") -> "DiagnosticProtocol":
        """
        AUTOSAR-compliant setter for sendRespPend with method chaining.

        Args:
            value: The sendRespPend to set

        Returns:
            self for method chaining

        Note:
            Delegates to send_resp_pend property setter (gets validation automatically)
        """
        self.send_resp_pend = value  # Delegates to property setter
        return self

    def getServiceTable(self) -> "DiagnosticServiceTable":
        """
        AUTOSAR-compliant getter for serviceTable.

        Returns:
            The serviceTable value

        Note:
            Delegates to service_table property (CODING_RULE_V2_00017)
        """
        return self.service_table  # Delegates to property

    def setServiceTable(self, value: "DiagnosticServiceTable") -> "DiagnosticProtocol":
        """
        AUTOSAR-compliant setter for serviceTable with method chaining.

        Args:
            value: The serviceTable to set

        Returns:
            self for method chaining

        Note:
            Delegates to service_table property setter (gets validation automatically)
        """
        self.service_table = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_priority(self, value: Optional["PositiveInteger"]) -> "DiagnosticProtocol":
        """
        Set priority and return self for chaining.

        Args:
            value: The priority to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_priority("value")
        """
        self.priority = value  # Use property setter (gets validation)
        return self

    def with_protocol_kind(self, value: Optional["NameToken"]) -> "DiagnosticProtocol":
        """
        Set protocolKind and return self for chaining.

        Args:
            value: The protocolKind to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_protocol_kind("value")
        """
        self.protocol_kind = value  # Use property setter (gets validation)
        return self

    def with_send_resp_pend(self, value: Optional["Boolean"]) -> "DiagnosticProtocol":
        """
        Set sendRespPend and return self for chaining.

        Args:
            value: The sendRespPend to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_send_resp_pend("value")
        """
        self.send_resp_pend = value  # Use property setter (gets validation)
        return self

    def with_service_table(self, value: Optional["DiagnosticServiceTable"]) -> "DiagnosticProtocol":
        """
        Set serviceTable and return self for chaining.

        Args:
            value: The serviceTable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_service_table("value")
        """
        self.service_table = value  # Use property setter (gets validation)
        return self
