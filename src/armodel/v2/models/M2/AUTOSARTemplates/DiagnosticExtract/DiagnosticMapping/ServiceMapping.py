from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping import DiagnosticSwMapping

    RefType,
)


class DiagnosticServiceDataMapping(DiagnosticSwMapping):
    """
    This represents the ability to define a mapping of a diagnostic service to a
    software-component. This kind of service mapping is applicable for the usage
    of SenderReceiverInterfaces or event/notifier semantics in ServiceInterfaces
    on the adaptive platform.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::ServiceMapping

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 228, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the applicable payload that corresponds the referenced
        # DataPrototype in the role mappedData (in case of a usage on the adaptive
        # platform).
        self._diagnosticData: Optional["DiagnosticDataElement"] = None

    @property
    def diagnostic_data(self) -> Optional["DiagnosticDataElement"]:
        """Get diagnosticData (Pythonic accessor)."""
        return self._diagnosticData

    @diagnostic_data.setter
    def diagnostic_data(self, value: Optional["DiagnosticDataElement"]) -> None:
        """
        Set diagnosticData with validation.

        Args:
            value: The diagnosticData to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._diagnosticData = None
            return

        if not isinstance(value, DiagnosticDataElement):
            raise TypeError(
                f"diagnosticData must be DiagnosticDataElement or None, got {type(value).__name__}"
            )
        self._diagnosticData = value
        # This represents the applicable payload that corresponds to the referenced
        # DataPrototype in the role mappedData.
        self._diagnostic: Optional["DiagnosticParameter"] = None

    @property
    def diagnostic(self) -> Optional["DiagnosticParameter"]:
        """Get diagnostic (Pythonic accessor)."""
        return self._diagnostic

    @diagnostic.setter
    def diagnostic(self, value: Optional["DiagnosticParameter"]) -> None:
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

        if not isinstance(value, DiagnosticParameter):
            raise TypeError(
                f"diagnostic must be DiagnosticParameter or None, got {type(value).__name__}"
            )
        self._diagnostic = value
        # that is accessed for diagnostic purpose.
        # This applicable on the classic platform.
        # by: DataPrototypeInSystem.
        self._mappedData: RefType = None

    @property
    def mapped_data(self) -> RefType:
        """Get mappedData (Pythonic accessor)."""
        return self._mappedData

    @mapped_data.setter
    def mapped_data(self, value: RefType) -> None:
        """
        Set mappedData with validation.

        Args:
            value: The mappedData to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mappedData = None
            return

        self._mappedData = value
        # This aggregation represents the single point of access to the reference to
        # one specific DiagnosticParameter.
        self._parameter: Optional["DiagnosticParameter"] = None

    @property
    def parameter(self) -> Optional["DiagnosticParameter"]:
        """Get parameter (Pythonic accessor)."""
        return self._parameter

    @parameter.setter
    def parameter(self, value: Optional["DiagnosticParameter"]) -> None:
        """
        Set parameter with validation.

        Args:
            value: The parameter to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._parameter = None
            return

        if not isinstance(value, DiagnosticParameter):
            raise TypeError(
                f"parameter must be DiagnosticParameter or None, got {type(value).__name__}"
            )
        self._parameter = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDiagnosticData(self) -> "DiagnosticDataElement":
        """
        AUTOSAR-compliant getter for diagnosticData.

        Returns:
            The diagnosticData value

        Note:
            Delegates to diagnostic_data property (CODING_RULE_V2_00017)
        """
        return self.diagnostic_data  # Delegates to property

    def setDiagnosticData(self, value: "DiagnosticDataElement") -> "DiagnosticServiceDataMapping":
        """
        AUTOSAR-compliant setter for diagnosticData with method chaining.

        Args:
            value: The diagnosticData to set

        Returns:
            self for method chaining

        Note:
            Delegates to diagnostic_data property setter (gets validation automatically)
        """
        self.diagnostic_data = value  # Delegates to property setter
        return self

    def getDiagnostic(self) -> "DiagnosticParameter":
        """
        AUTOSAR-compliant getter for diagnostic.

        Returns:
            The diagnostic value

        Note:
            Delegates to diagnostic property (CODING_RULE_V2_00017)
        """
        return self.diagnostic  # Delegates to property

    def setDiagnostic(self, value: "DiagnosticParameter") -> "DiagnosticServiceDataMapping":
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

    def getMappedData(self) -> RefType:
        """
        AUTOSAR-compliant getter for mappedData.

        Returns:
            The mappedData value

        Note:
            Delegates to mapped_data property (CODING_RULE_V2_00017)
        """
        return self.mapped_data  # Delegates to property

    def setMappedData(self, value: RefType) -> "DiagnosticServiceDataMapping":
        """
        AUTOSAR-compliant setter for mappedData with method chaining.

        Args:
            value: The mappedData to set

        Returns:
            self for method chaining

        Note:
            Delegates to mapped_data property setter (gets validation automatically)
        """
        self.mapped_data = value  # Delegates to property setter
        return self

    def getParameter(self) -> "DiagnosticParameter":
        """
        AUTOSAR-compliant getter for parameter.

        Returns:
            The parameter value

        Note:
            Delegates to parameter property (CODING_RULE_V2_00017)
        """
        return self.parameter  # Delegates to property

    def setParameter(self, value: "DiagnosticParameter") -> "DiagnosticServiceDataMapping":
        """
        AUTOSAR-compliant setter for parameter with method chaining.

        Args:
            value: The parameter to set

        Returns:
            self for method chaining

        Note:
            Delegates to parameter property setter (gets validation automatically)
        """
        self.parameter = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_diagnostic_data(self, value: Optional["DiagnosticDataElement"]) -> "DiagnosticServiceDataMapping":
        """
        Set diagnosticData and return self for chaining.

        Args:
            value: The diagnosticData to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_diagnostic_data("value")
        """
        self.diagnostic_data = value  # Use property setter (gets validation)
        return self

    def with_diagnostic(self, value: Optional["DiagnosticParameter"]) -> "DiagnosticServiceDataMapping":
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

    def with_mapped_data(self, value: Optional[RefType]) -> "DiagnosticServiceDataMapping":
        """
        Set mappedData and return self for chaining.

        Args:
            value: The mappedData to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mapped_data("value")
        """
        self.mapped_data = value  # Use property setter (gets validation)
        return self

    def with_parameter(self, value: Optional["DiagnosticParameter"]) -> "DiagnosticServiceDataMapping":
        """
        Set parameter and return self for chaining.

        Args:
            value: The parameter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_parameter("value")
        """
        self.parameter = value  # Use property setter (gets validation)
        return self

