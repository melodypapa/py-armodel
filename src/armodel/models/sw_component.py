from typing import List
from abc import ABCMeta

from .m2.autosar_templates.sw_component_template.components.instance_refs import RModeInAtomicSwcInstanceRef, RVariableInAtomicSwcInstanceRef
from .m2.autosar_templates.sw_component_template.swc_internal_behavior import RunnableEntity
from .internal_behavior import IncludedDataTypeSet, InternalBehavior
from .service_mapping import RoleBasedPortAssignment
from .per_instance_memory import PerInstanceMemory
from .service_needs import NvBlockNeeds, RoleBasedDataAssignment, ServiceNeeds
from .ar_object import ARBoolean, ARLiteral
from .general_structure import ARElement, Identifiable, ARObject
from .ar_ref import InnerPortGroupInCompositionInstanceRef, POperationInAtomicSwcInstanceRef, TRefType
from .ar_ref import RefType, PortInCompositionTypeInstanceRef, PPortInCompositionInstanceRef, RPortInCompositionInstanceRef
from .port_prototype import RPortPrototype, PPortPrototype, PortPrototype
from .data_prototype import ParameterDataPrototype, VariableDataPrototype
from .m2.autosar_templates.common_structure import ValueSpecification

class AbstractEvent(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

class RTEEvent(AbstractEvent):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.start_on_event_ref = None      # type: RefType
        self.disabled_mode_irefs = []       # type: List[RModeInAtomicSwcInstanceRef]

    def addDisabledModeIRef(self, iref: RModeInAtomicSwcInstanceRef):
        self.disabled_mode_irefs.append(iref)

    def getDisabledModeIRefs(self) -> List[RModeInAtomicSwcInstanceRef]:
        return self.disabled_mode_irefs

class AsynchronousServerCallReturnsEvent(RTEEvent):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

class DataSendCompletedEvent(RTEEvent):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

class DataWriteCompletedEvent(RTEEvent):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

class DataReceivedEvent(RTEEvent):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.dataIRef = None                   # type: RVariableInAtomicSwcInstanceRef

    def getDataIRef(self):
        return self.dataIRef

    def setDataIRef(self, value):
        self.dataIRef = value
        return self

class SwcModeSwitchEvent(RTEEvent):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self._activation = None             # type: ARLiteral
        self.mode_irefs = []                # type: List[RModeInAtomicSwcInstanceRef]

    def addModeIRef(self, iref: RModeInAtomicSwcInstanceRef):
        self.mode_irefs.append(iref)

    def getModeIRefs(self) -> List[RModeInAtomicSwcInstanceRef]:
        return self.mode_irefs

    @property
    def activation(self) -> ARLiteral:
        return self._activation

    @activation.setter
    def activation(self, value: ARLiteral):
        if value.getValue() not in ("ON-ENTRY", "ON-EXIT", "ON-TRANSITION"):
            raise ValueError("Invalid activation <%s> of SwcModeSwitchEvent <%s>" % (value, self.short_name))
        self._activation = value

    def addModeIRef(self, mode_iref: RModeInAtomicSwcInstanceRef):
        self.mode_irefs.append(mode_iref)

class DataReceiveErrorEvent(RTEEvent):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.variable_data_prototype_iref = None    

class OperationInvokedEvent(RTEEvent):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
        self.operation_iref = None      # type: POperationInAtomicSwcInstanceRef

    @property
    def operationIRef(self) -> POperationInAtomicSwcInstanceRef:
        return self.operation_iref
    
    @operationIRef.setter
    def operationIRef(self, value: POperationInAtomicSwcInstanceRef):
        self.operation_iref = value

class InitEvent(RTEEvent):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

class TimingEvent(RTEEvent):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
        self.offset = None
        self.period = 0
    
    @property
    def period_ms(self):
        if (self.period < 0.001):
            return self.period * 1000
        else:
            return (int)(self.period * 1000)

class InternalTriggerOccurredEvent(RTEEvent):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.event_source_ref = None    # type: RefType  

class PortDefinedArgumentValue(ARObject):
    def __init__(self):
        super().__init__()

        self.value = None                   # type: ValueSpecification
        self.value_type = None              # type: TRefType
            
class PortAPIOption(ARObject):
    def __init__(self):
        super().__init__()

        self.enable_take_address = None     # type: ARBoolean
        self.indirect_api = None            # type: ARBoolean
        self.port_ref = None                # type: RefType
        self._port_arg_values = []          # type: List[PortDefinedArgumentValue]

    def addPortArgValue(self, value:PortDefinedArgumentValue):
        self._port_arg_values.append(value)

    def getPortArgValues(self) -> List[PortDefinedArgumentValue]:
        return self._port_arg_values

class ServiceDependency(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

class SwcServiceDependency(ServiceDependency):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self._assigned_data = []
        self._assigned_ports = []
        
    def AddAssignedData(self, data: RoleBasedDataAssignment):
        self._assigned_data.append(data)

    def getAssignedData(self) -> List[RoleBasedDataAssignment]:
        return self._assigned_data

    def AddAssignedPort(self, data: RoleBasedPortAssignment):
        self._assigned_ports.append(data)

    def getAssignedPorts(self) -> List[RoleBasedPortAssignment]:
        return self._assigned_ports
    
    def createNvBlockNeeds(self, short_name: str) -> NvBlockNeeds:
        if (short_name not in self.elements):
            event = NvBlockNeeds(self, short_name)
            self.elements[short_name] = event
        return self.elements[short_name]
    
    def getNvBlockNeeds(self) -> List[NvBlockNeeds]:
        return sorted(filter(lambda c: isinstance(c, NvBlockNeeds), self.elements.values()), key=lambda e: e.short_name)

    def getServiceNeeds(self) -> List[ServiceNeeds]:
        return sorted(filter(lambda c: isinstance(c, ServiceNeeds), self.elements.values()), key=lambda e: e.short_name)
    
class SwcInternalBehavior(InternalBehavior):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.handle_termination_and_restart = None      # type: str
        self.supports_multiple_instantiation = None     # type: ARBoolean
        self.explicit_inter_runnable_variables = []     # type: List[VariableDataPrototype]
        self.implicit_inter_runnable_variables = []     # type: List[VariableDataPrototype]
        self.per_instance_memories = []                 # type: List[PerInstanceMemory]
        self.per_instance_parameters = []               # type: List[ParameterDataPrototype]
        self.port_api_options = []                      # type: List[PortAPIOption]
        self.included_data_type_sets = []               # type: List[IncludedDataTypeSet]

    def getExplicitInterRunnableVariables(self) -> List[VariableDataPrototype]:
        return self.explicit_inter_runnable_variables
    
    def getImplicitInterRunnableVariables(self) -> List[VariableDataPrototype]:
        return self.implicit_inter_runnable_variables
    
    def getPerInstanceMemories(self) -> List[PerInstanceMemory]:
        return self.per_instance_memories
    
    def getPerInstanceParameters(self) -> List[ParameterDataPrototype]:
        return self.per_instance_parameters
    
    def addPortAPIOption(self, option: PortAPIOption):
        self.port_api_options.append(option)

    def getPortAPIOptions(self) -> List[PortAPIOption]:
        return self.port_api_options
    
    def addIncludedDataTypeSet(self, set: IncludedDataTypeSet):
        self.included_data_type_sets.append(set)

    def getIncludedDataTypeSets(self) -> List[IncludedDataTypeSet]:
        return self.included_data_type_sets
    
    def createOperationInvokedEvent(self, short_name: str) -> OperationInvokedEvent:
        if (short_name not in self.elements):
            event = OperationInvokedEvent(self, short_name)
            self.elements[short_name] = event
        return self.elements[short_name]

    def createTimingEvent(self, short_name: str) -> TimingEvent:
        if (short_name not in self.elements):
            event = TimingEvent(self, short_name)
            self.elements[short_name] = event
        return self.elements[short_name]

    def createInitEvent(self, short_name: str) -> InitEvent:
        if (short_name not in self.elements):
            event = InitEvent(self, short_name)
            self.elements[short_name] = event
        return self.elements[short_name]

    def createDataReceivedEvent(self, short_name: str) -> DataReceivedEvent:
        if (short_name not in self.elements):
            event = DataReceivedEvent(self, short_name)
            self.elements[short_name] = event
        return self.elements[short_name]

    def createSwcModeSwitchEvent(self, short_name: str) -> SwcModeSwitchEvent:
        if (short_name not in self.elements):
            event = SwcModeSwitchEvent(self, short_name)
            self.elements[short_name] = event
        return self.elements[short_name]

    def createInternalTriggerOccurredEvent(self, short_name: str) -> InternalTriggerOccurredEvent:
        if (short_name not in self.elements):
            event = InternalTriggerOccurredEvent(self, short_name)
            self.elements[short_name] = event
        return self.elements[short_name]
    
    def createSwcServiceDependency(self, short_name: str) -> SwcServiceDependency:
        if (short_name not in self.elements):
            event = SwcServiceDependency(self, short_name)
            self.elements[short_name] = event
        return self.elements[short_name]

    def getRteEvents(self) -> List[RTEEvent]:
        return sorted(filter(lambda c: isinstance(c, RTEEvent), self.elements.values()), key=lambda e: e.short_name)

    def getOperationInvokedEvents(self) -> List[OperationInvokedEvent]:
        return sorted(filter(lambda c: isinstance(c, OperationInvokedEvent), self.elements.values()), key=lambda e: e.short_name)

    def getInitEvents(self) -> List[InitEvent]:
        return sorted(filter(lambda c: isinstance(c, InitEvent), self.elements.values()), key=lambda e: e.short_name)

    def getTimingEvents(self) -> List[TimingEvent]:
        return sorted(filter(lambda c: isinstance(c, TimingEvent), self.elements.values()), key=lambda e: e.short_name)

    def getDataReceivedEvents(self) -> List[DataReceivedEvent]:
        return sorted(filter(lambda c: isinstance(c, DataReceivedEvent), self.elements.values()), key=lambda e: e.short_name)

    def getSwcModeSwitchEvents(self) -> List[SwcModeSwitchEvent]:
        return sorted(filter(lambda c: isinstance(c, SwcModeSwitchEvent), self.elements.values()), key=lambda e: e.short_name)

    def getInternalTriggerOccurredEvents(self) -> List[InternalTriggerOccurredEvent]:
        return sorted(filter(lambda c: isinstance(c, InternalTriggerOccurredEvent), self.elements.values()), key= lambda e: e.short_name)
    
    def getSwcServiceDependencies(self) -> List[SwcServiceDependency]:
        return sorted(filter(lambda c: isinstance(c, SwcServiceDependency), self.elements.values()), key= lambda e: e.short_name)
    
    def getEvent(self, short_name: str) -> RTEEvent:
        if (not isinstance(self.elements[short_name], RTEEvent)):
            raise ValueError("Invalid Event Type <%s> of <%s>" % type(self.elements[short_name]), short_name)
        return self.elements[short_name]

    def createExplicitInterRunnableVariable(self, short_name: str) -> VariableDataPrototype:
        if (short_name not in self.elements):
            prototype = VariableDataPrototype(self, short_name)
            self.elements[short_name] = prototype
            self.explicit_inter_runnable_variables.append(prototype)
        return self.elements[short_name]
    
    def createImplicitInterRunnableVariable(self, short_name: str) -> VariableDataPrototype:
        if (short_name not in self.elements):
            prototype = VariableDataPrototype(self, short_name)
            self.elements[short_name] = prototype
            self.implicit_inter_runnable_variables.append(prototype)
        return self.elements[short_name]
    
    def createPerInstanceMemory(self, short_name: str) -> PerInstanceMemory:
        if (short_name not in self.elements):
            memory = PerInstanceMemory(self, short_name)
            self.elements[short_name] = memory
            self.per_instance_memories.append(memory)
        return self.elements[short_name]
    
    def createPerInstanceParameter(self, short_name: str) -> ParameterDataPrototype:
        if (short_name not in self.elements):
            prototype = ParameterDataPrototype(self, short_name)
            self.elements[short_name] = prototype
            self.per_instance_parameters.append(prototype)
        return self.elements[short_name]

    def getVariableDataPrototypes(self) -> List[VariableDataPrototype]:
        return sorted(filter(lambda c: isinstance(c, VariableDataPrototype), self.elements.values()), key=lambda e: e.short_name)

    def createRunnableEntity(self, short_name: str) -> RunnableEntity:
        if (short_name not in self.elements):
            runnable = RunnableEntity(self, short_name)
            self.elements[short_name] = runnable
        return self.elements[short_name]

    def getRunnableEntities(self) -> List[RunnableEntity]:
        return sorted(filter(lambda c: isinstance(c, RunnableEntity), self.elements.values()), key=lambda r: r.short_name)
    
    def getRunnableEntity(self, short_name) -> RunnableEntity:
        return self.elements[short_name]
    
class PortGroup(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self._inner_group_iref = []    # type: List[InnerPortGroupInCompositionInstanceRef]
        self._outer_port_ref = []      # type: List[RefType]

    def addInnerGroupIRef(self, iref: InnerPortGroupInCompositionInstanceRef):
        self._inner_group_iref.append(iref)

    def getInnerGroupIRefs(self) -> List[InnerPortGroupInCompositionInstanceRef]:
        return self._inner_group_iref
    
    def addOuterPortRef(self, ref: RefType):
        self._outer_port_ref.append(ref)

    def getOuterPortRefs(self) -> List[RefType]:
        return self._outer_port_ref

class SwComponentType(ARElement):
    __metaclass__ = ABCMeta

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

    def createPPortPrototype(self, short_name: str) -> PPortPrototype:
        prototype = PPortPrototype(self, short_name)
        if (short_name not in self.elements):
            self.elements[short_name] = prototype
        return self.elements[short_name]

    def createRPortPrototype(self, short_name) -> RPortPrototype:
        prototype = RPortPrototype(self, short_name)
        if (short_name not in self.elements):
            self.elements[short_name] = prototype
        return self.elements[short_name]
    
    def createPortGroup(self, short_name) -> PortGroup:
        port_group = PortGroup(self, short_name)
        if (short_name not in self.elements):
            self.elements[short_name] = port_group
        return self.elements[short_name]

    def getPPortPrototypes(self) -> List[PPortPrototype]:
        return list(sorted(filter(lambda c: isinstance(c, PPortPrototype), self.elements.values()), key= lambda o: o.short_name))

    def getRPortPrototypes(self) -> List[RPortPrototype]:
        return list(sorted(filter(lambda c: isinstance(c, RPortPrototype), self.elements.values()), key= lambda o: o.short_name))
    
    def getPortPrototypes(self) -> List[PortPrototype]:
        return list(sorted(filter(lambda c: isinstance(c, PortPrototype), self.elements.values()), key= lambda o: o.short_name))
    
    def getPortGroups(self) -> List[PortGroup]:
        return list(sorted(filter(lambda c: isinstance(c, PortGroup), self.elements.values()), key= lambda o: o.short_name))

class AtomicSwComponentType(SwComponentType):
    __metaclass__ = ABCMeta

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

    def createSwcInternalBehavior(self, short_name) -> SwcInternalBehavior:
        if (short_name not in self.elements):
            if (len(list(filter(lambda e: isinstance(e, SwcInternalBehavior), self.elements.values()))) >= 1):
                raise ValueError("The internal behavior of <%s> can not more than 1" % self.short_name)
            behavior = SwcInternalBehavior(self, short_name)
            self.elements[short_name] = behavior
        return self.elements[short_name]

    @property
    def internal_behavior(self) -> SwcInternalBehavior:
        return next(filter(lambda e: isinstance(e, SwcInternalBehavior), self.elements.values()))

class EcuAbstractionSwComponentType(AtomicSwComponentType):
    def __init__(self, parent:ARObject, short_name: str):
        super().__init__(parent, short_name)

class ApplicationSwComponentType(AtomicSwComponentType):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

class ComplexDeviceDriverSwComponentType(AtomicSwComponentType):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

class NvBlockSwComponentType(AtomicSwComponentType):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

class SensorActuatorSwComponentType(AtomicSwComponentType):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

class ServiceProxySwComponentType(AtomicSwComponentType):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

class ServiceSwComponentType(AtomicSwComponentType):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

class SwConnector(Identifiable):
    __metaclass__ = ABCMeta

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.mapping_ref = None     # type: RefType

class AssemblySwConnector(SwConnector):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.provider_iref = None   # type: PPortInCompositionInstanceRef
        self.requester_iref = None  # type: RPortInCompositionInstanceRef

class DelegationSwConnector(SwConnector):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.inner_port_iref = None # type: PortInCompositionTypeInstanceRef
        self.outer_port_ref  = None # type: RefType

class PassThroughSwConnector(SwConnector):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.provided_outer_port_ref = None # type: RefType
        self.required_outer_port_ref = None # type: RefType

class SwComponentPrototype(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.type_tref = RefType()

class CompositionSwComponentType(SwComponentType):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.constant_value_mapping_refs = []   # type: List[RefType]
        self._data_type_mapping_refs = []       # type: List[RefType]
        self.instantiation_rte_event_props = [] # type: List[InstantiationRTEEventProps]

    def removeAllAssemblySwConnector(self):
        for sw_connector in self.getAssemblySwConnectors():
            self.elements.pop(sw_connector.short_name)

    def removeAllDelegationSwConnector(self):
        for sw_connector in self.getDelegationSwConnectors():
            self.elements.pop(sw_connector.short_name)

    def createAssemblySwConnector(self, short_name: str) -> AssemblySwConnector:
        if (short_name not in self.elements):
            connector = AssemblySwConnector(self, short_name)
            self.elements[short_name] = connector
        return self.elements[short_name]
    
    def createDelegationSwConnector(self, short_name: str) -> DelegationSwConnector:
        if short_name not in self.elements:
            connector = DelegationSwConnector(self, short_name)
            self.elements[short_name] = connector
        return self.elements[short_name]

    def getAssemblySwConnectors(self) -> List[AssemblySwConnector]:
        return list(sorted(filter(lambda e: isinstance(e, AssemblySwConnector), self.elements.values()), key = lambda c: c.short_name))
    
    def getDelegationSwConnectors(self) -> List[DelegationSwConnector]:
        return list(sorted(filter(lambda e: isinstance(e, DelegationSwConnector), self.elements.values()), key = lambda c: c.short_name))
    
    def getSwConnectors(self) -> List[SwConnector]:
        return list(sorted(filter(lambda e: isinstance(e, SwConnector), self.elements.values()), key = lambda c: c.short_name))
    
    def createSwComponentPrototype(self, short_name: str) -> SwComponentPrototype:
        if (short_name not in self.elements):
            connector = SwComponentPrototype(self, short_name)
            self.elements[short_name] = connector
        return self.elements[short_name] 

    def getSwComponentPrototypes(self) -> List[SwComponentPrototype]:
        return list(filter(lambda e: isinstance(e, SwComponentPrototype), self.elements.values()))
    
    def addDataTypeMapping(self, data_type_mapping_ref: RefType):
        self._data_type_mapping_refs.append(data_type_mapping_ref)

    def getDataTypeMappings(self) -> List[RefType]:
        return self._data_type_mapping_refs