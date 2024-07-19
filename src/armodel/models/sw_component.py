from typing import List, Dict
from abc import ABCMeta

from .service_mapping import RoleBasedPortAssignment
from .per_instance_memory import PerInstanceMemory
from .service_needs import NvBlockNeeds, RoleBasedDataAssignment, ServiceNeeds
from .ar_object import ARBoolean
from .general_structure import ARElement, Identifiable, ARObject
from .ar_ref import AutosarParameterRef, AutosarVariableRef, InnerPortGroupInCompositionInstanceRef, ParameterInAtomicSWCTypeInstanceRef,  POperationInAtomicSwcInstanceRef, ROperationInAtomicSwcInstanceRef, TRefType
from .ar_ref import RefType, PortInCompositionTypeInstanceRef, PPortInCompositionInstanceRef, RPortInCompositionInstanceRef
from .ar_ref import RVariableInAtomicSwcInstanceRef, RModeInAtomicSwcInstanceRef
from .port_prototype import RPortPrototype, PPortPrototype, PortPrototype
from .data_prototype import ParameterDataPrototype, VariableDataPrototype
from .common_structure import ExecutableEntity, InternalBehavior, ValueSpecification

class VariableAccess(Identifiable):
    def __init__(self, parent: ARObject, short_name):
        super().__init__(parent, short_name)
        self.accessed_variable_ref = AutosarVariableRef()
        self.accessed_variable_ref.parent = self
        self.parent = parent
        self.local_variable_ref = None  # type: RefType

class AbstractAccessPoint(Identifiable):
    __metaclass__ = ABCMeta

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == AbstractAccessPoint:
            raise NotImplementedError("ARObject is an abstract class.")
        
        super().__init__(parent, short_name)

        self.return_value_provision = None  

class ParameterAccess(AbstractAccessPoint):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.accessed_parameter = None  # type: AutosarParameterRef
        self.sw_data_def_props = None   #   

class ServerCallPoint(AbstractAccessPoint):
    __metaclass__ = ABCMeta

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
        self.operation_iref = None  # type: ROperationInAtomicSwcInstanceRef
        self.timeout = None         # type: float

class SynchronousServerCallPoint(ServerCallPoint):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.called_from_within_exclusive_area_ref = None # Type: RefType

class AsynchronousServerCallPoint(ServerCallPoint):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

class AsynchronousServerCallResultPoint(ServerCallPoint):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.asynchronous_server_call_point_ref = None # Type:RefType

class InternalTriggeringPoint(AbstractAccessPoint):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name) 

        self.sw_impl_policy = None

class RunnableEntity(ExecutableEntity):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
        self.can_be_invoked_concurrently = None         # Type: ARBoolean
        self.data_read_accesses = {}                    # Type: Dict[str, VariableAccess]
        self.data_received_point_by_arguments = {}      # Type: Dict[str, VariableAccess]
        self.data_received_point_by_values = {}         # Type: Dict[str, VariableAccess]
        self.data_send_points = {}                      # Type: Dict[str, VariableAccess]
        self.data_write_accesses = {}                   # Type: Dict[str, VariableAccess]
        self.written_local_variables = {}               # Type: Dict[str, VariableAccess]
        self.read_local_variables = {}                  # Type: Dict[str, VariableAccess]
        self.external_triggering_points = {}            # Type: Dict[InternalTriggeringPoint]
        self.internal_triggering_points = {}
        self.mode_access_points = {}
        self.mode_switch_points = {}
        self.parameter_accesses = {}                    # Type: Dict[str, ParameterAccess]
        self.server_call_points = {}                    # Type: Dict[str, ServerCallPoint]
        self.wait_points = {}                           # Type: Dict[str, WaitPoint]
        self.symbol = ""

    def _createVariableAccess(self, short_name, variable_accesses: Dict[str, VariableAccess]):
        if (short_name not in variable_accesses):
            variable_access = VariableAccess(self, short_name)
            variable_accesses[short_name] = variable_access
        return variable_accesses[short_name]

    def createDataReadAccess(self, short_name: str) -> VariableAccess:
       return self._createVariableAccess(short_name, self.data_read_accesses)

    def getDataReadAccesses(self) -> List[VariableAccess]:
        return sorted(self.data_read_accesses.values(), key=lambda v: v.short_name)
    
    def createDataWriteAccess(self, short_name: str) -> VariableAccess:
       return self._createVariableAccess(short_name, self.data_write_accesses)

    def getDataWriteAccesses(self) -> List[VariableAccess]:
        return sorted(self.data_write_accesses.values(), key=lambda v: v.short_name)

    def createDataReceivePointByArgument(self, short_name: str) -> VariableAccess:
       return self._createVariableAccess(short_name, self.data_received_point_by_arguments)

    def getDataReceivePointByArguments(self) -> List[VariableAccess]:
        return sorted(self.data_received_point_by_arguments.values(), key=lambda v: v.short_name)

    def createDataReceivePointByValue(self, short_name: str) -> VariableAccess:
       return self._createVariableAccess(short_name, self.data_received_point_by_values)

    def getDataReceivePointByValues(self) -> List[VariableAccess]:
        return sorted(self.data_received_point_by_values.values(), key=lambda v: v.short_name)

    def createDataSendPoint(self, short_name: str) -> VariableAccess:
        return self._createVariableAccess(short_name, self.data_send_points)

    def getDataSendPoints(self) -> List[VariableAccess]:
        return sorted(self.data_send_points.values(), key=lambda v: v.short_name)

    def createReadLocalVariable(self, short_name: str) -> VariableAccess:
        return self._createVariableAccess(short_name, self.read_local_variables)

    def getReadLocalVariables(self) -> List[VariableAccess]:
        return sorted(self.read_local_variables.values(), key=lambda v: v.short_name)

    def createWrittenLocalVariable(self, short_name: str) -> VariableAccess:
        return self._createVariableAccess(short_name, self.written_local_variables)

    def getWrittenLocalVariables(self) -> List[VariableAccess]:
        return sorted(self.written_local_variables.values(), key=lambda v: v.short_name)
    
    def createParameterAccess(self, short_name: str) -> ParameterAccess:
        if (short_name not in self.server_call_points):
            parameter_access = ParameterAccess(self, short_name)
            self.parameter_accesses[short_name] = parameter_access
        return self.parameter_accesses[short_name]
    
    def getParameterAccesses(self) -> List[ParameterAccess]:
        return sorted(self.parameter_accesses.values(), key= lambda o: o.short_name)
    
    def createSynchronousServerCallPoint(self, short_name: str) -> SynchronousServerCallPoint:
        if (short_name not in self.server_call_points):
            server_call_point = SynchronousServerCallPoint(self, short_name)
            self.server_call_points[short_name] = server_call_point
        return self.server_call_points[short_name]

    def createAsynchronousServerCallPoint(self, short_name: str) -> AsynchronousServerCallPoint:
        if (short_name not in self.server_call_points):
            server_call_point = AsynchronousServerCallPoint(self, short_name)
            self.server_call_points[short_name] = server_call_point
        return self.server_call_points[short_name]

    def getSynchronousServerCallPoint(self) -> List[ServerCallPoint]:
        return filter(lambda o: isinstance(o, SynchronousServerCallPoint), self.getServerCallPoints())
    
    def getAsynchronousServerCallPoint(self) -> List[ServerCallPoint]:
        return filter(lambda o: isinstance(o, AsynchronousServerCallPoint), self.getServerCallPoints())

    def getServerCallPoints(self) -> List[ServerCallPoint]:
        return sorted(self.server_call_points.values(), key=lambda v: v.short_name)

    def createInternalTriggeringPoint(self, short_name: str) -> InternalTriggeringPoint:
        if (short_name not in self.elements):
            point = InternalTriggeringPoint(self, short_name)
            self.elements[point.short_name] = point
        return self.elements[point.short_name]

    def getInternalTriggeringPoints(self) -> List[InternalTriggeringPoint]:
        return filter(lambda o: isinstance(o, InternalTriggeringPoint), self.elements)

