"""
AUTOSAR Package - DiagnosticContribution

Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticContribution
"""


from __future__ import annotations

from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import (
    DiagnosticCommonElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService import (
    DiagnosticServiceInstance,
)
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticCommonProps import (
    DiagnosticCommonProps,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    Boolean,
    NameToken,
    PositiveInteger,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection import (
    DiagnosticConnection,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import (
    EcuInstance,
)


class DiagnosticContributionSet(ARElement):
    """
    This meta-class represents a root node of a diagnostic extract. It bundles a
    given set of diagnostic model elements. The granularity of the
    DiagonsticContributionSet is arbitrary in order to support the aspect of
    decentralized configuration, i.e. different contributors can come up with an
    own DiagnosticContribution Set.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticContribution::DiagnosticContributionSet

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 56, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute represents a collection of diagnostic properties that are
        # shared among the entire Diagnostic.
        self._common: Optional[DiagnosticCommonProps] = None

    @property
    def common(self) -> Optional[DiagnosticCommonProps]:
        """Get common (Pythonic accessor)."""
        return self._common

    @common.setter
    def common(self, value: Optional[DiagnosticCommonProps]) -> None:
        """
        Set common with validation.

        Args:
            value: The common to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._common = None
            return

        if not isinstance(value, DiagnosticCommonProps):
            raise TypeError(
                f"common must be DiagnosticCommonProps or None, got {type(value).__name__}"
            )
        self._common = value
        # DiagnosticContributionSet atpVariation 719 Document ID 673:
        # AUTOSAR_CP_TPS_DiagnosticExtractTemplate Template R23-11.
        self._element: List[DiagnosticCommonProps] = []

    @property
    def element(self) -> List[DiagnosticCommonProps]:
        """Get element (Pythonic accessor)."""
        return self._element
        # This represents the collection of DiagnosticServiceTables considered in the
        # scope of this Diagnostic atpVariation.
        self._serviceTable: List[DiagnosticServiceTable] = []

    @property
    def service_table(self) -> List[DiagnosticServiceTable]:
        """Get serviceTable (Pythonic accessor)."""
        return self._serviceTable

    def with_element(self, value):
        """
        Set element and return self for chaining.

        Args:
            value: The element to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_element("value")
        """
        self.element = value  # Use property setter (gets validation)
        return self

    def with_diagnostic(self, value):
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

    def with_diagnostic(self, value):
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

    def with_service_instance(self, value):
        """
        Set service_instance and return self for chaining.

        Args:
            value: The service_instance to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_service_instance("value")
        """
        self.service_instance = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCommon(self) -> DiagnosticCommonProps:
        """
        AUTOSAR-compliant getter for common.

        Returns:
            The common value

        Note:
            Delegates to common property (CODING_RULE_V2_00017)
        """
        return self.common  # Delegates to property

    def setCommon(self, value: DiagnosticCommonProps) -> DiagnosticContributionSet:
        """
        AUTOSAR-compliant setter for common with method chaining.

        Args:
            value: The common to set

        Returns:
            self for method chaining

        Note:
            Delegates to common property setter (gets validation automatically)
        """
        self.common = value  # Delegates to property setter
        return self

    def getElement(self) -> List[DiagnosticCommonProps]:
        """
        AUTOSAR-compliant getter for element.

        Returns:
            The element value

        Note:
            Delegates to element property (CODING_RULE_V2_00017)
        """
        return self.element  # Delegates to property

    def getServiceTable(self) -> List[DiagnosticServiceTable]:
        """
        AUTOSAR-compliant getter for serviceTable.

        Returns:
            The serviceTable value

        Note:
            Delegates to service_table property (CODING_RULE_V2_00017)
        """
        return self.service_table  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_common(self, value: Optional[DiagnosticCommonProps]) -> DiagnosticContributionSet:
        """
        Set common and return self for chaining.

        Args:
            value: The common to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_common("value")
        """
        self.common = value  # Use property setter (gets validation)
        return self



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
        self._diagnostic: List[DiagnosticConnection] = []

    @property
    def diagnostic(self) -> List[DiagnosticConnection]:
        """Get diagnostic (Pythonic accessor)."""
        return self._diagnostic
        # This represents the priority of the diagnostic protocol in other diagnostic
                # protocols.
        # Lower numeric higher protocol priority: - Highest protocol priority - Lowest
                # protocol priority.
        self._priority: Optional[PositiveInteger] = None

    @property
    def priority(self) -> Optional[PositiveInteger]:
        """Get priority (Pythonic accessor)."""
        return self._priority

    @priority.setter
    def priority(self, value: Optional[PositiveInteger]) -> None:
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

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"priority must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._priority = value
        self._protocolKind: Optional[NameToken] = None

    @property
    def protocol_kind(self) -> Optional[NameToken]:
        """Get protocolKind (Pythonic accessor)."""
        return self._protocolKind

    @protocol_kind.setter
    def protocol_kind(self, value: Optional[NameToken]) -> None:
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

        if not isinstance(value, (NameToken, str)):
            raise TypeError(
                f"protocolKind must be NameToken or str or None, got {type(value).__name__}"
            )
        self._protocolKind = value
        # NRC 0x78 (response pending) to the bootloader (in this case the be set to
        # "true") or if the transition shall be sending NRC 0x78 (in this case the be
        # set to "false").
        self._sendRespPend: Optional[Boolean] = None

    @property
    def send_resp_pend(self) -> Optional[Boolean]:
        """Get sendRespPend (Pythonic accessor)."""
        return self._sendRespPend

    @send_resp_pend.setter
    def send_resp_pend(self, value: Optional[Boolean]) -> None:
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

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"sendRespPend must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._sendRespPend = value
        self._serviceTable: Optional[DiagnosticServiceTable] = None

    @property
    def service_table(self) -> Optional[DiagnosticServiceTable]:
        """Get serviceTable (Pythonic accessor)."""
        return self._serviceTable

    @service_table.setter
    def service_table(self, value: Optional[DiagnosticServiceTable]) -> None:
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

    def getDiagnostic(self) -> List[DiagnosticConnection]:
        """
        AUTOSAR-compliant getter for diagnostic.

        Returns:
            The diagnostic value

        Note:
            Delegates to diagnostic property (CODING_RULE_V2_00017)
        """
        return self.diagnostic  # Delegates to property

    def getPriority(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for priority.

        Returns:
            The priority value

        Note:
            Delegates to priority property (CODING_RULE_V2_00017)
        """
        return self.priority  # Delegates to property

    def setPriority(self, value: PositiveInteger) -> DiagnosticProtocol:
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

    def getProtocolKind(self) -> NameToken:
        """
        AUTOSAR-compliant getter for protocolKind.

        Returns:
            The protocolKind value

        Note:
            Delegates to protocol_kind property (CODING_RULE_V2_00017)
        """
        return self.protocol_kind  # Delegates to property

    def setProtocolKind(self, value: NameToken) -> DiagnosticProtocol:
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

    def getSendRespPend(self) -> Boolean:
        """
        AUTOSAR-compliant getter for sendRespPend.

        Returns:
            The sendRespPend value

        Note:
            Delegates to send_resp_pend property (CODING_RULE_V2_00017)
        """
        return self.send_resp_pend  # Delegates to property

    def setSendRespPend(self, value: Boolean) -> DiagnosticProtocol:
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

    def getServiceTable(self) -> DiagnosticServiceTable:
        """
        AUTOSAR-compliant getter for serviceTable.

        Returns:
            The serviceTable value

        Note:
            Delegates to service_table property (CODING_RULE_V2_00017)
        """
        return self.service_table  # Delegates to property

    def setServiceTable(self, value: DiagnosticServiceTable) -> DiagnosticProtocol:
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

    def with_priority(self, value: Optional[PositiveInteger]) -> DiagnosticProtocol:
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

    def with_protocol_kind(self, value: Optional[NameToken]) -> DiagnosticProtocol:
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

    def with_send_resp_pend(self, value: Optional[Boolean]) -> DiagnosticProtocol:
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

    def with_service_table(self, value: Optional[DiagnosticServiceTable]) -> DiagnosticProtocol:
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
        self._ecuInstance: Optional[EcuInstance] = None

    @property
    def ecu_instance(self) -> Optional[EcuInstance]:
        """Get ecuInstance (Pythonic accessor)."""
        return self._ecuInstance

    @ecu_instance.setter
    def ecu_instance(self, value: Optional[EcuInstance]) -> None:
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
        self._protocolKind: Optional[NameToken] = None

    @property
    def protocol_kind(self) -> Optional[NameToken]:
        """Get protocolKind (Pythonic accessor)."""
        return self._protocolKind

    @protocol_kind.setter
    def protocol_kind(self, value: Optional[NameToken]) -> None:
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

        if not isinstance(value, (NameToken, str)):
            raise TypeError(
                f"protocolKind must be NameToken or str or None, got {type(value).__name__}"
            )
        self._protocolKind = value
        # scope of this Diagnostic.
        self._serviceInstance: List[DiagnosticServiceInstance] = []

    @property
    def service_instance(self) -> List[DiagnosticServiceInstance]:
        """Get serviceInstance (Pythonic accessor)."""
        return self._serviceInstance

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDiagnostic(self) -> List[DiagnosticConnection]:
        """
        AUTOSAR-compliant getter for diagnostic.

        Returns:
            The diagnostic value

        Note:
            Delegates to diagnostic property (CODING_RULE_V2_00017)
        """
        return self.diagnostic  # Delegates to property

    def getEcuInstance(self) -> EcuInstance:
        """
        AUTOSAR-compliant getter for ecuInstance.

        Returns:
            The ecuInstance value

        Note:
            Delegates to ecu_instance property (CODING_RULE_V2_00017)
        """
        return self.ecu_instance  # Delegates to property

    def setEcuInstance(self, value: EcuInstance) -> DiagnosticServiceTable:
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

    def getProtocolKind(self) -> NameToken:
        """
        AUTOSAR-compliant getter for protocolKind.

        Returns:
            The protocolKind value

        Note:
            Delegates to protocol_kind property (CODING_RULE_V2_00017)
        """
        return self.protocol_kind  # Delegates to property

    def setProtocolKind(self, value: NameToken) -> DiagnosticServiceTable:
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

    def getServiceInstance(self) -> List[DiagnosticServiceInstance]:
        """
        AUTOSAR-compliant getter for serviceInstance.

        Returns:
            The serviceInstance value

        Note:
            Delegates to service_instance property (CODING_RULE_V2_00017)
        """
        return self.service_instance  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ecu_instance(self, value: Optional[EcuInstance]) -> DiagnosticServiceTable:
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

    def with_protocol_kind(self, value: Optional[NameToken]) -> DiagnosticServiceTable:
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



class DiagnosticEcuInstanceProps(DiagnosticCommonElement):
    """
    This meta-class represents the ability to model properties that are specific
    for a given EcuInstance but on the other hand represent purely
    diagnostic-related information. In the spirit of decentralized configuration
    it is therefore possible to specify the diagnostic-related information
    related to a given EcuInstance even if the EcuInstance does not yet exist.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticContribution::DiagnosticEcuInstanceProps

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 207, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the actual EcuInstance to which the in the
        # DiagnosticEcuInstance.
        self._ecuInstance: List[EcuInstance] = []

    @property
    def ecu_instance(self) -> List[EcuInstance]:
        """Get ecuInstance (Pythonic accessor)."""
        return self._ecuInstance
        # This attribute is used to specify the role (if applicable) in the
        # DiagnosticEcuInstance supports OBD.
        self._obdSupport: Optional[DiagnosticObdSupportEnum] = None

    @property
    def obd_support(self) -> Optional[DiagnosticObdSupportEnum]:
        """Get obdSupport (Pythonic accessor)."""
        return self._obdSupport

    @obd_support.setter
    def obd_support(self, value: Optional[DiagnosticObdSupportEnum]) -> None:
        """
        Set obdSupport with validation.

        Args:
            value: The obdSupport to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._obdSupport = None
            return

        if not isinstance(value, DiagnosticObdSupportEnum):
            raise TypeError(
                f"obdSupport must be DiagnosticObdSupportEnum or None, got {type(value).__name__}"
            )
        self._obdSupport = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEcuInstance(self) -> List[EcuInstance]:
        """
        AUTOSAR-compliant getter for ecuInstance.

        Returns:
            The ecuInstance value

        Note:
            Delegates to ecu_instance property (CODING_RULE_V2_00017)
        """
        return self.ecu_instance  # Delegates to property

    def getObdSupport(self) -> DiagnosticObdSupportEnum:
        """
        AUTOSAR-compliant getter for obdSupport.

        Returns:
            The obdSupport value

        Note:
            Delegates to obd_support property (CODING_RULE_V2_00017)
        """
        return self.obd_support  # Delegates to property

    def setObdSupport(self, value: DiagnosticObdSupportEnum) -> DiagnosticEcuInstanceProps:
        """
        AUTOSAR-compliant setter for obdSupport with method chaining.

        Args:
            value: The obdSupport to set

        Returns:
            self for method chaining

        Note:
            Delegates to obd_support property setter (gets validation automatically)
        """
        self.obd_support = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_obd_support(self, value: Optional[DiagnosticObdSupportEnum]) -> DiagnosticEcuInstanceProps:
        """
        Set obdSupport and return self for chaining.

        Args:
            value: The obdSupport to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_obd_support("value")
        """
        self.obd_support = value  # Use property setter (gets validation)
        return self


class DiagnosticObdSupportEnum(AREnum):
    """
    DiagnosticObdSupportEnum enumeration

This meta-class represents the ability to model the roles in which a participation in OBD is foreseen. At the moment, this applies exclusively to the Dem. However, future extension of the Dcm may require this setting as well. Aggregated by DiagnosticEcuInstanceProps.obdSupport

Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticContribution
    """
    # This represent the role "master ECU".
    masterEcu = "0"

    # This represents the ability to explicitly specify that no participation in OBD is foreseen.
    noObdSupport = "1"

    # This represents the role "primary ECU".
    primaryEcu = "2"

    # This represents the role "secondary ECU".
    secondaryEcu = "3"
