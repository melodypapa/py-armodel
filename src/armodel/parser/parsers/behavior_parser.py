"""
Parser for AUTOSAR behavior elements.

Handles:
- InternalBehavior (SwcInternalBehavior, BswInternalBehavior)
- RunnableEntity
- RTE Events (InitEvent, TimingEvent, DataReceivedEvent, etc.)
- BSW behaviors (BswInternalBehavior, BswModuleEntity)
- SwcImplementation, BswImplementation
- Service dependencies
- Resource consumption (MemorySection, StackUsage)
- SwcBswMapping
"""
from typing import List
import xml.etree.ElementTree as ET

from ..base_arxml_parser import BaseARXMLParser
from ...models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR

# Import behavior-related model classes
from ...models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import (
    ExecutableEntity,
    InternalBehavior,
)
from ...models.M2.AUTOSARTemplates.CommonStructure.Implementation import (
    Implementation,
)
from ...models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption import (
    ResourceConsumption,
)
from ...models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.MemorySectionUsage import (
    MemorySection,
)
from ...models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.StackUsage import (
    RoughEstimateStackUsage,
    StackUsage,
)
from ...models.M2.AUTOSARTemplates.CommonStructure.SwcBswMapping import (
    SwcBswMapping,
    SwcBswRunnableMapping,
)
from ...models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    CryptoServiceNeeds,
    DiagnosticCapabilityElement,
    DiagnosticCommunicationManagerNeeds,
    DiagnosticEventInfoNeeds,
    DiagnosticEventNeeds,
    DiagEventDebounceMonitorInternal,
    DltUserNeeds,
    DtcStatusChangeNotificationNeeds,
    EcuStateMgrUserNeeds,
    DiagnosticRoutineNeeds,
    DiagnosticValueNeeds,
    NvBlockNeeds,
    RoleBasedDataAssignment,
    RoleBasedDataTypeAssignment,
    ServiceDependency,
    ServiceNeeds,
)
from ...models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration import Trigger
from ...models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import (
    BswApiOptions,
    BswAsynchronousServerCallPoint,
    BswBackgroundEvent,
    BswDataReceivedEvent,
    BswDataReceptionPolicy,
    BswExternalTriggerOccurredEvent,
    BswInternalBehavior,
    BswInternalTriggerOccurredEvent,
    BswInternalTriggeringPoint,
    BswInterruptEntity,
    BswModeSenderPolicy,
    BswModuleCallPoint,
    BswOperationInvokedEvent,
    BswQueuedDataReceptionPolicy,
    BswScheduleEvent,
    BswSynchronousServerCallPoint,
    BswTimingEvent,
    BswVariableAccess,
)
from ...models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import (
    BswCalledEntity,
    BswModeSwitchEvent,
    BswModuleEntity,
    BswSchedulableEntity,
)
from ...models.M2.AUTOSARTemplates.BswModuleTemplate.BswImplementation import (
    BswImplementation,
)
from ...models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces import (
    BswModuleClientServerEntry,
)
from ...models.M2.AUTOSARTemplates.BswModuleTemplate.BswOverview import (
    BswModuleDescription,
)
from ...models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior import (
    RunnableEntity,
    RunnableEntityArgument,
    SwcInternalBehavior,
)
from ...models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AutosarVariableRef import (
    AutosarVariableRef,
)
from ...models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import (
    ParameterAccess,
)
from ...models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.IncludedDataTypes import (
    IncludedDataTypeSet,
)
from ...models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.InstanceRefsUsage import (
    AutosarParameterRef,
    ParameterInAtomicSWCTypeInstanceRef,
    VariableInAtomicSWCTypeInstanceRef,
)
from ...models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ModeDeclarationGroup import (
    IncludedModeDeclarationGroupSet,
)
from ...models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions import (
    PortAPIOption,
    PortDefinedArgumentValue,
)
from ...models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents import (
    AsynchronousServerCallReturnsEvent,
    BackgroundEvent,
    DataReceivedEvent,
    DataSendCompletedEvent,
    InitEvent,
    InternalTriggerOccurredEvent,
    ModeSwitchedAckEvent,
    OperationInvokedEvent,
    RTEEvent,
    SwcModeSwitchEvent,
    TimingEvent,
)
from ...models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServerCall import (
    ServerCallPoint,
)
from ...models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping import (
    RoleBasedPortAssignment,
    SwcServiceDependency,
)
from ...models.M2.AUTOSARTemplates.SWComponentTemplate.SwcImplementation import (
    SwcImplementation,
)
from ...models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import (
    AutosarDataPrototype,
    VariableDataPrototype,
)
from ...models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.InstanceRefs import (
    ApplicationCompositeElementInPortInterfaceInstanceRef,
)
from ...models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import (
    RModeInAtomicSwcInstanceRef,
)
from ...models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs import (
    POperationInAtomicSwcInstanceRef,
    ROperationInAtomicSwcInstanceRef,
)
from ...models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
    ParameterDataPrototype,
)
from ...models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class BehaviorParser(BaseARXMLParser):
    """
    Parser for AUTOSAR behavior elements.

    Handles internal behavior definitions for software components and BSW modules,
    including runnables, events, service dependencies, and implementations.
    """

    def __init__(self, options=None, main_parser=None):
        """Initialize BehaviorParser."""
        super().__init__(options)
        self._main_parser = main_parser

    # ========================================================================
    # Helper Methods
    # ========================================================================

    def getVariableInAtomicSWCTypeInstanceRef(
        self, element: ET.Element
    ) -> VariableInAtomicSWCTypeInstanceRef:
        """Get variable instance reference."""
        instance_ref = None
        if element is not None:
            instance_ref = VariableInAtomicSWCTypeInstanceRef()
            self.readARObjectAttributes(element, instance_ref)
            instance_ref.setPortPrototypeRef(
                self.getChildElementOptionalRefType(element, "PORT-PROTOTYPE-REF")
            )
            instance_ref.setTargetDataPrototypeRef(
                self.getChildElementOptionalRefType(element, "TARGET-DATA-PROTOTYPE-REF")
            )
        return instance_ref

    def getAutosarVariableRef(
        self, element: ET.Element, key: str
    ) -> AutosarVariableRef:
        """Get autosar variable reference."""
        child_element = self.find(element, key)
        instance_ref = None
        if child_element is not None:
            instance_ref = AutosarVariableRef()
            self.readARObjectAttributes(child_element, instance_ref)
            instance_ref.setAutosarVariableIRef(
                self.getVariableInAtomicSWCTypeInstanceRef(
                    self.find(child_element, "AUTOSAR-VARIABLE-IREF")
                )
            )
            instance_ref.setLocalVariableRef(
                self.getChildElementOptionalRefType(child_element, "LOCAL-VARIABLE-REF")
            )
        return instance_ref

    def getParameterInAtomicSWCTypeInstanceRef(
        self, element: ET.Element, key: str
    ) -> ParameterInAtomicSWCTypeInstanceRef:
        """Get parameter instance reference."""
        parameter_iref = None
        child_element = self.find(element, key)
        if child_element is not None:
            parameter_iref = ParameterInAtomicSWCTypeInstanceRef()
            parameter_iref.setBaseRef(
                self.getChildElementOptionalRefType(child_element, "BASE-REF")
            )
            parameter_iref.setContextDataPrototypeRef(
                self.getChildElementOptionalRefType(
                    child_element, "CONTEXT-DATA-PROTOTYPE-REF"
                )
            )
            parameter_iref.setPortPrototypeRef(
                self.getChildElementOptionalRefType(child_element, "PORT-PROTOTYPE-REF")
            )
            parameter_iref.setRootParameterDataPrototypeRef(
                self.getChildElementOptionalRefType(
                    child_element, "ROOT-PARAMETER-DATA-PROTOTYPE-REF"
                )
            )
            parameter_iref.setTargetDataPrototypeRef(
                self.getChildElementOptionalRefType(
                    child_element, "TARGET-DATA-PROTOTYPE-REF"
                )
            )
        return parameter_iref

    def getAutosarParameterRef(
        self, element: ET.Element, key: str
    ) -> AutosarParameterRef:
        """Get autosar parameter reference."""
        parameter = None
        child_element = self.find(element, key)
        if child_element is not None:
            parameter = AutosarParameterRef()
            parameter.setAutosarParameterIRef(
                self.getParameterInAtomicSWCTypeInstanceRef(
                    child_element, "AUTOSAR-PARAMETER-IREF"
                )
            )
            parameter.setLocalParameterRef(
                self.getChildElementOptionalRefType(child_element, "LOCAL-PARAMETER-REF")
            )
        return parameter

    def getRunnableEntityArgument(
        self, element: ET.Element
    ) -> RunnableEntityArgument:
        """Get runnable entity argument."""
        argument = RunnableEntityArgument()
        argument.setSymbol(self.getChildElementOptionalLiteral(element, "SYMBOL"))
        return argument

    def getIncludedModeDeclarationGroupSets(
        self, element: ET.Element
    ) -> List[IncludedModeDeclarationGroupSet]:
        """Get included mode declaration group sets."""
        group_sets = []
        for child_element in self.findall(
            element,
            "INCLUDED-MODE-DECLARATION-GROUP-SETS/INCLUDED-MODE-DECLARATION-GROUP-SET",
        ):
            group_set = IncludedModeDeclarationGroupSet()
            for ref_type in self.getChildElementRefTypeList(
                child_element, "MODE-DECLARATION-GROUP-REFS/MODE-DECLARATION-GROUP-REF"
            ):
                group_set.addModeDeclarationGroupRef(ref_type)
            group_sets.append(group_set)
        return group_sets

    def getIncludedDataTypeSets(self, element: ET.Element) -> List[IncludedDataTypeSet]:
        """Get included data type sets."""
        include_data_type_sets = []
        for child_element in self.findall(
            element, "INCLUDED-DATA-TYPE-SETS/INCLUDED-DATA-TYPE-SET"
        ):
            include_data_type_set = IncludedDataTypeSet()
            self.readARObjectAttributes(child_element, include_data_type_set)
            for ref_type in self.getChildElementRefTypeList(
                child_element, "DATA-TYPE-REFS/DATA-TYPE-REF"
            ):
                include_data_type_set.addDataTypeRef(ref_type)
            include_data_type_sets.append(include_data_type_set)
        return include_data_type_sets

    def getRoleBasedDataAssignment(
        self, element: ET.Element
    ) -> RoleBasedDataAssignment:
        """Get role based data assignment."""
        assignment = RoleBasedDataAssignment()
        assignment.setRole(self.getChildElementOptionalLiteral(element, "ROLE"))
        assignment.setUsedDataElement(self.getAutosarVariableRef(element, "USED-DATA-ELEMENT"))
        assignment.setUsedParameterElement(
            self.getAutosarParameterRef(element, "USED-PARAMETER-ELEMENT")
        )
        assignment.setUsedPimRef(
            self.getChildElementOptionalRefType(element, "USED-PIM-REF")
        )
        return assignment

    def getRoleBasedPortAssignment(
        self, element: ET.Element
    ) -> RoleBasedPortAssignment:
        """Get role based port assignment."""
        assignment = RoleBasedPortAssignment()
        self.readARObjectAttributes(element, assignment)
        assignment.portPrototypeRef = self.getChildElementOptionalRefType(
            element, "PORT-PROTOTYPE-REF"
        )
        assignment.role = self.getChildElementOptionalLiteral(element, "ROLE")
        return assignment

    def getRoleBasedDataTypeAssignment(
        self, element: ET.Element
    ) -> RoleBasedDataTypeAssignment:
        """Get role based data type assignment."""
        assignment = RoleBasedDataTypeAssignment()
        assignment.setRole(self.getChildElementOptionalLiteral(element, "ROLE"))
        assignment.setUsedImplementationDataTypeRef(
            self.getChildElementOptionalRefType(element, "USED-IMPLEMENTATION-DATA-TYPE-REF")
        )
        return assignment

    def getBswModeSenderPolicy(self, element: ET.Element) -> BswModeSenderPolicy:
        """Get BSW mode sender policy."""
        policy = BswModeSenderPolicy()
        policy.setProvidedModeGroupRef(
            self.getChildElementOptionalRefType(element, "PROVIDED-MODE-GROUP-REF")
        )
        policy.setQueueLength(
            self.getChildElementOptionalNumericalValue(element, "QUEUE-LENGTH")
        )
        return policy

    # ========================================================================
    # Internal Behavior
    # ========================================================================

    def readInternalBehaviorConstantMemories(
        self, element: ET.Element, behavior: InternalBehavior
    ):
        """Read internal behavior constant memories."""
        for child_element in self.findall(element, "CONSTANT-MEMORYS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "PARAMETER-DATA-PROTOTYPE":
                prototype = behavior.createConstantMemory(self.getShortName(child_element))
                # Delegate to PortInterfaceParser for ParameterDataPrototype
                if self._main_parser:
                    self._main_parser._port_interface_parser.readParameterDataPrototype(
                        child_element, prototype
                    )
                else:
                    self.raiseError("PortInterfaceParser not available")
            else:
                self.notImplemented("Unsupported constant memories <%s>" % tag_name)

    def readInternalBehaviorStaticMemories(
        self, element: ET.Element, behavior: InternalBehavior
    ):
        """Read internal behavior static memories."""
        for child_element in self.findall(element, "STATIC-MEMORYS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "VARIABLE-DATA-PROTOTYPE":
                prototype = behavior.createStaticMemory(self.getShortName(child_element))
                self.readVariableDataPrototype(child_element, prototype)
            else:
                self.notImplemented("Unsupported static memories <%s>" % tag_name)

    def readInternalBehavior(
        self, element: ET.Element, behavior: InternalBehavior
    ):
        """Read internal behavior."""
        self.readIdentifiable(element, behavior)
        self.readInternalBehaviorConstantMemories(element, behavior)
        for child_element in self.findall(element, "EXCLUSIVE-AREAS/EXCLUSIVE-AREA"):
            short_name = self.getShortName(child_element)
            behavior.createExclusiveArea(short_name)
        # Delegate to DataTypeParser for DataTypeMappingRefs
        if self._main_parser:
            self._main_parser._datatype_parser.readDataTypeMappingRefs(
                element, behavior
            )
        else:
            self.notImplemented("DataTypeParser not available for DataTypeMappingRefs")
        self.readInternalBehaviorStaticMemories(element, behavior)

    # ========================================================================
    # SwcInternalBehavior
    # ========================================================================

    def readSwcInternalBehaviorArTypedPerInstanceMemories(
        self, element: ET.Element, parent: SwcInternalBehavior
    ):
        """Read AR-typed per-instance memories."""
        for child_element in self.findall(
            element, "AR-TYPED-PER-INSTANCE-MEMORYS/VARIABLE-DATA-PROTOTYPE"
        ):
            short_name = self.getShortName(child_element)
            prototype = parent.createArTypedPerInstanceMemory(short_name)
            self.readVariableDataPrototype(child_element, prototype)

    def readSwcInternalBehaviorSharedParameters(
        self, element: ET.Element, behavior: SwcInternalBehavior
    ):
        """Read shared parameters."""
        for child_element in self.findall(
            element, "SHARED-PARAMETERS/PARAMETER-DATA-PROTOTYPE"
        ):
            short_name = self.getShortName(child_element)
            prototype = behavior.createSharedParameter(short_name)
            # Delegate to PortInterfaceParser
            if self._main_parser:
                self._main_parser._port_interface_parser.readParameterDataPrototype(
                    child_element, prototype
                )
            else:
                self.raiseError("PortInterfaceParser not available")

    def readSwcInternalBehaviorEvents(
        self, element: ET.Element, parent: SwcInternalBehavior
    ):
        """Read SWC internal behavior events."""
        for child_element in self.findall(element, "EVENTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "TIMING-EVENT":
                event = parent.createTimingEvent(self.getShortName(child_element))
                self.readTimingEvent(child_element, event)
            elif tag_name == "SWC-MODE-SWITCH-EVENT":
                event = parent.createSwcModeSwitchEvent(self.getShortName(child_element))
                # Delegate to PortInterfaceParser
                if self._main_parser:
                    self._main_parser._port_interface_parser.readSwcModeSwitchEvent(
                        child_element, event
                    )
                else:
                    self.raiseError("PortInterfaceParser not available")
            elif tag_name == "OPERATION-INVOKED-EVENT":
                event = parent.createOperationInvokedEvent(self.getShortName(child_element))
                self.readOperationInvokedEvent(child_element, event)
            elif tag_name == "DATA-RECEIVED-EVENT":
                event = parent.createDataReceivedEvent(self.getShortName(child_element))
                self.readDataReceivedEvent(child_element, event)
            elif tag_name == "INTERNAL-TRIGGER-OCCURRED-EVENT":
                event = parent.createInternalTriggerOccurredEvent(
                    self.getShortName(child_element)
                )
                self.readInternalTriggerOccurredEvent(child_element, event)
            elif tag_name == "INIT-EVENT":
                event = parent.createInitEvent(self.getShortName(child_element))
                self.readInitEvent(child_element, event)
            elif tag_name == "ASYNCHRONOUS-SERVER-CALL-RETURNS-EVENT":
                event = parent.createAsynchronousServerCallReturnsEvent(
                    self.getShortName(child_element)
                )
                self.readAsynchronousServerCallReturnsEvent(child_element, event)
            elif tag_name == "MODE-SWITCHED-ACK-EVENT":
                event = parent.createModeSwitchedAckEvent(self.getShortName(child_element))
                # Delegate to PortInterfaceParser
                if self._main_parser:
                    self._main_parser._port_interface_parser.readModeSwitchedAckEvent(
                        child_element, event
                    )
                else:
                    self.raiseError("PortInterfaceParser not available")
            elif tag_name == "BACKGROUND-EVENT":
                event = parent.createBackgroundEvent(self.getShortName(child_element))
                self.readBackgroundEvent(child_element, event)
            elif tag_name == "DATA-SEND-COMPLETED-EVENT":
                event = parent.createDataSendCompletedEvent(self.getShortName(child_element))
                self.readDataSendCompletedEvent(child_element, event)
            else:
                self.notImplemented("Unsupported SwcInternalBehavior Event <%s>" % tag_name)

    def readSwcInternalBehaviorExplicitInterRunnableVariables(
        self, element: ET.Element, parent: SwcInternalBehavior
    ):
        """Read explicit inter-runnable variables."""
        for child_element in self.findall(
            element, "EXPLICIT-INTER-RUNNABLE-VARIABLES/VARIABLE-DATA-PROTOTYPE"
        ):
            short_name = self.getShortName(child_element)
            prototype = parent.createExplicitInterRunnableVariable(short_name)
            self.readVariableDataPrototype(child_element, prototype)

    def readSwcInternalBehaviorPerInstanceMemories(
        self, element: ET.Element, behavior: SwcInternalBehavior
    ):
        """Read per-instance memories."""
        for child_element in self.findall(
            element, "PER-INSTANCE-MEMORYS/PER-INSTANCE-MEMORY"
        ):
            short_name = self.getShortName(child_element)
            memory = behavior.createPerInstanceMemory(short_name)
            self.readIdentifiable(child_element, memory)
            memory.setInitValue(
                self.getChildElementOptionalLiteral(child_element, "INIT-VALUE")
            )
            # Delegate to DataTypeParser for SwDataDefProps
            if self._main_parser:
                memory.setSwDataDefProps(
                    self._main_parser._datatype_parser.getSwDataDefProps(
                        child_element, "SW-DATA-DEF-PROPS"
                    )
                )
            else:
                self.notImplemented("DataTypeParser not available for SwDataDefProps")
            memory.setType(self.getChildElementOptionalLiteral(child_element, "TYPE"))
            memory.setTypeDefinition(
                self.getChildElementOptionalLiteral(child_element, "TYPE-DEFINITION")
            )

    def readSwcInternalBehaviorPortAPIOptions(
        self, element: ET.Element, behavior: SwcInternalBehavior
    ):
        """Read port API options."""
        for child_element in self.findall(element, "PORT-API-OPTIONS/PORT-API-OPTION"):
            option = PortAPIOption()
            option.setEnableTakeAddress(
                self.getChildElementOptionalBooleanValue(child_element, "ENABLE-TAKE-ADDRESS")
            )
            option.setErrorHandling(
                self.getChildElementOptionalLiteral(child_element, "ERROR-HANDLING")
            )
            option.setIndirectAPI(
                self.getChildElementOptionalBooleanValue(child_element, "INDIRECT-API")
            )
            option.setPortRef(
                self.getChildElementOptionalRefType(child_element, "PORT-REF")
            )
            for argument_value_tag in self.findall(
                child_element, "PORT-ARG-VALUES/PORT-DEFINED-ARGUMENT-VALUE"
            ):
                # Delegate to PortInterfaceParser
                if self._main_parser:
                    option.addPortArgValue(
                        self._main_parser._port_interface_parser.readPortDefinedArgumentValue(
                            argument_value_tag
                        )
                    )
            behavior.addPortAPIOption(option)

    def readSwcInternalBehavior(
        self, element: ET.Element, behavior: SwcInternalBehavior
    ):
        """Read SWC internal behavior."""
        # Read the internal behavior
        self.readInternalBehavior(element, behavior)

        # Read the extra SwcInternalBehavior
        self.readSwcInternalBehaviorArTypedPerInstanceMemories(element, behavior)
        self.readSwcInternalBehaviorEvents(element, behavior)
        self.readSwcInternalBehaviorExplicitInterRunnableVariables(element, behavior)
        behavior.setHandleTerminationAndRestart(
            self.getChildElementOptionalLiteral(element, "HANDLE-TERMINATION-AND-RESTART")
        )
        # Delegate to PortInterfaceParser
        if self._main_parser:
            self._main_parser._port_interface_parser.readSwcInternalBehaviorIncludedModeDeclarationGroupSets(
                element, behavior
            )
            self._main_parser._port_interface_parser.readSwcInternalBehaviorPerInstanceParameters(
                element, behavior
            )
        else:
            self.notImplemented("PortInterfaceParser not available")
        self.readSwcInternalBehaviorPerInstanceMemories(element, behavior)
        self.readSwcInternalBehaviorPortAPIOptions(element, behavior)
        self.readSwcInternalBehaviorRunnables(element, behavior)
        self.readSwcInternalBehaviorServiceDependencies(element, behavior)
        self.readSwcInternalBehaviorSharedParameters(element, behavior)
        behavior.setSupportsMultipleInstantiation(
            self.getChildElementOptionalBooleanValue(element, "SUPPORTS-MULTIPLE-INSTANTIATION")
        )

    # ========================================================================
    # RunnableEntity
    # ========================================================================

    def _readVariableAccesses(
        self, element: ET.Element, parent: RunnableEntity, key: str
    ):
        """Read variable accesses."""
        for child_element in self.findall(element, "%s/VARIABLE-ACCESS" % key):
            short_name = self.getShortName(child_element)

            if key == "DATA-RECEIVE-POINT-BY-ARGUMENTS":
                variable_access = parent.createDataReceivePointByArgument(short_name)
                variable_access.setAccessedVariableRef(
                    self.getAutosarVariableRef(child_element, "ACCESSED-VARIABLE")
                )
            elif key == "DATA-RECEIVE-POINT-BY-VALUES":
                variable_access = parent.createDataReceivePointByValue(short_name)
                variable_access.setAccessedVariableRef(
                    self.getAutosarVariableRef(child_element, "ACCESSED-VARIABLE")
                )
            elif key == "DATA-READ-ACCESSS":
                variable_access = parent.createDataReadAccess(short_name)
                variable_access.setAccessedVariableRef(
                    self.getAutosarVariableRef(child_element, "ACCESSED-VARIABLE")
                )
            elif key == "DATA-WRITE-ACCESSS":
                variable_access = parent.createDataWriteAccess(short_name)
                variable_access.setAccessedVariableRef(
                    self.getAutosarVariableRef(child_element, "ACCESSED-VARIABLE")
                )
            elif key == "DATA-SEND-POINTS":
                variable_access = parent.createDataSendPoint(short_name)
                variable_access.setAccessedVariableRef(
                    self.getAutosarVariableRef(child_element, "ACCESSED-VARIABLE")
                )
            elif key == "WRITTEN-LOCAL-VARIABLES":
                variable_access = parent.createWrittenLocalVariable(short_name)
                variable_access.setAccessedVariableRef(
                    self.getAutosarVariableRef(child_element, "ACCESSED-VARIABLE")
                )
            elif key == "READ-LOCAL-VARIABLES":
                variable_access = parent.createReadLocalVariable(short_name)
                variable_access.setAccessedVariableRef(
                    self.getAutosarVariableRef(child_element, "ACCESSED-VARIABLE")
                )
            else:
                self.notImplemented("Unsupported Variable Accesss <%s>" % key)

            self.readIdentifiable(child_element, variable_access)

    def readRunnableEntityDataReceivePointByArguments(
        self, element, parent: RunnableEntity
    ):
        """Read data receive points by arguments."""
        self._readVariableAccesses(element, parent, "DATA-RECEIVE-POINT-BY-ARGUMENTS")

    def readRunnableEntityDataReceivePointByValues(
        self, element: ET.Element, parent: RunnableEntity
    ):
        """Read data receive points by values."""
        self._readVariableAccesses(element, parent, "DATA-RECEIVE-POINT-BY-VALUES")

    def readRunnableEntityDataReadAccesses(
        self, element: ET.Element, parent: RunnableEntity
    ):
        """Read data read accesses."""
        self._readVariableAccesses(element, parent, "DATA-READ-ACCESSS")

    def readRunnableEntityDataWriteAccesses(
        self, element: ET.Element, parent: RunnableEntity
    ):
        """Read data write accesses."""
        self._readVariableAccesses(element, parent, "DATA-WRITE-ACCESSS")

    def readRunnableEntityDataSendPoints(
        self, element: ET.Element, parent: RunnableEntity
    ):
        """Read data send points."""
        self._readVariableAccesses(element, parent, "DATA-SEND-POINTS")

    def readParameterAccess(self, element: ET.Element, access: ParameterAccess):
        """Read parameter access."""
        self.readIdentifiable(element, access)
        access.setAccessedParameter(
            self.getAutosarParameterRef(element, "ACCESSED-PARAMETER")
        )

    def readRunnableEntityParameterAccesses(
        self, element: ET.Element, parent: RunnableEntity
    ):
        """Read parameter accesses."""
        for child_element in self.findall(element, "PARAMETER-ACCESSS/PARAMETER-ACCESS"):
            short_name = self.getShortName(child_element)
            parameter_access = parent.createParameterAccess(short_name)
            self.readParameterAccess(child_element, parameter_access)

    def readRunnableEntityWrittenLocalVariables(
        self, element: ET.Element, parent: RunnableEntity
    ):
        """Read written local variables."""
        self._readVariableAccesses(element, parent, "WRITTEN-LOCAL-VARIABLES")

    def readRunnableEntityReadLocalVariables(
        self, element: ET.Element, parent: RunnableEntity
    ):
        """Read read local variables."""
        self._readVariableAccesses(element, parent, "READ-LOCAL-VARIABLES")

    def readROperationIRef(
        self, element: ET.Element, key: str, parent: ServerCallPoint
    ):
        """Read required operation instance reference."""
        child_element = self.find(element, key)
        if child_element is not None:
            operation_iref = ROperationInAtomicSwcInstanceRef()
            self.readARObjectAttributes(child_element, operation_iref)
            operation_iref.setContextRPortRef(
                self.getChildElementOptionalRefType(child_element, "CONTEXT-R-PORT-REF")
            ).setTargetRequiredOperationRef(
                self.getChildElementOptionalRefType(
                    child_element, "TARGET-REQUIRED-OPERATION-REF"
                )
            )
            parent.setOperationIRef(operation_iref)

    def readSynchronousServerCallPoint(
        self, element: ET.Element, parent: RunnableEntity
    ):
        """Read synchronous server call point."""
        short_name = self.getShortName(element)
        server_call_point = parent.createSynchronousServerCallPoint(short_name)
        self.readIdentifiable(element, server_call_point)
        server_call_point.setTimeout(
            self.getChildElementOptionalFloatValue(element, "TIMEOUT")
        )
        self.readROperationIRef(element, "OPERATION-IREF", server_call_point)

    def readAsynchronousServerCallPoint(
        self, element: ET.Element, parent: RunnableEntity
    ):
        """Read asynchronous server call point."""
        short_name = self.getShortName(element)
        server_call_point = parent.createAsynchronousServerCallPoint(short_name)
        self.readIdentifiable(element, server_call_point)
        server_call_point.setTimeout(
            self.getChildElementOptionalFloatValue(element, "TIMEOUT")
        )
        self.readROperationIRef(element, "OPERATION-IREF", server_call_point)

    def readRunnableEntityInternalBehaviorServerCallPoint(
        self, element: ET.Element, parent: RunnableEntity
    ):
        """Read server call points."""
        for child_element in self.findall(element, "SERVER-CALL-POINTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "SYNCHRONOUS-SERVER-CALL-POINT":
                self.readSynchronousServerCallPoint(child_element, parent)
            elif tag_name == "ASYNCHRONOUS-SERVER-CALL-POINT":
                self.readAsynchronousServerCallPoint(child_element, parent)
            else:
                self.raiseError("Unsupported server call point type <%s>" % tag_name)

    def readRunnableEntityInternalTriggeringPoints(
        self, element: ET.Element, parent: RunnableEntity
    ):
        """Read internal triggering points."""
        for child_element in self.findall(
            element, "INTERNAL-TRIGGERING-POINTS/INTERNAL-TRIGGERING-POINT"
        ):
            short_name = self.getShortName(child_element)
            point = parent.createInternalTriggeringPoint(short_name)
            point.sw_impl_policy = self.getChildElementOptionalLiteral(
                child_element, "SW-IMPL-POLICY"
            )

    def readRunnableEntityModeAccessPoints(self, element, parent):
        """Delegate to PortInterfaceParser."""
        if self._main_parser:
            return self._main_parser._port_interface_parser.readRunnableEntityModeAccessPoints(
                element, parent
            )
        else:
            self.raiseError("PortInterfaceParser not available")

    def readRunnableEntityModeSwitchPoints(self, element, parent):
        """Delegate to PortInterfaceParser."""
        if self._main_parser:
            return self._main_parser._port_interface_parser.readRunnableEntityModeSwitchPoints(
                element, parent
            )
        else:
            self.raiseError("PortInterfaceParser not available")

    def readRunnableEntityArguments(
        self, element: ET.Element, entity: RunnableEntity
    ):
        """Read runnable entity arguments."""
        for child_element in self.findall(element, "ARGUMENTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "RUNNABLE-ENTITY-ARGUMENT":
                entity.addArgument(self.getRunnableEntityArgument(child_element))
            else:
                self.notImplemented(
                    "Unsupported Arguments of runnable entity <%s>" % tag_name
                )

    def readRunnableEntityAsynchronousServerCallResultPoint(
        self, element: ET.Element, entity: RunnableEntity
    ):
        """Read asynchronous server call result points."""
        for child_element in self.findall(
            element,
            "ASYNCHRONOUS-SERVER-CALL-RESULT-POINTS/ASYNCHRONOUS-SERVER-CALL-RESULT-POINT",
        ):
            point = entity.createAsynchronousServerCallResultPoint(
                self.getShortName(child_element)
            )
            self.readIdentifiable(child_element, point)
            point.setAsynchronousServerCallPointRef(
                self.getChildElementOptionalRefType(
                    child_element, "ASYNCHRONOUS-SERVER-CALL-POINT-REF"
                )
            )

    def readRunnableEntity(self, element: ET.Element, entity: RunnableEntity):
        """Read runnable entity."""
        self.readExecutableEntity(element, entity)
        self.readRunnableEntityArguments(element, entity)

        self.readRunnableEntityAsynchronousServerCallResultPoint(element, entity)
        entity.setCanBeInvokedConcurrently(
            self.getChildElementOptionalBooleanValue(element, "CAN-BE-INVOKED-CONCURRENTLY")
        )
        self.readRunnableEntityDataReadAccesses(element, entity)
        self.readRunnableEntityDataReceivePointByArguments(element, entity)
        self.readRunnableEntityDataReceivePointByValues(element, entity)
        self.readRunnableEntityDataWriteAccesses(element, entity)
        self.readRunnableEntityDataSendPoints(element, entity)
        self.readRunnableEntityInternalBehaviorServerCallPoint(element, entity)
        self.readRunnableEntityInternalTriggeringPoints(element, entity)
        self.readRunnableEntityModeAccessPoints(element, entity)
        self.readRunnableEntityModeSwitchPoints(element, entity)
        self.readRunnableEntityParameterAccesses(element, entity)
        self.readRunnableEntityReadLocalVariables(element, entity)
        self.readRunnableEntityWrittenLocalVariables(element, entity)

        entity.setSymbol(self.getChildElementOptionalLiteral(element, "SYMBOL"))

    def readSwcInternalBehaviorRunnables(
        self, element: ET.Element, parent: SwcInternalBehavior
    ):
        """Read runnables."""
        for child_element in self.findall(element, "RUNNABLES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "RUNNABLE-ENTITY":
                entity = parent.createRunnableEntity(self.getShortName(child_element))
                self.readRunnableEntity(child_element, entity)
            else:
                self.notImplemented("Unsupported Runnables <%s>" % tag_name)

    # ========================================================================
    # RTE Events
    # ========================================================================

    def getRModeInAtomicSwcInstanceRef(
        self, element: ET.Element
    ) -> RModeInAtomicSwcInstanceRef:
        """Get RModeInAtomicSwcInstanceRef."""
        instance_ref = RModeInAtomicSwcInstanceRef()
        instance_ref.setBaseRef(
            self.getChildElementOptionalRefType(element, "BASE-REF")
        ).setContextPortRef(
            self.getChildElementOptionalRefType(element, "CONTEXT-PORT-REF")
        ).setContextModeDeclarationGroupPrototypeRef(
            self.getChildElementOptionalRefType(
                element, "CONTEXT-MODE-DECLARATION-GROUP-PROTOTYPE-REF"
            )
        ).setTargetModeDeclarationRef(
            self.getChildElementOptionalRefType(element, "TARGET-MODE-DECLARATION-REF")
        )
        return instance_ref

    def readRTEEvent(self, element: ET.Element, event: RTEEvent):
        """Read RTE event."""
        self.readIdentifiable(element, event)
        event.startOnEventRef = self.getChildElementOptionalRefType(
            element, "START-ON-EVENT-REF"
        )
        for child_element in self.findall(
            element, "DISABLED-MODE-IREFS/DISABLED-MODE-IREF"
        ):
            iref = self.getRModeInAtomicSwcInstanceRef(child_element)
            event.addDisabledModeIRef(iref)

    def readRVariableInAtomicSwcInstanceRef(
        self, element: ET.Element, parent: DataReceivedEvent
    ):
        """Read RVariableInAtomicSwcInstanceRef."""
        child_element = self.find(element, "DATA-IREF")
        if child_element is not None:
            data_iref = RVariableInAtomicSwcInstanceRef()
            data_iref.setContextRPortRef(
                self.getChildElementOptionalRefType(child_element, "CONTEXT-R-PORT-REF")
            ).setTargetDataElementRef(
                self.getChildElementOptionalRefType(child_element, "TARGET-DATA-ELEMENT-REF")
            )
            parent.setDataIRef(data_iref)

    def readTimingEvent(self, element: ET.Element, event: TimingEvent):
        """Read timing event."""
        self.readRTEEvent(element, event)
        event.setOffset(self.getChildElementOptionalTimeValue(element, "OFFSET")).setPeriod(
            self.getChildElementOptionalTimeValue(element, "PERIOD")
        )

    def readDataReceivedEvent(self, element: ET.Element, event: DataReceivedEvent):
        """Read data received event."""
        self.readRTEEvent(element, event)
        self.readRVariableInAtomicSwcInstanceRef(element, event)

    def readInternalTriggerOccurredEvent(
        self, element: ET.Element, event: InternalTriggerOccurredEvent
    ):
        """Read internal trigger occurred event."""
        self.readRTEEvent(element, event)
        event.setEventSourceRef(
            self.getChildElementOptionalRefType(element, "EVENT-SOURCE-REF")
        )

    def readInitEvent(self, element, event: InitEvent):
        """Read init event."""
        self.readRTEEvent(element, event)

    def readAsynchronousServerCallReturnsEvent(
        self, element, event: AsynchronousServerCallReturnsEvent
    ):
        """Read asynchronous server call returns event."""
        self.readRTEEvent(element, event)
        event.setActivationReasonRepresentationRef(
            self.getChildElementOptionalRefType(element, "EVENT-SOURCE-REF")
        )

    def readBackgroundEvent(self, element, event: BackgroundEvent):
        """Read background event."""
        self.readRTEEvent(element, event)

    def readDataSendCompletedEvent(self, element, event: DataSendCompletedEvent):
        """Read data send completed event."""
        self.readRTEEvent(element, event)
        event.setEventSourceRef(
            self.getChildElementOptionalRefType(element, "EVENT-SOURCE-REF")
        )

    def readPOperationIRef(
        self, element: ET.Element, key: str, parent: OperationInvokedEvent
    ):
        """Read POperationInAtomicSwcInstanceRef."""
        child_element = self.find(element, key)
        if child_element is not None:
            operation_iref = POperationInAtomicSwcInstanceRef()
            self.readARObjectAttributes(child_element, operation_iref)
            operation_iref.setContextPPortRef(
                self.getChildElementRefType(
                    parent.getShortName(), child_element, "CONTEXT-P-PORT-REF"
                )
            ).setTargetProvidedOperationRef(
                self.getChildElementRefType(
                    parent.getShortName(), child_element, "TARGET-PROVIDED-OPERATION-REF"
                )
            )
            parent.setOperationIRef(operation_iref)

    def readOperationInvokedEvent(self, element: ET.Element, event: OperationInvokedEvent):
        """Read operation invoked event."""
        self.readPOperationIRef(element, "OPERATION-IREF", event)
        self.readRTEEvent(element, event)

    # ========================================================================
    # ExecutableEntity
    # ========================================================================

    def readCanEnterExclusiveAreaRefs(
        self, element: ET.Element, entity: ExecutableEntity
    ):
        """Read can enter exclusive area refs."""
        for ref in self.getChildElementRefTypeList(
            element, "CAN-ENTER-EXCLUSIVE-AREA-REFS/CAN-ENTER-EXCLUSIVE-AREA-REF"
        ):
            entity.addCanEnterExclusiveAreaRef(ref)

    def readExecutableEntity(self, element: ET.Element, entity: ExecutableEntity):
        """Read executable entity."""
        self.readIdentifiable(element, entity)
        self.readCanEnterExclusiveAreaRefs(element, entity)
        entity.setMinimumStartInterval(
            self.getChildElementOptionalFloatValue(element, "MINIMUM-START-INTERVAL")
        ).setSwAddrMethodRef(
            self.getChildElementOptionalRefType(element, "SW-ADDR-METHOD-REF")
        )

    # ========================================================================
    # BSW Internal Behavior
    # ========================================================================

    def readBswEvent(self, element: ET.Element, event: BswScheduleEvent):
        """Read BSW event."""
        event.startsOnEventRef = self.getChildElementOptionalRefType(
            element, "STARTS-ON-EVENT-REF"
        )

    def readBswScheduleEvent(self, element, event: BswScheduleEvent):
        """Read BSW schedule event."""
        self.readBswEvent(element, event)

    def readBswTimingEvent(self, element: ET.Element, event: BswTimingEvent):
        """Read BSW timing event."""
        self.logger.debug("Read BswTimingEvent <%s>" % event.getShortName())
        # Read the Inherit BswScheduleEvent
        self.readBswScheduleEvent(element, event)
        event.setPeriod(self.getChildElementOptionalTimeValue(element, "PERIOD"))
        if event.getPeriod() is None:
            self.logger.warning(
                "Period of BswTimingEvent <%s> is invalid." % event.getShortName()
            )
        else:
            self.logger.debug(
                " Period: <%f, %s>"
                % (event.getPeriod().getValue(), event.getPeriod().getText())
            )

    def readBswDataReceivedEvent(self, element: ET.Element, event: BswDataReceivedEvent):
        """Read BSW data received event."""
        # Read the Inherit BswScheduleEvent
        self.readBswScheduleEvent(element, event)
        event.setDataRef(self.getChildElementOptionalRefType(element, "DATA-REF"))

    def readBswInternalTriggerOccurredEvent(
        self, element: ET.Element, event: BswInternalTriggerOccurredEvent
    ):
        """Read BSW internal trigger occurred event."""
        # Read the Inherit BswScheduleEvent
        self.readBswScheduleEvent(element, event)
        event.setEventSourceRef(
            self.getChildElementOptionalRefType(element, "EVENT-SOURCE-REF")
        )

    def readBswInternalBehaviorModeSenderPolicy(
        self, element: ET.Element, parent: BswInternalBehavior
    ):
        """Read BSW internal behavior mode sender policy."""
        for child_element in self.findall(element, "MODE-SENDER-POLICYS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "BSW-MODE-SENDER-POLICY":
                parent.addModeSenderPolicy(self.getBswModeSenderPolicy(child_element))
            else:
                self.raiseError("Unsupported ModeSenderPolicy type <%s>." % tag_name)

    def readBswInternalTriggeringPoint(
        self, element: ET.Element, point: BswInternalTriggeringPoint
    ):
        """Read BSW internal triggering point."""
        self.readIdentifiable(element, point)

    def readBswInternalBehaviorInternalTriggeringPoints(
        self, element: ET.Element, behavior: BswInternalBehavior
    ):
        """Read BSW internal behavior internal triggering points."""
        for child_element in self.findall(element, "INTERNAL-TRIGGERING-POINTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "BSW-INTERNAL-TRIGGERING-POINT":
                point = behavior.createBswInternalTriggeringPoint(
                    self.getShortName(child_element)
                )
                self.readBswInternalTriggeringPoint(child_element, point)
            else:
                self.notImplemented(
                    "Unsupported Internal Triggering Points <%s>" % tag_name
                )

    def readBswVariableAccess(
        self, element: ET.Element, access: BswVariableAccess
    ):
        """Read BSW variable access."""
        self.readReferrable(element, access)
        access.setAccessedVariableRef(
            self.getChildElementOptionalRefType(element, "ACCESSED-VARIABLE-REF")
        )

    def readBswModuleEntityDataSendPoints(
        self, element: ET.Element, entity: BswModuleEntity
    ):
        """Read BSW module entity data send points."""
        for child_element in self.findall(element, "DATA-SEND-POINTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "BSW-VARIABLE-ACCESS":
                point = entity.createDataSendPoint(self.getShortName(child_element))
                self.readBswVariableAccess(child_element, point)
            else:
                self.notImplemented("Unsupported Data Send Point <%s>" % tag_name)

    def readBswModuleEntityDataReceiverPoints(
        self, element: ET.Element, entity: BswModuleEntity
    ):
        """Read BSW module entity data receiver points."""
        for child_element in self.findall(element, "DATA-RECEIVE-POINTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "BSW-VARIABLE-ACCESS":
                point = entity.createDataReceivePoint(self.getShortName(child_element))
                self.readBswVariableAccess(child_element, point)
            else:
                self.notImplemented("Unsupported Data Receive Point <%s>" % tag_name)

    def readBswModuleEntityIssuedTriggerRefs(
        self, element: ET.Element, entity: BswModuleEntity
    ):
        """Read BSW module entity issued trigger refs."""
        for ref in self.getChildElementRefTypeList(
            element, "ISSUED-TRIGGERS/TRIGGER-REF-CONDITIONAL/TRIGGER-REF"
        ):
            entity.addIssuedTriggerRef(ref)

    def readBswModuleEntityActivationPointRefs(
        self, element: ET.Element, entity: BswModuleEntity
    ):
        """Read BSW module entity activation point refs."""
        for ref in self.getChildElementRefTypeList(
            element,
            "ACTIVATION-POINTS/BSW-INTERNAL-TRIGGERING-POINT-REF-CONDITIONAL/BSW-INTERNAL-TRIGGERING-POINT-REF",
        ):
            entity.addActivationPointRef(ref)

    def readBswModuleCallPoint(self, element: ET.Element, point: BswModuleCallPoint):
        """Read BSW module call point."""
        self.readReferrable(element, point)

    def readBswAsynchronousServerCallPoint(
        self, element: ET.Element, point: BswAsynchronousServerCallPoint
    ):
        """Read BSW asynchronous server call point."""
        self.readBswModuleCallPoint(element, point)
        point.setCalledEntryRef(
            self.getChildElementOptionalRefType(element, "CALLED-ENTRY-REF")
        )

    def readBswSynchronousServerCallPoint(
        self, element: ET.Element, point: BswSynchronousServerCallPoint
    ):
        """Read BSW synchronous server call point."""
        self.readBswModuleCallPoint(element, point)
        point.setCalledEntryRef(
            self.getChildElementOptionalRefType(element, "CALLED-ENTRY-REF")
        )

    def readBswModuleEntityCallPoints(
        self, element: ET.Element, entity: BswModuleEntity
    ):
        """Read BSW module entity call points."""
        for child_element in self.findall(element, "CALL-POINTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "BSW-ASYNCHRONOUS-SERVER-CALL-POINT":
                point = entity.createBswAsynchronousServerCallPoint(
                    self.getShortName(child_element)
                )
                self.readBswAsynchronousServerCallPoint(child_element, point)
            elif tag_name == "BSW-SYNCHRONOUS-SERVER-CALL-POINT":
                point = entity.createBswSynchronousServerCallPoint(
                    self.getShortName(child_element)
                )
                self.readBswSynchronousServerCallPoint(child_element, point)
            else:
                self.notImplemented("Unsupported Call Point <%s>" % tag_name)

    def readBswModuleEntityManagedModeGroups(self, element, entity):
        """Delegate to PortInterfaceParser."""
        if self._main_parser:
            return self._main_parser._port_interface_parser.readBswModuleEntityManagedModeGroups(
                element, entity
            )
        else:
            self.raiseError("PortInterfaceParser not available")

    def readBswModuleEntity(self, element: ET.Element, entity: BswModuleEntity):
        """Read BSW module entity."""
        self.readExecutableEntity(element, entity)
        self.readBswModuleEntityActivationPointRefs(element, entity)
        self.readBswModuleEntityCallPoints(element, entity)
        self.readBswModuleEntityDataReceiverPoints(element, entity)
        self.readBswModuleEntityDataSendPoints(element, entity)
        entity.setImplementedEntryRef(
            self.getChildElementRefType(entity.getShortName(), element, "IMPLEMENTED-ENTRY-REF")
        )
        self.readBswModuleEntityManagedModeGroups(element, entity)
        self.readBswModuleEntityIssuedTriggerRefs(element, entity)

    def readBswCalledEntity(self, element: ET.Element, entity: BswCalledEntity):
        """Read BSW called entity."""
        self.readBswModuleEntity(element, entity)

    def readBswSchedulableEntity(
        self, element: ET.Element, entity: BswSchedulableEntity
    ):
        """Read BSW schedulable entity."""
        self.readBswModuleEntity(element, entity)

    def readBswInterruptEntity(self, element: ET.Element, entity: BswInterruptEntity):
        """Read BSW interrupt entity."""
        self.readBswModuleEntity(element, entity)
        entity.setInterruptCategory(
            self.getChildElementOptionalLiteral(element, "INTERRUPT-CATEGORY")
        ).setInterruptSource(self.getChildElementOptionalLiteral(element, "INTERRUPT-SOURCE"))

    def readBswInternalBehaviorEntities(
        self, element: ET.Element, behavior: BswInternalBehavior
    ):
        """Read BSW internal behavior entities."""
        for child_element in self.findall(element, "ENTITYS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "BSW-CALLED-ENTITY":
                entity = behavior.createBswCalledEntity(self.getShortName(child_element))
                self.readBswCalledEntity(child_element, entity)
            elif tag_name == "BSW-SCHEDULABLE-ENTITY":
                entity = behavior.createBswSchedulableEntity(
                    self.getShortName(child_element)
                )
                self.readBswSchedulableEntity(child_element, entity)
            elif tag_name == "BSW-INTERRUPT-ENTITY":
                entity = behavior.createBswInterruptEntity(self.getShortName(child_element))
                self.readBswInterruptEntity(child_element, entity)
            else:
                self.notImplemented("Unsupported BswModuleEntity <%s>" % tag_name)

    def readBswBackgroundEvent(self, element: ET.Element, event: BswBackgroundEvent):
        """Read BSW background event."""
        self.readBswScheduleEvent(element, event)

    def readBswExternalTriggerOccurredEvent(
        self, element: ET.Element, event: BswExternalTriggerOccurredEvent
    ):
        """Read BSW external trigger occurred event."""
        self.readBswScheduleEvent(element, event)
        event.setTriggerRef(self.getChildElementOptionalRefType(element, "TRIGGER-REF"))

    def readBswOperationInvokedEvent(
        self, element: ET.Element, event: BswOperationInvokedEvent
    ):
        """Read BSW operation invoked event."""
        self.readBswEvent(element, event)
        event.setEntryRef(self.getChildElementOptionalRefType(element, "ENTRY-REF"))

    def readBswInternalBehaviorEvents(
        self, element: ET.Element, behavior: BswInternalBehavior
    ):
        """Read BSW internal behavior events."""
        for child_element in self.findall(element, "EVENTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "BSW-MODE-SWITCH-EVENT":
                event = behavior.createBswModeSwitchEvent(self.getShortName(child_element))
                # Delegate to PortInterfaceParser
                if self._main_parser:
                    self._main_parser._port_interface_parser.readBswModeSwitchEvent(
                        child_element, event
                    )
                else:
                    self.raiseError("PortInterfaceParser not available")
            elif tag_name == "BSW-TIMING-EVENT":
                event = behavior.createBswTimingEvent(self.getShortName(child_element))
                self.readBswTimingEvent(child_element, event)
            elif tag_name == "BSW-DATA-RECEIVED-EVENT":
                event = behavior.createBswDataReceivedEvent(self.getShortName(child_element))
                self.readBswDataReceivedEvent(child_element, event)
            elif tag_name == "BSW-INTERNAL-TRIGGER-OCCURRED-EVENT":
                event = behavior.createBswInternalTriggerOccurredEvent(
                    self.getShortName(child_element)
                )
                self.readBswInternalTriggerOccurredEvent(child_element, event)
            elif tag_name == "BSW-BACKGROUND-EVENT":
                event = behavior.createBswBackgroundEvent(self.getShortName(child_element))
                self.readBswBackgroundEvent(child_element, event)
            elif tag_name == "BSW-EXTERNAL-TRIGGER-OCCURRED-EVENT":
                event = behavior.createBswExternalTriggerOccurredEvent(
                    self.getShortName(child_element)
                )
                self.readBswExternalTriggerOccurredEvent(child_element, event)
            elif tag_name == "BSW-OPERATION-INVOKED-EVENT":
                event = behavior.createBswOperationInvokedEvent(
                    self.getShortName(child_element)
                )
                self.readBswOperationInvokedEvent(child_element, event)
            else:
                self.notImplemented("Unsupported BswModuleEntity <%s>" % tag_name)

    def readBswApiOptions(self, element: ET.Element, options: BswApiOptions):
        """Read BSW API options."""
        self.readARObjectAttributes(element, options)
        options.setEnableTakeAddress(
            self.getChildElementOptionalBooleanValue(element, "ENABLE-TAKE-ADDRESS")
        )

    def readBswDataReceptionPolicy(
        self, element: ET.Element, policy: BswDataReceptionPolicy
    ):
        """Read BSW data reception policy."""
        self.readBswApiOptions(element, policy)
        policy.setReceivedDataRef(
            self.getChildElementOptionalRefType(element, "RECEIVED-DATA-REF")
        )

    def readBswQueuedDataReceptionPolicy(
        self, element: ET.Element, policy: BswQueuedDataReceptionPolicy
    ):
        """Read BSW queued data reception policy."""
        self.readBswDataReceptionPolicy(element, policy)
        policy.setQueueLength(
            self.getChildElementOptionalPositiveInteger(element, "QUEUE-LENGTH")
        )

    def readBswInternalBehaviorReceptionPolicies(
        self, element: ET.Element, behavior: BswInternalBehavior
    ):
        """Read BSW internal behavior reception policies."""
        for child_element in self.findall(element, "RECEPTION-POLICYS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "BSW-QUEUED-DATA-RECEPTION-POLICY":
                policy = BswQueuedDataReceptionPolicy()
                self.readBswQueuedDataReceptionPolicy(child_element, policy)
                behavior.addReceptionPolicy(policy)
            else:
                self.notImplemented("Unsupported Reception Policies <%s>" % tag_name)

    def readBswInternalBehavior(
        self, element: ET.Element, behavior: BswInternalBehavior
    ):
        """Read BSW internal behavior."""
        self.logger.debug("Read BswInternalBehavior <%s>" % behavior.full_name)

        # read the internal behavior
        self.readInternalBehavior(element, behavior)
        self.readBswInternalBehaviorInternalTriggeringPoints(element, behavior)
        self.readBswInternalBehaviorEntities(element, behavior)
        self.readBswInternalBehaviorEvents(element, behavior)
        self.readBswInternalBehaviorModeSenderPolicy(element, behavior)
        for group_set in self.getIncludedModeDeclarationGroupSets(element):
            behavior.addIncludedModeDeclarationGroupSet(group_set)
        self.readBswInternalBehaviorReceptionPolicies(element, behavior)

    # ========================================================================
    # Service Dependencies and Service Needs
    # ========================================================================

    def readServiceDependency(self, element: ET.Element, dependency: ServiceDependency):
        """Read service dependency."""
        self.readIdentifiable(element, dependency)
        for child_element in self.findall(element, "ASSIGNED-DATA-TYPES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ROLE-BASED-DATA-TYPE-ASSIGNMENT":
                dependency.addAssignedDataType(
                    self.getRoleBasedDataTypeAssignment(child_element)
                )
            else:
                self.notImplemented("Unsupported assigned data type <%s>" % tag_name)

    def readSwcServiceDependencyAssignedData(
        self, element: ET.Element, dependency: SwcServiceDependency
    ):
        """Read SWC service dependency assigned data."""
        for child_element in self.findall(element, "ASSIGNED-DATAS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ROLE-BASED-DATA-ASSIGNMENT":
                dependency.AddAssignedData(self.getRoleBasedDataAssignment(child_element))
            else:
                self.raiseError("Unsupported assigned data <%s>" % tag_name)

    def readSwcServiceDependencyAssignedPorts(
        self, element: ET.Element, dependency: SwcServiceDependency
    ):
        """Read SWC service dependency assigned ports."""
        for child_element in self.findall(element, "ASSIGNED-PORTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ROLE-BASED-PORT-ASSIGNMENT":
                dependency.AddAssignedPort(self.getRoleBasedPortAssignment(child_element))
            else:
                self.raiseError("Unsupported assigned ports <%s>" % tag_name)

    def readServiceNeeds(self, element: ET.Element, needs: ServiceNeeds):
        """Read service needs."""
        self.readIdentifiable(element, needs)

    def readNvBlockNeeds(self, element: ET.Element, needs: NvBlockNeeds):
        """Read NV block needs."""
        self.readServiceNeeds(element, needs)
        needs.setCalcRamBlockCrc(
            self.getChildElementOptionalBooleanValue(element, "CALC-RAM-BLOCK-CRC")
        ).setCheckStaticBlockId(
            self.getChildElementOptionalBooleanValue(element, "CHECK-STATIC-BLOCK-ID")
        ).setNDataSets(
            self.getChildElementOptionalNumericalValue(element, "N-DATA-SETS")
        ).setNRomBlocks(
            self.getChildElementOptionalNumericalValue(element, "N-ROM-BLOCKS")
        ).setRamBlockStatusControl(
            self.getChildElementOptionalLiteral(element, "RAM-BLOCK-STATUS-CONTROL")
        ).setReadonly(
            self.getChildElementOptionalBooleanValue(element, "READONLY")
        ).setReliability(
            self.getChildElementOptionalLiteral(element, "RELIABILITY")
        ).setResistantToChangedSw(
            self.getChildElementOptionalBooleanValue(element, "RESISTANT-TO-CHANGED-SW")
        ).setRestoreAtStart(
            self.getChildElementOptionalBooleanValue(element, "RESTORE-AT-START")
        ).setStoreAtShutdown(
            self.getChildElementOptionalBooleanValue(element, "STORE-AT-SHUTDOWN")
        ).setStoreCyclic(
            self.getChildElementOptionalBooleanValue(element, "STORE-CYCLIC")
        ).setStoreEmergency(
            self.getChildElementOptionalBooleanValue(element, "STORE-EMERGENCY")
        ).setStoreImmediate(
            self.getChildElementOptionalBooleanValue(element, "STORE-IMMEDIATE")
        ).setUseAutoValidationAtShutDown(
            self.getChildElementOptionalBooleanValue(element, "USE-AUTO-VALIDATION-AT-SHUT-DOWN")
        ).setUseCRCCompMechanism(
            self.getChildElementOptionalBooleanValue(element, "USE-CRC-COMP-MECHANISM")
        ).setWriteOnlyOnce(
            self.getChildElementOptionalBooleanValue(element, "WRITE-ONLY-ONCE")
        ).setWriteVerification(
            self.getChildElementOptionalBooleanValue(element, "WRITE-VERIFICATION")
        ).setWritingFrequency(
            self.getChildElementOptionalIntegerValue(element, "WRITING-FREQUENCY")
        ).setWritingPriority(
            self.getChildElementOptionalLiteral(element, "WRITING-PRIORITY")
        )

    def readDiagnosticCapabilityElement(
        self, element: ET.Element, needs: DiagnosticCapabilityElement
    ):
        """Read diagnostic capability element."""
        self.readServiceNeeds(element, needs)

    def readDiagnosticCommunicationManagerNeeds(
        self, element: ET.Element, needs: DiagnosticCommunicationManagerNeeds
    ):
        """Read diagnostic communication manager needs."""
        self.readDiagnosticCapabilityElement(element, needs)
        needs.setServiceRequestCallbackType(
            self.getChildElementOptionalLiteral(element, "SERVICE-REQUEST-CALLBACK-TYPE")
        )

    def readDiagnosticRoutineNeeds(self, element: ET.Element, needs: DiagnosticRoutineNeeds):
        """Read diagnostic routine needs."""
        self.readDiagnosticCapabilityElement(element, needs)
        needs.setDiagRoutineType(
            self.getChildElementOptionalLiteral(element, "DIAG-ROUTINE-TYPE")
        ).setRidNumber(self.getChildElementOptionalIntegerValue(element, "RID-NUMBER"))

    def readDiagnosticValueNeeds(self, element: ET.Element, needs: DiagnosticValueNeeds):
        """Read diagnostic value needs."""
        self.readDiagnosticCapabilityElement(element, needs)
        needs.setDataLength(
            self.getChildElementOptionalPositiveInteger(element, "DATA-LENGTH")
        ).setDiagnosticValueAccess(
            self.getChildElementOptionalLiteral(element, "DIAGNOSTIC-VALUE-ACCESS")
        ).setDidNumber(self.getChildElementOptionalIntegerValue(element, "DID-NUMBER")).setFixedLength(
            self.getChildElementOptionalBooleanValue(element, "FIXED-LENGTH")
        ).setProcessingStyle(
            self.getChildElementOptionalLiteral(element, "PROCESSING-STYLE")
        )

    def readDiagEventDebounceMonitorInternal(
        self, element: ET.Element, algorithm: DiagEventDebounceMonitorInternal
    ):
        """Read diagnostic event debounce monitor internal."""
        self.readDiagnosticCapabilityElement(element, algorithm)

    def readDiagEventDebounceAlgorithm(
        self, element: ET.Element, needs: DiagnosticEventNeeds
    ):
        """Read diagnostic event debounce algorithm."""
        for child_element in self.findall(element, "DIAG-EVENT-DEBOUNCE-ALGORITHM/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "DIAG-EVENT-DEBOUNCE-MONITOR-INTERNAL":
                algorithm = needs.createDiagEventDebounceMonitorInternal(
                    self.getShortName(child_element)
                )
                self.readDiagEventDebounceMonitorInternal(child_element, algorithm)
            else:
                self.notImplemented(
                    "Unsupported DiagEventDebounceAlgorithm <%s>" % tag_name
                )

    def readDiagnosticEventNeeds(self, element: ET.Element, needs: DiagnosticEventNeeds):
        """Read diagnostic event needs."""
        self.readDiagnosticCapabilityElement(element, needs)
        self.readDiagEventDebounceAlgorithm(element, needs)
        needs.setDtcKind(self.getChildElementOptionalLiteral(element, "DTC-KIND")).setUdsDtcNumber(
            self.getChildElementOptionalIntegerValue(element, "UDS-DTC-NUMBER")
        )

    def readDiagnosticEventInfoNeeds(
        self, element: ET.Element, needs: DiagnosticEventInfoNeeds
    ):
        """Read diagnostic event info needs."""
        self.readDiagnosticCapabilityElement(element, needs)
        needs.setDtcKind(self.getChildElementOptionalLiteral(element, "DTC-KIND"))
        needs.setUdsDtcNumber(
            self.getChildElementOptionalPositiveInteger(element, "UDS-DTC-NUMBER")
        )

    def readCryptoServiceNeeds(self, element: ET.Element, needs: CryptoServiceNeeds):
        """Read crypto service needs."""
        self.readServiceNeeds(element, needs)
        needs.setMaximumKeyLength(
            self.getChildElementOptionalPositiveInteger(element, "MAXIMUM-KEY-LENGTH")
        )

    def readEcuStateMgrUserNeeds(self, element: ET.Element, needs: EcuStateMgrUserNeeds):
        """Read ECU state manager user needs."""
        self.readServiceNeeds(element, needs)

    def readDtcStatusChangeNotificationNeeds(
        self, element: ET.Element, needs: DtcStatusChangeNotificationNeeds
    ):
        """Read DTC status change notification needs."""
        self.readDiagnosticCapabilityElement(element, needs)
        needs.setDtcFormatType(
            self.getChildElementOptionalLiteral(element, "DTC-FORMAT-TYPE")
        )

    def readDltUserNeeds(self, element: ET.Element, needs: DltUserNeeds):
        """Read DLT user needs."""
        self.readServiceNeeds(element, needs)

    def readSwcServiceDependencyServiceNeeds(
        self, element: ET.Element, parent: SwcServiceDependency
    ):
        """Read SWC service dependency service needs."""
        for child_element in self.findall(element, "SERVICE-NEEDS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "NV-BLOCK-NEEDS":
                needs = parent.createNvBlockNeeds(self.getShortName(child_element))
                self.readNvBlockNeeds(child_element, needs)
            elif tag_name == "DIAGNOSTIC-COMMUNICATION-MANAGER-NEEDS":
                needs = parent.createDiagnosticCommunicationManagerNeeds(
                    self.getShortName(child_element)
                )
                self.readDiagnosticCommunicationManagerNeeds(child_element, needs)
            elif tag_name == "DIAGNOSTIC-ROUTINE-NEEDS":
                needs = parent.createDiagnosticRoutineNeeds(
                    self.getShortName(child_element)
                )
                self.readDiagnosticRoutineNeeds(child_element, needs)
            elif tag_name == "DIAGNOSTIC-VALUE-NEEDS":
                needs = parent.createDiagnosticValueNeeds(self.getShortName(child_element))
                self.readDiagnosticValueNeeds(child_element, needs)
            elif tag_name == "DIAGNOSTIC-EVENT-NEEDS":
                needs = parent.createDiagnosticEventNeeds(self.getShortName(child_element))
                self.readDiagnosticEventNeeds(child_element, needs)
            elif tag_name == "DIAGNOSTIC-EVENT-INFO-NEEDS":
                needs = parent.createDiagnosticEventInfoNeeds(
                    self.getShortName(child_element)
                )
                self.readDiagnosticEventInfoNeeds(child_element, needs)
            elif tag_name == "CRYPTO-SERVICE-NEEDS":
                needs = parent.createCryptoServiceNeeds(self.getShortName(child_element))
                self.readCryptoServiceNeeds(child_element, needs)
            elif tag_name == "ECU-STATE-MGR-USER-NEEDS":
                needs = parent.createEcuStateMgrUserNeeds(self.getShortName(child_element))
                self.readEcuStateMgrUserNeeds(child_element, needs)
            elif tag_name == "DTC-STATUS-CHANGE-NOTIFICATION-NEEDS":
                needs = parent.createDtcStatusChangeNotificationNeeds(
                    self.getShortName(child_element)
                )
                self.readDtcStatusChangeNotificationNeeds(child_element, needs)
            elif tag_name == "DLT-USER-NEEDS":
                needs = parent.createDltUserNeeds(self.getShortName(child_element))
                self.readDltUserNeeds(child_element, needs)
            else:
                self.notImplemented("Unsupported service needs <%s>" % tag_name)

    def readSwcServiceDependency(
        self, element: ET.Element, parent: SwcInternalBehavior
    ):
        """Read SWC service dependency."""
        short_name = self.getShortName(element)
        dependency = parent.createSwcServiceDependency(short_name)
        self.readServiceDependency(element, dependency)
        self.readSwcServiceDependencyAssignedData(element, dependency)
        self.readSwcServiceDependencyAssignedPorts(element, dependency)
        self.readSwcServiceDependencyServiceNeeds(element, dependency)

    def readSwcInternalBehaviorServiceDependencies(
        self, element: ET.Element, parent: SwcInternalBehavior
    ):
        """Read SWC internal behavior service dependencies."""
        for child_element in self.findall(element, "SERVICE-DEPENDENCYS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "SWC-SERVICE-DEPENDENCY":
                self.readSwcServiceDependency(child_element, parent)
            else:
                self.notImplemented("Unsupported Service Dependencies <%s>" % tag_name)

    # ========================================================================
    # Implementation (SwcImplementation, BswImplementation)
    # ========================================================================

    def readArtifactDescriptor(self, element: ET.Element, code):
        """Read artifact descriptor."""
        for child_element in self.findall(element, "ARTIFACT-DESCRIPTORS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "AUTOSAR-ENGINEERING-OBJECT":
                code.addArtifactDescriptor(self.getAutosarEngineeringObject(child_element))
            else:
                self.notImplemented("Unsupported Artifact Descriptor <%s>" % tag_name)

    def readCodeDescriptor(self, element: ET.Element, impl: Implementation):
        """Read code descriptor."""
        for child_element in self.findall(element, "CODE-DESCRIPTORS/CODE"):
            short_name = self.getShortName(child_element)
            code_desc = impl.createCodeDescriptor(short_name)
            self.readIdentifiable(child_element, code_desc)
            self.readArtifactDescriptor(child_element, code_desc)

    def readMemorySectionOptions(self, element: ET.Element, section: MemorySection):
        """Read memory section options."""
        child_element = self.find(element, "OPTIONS")
        if child_element is not None:
            for value in self.getChildElementLiteralValueList(child_element, "OPTION"):
                section.addOption(value)

    def readMemorySections(self, element: ET.Element, consumption: ResourceConsumption):
        """Read memory sections."""
        for child_element in self.findall(element, "MEMORY-SECTIONS/MEMORY-SECTION"):
            memory_section = consumption.createMemorySection(self.getShortName(child_element))
            self.readIdentifiable(child_element, memory_section)
            memory_section.setAlignment(
                self.getChildElementOptionalLiteral(child_element, "ALIGNMENT")
            ).setMemClassSymbol(
                self.getChildElementOptionalLiteral(child_element, "MEM-CLASS-SYMBOL")
            )
            self.readMemorySectionOptions(child_element, memory_section)
            memory_section.setSize(
                self.getChildElementOptionalNumericalValue(child_element, "SIZE")
            ).setSwAddrMethodRef(
                self.getChildElementOptionalRefType(child_element, "SW-ADDRMETHOD-REF")
            ).setSymbol(self.getChildElementOptionalLiteral(child_element, "SYMBOL"))

    def readStackUsage(self, element: ET.Element, usage: StackUsage):
        """Read stack usage."""
        self.logger.debug("read StackUsage %s" % usage.getShortName())
        self.readIdentifiable(element, usage)

    def readRoughEstimateStackUsage(
        self, element: ET.Element, usage: RoughEstimateStackUsage
    ):
        """Read rough estimate stack usage."""
        self.readStackUsage(element, usage)
        usage.setMemoryConsumption(
            self.getChildElementOptionalPositiveInteger(element, "MEMORY-CONSUMPTION")
        )

    def readStackUsages(self, element: ET.Element, consumption: ResourceConsumption):
        """Read stack usages."""
        for child_element in self.findall(element, "STACK-USAGES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ROUGH-ESTIMATE-STACK-USAGE":
                usage = consumption.createRoughEstimateStackUsage(
                    self.getShortName(child_element)
                )
                self.readRoughEstimateStackUsage(child_element, usage)
            else:
                self.notImplemented("Unsupported Stack Usages: <%s>" % tag_name)

    def readResourceConsumption(self, element: ET.Element, impl: Implementation):
        """Read resource consumption."""
        child_element = self.find(element, "RESOURCE-CONSUMPTION")
        if child_element is not None:
            consumption = impl.createResourceConsumption(self.getShortName(child_element))
            self.readIdentifiable(child_element, consumption)
            self.readMemorySections(child_element, consumption)
            self.readStackUsages(child_element, consumption)

    def readImplementation(self, element: ET.Element, impl: Implementation):
        """Read implementation."""
        self.readIdentifiable(element, impl)
        self.readCodeDescriptor(element, impl)
        impl.setProgrammingLanguage(
            self.getChildElementOptionalLiteral(element, "PROGRAMMING-LANGUAGE")
        )
        self.readResourceConsumption(element, impl)
        impl.setSwVersion(self.getChildElementOptionalLiteral(element, "SW-VERSION")).setSwcBswMappingRef(
            self.getChildElementOptionalRefType(element, "SWC-BSW-MAPPING-REF")
        ).setUsedCodeGenerator(
            self.getChildElementOptionalLiteral(element, "USED-CODE-GENERATOR")
        ).setVendorId(self.getChildElementOptionalNumericalValue(element, "VENDOR-ID"))

    def readSwcImplementation(self, element: ET.Element, impl: SwcImplementation):
        """Read SWC implementation."""
        self.logger.debug("Read SwcImplementation <%s>" % impl.getShortName())
        self.readImplementation(element, impl)
        impl.setBehaviorRef(self.getChildElementOptionalRefType(element, "BEHAVIOR-REF"))
        AUTOSAR.getInstance().addImplementationBehaviorMap(
            impl.getFullName(), impl.getBehaviorRef().getValue()
        )

    def readBswImplementationVendorSpecificModuleDefRefs(
        self, element: ET.Element, impl: BswImplementation
    ):
        """Read BSW implementation vendor specific module def refs."""
        child_element = self.find(element, "VENDOR-SPECIFIC-MODULE-DEF-REFS")
        if child_element is not None:
            for ref in self.getChildElementRefTypeList(
                child_element, "VENDOR-SPECIFIC-MODULE-DEF-REF"
            ):
                impl.addVendorSpecificModuleDefRef(ref)

    def readBswImplementation(self, element: ET.Element, impl: BswImplementation):
        """Read BSW implementation."""
        self.logger.debug("Read BswImplementation <%s>" % impl.getShortName())
        self.readImplementation(element, impl)
        impl.setArReleaseVersion(
            self.getChildElementOptionalLiteral(element, "AR-RELEASE-VERSION")
        ).setBehaviorRef(self.getChildElementOptionalRefType(element, "BEHAVIOR-REF")).setVendorApiInfix(
            self.getChildElementOptionalLiteral(element, "VENDOR-API-INFIX")
        )
        self.readBswImplementationVendorSpecificModuleDefRefs(element, impl)
        AUTOSAR.getInstance().addImplementationBehaviorMap(
            impl.getFullName(), impl.getBehaviorRef().getValue()
        )

    # ========================================================================
    # SwcBswMapping
    # ========================================================================

    def readSwcBswMappingSwcBswRunnableMappings(
        self, element: ET.Element, parent: SwcBswMapping
    ):
        """Read SWC BSW mapping runnable mappings."""
        for child_element in self.findall(
            element, "RUNNABLE-MAPPINGS/SWC-BSW-RUNNABLE-MAPPING"
        ):
            mapping = SwcBswRunnableMapping()
            mapping.setBswEntityRef(
                self.getChildElementOptionalRefType(child_element, "BSW-ENTITY-REF")
            ).setSwcRunnableRef(
                self.getChildElementOptionalRefType(child_element, "SWC-RUNNABLE-REF")
            )
            parent.addRunnableMapping(mapping)

    def readSwcBswMapping(self, element: ET.Element, mapping: SwcBswMapping):
        """Read SWC BSW mapping."""
        self.logger.debug("Read SwcBswMapping <%s>" % mapping.getShortName())
        self.readIdentifiable(element, mapping)
        mapping.setBswBehaviorRef(
            self.getChildElementOptionalRefType(element, "BSW-BEHAVIOR-REF")
        )
        self.readSwcBswMappingSwcBswRunnableMappings(element, mapping)
        mapping.setSwcBehaviorRef(
            self.getChildElementOptionalRefType(element, "SWC-BEHAVIOR-REF")
        )

    # ========================================================================
    # Data Prototype Methods
    # ========================================================================

    def readVariableDataPrototype(
        self, element: ET.Element, prototype: VariableDataPrototype
    ):
        """Read variable data prototype."""
        self.readAutosarDataPrototype(element, prototype)
        # Delegate to DataTypeParser for init value
        if self._main_parser:
            prototype.setInitValue(
                self._main_parser._datatype_parser.getInitValue(element)
            )
        else:
            self.notImplemented("DataTypeParser not available for InitValue")

    def readAutosarDataPrototype(
        self, element: ET.Element, prototype: AutosarDataPrototype
    ):
        """Read autosar data prototype."""
        # Delegate to DataTypeParser for DataPrototype
        if self._main_parser:
            self._main_parser._datatype_parser.readDataPrototype(element, prototype)
        else:
            self.notImplemented("DataTypeParser not available for DataPrototype")
        prototype.setTypeTRef(self.getChildElementOptionalRefType(element, "TYPE-TREF"))

    # ========================================================================
    # BSW Module Description Methods
    # ========================================================================

    def readBswModuleDescriptionImplementedEntryRefs(
        self, element: ET.Element, parent: BswModuleDescription
    ):
        """Read BSW module description implemented entry refs."""
        for child_element in self.findall(
            element, "PROVIDED-ENTRYS/BSW-MODULE-ENTRY-REF-CONDITIONAL"
        ):
            ref = self.getChildElementOptionalRefType(child_element, "BSW-MODULE-ENTRY-REF")
            if ref is not None:
                parent.addImplementedEntryRef(ref)

    def readBswModuleClientServerEntry(
        self, element: ET.Element, entry: BswModuleClientServerEntry
    ):
        """Read BSW module client server entry."""
        self.readReferrable(element, entry)
        entry.setEncapsulatedEntryRef(
            self.getChildElementOptionalRefType(element, "ENCAPSULATED-ENTRY-REF")
        ).setIsReentrant(self.getChildElementOptionalBooleanValue(element, "IS-REENTRANT")).setIsSynchronous(
            self.getChildElementOptionalBooleanValue(element, "IS-SYNCHRONOUS")
        )

    def readTrigger(self, element: ET.Element, trigger: Trigger):
        """Read trigger."""
        self.readIdentifiable(element, trigger)

    def readBswModuleDescriptionReleasedTriggers(
        self, element: ET.Element, desc: BswModuleDescription
    ):
        """Read BSW module description released triggers."""
        for child_element in self.findall(element, "RELEASED-TRIGGERS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "TRIGGER":
                trigger = desc.createReleasedTrigger(self.getShortName(child_element))
                self.readTrigger(child_element, trigger)
            else:
                self.notImplemented("Unsupported Released Trigger <%s>" % tag_name)

    def readBswModuleDescriptionRequiredTriggers(
        self, element: ET.Element, desc: BswModuleDescription
    ):
        """Read BSW module description required triggers."""
        for child_element in self.findall(element, "REQUIRED-TRIGGERS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "TRIGGER":
                trigger = desc.createRequiredTrigger(self.getShortName(child_element))
                self.readTrigger(child_element, trigger)
            else:
                self.notImplemented("Unsupported Required Trigger <%s>" % tag_name)

    # ========================================================================
    # Helper Methods for Engineering Objects (delegated to main parser)
    # ========================================================================

    def getAutosarEngineeringObject(self, element: ET.Element):
        """Get autosar engineering object - delegate to main parser."""
        if self._main_parser:
            return self._main_parser.getAutosarEngineeringObject(element)
        else:
            self.raiseError("Main parser not available for getAutosarEngineeringObject")
            return None