from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class DiagnosticParameterElementAccess(ARObject):
    """
    This meta-class acts as a single point for defining structured references to
    a specific Diagnostic ParameterElement.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::ServiceMapping

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 229, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the context of an applicable payload that corresponds to the
        # referenced DataPrototype in the role.
        self._contextElement: List["DiagnosticParameter"] = []

    @property
    def context_element(self) -> List["DiagnosticParameter"]:
        """Get contextElement (Pythonic accessor)."""
        return self._contextElement
        # This represents the target reference of an applicable that corresponds to the
        # referenced Data the role mappedDataElement.
        self._targetElement: Optional["DiagnosticParameter"] = None

    @property
    def target_element(self) -> Optional["DiagnosticParameter"]:
        """Get targetElement (Pythonic accessor)."""
        return self._targetElement

    @target_element.setter
    def target_element(self, value: Optional["DiagnosticParameter"]) -> None:
        """
        Set targetElement with validation.

        Args:
            value: The targetElement to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetElement = None
            return

        if not isinstance(value, DiagnosticParameter):
            raise TypeError(
                f"targetElement must be DiagnosticParameter or None, got {type(value).__name__}"
            )
        self._targetElement = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getContextElement(self) -> List["DiagnosticParameter"]:
        """
        AUTOSAR-compliant getter for contextElement.

        Returns:
            The contextElement value

        Note:
            Delegates to context_element property (CODING_RULE_V2_00017)
        """
        return self.context_element  # Delegates to property

    def getTargetElement(self) -> "DiagnosticParameter":
        """
        AUTOSAR-compliant getter for targetElement.

        Returns:
            The targetElement value

        Note:
            Delegates to target_element property (CODING_RULE_V2_00017)
        """
        return self.target_element  # Delegates to property

    def setTargetElement(self, value: "DiagnosticParameter") -> "DiagnosticParameterElementAccess":
        """
        AUTOSAR-compliant setter for targetElement with method chaining.

        Args:
            value: The targetElement to set

        Returns:
            self for method chaining

        Note:
            Delegates to target_element property setter (gets validation automatically)
        """
        self.target_element = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_target_element(self, value: Optional["DiagnosticParameter"]) -> "DiagnosticParameterElementAccess":
        """
        Set targetElement and return self for chaining.

        Args:
            value: The targetElement to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_target_element("value")
        """
        self.target_element = value  # Use property setter (gets validation)
        return self

