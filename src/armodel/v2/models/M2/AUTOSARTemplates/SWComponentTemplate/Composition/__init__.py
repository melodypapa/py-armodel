"""
AUTOSAR Package - Composition

Package: M2::AUTOSARTemplates::SWComponentTemplate::Composition
"""


from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.__init__ import (
    SwComponentType,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.__init__ import (
    InstantiationRTEEventProps,
    SwConnector,
)


class CompositionSwComponentType(SwComponentType):
    """
    A CompositionSwComponentType aggregates SwComponentPrototypes (that in turn
    are typed by SwComponentTypes) as well as SwConnectors for primarily
    connecting SwComponentPrototypes among each others and towards the surface
    of the CompositionSwComponentType. By this means, a hierarchical structures
    of software-components can be created.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Composition::CompositionSwComponentType

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 307, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 291, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 75, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 895, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 219, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 21, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 434, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The instantiated components that are part of this The aggregation of subject
                # to variability with to support the conditional existence of a be aware: if
                # the of SwComponentPrototypes is the deselected still contained in the but the
                # instances are inactive in that they are by the RTE.
        # is marked as atpSplitable in order to addition of service components to the
                # ECU the ECU integration.
        # case for having 0 components owned by the be to deliver an to e.
        # g.
        # a filling the internal structure.
        # atpVariation.
        self._component: List["SwComponent"] = []

    @property
    def component(self) -> List["SwComponent"]:
        """Get component (Pythonic accessor)."""
        return self._component
        # SwConnectors have the principal ability to establish a PortPrototypes.
        # They can have in the context of a are refined of SwConnectors is subject to
                # the purpose to support variant data flow.
        # is marked as atpSplitable in order to extension of the ECU extract with the
                # ECU atpVariation.
        self._connector: List[SwConnector] = []

    @property
    def connector(self) -> List[SwConnector]:
        """Get connector (Pythonic accessor)."""
        return self._connector
        # Reference to the ConstantSpecificationMapping to be applied for initValues of
        # PPortComSpecs and 719 Document ID 673:
        # AUTOSAR_CP_TPS_DiagnosticExtractTemplate Template R23-11.
        self._constantValue: List["ConstantSpecification"] = []

    @property
    def constant_value(self) -> List["ConstantSpecification"]:
        """Get constantValue (Pythonic accessor)."""
        return self._constantValue
        # Reference to the DataTypeMappingSet to be applied the used
                # ApplicationDataTypes in developing subsystems it may happen are used on the
                # surface In this case it reasonable to be able to also provide the to the
                # ImplementationDataTypes.
        # mapping shall be informal and not for the implementors mainly because
                # generator is not concerned about the the mapping of ApplicationDataTypes
                # delegated and inner PortPrototype matches mapping to ImplementationDataTypes
                # is not.
        self._dataType: List[RefType] = []

    @property
    def data_type(self) -> List[RefType]:
        """Get dataType (Pythonic accessor)."""
        return self._dataType
        # This allows to define instantiation specific properties for RTE Events, in
                # particular for instance specific scheduling.
        # atpVariation.
        self._instantiation: List["InstantiationRTEEvent"] = []

    @property
    def instantiation(self) -> List["InstantiationRTEEvent"]:
        """Get instantiation (Pythonic accessor)."""
        return self._instantiation
        # This reference identifies the PhysicalDimensionMappingSet that is applicable
        # in context of the enclosing in the be taken into the assessment of the
        # compatibility of the context of creation of a the scope of the.
        self._physical: Optional["PhysicalDimension"] = None

    @property
    def physical(self) -> Optional["PhysicalDimension"]:
        """Get physical (Pythonic accessor)."""
        return self._physical

    @physical.setter
    def physical(self, value: Optional["PhysicalDimension"]) -> None:
        """
        Set physical with validation.

        Args:
            value: The physical to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._physical = None
            return

        if not isinstance(value, PhysicalDimension):
            raise TypeError(
                f"physical must be PhysicalDimension or None, got {type(value).__name__}"
            )
        self._physical = value

    def with_component(self, value):
        """
        Set component and return self for chaining.

        Args:
            value: The component to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_component("value")
        """
        self.component = value  # Use property setter (gets validation)
        return self

    def with_connector(self, value):
        """
        Set connector and return self for chaining.

        Args:
            value: The connector to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_connector("value")
        """
        self.connector = value  # Use property setter (gets validation)
        return self

    def with_constant_value(self, value):
        """
        Set constant_value and return self for chaining.

        Args:
            value: The constant_value to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_constant_value("value")
        """
        self.constant_value = value  # Use property setter (gets validation)
        return self

    def with_data_type(self, value):
        """
        Set data_type and return self for chaining.

        Args:
            value: The data_type to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_type("value")
        """
        self.data_type = value  # Use property setter (gets validation)
        return self

    def with_instantiation(self, value):
        """
        Set instantiation and return self for chaining.

        Args:
            value: The instantiation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_instantiation("value")
        """
        self.instantiation = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getComponent(self) -> List["SwComponent"]:
        """
        AUTOSAR-compliant getter for component.

        Returns:
            The component value

        Note:
            Delegates to component property (CODING_RULE_V2_00017)
        """
        return self.component  # Delegates to property

    def getConnector(self) -> List[SwConnector]:
        """
        AUTOSAR-compliant getter for connector.

        Returns:
            The connector value

        Note:
            Delegates to connector property (CODING_RULE_V2_00017)
        """
        return self.connector  # Delegates to property

    def getConstantValue(self) -> List["ConstantSpecification"]:
        """
        AUTOSAR-compliant getter for constantValue.

        Returns:
            The constantValue value

        Note:
            Delegates to constant_value property (CODING_RULE_V2_00017)
        """
        return self.constant_value  # Delegates to property

    def getDataType(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for dataType.

        Returns:
            The dataType value

        Note:
            Delegates to data_type property (CODING_RULE_V2_00017)
        """
        return self.data_type  # Delegates to property

    def getInstantiation(self) -> List["InstantiationRTEEvent"]:
        """
        AUTOSAR-compliant getter for instantiation.

        Returns:
            The instantiation value

        Note:
            Delegates to instantiation property (CODING_RULE_V2_00017)
        """
        return self.instantiation  # Delegates to property

    def getPhysical(self) -> "PhysicalDimension":
        """
        AUTOSAR-compliant getter for physical.

        Returns:
            The physical value

        Note:
            Delegates to physical property (CODING_RULE_V2_00017)
        """
        return self.physical  # Delegates to property

    def setPhysical(self, value: "PhysicalDimension") -> CompositionSwComponentType:
        """
        AUTOSAR-compliant setter for physical with method chaining.

        Args:
            value: The physical to set

        Returns:
            self for method chaining

        Note:
            Delegates to physical property setter (gets validation automatically)
        """
        self.physical = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_physical(self, value: Optional["PhysicalDimension"]) -> CompositionSwComponentType:
        """
        Set physical and return self for chaining.

        Args:
            value: The physical to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_physical("value")
        """
        self.physical = value  # Use property setter (gets validation)
        return self



class SwComponentPrototype(Identifiable):
    """
    Role of a software component within a composition.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Composition::SwComponentPrototype

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 330, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 307, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 77, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 896, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 245, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 21, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 79, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 466, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 210, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        self._type: Optional[SwComponentType] = None

    @property
    def type(self) -> Optional[SwComponentType]:
        """Get type (Pythonic accessor)."""
        return self._type

    @type.setter
    def type(self, value: Optional[SwComponentType]) -> None:
        """
        Set type with validation.

        Args:
            value: The type to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._type = None
            return

        if not isinstance(value, SwComponentType):
            raise TypeError(
                f"type must be SwComponentType or None, got {type(value).__name__}"
            )
        self._type = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getType(self) -> SwComponentType:
        """
        AUTOSAR-compliant getter for type.

        Returns:
            The type value

        Note:
            Delegates to type property (CODING_RULE_V2_00017)
        """
        return self.type  # Delegates to property

    def setType(self, value: SwComponentType) -> SwComponentPrototype:
        """
        AUTOSAR-compliant setter for type with method chaining.

        Args:
            value: The type to set

        Returns:
            self for method chaining

        Note:
            Delegates to type property setter (gets validation automatically)
        """
        self.type = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_type(self, value: Optional[SwComponentType]) -> SwComponentPrototype:
        """
        Set type and return self for chaining.

        Args:
            value: The type to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_type("value")
        """
        self.type = value  # Use property setter (gets validation)
        return self



class SwConnector(Identifiable, ABC):
    """
    The base class for connectors between ports. Connectors have to be
    identifiable to allow references from the system constraint template.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Composition::SwConnector

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 307, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 80, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2061, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is SwConnector:
            raise TypeError("SwConnector is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to a PortInterfaceMapping specifying the unequal named
        # PortInterface elements of the PortInterfaces typing the two PortPrototypes
        # referenced by the ConnectorPrototype.
        self._mapping: Optional[RefType] = None

    @property
    def mapping(self) -> Optional[RefType]:
        """Get mapping (Pythonic accessor)."""
        return self._mapping

    @mapping.setter
    def mapping(self, value: Optional[RefType]) -> None:
        """
        Set mapping with validation.

        Args:
            value: The mapping to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mapping = None
            return

        self._mapping = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMapping(self) -> RefType:
        """
        AUTOSAR-compliant getter for mapping.

        Returns:
            The mapping value

        Note:
            Delegates to mapping property (CODING_RULE_V2_00017)
        """
        return self.mapping  # Delegates to property

    def setMapping(self, value: RefType) -> SwConnector:
        """
        AUTOSAR-compliant setter for mapping with method chaining.

        Args:
            value: The mapping to set

        Returns:
            self for method chaining

        Note:
            Delegates to mapping property setter (gets validation automatically)
        """
        self.mapping = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_mapping(self, value: Optional[RefType]) -> SwConnector:
        """
        Set mapping and return self for chaining.

        Args:
            value: The mapping to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mapping("value")
        """
        self.mapping = value  # Use property setter (gets validation)
        return self



class InstantiationRTEEventProps(ARObject, ABC):
    """
    This meta-class represents the ability to refine the properties of RTEEvents
    for particular instances of a software component.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Composition::InstantiationRTEEventProps

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 85, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is InstantiationRTEEventProps:
            raise TypeError("InstantiationRTEEventProps is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # be refined on an instance level.
        # by: InstanceEventIn.
        self._refinedEvent: Optional[RTEEvent] = None

    @property
    def refined_event(self) -> Optional[RTEEvent]:
        """Get refinedEvent (Pythonic accessor)."""
        return self._refinedEvent

    @refined_event.setter
    def refined_event(self, value: Optional[RTEEvent]) -> None:
        """
        Set refinedEvent with validation.

        Args:
            value: The refinedEvent to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._refinedEvent = None
            return

        if not isinstance(value, RTEEvent):
            raise TypeError(
                f"refinedEvent must be RTEEvent or None, got {type(value).__name__}"
            )
        self._refinedEvent = value
        # The main purpose of the shortLabel is to contribute to the aggregations that
        # are <<atpSplitable>>.
        self._shortLabel: Optional["Identifier"] = None

    @property
    def short_label(self) -> Optional["Identifier"]:
        """Get shortLabel (Pythonic accessor)."""
        return self._shortLabel

    @short_label.setter
    def short_label(self, value: Optional["Identifier"]) -> None:
        """
        Set shortLabel with validation.

        Args:
            value: The shortLabel to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._shortLabel = None
            return

        if not isinstance(value, (Identifier, str)):
            raise TypeError(
                f"shortLabel must be Identifier or str or None, got {type(value).__name__}"
            )
        self._shortLabel = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRefinedEvent(self) -> RTEEvent:
        """
        AUTOSAR-compliant getter for refinedEvent.

        Returns:
            The refinedEvent value

        Note:
            Delegates to refined_event property (CODING_RULE_V2_00017)
        """
        return self.refined_event  # Delegates to property

    def setRefinedEvent(self, value: RTEEvent) -> InstantiationRTEEventProps:
        """
        AUTOSAR-compliant setter for refinedEvent with method chaining.

        Args:
            value: The refinedEvent to set

        Returns:
            self for method chaining

        Note:
            Delegates to refined_event property setter (gets validation automatically)
        """
        self.refined_event = value  # Delegates to property setter
        return self

    def getShortLabel(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for shortLabel.

        Returns:
            The shortLabel value

        Note:
            Delegates to short_label property (CODING_RULE_V2_00017)
        """
        return self.short_label  # Delegates to property

    def setShortLabel(self, value: "Identifier") -> InstantiationRTEEventProps:
        """
        AUTOSAR-compliant setter for shortLabel with method chaining.

        Args:
            value: The shortLabel to set

        Returns:
            self for method chaining

        Note:
            Delegates to short_label property setter (gets validation automatically)
        """
        self.short_label = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_refined_event(self, value: Optional[RTEEvent]) -> InstantiationRTEEventProps:
        """
        Set refinedEvent and return self for chaining.

        Args:
            value: The refinedEvent to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_refined_event("value")
        """
        self.refined_event = value  # Use property setter (gets validation)
        return self

    def with_short_label(self, value: Optional["Identifier"]) -> InstantiationRTEEventProps:
        """
        Set shortLabel and return self for chaining.

        Args:
            value: The shortLabel to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_short_label("value")
        """
        self.short_label = value  # Use property setter (gets validation)
        return self



class AssemblySwConnector(SwConnector):
    """
    AssemblySwConnectors are exclusively used to connect SwComponentPrototypes
    in the context of a CompositionSwComponentType.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Composition::AssemblySwConnector

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 289, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 80, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2000, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 423, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # implemented by: PPortInComposition.
        self._providerInstanceRef: Optional[AbstractProvidedPort] = None

    @property
    def provider_instance_ref(self) -> Optional[AbstractProvidedPort]:
        """Get providerInstanceRef (Pythonic accessor)."""
        return self._providerInstanceRef

    @provider_instance_ref.setter
    def provider_instance_ref(self, value: Optional[AbstractProvidedPort]) -> None:
        """
        Set providerInstanceRef with validation.

        Args:
            value: The providerInstanceRef to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._providerInstanceRef = None
            return

        if not isinstance(value, AbstractProvidedPort):
            raise TypeError(
                f"providerInstanceRef must be AbstractProvidedPort or None, got {type(value).__name__}"
            )
        self._providerInstanceRef = value
        # implemented by: RPortInComposition.
        self._requesterInstanceRef: Optional[AbstractRequiredPort] = None

    @property
    def requester_instance_ref(self) -> Optional[AbstractRequiredPort]:
        """Get requesterInstanceRef (Pythonic accessor)."""
        return self._requesterInstanceRef

    @requester_instance_ref.setter
    def requester_instance_ref(self, value: Optional[AbstractRequiredPort]) -> None:
        """
        Set requesterInstanceRef with validation.

        Args:
            value: The requesterInstanceRef to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._requesterInstanceRef = None
            return

        if not isinstance(value, AbstractRequiredPort):
            raise TypeError(
                f"requesterInstanceRef must be AbstractRequiredPort or None, got {type(value).__name__}"
            )
        self._requesterInstanceRef = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getProviderInstanceRef(self) -> AbstractProvidedPort:
        """
        AUTOSAR-compliant getter for providerInstanceRef.

        Returns:
            The providerInstanceRef value

        Note:
            Delegates to provider_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.provider_instance_ref  # Delegates to property

    def setProviderInstanceRef(self, value: AbstractProvidedPort) -> AssemblySwConnector:
        """
        AUTOSAR-compliant setter for providerInstanceRef with method chaining.

        Args:
            value: The providerInstanceRef to set

        Returns:
            self for method chaining

        Note:
            Delegates to provider_instance_ref property setter (gets validation automatically)
        """
        self.provider_instance_ref = value  # Delegates to property setter
        return self

    def getRequesterInstanceRef(self) -> AbstractRequiredPort:
        """
        AUTOSAR-compliant getter for requesterInstanceRef.

        Returns:
            The requesterInstanceRef value

        Note:
            Delegates to requester_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.requester_instance_ref  # Delegates to property

    def setRequesterInstanceRef(self, value: AbstractRequiredPort) -> AssemblySwConnector:
        """
        AUTOSAR-compliant setter for requesterInstanceRef with method chaining.

        Args:
            value: The requesterInstanceRef to set

        Returns:
            self for method chaining

        Note:
            Delegates to requester_instance_ref property setter (gets validation automatically)
        """
        self.requester_instance_ref = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_provider_instance_ref(self, value: Optional[AbstractProvidedPort]) -> AssemblySwConnector:
        """
        Set providerInstanceRef and return self for chaining.

        Args:
            value: The providerInstanceRef to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_provider_instance_ref("value")
        """
        self.provider_instance_ref = value  # Use property setter (gets validation)
        return self

    def with_requester_instance_ref(self, value: Optional[AbstractRequiredPort]) -> AssemblySwConnector:
        """
        Set requesterInstanceRef and return self for chaining.

        Args:
            value: The requesterInstanceRef to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_requester_instance_ref("value")
        """
        self.requester_instance_ref = value  # Use property setter (gets validation)
        return self



class DelegationSwConnector(SwConnector):
    """
    A delegation connector delegates one inner PortPrototype (a port of a
    component that is used inside the composition) to a outer PortPrototype of
    compatible type that belongs directly to the composition (a port that is
    owned by the composition).

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Composition::DelegationSwConnector

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 80, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2016, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # by: PortInCompositionType.
        self._innerPortInstanceRef: Optional[RefType] = None

    @property
    def inner_port_instance_ref(self) -> Optional[RefType]:
        """Get innerPortInstanceRef (Pythonic accessor)."""
        return self._innerPortInstanceRef

    @inner_port_instance_ref.setter
    def inner_port_instance_ref(self, value: Optional[RefType]) -> None:
        """
        Set innerPortInstanceRef with validation.

        Args:
            value: The innerPortInstanceRef to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._innerPortInstanceRef = None
            return

        self._innerPortInstanceRef = value
        # The port that is located on the outside of the Composition.
        self._outerPort: Optional[RefType] = None

    @property
    def outer_port(self) -> Optional[RefType]:
        """Get outerPort (Pythonic accessor)."""
        return self._outerPort

    @outer_port.setter
    def outer_port(self, value: Optional[RefType]) -> None:
        """
        Set outerPort with validation.

        Args:
            value: The outerPort to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._outerPort = None
            return

        self._outerPort = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getInnerPortInstanceRef(self) -> RefType:
        """
        AUTOSAR-compliant getter for innerPortInstanceRef.

        Returns:
            The innerPortInstanceRef value

        Note:
            Delegates to inner_port_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.inner_port_instance_ref  # Delegates to property

    def setInnerPortInstanceRef(self, value: RefType) -> DelegationSwConnector:
        """
        AUTOSAR-compliant setter for innerPortInstanceRef with method chaining.

        Args:
            value: The innerPortInstanceRef to set

        Returns:
            self for method chaining

        Note:
            Delegates to inner_port_instance_ref property setter (gets validation automatically)
        """
        self.inner_port_instance_ref = value  # Delegates to property setter
        return self

    def getOuterPort(self) -> RefType:
        """
        AUTOSAR-compliant getter for outerPort.

        Returns:
            The outerPort value

        Note:
            Delegates to outer_port property (CODING_RULE_V2_00017)
        """
        return self.outer_port  # Delegates to property

    def setOuterPort(self, value: RefType) -> DelegationSwConnector:
        """
        AUTOSAR-compliant setter for outerPort with method chaining.

        Args:
            value: The outerPort to set

        Returns:
            self for method chaining

        Note:
            Delegates to outer_port property setter (gets validation automatically)
        """
        self.outer_port = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_inner_port_instance_ref(self, value: Optional[RefType]) -> DelegationSwConnector:
        """
        Set innerPortInstanceRef and return self for chaining.

        Args:
            value: The innerPortInstanceRef to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_inner_port_instance_ref("value")
        """
        self.inner_port_instance_ref = value  # Use property setter (gets validation)
        return self

    def with_outer_port(self, value: Optional[RefType]) -> DelegationSwConnector:
        """
        Set outerPort and return self for chaining.

        Args:
            value: The outerPort to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_outer_port("value")
        """
        self.outer_port = value  # Use property setter (gets validation)
        return self



class PassThroughSwConnector(SwConnector):
    """
    This kind of SwConnector can be used inside a CompositionSwComponentType to
    connect two delegation PortPrototypes.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Composition::PassThroughSwConnector

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 83, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2043, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the provided outer delegation Port Prototype of the
        # PassThroughSwConnector.
        self._providedOuter: Optional[AbstractProvidedPort] = None

    @property
    def provided_outer(self) -> Optional[AbstractProvidedPort]:
        """Get providedOuter (Pythonic accessor)."""
        return self._providedOuter

    @provided_outer.setter
    def provided_outer(self, value: Optional[AbstractProvidedPort]) -> None:
        """
        Set providedOuter with validation.

        Args:
            value: The providedOuter to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._providedOuter = None
            return

        if not isinstance(value, AbstractProvidedPort):
            raise TypeError(
                f"providedOuter must be AbstractProvidedPort or None, got {type(value).__name__}"
            )
        self._providedOuter = value
        # This represents the required outer delegation Port Prototype of the
        # PassThroughSwConnector.
        self._requiredOuter: Optional[AbstractRequiredPort] = None

    @property
    def required_outer(self) -> Optional[AbstractRequiredPort]:
        """Get requiredOuter (Pythonic accessor)."""
        return self._requiredOuter

    @required_outer.setter
    def required_outer(self, value: Optional[AbstractRequiredPort]) -> None:
        """
        Set requiredOuter with validation.

        Args:
            value: The requiredOuter to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._requiredOuter = None
            return

        if not isinstance(value, AbstractRequiredPort):
            raise TypeError(
                f"requiredOuter must be AbstractRequiredPort or None, got {type(value).__name__}"
            )
        self._requiredOuter = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getProvidedOuter(self) -> AbstractProvidedPort:
        """
        AUTOSAR-compliant getter for providedOuter.

        Returns:
            The providedOuter value

        Note:
            Delegates to provided_outer property (CODING_RULE_V2_00017)
        """
        return self.provided_outer  # Delegates to property

    def setProvidedOuter(self, value: AbstractProvidedPort) -> PassThroughSwConnector:
        """
        AUTOSAR-compliant setter for providedOuter with method chaining.

        Args:
            value: The providedOuter to set

        Returns:
            self for method chaining

        Note:
            Delegates to provided_outer property setter (gets validation automatically)
        """
        self.provided_outer = value  # Delegates to property setter
        return self

    def getRequiredOuter(self) -> AbstractRequiredPort:
        """
        AUTOSAR-compliant getter for requiredOuter.

        Returns:
            The requiredOuter value

        Note:
            Delegates to required_outer property (CODING_RULE_V2_00017)
        """
        return self.required_outer  # Delegates to property

    def setRequiredOuter(self, value: AbstractRequiredPort) -> PassThroughSwConnector:
        """
        AUTOSAR-compliant setter for requiredOuter with method chaining.

        Args:
            value: The requiredOuter to set

        Returns:
            self for method chaining

        Note:
            Delegates to required_outer property setter (gets validation automatically)
        """
        self.required_outer = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_provided_outer(self, value: Optional[AbstractProvidedPort]) -> PassThroughSwConnector:
        """
        Set providedOuter and return self for chaining.

        Args:
            value: The providedOuter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_provided_outer("value")
        """
        self.provided_outer = value  # Use property setter (gets validation)
        return self

    def with_required_outer(self, value: Optional[AbstractRequiredPort]) -> PassThroughSwConnector:
        """
        Set requiredOuter and return self for chaining.

        Args:
            value: The requiredOuter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_required_outer("value")
        """
        self.required_outer = value  # Use property setter (gets validation)
        return self



class InstantiationTimingEventProps(InstantiationRTEEventProps):
    """
    This meta-class represents the ability to refine a timing event for
    particular instances of a software component. This approach supports an
    instance specific timing.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Composition::InstantiationTimingEventProps

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 85, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute represents the value of the refined.
        self._period: Optional[TimeValue] = None

    @property
    def period(self) -> Optional[TimeValue]:
        """Get period (Pythonic accessor)."""
        return self._period

    @period.setter
    def period(self, value: Optional[TimeValue]) -> None:
        """
        Set period with validation.

        Args:
            value: The period to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._period = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"period must be TimeValue or None, got {type(value).__name__}"
            )
        self._period = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getPeriod(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for period.

        Returns:
            The period value

        Note:
            Delegates to period property (CODING_RULE_V2_00017)
        """
        return self.period  # Delegates to property

    def setPeriod(self, value: TimeValue) -> InstantiationTimingEventProps:
        """
        AUTOSAR-compliant setter for period with method chaining.

        Args:
            value: The period to set

        Returns:
            self for method chaining

        Note:
            Delegates to period property setter (gets validation automatically)
        """
        self.period = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_period(self, value: Optional[TimeValue]) -> InstantiationTimingEventProps:
        """
        Set period and return self for chaining.

        Args:
            value: The period to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_period("value")
        """
        self.period = value  # Use property setter (gets validation)
        return self


__all__ = [
    CompositionSwComponentType,
    SwComponentPrototype,
    SwConnector,
    InstantiationRTEEventProps,
    AssemblySwConnector,
    DelegationSwConnector,
    PassThroughSwConnector,
    InstantiationTimingEventProps,
]
