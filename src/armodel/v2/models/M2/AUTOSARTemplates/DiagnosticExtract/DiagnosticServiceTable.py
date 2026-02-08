from typing import List, Optional


class DiagnosticServiceTable(DiagnosticCommonElement):
    """
    This meta-class represents a model of a diagnostic service table, i.e. the
    UDS services applicable for a given ECU.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticContribution::DiagnosticServiceTable

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 59, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the DiagnosticConnection that is taken handling the data
        # transmission for the enclosing possible to refer to more than one diagnostic
        # order to support more than one diagnostic atpVariation.
        self._diagnostic: List["DiagnosticConnection"] = []

    @property
    def diagnostic(self) -> List["DiagnosticConnection"]:
        """Get diagnostic (Pythonic accessor)."""
        return self._diagnostic
        # This represents the applicable EcuInstance for this.
        self._ecuInstance: Optional["EcuInstance"] = None

    @property
    def ecu_instance(self) -> Optional["EcuInstance"]:
        """Get ecuInstance (Pythonic accessor)."""
        return self._ecuInstance

    @ecu_instance.setter
    def ecu_instance(self, value: Optional["EcuInstance"]) -> None:
        """
        Set ecuInstance with validation.

        Args:
            value: The ecuInstance to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ecuInstance = None
            return

        if not isinstance(value, EcuInstance):
            raise TypeError(
                f"ecuInstance must be EcuInstance or None, got {type(value).__name__}"
            )
        self._ecuInstance = value
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
        # This represents the collection of DiagnosticService to be considered in the
        # scope of this Diagnostic.
        self._serviceInstance: List["DiagnosticService"] = []

    @property
    def service_instance(self) -> List["DiagnosticService"]:
        """Get serviceInstance (Pythonic accessor)."""
        return self._serviceInstance

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

    def getEcuInstance(self) -> "EcuInstance":
        """
        AUTOSAR-compliant getter for ecuInstance.

        Returns:
            The ecuInstance value

        Note:
            Delegates to ecu_instance property (CODING_RULE_V2_00017)
        """
        return self.ecu_instance  # Delegates to property

    def setEcuInstance(self, value: "EcuInstance") -> "DiagnosticServiceTable":
        """
        AUTOSAR-compliant setter for ecuInstance with method chaining.

        Args:
            value: The ecuInstance to set

        Returns:
            self for method chaining

        Note:
            Delegates to ecu_instance property setter (gets validation automatically)
        """
        self.ecu_instance = value  # Delegates to property setter
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

    def setProtocolKind(self, value: "NameToken") -> "DiagnosticServiceTable":
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

    def getServiceInstance(self) -> List["DiagnosticService"]:
        """
        AUTOSAR-compliant getter for serviceInstance.

        Returns:
            The serviceInstance value

        Note:
            Delegates to service_instance property (CODING_RULE_V2_00017)
        """
        return self.service_instance  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ecu_instance(self, value: Optional["EcuInstance"]) -> "DiagnosticServiceTable":
        """
        Set ecuInstance and return self for chaining.

        Args:
            value: The ecuInstance to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ecu_instance("value")
        """
        self.ecu_instance = value  # Use property setter (gets validation)
        return self

    def with_protocol_kind(self, value: Optional["NameToken"]) -> "DiagnosticServiceTable":
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
