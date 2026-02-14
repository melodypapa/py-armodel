"""
AUTOSAR Package - DiagnosticMapping

Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping
"""


from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import (
    DiagnosticCommonElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.__init__ import (
    CpSoftwareCluster,
    DiagnosticIumpr,
    DiagnosticMapping,
    DiagnosticStartRoutine,
    DiagnosticSwMapping,
)


class DiagnosticMapping(DiagnosticCommonElement, ABC):
    """
    Abstract element for different kinds of diagnostic mappings.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::DiagnosticMapping

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 223, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is DiagnosticMapping:
            raise TypeError("DiagnosticMapping is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference can be used in an early design phase to an element of a
        # diagnostic extract with an CPSoftwareCluster.
        self._provider: Optional["CpSoftwareCluster"] = None

    @property
    def provider(self) -> Optional["CpSoftwareCluster"]:
        """Get provider (Pythonic accessor)."""
        return self._provider

    @provider.setter
    def provider(self, value: Optional["CpSoftwareCluster"]) -> None:
        """
        Set provider with validation.

        Args:
            value: The provider to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._provider = None
            return

        if not isinstance(value, CpSoftwareCluster):
            raise TypeError(
                f"provider must be CpSoftwareCluster or None, got {type(value).__name__}"
            )
        self._provider = value
        # This reference can be used in an early design phase to an element of a
        # diagnostic extract with an CPSoftwareCluster.
        self._requester: Optional["CpSoftwareCluster"] = None

    @property
    def requester(self) -> Optional["CpSoftwareCluster"]:
        """Get requester (Pythonic accessor)."""
        return self._requester

    @requester.setter
    def requester(self, value: Optional["CpSoftwareCluster"]) -> None:
        """
        Set requester with validation.

        Args:
            value: The requester to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._requester = None
            return

        if not isinstance(value, CpSoftwareCluster):
            raise TypeError(
                f"requester must be CpSoftwareCluster or None, got {type(value).__name__}"
            )
        self._requester = value

    def with_crypto_service(self, value):
        """
        Set crypto_service and return self for chaining.

        Args:
            value: The crypto_service to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_crypto_service("value")
        """
        self.crypto_service = value  # Use property setter (gets validation)
        return self

    def with_data_identifier(self, value):
        """
        Set data_identifier and return self for chaining.

        Args:
            value: The data_identifier to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_identifier("value")
        """
        self.data_identifier = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getProvider(self) -> CpSoftwareCluster:
        """
        AUTOSAR-compliant getter for provider.

        Returns:
            The provider value

        Note:
            Delegates to provider property (CODING_RULE_V2_00017)
        """
        return self.provider  # Delegates to property

    def setProvider(self, value: CpSoftwareCluster) -> DiagnosticMapping:
        """
        AUTOSAR-compliant setter for provider with method chaining.

        Args:
            value: The provider to set

        Returns:
            self for method chaining

        Note:
            Delegates to provider property setter (gets validation automatically)
        """
        self.provider = value  # Delegates to property setter
        return self

    def getRequester(self) -> CpSoftwareCluster:
        """
        AUTOSAR-compliant getter for requester.

        Returns:
            The requester value

        Note:
            Delegates to requester property (CODING_RULE_V2_00017)
        """
        return self.requester  # Delegates to property

    def setRequester(self, value: CpSoftwareCluster) -> DiagnosticMapping:
        """
        AUTOSAR-compliant setter for requester with method chaining.

        Args:
            value: The requester to set

        Returns:
            self for method chaining

        Note:
            Delegates to requester property setter (gets validation automatically)
        """
        self.requester = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_provider(self, value: Optional["CpSoftwareCluster"]) -> DiagnosticMapping:
        """
        Set provider and return self for chaining.

        Args:
            value: The provider to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_provider("value")
        """
        self.provider = value  # Use property setter (gets validation)
        return self

    def with_requester(self, value: Optional["CpSoftwareCluster"]) -> DiagnosticMapping:
        """
        Set requester and return self for chaining.

        Args:
            value: The requester to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_requester("value")
        """
        self.requester = value  # Use property setter (gets validation)
        return self



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

    def setTroubleCode(self, value: "DiagnosticTroubleCode") -> DiagnosticTroubleCodeUdsToTroubleCodeObdMapping:
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

    def setTroubleCodeUds(self, value: "DiagnosticTroubleCode") -> DiagnosticTroubleCodeUdsToTroubleCodeObdMapping:
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

    def with_trouble_code(self, value: Optional["DiagnosticTroubleCode"]) -> DiagnosticTroubleCodeUdsToTroubleCodeObdMapping:
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

    def with_trouble_code_uds(self, value: Optional["DiagnosticTroubleCode"]) -> DiagnosticTroubleCodeUdsToTroubleCodeObdMapping:
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



class DiagnosticSwMapping(DiagnosticMapping, ABC):
    """
    This represents the ability to define a mapping between a diagnostic
    information (at this point there is no way to become more specific about the
    semantics) to a software-component.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::DiagnosticSwMapping

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 238, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is DiagnosticSwMapping:
            raise TypeError("DiagnosticSwMapping is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DiagnosticAuthTransmitCertificateMapping(DiagnosticMapping):
    """
    This meta-class represents the ability to associate a
    CryptoServiceCertificate with a DiagnosticAuth CertificateEvaluation with
    the purpose to configure the evaluation of the certificate.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::DiagnosticAuthTransmitCertificateMapping

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 242, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference identifies the description of the applicable crypto
        # certificate.
        self._cryptoService: List["CryptoService"] = []

    @property
    def crypto_service(self) -> List["CryptoService"]:
        """Get cryptoService (Pythonic accessor)."""
        return self._cryptoService
        # This reference identifies the applicable DiagnosticAuth service instance (via
        # the aggregation role certificateEvaluation).
        self._serviceInstance: Optional["DiagnosticAuthTransmit"] = None

    @property
    def service_instance(self) -> Optional["DiagnosticAuthTransmit"]:
        """Get serviceInstance (Pythonic accessor)."""
        return self._serviceInstance

    @service_instance.setter
    def service_instance(self, value: Optional["DiagnosticAuthTransmit"]) -> None:
        """
        Set serviceInstance with validation.

        Args:
            value: The serviceInstance to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._serviceInstance = None
            return

        if not isinstance(value, DiagnosticAuthTransmit):
            raise TypeError(
                f"serviceInstance must be DiagnosticAuthTransmit or None, got {type(value).__name__}"
            )
        self._serviceInstance = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCryptoService(self) -> List["CryptoService"]:
        """
        AUTOSAR-compliant getter for cryptoService.

        Returns:
            The cryptoService value

        Note:
            Delegates to crypto_service property (CODING_RULE_V2_00017)
        """
        return self.crypto_service  # Delegates to property

    def getServiceInstance(self) -> "DiagnosticAuthTransmit":
        """
        AUTOSAR-compliant getter for serviceInstance.

        Returns:
            The serviceInstance value

        Note:
            Delegates to service_instance property (CODING_RULE_V2_00017)
        """
        return self.service_instance  # Delegates to property

    def setServiceInstance(self, value: "DiagnosticAuthTransmit") -> DiagnosticAuthTransmitCertificateMapping:
        """
        AUTOSAR-compliant setter for serviceInstance with method chaining.

        Args:
            value: The serviceInstance to set

        Returns:
            self for method chaining

        Note:
            Delegates to service_instance property setter (gets validation automatically)
        """
        self.service_instance = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_service_instance(self, value: Optional["DiagnosticAuthTransmit"]) -> DiagnosticAuthTransmitCertificateMapping:
        """
        Set serviceInstance and return self for chaining.

        Args:
            value: The serviceInstance to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_service_instance("value")
        """
        self.service_instance = value  # Use property setter (gets validation)
        return self



class DiagnosticEventToTroubleCodeUdsMapping(DiagnosticMapping):
    """
    Defines which UDS Diagnostic Trouble Code is applicable for a
    DiagnosticEvent.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::DiagnosticEventToTroubleCodeUdsMapping

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 245, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to a DiagnosticEvent to which a UDS Code is assigned.
        self._diagnosticEvent: Optional["DiagnosticEvent"] = None

    @property
    def diagnostic_event(self) -> Optional["DiagnosticEvent"]:
        """Get diagnosticEvent (Pythonic accessor)."""
        return self._diagnosticEvent

    @diagnostic_event.setter
    def diagnostic_event(self, value: Optional["DiagnosticEvent"]) -> None:
        """
        Set diagnosticEvent with validation.

        Args:
            value: The diagnosticEvent to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._diagnosticEvent = None
            return

        if not isinstance(value, DiagnosticEvent):
            raise TypeError(
                f"diagnosticEvent must be DiagnosticEvent or None, got {type(value).__name__}"
            )
        self._diagnosticEvent = value
        # Reference to an UDS Diagnostic Trouble Code assigned a DiagnosticEvent.
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

    def getDiagnosticEvent(self) -> "DiagnosticEvent":
        """
        AUTOSAR-compliant getter for diagnosticEvent.

        Returns:
            The diagnosticEvent value

        Note:
            Delegates to diagnostic_event property (CODING_RULE_V2_00017)
        """
        return self.diagnostic_event  # Delegates to property

    def setDiagnosticEvent(self, value: "DiagnosticEvent") -> DiagnosticEventToTroubleCodeUdsMapping:
        """
        AUTOSAR-compliant setter for diagnosticEvent with method chaining.

        Args:
            value: The diagnosticEvent to set

        Returns:
            self for method chaining

        Note:
            Delegates to diagnostic_event property setter (gets validation automatically)
        """
        self.diagnostic_event = value  # Delegates to property setter
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

    def setTroubleCodeUds(self, value: "DiagnosticTroubleCode") -> DiagnosticEventToTroubleCodeUdsMapping:
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

    def with_diagnostic_event(self, value: Optional["DiagnosticEvent"]) -> DiagnosticEventToTroubleCodeUdsMapping:
        """
        Set diagnosticEvent and return self for chaining.

        Args:
            value: The diagnosticEvent to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_diagnostic_event("value")
        """
        self.diagnostic_event = value  # Use property setter (gets validation)
        return self

    def with_trouble_code_uds(self, value: Optional["DiagnosticTroubleCode"]) -> DiagnosticEventToTroubleCodeUdsMapping:
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



class DiagnosticEventToOperationCycleMapping(DiagnosticMapping):
    """
    Defines which OperationCycle is applicable for a DiagnosticEvent.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::DiagnosticEventToOperationCycleMapping

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 245, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to a DiagnosticEvent to which an Operation assigned.
        self._diagnosticEvent: Optional["DiagnosticEvent"] = None

    @property
    def diagnostic_event(self) -> Optional["DiagnosticEvent"]:
        """Get diagnosticEvent (Pythonic accessor)."""
        return self._diagnosticEvent

    @diagnostic_event.setter
    def diagnostic_event(self, value: Optional["DiagnosticEvent"]) -> None:
        """
        Set diagnosticEvent with validation.

        Args:
            value: The diagnosticEvent to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._diagnosticEvent = None
            return

        if not isinstance(value, DiagnosticEvent):
            raise TypeError(
                f"diagnosticEvent must be DiagnosticEvent or None, got {type(value).__name__}"
            )
        self._diagnosticEvent = value
        # Reference to an OperationCycle assigned to a Diagnostic.
        self._operationCycle: Optional["DiagnosticOperation"] = None

    @property
    def operation_cycle(self) -> Optional["DiagnosticOperation"]:
        """Get operationCycle (Pythonic accessor)."""
        return self._operationCycle

    @operation_cycle.setter
    def operation_cycle(self, value: Optional["DiagnosticOperation"]) -> None:
        """
        Set operationCycle with validation.

        Args:
            value: The operationCycle to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._operationCycle = None
            return

        if not isinstance(value, DiagnosticOperation):
            raise TypeError(
                f"operationCycle must be DiagnosticOperation or None, got {type(value).__name__}"
            )
        self._operationCycle = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDiagnosticEvent(self) -> "DiagnosticEvent":
        """
        AUTOSAR-compliant getter for diagnosticEvent.

        Returns:
            The diagnosticEvent value

        Note:
            Delegates to diagnostic_event property (CODING_RULE_V2_00017)
        """
        return self.diagnostic_event  # Delegates to property

    def setDiagnosticEvent(self, value: "DiagnosticEvent") -> DiagnosticEventToOperationCycleMapping:
        """
        AUTOSAR-compliant setter for diagnosticEvent with method chaining.

        Args:
            value: The diagnosticEvent to set

        Returns:
            self for method chaining

        Note:
            Delegates to diagnostic_event property setter (gets validation automatically)
        """
        self.diagnostic_event = value  # Delegates to property setter
        return self

    def getOperationCycle(self) -> "DiagnosticOperation":
        """
        AUTOSAR-compliant getter for operationCycle.

        Returns:
            The operationCycle value

        Note:
            Delegates to operation_cycle property (CODING_RULE_V2_00017)
        """
        return self.operation_cycle  # Delegates to property

    def setOperationCycle(self, value: "DiagnosticOperation") -> DiagnosticEventToOperationCycleMapping:
        """
        AUTOSAR-compliant setter for operationCycle with method chaining.

        Args:
            value: The operationCycle to set

        Returns:
            self for method chaining

        Note:
            Delegates to operation_cycle property setter (gets validation automatically)
        """
        self.operation_cycle = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_diagnostic_event(self, value: Optional["DiagnosticEvent"]) -> DiagnosticEventToOperationCycleMapping:
        """
        Set diagnosticEvent and return self for chaining.

        Args:
            value: The diagnosticEvent to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_diagnostic_event("value")
        """
        self.diagnostic_event = value  # Use property setter (gets validation)
        return self

    def with_operation_cycle(self, value: Optional["DiagnosticOperation"]) -> DiagnosticEventToOperationCycleMapping:
        """
        Set operationCycle and return self for chaining.

        Args:
            value: The operationCycle to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_operation_cycle("value")
        """
        self.operation_cycle = value  # Use property setter (gets validation)
        return self



class DiagnosticEventToDebounceAlgorithmMapping(DiagnosticMapping):
    """
    Defines which Debounce Algorithm is applicable for a DiagnosticEvent.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::DiagnosticEventToDebounceAlgorithmMapping

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 246, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to a DebounceAlgorithm assigned to a DiagnosticEvent.
        self._debounce: Optional["DiagnosticDebounce"] = None

    @property
    def debounce(self) -> Optional["DiagnosticDebounce"]:
        """Get debounce (Pythonic accessor)."""
        return self._debounce

    @debounce.setter
    def debounce(self, value: Optional["DiagnosticDebounce"]) -> None:
        """
        Set debounce with validation.

        Args:
            value: The debounce to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._debounce = None
            return

        if not isinstance(value, DiagnosticDebounce):
            raise TypeError(
                f"debounce must be DiagnosticDebounce or None, got {type(value).__name__}"
            )
        self._debounce = value
        # Reference to a DiagnosticEvent to which a Debounce assigned.
        self._diagnosticEvent: Optional["DiagnosticEvent"] = None

    @property
    def diagnostic_event(self) -> Optional["DiagnosticEvent"]:
        """Get diagnosticEvent (Pythonic accessor)."""
        return self._diagnosticEvent

    @diagnostic_event.setter
    def diagnostic_event(self, value: Optional["DiagnosticEvent"]) -> None:
        """
        Set diagnosticEvent with validation.

        Args:
            value: The diagnosticEvent to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._diagnosticEvent = None
            return

        if not isinstance(value, DiagnosticEvent):
            raise TypeError(
                f"diagnosticEvent must be DiagnosticEvent or None, got {type(value).__name__}"
            )
        self._diagnosticEvent = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDebounce(self) -> "DiagnosticDebounce":
        """
        AUTOSAR-compliant getter for debounce.

        Returns:
            The debounce value

        Note:
            Delegates to debounce property (CODING_RULE_V2_00017)
        """
        return self.debounce  # Delegates to property

    def setDebounce(self, value: "DiagnosticDebounce") -> DiagnosticEventToDebounceAlgorithmMapping:
        """
        AUTOSAR-compliant setter for debounce with method chaining.

        Args:
            value: The debounce to set

        Returns:
            self for method chaining

        Note:
            Delegates to debounce property setter (gets validation automatically)
        """
        self.debounce = value  # Delegates to property setter
        return self

    def getDiagnosticEvent(self) -> "DiagnosticEvent":
        """
        AUTOSAR-compliant getter for diagnosticEvent.

        Returns:
            The diagnosticEvent value

        Note:
            Delegates to diagnostic_event property (CODING_RULE_V2_00017)
        """
        return self.diagnostic_event  # Delegates to property

    def setDiagnosticEvent(self, value: "DiagnosticEvent") -> DiagnosticEventToDebounceAlgorithmMapping:
        """
        AUTOSAR-compliant setter for diagnosticEvent with method chaining.

        Args:
            value: The diagnosticEvent to set

        Returns:
            self for method chaining

        Note:
            Delegates to diagnostic_event property setter (gets validation automatically)
        """
        self.diagnostic_event = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_debounce(self, value: Optional["DiagnosticDebounce"]) -> DiagnosticEventToDebounceAlgorithmMapping:
        """
        Set debounce and return self for chaining.

        Args:
            value: The debounce to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_debounce("value")
        """
        self.debounce = value  # Use property setter (gets validation)
        return self

    def with_diagnostic_event(self, value: Optional["DiagnosticEvent"]) -> DiagnosticEventToDebounceAlgorithmMapping:
        """
        Set diagnosticEvent and return self for chaining.

        Args:
            value: The diagnosticEvent to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_diagnostic_event("value")
        """
        self.diagnostic_event = value  # Use property setter (gets validation)
        return self



class DiagnosticEventToEnableConditionGroupMapping(DiagnosticMapping):
    """
    Defines which EnableConditionGroup is applicable for a DiagnosticEvent.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::DiagnosticEventToEnableConditionGroupMapping

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 247, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to a DiagnosticEvent to which an Enable assigned.
        self._diagnosticEvent: Optional["DiagnosticEvent"] = None

    @property
    def diagnostic_event(self) -> Optional["DiagnosticEvent"]:
        """Get diagnosticEvent (Pythonic accessor)."""
        return self._diagnosticEvent

    @diagnostic_event.setter
    def diagnostic_event(self, value: Optional["DiagnosticEvent"]) -> None:
        """
        Set diagnosticEvent with validation.

        Args:
            value: The diagnosticEvent to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._diagnosticEvent = None
            return

        if not isinstance(value, DiagnosticEvent):
            raise TypeError(
                f"diagnosticEvent must be DiagnosticEvent or None, got {type(value).__name__}"
            )
        self._diagnosticEvent = value
        # Reference to an EnableConditionGroup assigned to a DiagnosticEvent.
        self._enableCondition: Optional["DiagnosticEnable"] = None

    @property
    def enable_condition(self) -> Optional["DiagnosticEnable"]:
        """Get enableCondition (Pythonic accessor)."""
        return self._enableCondition

    @enable_condition.setter
    def enable_condition(self, value: Optional["DiagnosticEnable"]) -> None:
        """
        Set enableCondition with validation.

        Args:
            value: The enableCondition to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._enableCondition = None
            return

        if not isinstance(value, DiagnosticEnable):
            raise TypeError(
                f"enableCondition must be DiagnosticEnable or None, got {type(value).__name__}"
            )
        self._enableCondition = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDiagnosticEvent(self) -> "DiagnosticEvent":
        """
        AUTOSAR-compliant getter for diagnosticEvent.

        Returns:
            The diagnosticEvent value

        Note:
            Delegates to diagnostic_event property (CODING_RULE_V2_00017)
        """
        return self.diagnostic_event  # Delegates to property

    def setDiagnosticEvent(self, value: "DiagnosticEvent") -> DiagnosticEventToEnableConditionGroupMapping:
        """
        AUTOSAR-compliant setter for diagnosticEvent with method chaining.

        Args:
            value: The diagnosticEvent to set

        Returns:
            self for method chaining

        Note:
            Delegates to diagnostic_event property setter (gets validation automatically)
        """
        self.diagnostic_event = value  # Delegates to property setter
        return self

    def getEnableCondition(self) -> "DiagnosticEnable":
        """
        AUTOSAR-compliant getter for enableCondition.

        Returns:
            The enableCondition value

        Note:
            Delegates to enable_condition property (CODING_RULE_V2_00017)
        """
        return self.enable_condition  # Delegates to property

    def setEnableCondition(self, value: "DiagnosticEnable") -> DiagnosticEventToEnableConditionGroupMapping:
        """
        AUTOSAR-compliant setter for enableCondition with method chaining.

        Args:
            value: The enableCondition to set

        Returns:
            self for method chaining

        Note:
            Delegates to enable_condition property setter (gets validation automatically)
        """
        self.enable_condition = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_diagnostic_event(self, value: Optional["DiagnosticEvent"]) -> DiagnosticEventToEnableConditionGroupMapping:
        """
        Set diagnosticEvent and return self for chaining.

        Args:
            value: The diagnosticEvent to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_diagnostic_event("value")
        """
        self.diagnostic_event = value  # Use property setter (gets validation)
        return self

    def with_enable_condition(self, value: Optional["DiagnosticEnable"]) -> DiagnosticEventToEnableConditionGroupMapping:
        """
        Set enableCondition and return self for chaining.

        Args:
            value: The enableCondition to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_enable_condition("value")
        """
        self.enable_condition = value  # Use property setter (gets validation)
        return self



class DiagnosticEventToStorageConditionGroupMapping(DiagnosticMapping):
    """
    Defines which StorageConditionGroup is applicable for a DiagnosticEvent.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::DiagnosticEventToStorageConditionGroupMapping

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 248, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to a DiagnosticEvent to which a Storage assigned.
        self._diagnosticEvent: Optional["DiagnosticEvent"] = None

    @property
    def diagnostic_event(self) -> Optional["DiagnosticEvent"]:
        """Get diagnosticEvent (Pythonic accessor)."""
        return self._diagnosticEvent

    @diagnostic_event.setter
    def diagnostic_event(self, value: Optional["DiagnosticEvent"]) -> None:
        """
        Set diagnosticEvent with validation.

        Args:
            value: The diagnosticEvent to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._diagnosticEvent = None
            return

        if not isinstance(value, DiagnosticEvent):
            raise TypeError(
                f"diagnosticEvent must be DiagnosticEvent or None, got {type(value).__name__}"
            )
        self._diagnosticEvent = value
        # Reference to a StorageConditionGroup assigned to a DiagnosticEvent.
        self._storage: Optional["DiagnosticStorage"] = None

    @property
    def storage(self) -> Optional["DiagnosticStorage"]:
        """Get storage (Pythonic accessor)."""
        return self._storage

    @storage.setter
    def storage(self, value: Optional["DiagnosticStorage"]) -> None:
        """
        Set storage with validation.

        Args:
            value: The storage to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._storage = None
            return

        if not isinstance(value, DiagnosticStorage):
            raise TypeError(
                f"storage must be DiagnosticStorage or None, got {type(value).__name__}"
            )
        self._storage = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDiagnosticEvent(self) -> "DiagnosticEvent":
        """
        AUTOSAR-compliant getter for diagnosticEvent.

        Returns:
            The diagnosticEvent value

        Note:
            Delegates to diagnostic_event property (CODING_RULE_V2_00017)
        """
        return self.diagnostic_event  # Delegates to property

    def setDiagnosticEvent(self, value: "DiagnosticEvent") -> DiagnosticEventToStorageConditionGroupMapping:
        """
        AUTOSAR-compliant setter for diagnosticEvent with method chaining.

        Args:
            value: The diagnosticEvent to set

        Returns:
            self for method chaining

        Note:
            Delegates to diagnostic_event property setter (gets validation automatically)
        """
        self.diagnostic_event = value  # Delegates to property setter
        return self

    def getStorage(self) -> "DiagnosticStorage":
        """
        AUTOSAR-compliant getter for storage.

        Returns:
            The storage value

        Note:
            Delegates to storage property (CODING_RULE_V2_00017)
        """
        return self.storage  # Delegates to property

    def setStorage(self, value: "DiagnosticStorage") -> DiagnosticEventToStorageConditionGroupMapping:
        """
        AUTOSAR-compliant setter for storage with method chaining.

        Args:
            value: The storage to set

        Returns:
            self for method chaining

        Note:
            Delegates to storage property setter (gets validation automatically)
        """
        self.storage = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_diagnostic_event(self, value: Optional["DiagnosticEvent"]) -> DiagnosticEventToStorageConditionGroupMapping:
        """
        Set diagnosticEvent and return self for chaining.

        Args:
            value: The diagnosticEvent to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_diagnostic_event("value")
        """
        self.diagnostic_event = value  # Use property setter (gets validation)
        return self

    def with_storage(self, value: Optional["DiagnosticStorage"]) -> DiagnosticEventToStorageConditionGroupMapping:
        """
        Set storage and return self for chaining.

        Args:
            value: The storage to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_storage("value")
        """
        self.storage = value  # Use property setter (gets validation)
        return self



class DiagnosticMasterToSlaveEventMapping(DiagnosticMapping):
    """
    This meta-class provides the ability to map a master diagnostic event with a
    slave diagnostic event such that reporting of the master event with a given
    value also reports the slave event with the same value

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::DiagnosticMasterToSlaveEventMapping

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 256, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the master diagnostic event.
        self._masterEvent: Optional["DiagnosticEvent"] = None

    @property
    def master_event(self) -> Optional["DiagnosticEvent"]:
        """Get masterEvent (Pythonic accessor)."""
        return self._masterEvent

    @master_event.setter
    def master_event(self, value: Optional["DiagnosticEvent"]) -> None:
        """
        Set masterEvent with validation.

        Args:
            value: The masterEvent to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._masterEvent = None
            return

        if not isinstance(value, DiagnosticEvent):
            raise TypeError(
                f"masterEvent must be DiagnosticEvent or None, got {type(value).__name__}"
            )
        self._masterEvent = value
        # This represents the slave diagnostic event.
        self._slaveEvent: Optional["DiagnosticEvent"] = None

    @property
    def slave_event(self) -> Optional["DiagnosticEvent"]:
        """Get slaveEvent (Pythonic accessor)."""
        return self._slaveEvent

    @slave_event.setter
    def slave_event(self, value: Optional["DiagnosticEvent"]) -> None:
        """
        Set slaveEvent with validation.

        Args:
            value: The slaveEvent to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._slaveEvent = None
            return

        if not isinstance(value, DiagnosticEvent):
            raise TypeError(
                f"slaveEvent must be DiagnosticEvent or None, got {type(value).__name__}"
            )
        self._slaveEvent = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMasterEvent(self) -> "DiagnosticEvent":
        """
        AUTOSAR-compliant getter for masterEvent.

        Returns:
            The masterEvent value

        Note:
            Delegates to master_event property (CODING_RULE_V2_00017)
        """
        return self.master_event  # Delegates to property

    def setMasterEvent(self, value: "DiagnosticEvent") -> DiagnosticMasterToSlaveEventMapping:
        """
        AUTOSAR-compliant setter for masterEvent with method chaining.

        Args:
            value: The masterEvent to set

        Returns:
            self for method chaining

        Note:
            Delegates to master_event property setter (gets validation automatically)
        """
        self.master_event = value  # Delegates to property setter
        return self

    def getSlaveEvent(self) -> "DiagnosticEvent":
        """
        AUTOSAR-compliant getter for slaveEvent.

        Returns:
            The slaveEvent value

        Note:
            Delegates to slave_event property (CODING_RULE_V2_00017)
        """
        return self.slave_event  # Delegates to property

    def setSlaveEvent(self, value: "DiagnosticEvent") -> DiagnosticMasterToSlaveEventMapping:
        """
        AUTOSAR-compliant setter for slaveEvent with method chaining.

        Args:
            value: The slaveEvent to set

        Returns:
            self for method chaining

        Note:
            Delegates to slave_event property setter (gets validation automatically)
        """
        self.slave_event = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_master_event(self, value: Optional["DiagnosticEvent"]) -> DiagnosticMasterToSlaveEventMapping:
        """
        Set masterEvent and return self for chaining.

        Args:
            value: The masterEvent to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_master_event("value")
        """
        self.master_event = value  # Use property setter (gets validation)
        return self

    def with_slave_event(self, value: Optional["DiagnosticEvent"]) -> DiagnosticMasterToSlaveEventMapping:
        """
        Set slaveEvent and return self for chaining.

        Args:
            value: The slaveEvent to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_slave_event("value")
        """
        self.slave_event = value  # Use property setter (gets validation)
        return self



class DiagnosticEventToSecurityEventMapping(DiagnosticMapping):
    """
    This meta-class represents the ability to map a security event that is
    defined in the context of the Security Extract to a diagnostic event defined
    on the context of the DiagnosticExtract.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::DiagnosticEventToSecurityEventMapping

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 257, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference identifies the applicable diagnostic event.
        self._diagnosticEvent: Optional["DiagnosticEvent"] = None

    @property
    def diagnostic_event(self) -> Optional["DiagnosticEvent"]:
        """Get diagnosticEvent (Pythonic accessor)."""
        return self._diagnosticEvent

    @diagnostic_event.setter
    def diagnostic_event(self, value: Optional["DiagnosticEvent"]) -> None:
        """
        Set diagnosticEvent with validation.

        Args:
            value: The diagnosticEvent to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._diagnosticEvent = None
            return

        if not isinstance(value, DiagnosticEvent):
            raise TypeError(
                f"diagnosticEvent must be DiagnosticEvent or None, got {type(value).__name__}"
            )
        self._diagnosticEvent = value
        # This reference identifies the qualification of the applicable security event.
        self._securityEvent: Optional["SecurityEventContext"] = None

    @property
    def security_event(self) -> Optional["SecurityEventContext"]:
        """Get securityEvent (Pythonic accessor)."""
        return self._securityEvent

    @security_event.setter
    def security_event(self, value: Optional["SecurityEventContext"]) -> None:
        """
        Set securityEvent with validation.

        Args:
            value: The securityEvent to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._securityEvent = None
            return

        if not isinstance(value, SecurityEventContext):
            raise TypeError(
                f"securityEvent must be SecurityEventContext or None, got {type(value).__name__}"
            )
        self._securityEvent = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDiagnosticEvent(self) -> "DiagnosticEvent":
        """
        AUTOSAR-compliant getter for diagnosticEvent.

        Returns:
            The diagnosticEvent value

        Note:
            Delegates to diagnostic_event property (CODING_RULE_V2_00017)
        """
        return self.diagnostic_event  # Delegates to property

    def setDiagnosticEvent(self, value: "DiagnosticEvent") -> DiagnosticEventToSecurityEventMapping:
        """
        AUTOSAR-compliant setter for diagnosticEvent with method chaining.

        Args:
            value: The diagnosticEvent to set

        Returns:
            self for method chaining

        Note:
            Delegates to diagnostic_event property setter (gets validation automatically)
        """
        self.diagnostic_event = value  # Delegates to property setter
        return self

    def getSecurityEvent(self) -> "SecurityEventContext":
        """
        AUTOSAR-compliant getter for securityEvent.

        Returns:
            The securityEvent value

        Note:
            Delegates to security_event property (CODING_RULE_V2_00017)
        """
        return self.security_event  # Delegates to property

    def setSecurityEvent(self, value: "SecurityEventContext") -> DiagnosticEventToSecurityEventMapping:
        """
        AUTOSAR-compliant setter for securityEvent with method chaining.

        Args:
            value: The securityEvent to set

        Returns:
            self for method chaining

        Note:
            Delegates to security_event property setter (gets validation automatically)
        """
        self.security_event = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_diagnostic_event(self, value: Optional["DiagnosticEvent"]) -> DiagnosticEventToSecurityEventMapping:
        """
        Set diagnosticEvent and return self for chaining.

        Args:
            value: The diagnosticEvent to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_diagnostic_event("value")
        """
        self.diagnostic_event = value  # Use property setter (gets validation)
        return self

    def with_security_event(self, value: Optional["SecurityEventContext"]) -> DiagnosticEventToSecurityEventMapping:
        """
        Set securityEvent and return self for chaining.

        Args:
            value: The securityEvent to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_security_event("value")
        """
        self.security_event = value  # Use property setter (gets validation)
        return self



class DiagnosticIumprToFunctionIdentifierMapping(DiagnosticMapping):
    """
    This meta-class represents the ability to associate a
    DiagnosticFunctionIdentifier with a DiagnosticIumpr.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::DiagnosticIumprToFunctionIdentifierMapping

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 265, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference identifies the applicable Diagnostic FunctionIdentifier.
        self._function: Optional["DiagnosticFunction"] = None

    @property
    def function(self) -> Optional["DiagnosticFunction"]:
        """Get function (Pythonic accessor)."""
        return self._function

    @function.setter
    def function(self, value: Optional["DiagnosticFunction"]) -> None:
        """
        Set function with validation.

        Args:
            value: The function to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._function = None
            return

        if not isinstance(value, DiagnosticFunction):
            raise TypeError(
                f"function must be DiagnosticFunction or None, got {type(value).__name__}"
            )
        self._function = value
        # This reference identifies the applicable DiagnosticIumpr.
        self._iumpr: Optional["DiagnosticIumpr"] = None

    @property
    def iumpr(self) -> Optional["DiagnosticIumpr"]:
        """Get iumpr (Pythonic accessor)."""
        return self._iumpr

    @iumpr.setter
    def iumpr(self, value: Optional["DiagnosticIumpr"]) -> None:
        """
        Set iumpr with validation.

        Args:
            value: The iumpr to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._iumpr = None
            return

        if not isinstance(value, DiagnosticIumpr):
            raise TypeError(
                f"iumpr must be DiagnosticIumpr or None, got {type(value).__name__}"
            )
        self._iumpr = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFunction(self) -> "DiagnosticFunction":
        """
        AUTOSAR-compliant getter for function.

        Returns:
            The function value

        Note:
            Delegates to function property (CODING_RULE_V2_00017)
        """
        return self.function  # Delegates to property

    def setFunction(self, value: "DiagnosticFunction") -> DiagnosticIumprToFunctionIdentifierMapping:
        """
        AUTOSAR-compliant setter for function with method chaining.

        Args:
            value: The function to set

        Returns:
            self for method chaining

        Note:
            Delegates to function property setter (gets validation automatically)
        """
        self.function = value  # Delegates to property setter
        return self

    def getIumpr(self) -> DiagnosticIumpr:
        """
        AUTOSAR-compliant getter for iumpr.

        Returns:
            The iumpr value

        Note:
            Delegates to iumpr property (CODING_RULE_V2_00017)
        """
        return self.iumpr  # Delegates to property

    def setIumpr(self, value: DiagnosticIumpr) -> DiagnosticIumprToFunctionIdentifierMapping:
        """
        AUTOSAR-compliant setter for iumpr with method chaining.

        Args:
            value: The iumpr to set

        Returns:
            self for method chaining

        Note:
            Delegates to iumpr property setter (gets validation automatically)
        """
        self.iumpr = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_function(self, value: Optional["DiagnosticFunction"]) -> DiagnosticIumprToFunctionIdentifierMapping:
        """
        Set function and return self for chaining.

        Args:
            value: The function to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_function("value")
        """
        self.function = value  # Use property setter (gets validation)
        return self

    def with_iumpr(self, value: Optional["DiagnosticIumpr"]) -> DiagnosticIumprToFunctionIdentifierMapping:
        """
        Set iumpr and return self for chaining.

        Args:
            value: The iumpr to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_iumpr("value")
        """
        self.iumpr = value  # Use property setter (gets validation)
        return self



class DiagnosticSecureCodingMapping(DiagnosticMapping):
    """
    This meta-class acts a mapping element to select diagnostic service
    instances that are used in the secure coding procedure. Besides, there are
    already defined diagnostic capabilities they furthermore have a additional
    semantics that is used during the secure coding process. In particular, this
    class references write data by identifier instances that mandatory require a
    secure coding and this class references a diagnostic routine control that is
    used to provide the signature and to persist the data in non-volatile
    memory.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::DiagnosticSecureCodingMapping

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 312, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Refer to write data by identifier instances that have the to be a secure
        # coding DID.
        self._dataIdentifier: List["DiagnosticWriteDataBy"] = []

    @property
    def data_identifier(self) -> List["DiagnosticWriteDataBy"]:
        """Get dataIdentifier (Pythonic accessor)."""
        return self._dataIdentifier
        # Refer to a routine control that is used to authenticate and secure coding
        # data.
        self._validation: Optional["DiagnosticStartRoutine"] = None

    @property
    def validation(self) -> Optional["DiagnosticStartRoutine"]:
        """Get validation (Pythonic accessor)."""
        return self._validation

    @validation.setter
    def validation(self, value: Optional["DiagnosticStartRoutine"]) -> None:
        """
        Set validation with validation.

        Args:
            value: The validation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._validation = None
            return

        if not isinstance(value, DiagnosticStartRoutine):
            raise TypeError(
                f"validation must be DiagnosticStartRoutine or None, got {type(value).__name__}"
            )
        self._validation = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataIdentifier(self) -> List["DiagnosticWriteDataBy"]:
        """
        AUTOSAR-compliant getter for dataIdentifier.

        Returns:
            The dataIdentifier value

        Note:
            Delegates to data_identifier property (CODING_RULE_V2_00017)
        """
        return self.data_identifier  # Delegates to property

    def getValidation(self) -> DiagnosticStartRoutine:
        """
        AUTOSAR-compliant getter for validation.

        Returns:
            The validation value

        Note:
            Delegates to validation property (CODING_RULE_V2_00017)
        """
        return self.validation  # Delegates to property

    def setValidation(self, value: DiagnosticStartRoutine) -> DiagnosticSecureCodingMapping:
        """
        AUTOSAR-compliant setter for validation with method chaining.

        Args:
            value: The validation to set

        Returns:
            self for method chaining

        Note:
            Delegates to validation property setter (gets validation automatically)
        """
        self.validation = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_validation(self, value: Optional["DiagnosticStartRoutine"]) -> DiagnosticSecureCodingMapping:
        """
        Set validation and return self for chaining.

        Args:
            value: The validation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_validation("value")
        """
        self.validation = value  # Use property setter (gets validation)
        return self



class DiagnosticEventPortMapping(DiagnosticSwMapping):
    """
    Defines to which SWC service ports the DiagnosticEvent is mapped.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::DiagnosticEventPortMapping

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 249, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to a BswServiceDependency that links Service Needs to
        # BswModuleEntries.
        self._bswService: Optional["BswService"] = None

    @property
    def bsw_service(self) -> Optional["BswService"]:
        """Get bswService (Pythonic accessor)."""
        return self._bswService

    @bsw_service.setter
    def bsw_service(self, value: Optional["BswService"]) -> None:
        """
        Set bswService with validation.

        Args:
            value: The bswService to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._bswService = None
            return

        if not isinstance(value, BswService):
            raise TypeError(
                f"bswService must be BswService or None, got {type(value).__name__}"
            )
        self._bswService = value
        # Reference to the DiagnosticEvent that is assigned to ports.
        self._diagnosticEvent: Optional["DiagnosticEvent"] = None

    @property
    def diagnostic_event(self) -> Optional["DiagnosticEvent"]:
        """Get diagnosticEvent (Pythonic accessor)."""
        return self._diagnosticEvent

    @diagnostic_event.setter
    def diagnostic_event(self, value: Optional["DiagnosticEvent"]) -> None:
        """
        Set diagnosticEvent with validation.

        Args:
            value: The diagnosticEvent to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._diagnosticEvent = None
            return

        if not isinstance(value, DiagnosticEvent):
            raise TypeError(
                f"diagnosticEvent must be DiagnosticEvent or None, got {type(value).__name__}"
            )
        self._diagnosticEvent = value
        # Reference to a SwcServiceDependencyType that links ServiceNeeds to SWC
        # service ports.
        self._swcFlatService: Optional["SwcService"] = None

    @property
    def swc_flat_service(self) -> Optional["SwcService"]:
        """Get swcFlatService (Pythonic accessor)."""
        return self._swcFlatService

    @swc_flat_service.setter
    def swc_flat_service(self, value: Optional["SwcService"]) -> None:
        """
        Set swcFlatService with validation.

        Args:
            value: The swcFlatService to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swcFlatService = None
            return

        if not isinstance(value, SwcService):
            raise TypeError(
                f"swcFlatService must be SwcService or None, got {type(value).__name__}"
            )
        self._swcFlatService = value
        # ServiceNeeds to SWC service ports.
        # implemented by: SwcServiceDependency.
        self._swcService: Optional["SwcService"] = None

    @property
    def swc_service(self) -> Optional["SwcService"]:
        """Get swcService (Pythonic accessor)."""
        return self._swcService

    @swc_service.setter
    def swc_service(self, value: Optional["SwcService"]) -> None:
        """
        Set swcService with validation.

        Args:
            value: The swcService to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swcService = None
            return

        if not isinstance(value, SwcService):
            raise TypeError(
                f"swcService must be SwcService or None, got {type(value).__name__}"
            )
        self._swcService = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBswService(self) -> "BswService":
        """
        AUTOSAR-compliant getter for bswService.

        Returns:
            The bswService value

        Note:
            Delegates to bsw_service property (CODING_RULE_V2_00017)
        """
        return self.bsw_service  # Delegates to property

    def setBswService(self, value: "BswService") -> DiagnosticEventPortMapping:
        """
        AUTOSAR-compliant setter for bswService with method chaining.

        Args:
            value: The bswService to set

        Returns:
            self for method chaining

        Note:
            Delegates to bsw_service property setter (gets validation automatically)
        """
        self.bsw_service = value  # Delegates to property setter
        return self

    def getDiagnosticEvent(self) -> "DiagnosticEvent":
        """
        AUTOSAR-compliant getter for diagnosticEvent.

        Returns:
            The diagnosticEvent value

        Note:
            Delegates to diagnostic_event property (CODING_RULE_V2_00017)
        """
        return self.diagnostic_event  # Delegates to property

    def setDiagnosticEvent(self, value: "DiagnosticEvent") -> DiagnosticEventPortMapping:
        """
        AUTOSAR-compliant setter for diagnosticEvent with method chaining.

        Args:
            value: The diagnosticEvent to set

        Returns:
            self for method chaining

        Note:
            Delegates to diagnostic_event property setter (gets validation automatically)
        """
        self.diagnostic_event = value  # Delegates to property setter
        return self

    def getSwcFlatService(self) -> "SwcService":
        """
        AUTOSAR-compliant getter for swcFlatService.

        Returns:
            The swcFlatService value

        Note:
            Delegates to swc_flat_service property (CODING_RULE_V2_00017)
        """
        return self.swc_flat_service  # Delegates to property

    def setSwcFlatService(self, value: "SwcService") -> DiagnosticEventPortMapping:
        """
        AUTOSAR-compliant setter for swcFlatService with method chaining.

        Args:
            value: The swcFlatService to set

        Returns:
            self for method chaining

        Note:
            Delegates to swc_flat_service property setter (gets validation automatically)
        """
        self.swc_flat_service = value  # Delegates to property setter
        return self

    def getSwcService(self) -> "SwcService":
        """
        AUTOSAR-compliant getter for swcService.

        Returns:
            The swcService value

        Note:
            Delegates to swc_service property (CODING_RULE_V2_00017)
        """
        return self.swc_service  # Delegates to property

    def setSwcService(self, value: "SwcService") -> DiagnosticEventPortMapping:
        """
        AUTOSAR-compliant setter for swcService with method chaining.

        Args:
            value: The swcService to set

        Returns:
            self for method chaining

        Note:
            Delegates to swc_service property setter (gets validation automatically)
        """
        self.swc_service = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bsw_service(self, value: Optional["BswService"]) -> DiagnosticEventPortMapping:
        """
        Set bswService and return self for chaining.

        Args:
            value: The bswService to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bsw_service("value")
        """
        self.bsw_service = value  # Use property setter (gets validation)
        return self

    def with_diagnostic_event(self, value: Optional["DiagnosticEvent"]) -> DiagnosticEventPortMapping:
        """
        Set diagnosticEvent and return self for chaining.

        Args:
            value: The diagnosticEvent to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_diagnostic_event("value")
        """
        self.diagnostic_event = value  # Use property setter (gets validation)
        return self

    def with_swc_flat_service(self, value: Optional["SwcService"]) -> DiagnosticEventPortMapping:
        """
        Set swcFlatService and return self for chaining.

        Args:
            value: The swcFlatService to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_swc_flat_service("value")
        """
        self.swc_flat_service = value  # Use property setter (gets validation)
        return self

    def with_swc_service(self, value: Optional["SwcService"]) -> DiagnosticEventPortMapping:
        """
        Set swcService and return self for chaining.

        Args:
            value: The swcService to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_swc_service("value")
        """
        self.swc_service = value  # Use property setter (gets validation)
        return self



class DiagnosticOperationCyclePortMapping(DiagnosticSwMapping):
    """
    Defines to which SWC service ports the DiagnosticOperationCycle is mapped.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::DiagnosticOperationCyclePortMapping

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 250, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the DiagnosticOperationCycle that is to SWC service ports.
        self._operationCycle: Optional["DiagnosticOperation"] = None

    @property
    def operation_cycle(self) -> Optional["DiagnosticOperation"]:
        """Get operationCycle (Pythonic accessor)."""
        return self._operationCycle

    @operation_cycle.setter
    def operation_cycle(self, value: Optional["DiagnosticOperation"]) -> None:
        """
        Set operationCycle with validation.

        Args:
            value: The operationCycle to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._operationCycle = None
            return

        if not isinstance(value, DiagnosticOperation):
            raise TypeError(
                f"operationCycle must be DiagnosticOperation or None, got {type(value).__name__}"
            )
        self._operationCycle = value
        # Reference to a SwcServiceDependencyType that links ServiceNeeds to SWC
        # service ports.
        self._swcFlatService: Optional["SwcService"] = None

    @property
    def swc_flat_service(self) -> Optional["SwcService"]:
        """Get swcFlatService (Pythonic accessor)."""
        return self._swcFlatService

    @swc_flat_service.setter
    def swc_flat_service(self, value: Optional["SwcService"]) -> None:
        """
        Set swcFlatService with validation.

        Args:
            value: The swcFlatService to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swcFlatService = None
            return

        if not isinstance(value, SwcService):
            raise TypeError(
                f"swcFlatService must be SwcService or None, got {type(value).__name__}"
            )
        self._swcFlatService = value
        # ServiceNeeds to SWC service ports.
        # implemented by: SwcServiceDependency.
        self._swcService: Optional["SwcService"] = None

    @property
    def swc_service(self) -> Optional["SwcService"]:
        """Get swcService (Pythonic accessor)."""
        return self._swcService

    @swc_service.setter
    def swc_service(self, value: Optional["SwcService"]) -> None:
        """
        Set swcService with validation.

        Args:
            value: The swcService to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swcService = None
            return

        if not isinstance(value, SwcService):
            raise TypeError(
                f"swcService must be SwcService or None, got {type(value).__name__}"
            )
        self._swcService = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getOperationCycle(self) -> "DiagnosticOperation":
        """
        AUTOSAR-compliant getter for operationCycle.

        Returns:
            The operationCycle value

        Note:
            Delegates to operation_cycle property (CODING_RULE_V2_00017)
        """
        return self.operation_cycle  # Delegates to property

    def setOperationCycle(self, value: "DiagnosticOperation") -> DiagnosticOperationCyclePortMapping:
        """
        AUTOSAR-compliant setter for operationCycle with method chaining.

        Args:
            value: The operationCycle to set

        Returns:
            self for method chaining

        Note:
            Delegates to operation_cycle property setter (gets validation automatically)
        """
        self.operation_cycle = value  # Delegates to property setter
        return self

    def getSwcFlatService(self) -> "SwcService":
        """
        AUTOSAR-compliant getter for swcFlatService.

        Returns:
            The swcFlatService value

        Note:
            Delegates to swc_flat_service property (CODING_RULE_V2_00017)
        """
        return self.swc_flat_service  # Delegates to property

    def setSwcFlatService(self, value: "SwcService") -> DiagnosticOperationCyclePortMapping:
        """
        AUTOSAR-compliant setter for swcFlatService with method chaining.

        Args:
            value: The swcFlatService to set

        Returns:
            self for method chaining

        Note:
            Delegates to swc_flat_service property setter (gets validation automatically)
        """
        self.swc_flat_service = value  # Delegates to property setter
        return self

    def getSwcService(self) -> "SwcService":
        """
        AUTOSAR-compliant getter for swcService.

        Returns:
            The swcService value

        Note:
            Delegates to swc_service property (CODING_RULE_V2_00017)
        """
        return self.swc_service  # Delegates to property

    def setSwcService(self, value: "SwcService") -> DiagnosticOperationCyclePortMapping:
        """
        AUTOSAR-compliant setter for swcService with method chaining.

        Args:
            value: The swcService to set

        Returns:
            self for method chaining

        Note:
            Delegates to swc_service property setter (gets validation automatically)
        """
        self.swc_service = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_operation_cycle(self, value: Optional["DiagnosticOperation"]) -> DiagnosticOperationCyclePortMapping:
        """
        Set operationCycle and return self for chaining.

        Args:
            value: The operationCycle to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_operation_cycle("value")
        """
        self.operation_cycle = value  # Use property setter (gets validation)
        return self

    def with_swc_flat_service(self, value: Optional["SwcService"]) -> DiagnosticOperationCyclePortMapping:
        """
        Set swcFlatService and return self for chaining.

        Args:
            value: The swcFlatService to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_swc_flat_service("value")
        """
        self.swc_flat_service = value  # Use property setter (gets validation)
        return self

    def with_swc_service(self, value: Optional["SwcService"]) -> DiagnosticOperationCyclePortMapping:
        """
        Set swcService and return self for chaining.

        Args:
            value: The swcService to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_swc_service("value")
        """
        self.swc_service = value  # Use property setter (gets validation)
        return self



class DiagnosticEnableConditionPortMapping(DiagnosticSwMapping):
    """
    Defines to which SWC service ports the DiagnosticEnableCondition is mapped.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::DiagnosticEnableConditionPortMapping

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 251, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the EnableCondition which is mapped to a service port.
        self._enableCondition: Optional["DiagnosticEnable"] = None

    @property
    def enable_condition(self) -> Optional["DiagnosticEnable"]:
        """Get enableCondition (Pythonic accessor)."""
        return self._enableCondition

    @enable_condition.setter
    def enable_condition(self, value: Optional["DiagnosticEnable"]) -> None:
        """
        Set enableCondition with validation.

        Args:
            value: The enableCondition to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._enableCondition = None
            return

        if not isinstance(value, DiagnosticEnable):
            raise TypeError(
                f"enableCondition must be DiagnosticEnable or None, got {type(value).__name__}"
            )
        self._enableCondition = value
        # Reference to a SwcServiceDependencyType that links ServiceNeeds to SWC
                # service ports.
        # This reference can in early stages of the development in order to
                # SwcServiceDependency without a full System.
        self._swcFlatService: Optional["SwcService"] = None

    @property
    def swc_flat_service(self) -> Optional["SwcService"]:
        """Get swcFlatService (Pythonic accessor)."""
        return self._swcFlatService

    @swc_flat_service.setter
    def swc_flat_service(self, value: Optional["SwcService"]) -> None:
        """
        Set swcFlatService with validation.

        Args:
            value: The swcFlatService to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swcFlatService = None
            return

        if not isinstance(value, SwcService):
            raise TypeError(
                f"swcFlatService must be SwcService or None, got {type(value).__name__}"
            )
        self._swcFlatService = value
        # ServiceNeeds to SWC service ports.
        # implemented by: SwcServiceDependency.
        self._swcService: Optional["SwcService"] = None

    @property
    def swc_service(self) -> Optional["SwcService"]:
        """Get swcService (Pythonic accessor)."""
        return self._swcService

    @swc_service.setter
    def swc_service(self, value: Optional["SwcService"]) -> None:
        """
        Set swcService with validation.

        Args:
            value: The swcService to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swcService = None
            return

        if not isinstance(value, SwcService):
            raise TypeError(
                f"swcService must be SwcService or None, got {type(value).__name__}"
            )
        self._swcService = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEnableCondition(self) -> "DiagnosticEnable":
        """
        AUTOSAR-compliant getter for enableCondition.

        Returns:
            The enableCondition value

        Note:
            Delegates to enable_condition property (CODING_RULE_V2_00017)
        """
        return self.enable_condition  # Delegates to property

    def setEnableCondition(self, value: "DiagnosticEnable") -> DiagnosticEnableConditionPortMapping:
        """
        AUTOSAR-compliant setter for enableCondition with method chaining.

        Args:
            value: The enableCondition to set

        Returns:
            self for method chaining

        Note:
            Delegates to enable_condition property setter (gets validation automatically)
        """
        self.enable_condition = value  # Delegates to property setter
        return self

    def getSwcFlatService(self) -> "SwcService":
        """
        AUTOSAR-compliant getter for swcFlatService.

        Returns:
            The swcFlatService value

        Note:
            Delegates to swc_flat_service property (CODING_RULE_V2_00017)
        """
        return self.swc_flat_service  # Delegates to property

    def setSwcFlatService(self, value: "SwcService") -> DiagnosticEnableConditionPortMapping:
        """
        AUTOSAR-compliant setter for swcFlatService with method chaining.

        Args:
            value: The swcFlatService to set

        Returns:
            self for method chaining

        Note:
            Delegates to swc_flat_service property setter (gets validation automatically)
        """
        self.swc_flat_service = value  # Delegates to property setter
        return self

    def getSwcService(self) -> "SwcService":
        """
        AUTOSAR-compliant getter for swcService.

        Returns:
            The swcService value

        Note:
            Delegates to swc_service property (CODING_RULE_V2_00017)
        """
        return self.swc_service  # Delegates to property

    def setSwcService(self, value: "SwcService") -> DiagnosticEnableConditionPortMapping:
        """
        AUTOSAR-compliant setter for swcService with method chaining.

        Args:
            value: The swcService to set

        Returns:
            self for method chaining

        Note:
            Delegates to swc_service property setter (gets validation automatically)
        """
        self.swc_service = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_enable_condition(self, value: Optional["DiagnosticEnable"]) -> DiagnosticEnableConditionPortMapping:
        """
        Set enableCondition and return self for chaining.

        Args:
            value: The enableCondition to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_enable_condition("value")
        """
        self.enable_condition = value  # Use property setter (gets validation)
        return self

    def with_swc_flat_service(self, value: Optional["SwcService"]) -> DiagnosticEnableConditionPortMapping:
        """
        Set swcFlatService and return self for chaining.

        Args:
            value: The swcFlatService to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_swc_flat_service("value")
        """
        self.swc_flat_service = value  # Use property setter (gets validation)
        return self

    def with_swc_service(self, value: Optional["SwcService"]) -> DiagnosticEnableConditionPortMapping:
        """
        Set swcService and return self for chaining.

        Args:
            value: The swcService to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_swc_service("value")
        """
        self.swc_service = value  # Use property setter (gets validation)
        return self



class DiagnosticStorageConditionPortMapping(DiagnosticSwMapping):
    """
    Defines to which SWC service ports with DiagnosticStorageConditionNeeds the
    DiagnosticStorage Condition is mapped.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::DiagnosticStorageConditionPortMapping

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 253, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the StorageCondition which is mapped to a SWC service port with
        # DiagnosticStorageCondition.
        self._diagnostic: Optional["DiagnosticStorage"] = None

    @property
    def diagnostic(self) -> Optional["DiagnosticStorage"]:
        """Get diagnostic (Pythonic accessor)."""
        return self._diagnostic

    @diagnostic.setter
    def diagnostic(self, value: Optional["DiagnosticStorage"]) -> None:
        """
        Set diagnostic with validation.

        Args:
            value: The diagnostic to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._diagnostic = None
            return

        if not isinstance(value, DiagnosticStorage):
            raise TypeError(
                f"diagnostic must be DiagnosticStorage or None, got {type(value).__name__}"
            )
        self._diagnostic = value
        # Reference to a SwcServiceDependencyType that links ServiceNeeds to SWC
        # service ports.
        self._swcFlatService: Optional["SwcService"] = None

    @property
    def swc_flat_service(self) -> Optional["SwcService"]:
        """Get swcFlatService (Pythonic accessor)."""
        return self._swcFlatService

    @swc_flat_service.setter
    def swc_flat_service(self, value: Optional["SwcService"]) -> None:
        """
        Set swcFlatService with validation.

        Args:
            value: The swcFlatService to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swcFlatService = None
            return

        if not isinstance(value, SwcService):
            raise TypeError(
                f"swcFlatService must be SwcService or None, got {type(value).__name__}"
            )
        self._swcFlatService = value
        # ServiceNeeds to SWC service ports.
        # implemented by: SwcServiceDependency.
        self._swcService: Optional["SwcService"] = None

    @property
    def swc_service(self) -> Optional["SwcService"]:
        """Get swcService (Pythonic accessor)."""
        return self._swcService

    @swc_service.setter
    def swc_service(self, value: Optional["SwcService"]) -> None:
        """
        Set swcService with validation.

        Args:
            value: The swcService to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swcService = None
            return

        if not isinstance(value, SwcService):
            raise TypeError(
                f"swcService must be SwcService or None, got {type(value).__name__}"
            )
        self._swcService = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDiagnostic(self) -> "DiagnosticStorage":
        """
        AUTOSAR-compliant getter for diagnostic.

        Returns:
            The diagnostic value

        Note:
            Delegates to diagnostic property (CODING_RULE_V2_00017)
        """
        return self.diagnostic  # Delegates to property

    def setDiagnostic(self, value: "DiagnosticStorage") -> DiagnosticStorageConditionPortMapping:
        """
        AUTOSAR-compliant setter for diagnostic with method chaining.

        Args:
            value: The diagnostic to set

        Returns:
            self for method chaining

        Note:
            Delegates to diagnostic property setter (gets validation automatically)
        """
        self.diagnostic = value  # Delegates to property setter
        return self

    def getSwcFlatService(self) -> "SwcService":
        """
        AUTOSAR-compliant getter for swcFlatService.

        Returns:
            The swcFlatService value

        Note:
            Delegates to swc_flat_service property (CODING_RULE_V2_00017)
        """
        return self.swc_flat_service  # Delegates to property

    def setSwcFlatService(self, value: "SwcService") -> DiagnosticStorageConditionPortMapping:
        """
        AUTOSAR-compliant setter for swcFlatService with method chaining.

        Args:
            value: The swcFlatService to set

        Returns:
            self for method chaining

        Note:
            Delegates to swc_flat_service property setter (gets validation automatically)
        """
        self.swc_flat_service = value  # Delegates to property setter
        return self

    def getSwcService(self) -> "SwcService":
        """
        AUTOSAR-compliant getter for swcService.

        Returns:
            The swcService value

        Note:
            Delegates to swc_service property (CODING_RULE_V2_00017)
        """
        return self.swc_service  # Delegates to property

    def setSwcService(self, value: "SwcService") -> DiagnosticStorageConditionPortMapping:
        """
        AUTOSAR-compliant setter for swcService with method chaining.

        Args:
            value: The swcService to set

        Returns:
            self for method chaining

        Note:
            Delegates to swc_service property setter (gets validation automatically)
        """
        self.swc_service = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_diagnostic(self, value: Optional["DiagnosticStorage"]) -> DiagnosticStorageConditionPortMapping:
        """
        Set diagnostic and return self for chaining.

        Args:
            value: The diagnostic to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_diagnostic("value")
        """
        self.diagnostic = value  # Use property setter (gets validation)
        return self

    def with_swc_flat_service(self, value: Optional["SwcService"]) -> DiagnosticStorageConditionPortMapping:
        """
        Set swcFlatService and return self for chaining.

        Args:
            value: The swcFlatService to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_swc_flat_service("value")
        """
        self.swc_flat_service = value  # Use property setter (gets validation)
        return self

    def with_swc_service(self, value: Optional["SwcService"]) -> DiagnosticStorageConditionPortMapping:
        """
        Set swcService and return self for chaining.

        Args:
            value: The swcService to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_swc_service("value")
        """
        self.swc_service = value  # Use property setter (gets validation)
        return self


__all__ = [
    DiagnosticMapping,
    DiagnosticTroubleCodeUdsToTroubleCodeObdMapping,
    DiagnosticSwMapping,
    DiagnosticAuthTransmitCertificateMapping,
    DiagnosticEventToTroubleCodeUdsMapping,
    DiagnosticEventToOperationCycleMapping,
    DiagnosticEventToDebounceAlgorithmMapping,
    DiagnosticEventToEnableConditionGroupMapping,
    DiagnosticEventToStorageConditionGroupMapping,
    DiagnosticMasterToSlaveEventMapping,
    DiagnosticEventToSecurityEventMapping,
    DiagnosticIumprToFunctionIdentifierMapping,
    DiagnosticSecureCodingMapping,
    DiagnosticEventPortMapping,
    DiagnosticOperationCyclePortMapping,
    DiagnosticEnableConditionPortMapping,
    DiagnosticStorageConditionPortMapping,
]
