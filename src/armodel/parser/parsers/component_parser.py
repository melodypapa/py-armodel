"""
Parser for AUTOSAR software component elements.

Handles:
- ApplicationSwComponentType
- CompositionSwComponentType
- SensorActuatorSwComponentType
- ServiceSwComponentType
- ComplexDeviceDriverSwComponentType
- EcuAbstractionSwComponentType
- ServiceProxySwComponentType
- NvBlockSwComponentType
- SwConnector (AssemblySwConnector, DelegationSwConnector)
- SwComponentPrototype
"""
import xml.etree.ElementTree as ET

from ..base_arxml_parser import BaseARXMLParser
from ...models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR

# Import component-related model classes
from ...models.M2.AUTOSARTemplates.SWComponentTemplate.Components import (
    ApplicationSwComponentType,
    AtomicSwComponentType,
    ComplexDeviceDriverSwComponentType,
    EcuAbstractionSwComponentType,
    SensorActuatorSwComponentType,
    ServiceSwComponentType,
    SwComponentType,
)
from ...models.M2.AUTOSARTemplates.SWComponentTemplate.Composition import (
    AssemblySwConnector,
    CompositionSwComponentType,
    DelegationSwConnector,
    SwComponentPrototype,
    SwConnector,
)
from ...models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs import (
    PPortInCompositionInstanceRef,
    RPortInCompositionInstanceRef,
)
from ...models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior import (
    SwcInternalBehavior,
)