from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class DiagnosticServiceMappingDiagTarget(ARObject, ABC):
    """
    This meta-class serves as a base class for diagnostics-related targets of
    subclasses of DiagnosticSw Mapping

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::ServiceMapping

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 234, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is DiagnosticServiceMappingDiagTarget:
            raise TypeError("DiagnosticServiceMappingDiagTarget is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping import DiagnosticSwMapping

    RefType,
)


class DiagnosticServiceSwMapping(DiagnosticSwMapping):
    """
    This represents the ability to define a mapping of a diagnostic service to a
    software-component or a basic-software module. If the former is used then
    this kind of service mapping is applicable for the usage of
    ClientServerInterfaces.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::ServiceMapping

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 238, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # to be accessed in the context of the operation by: DataPrototypeInClient.
        self._accessedData: RefType = None

    @property
    def accessed_data(self) -> RefType:
        """Get accessedData (Pythonic accessor)."""
        return self._accessedData

    @accessed_data.setter
    def accessed_data(self, value: RefType) -> None:
        """
        Set accessedData with validation.

        Args:
            value: The accessedData to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._accessedData = None
            return

        self._accessedData = value
        # This represents a DiagnosticDataElement required to the respective diagnostic
        # service in the context of service mapping,.
        self._diagnosticData: Optional["DiagnosticDataElement"] = None

    @property
    def diagnostic_data(self) -> Optional["DiagnosticDataElement"]:
        """Get diagnosticData (Pythonic accessor)."""
        return self._diagnosticData

    @diagnostic_data.setter
    def diagnostic_data(self, value: Optional["DiagnosticDataElement"]) -> None:
        """
        Set diagnosticData with validation.

        Args:
            value: The diagnosticData to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._diagnosticData = None
            return

        if not isinstance(value, DiagnosticDataElement):
            raise TypeError(
                f"diagnosticData must be DiagnosticDataElement or None, got {type(value).__name__}"
            )
        self._diagnosticData = value
        # This represents the applicable payload that corresponds to the referenced
        # DataPrototype in the role mappedData.
        self._diagnostic: Optional["DiagnosticParameter"] = None

    @property
    def diagnostic(self) -> Optional["DiagnosticParameter"]:
        """Get diagnostic (Pythonic accessor)."""
        return self._diagnostic

    @diagnostic.setter
    def diagnostic(self, value: Optional["DiagnosticParameter"]) -> None:
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

        if not isinstance(value, DiagnosticParameter):
            raise TypeError(
                f"diagnostic must be DiagnosticParameter or None, got {type(value).__name__}"
            )
        self._diagnostic = value
        # This is supposed to represent a reference to a Bsw ServiceDependency.
        # the latter is not derived from and therefore this detour needs to be still
                # let BswServiceDependency become of a reference.
        # 719 Document ID 673: AUTOSAR_CP_TPS_DiagnosticExtractTemplate Template
                # R23-11.
        self._mappedBsw: Optional["BswService"] = None

    @property
    def mapped_bsw(self) -> Optional["BswService"]:
        """Get mappedBsw (Pythonic accessor)."""
        return self._mappedBsw

    @mapped_bsw.setter
    def mapped_bsw(self, value: Optional["BswService"]) -> None:
        """
        Set mappedBsw with validation.

        Args:
            value: The mappedBsw to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mappedBsw = None
            return

        if not isinstance(value, BswService):
            raise TypeError(
                f"mappedBsw must be BswService or None, got {type(value).__name__}"
            )
        self._mappedBsw = value
        # This represents the ability to refer to an AtomicSw ComponentType that is
        # available without the definition of it will be embedded into the component
        # hierarchy.
        self._mappedFlatSwc: Optional["SwcService"] = None

    @property
    def mapped_flat_swc(self) -> Optional["SwcService"]:
        """Get mappedFlatSwc (Pythonic accessor)."""
        return self._mappedFlatSwc

    @mapped_flat_swc.setter
    def mapped_flat_swc(self, value: Optional["SwcService"]) -> None:
        """
        Set mappedFlatSwc with validation.

        Args:
            value: The mappedFlatSwc to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mappedFlatSwc = None
            return

        if not isinstance(value, SwcService):
            raise TypeError(
                f"mappedFlatSwc must be SwcService or None, got {type(value).__name__}"
            )
        self._mappedFlatSwc = value
        # hierarchy (under possible consideration of the root implemented by:
        # SwcServiceDependency.
        self._mappedSwc: Optional["SwcService"] = None

    @property
    def mapped_swc(self) -> Optional["SwcService"]:
        """Get mappedSwc (Pythonic accessor)."""
        return self._mappedSwc

    @mapped_swc.setter
    def mapped_swc(self, value: Optional["SwcService"]) -> None:
        """
        Set mappedSwc with validation.

        Args:
            value: The mappedSwc to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mappedSwc = None
            return

        if not isinstance(value, SwcService):
            raise TypeError(
                f"mappedSwc must be SwcService or None, got {type(value).__name__}"
            )
        self._mappedSwc = value
        # This aggregation represents the single point of access to the reference to
        # one specific DiagnosticParameter.
        self._parameter: Optional["DiagnosticParameter"] = None

    @property
    def parameter(self) -> Optional["DiagnosticParameter"]:
        """Get parameter (Pythonic accessor)."""
        return self._parameter

    @parameter.setter
    def parameter(self, value: Optional["DiagnosticParameter"]) -> None:
        """
        Set parameter with validation.

        Args:
            value: The parameter to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._parameter = None
            return

        if not isinstance(value, DiagnosticParameter):
            raise TypeError(
                f"parameter must be DiagnosticParameter or None, got {type(value).__name__}"
            )
        self._parameter = value
        # This represents the service instance that needs to be in this diagnostics
        # service mapping.
        self._serviceInstance: Optional["DiagnosticService"] = None

    @property
    def service_instance(self) -> Optional["DiagnosticService"]:
        """Get serviceInstance (Pythonic accessor)."""
        return self._serviceInstance

    @service_instance.setter
    def service_instance(self, value: Optional["DiagnosticService"]) -> None:
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

        if not isinstance(value, DiagnosticService):
            raise TypeError(
                f"serviceInstance must be DiagnosticService or None, got {type(value).__name__}"
            )
        self._serviceInstance = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAccessedData(self) -> RefType:
        """
        AUTOSAR-compliant getter for accessedData.

        Returns:
            The accessedData value

        Note:
            Delegates to accessed_data property (CODING_RULE_V2_00017)
        """
        return self.accessed_data  # Delegates to property

    def setAccessedData(self, value: RefType) -> "DiagnosticServiceSwMapping":
        """
        AUTOSAR-compliant setter for accessedData with method chaining.

        Args:
            value: The accessedData to set

        Returns:
            self for method chaining

        Note:
            Delegates to accessed_data property setter (gets validation automatically)
        """
        self.accessed_data = value  # Delegates to property setter
        return self

    def getDiagnosticData(self) -> "DiagnosticDataElement":
        """
        AUTOSAR-compliant getter for diagnosticData.

        Returns:
            The diagnosticData value

        Note:
            Delegates to diagnostic_data property (CODING_RULE_V2_00017)
        """
        return self.diagnostic_data  # Delegates to property

    def setDiagnosticData(self, value: "DiagnosticDataElement") -> "DiagnosticServiceSwMapping":
        """
        AUTOSAR-compliant setter for diagnosticData with method chaining.

        Args:
            value: The diagnosticData to set

        Returns:
            self for method chaining

        Note:
            Delegates to diagnostic_data property setter (gets validation automatically)
        """
        self.diagnostic_data = value  # Delegates to property setter
        return self

    def getDiagnostic(self) -> "DiagnosticParameter":
        """
        AUTOSAR-compliant getter for diagnostic.

        Returns:
            The diagnostic value

        Note:
            Delegates to diagnostic property (CODING_RULE_V2_00017)
        """
        return self.diagnostic  # Delegates to property

    def setDiagnostic(self, value: "DiagnosticParameter") -> "DiagnosticServiceSwMapping":
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

    def getMappedBsw(self) -> "BswService":
        """
        AUTOSAR-compliant getter for mappedBsw.

        Returns:
            The mappedBsw value

        Note:
            Delegates to mapped_bsw property (CODING_RULE_V2_00017)
        """
        return self.mapped_bsw  # Delegates to property

    def setMappedBsw(self, value: "BswService") -> "DiagnosticServiceSwMapping":
        """
        AUTOSAR-compliant setter for mappedBsw with method chaining.

        Args:
            value: The mappedBsw to set

        Returns:
            self for method chaining

        Note:
            Delegates to mapped_bsw property setter (gets validation automatically)
        """
        self.mapped_bsw = value  # Delegates to property setter
        return self

    def getMappedFlatSwc(self) -> "SwcService":
        """
        AUTOSAR-compliant getter for mappedFlatSwc.

        Returns:
            The mappedFlatSwc value

        Note:
            Delegates to mapped_flat_swc property (CODING_RULE_V2_00017)
        """
        return self.mapped_flat_swc  # Delegates to property

    def setMappedFlatSwc(self, value: "SwcService") -> "DiagnosticServiceSwMapping":
        """
        AUTOSAR-compliant setter for mappedFlatSwc with method chaining.

        Args:
            value: The mappedFlatSwc to set

        Returns:
            self for method chaining

        Note:
            Delegates to mapped_flat_swc property setter (gets validation automatically)
        """
        self.mapped_flat_swc = value  # Delegates to property setter
        return self

    def getMappedSwc(self) -> "SwcService":
        """
        AUTOSAR-compliant getter for mappedSwc.

        Returns:
            The mappedSwc value

        Note:
            Delegates to mapped_swc property (CODING_RULE_V2_00017)
        """
        return self.mapped_swc  # Delegates to property

    def setMappedSwc(self, value: "SwcService") -> "DiagnosticServiceSwMapping":
        """
        AUTOSAR-compliant setter for mappedSwc with method chaining.

        Args:
            value: The mappedSwc to set

        Returns:
            self for method chaining

        Note:
            Delegates to mapped_swc property setter (gets validation automatically)
        """
        self.mapped_swc = value  # Delegates to property setter
        return self

    def getParameter(self) -> "DiagnosticParameter":
        """
        AUTOSAR-compliant getter for parameter.

        Returns:
            The parameter value

        Note:
            Delegates to parameter property (CODING_RULE_V2_00017)
        """
        return self.parameter  # Delegates to property

    def setParameter(self, value: "DiagnosticParameter") -> "DiagnosticServiceSwMapping":
        """
        AUTOSAR-compliant setter for parameter with method chaining.

        Args:
            value: The parameter to set

        Returns:
            self for method chaining

        Note:
            Delegates to parameter property setter (gets validation automatically)
        """
        self.parameter = value  # Delegates to property setter
        return self

    def getServiceInstance(self) -> "DiagnosticService":
        """
        AUTOSAR-compliant getter for serviceInstance.

        Returns:
            The serviceInstance value

        Note:
            Delegates to service_instance property (CODING_RULE_V2_00017)
        """
        return self.service_instance  # Delegates to property

    def setServiceInstance(self, value: "DiagnosticService") -> "DiagnosticServiceSwMapping":
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

    def with_accessed_data(self, value: Optional[RefType]) -> "DiagnosticServiceSwMapping":
        """
        Set accessedData and return self for chaining.

        Args:
            value: The accessedData to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_accessed_data("value")
        """
        self.accessed_data = value  # Use property setter (gets validation)
        return self

    def with_diagnostic_data(self, value: Optional["DiagnosticDataElement"]) -> "DiagnosticServiceSwMapping":
        """
        Set diagnosticData and return self for chaining.

        Args:
            value: The diagnosticData to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_diagnostic_data("value")
        """
        self.diagnostic_data = value  # Use property setter (gets validation)
        return self

    def with_diagnostic(self, value: Optional["DiagnosticParameter"]) -> "DiagnosticServiceSwMapping":
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

    def with_mapped_bsw(self, value: Optional["BswService"]) -> "DiagnosticServiceSwMapping":
        """
        Set mappedBsw and return self for chaining.

        Args:
            value: The mappedBsw to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mapped_bsw("value")
        """
        self.mapped_bsw = value  # Use property setter (gets validation)
        return self

    def with_mapped_flat_swc(self, value: Optional["SwcService"]) -> "DiagnosticServiceSwMapping":
        """
        Set mappedFlatSwc and return self for chaining.

        Args:
            value: The mappedFlatSwc to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mapped_flat_swc("value")
        """
        self.mapped_flat_swc = value  # Use property setter (gets validation)
        return self

    def with_mapped_swc(self, value: Optional["SwcService"]) -> "DiagnosticServiceSwMapping":
        """
        Set mappedSwc and return self for chaining.

        Args:
            value: The mappedSwc to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mapped_swc("value")
        """
        self.mapped_swc = value  # Use property setter (gets validation)
        return self

    def with_parameter(self, value: Optional["DiagnosticParameter"]) -> "DiagnosticServiceSwMapping":
        """
        Set parameter and return self for chaining.

        Args:
            value: The parameter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_parameter("value")
        """
        self.parameter = value  # Use property setter (gets validation)
        return self

    def with_service_instance(self, value: Optional["DiagnosticService"]) -> "DiagnosticServiceSwMapping":
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

