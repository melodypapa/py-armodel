from typing import List, Dict
from abc import ABCMeta
from .general_structure import ARElement, Identifiable, ARObject
from .ar_ref import AutosarVariableRef, RefType, POperationInAtomicSwcInstanceRef, ROperationInAtomicSwcInstanceRef, ProvidedPortPrototypeInstanceRef, RequiredPortPrototypeInstanceRef
from .port_prototype import RPortPrototype, PPortPrototype
from .data_prototype import VariableDataPrototype

class VariableAccess(Identifiable):
    def __init__(self, parent: ARObject, short_name):
        super().__init__(parent, short_name)
        self.accessed_variable_ref = AutosarVariableRef()
        self.local_variable_ref = None  # type: RefType

class ExecutableEntity(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

class AbstractAccessPoint(Identifiable):
    __metaclass__ = ABCMeta

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name) 

class ServerCallPoint(AbstractAccessPoint):
    __metaclass__ = ABCMeta

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
        self.operation_iref = None  # type: ROperationInAtomicSwcInstanceRef
        self.timeout = 0

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

class RunnableEntity(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
        self.can_be_invoked_concurrently = False        # Type: bool
        self.data_read_accesses = {}                    # Type: Dict[VariableAccess]
        self.data_received_point_by_arguments = {}      # Type: Dict[VariableAccess]
        self.data_received_point_by_values = {}         # Type: Dict[VariableAccess]
        self.data_send_points = {}                      # Type: Dict[VariableAccess]
        self.data_write_accesses = {}                   # Type: Dict[VariableAccess]
        self.written_local_variables = {}               # Type: Dict[VariableAccess]
        self.read_local_variables = {}                  # Type: Dict[VariableAccess]
        self.external_triggering_points = {}            # Type: Dict[InternalTriggeringPoint]
        self.internal_triggering_points = {}
        self.mode_access_points = {}
        self.mode_switch_points = {}
        self.parameter_accesses = {}
        self.server_call_points = {}                    # Type: Dict[ServerCallPoint]
        self.wait_points = {}                           # Type: Dict[WaitPoint]
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
    
    def createSynchronousServerCallPoint(self, short_name: str) -> SynchronousServerCallPoint:
        if (short_name not in self.server_call_points):
            server_call_point = SynchronousServerCallPoint(self, short_name)
            self.server_call_points[short_name] = server_call_point
        return self.server_call_points[short_name]

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
        self.start_on_event_ref = None # type: RefType

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

class DataReceiveErrorEvent(RTEEvent):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

class OperationInvokedEvent(RTEEvent):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
        self.operation_iref = None      # type: POperationInAtomicSwcInstanceRef

class TimingEvent(RTEEvent):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
        self.offset = None
        self.period = 0
    
    @property
    def peroid_ms(self):
        if (self.period < 0.001):
            return self.period * 1000
        else:
            return (int)(self.period * 1000)

class InternalTriggerOccurredEvent(RTEEvent):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.event_source_ref = None    # type: RefType  

class InternalBehavior(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

class SwcInternalBehavior(InternalBehavior):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

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

    def createInternalTriggerOccurredEvent(self, short_name: str) -> InternalTriggerOccurredEvent:
        if (short_name not in self.elements):
            event = InternalTriggerOccurredEvent(self, short_name)
            self.elements[short_name] = event
        return self.elements[short_name]

    def getEvents(self) -> List[RTEEvent]:
        return sorted(filter(lambda c: isinstance(c, RTEEvent), self.elements.values()), key=lambda e: e.short_name)

    def getOperationInvokedEvents(self) -> List[OperationInvokedEvent]:
        return sorted(filter(lambda c: isinstance(c, OperationInvokedEvent), self.elements.values()), key=lambda e: e.short_name)

    def getTimingEvents(self) -> List[TimingEvent]:
        return sorted(filter(lambda c: isinstance(c, TimingEvent), self.elements.values()), key=lambda e: e.short_name)

    def getInternalTriggerOccurredEvents(self) -> List[InternalTriggerOccurredEvent]:
        return sorted(filter(lambda c: isinstance(c, InternalTriggerOccurredEvent), self.elements.values()), key= lambda e: e.short_name)
    
    def getEvent(self, short_name: str) -> RTEEvent:
        if (not isinstance(self.elements[short_name], RTEEvent)):
            raise ValueError("Invalid Event Type <%s> of <%s>" % type(self.elements[short_name]), short_name)
        return self.elements[short_name]

    def createExplicitInterRunnableVariable(self, short_name: str) -> VariableDataPrototype:
        if (short_name not in self.elements):
            prototype = VariableDataPrototype(self, short_name)
            self.elements[short_name] = prototype
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

class SwComponentType(ARElement):
    __metaclass__ = ABCMeta

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

    def createPPortPrototype(self, short_name: str) -> PPortPrototype:
        if (short_name not in self.elements):
            prototype = PPortPrototype(self, short_name)
            self.elements[short_name] = prototype
        return self.elements[short_name]

    def createRPortPrototype(self, short_name) -> RPortPrototype:
        if (short_name not in self.elements):
            prototype = RPortPrototype(self, short_name)
            self.elements[short_name] = prototype
        return self.elements[short_name]

    def getPPortPrototypes(self) -> List[PPortPrototype]:
        return list(filter(lambda c: isinstance(c, PPortPrototype), self.elements.values()))

    def getRPortPrototypes(self) -> List[RPortPrototype]:
        return list(filter(lambda c: isinstance(c, RPortPrototype), self.elements.values()))

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

        self.provider_iref = None   # type: ProvidedPortPrototypeInstanceRef
        self.requester_iref = None  # type: RequiredPortPrototypeInstanceRef

class DelegationSwConnector(SwConnector):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.inner_port_iref = None # type: RefType
        self.outer_port_iref = None # type: RefType

class PassThroughSwConnector(SwConnector):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.provided_outer_port_iref = None # type: RefType
        self.required_outer_port_iref = None # type: RefType

class SwComponentPrototype(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.type_tref = RefType()

class CompositionSwComponentType(SwComponentType):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.constant_value_mapping_refs = []   # type: List[RefType]
        self.data_type_mapping_refs = []        # type: List[RefType]
        self.instantiation_rte_event_props = [] # type: List[InstantiationRTEEventProps]

    def createAssemblySwConnector(self, short_name: str) -> AssemblySwConnector:
        if (short_name not in self.elements):
            connector = AssemblySwConnector(self, short_name)
            self.elements[short_name] = connector
        return self.elements[short_name] 

    def getAssemblySwConnectors(self) -> List[AssemblySwConnector]:
        return list(filter(lambda e: isinstance(e, AssemblySwConnector), self.elements.values()))

    def createSwComponentPrototype(self, short_name: str) -> SwComponentPrototype:
        if (short_name not in self.elements):
            connector = SwComponentPrototype(self, short_name)
            self.elements[short_name] = connector
        return self.elements[short_name] 

    def getSwComponentPrototypes(self) -> List[SwComponentPrototype]:
        return list(filter(lambda e: isinstance(e, SwComponentPrototype), self.elements.values()))