class AbstractEvent(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

class RTEEvent(AbstractEvent):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.start_on_event_ref = None  # type: RefType
        self.disabled_mode_irefs = []   # type: List[RModeInAtomicSwcInstanceRef]

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

        self.data_iref = None       # type: RVariableInAtomicSwcInstanceRef

class SwcModeSwitchEvent(RTEEvent):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self._activation = ""     
        self.mode_irefs = []       # type: List[RModeInAtomicSwcInstanceRef]

    def addModeIRef(self, iref: RModeInAtomicSwcInstanceRef):
        self.mode_irefs.append(iref)

    def getModeIRefs(self) -> List[RModeInAtomicSwcInstanceRef]:
        return self.mode_irefs

    @property
    def activation(self) -> str:
        return self._activation

    @activation.setter
    def activation(self, value: str):
        if value not in ("ON-ENTRY", "ON-EXIT", "ON-TRANSITION"):
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
        self.indirect_API = None            # type: ARBoolean
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
        self._explicit_inter_runnable_variables = []    # type: List[VariableDataPrototype]
        self._implicit_inter_runnable_variables = []    # type: List[VariableDataPrototype]
        self._per_instance_memories = []                # type: List[PerInstanceMemory]
        self._per_instance_parameters = []              # type: List[ParameterDataPrototype]
        self._port_api_options = []                     # type: List[PortAPIOption]

    def getExplicitInterRunnableVariables(self) -> List[VariableDataPrototype]:
        return self._explicit_inter_runnable_variables
    
    def getImplicitInterRunnableVariables(self) -> List[VariableDataPrototype]:
        return self._implicit_inter_runnable_variables
    
    def getPerInstanceMemories(self) -> List[PerInstanceMemory]:
        return self._per_instance_memories
    
    def getParameterDataPrototypes(self) -> List[ParameterDataPrototype]:
        return self._per_instance_parameters
    
    def addPortAPIOption(self, option: PortAPIOption):
        self._port_api_options.append(option)

    def getPortAPIOptions(self) -> List[PortAPIOption]:
        return self._port_api_options

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
            self._explicit_inter_runnable_variables.append(prototype)
        return self.elements[short_name]
    
    def createImplicitInterRunnableVariable(self, short_name: str) -> VariableDataPrototype:
        if (short_name not in self.elements):
            prototype = VariableDataPrototype(self, short_name)
            self.elements[short_name] = prototype
            self._implicit_inter_runnable_variables.append(prototype)
        return self.elements[short_name]
    
    def createPerInstanceMemory(self, short_name: str) -> PerInstanceMemory:
        if (short_name not in self.elements):
            memory = PerInstanceMemory(self, short_name)
            self.elements[short_name] = memory
            self._per_instance_memories.append(memory)
        return self.elements[short_name]
    
    def createParameterDataPrototype(self, short_name: str) -> ParameterDataPrototype:
        if (short_name not in self.elements):
            prototype = ParameterDataPrototype(self, short_name)
            self.elements[short_name] = prototype
            self._per_instance_parameters.append(prototype)
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
    
    def getPortPrototype(self) -> List[PortPrototype]:
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