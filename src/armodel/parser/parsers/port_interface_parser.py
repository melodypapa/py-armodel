"""
Parser for AUTOSAR port interface elements.

Handles:
- SenderReceiverInterface
- ClientServerInterface
- ModeSwitchInterface
- ParameterInterface
- DataInterface
- TriggerInterface
- Port prototypes (PPort, RPort, PRPort)
- Communication specifications
- Frame triggering
- Interface mappings
- Mode declarations
"""
from typing import List
import xml.etree.ElementTree as ET

from ..base_arxml_parser import BaseARXMLParser

# Import all required model classes
from ...models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
    ArgumentDataPrototype,
    ClientServerInterface,
    ClientServerInterfaceMapping,
    ClientServerOperation,
    ClientServerOperationMapping,
    DataInterface,
    InvalidationPolicy,
    ModeDeclarationMapping,
    ModeDeclarationMappingSet,
    ModeInterfaceMapping,
    ModeSwitchInterface,
    ParameterInterface,
    PortInterface,
    PortInterfaceMappingSet,
    SenderReceiverInterface,
    TriggerInterface,
    VariableAndParameterInterfaceMapping,
)
from ...models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
    DataPrototypeMapping,
)
from ...models.M2.AUTOSARTemplates.SWComponentTemplate.Components import (
    AbstractProvidedPortPrototype,
    AbstractRequiredPortPrototype,
    PortGroup,
    PRPortPrototype,
    PPortPrototype,
    RPortPrototype,
    SwComponentType,
)
from ...models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import (
    InnerPortGroupInCompositionInstanceRef,
    ModeGroupInAtomicSwcInstanceRef,
    PModeGroupInAtomicSwcInstanceRef,
    RModeGroupInAtomicSWCInstanceRef,
)
from ...models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import (
    ClientComSpec,
    ModeSwitchReceiverComSpec,
    ModeSwitchSenderComSpec,
    NonqueuedReceiverComSpec,
    NonqueuedSenderComSpec,
    NvProvideComSpec,
    NvRequireComSpec,
    ParameterRequireComSpec,
    PPortComSpec,
    QueuedReceiverComSpec,
    QueuedSenderComSpec,
    RPortComSpec,
    ReceiverComSpec,
    ServerComSpec,
    SenderComSpec,
    TransmissionAcknowledgementRequest,
    TransformationComSpecProps,
    UserDefinedTransformationComSpecProps,
)
from ...models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior import (
    IncludedModeDeclarationGroupSet,
    ModeAccessPoint,
    ModeSwitchPoint,
    ParameterDataPrototype,
    PortAPIOption,
    RunnableEntity,
    SwcInternalBehavior,
)
from ...models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions import (
    PortDefinedArgumentValue,
)
from ...models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents import (
    ModeSwitchedAckEvent,
    SwcModeSwitchEvent,
)
from ...models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import (
    AutosarDataPrototype,
    VariableDataPrototype,
)
from ...models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs import (
    PPortInCompositionInstanceRef,
    RPortInCompositionInstanceRef,
)
from ...models.M2.AUTOSARTemplates.SWComponentTemplate.Composition import (
    DelegationSwConnector,
)
from ...models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import (
    ModeDeclarationGroup,
    ModeDeclarationGroupPrototype,
)
from ...models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import (
    BswInternalBehavior,
    BswModuleEntity,
    BswModeSwitchEvent,
)
from ...models.M2.AUTOSARTemplates.BswModuleTemplate.BswOverview import (
    BswModuleDescription,
)
from ...models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    FrameTriggering,
    ISignalTriggering,
    PduTriggering,
)
from ...models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import (
    CanFrameTriggering,
)
from ...models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayCommunication import (
    FlexrayFrameTriggering,
)
from ...models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import (
    LinFrameTriggering,
)
from ...models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import (
    CommunicationConnector,
    CommConnectorPort,
    FramePort,
    IPduPort,
    ISignalPort,
    PhysicalChannel,
)
from ...models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    CouplingPort,
    CouplingPortDetails,
    CouplingPortFifo,
    CouplingPortScheduler,
    CouplingPortStructuralElement,
    EthernetCommunicationController,
)
from ...models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    EthernetPriorityRegeneration,
    VlanMembership,
)
from ...models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import (
    SenderReceiverToSignalGroupMapping,
    SenderReceiverToSignalMapping,
    SenderRecCompositeTypeMapping,
    SenderRecRecordElementMapping,
    SenderRecRecordTypeMapping,
)
from ...models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintDedicated.PortPrototypeBlueprint import (
    PortPrototypeBlueprint,
)


class PortInterfaceParser(BaseARXMLParser):
    """
    Parser for AUTOSAR port interface elements.

    Handles all port interface types that define communication patterns
    between software components, including:
    - Port interfaces (SenderReceiver, ClientServer, ModeSwitch, etc.)
    - Port prototypes (P-PORT, R-PORT, PR-PORT)
    - Communication specifications
    - Frame triggering
    - Interface mappings
    - Mode declarations
    """

    def __init__(self, options=None, parent_parser=None):
        """
        Initialize PortInterfaceParser.

        Args:
            options: Parser options dict
            parent_parser: The main ARXMLParser instance (for delegation)
        """
        super().__init__(options)
        self._parent_parser = parent_parser

    # Delegation methods for commonly used ARXMLParser methods
    def readIdentifiable(self, *args, **kwargs):
        """Delegate to parent parser."""
        return self._parent_parser.readIdentifiable(*args, **kwargs)

    def readARObjectAttributes(self, *args, **kwargs):
        """Delegate to parent parser."""
        return self._parent_parser.readARObjectAttributes(*args, **kwargs)

    def readARElement(self, *args, **kwargs):
        """Delegate to parent parser."""
        return self._parent_parser.readARElement(*args, **kwargs)

    def readAutosarDataPrototype(self, *args, **kwargs):
        """Delegate to parent parser."""
        return self._parent_parser.readAutosarDataPrototype(*args, **kwargs)

    def readVariableDataPrototype(self, *args, **kwargs):
        """Delegate to parent parser."""
        return self._parent_parser.readVariableDataPrototype(*args, **kwargs)

    def readArgumentDataPrototype(self, *args, **kwargs):
        """Delegate to parent parser."""
        return self._parent_parser.readArgumentDataPrototype(*args, **kwargs)

    def readRTEEvent(self, *args, **kwargs):
        """Delegate to parent parser."""
        return self._parent_parser.readRTEEvent(*args, **kwargs)

    def readRModeInAtomicSwcInstanceRef(self, *args, **kwargs):
        """Delegate to parent parser."""
        return self._parent_parser.readRModeInAtomicSwcInstanceRef(*args, **kwargs)

    def readPModeGroupInAtomicSWCInstanceRef(self, *args, **kwargs):
        """Delegate to parent parser."""
        return self._parent_parser.readPModeGroupInAtomicSWCInstanceRef(*args, **kwargs)

    def getModeGroupIRef(self, *args, **kwargs):
        """Delegate to parent parser."""
        return self._parent_parser.getModeGroupIRef(*args, **kwargs)

    def readBswScheduleEvent(self, *args, **kwargs):
        """Delegate to parent parser."""
        return self._parent_parser.readBswScheduleEvent(*args, **kwargs)

    def getVariableDataPrototypeInSystemInstanceRef(self, *args, **kwargs):
        """Delegate to parent parser."""
        return self._parent_parser.getVariableDataPrototypeInSystemInstanceRef(*args, **kwargs)

    def getChildElementRxIdentifierRange(self, *args, **kwargs):
        """Delegate to parent parser."""
        return self._parent_parser.getChildElementRxIdentifierRange(*args, **kwargs)

    def getServerComSpec(self, *args, **kwargs):
        """Delegate to parent parser."""
        return self._parent_parser.getServerComSpec(*args, **kwargs)

    def getClientComSpec(self, *args, **kwargs):
        """Delegate to parent parser."""
        return self._parent_parser.getClientComSpec(*args, **kwargs)

    def getDataPrototypeMappings(self, *args, **kwargs):
        """Delegate to parent parser."""
        return self._parent_parser.getDataPrototypeMappings(*args, **kwargs)

    def getNonqueuedSenderComSpec(self, *args, **kwargs):
        """Delegate to parent parser."""
        return self._parent_parser.getNonqueuedSenderComSpec(*args, **kwargs)

    def getSwDataDefProps(self, *args, **kwargs):
        """Delegate to parent parser."""
        return self._parent_parser.getSwDataDefProps(*args, **kwargs)

    def readTransmissionAcknowledgementRequest(self, *args, **kwargs):
        """Delegate to parent parser."""
        return self._parent_parser.readTransmissionAcknowledgementRequest(*args, **kwargs)

    def getNonqueuedReceiverComSpec(self, *args, **kwargs):
        """Delegate to parent parser."""
        return self._parent_parser.getNonqueuedReceiverComSpec(*args, **kwargs)

    def getQueuedReceiverComSpec(self, *args, **kwargs):
        """Delegate to parent parser."""
        return self._parent_parser.getQueuedReceiverComSpec(*args, **kwargs)

    def getInitValue(self, *args, **kwargs):
        """Delegate to parent parser."""
        return self._parent_parser.getInitValue(*args, **kwargs)

    def getValueSpecification(self, *args, **kwargs):
        """Delegate to parent parser."""
        return self._parent_parser.getValueSpecification(*args, **kwargs)