from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario import (
    IdentCaption,
)


class BswServiceDependencyIdent(IdentCaption):
    """
    This meta-class is created to add the ability to become the target of a
    reference to the non-Referrable BswServiceDependency. (cid:53) 239 of 719
    Document ID 673: AUTOSAR_CP_TPS_DiagnosticExtractTemplate Diagnostic Extract
    Template AUTOSAR CP R23-11 (cid:52)

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::ServiceMapping

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 239, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping import (
    DiagnosticMapping,
)


class DiagnosticSecurityEventReportingModeMapping(DiagnosticMapping):
    """
    This meta-class represents the ability to associate a location in a DID with
    a security event. The purpose of this mapping is that the location in the
    DID contains the setting of the reporting mode for the specific security
    event. This means that the reporting mode of the security event can be set
    via the diagnostic service WriteDataByIdentifier.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::ServiceMapping

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 243, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference identifies the data element that carries the the reporting
        # mode.
        self._dataElement: Optional["DiagnosticDataElement"] = None

    @property
    def data_element(self) -> Optional["DiagnosticDataElement"]:
        """Get dataElement (Pythonic accessor)."""
        return self._dataElement

    @data_element.setter
    def data_element(self, value: Optional["DiagnosticDataElement"]) -> None:
        """
        Set dataElement with validation.

        Args:
            value: The dataElement to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataElement = None
            return

        if not isinstance(value, DiagnosticDataElement):
            raise TypeError(
                f"dataElement must be DiagnosticDataElement or None, got {type(value).__name__}"
            )
        self._dataElement = value
        # This reference identifies the mapped security event.
        # atp.
        # Status=candidate.
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

    def getDataElement(self) -> "DiagnosticDataElement":
        """
        AUTOSAR-compliant getter for dataElement.

        Returns:
            The dataElement value

        Note:
            Delegates to data_element property (CODING_RULE_V2_00017)
        """
        return self.data_element  # Delegates to property

    def setDataElement(self, value: "DiagnosticDataElement") -> "DiagnosticSecurityEventReportingModeMapping":
        """
        AUTOSAR-compliant setter for dataElement with method chaining.

        Args:
            value: The dataElement to set

        Returns:
            self for method chaining

        Note:
            Delegates to data_element property setter (gets validation automatically)
        """
        self.data_element = value  # Delegates to property setter
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

    def setSecurityEvent(self, value: "SecurityEventContext") -> "DiagnosticSecurityEventReportingModeMapping":
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

    def with_data_element(self, value: Optional["DiagnosticDataElement"]) -> "DiagnosticSecurityEventReportingModeMapping":
        """
        Set dataElement and return self for chaining.

        Args:
            value: The dataElement to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_element("value")
        """
        self.data_element = value  # Use property setter (gets validation)
        return self

    def with_security_event(self, value: Optional["SecurityEventContext"]) -> "DiagnosticSecurityEventReportingModeMapping":
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

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping import (
    DiagnosticMapping,
)


class DiagnosticDemProvidedDataMapping(DiagnosticMapping):
    """
    This represents the ability to define the nature of a data access for a
    DiagnosticDataElement in the Dem.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::ServiceMapping

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 255, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the DiagnosticDataElement for which the further qualified by
        # the DiagnosticDemProvided.
        self._dataElement: Optional["DiagnosticDataElement"] = None

    @property
    def data_element(self) -> Optional["DiagnosticDataElement"]:
        """Get dataElement (Pythonic accessor)."""
        return self._dataElement

    @data_element.setter
    def data_element(self, value: Optional["DiagnosticDataElement"]) -> None:
        """
        Set dataElement with validation.

        Args:
            value: The dataElement to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataElement = None
            return

        if not isinstance(value, DiagnosticDataElement):
            raise TypeError(
                f"dataElement must be DiagnosticDataElement or None, got {type(value).__name__}"
            )
        self._dataElement = value
        # This represents the ability to further specify the access Dem.
        self._dataProvider: Optional["NameToken"] = None

    @property
    def data_provider(self) -> Optional["NameToken"]:
        """Get dataProvider (Pythonic accessor)."""
        return self._dataProvider

    @data_provider.setter
    def data_provider(self, value: Optional["NameToken"]) -> None:
        """
        Set dataProvider with validation.

        Args:
            value: The dataProvider to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataProvider = None
            return

        if not isinstance(value, NameToken):
            raise TypeError(
                f"dataProvider must be NameToken or None, got {type(value).__name__}"
            )
        self._dataProvider = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataElement(self) -> "DiagnosticDataElement":
        """
        AUTOSAR-compliant getter for dataElement.

        Returns:
            The dataElement value

        Note:
            Delegates to data_element property (CODING_RULE_V2_00017)
        """
        return self.data_element  # Delegates to property

    def setDataElement(self, value: "DiagnosticDataElement") -> "DiagnosticDemProvidedDataMapping":
        """
        AUTOSAR-compliant setter for dataElement with method chaining.

        Args:
            value: The dataElement to set

        Returns:
            self for method chaining

        Note:
            Delegates to data_element property setter (gets validation automatically)
        """
        self.data_element = value  # Delegates to property setter
        return self

    def getDataProvider(self) -> "NameToken":
        """
        AUTOSAR-compliant getter for dataProvider.

        Returns:
            The dataProvider value

        Note:
            Delegates to data_provider property (CODING_RULE_V2_00017)
        """
        return self.data_provider  # Delegates to property

    def setDataProvider(self, value: "NameToken") -> "DiagnosticDemProvidedDataMapping":
        """
        AUTOSAR-compliant setter for dataProvider with method chaining.

        Args:
            value: The dataProvider to set

        Returns:
            self for method chaining

        Note:
            Delegates to data_provider property setter (gets validation automatically)
        """
        self.data_provider = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_element(self, value: Optional["DiagnosticDataElement"]) -> "DiagnosticDemProvidedDataMapping":
        """
        Set dataElement and return self for chaining.

        Args:
            value: The dataElement to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_element("value")
        """
        self.data_element = value  # Use property setter (gets validation)
        return self

    def with_data_provider(self, value: Optional["NameToken"]) -> "DiagnosticDemProvidedDataMapping":
        """
        Set dataProvider and return self for chaining.

        Args:
            value: The dataProvider to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_provider("value")
        """
        self.data_provider = value  # Use property setter (gets validation)
        return self

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping import (
    DiagnosticSwMapping,
)


