"""
AUTOSAR Package - Components

Package: M2::AUTOSARTemplates::SWComponentTemplate::Components
"""


from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Implementation import (
    ImplementationProps,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class PortPrototype(Identifiable, ABC):
    """
    Base class for the ports of an AUTOSAR software component. The aggregation
    of PortPrototypes is subject to variability with the purpose to support the
    conditional existence of ports.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components::PortPrototype

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 326, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 326, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 304, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (Page 62, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 66, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2047, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 236, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_ARXMLSerializationRules.pdf (Page 30, Foundation R23-11)
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 48, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 76, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 458, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (Page 33, Foundation R23-11)
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 65, Foundation R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 201, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is PortPrototype:
            raise TypeError("PortPrototype is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Annotation of this PortPrototype with respect to client/ communication.
        self._clientServer: List["ClientServerAnnotation"] = []

    @property
    def client_server(self) -> List["ClientServerAnnotation"]:
        """Get clientServer (Pythonic accessor)."""
        return self._clientServer
        # Annotations on this delegated port.
        self._delegatedPort: Optional["DelegatedPort"] = None

    @property
    def delegated_port(self) -> Optional["DelegatedPort"]:
        """Get delegatedPort (Pythonic accessor)."""
        return self._delegatedPort

    @delegated_port.setter
    def delegated_port(self, value: Optional["DelegatedPort"]) -> None:
        """
        Set delegatedPort with validation.

        Args:
            value: The delegatedPort to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._delegatedPort = None
            return

        if not isinstance(value, DelegatedPort):
            raise TypeError(
                f"delegatedPort must be DelegatedPort or None, got {type(value).__name__}"
            )
        self._delegatedPort = value
        # Annotations on this IO Hardware Abstraction port.
        self._ioHwAbstractionAnnotation: List["IoHwAbstractionServer"] = []

    @property
    def io_hw_abstraction_annotation(self) -> List["IoHwAbstractionServer"]:
        """Get ioHwAbstractionAnnotation (Pythonic accessor)."""
        return self._ioHwAbstractionAnnotation
        # Annotations on this mode port.
        self._modePortAnnotation: List["ModePortAnnotation"] = []

    @property
    def mode_port_annotation(self) -> List["ModePortAnnotation"]:
        """Get modePortAnnotation (Pythonic accessor)."""
        return self._modePortAnnotation
        # Annotations on this non voilatile data port.
        self._nvDataPortAnnotation: List["NvDataPortAnnotation"] = []

    @property
    def nv_data_port_annotation(self) -> List["NvDataPortAnnotation"]:
        """Get nvDataPortAnnotation (Pythonic accessor)."""
        return self._nvDataPortAnnotation
        # Annotations on this parameter port.
        self._parameterPort: List["ParameterPort"] = []

    @property
    def parameter_port(self) -> List["ParameterPort"]:
        """Get parameterPort (Pythonic accessor)."""
        return self._parameterPort
        # Collection of annotations of this ports sender/receiver communication.
        self._senderReceiver: List["SenderReceiver"] = []

    @property
    def sender_receiver(self) -> List["SenderReceiver"]:
        """Get senderReceiver (Pythonic accessor)."""
        return self._senderReceiver
        # Annotations on this trigger port.
        self._triggerPortAnnotation: List[RefType] = []

    @property
    def trigger_port_annotation(self) -> List[RefType]:
        """Get triggerPortAnnotation (Pythonic accessor)."""
        return self._triggerPortAnnotation

    def with_client_server(self, value):
        """
        Set client_server and return self for chaining.

        Args:
            value: The client_server to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_client_server("value")
        """
        self.client_server = value  # Use property setter (gets validation)
        return self

    def with_io_hw_abstraction_annotation(self, value):
        """
        Set io_hw_abstraction_annotation and return self for chaining.

        Args:
            value: The io_hw_abstraction_annotation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_io_hw_abstraction_annotation("value")
        """
        self.io_hw_abstraction_annotation = value  # Use property setter (gets validation)
        return self

    def with_mode_port_annotation(self, value):
        """
        Set mode_port_annotation and return self for chaining.

        Args:
            value: The mode_port_annotation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mode_port_annotation("value")
        """
        self.mode_port_annotation = value  # Use property setter (gets validation)
        return self

    def with_nv_data_port_annotation(self, value):
        """
        Set nv_data_port_annotation and return self for chaining.

        Args:
            value: The nv_data_port_annotation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nv_data_port_annotation("value")
        """
        self.nv_data_port_annotation = value  # Use property setter (gets validation)
        return self

    def with_parameter_port(self, value):
        """
        Set parameter_port and return self for chaining.

        Args:
            value: The parameter_port to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_parameter_port("value")
        """
        self.parameter_port = value  # Use property setter (gets validation)
        return self

    def with_sender_receiver(self, value):
        """
        Set sender_receiver and return self for chaining.

        Args:
            value: The sender_receiver to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sender_receiver("value")
        """
        self.sender_receiver = value  # Use property setter (gets validation)
        return self

    def with_trigger_port_annotation(self, value):
        """
        Set trigger_port_annotation and return self for chaining.

        Args:
            value: The trigger_port_annotation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_trigger_port_annotation("value")
        """
        self.trigger_port_annotation = value  # Use property setter (gets validation)
        return self

    def with_consistency(self, value):
        """
        Set consistency and return self for chaining.

        Args:
            value: The consistency to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_consistency("value")
        """
        self.consistency = value  # Use property setter (gets validation)
        return self

    def with_port(self, value):
        """
        Set port and return self for chaining.

        Args:
            value: The port to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_port("value")
        """
        self.port = value  # Use property setter (gets validation)
        return self

    def with_port_group(self, value):
        """
        Set port_group and return self for chaining.

        Args:
            value: The port_group to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_port_group("value")
        """
        self.port_group = value  # Use property setter (gets validation)
        return self

    def with_swc_mapping(self, value):
        """
        Set swc_mapping and return self for chaining.

        Args:
            value: The swc_mapping to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_swc_mapping("value")
        """
        self.swc_mapping = value  # Use property setter (gets validation)
        return self

    def with_unit_group(self, value):
        """
        Set unit_group and return self for chaining.

        Args:
            value: The unit_group to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_unit_group("value")
        """
        self.unit_group = value  # Use property setter (gets validation)
        return self

    def with_inner_group(self, value):
        """
        Set inner_group and return self for chaining.

        Args:
            value: The inner_group to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_inner_group("value")
        """
        self.inner_group = value  # Use property setter (gets validation)
        return self

    def with_outer_port(self, value):
        """
        Set outer_port and return self for chaining.

        Args:
            value: The outer_port to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_outer_port("value")
        """
        self.outer_port = value  # Use property setter (gets validation)
        return self

    def with_required_com(self, value):
        """
        Set required_com and return self for chaining.

        Args:
            value: The required_com to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_required_com("value")
        """
        self.required_com = value  # Use property setter (gets validation)
        return self

    def with_provided_com(self, value):
        """
        Set provided_com and return self for chaining.

        Args:
            value: The provided_com to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_provided_com("value")
        """
        self.provided_com = value  # Use property setter (gets validation)
        return self

    def with_constant(self, value):
        """
        Set constant and return self for chaining.

        Args:
            value: The constant to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_constant("value")
        """
        self.constant = value  # Use property setter (gets validation)
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

    def with_hardware(self, value):
        """
        Set hardware and return self for chaining.

        Args:
            value: The hardware to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_hardware("value")
        """
        self.hardware = value  # Use property setter (gets validation)
        return self

    def with_hardware(self, value):
        """
        Set hardware and return self for chaining.

        Args:
            value: The hardware to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_hardware("value")
        """
        self.hardware = value  # Use property setter (gets validation)
        return self

    def with_bulk_nv_data(self, value):
        """
        Set bulk_nv_data and return self for chaining.

        Args:
            value: The bulk_nv_data to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bulk_nv_data("value")
        """
        self.bulk_nv_data = value  # Use property setter (gets validation)
        return self

    def with_nv_block(self, value):
        """
        Set nv_block and return self for chaining.

        Args:
            value: The nv_block to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nv_block("value")
        """
        self.nv_block = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getClientServer(self) -> List["ClientServerAnnotation"]:
        """
        AUTOSAR-compliant getter for clientServer.

        Returns:
            The clientServer value

        Note:
            Delegates to client_server property (CODING_RULE_V2_00017)
        """
        return self.client_server  # Delegates to property

    def getDelegatedPort(self) -> "DelegatedPort":
        """
        AUTOSAR-compliant getter for delegatedPort.

        Returns:
            The delegatedPort value

        Note:
            Delegates to delegated_port property (CODING_RULE_V2_00017)
        """
        return self.delegated_port  # Delegates to property

    def setDelegatedPort(self, value: "DelegatedPort") -> PortPrototype:
        """
        AUTOSAR-compliant setter for delegatedPort with method chaining.

        Args:
            value: The delegatedPort to set

        Returns:
            self for method chaining

        Note:
            Delegates to delegated_port property setter (gets validation automatically)
        """
        self.delegated_port = value  # Delegates to property setter
        return self

    def getIoHwAbstractionAnnotation(self) -> List["IoHwAbstractionServer"]:
        """
        AUTOSAR-compliant getter for ioHwAbstractionAnnotation.

        Returns:
            The ioHwAbstractionAnnotation value

        Note:
            Delegates to io_hw_abstraction_annotation property (CODING_RULE_V2_00017)
        """
        return self.io_hw_abstraction_annotation  # Delegates to property

    def getModePortAnnotation(self) -> List["ModePortAnnotation"]:
        """
        AUTOSAR-compliant getter for modePortAnnotation.

        Returns:
            The modePortAnnotation value

        Note:
            Delegates to mode_port_annotation property (CODING_RULE_V2_00017)
        """
        return self.mode_port_annotation  # Delegates to property

    def getNvDataPortAnnotation(self) -> List["NvDataPortAnnotation"]:
        """
        AUTOSAR-compliant getter for nvDataPortAnnotation.

        Returns:
            The nvDataPortAnnotation value

        Note:
            Delegates to nv_data_port_annotation property (CODING_RULE_V2_00017)
        """
        return self.nv_data_port_annotation  # Delegates to property

    def getParameterPort(self) -> List["ParameterPort"]:
        """
        AUTOSAR-compliant getter for parameterPort.

        Returns:
            The parameterPort value

        Note:
            Delegates to parameter_port property (CODING_RULE_V2_00017)
        """
        return self.parameter_port  # Delegates to property

    def getSenderReceiver(self) -> List["SenderReceiver"]:
        """
        AUTOSAR-compliant getter for senderReceiver.

        Returns:
            The senderReceiver value

        Note:
            Delegates to sender_receiver property (CODING_RULE_V2_00017)
        """
        return self.sender_receiver  # Delegates to property

    def getTriggerPortAnnotation(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for triggerPortAnnotation.

        Returns:
            The triggerPortAnnotation value

        Note:
            Delegates to trigger_port_annotation property (CODING_RULE_V2_00017)
        """
        return self.trigger_port_annotation  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_delegated_port(self, value: Optional["DelegatedPort"]) -> PortPrototype:
        """
        Set delegatedPort and return self for chaining.

        Args:
            value: The delegatedPort to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_delegated_port("value")
        """
        self.delegated_port = value  # Use property setter (gets validation)
        return self



class SwComponentType(ARElement, ABC):
    """
    Base class for AUTOSAR software components.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components::SwComponentType

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 330, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 64, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2060, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 245, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 22, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 466, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 210, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is SwComponentType:
            raise TypeError("SwComponentType is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the collection of ConsistencyNeeds by the enclosing
                # SwComponentType.
        # atpVariation.
        self._consistency: List["ConsistencyNeeds"] = []

    @property
    def consistency(self) -> List["ConsistencyNeeds"]:
        """Get consistency (Pythonic accessor)."""
        return self._consistency
        # The PortPrototypes through which this SwComponent communicate.
        # of PortPrototype is subject to variability purpose to support the conditional
                # existence of atpVariation.
        self._port: List[RefType] = []

    @property
    def port(self) -> List[RefType]:
        """Get port (Pythonic accessor)."""
        return self._port
        # A port group being part of this component.
        # atpVariation.
        self._portGroup: List[RefType] = []

    @property
    def port_group(self) -> List[RefType]:
        """Get portGroup (Pythonic accessor)."""
        return self._portGroup
        # Reference to constraints that are valid for this Sw ComponentType.
        self._swcMapping: List[RefType] = []

    @property
    def swc_mapping(self) -> List[RefType]:
        """Get swcMapping (Pythonic accessor)."""
        return self._swcMapping
        # This adds a documentation to the SwComponentType.
        # Stereotypes: atpSplitable; atpVariation.
        self._swComponent: Optional["SwComponent"] = None

    @property
    def sw_component(self) -> Optional["SwComponent"]:
        """Get swComponent (Pythonic accessor)."""
        return self._swComponent

    @sw_component.setter
    def sw_component(self, value: Optional["SwComponent"]) -> None:
        """
        Set swComponent with validation.

        Args:
            value: The swComponent to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swComponent = None
            return

        if not isinstance(value, SwComponent):
            raise TypeError(
                f"swComponent must be SwComponent or None, got {type(value).__name__}"
            )
        self._swComponent = value
        # This allows for the specification of which UnitGroups are the context of
        # referencing SwComponentType.
        self._unitGroup: List[RefType] = []

    @property
    def unit_group(self) -> List[RefType]:
        """Get unitGroup (Pythonic accessor)."""
        return self._unitGroup

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getConsistency(self) -> List["ConsistencyNeeds"]:
        """
        AUTOSAR-compliant getter for consistency.

        Returns:
            The consistency value

        Note:
            Delegates to consistency property (CODING_RULE_V2_00017)
        """
        return self.consistency  # Delegates to property

    def getPort(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for port.

        Returns:
            The port value

        Note:
            Delegates to port property (CODING_RULE_V2_00017)
        """
        return self.port  # Delegates to property

    def getPortGroup(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for portGroup.

        Returns:
            The portGroup value

        Note:
            Delegates to port_group property (CODING_RULE_V2_00017)
        """
        return self.port_group  # Delegates to property

    def getSwcMapping(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for swcMapping.

        Returns:
            The swcMapping value

        Note:
            Delegates to swc_mapping property (CODING_RULE_V2_00017)
        """
        return self.swc_mapping  # Delegates to property

    def getSwComponent(self) -> "SwComponent":
        """
        AUTOSAR-compliant getter for swComponent.

        Returns:
            The swComponent value

        Note:
            Delegates to sw_component property (CODING_RULE_V2_00017)
        """
        return self.sw_component  # Delegates to property

    def setSwComponent(self, value: "SwComponent") -> SwComponentType:
        """
        AUTOSAR-compliant setter for swComponent with method chaining.

        Args:
            value: The swComponent to set

        Returns:
            self for method chaining

        Note:
            Delegates to sw_component property setter (gets validation automatically)
        """
        self.sw_component = value  # Delegates to property setter
        return self

    def getUnitGroup(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for unitGroup.

        Returns:
            The unitGroup value

        Note:
            Delegates to unit_group property (CODING_RULE_V2_00017)
        """
        return self.unit_group  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_sw_component(self, value: Optional["SwComponent"]) -> SwComponentType:
        """
        Set swComponent and return self for chaining.

        Args:
            value: The swComponent to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_component("value")
        """
        self.sw_component = value  # Use property setter (gets validation)
        return self



class PortGroup(Identifiable):
    """
    Group of ports which share a common functionality , e.g. need specific
    network resources. This information shall be available on the VFB level in
    order to delegate it properly via compositions. When propagated into the ECU
    extract, this information is used as input for the configuration of Services
    like the Communication Manager. A PortGroup is defined locally in a
    component (which can be a composition) and refers to the "outer" ports
    belonging to the group as well as to the "inner" groups which propagate this
    group into the components which are part of a composition. A PortGroup
    within an atomic SWC cannot be linked to inner groups.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components::PortGroup

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 203, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2045, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # defined in a component which is part of this by: InnerPortGroupIn.
        self._innerGroup: List[RefType] = []

    @property
    def inner_group(self) -> List[RefType]:
        """Get innerGroup (Pythonic accessor)."""
        return self._innerGroup
        # Outer PortPrototype of this AtomicSwComponentType to the group.
        # A port can belong to several to no group at all.
        # atpVariation.
        self._outerPort: List[RefType] = []

    @property
    def outer_port(self) -> List[RefType]:
        """Get outerPort (Pythonic accessor)."""
        return self._outerPort

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getInnerGroup(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for innerGroup.

        Returns:
            The innerGroup value

        Note:
            Delegates to inner_group property (CODING_RULE_V2_00017)
        """
        return self.inner_group  # Delegates to property

    def getOuterPort(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for outerPort.

        Returns:
            The outerPort value

        Note:
            Delegates to outer_port property (CODING_RULE_V2_00017)
        """
        return self.outer_port  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class SymbolProps(ImplementationProps):
    """
    This meta-class represents the ability to attach with the symbol attribute a
    symbolic name that is conform to C language requirements to another
    meta-class, e.g. AtomicSwComponentType, that is a potential subject to a
    name clash on the level of RTE source code.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components::SymbolProps

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 288, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2074, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 66, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class AbstractRequiredPortPrototype(PortPrototype, ABC):
    """
    This abstract class provides the ability to become a required PortPrototype.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components::AbstractRequiredPortPrototype

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 67, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 204, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 422, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is AbstractRequiredPortPrototype:
            raise TypeError("AbstractRequiredPortPrototype is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Required communication attributes, one for each element.
        self._requiredCom: List["RPortComSpec"] = []

    @property
    def required_com(self) -> List["RPortComSpec"]:
        """Get requiredCom (Pythonic accessor)."""
        return self._requiredCom

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRequiredCom(self) -> List["RPortComSpec"]:
        """
        AUTOSAR-compliant getter for requiredCom.

        Returns:
            The requiredCom value

        Note:
            Delegates to required_com property (CODING_RULE_V2_00017)
        """
        return self.required_com  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class AbstractProvidedPortPrototype(PortPrototype, ABC):
    """
    This abstract class provides the ability to become a provided PortPrototype.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components::AbstractProvidedPortPrototype

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 67, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is AbstractProvidedPortPrototype:
            raise TypeError("AbstractProvidedPortPrototype is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Provided communication attributes per interface element element or
        # operation).
        self._providedCom: List["PPortComSpec"] = []

    @property
    def provided_com(self) -> List["PPortComSpec"]:
        """Get providedCom (Pythonic accessor)."""
        return self._providedCom

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getProvidedCom(self) -> List["PPortComSpec"]:
        """
        AUTOSAR-compliant getter for providedCom.

        Returns:
            The providedCom value

        Note:
            Delegates to provided_com property (CODING_RULE_V2_00017)
        """
        return self.provided_com  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class AtomicSwComponentType(SwComponentType, ABC):
    """
    An atomic software component is atomic in the sense that it cannot be
    further decomposed and distributed across multiple ECUs.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components::AtomicSwComponentType

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 304, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 300, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 70, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2000, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 205, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 43, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 161, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is AtomicSwComponentType:
            raise TypeError("AtomicSwComponentType is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The SwcInternalBehaviors owned by an AtomicSw be located in a different
                # physical file.
        # aggregation is <<atpSplitable>>.
        # atpVariation.
        self._internalBehavior: Optional[SwcInternalBehavior] = None

    @property
    def internal_behavior(self) -> Optional[SwcInternalBehavior]:
        """Get internalBehavior (Pythonic accessor)."""
        return self._internalBehavior

    @internal_behavior.setter
    def internal_behavior(self, value: Optional[SwcInternalBehavior]) -> None:
        """
        Set internalBehavior with validation.

        Args:
            value: The internalBehavior to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._internalBehavior = None
            return

        if not isinstance(value, SwcInternalBehavior):
            raise TypeError(
                f"internalBehavior must be SwcInternalBehavior or None, got {type(value).__name__}"
            )
        self._internalBehavior = value
        # This represents the SymbolProps for the AtomicSw.
        self._symbolProps: Optional[SymbolProps] = None

    @property
    def symbol_props(self) -> Optional[SymbolProps]:
        """Get symbolProps (Pythonic accessor)."""
        return self._symbolProps

    @symbol_props.setter
    def symbol_props(self, value: Optional[SymbolProps]) -> None:
        """
        Set symbolProps with validation.

        Args:
            value: The symbolProps to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._symbolProps = None
            return

        if not isinstance(value, SymbolProps):
            raise TypeError(
                f"symbolProps must be SymbolProps or None, got {type(value).__name__}"
            )
        self._symbolProps = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getInternalBehavior(self) -> SwcInternalBehavior:
        """
        AUTOSAR-compliant getter for internalBehavior.

        Returns:
            The internalBehavior value

        Note:
            Delegates to internal_behavior property (CODING_RULE_V2_00017)
        """
        return self.internal_behavior  # Delegates to property

    def setInternalBehavior(self, value: SwcInternalBehavior) -> AtomicSwComponentType:
        """
        AUTOSAR-compliant setter for internalBehavior with method chaining.

        Args:
            value: The internalBehavior to set

        Returns:
            self for method chaining

        Note:
            Delegates to internal_behavior property setter (gets validation automatically)
        """
        self.internal_behavior = value  # Delegates to property setter
        return self

    def getSymbolProps(self) -> SymbolProps:
        """
        AUTOSAR-compliant getter for symbolProps.

        Returns:
            The symbolProps value

        Note:
            Delegates to symbol_props property (CODING_RULE_V2_00017)
        """
        return self.symbol_props  # Delegates to property

    def setSymbolProps(self, value: SymbolProps) -> AtomicSwComponentType:
        """
        AUTOSAR-compliant setter for symbolProps with method chaining.

        Args:
            value: The symbolProps to set

        Returns:
            self for method chaining

        Note:
            Delegates to symbol_props property setter (gets validation automatically)
        """
        self.symbol_props = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_internal_behavior(self, value: Optional[SwcInternalBehavior]) -> AtomicSwComponentType:
        """
        Set internalBehavior and return self for chaining.

        Args:
            value: The internalBehavior to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_internal_behavior("value")
        """
        self.internal_behavior = value  # Use property setter (gets validation)
        return self

    def with_symbol_props(self, value: Optional[SymbolProps]) -> AtomicSwComponentType:
        """
        Set symbolProps and return self for chaining.

        Args:
            value: The symbolProps to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_symbol_props("value")
        """
        self.symbol_props = value  # Use property setter (gets validation)
        return self



class ParameterSwComponentType(SwComponentType):
    """
    The ParameterSwComponentType defines parameters and characteristic values
    accessible via provided Ports. The provided values are the same for all
    connected SwComponentPrototypes

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components::ParameterSwComponentType

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 41, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2043, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the ConstantSpecificationMapping to be applied for the
        # particular ParameterSwComponentType.
        self._constant: List["ConstantSpecification"] = []

    @property
    def constant(self) -> List["ConstantSpecification"]:
        """Get constant (Pythonic accessor)."""
        return self._constant
        # Reference to the DataTypeMapping to be applied for the
        # ParameterSwComponentType.
        self._dataType: List[RefType] = []

    @property
    def data_type(self) -> List[RefType]:
        """Get dataType (Pythonic accessor)."""
        return self._dataType
        # The purpose of this is that within the context of a given SwComponentType
                # some data def properties of individual be modified.
        # of InstantiationDataDefProps is subject with the purpose to support the
                # conditional PortPrototypes atpVariation.
        self._instantiation: List["InstantiationDataDef"] = []

    @property
    def instantiation(self) -> List["InstantiationDataDef"]:
        """Get instantiation (Pythonic accessor)."""
        return self._instantiation

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getConstant(self) -> List["ConstantSpecification"]:
        """
        AUTOSAR-compliant getter for constant.

        Returns:
            The constant value

        Note:
            Delegates to constant property (CODING_RULE_V2_00017)
        """
        return self.constant  # Delegates to property

    def getDataType(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for dataType.

        Returns:
            The dataType value

        Note:
            Delegates to data_type property (CODING_RULE_V2_00017)
        """
        return self.data_type  # Delegates to property

    def getInstantiation(self) -> List["InstantiationDataDef"]:
        """
        AUTOSAR-compliant getter for instantiation.

        Returns:
            The instantiation value

        Note:
            Delegates to instantiation property (CODING_RULE_V2_00017)
        """
        return self.instantiation  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class PRPortPrototype(AbstractRequiredPortPrototype):
    """
    This kind of PortPrototype can take the role of both a required and a
    provided PortPrototype.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components::PRPortPrototype

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 325, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 68, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2042, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 199, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # isOfType.
        self._provided: Optional[PortInterface] = None

    @property
    def provided(self) -> Optional[PortInterface]:
        """Get provided (Pythonic accessor)."""
        return self._provided

    @provided.setter
    def provided(self, value: Optional[PortInterface]) -> None:
        """
        Set provided with validation.

        Args:
            value: The provided to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._provided = None
            return

        if not isinstance(value, PortInterface):
            raise TypeError(
                f"provided must be PortInterface or None, got {type(value).__name__}"
            )
        self._provided = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getProvided(self) -> PortInterface:
        """
        AUTOSAR-compliant getter for provided.

        Returns:
            The provided value

        Note:
            Delegates to provided property (CODING_RULE_V2_00017)
        """
        return self.provided  # Delegates to property

    def setProvided(self, value: PortInterface) -> PRPortPrototype:
        """
        AUTOSAR-compliant setter for provided with method chaining.

        Args:
            value: The provided to set

        Returns:
            self for method chaining

        Note:
            Delegates to provided property setter (gets validation automatically)
        """
        self.provided = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_provided(self, value: Optional[PortInterface]) -> PRPortPrototype:
        """
        Set provided and return self for chaining.

        Args:
            value: The provided to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_provided("value")
        """
        self.provided = value  # Use property setter (gets validation)
        return self



class RPortPrototype(AbstractRequiredPortPrototype):
    """
    Component port requiring a certain port interface.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components::RPortPrototype

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 68, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2047, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 237, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 460, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 202, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # If set to true, this attribute indicates that the enclosing may be left
        # unconnected and that this explicitly been considered in the.
        self._mayBe: Optional[Boolean] = None

    @property
    def may_be(self) -> Optional[Boolean]:
        """Get mayBe (Pythonic accessor)."""
        return self._mayBe

    @may_be.setter
    def may_be(self, value: Optional[Boolean]) -> None:
        """
        Set mayBe with validation.

        Args:
            value: The mayBe to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mayBe = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"mayBe must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._mayBe = value
        # isOfType.
        self._required: Optional[PortInterface] = None

    @property
    def required(self) -> Optional[PortInterface]:
        """Get required (Pythonic accessor)."""
        return self._required

    @required.setter
    def required(self, value: Optional[PortInterface]) -> None:
        """
        Set required with validation.

        Args:
            value: The required to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._required = None
            return

        if not isinstance(value, PortInterface):
            raise TypeError(
                f"required must be PortInterface or None, got {type(value).__name__}"
            )
        self._required = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMayBe(self) -> Boolean:
        """
        AUTOSAR-compliant getter for mayBe.

        Returns:
            The mayBe value

        Note:
            Delegates to may_be property (CODING_RULE_V2_00017)
        """
        return self.may_be  # Delegates to property

    def setMayBe(self, value: Boolean) -> RPortPrototype:
        """
        AUTOSAR-compliant setter for mayBe with method chaining.

        Args:
            value: The mayBe to set

        Returns:
            self for method chaining

        Note:
            Delegates to may_be property setter (gets validation automatically)
        """
        self.may_be = value  # Delegates to property setter
        return self

    def getRequired(self) -> PortInterface:
        """
        AUTOSAR-compliant getter for required.

        Returns:
            The required value

        Note:
            Delegates to required property (CODING_RULE_V2_00017)
        """
        return self.required  # Delegates to property

    def setRequired(self, value: PortInterface) -> RPortPrototype:
        """
        AUTOSAR-compliant setter for required with method chaining.

        Args:
            value: The required to set

        Returns:
            self for method chaining

        Note:
            Delegates to required property setter (gets validation automatically)
        """
        self.required = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_may_be(self, value: Optional[Boolean]) -> RPortPrototype:
        """
        Set mayBe and return self for chaining.

        Args:
            value: The mayBe to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_may_be("value")
        """
        self.may_be = value  # Use property setter (gets validation)
        return self

    def with_required(self, value: Optional[PortInterface]) -> RPortPrototype:
        """
        Set required and return self for chaining.

        Args:
            value: The required to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_required("value")
        """
        self.required = value  # Use property setter (gets validation)
        return self



class PPortPrototype(AbstractProvidedPortPrototype):
    """
    Component port providing a certain port interface.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components::PPortPrototype

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 324, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 68, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2041, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 234, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 199, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # isOfType.
        self._provided: Optional[PortInterface] = None

    @property
    def provided(self) -> Optional[PortInterface]:
        """Get provided (Pythonic accessor)."""
        return self._provided

    @provided.setter
    def provided(self, value: Optional[PortInterface]) -> None:
        """
        Set provided with validation.

        Args:
            value: The provided to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._provided = None
            return

        if not isinstance(value, PortInterface):
            raise TypeError(
                f"provided must be PortInterface or None, got {type(value).__name__}"
            )
        self._provided = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getProvided(self) -> PortInterface:
        """
        AUTOSAR-compliant getter for provided.

        Returns:
            The provided value

        Note:
            Delegates to provided property (CODING_RULE_V2_00017)
        """
        return self.provided  # Delegates to property

    def setProvided(self, value: PortInterface) -> PPortPrototype:
        """
        AUTOSAR-compliant setter for provided with method chaining.

        Args:
            value: The provided to set

        Returns:
            self for method chaining

        Note:
            Delegates to provided property setter (gets validation automatically)
        """
        self.provided = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_provided(self, value: Optional[PortInterface]) -> PPortPrototype:
        """
        Set provided and return self for chaining.

        Args:
            value: The provided to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_provided("value")
        """
        self.provided = value  # Use property setter (gets validation)
        return self



class ComplexDeviceDriverSwComponentType(AtomicSwComponentType):
    """
    The ComplexDeviceDriverSwComponentType is a special AtomicSwComponentType
    that has direct access to hardware on an ECU and which is therefore linked
    to a specific ECU or specific hardware. The
    ComplexDeviceDriverSwComponentType introduces the possibility to link from
    the software representation to its hardware description provided by the ECU
    Resource Template.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components::ComplexDeviceDriverSwComponentType

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 310, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 648, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2010, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 218, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference from the ComplexDeviceDriverSwComponent to the description of the
        # used HwElements.
        self._hardware: List["HwDescriptionEntity"] = []

    @property
    def hardware(self) -> List["HwDescriptionEntity"]:
        """Get hardware (Pythonic accessor)."""
        return self._hardware

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getHardware(self) -> List["HwDescriptionEntity"]:
        """
        AUTOSAR-compliant getter for hardware.

        Returns:
            The hardware value

        Note:
            Delegates to hardware property (CODING_RULE_V2_00017)
        """
        return self.hardware  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class EcuAbstractionSwComponentType(AtomicSwComponentType):
    """
    The ECUAbstraction is a special AtomicSwComponentType that resides between a
    software-component that wants to access ECU periphery and the
    Microcontroller Abstraction. The EcuAbstractionSw ComponentType introduces
    the possibility to link from the software representation to its hardware
    description provided by the ECU Resource Template.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components::EcuAbstractionSwComponentType

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 313, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 647, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2020, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 222, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference from the EcuAbstractionComponentType to the of the used HwElements.
        self._hardware: List["HwDescriptionEntity"] = []

    @property
    def hardware(self) -> List["HwDescriptionEntity"]:
        """Get hardware (Pythonic accessor)."""
        return self._hardware

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getHardware(self) -> List["HwDescriptionEntity"]:
        """
        AUTOSAR-compliant getter for hardware.

        Returns:
            The hardware value

        Note:
            Delegates to hardware property (CODING_RULE_V2_00017)
        """
        return self.hardware  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class ServiceSwComponentType(AtomicSwComponentType):
    """
    ServiceSwComponentType is used for configuring services for a given ECU.
    Instances of this class are only to be created in ECU Configuration phase
    for the specific purpose of the service configuration.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components::ServiceSwComponentType

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 336, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 306, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 659, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2056, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class ApplicationSwComponentType(AtomicSwComponentType):
    """
    The ApplicationSwComponentType is used to represent the application
    software.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components::ApplicationSwComponentType

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 231, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 71, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 1998, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 205, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 423, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class SensorActuatorSwComponentType(AtomicSwComponentType):
    """
    The SensorActuatorSwComponentType introduces the possibility to link from
    the software representation of a sensor/actuator to its hardware description
    provided by the ECU Resource Template.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components::SensorActuatorSwComponentType

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 646, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2055, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 244, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference from the Sensor Actuator Software Component the description of the
        # actual hardware.
        self._sensorActuator: Optional["HwDescriptionEntity"] = None

    @property
    def sensor_actuator(self) -> Optional["HwDescriptionEntity"]:
        """Get sensorActuator (Pythonic accessor)."""
        return self._sensorActuator

    @sensor_actuator.setter
    def sensor_actuator(self, value: Optional["HwDescriptionEntity"]) -> None:
        """
        Set sensorActuator with validation.

        Args:
            value: The sensorActuator to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sensorActuator = None
            return

        if not isinstance(value, HwDescriptionEntity):
            raise TypeError(
                f"sensorActuator must be HwDescriptionEntity or None, got {type(value).__name__}"
            )
        self._sensorActuator = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSensorActuator(self) -> "HwDescriptionEntity":
        """
        AUTOSAR-compliant getter for sensorActuator.

        Returns:
            The sensorActuator value

        Note:
            Delegates to sensor_actuator property (CODING_RULE_V2_00017)
        """
        return self.sensor_actuator  # Delegates to property

    def setSensorActuator(self, value: "HwDescriptionEntity") -> SensorActuatorSwComponentType:
        """
        AUTOSAR-compliant setter for sensorActuator with method chaining.

        Args:
            value: The sensorActuator to set

        Returns:
            self for method chaining

        Note:
            Delegates to sensor_actuator property setter (gets validation automatically)
        """
        self.sensor_actuator = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_sensor_actuator(self, value: Optional["HwDescriptionEntity"]) -> SensorActuatorSwComponentType:
        """
        Set sensorActuator and return self for chaining.

        Args:
            value: The sensorActuator to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sensor_actuator("value")
        """
        self.sensor_actuator = value  # Use property setter (gets validation)
        return self



class ServiceProxySwComponentType(AtomicSwComponentType):
    """
    This class provides the ability to express a software-component which
    provides access to an internal service for remote ECUs. It acts as a proxy
    for the service providing access to the service. An important use case is
    the request of vehicle mode switches: Such requests can be communicated via
    sender-receiver interfaces across ECU boundaries, but the mode manager being
    responsible to perform the mode switches is an AUTOSAR Service which is
    located in the Basic Software and is not visible in the VFB view. To handle
    this situation, a ServiceProxySwComponentType will act as proxy for the mode
    manager. It will have R-Ports to be connected with the mode requestors on
    VFB level and Service-Ports to be connected with the local mode manager at
    ECU integration time. Apart from the semantics, a
    ServiceProxySwComponentType has these specific properties: • A prototype of
    it can be mapped to more than one ECUs in the system description. • Exactly
    one additional instance of it will be created in the ECU-Extract per ECU to
    which the prototype has been mapped. • For remote communication, it can have
    only R-Ports with sender-receiver interfaces and 1:n semantics. • There
    shall be no connectors between two prototypes of any
    ServiceProxySwComponentType.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components::ServiceProxySwComponentType

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 661, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2056, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class NvBlockSwComponentType(AtomicSwComponentType):
    """
    The NvBlockSwComponentType defines non volatile data which data can be
    shared between Sw ComponentPrototypes. The non volatile data of the
    NvBlockSwComponentType are accessible via provided and required ports.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components::NvBlockSwComponentType

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 663, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2040, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This aggregation formally defines the bulk Nv Blocks that provided to the
        # application software by the enclosing atpVariation.
        self._bulkNvData: List["BulkNvDataDescriptor"] = []

    @property
    def bulk_nv_data(self) -> List["BulkNvDataDescriptor"]:
        """Get bulkNvData (Pythonic accessor)."""
        return self._bulkNvData
        # Specification of the properties of exactly one NVRAM atpVariation.
        self._nvBlock: List["NvBlockDescriptor"] = []

    @property
    def nv_block(self) -> List["NvBlockDescriptor"]:
        """Get nvBlock (Pythonic accessor)."""
        return self._nvBlock

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBulkNvData(self) -> List["BulkNvDataDescriptor"]:
        """
        AUTOSAR-compliant getter for bulkNvData.

        Returns:
            The bulkNvData value

        Note:
            Delegates to bulk_nv_data property (CODING_RULE_V2_00017)
        """
        return self.bulk_nv_data  # Delegates to property

    def getNvBlock(self) -> List["NvBlockDescriptor"]:
        """
        AUTOSAR-compliant getter for nvBlock.

        Returns:
            The nvBlock value

        Note:
            Delegates to nv_block property (CODING_RULE_V2_00017)
        """
        return self.nv_block  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====


__all__ = [
    PortPrototype,
    SwComponentType,
    PortGroup,
    SymbolProps,
    AbstractRequiredPortPrototype,
    AbstractProvidedPortPrototype,
    AtomicSwComponentType,
    ParameterSwComponentType,
    PRPortPrototype,
    RPortPrototype,
    PPortPrototype,
    ComplexDeviceDriverSwComponentType,
    EcuAbstractionSwComponentType,
    ServiceSwComponentType,
    ApplicationSwComponentType,
    SensorActuatorSwComponentType,
    ServiceProxySwComponentType,
    NvBlockSwComponentType,
]