class ComponentParser(BaseARXMLParser):
    """
    Parser for AUTOSAR software component elements.

    Handles all software component types and their connectors,
    including atomic and composition components.
    """

    def __init__(self, options=None, main_parser=None):
        """Initialize ComponentParser."""
        super().__init__(options)
        self._main_parser = main_parser

    # ========================================================================
    # Software Component Types
    # ========================================================================

    def readSwComponentTypePorts(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        if self._main_parser:
            return self._main_parser._port_interface_parser.readSwComponentTypePorts(
                *args, **kwargs
            )
        else:
            self.raiseError("PortInterfaceParser not available")

    def readSwComponentTypePortGroups(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        if self._main_parser:
            return self._main_parser._port_interface_parser.readSwComponentTypePortGroups(
                *args, **kwargs
            )
        else:
            self.raiseError("PortInterfaceParser not available")

    def readSwComponentType(self, element: ET.Element, parent: SwComponentType):
        """Read software component type."""
        self.readIdentifiable(element, parent)
        self.readSwComponentTypePorts(element, parent)
        self.readSwComponentTypePortGroups(element, parent)

    def readAtomicSwComponentType(
        self, element, parent: AtomicSwComponentType
    ):
        """Read atomic software component type."""
        self.readSwComponentType(element, parent)
        self.readAtomicSwComponentTypeSwcInternalBehavior(element, parent)

    def readAtomicSwComponentTypeSwcInternalBehavior(
        self, element: ET.Element, parent: AtomicSwComponentType
    ):
        """Read SWC internal behavior for atomic component type."""
        for child_element in self.findall(element, "INTERNAL-BEHAVIORS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "SWC-INTERNAL-BEHAVIOR":
                behavior = parent.createSwcInternalBehavior(
                    self.getShortName(child_element)
                )
                # Delegate to BehaviorParser
                if self._main_parser:
                    self._main_parser._behavior_parser.readSwcInternalBehavior(
                        child_element, behavior
                    )
                else:
                    self.raiseError("BehaviorParser not available")
            else:
                self.notImplemented(
                    "Unsupported Internal Behaviors <%s>" % tag_name
                )

    def readEcuAbstractionSwComponentType(
        self, element, sw_component: EcuAbstractionSwComponentType
    ):
        """Read ECU abstraction software component type."""
        self.logger.debug(
            "Read EcuAbstractionSwComponentType <%s>"
            % sw_component.getShortName()
        )
        self.readAtomicSwComponentType(element, sw_component)

    def readApplicationSwComponentType(
        self, element: ET.Element, sw_component: ApplicationSwComponentType
    ):
        """Read application software component type."""
        self.logger.debug(
            "Read ApplicationSwComponentType <%s>" % sw_component.getShortName()
        )
        self.readAtomicSwComponentType(element, sw_component)

    def readComplexDeviceDriverSwComponentType(
        self, element: ET.Element, type: ComplexDeviceDriverSwComponentType
    ):
        """Read complex device driver software component type."""
        self.logger.debug(
            "Read ComplexDeviceDriverSwComponentType <%s>" % type.getShortName()
        )
        self.readAtomicSwComponentType(element, type)

    def readSensorActuatorSwComponentType(
        self, element: ET.Element, sw_component: SensorActuatorSwComponentType
    ):
        """Read sensor/actuator software component type."""
        self.logger.debug(
            "Read SensorActuatorSwComponentType <%s>"
            % sw_component.getShortName()
        )
        self.readAtomicSwComponentType(element, sw_component)

    def readServiceSwComponentType(
        self, element: ET.Element, sw_component: ServiceSwComponentType
    ):
        """Read service software component type."""
        self.logger.debug(
            "Read ServiceSwComponentType <%s>" % sw_component.getShortName()
        )
        self.readAtomicSwComponentType(element, sw_component)

    # ========================================================================
    # SwConnector (AssemblySwConnector, DelegationSwConnector)
    # ========================================================================

    def readPPortInCompositionInstanceRef(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        if self._main_parser:
            return self._main_parser._port_interface_parser.readPPortInCompositionInstanceRef(
                *args, **kwargs
            )
        else:
            self.raiseError("PortInterfaceParser not available")

    def readRPortInCompositionInstanceRef(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        if self._main_parser:
            return self._main_parser._port_interface_parser.readRPortInCompositionInstanceRef(
                *args, **kwargs
            )
        else:
            self.raiseError("PortInterfaceParser not available")

    def readAssemblySwConnectorProviderIRef(
        self, element: ET.Element, parent: AssemblySwConnector
    ):
        """Read assembly SW connector provider interface reference."""
        child_element = self.find(element, "PROVIDER-IREF")
        if child_element is not None:
            provide_iref = PPortInCompositionInstanceRef()
            self.readARObjectAttributes(child_element, provide_iref)
            self.readPPortInCompositionInstanceRef(child_element, provide_iref)
            parent.setProviderIRef(provide_iref)

    def readAssemblySwConnectorRequesterIRef(
        self, element: ET.Element, parent: AssemblySwConnector
    ):
        """Read assembly SW connector requester interface reference."""
        child_element = self.find(element, "REQUESTER-IREF")
        if child_element is not None:
            requester_iref = RPortInCompositionInstanceRef()
            self.readARObjectAttributes(child_element, requester_iref)
            self.readRPortInCompositionInstanceRef(child_element, requester_iref)
            parent.setRequesterIRef(requester_iref)

    def readSwConnector(self, element: ET.Element, connector: SwConnector):
        """Read software connector."""
        self.readIdentifiable(element, connector)
        connector.setMappingRef(
            self.getChildElementOptionalRefType(element, "MAPPING-REF")
        )

    def readAssemblySwConnector(
        self, element: ET.Element, connector: AssemblySwConnector
    ):
        """Read assembly SW connector."""
        self.readSwConnector(element, connector)
        self.readAssemblySwConnectorProviderIRef(element, connector)
        self.readAssemblySwConnectorRequesterIRef(element, connector)

    def readDelegationSwConnectorInnerPortIRef(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        if self._main_parser:
            return self._main_parser._port_interface_parser.readDelegationSwConnectorInnerPortIRef(
                *args, **kwargs
            )
        else:
            self.raiseError("PortInterfaceParser not available")

    def readDelegationSwConnector(
        self, element, connector: DelegationSwConnector
    ):
        """Read delegation SW connector."""
        self.readSwConnector(element, connector)
        self.readDelegationSwConnectorInnerPortIRef(element, connector)

        if (
            connector.getInnerPortIRref() is None
            and connector.getOuterPortRef() is None
        ):
            self.raiseError("Invalid PortPrototype of DELEGATION-SW-CONNECTOR")

        connector.setOuterPortRef(
            self.getChildElementOptionalRefType(element, "OUTER-PORT-REF")
        )

    def readCompositionSwComponentTypeSwConnectors(
        self, element: ET.Element, parent: CompositionSwComponentType
    ):
        """Read composition SW component type connectors."""
        for child_element in self.findall(element, "CONNECTORS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ASSEMBLY-SW-CONNECTOR":
                connector = parent.createAssemblySwConnector(
                    self.getShortName(child_element)
                )
                self.readAssemblySwConnector(child_element, connector)
            elif tag_name == "DELEGATION-SW-CONNECTOR":
                connector = parent.createDelegationSwConnector(
                    self.getShortName(child_element)
                )
                self.readDelegationSwConnector(child_element, connector)
            else:
                self.notImplemented("Unsupported SwConnector <%s>" % tag_name)

    # ========================================================================
    # SwComponentPrototype
    # ========================================================================

    def readSwComponentPrototype(
        self, element: ET.Element, prototype: SwComponentPrototype
    ):
        """Read software component prototype."""
        self.logger.debug(
            "Read SwComponentPrototypes <%s>" % prototype.getShortName()
        )
        self.readIdentifiable(element, prototype)
        prototype.setTypeTRef(
            self.getChildElementOptionalRefType(element, "TYPE-TREF")
        )

    def readCompositionSwComponentTypeComponents(
        self, element: ET.Element, parent: CompositionSwComponentType
    ):
        """Read composition SW component type components."""
        for child_element in self.findall(element, "COMPONENTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "SW-COMPONENT-PROTOTYPE":
                prototype = parent.createSwComponentPrototype(
                    self.getShortName(child_element)
                )
                self.readSwComponentPrototype(child_element, prototype)
            else:
                self.notImplemented("Unsupported Component <%s>" % tag_name)

    # ========================================================================
    # DataTypeMapping
    # ========================================================================

    def readCompositionSwComponentTypeDataTypeMappingSet(
        self, element: ET.Element, parent: CompositionSwComponentType
    ):
        """Delegate to DataTypeParser."""
        if self._main_parser:
            return self._main_parser._datatype_parser.readCompositionSwComponentTypeDataTypeMappingSet(
                element, parent
            )
        else:
            self.raiseError("DataTypeParser not available")

    # ========================================================================
    # CompositionSwComponentType
    # ========================================================================

    def readCompositionSwComponentType(
        self, element: ET.Element, type: CompositionSwComponentType
    ):
        """Read composition software component type."""
        self.logger.debug(
            "Read CompositionSwComponentType: <%s>" % type.getShortName()
        )
        self.readSwComponentType(element, type)
        self.readCompositionSwComponentTypeComponents(element, type)
        self.readCompositionSwComponentTypeSwConnectors(element, type)
        self.readCompositionSwComponentTypeDataTypeMappingSet(element, type)
        AUTOSAR.getInstance().addCompositionSwComponentType(type)