class DiagnosticFimFunctionMapping(DiagnosticSwMapping):
    """
    This meta-class represents the ability to define a mapping between a
    function identifier (FID) and the corresponding SwcServiceDependency in the
    application software resp. basic software.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::ServiceMapping

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 264, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is supposed to represent a reference to a Bsw ServiceDependency.
        # the latter is not derived from and therefore this detour needs to be still
                # let BswServiceDependency become of a reference.
        self._mappedBsw: Optional["BswService"] = None

    @property
    def mapped_bsw(self) -> Optional["BswService"]:
        """Get mappedBsw (Pythonic accessor)."""
        return self._mappedBsw

    @mapped_bsw.setter
    def mapped_bsw(self, value: Optional["BswService"]) -> None:
        """
        Set mappedBsw with validation.

        Args:
            value: The mappedBsw to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mappedBsw = None
            return

        if not isinstance(value, BswService):
            raise TypeError(
                f"mappedBsw must be BswService or None, got {type(value).__name__}"
            )
        self._mappedBsw = value
        # This represents the ability to refer to an AtomicSw ComponentType that is
        # available without the definition of it will be embedded into the component
        # hierarchy.
        self._mappedFlatSwc: Optional["SwcService"] = None

    @property
    def mapped_flat_swc(self) -> Optional["SwcService"]:
        """Get mappedFlatSwc (Pythonic accessor)."""
        return self._mappedFlatSwc

    @mapped_flat_swc.setter
    def mapped_flat_swc(self, value: Optional["SwcService"]) -> None:
        """
        Set mappedFlatSwc with validation.

        Args:
            value: The mappedFlatSwc to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mappedFlatSwc = None
            return

        if not isinstance(value, SwcService):
            raise TypeError(
                f"mappedFlatSwc must be SwcService or None, got {type(value).__name__}"
            )
        self._mappedFlatSwc = value
        # This represents the mapped FID.
        # 719 Document ID 673: AUTOSAR_CP_TPS_DiagnosticExtractTemplate Template
                # R23-11.
        self._mapped: Optional["DiagnosticFunction"] = None

    @property
    def mapped(self) -> Optional["DiagnosticFunction"]:
        """Get mapped (Pythonic accessor)."""
        return self._mapped

    @mapped.setter
    def mapped(self, value: Optional["DiagnosticFunction"]) -> None:
        """
        Set mapped with validation.

        Args:
            value: The mapped to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mapped = None
            return

        if not isinstance(value, DiagnosticFunction):
            raise TypeError(
                f"mapped must be DiagnosticFunction or None, got {type(value).__name__}"
            )
        self._mapped = value
        # hierarchy (under possible consideration of the root by: SwcServiceDependency.
        self._mappedSwc: Optional["SwcService"] = None

    @property
    def mapped_swc(self) -> Optional["SwcService"]:
        """Get mappedSwc (Pythonic accessor)."""
        return self._mappedSwc

    @mapped_swc.setter
    def mapped_swc(self, value: Optional["SwcService"]) -> None:
        """
        Set mappedSwc with validation.

        Args:
            value: The mappedSwc to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mappedSwc = None
            return

        if not isinstance(value, SwcService):
            raise TypeError(
                f"mappedSwc must be SwcService or None, got {type(value).__name__}"
            )
        self._mappedSwc = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMappedBsw(self) -> "BswService":
        """
        AUTOSAR-compliant getter for mappedBsw.

        Returns:
            The mappedBsw value

        Note:
            Delegates to mapped_bsw property (CODING_RULE_V2_00017)
        """
        return self.mapped_bsw  # Delegates to property

    def setMappedBsw(self, value: "BswService") -> "DiagnosticFimFunctionMapping":
        """
        AUTOSAR-compliant setter for mappedBsw with method chaining.

        Args:
            value: The mappedBsw to set

        Returns:
            self for method chaining

        Note:
            Delegates to mapped_bsw property setter (gets validation automatically)
        """
        self.mapped_bsw = value  # Delegates to property setter
        return self

    def getMappedFlatSwc(self) -> "SwcService":
        """
        AUTOSAR-compliant getter for mappedFlatSwc.

        Returns:
            The mappedFlatSwc value

        Note:
            Delegates to mapped_flat_swc property (CODING_RULE_V2_00017)
        """
        return self.mapped_flat_swc  # Delegates to property

    def setMappedFlatSwc(self, value: "SwcService") -> "DiagnosticFimFunctionMapping":
        """
        AUTOSAR-compliant setter for mappedFlatSwc with method chaining.

        Args:
            value: The mappedFlatSwc to set

        Returns:
            self for method chaining

        Note:
            Delegates to mapped_flat_swc property setter (gets validation automatically)
        """
        self.mapped_flat_swc = value  # Delegates to property setter
        return self

    def getMapped(self) -> "DiagnosticFunction":
        """
        AUTOSAR-compliant getter for mapped.

        Returns:
            The mapped value

        Note:
            Delegates to mapped property (CODING_RULE_V2_00017)
        """
        return self.mapped  # Delegates to property

    def setMapped(self, value: "DiagnosticFunction") -> "DiagnosticFimFunctionMapping":
        """
        AUTOSAR-compliant setter for mapped with method chaining.

        Args:
            value: The mapped to set

        Returns:
            self for method chaining

        Note:
            Delegates to mapped property setter (gets validation automatically)
        """
        self.mapped = value  # Delegates to property setter
        return self

    def getMappedSwc(self) -> "SwcService":
        """
        AUTOSAR-compliant getter for mappedSwc.

        Returns:
            The mappedSwc value

        Note:
            Delegates to mapped_swc property (CODING_RULE_V2_00017)
        """
        return self.mapped_swc  # Delegates to property

    def setMappedSwc(self, value: "SwcService") -> "DiagnosticFimFunctionMapping":
        """
        AUTOSAR-compliant setter for mappedSwc with method chaining.

        Args:
            value: The mappedSwc to set

        Returns:
            self for method chaining

        Note:
            Delegates to mapped_swc property setter (gets validation automatically)
        """
        self.mapped_swc = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_mapped_bsw(self, value: Optional["BswService"]) -> "DiagnosticFimFunctionMapping":
        """
        Set mappedBsw and return self for chaining.

        Args:
            value: The mappedBsw to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mapped_bsw("value")
        """
        self.mapped_bsw = value  # Use property setter (gets validation)
        return self

    def with_mapped_flat_swc(self, value: Optional["SwcService"]) -> "DiagnosticFimFunctionMapping":
        """
        Set mappedFlatSwc and return self for chaining.

        Args:
            value: The mappedFlatSwc to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mapped_flat_swc("value")
        """
        self.mapped_flat_swc = value  # Use property setter (gets validation)
        return self

    def with_mapped(self, value: Optional["DiagnosticFunction"]) -> "DiagnosticFimFunctionMapping":
        """
        Set mapped and return self for chaining.

        Args:
            value: The mapped to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mapped("value")
        """
        self.mapped = value  # Use property setter (gets validation)
        return self

    def with_mapped_swc(self, value: Optional["SwcService"]) -> "DiagnosticFimFunctionMapping":
        """
        Set mappedSwc and return self for chaining.

        Args:
            value: The mappedSwc to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mapped_swc("value")
        """
        self.mapped_swc = value  # Use property setter (gets validation)
        return self