# readModeDeclarationGroupPrototype
    def readModeDeclarationGroupPrototype(self, element: ET.Element, prototype: ModeDeclarationGroupPrototype):
        self.readIdentifiable(element, prototype)
        prototype.setTypeTRef(self.getChildElementOptionalRefType(element, "TYPE-TREF"))


# readBswModuleDescriptionProvidedModeGroups
    def readBswModuleDescriptionProvidedModeGroups(self, element: ET.Element, parent: BswModuleDescription):
        for child_element in self.findall(element, "PROVIDED-MODE-GROUPS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "MODE-DECLARATION-GROUP-PROTOTYPE":
                mode_group = parent.createProvidedModeGroup(self.getShortName(child_element))
                self.readModeDeclarationGroupPrototype(child_element, mode_group)
            else:
                self.notImplemented("Unsupported ProvidedModeGroup <%s>" % tag_name)


# readBswModuleDescriptionRequiredModeGroups
    def readBswModuleDescriptionRequiredModeGroups(self, element: ET.Element, parent: BswModuleDescription):
        for child_element in self.findall(element, "REQUIRED-MODE-GROUPS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "MODE-DECLARATION-GROUP-PROTOTYPE":
                prototype = parent.createProvidedModeGroup(self.getShortName(child_element))
                self.readModeDeclarationGroupPrototype(child_element, prototype)
            else:
                self.notImplemented("Unsupported RequiredModeGroup <%s>" % tag_name)


# readBswModuleEntityManagedModeGroups
    def readBswModuleEntityManagedModeGroups(self, element: ET.Element, entity: BswModuleEntity):
        for child_element in self.findall(element, "MANAGED-MODE-GROUPS/MODE-DECLARATION-GROUP-PROTOTYPE-REF-CONDITIONAL"):
            ref_type = self.getChildElementOptionalRefType(child_element, "MODE-DECLARATION-GROUP-PROTOTYPE-REF")
            if ref_type is not None:
                entity.addManagedModeGroupRef(ref_type)


# readBswModeSwitchEvent
    def readBswModeSwitchEvent(self, element: ET.Element, event: BswModeSwitchEvent):
        # self.logger.debug("Read BswModeSwitchEvent <%s>" % event.getShortName())
        # Read the Inherit BswScheduleEvent
        self.readBswScheduleEvent(element, event)


# readModeAccessPoint
    def readModeAccessPoint(self, element: ET.Element, point: ModeAccessPoint):
        self.readARObjectAttributes(element, point)
        point.setModeGroupIRef(self.getModeGroupIRef(element, "MODE-GROUP-IREF"))


# readRunnableEntityModeAccessPoints
    def readRunnableEntityModeAccessPoints(self, element: ET.Element, entity: RunnableEntity):
        for child_element in self.findall(element, "MODE-ACCESS-POINTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "MODE-ACCESS-POINT":
                point = ModeAccessPoint()
                self.readModeAccessPoint(child_element, point)
                entity.addModeAccessPoint(point)
            else:
                self.notImplemented("Unsupported Mode Access Point <%s>" % tag_name)


# readModeSwitchPointModeGroupIRef
    def readModeSwitchPointModeGroupIRef(self, element: ET.Element, point: ModeSwitchPoint):
        child_element = self.find(element, "MODE-GROUP-IREF")
        if child_element is not None:
            instance_ref = PModeGroupInAtomicSwcInstanceRef()
            self.readPModeGroupInAtomicSWCInstanceRef(child_element, instance_ref)
            point.setModeGroupIRef(instance_ref)


# readModeSwitchPoint
    def readModeSwitchPoint(self, element: ET.Element, point: ModeSwitchPoint):
        self.readARObjectAttributes(element, point)
        self.readModeSwitchPointModeGroupIRef(element, point)
    

# readRunnableEntityModeSwitchPoints
    def readRunnableEntityModeSwitchPoints(self, element: ET.Element, parent: RunnableEntity):
        for child_element in self.findall(element, "MODE-SWITCH-POINTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "MODE-SWITCH-POINT":
                point = parent.createModeSwitchPoint(self.getShortName(child_element))
                self.readModeSwitchPoint(child_element, point)
            else:
                self.notImplemented("Unsupported Mode Switch Point <%s>" % tag_name)


# readSwcModeSwitchEvent
    def readSwcModeSwitchEvent(self, element: ET.Element, event: SwcModeSwitchEvent):
        # self.logger.debug("Read SwcModeSwitchEvent <%s>" % event.getShortName())
        self.readRTEEvent(element, event)
        event.setActivation(self.getChildElementOptionalLiteral(element, "ACTIVATION"))
        self.readRModeInAtomicSwcInstanceRef(element, event)


# readModeSwitchedAckEvent
    def readModeSwitchedAckEvent(self, element, event: ModeSwitchedAckEvent):
        # self.logger.debug("Read ModeSwitchedAckEvent <%s>" % event.getShortName())
        self.readRTEEvent(element, event)
        event.setEventSourceRef(self.getChildElementOptionalRefType(element, "EVENT-SOURCE-REF"))


# readParameterDataPrototype
    def readParameterDataPrototype(self, element: ET.Element, prototype: ParameterDataPrototype):
        self.readAutosarDataPrototype(element, prototype)
        prototype.setInitValue(self.getInitValue(element))


# readPortDefinedArgumentValue
    def readPortDefinedArgumentValue(self, element: ET.Element) -> PortDefinedArgumentValue:
        argument_value = PortDefinedArgumentValue()
        child_element = self.find(element, "VALUE/*")
        if child_element is not None:
            argument_value.setValue(self.getValueSpecification(child_element, self.getTagName(child_element)))
        argument_value.setValueTypeTRef(self.getChildElementOptionalRefType(element, "VALUE-TYPE-TREF"))
        return argument_value


# readSwcInternalBehaviorPerInstanceParameters
    def readSwcInternalBehaviorPerInstanceParameters(self, element: ET.Element, behavior: SwcInternalBehavior):
        for child_element in self.findall(element, "PER-INSTANCE-PARAMETERS/PARAMETER-DATA-PROTOTYPE"):
            short_name = self.getShortName(child_element)
            prototype = behavior.createPerInstanceParameter(short_name)
            self.readParameterDataPrototype(child_element, prototype)


# readIncludedModeDeclarationGroupSet
    def readIncludedModeDeclarationGroupSet(self, element: ET.Element, group_set: IncludedModeDeclarationGroupSet):
        for ref in self.getChildElementRefTypeList(element, "MODE-DECLARATION-GROUP-REFS/MODE-DECLARATION-GROUP-REF"):
            group_set.addModeDeclarationGroupRef(ref)
        group_set.setPrefix(self.getChildElementOptionalLiteral(element, "PREFIX"))


# readSwcInternalBehaviorIncludedModeDeclarationGroupSets
    def readSwcInternalBehaviorIncludedModeDeclarationGroupSets(self, element: ET.Element, behavior: SwcInternalBehavior):
        for child_element in self.findall(element, "INCLUDED-MODE-DECLARATION-GROUP-SETS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "INCLUDED-MODE-DECLARATION-GROUP-SET":
                group_set = IncludedModeDeclarationGroupSet()
                self.readIncludedModeDeclarationGroupSet(child_element, group_set)
                behavior.addIncludedModeDeclarationGroupSet(group_set)
            else:
                self.notImplemented("Unsupported IncludedModeDeclarationGroupSet <%s>" % tag_name)


# readSenderReceiverInterfaceDataElements
    def readSenderReceiverInterfaceDataElements(self, element: ET.Element, sr_interface: SenderReceiverInterface):
        for child_element in self.findall(element, "DATA-ELEMENTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "VARIABLE-DATA-PROTOTYPE":
                prototype = sr_interface.createDataElement(self.getShortName(child_element))
                self.readVariableDataPrototype(child_element, prototype)
                # prototype.swDataDefProps = self.getSwDataDefProps(child_element, "SW-DATA-DEF-PROPS")
                # self.readAutosarDataPrototype(child_element, prototype)
            else:
                self.notImplemented("Unsupported Data Element <%s>" % tag_name)


# readSenderReceiverInterfaceInvalidationPolicies
    def readSenderReceiverInterfaceInvalidationPolicies(self, element: ET.Element, sr_interface: SenderReceiverInterface):
        for child_element in self.findall(element, "INVALIDATION-POLICYS/INVALIDATION-POLICY"):
            policy = InvalidationPolicy()
            policy.setDataElementRef(self.getChildElementOptionalRefType(child_element, "DATA-ELEMENT-REF")) \
                  .setHandleInvalid(self.getChildElementOptionalLiteral(child_element, "HANDLE-INVALID"))
            sr_interface.addInvalidationPolicy(policy)


# readInvalidationPolicys
    def readInvalidationPolicys(self, element: ET.Element, parent: SenderReceiverInterface):
        for child_element in self.findall(element, "INVALIDATION-POLICYS/INVALIDATION-POLICY"):
            # short_name = self.getShortName(child_element)
            policy = parent.createInvalidationPolicy()
            self.readIdentifiable(child_element, policy)
            policy.data_element_ref = self.getChildElementOptionalRefType(child_element, "DATA-ELEMENT-REF")
            policy.handle_invalid = self.getChildElementOptionalLiteral(child_element, "HANDLE-INVALID")


# readSenderReceiverInterface
    def readSenderReceiverInterface(self, element, sr_interface: SenderReceiverInterface):
        self.logger.debug("Read SenderReceiverInterface <%s>" % sr_interface.getShortName())
        self.readIdentifiable(element, sr_interface)
        sr_interface.setIsService(self.getChildElementOptionalBooleanValue(element, "IS-SERVICE"))
        self.readSenderReceiverInterfaceDataElements(element, sr_interface)
        self.readSenderReceiverInterfaceInvalidationPolicies(element, sr_interface)


# readClientServerOperationArguments
    def readClientServerOperationArguments(self, element: ET.Element, operation: ClientServerOperation):
        for child_element in self.findall(element, "ARGUMENTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ARGUMENT-DATA-PROTOTYPE":
                prototype = operation.createArgumentDataPrototype(self.getShortName(child_element))
                self.readArgumentDataPrototype(child_element, prototype)
            else:
                self.notImplemented("Unsupported Argument <%s>" % tag_name)


# readPossibleErrorRefs
    def readPossibleErrorRefs(self, element: ET.Element, parent: ClientServerOperation):
        child_element = self.find(element, "POSSIBLE-ERROR-REFS")
        if child_element is not None:
            for ref in self.getChildElementRefTypeList(child_element, "POSSIBLE-ERROR-REF"):
                parent.addPossibleErrorRef(ref)


# readClientServerOperation
    def readClientServerOperation(self, element: ET.Element, operation: ClientServerOperation):
        self.readIdentifiable(element, operation)
        self.readClientServerOperationArguments(element, operation)
        self.readPossibleErrorRefs(element, operation)


# readClientServerInterfaceOperations
    def readClientServerInterfaceOperations(self, element: ET.Element, parent: ClientServerInterface):
        for child_element in self.findall(element, "OPERATIONS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "CLIENT-SERVER-OPERATION":
                operation = parent.createOperation(self.getShortName(child_element))
                self.readClientServerOperation(child_element, operation)
            else:
                self.notImplemented("Unsupported Operation <%s>" % tag_name)


# readPossibleErrors
    def readPossibleErrors(self, element: ET.Element, parent: ClientServerInterface):
        for child_element in self.findall(element, "POSSIBLE-ERRORS/APPLICATION-ERROR"):
            short_name = self.getShortName(child_element)
            error = parent.createApplicationError(short_name)
            self.readIdentifiable(child_element, error)  # some errors has its uuid
            error.error_code = self.getChildElementOptionalNumericalValue(child_element, "ERROR-CODE")


# readPortInterface
    def readPortInterface(self, element: ET.Element, port_interface: PortInterface):
        self.readIdentifiable(element, port_interface)
        port_interface.setIsService(self.getChildElementOptionalBooleanValue(element, "IS-SERVICE"))\
                      .setServiceKind(self.getChildElementOptionalLiteral(element, "SERVICE-KIND"))


# readParameterInterfaceParameters
    def readParameterInterfaceParameters(self, element: ET.Element, param_interface: ParameterInterface):
        for child_element in self.findall(element, "PARAMETERS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "PARAMETER-DATA-PROTOTYPE":
                prototype = param_interface.createParameterDataPrototype(self.getShortName(child_element))
                self.readParameterDataPrototype(child_element, prototype)
            else:
                self.notImplemented("Unsupported Parameter <%s>" % tag_name)


# readDataInterface
    def readDataInterface(self, element: ET.Element, interface: DataInterface):
        self.readPortInterface(element, interface)
    

# readParameterInterface
    def readParameterInterface(self, element: ET.Element, interface: ParameterInterface):
        self.logger.debug("Read ParameterInterface <%s>" % interface.getShortName())
        self.readDataInterface(element, interface)
        self.readParameterInterfaceParameters(element, interface)


# readClientServerInterface
    def readClientServerInterface(self, element: ET.Element, cs_interface: ClientServerInterface):
        self.logger.debug("Read ClientServerInterface <%s>" % cs_interface.getShortName())
        self.readPortInterface(element, cs_interface)
        self.readClientServerInterfaceOperations(element, cs_interface)
        self.readPossibleErrors(element, cs_interface)


# readTriggerInterface
    def readTriggerInterface(self, element: ET.Element, trigger_if: TriggerInterface):
        self.logger.debug("Read TriggerInterface <%s>" % trigger_if.getShortName())
        self.readIdentifiable(element, trigger_if)


# readModeDeclarationGroupModeDeclaration
    def readModeDeclarationGroupModeDeclaration(self, element: ET.Element, parent: ModeDeclarationGroup):
        for child_element in self.findall(element, "MODE-DECLARATIONS/MODE-DECLARATION"):
            short_name = self.getShortName(child_element)
            declaration = parent.createModeDeclaration(short_name)
            self.readARObjectAttributes(child_element, declaration)
            declaration.setValue(self.getChildElementOptionalNumericalValue(child_element, "VALUE"))


# readModeSwitchInterfaceModeGroup
    def readModeSwitchInterfaceModeGroup(self, element: ET.Element, parent: ModeSwitchInterface):
        child_element = self.find(element, "MODE-GROUP")
        if child_element is not None:
            short_name = self.getShortName(child_element)
            mode_group = parent.createModeGroup(short_name)
            self.readIdentifiable(child_element, mode_group)
            mode_group.type_tref = self.getChildElementOptionalRefType(child_element, "TYPE-TREF")


# readModeDeclarationGroup
    def readModeDeclarationGroup(self, element: ET.Element, group: ModeDeclarationGroup):
        self.logger.debug("Read ModeDeclarationGroup <%s>" % group.getShortName())
        self.readIdentifiable(element, group)
        self.readModeDeclarationGroupModeDeclaration(element, group)
        group.setInitialModeRef(self.getChildElementOptionalRefType(element, "INITIAL-MODE-REF"))
        group.setOnTransitionValue(self.getChildElementOptionalNumericalValue(element, "ON-TRANSITION-VALUE"))


# readModeSwitchInterface
    def readModeSwitchInterface(self, element: ET.Element, mode_interface: ModeSwitchInterface):
        self.logger.debug("Read ModeSwitchInterface <%s>" % mode_interface.getShortName())
        self.readPortInterface(element, mode_interface)
        self.readModeSwitchInterfaceModeGroup(element, mode_interface)


# readAbstractRequiredPortPrototype
    def readAbstractRequiredPortPrototype(self, element: ET.Element, prototype: AbstractRequiredPortPrototype):
        self.readProvidedComSpec(element, prototype)


# readAbstractProvidedPortPrototype
    def readAbstractProvidedPortPrototype(self, element: ET.Element, prototype: AbstractProvidedPortPrototype):
        self.readRequiredComSpec(element, prototype)


# readPPortPrototype
    def readPPortPrototype(self, element: ET.Element, prototype: PPortPrototype):
        # self.logger.debug("Read PPortPrototype %s" % prototype.getShortName())
        self.readIdentifiable(element, prototype)
        self.readAbstractRequiredPortPrototype(element, prototype)
        prototype.setProvidedInterfaceTRef(self.getChildElementOptionalRefType(element, "PROVIDED-INTERFACE-TREF"))
        

# readRPortPrototype
    def readRPortPrototype(self, element: ET.Element, prototype: RPortPrototype):
        # self.logger.debug("Read RPortPrototype %s" % prototype.getShortName())
        self.readIdentifiable(element, prototype)
        self.readAbstractProvidedPortPrototype(element, prototype)
        prototype.setRequiredInterfaceTRef(self.getChildElementOptionalRefType(element, "REQUIRED-INTERFACE-TREF"))


# readPRPortPrototype
    def readPRPortPrototype(self, element: ET.Element, prototype: PRPortPrototype):
        # self.logger.debug("Read PRPortPrototype %s" % prototype.getShortName())
        self.readIdentifiable(element, prototype)
        self.readAbstractRequiredPortPrototype(element, prototype)
        self.readAbstractProvidedPortPrototype(element, prototype)
        prototype.setProvidedRequiredInterface(self.getChildElementOptionalRefType(element, "PROVIDED-REQUIRED-INTERFACE-TREF"))


# readSwComponentTypePorts
    def readSwComponentTypePorts(self, element: ET.Element, sw_component: SwComponentType):
        for child_element in self.findall(element, "PORTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "P-PORT-PROTOTYPE":
                prototype = sw_component.createPPortPrototype(self.getShortName(child_element))
                self.readPPortPrototype(child_element, prototype)
            elif tag_name == "R-PORT-PROTOTYPE":
                prototype = sw_component.createRPortPrototype(self.getShortName(child_element))
                self.readRPortPrototype(child_element, prototype)
            elif tag_name == "PR-PORT-PROTOTYPE":
                prototype = sw_component.createPRPortPrototype(self.getShortName(child_element))
                self.readPRPortPrototype(child_element, prototype)
            else:
                self.notImplemented("Unsupported Port Prototype <%s>" % tag_name)


# readSenderComSpec
    def readSenderComSpec(self, element: ET.Element, com_spec: SenderComSpec):
        self.readARObjectAttributes(element, com_spec)
        for child_element in self.findall(element, "COMPOSITE-NETWORK-REPRESENTATIONS/COMPOSITE-NETWORK-REPRESENTATION"):
            com_spec.addCompositeNetworkRepresentation(self.getCompositeNetworkRepresentation(child_element))
        com_spec.setDataElementRef(self.getChildElementOptionalRefType(element, "DATA-ELEMENT-REF"))
        com_spec.setNetworkRepresentation(self.getSwDataDefProps(element, "NETWORK-REPRESENTATION"))
        com_spec.setHandleOutOfRange(self.getChildElementOptionalLiteral(element, "HANDLE-OUT-OF-RANGE"))
        com_spec.setTransmissionAcknowledge(self.readTransmissionAcknowledgementRequest(element))
        com_spec.setUsesEndToEndProtection(self.getChildElementOptionalBooleanValue(element, "USES-END-TO-END-PROTECTION"))


# readServerComSpecTransformationComSpecProps
    def readServerComSpecTransformationComSpecProps(self, element: ET.Element, com_spec: ServerComSpec):
        for child_element in self.findall(element, "TRANSFORMATION-COM-SPEC-PROPSS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "USER-DEFINED-TRANSFORMATION-COM-SPEC-PROPS":
                props = UserDefinedTransformationComSpecProps()
                self.readUserDefinedTransformationComSpecProps(child_element, props)
                com_spec.addTransformationComSpecProps(props)
            else:
                self.notImplemented("Unsupported TransformationComSpecProps <%s>" % tag_name)
    

# readPPortComSpec
    def readPPortComSpec(self, element: ET.Element, com_spec: PPortComSpec):
        self.readARObjectAttributes(element, com_spec)


# readProvidedComSpec
    def readProvidedComSpec(self, element: ET.Element, parent: PPortPrototype):
        for child_element in self.findall(element, "PROVIDED-COM-SPECS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "NONQUEUED-SENDER-COM-SPEC":
                parent.addProvidedComSpec(self.getNonqueuedSenderComSpec(child_element))
            elif tag_name == "SERVER-COM-SPEC":
                parent.addProvidedComSpec(self.getServerComSpec(child_element))
            elif tag_name == "QUEUED-SENDER-COM-SPEC":
                parent.addProvidedComSpec(self.getQueuedSenderComSpec(child_element))
            elif tag_name == "MODE-SWITCH-SENDER-COM-SPEC":
                parent.addProvidedComSpec(self.getModeSwitchSenderComSpec(child_element))
            elif tag_name == "NV-PROVIDE-COM-SPEC":
                parent.addProvidedComSpec(self.getNvProvideComSpec(child_element))
            else:
                self.raiseError("Unsupported RequiredComSpec <%s>" % tag_name)


# readRPortComSpec
    def readRPortComSpec(self, element: ET.Element, com_spec: RPortComSpec):
        self.readARObjectAttributes(element, com_spec)


# readRequiredComSpec
    def readRequiredComSpec(self, element: ET.Element, parent: RPortPrototype):
        for child_element in self.findall(element, "REQUIRED-COM-SPECS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "NONQUEUED-RECEIVER-COM-SPEC":
                parent.addRequiredComSpec(self.getNonqueuedReceiverComSpec(child_element))
            elif tag_name == "CLIENT-COM-SPEC":
                parent.addRequiredComSpec(self.getClientComSpec(child_element))
            elif tag_name == "QUEUED-RECEIVER-COM-SPEC":
                parent.addRequiredComSpec(self.getQueuedReceiverComSpec(child_element))
            elif tag_name == "MODE-SWITCH-RECEIVER-COM-SPEC":
                parent.addRequiredComSpec(self.getModeSwitchReceiverComSpec(child_element))
            elif tag_name == "PARAMETER-REQUIRE-COM-SPEC":
                parent.addRequiredComSpec(self.getParameterRequireComSpec(child_element))
            elif tag_name == "NV-REQUIRE-COM-SPEC":
                parent.addRequiredComSpec(self.getNvRequireComSpec(child_element))
            else:
                self.raiseError("Unsupported RequiredComSpec <%s>" % tag_name)


# readPortGroupInnerGroupIRefs
    def readPortGroupInnerGroupIRefs(self, element: ET.Element, parent: PortGroup):
        for child_element in self.findall(element, "INNER-GROUP-IREFS/INNER-GROUP-IREF"):
            inner_group_iref = InnerPortGroupInCompositionInstanceRef()
            # inner_group_iref.contextRef = self.getChildElementOptionalRefType(child_element, "CONTEXT-REF")
            inner_group_iref.setTargetRef(self.getChildElementOptionalRefType(child_element, "TARGET-REF"))
            parent.addInnerGroupIRef(inner_group_iref)


# readPortGroupOuterPortRefs
    def readPortGroupOuterPortRefs(self, element: ET.Element, parent: PortGroup):
        for child_element in self.findall(element, "OUTER-PORTS/PORT-PROTOTYPE-REF-CONDITIONAL"):
            parent.addOuterPortRef(self.getChildElementOptionalRefType(child_element, "PORT-PROTOTYPE-REF"))


# readPortGroup
    def readPortGroup(self, element: ET.Element, parent: SwComponentType):
        short_name = self.getShortName(element)
        self.logger.debug("readPortGroup %s" % short_name)
        port_group = parent.createPortGroup(short_name)
        self.readIdentifiable(element, port_group)
        self.readPortGroupInnerGroupIRefs(element, port_group)
        self.readPortGroupOuterPortRefs(element, port_group)


# readSwComponentTypePortGroups
    def readSwComponentTypePortGroups(self, element: ET.Element, parent: SwComponentType):
        for child_element in self.findall(element, "PORT-GROUPS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "PORT-GROUP":
                self.readPortGroup(child_element, parent)
            else:
                self.raiseError("Unsupported Port Group type: %s" % tag_name)


# readPPortInCompositionInstanceRef
    def readPPortInCompositionInstanceRef(self, element: ET.Element, p_port_in_composition_instance_ref: PPortInCompositionInstanceRef):
        p_port_in_composition_instance_ref.setContextComponentRef(self.getChildElementOptionalRefType(element, "CONTEXT-COMPONENT-REF")) \
                                          .setTargetPPortRef(self.getChildElementOptionalRefType(element, "TARGET-P-PORT-REF"))
        
        
        '''
        self.logger.debug("PPortInCompositionInstanceRef")
        self.logger.debug("  CONTEXT-COMPONENT-REF DEST: %s, %s"
                          % (p_port_in_composition_instance_ref.getContextComponentRef().getDest(),
                             p_port_in_composition_instance_ref.getContextComponentRef().getValue()))
        self.logger.debug("  TARGET-P-PORT-REF DEST: %s, %s"
                          % (p_port_in_composition_instance_ref.getTargetPPortRef().getDest(),
                             p_port_in_composition_instance_ref.getTargetPPortRef().getValue()))
        '''


# readRPortInCompositionInstanceRef
    def readRPortInCompositionInstanceRef(self, element, r_port_in_composition_instance_ref: RPortInCompositionInstanceRef):
        r_port_in_composition_instance_ref.setContextComponentRef(self.getChildElementOptionalRefType(element, "CONTEXT-COMPONENT-REF")) \
                                          .setTargetRPortRef(self.getChildElementOptionalRefType(element, "TARGET-R-PORT-REF"))


        '''
        self.logger.debug("RPortInCompositionInstanceRef")
        self.logger.debug("  CONTEXT-COMPONENT-REF DEST: %s, %s"
                          % (r_port_in_composition_instance_ref.getContextComponentRef().getDest(),
                             r_port_in_composition_instance_ref.getContextComponentRef().getValue()))
        self.logger.debug("  TARGET-P-PORT-REF DEST: %s, %s"
                          % (r_port_in_composition_instance_ref.getTargetRPortRef().getDest(),
                             r_port_in_composition_instance_ref.getTargetRPortRef().getValue()))
        '''


# readDelegationSwConnectorInnerPortIRef
    def readDelegationSwConnectorInnerPortIRef(self, element, parent: DelegationSwConnector):
        inner_port_iref_element = self.find(element, "INNER-PORT-IREF")
        if (inner_port_iref_element is not None):
            child_element = self.find(inner_port_iref_element, "R-PORT-IN-COMPOSITION-INSTANCE-REF")
            if (child_element is not None):
                r_port_in_composition_instance_ref = RPortInCompositionInstanceRef()
                self.readRPortInCompositionInstanceRef(child_element, r_port_in_composition_instance_ref)
                parent.setInnerPortIRref(r_port_in_composition_instance_ref)
                return
            
            
            child_element = self.find(inner_port_iref_element, "P-PORT-IN-COMPOSITION-INSTANCE-REF")
            if (child_element is not None):
                p_port_in_composition_instance_ref = PPortInCompositionInstanceRef()
                self.readPPortInCompositionInstanceRef(child_element, p_port_in_composition_instance_ref)
                parent.setInnerPortIRref(p_port_in_composition_instance_ref)
                return
            
            
            self.raiseError("Unsupported child element of INNER-PORT-IREF")


# readModeDeclarationMappingFirstModeRefs
    def readModeDeclarationMappingFirstModeRefs(self, element: ET.Element, mapping: ModeDeclarationMapping):
        for ref_link in self.getChildElementRefTypeList(element, "FIRST-MODE-REFS/FIRST-MODE-REF"):
            mapping.addFirstModeRef(ref_link)


# readModeDeclarationMapping
    def readModeDeclarationMapping(self, element: ET.Element, mapping: ModeDeclarationMapping):
        # self.logger.debug("Read ModeDeclarationMapping <%s>" % mapping.getShortName())
        self.readIdentifiable(element, mapping)
        self.readModeDeclarationMappingFirstModeRefs(element, mapping)
        mapping.setSecondModeRef(self.getChildElementOptionalRefType(element, "SECOND-MODE-REF"))


# readModeDeclarationMappingSetModeDeclarationMappings
    def readModeDeclarationMappingSetModeDeclarationMappings(self, element: ET.Element, mapping_set: ModeDeclarationMappingSet):
        for child_element in self.findall(element, "MODE-DECLARATION-MAPPINGS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "MODE-DECLARATION-MAPPING":
                mapping = mapping_set.createModeDeclarationMapping(self.getShortName(child_element))
                self.readModeDeclarationMapping(child_element, mapping)
            else:
                self.notImplemented("Unsupported ModeDeclarationMapping <%s>" % tag_name)


# readModeDeclarationMappingSet
    def readModeDeclarationMappingSet(self, element: ET.Element, mapping_set: ModeDeclarationMappingSet):
        self.logger.debug("Read ModeDeclarationMappingSet <%s>" % mapping_set.getShortName())
        self.readARElement(element, mapping_set)
        self.readModeDeclarationMappingSetModeDeclarationMappings(element, mapping_set)


# readClientServerOperationMapping
    def readClientServerOperationMapping(self, element: ET.Element, mapping: ClientServerOperationMapping):
        mapping.setFirstOperationRef(self.getChildElementOptionalRefType(element, "FIRST-OPERATION-REF")) \
               .setSecondOperationRef(self.getChildElementOptionalRefType(element, "SECOND-OPERATION-REF"))


# readClientServerInterfaceMappingOperationMappings
    def readClientServerInterfaceMappingOperationMappings(self, element: ET.Element, mapping: ClientServerInterfaceMapping):
        for child_element in self.findall(element, "OPERATION-MAPPINGS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "CLIENT-SERVER-OPERATION-MAPPING":
                operation_mapping = ClientServerOperationMapping()
                self.readClientServerOperationMapping(child_element, operation_mapping)
                mapping.addOperationMapping(operation_mapping)
            else:
                self.notImplemented("Unsupported Operation Mapping <%s>" % tag_name)


# readClientServerInterfaceMapping
    def readClientServerInterfaceMapping(self, element: ET.Element, mapping: ClientServerInterfaceMapping):
        # self.logger.debug("Read ClientServerInterfaceMapping %s" % mapping.getShortName())
        self.readIdentifiable(element, mapping)
        self.readClientServerInterfaceMappingOperationMappings(element, mapping)


# readVariableAndParameterInterfaceMapping
    def readVariableAndParameterInterfaceMapping(self, element: ET.Element, mapping: VariableAndParameterInterfaceMapping):
        # self.logger.debug("Read VariableAndParameterInterfaceMapping %s" % mapping.getShortName())
        self.readIdentifiable(element, mapping)
        for item in self.getDataPrototypeMappings(element, "DATA-MAPPINGS"):
            mapping.addDataMapping(item)


# readModeInterfaceMappingModeMapping
    def readModeInterfaceMappingModeMapping(self, element: ET.Element, mapping: ModeInterfaceMapping):
        child_element = self.find(element, "MODE-MAPPING")
        if child_element is not None:
            mode_mapping = ModeDeclarationGroupPrototypeMapping()
            mode_mapping.setFirstModeGroupRef(self.getChildElementOptionalRefType(child_element, "FIRST-MODE-GROUP-REF")) \
                        .setModeDeclarationMappingSetRef(self.getChildElementOptionalRefType(child_element, "MODE-DECLARATION-MAPPING-SET-REF")) \
                        .setSecondModeGroupRef(self.getChildElementOptionalRefType(child_element, "SECOND-MODE-GROUP-REF"))
            mapping.setModeMapping(mode_mapping)


# readModeInterfaceMapping
    def readModeInterfaceMapping(self, element: ET.Element, mapping: ModeInterfaceMapping):
        # self.logger.debug("Read ModeInterfaceMapping %s" % mapping.getShortName())
        self.readIdentifiable(element, mapping)
        self.readModeInterfaceMappingModeMapping(element, mapping)


# readPortInterfaceMappings
    def readPortInterfaceMappings(self, element: ET.Element, mapping_set: PortInterfaceMappingSet):
        for child_element in self.findall(element, "PORT-INTERFACE-MAPPINGS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "VARIABLE-AND-PARAMETER-INTERFACE-MAPPING":
                mapping = mapping_set.createVariableAndParameterInterfaceMapping(self.getShortName(child_element))
                self.readVariableAndParameterInterfaceMapping(child_element, mapping)
            elif tag_name == "CLIENT-SERVER-INTERFACE-MAPPING":
                mapping = mapping_set.createClientServerInterfaceMapping(self.getShortName(child_element))
                self.readClientServerInterfaceMapping(child_element, mapping)
            elif tag_name == "MODE-INTERFACE-MAPPING":
                mapping = mapping_set.createModeInterfaceMapping(self.getShortName(child_element))
                self.readModeInterfaceMapping(child_element, mapping)
            else:
                self.notImplemented("Unsupported PortInterfaceMapping <%s>" % tag_name)


# readPortInterfaceMappingSet
    def readPortInterfaceMappingSet(self, element: ET.Element, mapping_set: PortInterfaceMappingSet):
        self.logger.debug("Read PortInterfaceMappingSet %s" % mapping_set.getShortName())
        self.readIdentifiable(element, mapping_set)
        self.readPortInterfaceMappings(element, mapping_set)


# readSenderReceiverToSignalMapping
    def readSenderReceiverToSignalMapping(self, element: ET.Element, mapping: SenderReceiverToSignalMapping):
        mapping.setCommunicationDirection(self.getChildElementOptionalLiteral(element, "COMMUNICATION-DIRECTION"))
        mapping.setDataElementIRef(self.getVariableDataPrototypeInSystemInstanceRef(self.find(element, "DATA-ELEMENT-IREF")))
        mapping.setSystemSignalRef(self.getChildElementOptionalRefType(element, "SYSTEM-SIGNAL-REF"))
        self.logger.debug("Read SenderReceiverToSignalMapping <%s>" % mapping.getSystemSignalRef().getValue())
    

# readSenderRecRecordElementMapping
    def readSenderRecRecordElementMapping(self, element: ET.Element, mapping: SenderRecRecordElementMapping):
        self.readARObjectAttributes(element, mapping)
        mapping.setApplicationRecordElementRef(self.getChildElementOptionalRefType(element, "APPLICATION-RECORD-ELEMENT-REF"))
        mapping.setImplementationRecordElementRef(self.getChildElementOptionalRefType(element, "IMPLEMENTATION-RECORD-ELEMENT-REF"))
        mapping.setSystemSignalRef(self.getChildElementOptionalRefType(element, "SYSTEM-SIGNAL-REF"))


# readSenderRecArrayTypeMappingRecordElementMapping
    def readSenderRecArrayTypeMappingRecordElementMapping(self, element: ET.Element, mapping: SenderRecRecordTypeMapping):
        for child_element in self.findall(element, "RECORD-ELEMENT-MAPPINGS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "SENDER-REC-RECORD-ELEMENT-MAPPING":
                record_element_mapping = SenderRecRecordElementMapping()
                self.readSenderRecRecordElementMapping(child_element, record_element_mapping)
                mapping.addRecordElementMapping(record_element_mapping)
            else:
                self.notImplemented("Unsupported RecordElementMapping %s" % tag_name)
    

# readSenderRecRecordTypeMapping
    def readSenderRecRecordTypeMapping(self, element: ET.Element, mapping: SenderRecRecordTypeMapping):
        self.readSenderRecCompositeTypeMapping(element, mapping)
        self.readSenderRecArrayTypeMappingRecordElementMapping(element, mapping)
    

# readSenderReceiverToSignalGroupMappingTypeMapping
    def readSenderReceiverToSignalGroupMappingTypeMapping(self, element: ET.Element, mapping: SenderReceiverToSignalGroupMapping):
        child_element = self.find(element, "TYPE-MAPPING/*")
        if child_element is not None:
            tag_name = self.getTagName(child_element)
            if tag_name == "SENDER-REC-RECORD-TYPE-MAPPING":
                type_mapping = SenderRecRecordTypeMapping()
                self.readSenderRecRecordTypeMapping(child_element, type_mapping)
                mapping.setTypeMapping(type_mapping)
            else:
                self.notImplemented("Unsupported Type Mapping %s" % tag_name)


# readSenderReceiverToSignalGroupMapping
    def readSenderReceiverToSignalGroupMapping(self, element: ET.Element, mapping: SenderReceiverToSignalGroupMapping):
        mapping.setDataElementIRef(self.getVariableDataPrototypeInSystemInstanceRef(self.find(element, "DATA-ELEMENT-IREF")))
        mapping.setSignalGroupRef(self.getChildElementOptionalRefType(element, "SIGNAL-GROUP-REF"))
        self.readSenderReceiverToSignalGroupMappingTypeMapping(element, mapping)


# readFrameTriggering
    def readFrameTriggering(self, element: ET.Element, triggering: FrameTriggering):
        self.readIdentifiable(element, triggering)
        for ref in self.getChildElementRefTypeList(element, 'FRAME-PORT-REFS/FRAME-PORT-REF'):
            triggering.addFramePortRef(ref)
        triggering.setFrameRef(self.getChildElementOptionalRefType(element, "FRAME-REF"))
        for child_element in self.findall(element, 'PDU-TRIGGERINGS/PDU-TRIGGERING-REF-CONDITIONAL'):
            triggering.addPduTriggeringRef(self.getChildElementOptionalRefType(child_element, "PDU-TRIGGERING-REF"))


# readCanFrameTriggering
    def readCanFrameTriggering(self, element: ET.Element, triggering: CanFrameTriggering):
        self.logger.debug("Read CanFrameTriggering %s" % triggering.getShortName())
        self.readFrameTriggering(element, triggering)
        triggering.setCanAddressingMode(self.getChildElementOptionalLiteral(element, "CAN-ADDRESSING-MODE")) \
                  .setCanFdFrameSupport(self.getChildElementOptionalBooleanValue(element, "CAN-FD-FRAME-SUPPORT")) \
                  .setCanFrameRxBehavior(self.getChildElementOptionalLiteral(element, "CAN-FRAME-RX-BEHAVIOR")) \
                  .setCanFrameTxBehavior(self.getChildElementOptionalLiteral(element, "CAN-FRAME-TX-BEHAVIOR")) \
                  .setIdentifier(self.getChildElementOptionalNumericalValue(element, "IDENTIFIER")) \
                  .setRxIdentifierRange(self.getChildElementRxIdentifierRange(element, "RX-IDENTIFIER-RANGE"))


# readLinFrameTriggering
    def readLinFrameTriggering(self, element: ET.Element, triggering: LinFrameTriggering):
        self.logger.debug("Read LinFrameTriggering %s" % triggering.getShortName())
        self.readFrameTriggering(element, triggering)
        triggering.setIdentifier(self.getChildElementOptionalNumericalValue(element, "IDENTIFIER")) \
                  .setLinChecksum(self.getChildElementOptionalLiteral(element, "LIN-CHECKSUM"))
        

# readFlexrayFrameTriggeringAbsolutelyScheduledTimings
    def readFlexrayFrameTriggeringAbsolutelyScheduledTimings(self, element: ET.Element, triggering: FlexrayFrameTriggering):
        for child_element in self.findall(element, "ABSOLUTELY-SCHEDULED-TIMINGS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "FLEXRAY-ABSOLUTELY-SCHEDULED-TIMING":
                timing = FlexrayAbsolutelyScheduledTiming()
                self.readFlexrayAbsolutelyScheduledTiming(child_element, timing)
                triggering.addAbsolutelyScheduledTiming(timing)
            else:
                self.notImplemented("Unsupported AbsolutelyScheduledTiming <%s>" % tag_name)
        

# readFlexrayFrameTriggering
    def readFlexrayFrameTriggering(self, element: ET.Element, triggering: FlexrayFrameTriggering):
        self.logger.debug("Read FlexrayFrameTriggering %s" % triggering.getShortName())
        self.readFrameTriggering(element, triggering)
        self.readFlexrayFrameTriggeringAbsolutelyScheduledTimings(element, triggering)
        triggering.setAllowDynamicLSduLength(self.getChildElementOptionalBooleanValue(element, "ALLOW-DYNAMIC-L-SDU-LENGTH")) \
                  .setMessageId(self.getChildElementOptionalPositiveInteger(element, "MESSAGE-ID")) \
                  .setPayloadPreambleIndicator(self.getChildElementOptionalBooleanValue(element, "PAYLOAD-PREAMBLE-INDICATOR"))


# readISignalTriggering
    def readISignalTriggering(self, element: ET.Element, triggering: ISignalTriggering):
        self.logger.debug("Read ISignalTriggering %s" % triggering.getShortName())
        self.readIdentifiable(element, triggering)
        triggering.setISignalGroupRef(self.getChildElementOptionalRefType(element, "I-SIGNAL-GROUP-REF"))
        for ref in self.getChildElementRefTypeList(element, 'I-SIGNAL-PORT-REFS/I-SIGNAL-PORT-REF'):
            triggering.addISignalPortRef(ref)
        triggering.setISignalRef(self.getChildElementOptionalRefType(element, "I-SIGNAL-REF"))


# readPduTriggering
    def readPduTriggering(self, element: ET.Element, triggering: PduTriggering):
        self.logger.debug("Read PduTriggering %s" % triggering.getShortName())
        self.readIdentifiable(element, triggering)
        for ref in self.getChildElementRefTypeList(element, 'I-PDU-PORT-REFS/I-PDU-PORT-REF'):
            triggering.addIPduPortRef(ref)
        triggering.setIPduRef(self.getChildElementOptionalRefType(element, "I-PDU-REF"))
        for child_element in self.findall(element, 'I-SIGNAL-TRIGGERINGS/I-SIGNAL-TRIGGERING-REF-CONDITIONAL'):
            triggering.addISignalTriggeringRef(self.getChildElementOptionalRefType(child_element, "I-SIGNAL-TRIGGERING-REF"))


# readPhysicalChannelFrameTriggerings
    def readPhysicalChannelFrameTriggerings(self, element: ET.Element, channel: PhysicalChannel):
        for child_element in self.findall(element, "FRAME-TRIGGERINGS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "CAN-FRAME-TRIGGERING":
                triggering = channel.createCanFrameTriggering(self.getShortName(child_element))
                self.readCanFrameTriggering(child_element, triggering)
            elif tag_name == "LIN-FRAME-TRIGGERING":
                triggering = channel.createLinFrameTriggering(self.getShortName(child_element))
                self.readLinFrameTriggering(child_element, triggering)
            elif tag_name == "FLEXRAY-FRAME-TRIGGERING":
                triggering = channel.createFlexrayFrameTriggering(self.getShortName(child_element))
                self.readFlexrayFrameTriggering(child_element, triggering)
            else:
                self.notImplemented("Unsupported Frame Triggering <%s>" % tag_name)


# readPhysicalChannelISignalTriggerings
    def readPhysicalChannelISignalTriggerings(self, element: ET.Element, channel: PhysicalChannel):
        for child_element in self.findall(element, "I-SIGNAL-TRIGGERINGS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "I-SIGNAL-TRIGGERING":
                triggering = channel.createISignalTriggering(self.getShortName(child_element))
                self.readISignalTriggering(child_element, triggering)
            else:
                self.notImplemented("Unsupported Frame Triggering <%s>" % tag_name)


# readPhysicalChannelPduTriggerings
    def readPhysicalChannelPduTriggerings(self, element, channel):
        for child_element in self.findall(element, "PDU-TRIGGERINGS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "PDU-TRIGGERING":
                triggering = channel.createPduTriggering(self.getShortName(child_element))
                self.readPduTriggering(child_element, triggering)
            else:
                self.notImplemented("Unsupported Frame Triggering <%s>" % tag_name)


# readPortPrototypeBlueprint
    def readPortPrototypeBlueprint(self, element: ET.Element, blueprint: PortPrototypeBlueprint):
        self.logger.debug("Read PortPrototypeBlueprint <%s>" % blueprint.getShortName())
        self.readARElement(element, blueprint)
        blueprint.setInterfaceRef(self.getChildElementOptionalRefType(element, "INTERFACE-REF"))


# readCouplingPortSchedulerCouplingPortStructuralElement
    def readCouplingPortSchedulerCouplingPortStructuralElement(self, element: ET.Element, item: CouplingPortStructuralElement):
        self.readIdentifiable(element, item)


# readCouplingPortFifo
    def readCouplingPortFifo(self, element: ET.Element, fifo: CouplingPortFifo):
        self.readCouplingPortSchedulerCouplingPortStructuralElement(element, fifo)


# readCouplingPortScheduler
    def readCouplingPortScheduler(self, element: ET.Element, scheduler: CouplingPortScheduler):
        self.readCouplingPortSchedulerCouplingPortStructuralElement(element, scheduler)
        scheduler.setPortScheduler(self.getChildElementOptionalLiteral(element, "PORT-SCHEDULER"))


# readCouplingPortDetailsCouplingPortStructuralElements
    def readCouplingPortDetailsCouplingPortStructuralElements(self, item: ET.Element, details: CouplingPortDetails):
        for child_element in self.findall(item, "COUPLING-PORT-STRUCTURAL-ELEMENTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "COUPLING-PORT-FIFO":
                item = details.createCouplingPortFifo(self.getShortName(child_element))
                self.readCouplingPortFifo(child_element, item)
            elif tag_name == "COUPLING-PORT-SCHEDULER":
                item = details.createCouplingPortScheduler(self.getShortName(child_element))
                self.readCouplingPortScheduler(child_element, item)
            else:
                self.notImplemented("Unsupported CouplingPortStructuralElement <%s>" % tag_name)


# readCouplingPortDetailsEthernetPriorityRegenerations
    def readCouplingPortDetailsEthernetPriorityRegenerations(self, element: ET.Element, details: CouplingPortDetails):
        for child_element in self.findall(element, "ETHERNET-PRIORITY-REGENERATIONS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ETHERNET-PRIORITY-REGENERATION":
                item = details.createEthernetPriorityRegeneration(self.getShortName(child_element))
                self.readEthernetPriorityRegeneration(child_element, item)
            else:
                self.notImplemented("Unsupported EthernetPriorityRegeneration <%s>" % tag_name)


# readCouplingPortVlanMemberships
    def readCouplingPortVlanMemberships(self, element: ET.Element, port: CouplingPort):
        for child_element in self.findall(element, "VLAN-MEMBERSHIPS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "VLAN-MEMBERSHIP":
                membership = VlanMembership()
                self.readVlanMembership(child_element, membership)
                port.addVlanMembership(membership)
            else:
                self.notImplemented("Unsupported VlanMembership <%s>" % tag_name)


# readCouplingPort
    def readCouplingPort(self, element: ET.Element, port: CouplingPort):
        self.readIdentifiable(element, port)
        port.setCouplingPortDetails(self.getCouplingPortDetails(element, "COUPLING-PORT-DETAILS")) \
            .setMacAddressVlanAssignments(self.getChildElementOptionalLiteral(element, "MAC-LAYER-TYPE"))
        self.readCouplingPortVlanMemberships(element, port)


# readEthernetCommunicationControllerCouplingPorts
    def readEthernetCommunicationControllerCouplingPorts(self, element: ET.Element, controller: EthernetCommunicationController):
        for child_element in self.findall(element, "COUPLING-PORTS/*"):
            tag_name = self.getTagName(child_element)
            if (tag_name == "COUPLING-PORT"):
                port = controller.createCouplingPort(self.getShortName(child_element))
                self.readCouplingPort(child_element, port)
            else:
                self.notImplemented("Unsupported Coupling Port <%s>" % tag_name)


# readFramePort
    def readFramePort(self, element: ET.Element, port: FramePort):
        self.readCommConnectorPort(element, port)


# readIPduPort
    def readIPduPort(self, element: ET.Element, port: IPduPort):
        self.readCommConnectorPort(element, port)
        port.setKeyId(self.getChildElementOptionalPositiveInteger(element, "KEY-ID")) \
            .setRxSecurityVerification(self.getChildElementOptionalBooleanValue(element, "RX-SECURITY-VERIFICATION")) \
            .setUseAuthDataFreshness(self.getChildElementOptionalBooleanValue(element, "USE-AUTH-DATA-FRESHNESS"))


# readCommConnectorPort
    def readCommConnectorPort(self, element: ET.Element, port: CommConnectorPort):
        self.readIdentifiable(element, port)
        port.setCommunicationDirection(self.getChildElementOptionalLiteral(element, "COMMUNICATION-DIRECTION"))


# readISignalPort
    def readISignalPort(self, element: ET.Element, port: ISignalPort):
        self.readCommConnectorPort(element, port)
        port.setTimeout(self.getChildElementOptionalTimeValue(element, "TIMEOUT"))


# readCommunicationConnectorEcuCommPortInstances
    def readCommunicationConnectorEcuCommPortInstances(self, element: ET.Element, connector: CommunicationConnector):
        self.logger.debug("read EcuCommPortInstances of CommunicationConnector %s" % connector.getShortName())
        for child_element in self.findall(element, "ECU-COMM-PORT-INSTANCES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "FRAME-PORT":
                port = connector.createFramePort(self.getShortName(child_element))
                self.readFramePort(child_element, port)
            elif tag_name == "I-PDU-PORT":
                port = connector.createIPduPort(self.getShortName(child_element))
                self.readIPduPort(child_element, port)
            elif tag_name == "I-SIGNAL-PORT":
                port = connector.createISignalPort(self.getShortName(child_element))
                self.readISignalPort(child_element, port)
            else:
                self.raiseError("Unsupported EcuCommPortInstances <%s>" % tag_name)



    def readSenderRecCompositeTypeMapping(self, element: ET.Element, mapping: SenderRecCompositeTypeMapping):
        self.readARObjectAttributes(element, mapping)
