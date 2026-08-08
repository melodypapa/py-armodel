from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount import AbstractAccessPoint
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions import PortAPIOption
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import ApiPrincipleEnum, InternalBehavior
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import ParameterDataPrototype, VariableDataPrototype
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.IncludedDataTypes import IncludedDataTypeSet
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.InstantiationDataDefProps import InstantiationDataDefProps
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PerInstanceMemory import PerInstanceMemory
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents import AsynchronousServerCallReturnsEvent, BackgroundEvent
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents import DataSendCompletedEvent
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents import DataReceivedEvent, InitEvent, InternalTriggerOccurredEvent
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents import ModeSwitchedAckEvent, OperationInvokedEvent, RTEEvent
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents import SwcModeSwitchEvent, TimingEvent
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping import SwcServiceDependency
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
    Boolean as Boolean,
    RefType as RefType,
    ARBoolean,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import ParameterAccess, VariableAccess
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServerCall import ServerCallPoint
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ModeDeclarationGroup import (
    IncludedModeDeclarationGroupSet as IncludedModeDeclarationGroupSet,
    ModeAccessPoint,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ModeDeclarationGroup import ModeSwitchPoint
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.Trigger import ExternalTriggeringPoint, InternalTriggeringPoint
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.VariantHandling import VariationPointProxy
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import ExecutableEntity


class RunnableEntityArgument(ARObject):
    # RunnableEntityArgument method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getSymbol                    [x] impl  [ ] docstring  [ ] test
    # [ ] setSymbol                    [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.symbol = None  # type: ARLiteral

    def getSymbol(self):
        return self.symbol

    def setSymbol(self, value):
        self.symbol = value
        return self


class AsynchronousServerCallResultPoint(AbstractAccessPoint):
    # AsynchronousServerCallResultPoint method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getAsynchronousServerCallPointRef [x] impl  [ ] docstring  [ ] test
    # [ ] setAsynchronousServerCallPointRef [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.asynchronousServerCallPointRef = None  # type: RefType

    def getAsynchronousServerCallPointRef(self):
        return self.asynchronousServerCallPointRef

    def setAsynchronousServerCallPointRef(self, value):
        self.asynchronousServerCallPointRef = value
        return self


class AsynchronousServerCallPoint(ServerCallPoint):
    # AsynchronousServerCallPoint method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class SynchronousServerCallPoint(ServerCallPoint):
    # SynchronousServerCallPoint method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getCalledFromWithinExclusiveAreaRef [x] impl  [ ] docstring  [ ] test
    # [ ] setCalledFromWithinExclusiveAreaRef [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.calledFromWithinExclusiveAreaRef = None  # type: RefType

    def getCalledFromWithinExclusiveAreaRef(self):
        return self.calledFromWithinExclusiveAreaRef

    def setCalledFromWithinExclusiveAreaRef(self, value):
        self.calledFromWithinExclusiveAreaRef = value
        return self


class RunnableEntity(ExecutableEntity):
    # RunnableEntity method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] _createVariableAccess        [x] impl  [ ] docstring  [ ] test
    # [ ] getArguments                 [x] impl  [ ] docstring  [ ] test
    # [ ] addArgument                  [x] impl  [ ] docstring  [ ] test
    # [ ] getCanBeInvokedConcurrently  [x] impl  [ ] docstring  [ ] test
    # [ ] setCanBeInvokedConcurrently  [x] impl  [ ] docstring  [ ] test
    # [ ] createDataReadAccess         [x] impl  [ ] docstring  [ ] test
    # [ ] getDataReadAccesses          [x] impl  [ ] docstring  [ ] test
    # [ ] createDataWriteAccess        [x] impl  [ ] docstring  [ ] test
    # [ ] getDataWriteAccesses         [x] impl  [ ] docstring  [ ] test
    # [ ] createDataReceivePointByArgument [x] impl  [ ] docstring  [ ] test
    # [ ] getDataReceivePointByArguments [x] impl  [ ] docstring  [ ] test
    # [ ] createDataReceivePointByValue [x] impl  [ ] docstring  [ ] test
    # [ ] getDataReceivePointByValues  [x] impl  [ ] docstring  [ ] test
    # [ ] createDataSendPoint          [x] impl  [ ] docstring  [ ] test
    # [ ] getDataSendPoints            [x] impl  [ ] docstring  [ ] test
    # [ ] createReadLocalVariable      [x] impl  [ ] docstring  [ ] test
    # [ ] getReadLocalVariables        [x] impl  [ ] docstring  [ ] test
    # [ ] createWrittenLocalVariable   [x] impl  [ ] docstring  [ ] test
    # [ ] getWrittenLocalVariables     [x] impl  [ ] docstring  [ ] test
    # [ ] getParameterAccesses         [x] impl  [ ] docstring  [ ] test
    # [ ] createParameterAccess        [x] impl  [ ] docstring  [ ] test
    # [ ] createSynchronousServerCallPoint [x] impl  [ ] docstring  [ ] test
    # [ ] createAsynchronousServerCallPoint [x] impl  [ ] docstring  [ ] test
    # [ ] createAsynchronousServerCallResultPoint [x] impl  [ ] docstring  [ ] test
    # [ ] getSynchronousServerCallPoint [x] impl  [ ] docstring  [ ] test
    # [ ] getAsynchronousServerCallPoint [x] impl  [ ] docstring  [ ] test
    # [ ] getAsynchronousServerCallResultPoints [x] impl  [ ] docstring  [ ] test
    # [ ] getServerCallPoints          [x] impl  [ ] docstring  [ ] test
    # [ ] createInternalTriggeringPoint [x] impl  [ ] docstring  [ ] test
    # [ ] getInternalTriggeringPoints  [x] impl  [ ] docstring  [ ] test
    # [ ] getModeAccessPoints          [x] impl  [ ] docstring  [ ] test
    # [ ] addModeAccessPoint           [x] impl  [ ] docstring  [ ] test
    # [ ] getModeSwitchPoints          [x] impl  [ ] docstring  [ ] test
    # [ ] createModeSwitchPoint        [x] impl  [ ] docstring  [ ] test
    # [ ] getSymbol                    [x] impl  [ ] docstring  [ ] test
    # [ ] setSymbol                    [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.arguments: List[RunnableEntityArgument] = []
        self.asynchronousServerCallResultPoints: List[AsynchronousServerCallResultPoint] = []
        self.canBeInvokedConcurrently: ARBoolean = None
        self.dataReadAccesses: List[VariableAccess] = []
        self.dataReceivePointByArguments: List[VariableAccess] = []
        self.dataReceivePointByValues: List[VariableAccess] = []
        self.dataSendPoints: List[VariableAccess] = []
        self.dataWriteAccesses: List[VariableAccess] = []
        self.externalTriggeringPoints: List[ExternalTriggeringPoint] = []
        self.internalTriggeringPoints: List[InternalTriggeringPoint] = []
        self.modeAccessPoints: List[ModeAccessPoint] = []
        self.modeSwitchPoints: List[ModeSwitchPoint] = []
        self.parameterAccesses: List[ParameterAccess] = []
        self.readLocalVariables: List[VariableAccess] = []
        self.serverCallPoints: List[ServerCallPoint] = []
        self.symbol: ARLiteral = None
        self.waitPoints = {}  # type: Dict[str, WaitPoint]
        self.writtenLocalVariables: List[VariableAccess] = []

    def _createVariableAccess(self, short_name, variable_accesses: List[VariableAccess]):
        if not self.IsElementExists(short_name):
            variable_access = VariableAccess(self, short_name)
            self.addElement(variable_access)
            variable_accesses.append(variable_access)
        return self.getElement(short_name, VariableAccess)

    def getArguments(self):
        return self.arguments

    def addArgument(self, value):
        self.arguments.append(value)
        return self

    def getCanBeInvokedConcurrently(self):
        return self.canBeInvokedConcurrently

    def setCanBeInvokedConcurrently(self, value):
        self.canBeInvokedConcurrently = value
        return self

    def createDataReadAccess(self, short_name: str) -> VariableAccess:
        return self._createVariableAccess(short_name, self.dataReadAccesses)

    def getDataReadAccesses(self) -> List[VariableAccess]:
        return sorted(self.dataReadAccesses, key=lambda v: v.short_name)

    def createDataWriteAccess(self, short_name: str) -> VariableAccess:
        return self._createVariableAccess(short_name, self.dataWriteAccesses)

    def getDataWriteAccesses(self) -> List[VariableAccess]:
        return sorted(self.dataWriteAccesses, key=lambda v: v.short_name)

    def createDataReceivePointByArgument(self, short_name: str) -> VariableAccess:
        return self._createVariableAccess(short_name, self.dataReceivePointByArguments)

    def getDataReceivePointByArguments(self) -> List[VariableAccess]:
        return sorted(self.dataReceivePointByArguments, key=lambda v: v.short_name)

    def createDataReceivePointByValue(self, short_name: str) -> VariableAccess:
        return self._createVariableAccess(short_name, self.dataReceivePointByValues)

    def getDataReceivePointByValues(self) -> List[VariableAccess]:
        return sorted(self.dataReceivePointByValues, key=lambda v: v.short_name)

    def createDataSendPoint(self, short_name: str) -> VariableAccess:
        return self._createVariableAccess(short_name, self.dataSendPoints)

    def getDataSendPoints(self) -> List[VariableAccess]:
        # return sorted(self.dataSendPoints.values(), key=lambda v: v.short_name)
        return self.dataSendPoints

    def createReadLocalVariable(self, short_name: str) -> VariableAccess:
        return self._createVariableAccess(short_name, self.readLocalVariables)

    def getReadLocalVariables(self) -> List[VariableAccess]:
        # return sorted(self.readLocalVariables.values(), key=lambda v: v.short_name)
        return self.readLocalVariables

    def createWrittenLocalVariable(self, short_name: str) -> VariableAccess:
        return self._createVariableAccess(short_name, self.writtenLocalVariables)

    def getWrittenLocalVariables(self) -> List[VariableAccess]:
        return self.writtenLocalVariables

    def getParameterAccesses(self) -> List[ParameterAccess]:
        return list(sorted(filter(lambda a: isinstance(a, ParameterAccess), self.elements), key=lambda o: o.short_name))

    def createParameterAccess(self, short_name: str) -> ParameterAccess:
        if not self.IsElementExists(short_name):
            access = ParameterAccess(self, short_name)
            self.addElement(access)
        return self.getElement(short_name)

    def createSynchronousServerCallPoint(self, short_name: str) -> SynchronousServerCallPoint:
        if short_name not in self.serverCallPoints:
            point = SynchronousServerCallPoint(self, short_name)
            self.addElement(point)
        return self.getElement(short_name)
        # self.serverCallPoints[short_name] = server_call_point
        # return self.serverCallPoints[short_name]

    def createAsynchronousServerCallPoint(self, short_name: str) -> AsynchronousServerCallPoint:
        if short_name not in self.serverCallPoints:
            point = AsynchronousServerCallPoint(self, short_name)
            self.addElement(point)
        return self.getElement(short_name, AsynchronousServerCallPoint)
        # self.serverCallPoints[short_name] = server_call_point
        # return self.serverCallPoints[short_name]

    def createAsynchronousServerCallResultPoint(self, short_name: str) -> AsynchronousServerCallResultPoint:
        if short_name not in self.serverCallPoints:
            point = AsynchronousServerCallResultPoint(self, short_name)
            self.addElement(point)
        return self.getElement(short_name)

    def getSynchronousServerCallPoint(self) -> List[SynchronousServerCallPoint]:
        return list(sorted(filter(lambda a: isinstance(a, SynchronousServerCallPoint), self.elements), key=lambda o: o.getShortName()))

    def getAsynchronousServerCallPoint(self) -> List[AsynchronousServerCallPoint]:
        return list(sorted(filter(lambda a: isinstance(a, AsynchronousServerCallPoint), self.elements), key=lambda o: o.getShortName()))

    def getAsynchronousServerCallResultPoints(self) -> List[AsynchronousServerCallResultPoint]:
        return list(sorted(filter(lambda a: isinstance(a, AsynchronousServerCallResultPoint), self.elements), key=lambda o: o.getShortName()))  # noqa E501

    def getServerCallPoints(self) -> List[ServerCallPoint]:
        return list(sorted(filter(lambda a: isinstance(a, ServerCallPoint), self.elements), key=lambda o: o.getShortName()))

    def createInternalTriggeringPoint(self, short_name: str) -> InternalTriggeringPoint:
        if not self.IsElementExists(short_name):
            point = InternalTriggeringPoint(self, short_name)
            self.addElement(point)
        return self.getElement(short_name, InternalTriggeringPoint)

    def getInternalTriggeringPoints(self) -> List[InternalTriggeringPoint]:
        return filter(lambda o: isinstance(o, InternalTriggeringPoint), self.elements)

    def getModeAccessPoints(self) -> List[ModeAccessPoint]:
        return self.modeAccessPoints

    def addModeAccessPoint(self, value):
        self.modeAccessPoints.append(value)

    def getModeSwitchPoints(self) -> List[ModeSwitchPoint]:
        return list(sorted(filter(lambda a: isinstance(a, ModeSwitchPoint), self.elements), key=lambda o: o.short_name))

    def createModeSwitchPoint(self, short_name: str) -> ModeSwitchPoint:
        if not self.IsElementExists(short_name):
            access = ModeSwitchPoint(self, short_name)
            self.addElement(access)
            self.modeSwitchPoints.append(access)
        return self.getElement(short_name, ModeSwitchPoint)

    def getSymbol(self):
        return self.symbol

    def setSymbol(self, value):
        self.symbol = value
        return self


class SwcExclusiveAreaPolicy(ARObject):
    """
    Options how to generate the ExclusiveArea related APIs. If no
    SwcExclusiveAreaPolicy is specified for an ExclusiveArea the default values
    apply.
    """

    # SwcExclusiveAreaPolicy method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.28, p.556
    # Spec verified: R23-11
    # [x] __init__             [x] impl  [x] docstring  [x] test
    # [x] getApiPrinciple      [x] impl  [x] docstring  [x] test
    # [x] setApiPrinciple      [x] impl  [x] docstring  [x] test
    # [x] getExclusiveAreaRef  [x] impl  [x] docstring  [x] test
    # [x] setExclusiveAreaRef  [x] impl  [x] docstring  [x] test

    def __init__(self):
        super().__init__()

        # Specifies for this ExclusiveArea if either one common set of Enter
        # and Exit APIs for the whole software component is requested from the
        # Rte or if the set of Enter and Exit APIs is expected per
        # RunnableEntity. The default value is "common".
        self.apiPrinciple: Optional[ApiPrincipleEnum] = None

        # This reference represents the ExclusiveArea for which the policy
        # applies.
        self.exclusiveAreaRef: Optional[RefType] = None

    def getApiPrinciple(self) -> Optional[ApiPrincipleEnum]:
        """Gets the apiPrinciple (common vs per-RunnableEntity API generation) for this policy."""
        return self.apiPrinciple

    def setApiPrinciple(self, value: Optional[ApiPrincipleEnum]) -> "SwcExclusiveAreaPolicy":
        """
        Sets the apiPrinciple (common vs per-RunnableEntity API generation) for
        this policy. A None value is a no-op and does not overwrite an existing
        apiPrinciple.
        """
        if value is not None:
            self.apiPrinciple = value
        return self

    def getExclusiveAreaRef(self) -> Optional[RefType]:
        """Gets the reference to the ExclusiveArea for which this policy applies."""
        return self.exclusiveAreaRef

    def setExclusiveAreaRef(self, value: Optional[RefType]) -> "SwcExclusiveAreaPolicy":
        """
        Sets the reference to the ExclusiveArea for which this policy applies.
        A None value is a no-op and does not overwrite an existing
        exclusiveAreaRef.
        """
        if value is not None:
            self.exclusiveAreaRef = value
        return self


class SwcInternalBehavior(InternalBehavior):
    """
    The SwcInternalBehavior of an AtomicSwComponentType describes the
    relevant aspects of the software-component with respect to the RTE, i.e.
    the RunnableEntities and the RTEEvents they respond to.
    """

    # SwcInternalBehavior method parity checklist:
    # [x] __init__                                   [x] impl  [x] docstring  [x] test
    # [x] getArTypedPerInstanceMemories              [x] impl  [x] docstring  [x] test
    # [x] createArTypedPerInstanceMemory             [x] impl  [x] docstring  [x] test
    # [x] addExclusiveAreaPolicy                     [x] impl  [x] docstring  [x] test
    # [x] getExclusiveAreaPolicies                   [x] impl  [x] docstring  [x] test
    # [x] getExplicitInterRunnableVariables          [x] impl  [x] docstring  [x] test
    # [x] createExplicitInterRunnableVariable        [x] impl  [x] docstring  [x] test
    # [x] getHandleTerminationAndRestart             [x] impl  [x] docstring  [x] test
    # [x] setHandleTerminationAndRestart             [x] impl  [x] docstring  [x] test
    # [x] getImplicitInterRunnableVariables          [x] impl  [x] docstring  [x] test
    # [x] createImplicitInterRunnableVariable        [x] impl  [x] docstring  [x] test
    # [x] getPerInstanceMemories                     [x] impl  [x] docstring  [x] test
    # [x] createPerInstanceMemory                    [x] impl  [x] docstring  [x] test
    # [x] getPerInstanceParameters                   [x] impl  [x] docstring  [x] test
    # [x] createPerInstanceParameter                 [x] impl  [x] docstring  [x] test
    # [x] getSharedParameters                        [x] impl  [x] docstring  [x] test
    # [x] createSharedParameter                      [x] impl  [x] docstring  [x] test
    # [x] addPortAPIOption                           [x] impl  [x] docstring  [x] test
    # [x] getPortAPIOptions                          [x] impl  [x] docstring  [x] test
    # [x] addIncludedDataTypeSet                     [x] impl  [x] docstring  [x] test
    # [x] getIncludedDataTypeSets                    [x] impl  [x] docstring  [x] test
    # [x] addIncludedModeDeclarationGroupSet         [x] impl  [x] docstring  [x] test
    # [x] getIncludedModeDeclarationGroupSets        [x] impl  [x] docstring  [x] test
    # [x] createOperationInvokedEvent                [x] impl  [x] docstring  [x] test
    # [x] createTimingEvent                          [x] impl  [x] docstring  [x] test
    # [x] createInitEvent                            [x] impl  [x] docstring  [x] test
    # [x] createAsynchronousServerCallReturnsEvent   [x] impl  [x] docstring  [x] test
    # [x] createDataReceivedEvent                    [x] impl  [x] docstring  [x] test
    # [x] createSwcModeSwitchEvent                   [x] impl  [x] docstring  [x] test
    # [x] createInternalTriggerOccurredEvent         [x] impl  [x] docstring  [x] test
    # [x] createModeSwitchedAckEvent                 [x] impl  [x] docstring  [x] test
    # [x] createBackgroundEvent                      [x] impl  [x] docstring  [x] test
    # [x] createDataSendCompletedEvent               [x] impl  [x] docstring  [x] test
    # [x] getRteEvents                               [x] impl  [x] docstring  [x] test
    # [x] getOperationInvokedEvents                  [x] impl  [x] docstring  [x] test
    # [x] getInitEvents                              [x] impl  [x] docstring  [x] test
    # [x] getTimingEvents                            [x] impl  [x] docstring  [x] test
    # [x] getDataReceivedEvents                      [x] impl  [x] docstring  [x] test
    # [x] getSwcModeSwitchEvents                     [x] impl  [x] docstring  [x] test
    # [x] getInternalTriggerOccurredEvents           [x] impl  [x] docstring  [x] test
    # [x] getModeSwitchedAckEvents                   [x] impl  [x] docstring  [x] test
    # [x] getBackgroundEvents                        [x] impl  [x] docstring  [x] test
    # [x] getDataSendCompletedEvents                 [x] impl  [x] docstring  [x] test
    # [x] getEvent                                   [x] impl  [x] docstring  [x] test
    # [x] createSwcServiceDependency                 [x] impl  [x] docstring  [x] test
    # [x] getSwcServiceDependencies                  [x] impl  [x] docstring  [x] test
    # [x] getVariableDataPrototypes                  [x] impl  [x] docstring  [x] test
    # [x] createRunnableEntity                       [x] impl  [x] docstring  [x] test
    # [x] getRunnableEntities                        [x] impl  [x] docstring  [x] test
    # [x] getRunnableEntity                          [x] impl  [x] docstring  [x] test
    # [x] getSupportsMultipleInstantiation           [x] impl  [x] docstring  [x] test
    # [x] setSupportsMultipleInstantiation           [x] impl  [x] docstring  [x] test
    # [x] addInstantiationDataDefProps               [x] impl  [x] docstring  [x] test
    # [x] getInstantiationDataDefPropss              [x] impl  [x] docstring  [x] test
    # [x] addVariationPointProxy                     [x] impl  [x] docstring  [x] test
    # [x] getVariationPointProxies                   [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Defines an AUTOSAR typed memory-block that needs to be available for
        # each instance of the SW-component.
        self.arTypedPerInstanceMemories: List[VariableDataPrototype] = []

        # This is a RTEEvent specified for the particular Swc InternalBehavior.
        # RTEEvents are registered through the create*Event factories and are
        # retrieved from the elements registry via getRteEvents / getEvent.
        self.events: List[RTEEvent] = []

        # Options how to generate the ExclusiveArea related APIs.
        self.exclusiveAreaPolicies: List[SwcExclusiveAreaPolicy] = []

        # Implement state message semantics for establishing communication
        # among runnables of the same component.
        self.explicitInterRunnableVariables: List[VariableDataPrototype] = []

        # Controls the behavior with respect to stopping and restarting; the
        # corresponding AtomicSwComponentType may either not support stop and
        # restart, or support only stop, or support both. (Present in the XSD,
        # absent from the PDF table rendering; PDF enum
        # HandleTerminationAndRestartEnum not modeled, carried as ARLiteral.)
        self.handleTerminationAndRestart: Optional[ARLiteral] = None

        # Implement state message semantics for establishing communication
        # among runnables of the same component.
        self.implicitInterRunnableVariables: List[VariableDataPrototype] = []

        # The includedDataTypeSet is used by a software component for its
        # implementation.
        self.includedDataTypeSets: List[IncludedDataTypeSet] = []

        # This aggregation represents the included Mode DeclarationGroups.
        self.includedModeDeclarationGroupSets: List[IncludedModeDeclarationGroupSet] = []

        # Within the context of a given SwComponentType some data def
        # properties of individual instantiations can be modified.
        self.instantiationDataDefProps: List[InstantiationDataDefProps] = []

        # Defines a per-instance memory object needed by this software
        # component.
        self.perInstanceMemories: List[PerInstanceMemory] = []

        # Defines parameter(s) or characteristic value(s) that needs to be
        # available for each instance of the software-component.
        self.perInstanceParameters: List[ParameterDataPrototype] = []

        # Options for generating the signature of port-related calls from a
        # runnable to the RTE and vice versa.
        self.portAPIOptions: List[PortAPIOption] = []

        # This is a RunnableEntity specified for the particular Swc
        # InternalBehavior.
        self.runnables: List[RunnableEntity] = []

        # Defines the requirements on AUTOSAR Services for a particular item.
        self.serviceDependencies: List[SwcServiceDependency] = []

        # Defines parameter(s) or characteristic value(s) shared between
        # SwComponentPrototypes of the same SwComponentType.
        self.sharedParameters: List[ParameterDataPrototype] = []

        # Indicate whether the corresponding software-component can be multiply
        # instantiated on one ECU. [constr_1935]
        self.supportsMultipleInstantiation: Optional[Boolean] = None

        # Proxy of a variation points in the C/C++ implementation.
        self.variationPointProxies: List[VariationPointProxy] = []

    def getArTypedPerInstanceMemories(self) -> List[VariableDataPrototype]:
        """Gets the AUTOSAR typed per-instance memory blocks owned by this behavior."""
        return self.arTypedPerInstanceMemories

    def createArTypedPerInstanceMemory(self, short_name: str) -> VariableDataPrototype:
        """Creates (or returns an existing) arTypedPerInstanceMemory registered to this behavior."""
        if not self.IsElementExists(short_name):
            prototype = VariableDataPrototype(self, short_name)
            self.addElement(prototype)
            self.arTypedPerInstanceMemories.append(prototype)
        return self.getElement(short_name)

    def getExplicitInterRunnableVariables(self) -> List[VariableDataPrototype]:
        """Gets the explicitInterRunnableVariables owned by this behavior."""
        return self.explicitInterRunnableVariables

    def createExplicitInterRunnableVariable(self, short_name: str) -> VariableDataPrototype:
        """Creates (or returns an existing) explicitInterRunnableVariable registered to this behavior."""
        if not self.IsElementExists(short_name):
            prototype = VariableDataPrototype(self, short_name)
            self.addElement(prototype)
            self.explicitInterRunnableVariables.append(prototype)
        return self.getElement(short_name)

    def getHandleTerminationAndRestart(self) -> Optional[ARLiteral]:
        """Gets handleTerminationAndRestart (stop/restart support of the AtomicSwComponentType)."""
        return self.handleTerminationAndRestart

    def setHandleTerminationAndRestart(self, value: Optional[ARLiteral]) -> "SwcInternalBehavior":
        """
        Sets handleTerminationAndRestart (stop/restart support of the
        AtomicSwComponentType). A None value is a no-op and does not overwrite
        an existing handleTerminationAndRestart.
        """
        if value is not None:
            self.handleTerminationAndRestart = value
        return self

    def getImplicitInterRunnableVariables(self) -> List[VariableDataPrototype]:
        """Gets the implicitInterRunnableVariables owned by this behavior."""
        return self.implicitInterRunnableVariables

    def createImplicitInterRunnableVariable(self, short_name: str) -> VariableDataPrototype:
        """Creates (or returns an existing) implicitInterRunnableVariable registered to this behavior."""
        if not self.IsElementExists(short_name):
            prototype = VariableDataPrototype(self, short_name)
            self.addElement(prototype)
            self.implicitInterRunnableVariables.append(prototype)
        return self.getElement(short_name)

    def getPerInstanceMemories(self) -> List[PerInstanceMemory]:
        """Gets the perInstanceMemory objects owned by this behavior."""
        return self.perInstanceMemories

    def createPerInstanceMemory(self, short_name: str) -> PerInstanceMemory:
        """Creates (or returns an existing) perInstanceMemory registered to this behavior."""
        if not self.IsElementExists(short_name):
            memory = PerInstanceMemory(self, short_name)
            self.addElement(memory)
            self.perInstanceMemories.append(memory)
        return self.getElement(short_name)

    def getPerInstanceParameters(self) -> List[ParameterDataPrototype]:
        """Gets the perInstanceParameter objects owned by this behavior."""
        return self.perInstanceParameters

    def createPerInstanceParameter(self, short_name: str) -> ParameterDataPrototype:
        """Creates (or returns an existing) perInstanceParameter registered to this behavior."""
        if not self.IsElementExists(short_name):
            prototype = ParameterDataPrototype(self, short_name)
            self.addElement(prototype)
            self.perInstanceParameters.append(prototype)
        return self.getElement(short_name)

    def getSharedParameters(self) -> List[ParameterDataPrototype]:
        """Gets the sharedParameter objects owned by this behavior."""
        return self.sharedParameters

    def createSharedParameter(self, short_name: str) -> ParameterDataPrototype:
        """Creates (or returns an existing) sharedParameter registered to this behavior."""
        if not self.IsElementExists(short_name):
            memory = ParameterDataPrototype(self, short_name)
            self.addElement(memory)
            self.sharedParameters.append(memory)
        return self.getElement(short_name)

    def addPortAPIOption(self, value: Optional[PortAPIOption]) -> "SwcInternalBehavior":
        """
        Adds a portAPIOption (options for generating port-related call signatures).
        A None value is a no-op and does not append to portAPIOptions.
        """
        if value is not None:
            self.portAPIOptions.append(value)
        return self

    def getPortAPIOptions(self) -> List[PortAPIOption]:
        """Gets the portAPIOption objects owned by this behavior."""
        return self.portAPIOptions

    def addIncludedDataTypeSet(self, value: Optional[IncludedDataTypeSet]) -> "SwcInternalBehavior":
        """
        Adds an includedDataTypeSet used by the software component for its
        implementation. A None value is a no-op and does not append to
        includedDataTypeSets.
        """
        if value is not None:
            self.includedDataTypeSets.append(value)
        return self

    def getIncludedDataTypeSets(self) -> List[IncludedDataTypeSet]:
        """Gets the includedDataTypeSet objects owned by this behavior."""
        return self.includedDataTypeSets

    def addIncludedModeDeclarationGroupSet(self, value: Optional[IncludedModeDeclarationGroupSet]) -> "SwcInternalBehavior":
        """
        Adds an includedModeDeclarationGroupSet representing the included Mode
        DeclarationGroups. A None value is a no-op and does not append to
        includedModeDeclarationGroupSets.
        """
        if value is not None:
            self.includedModeDeclarationGroupSets.append(value)
        return self

    def getIncludedModeDeclarationGroupSets(self) -> List[IncludedModeDeclarationGroupSet]:
        """Gets the includedModeDeclarationGroupSet objects owned by this behavior."""
        return self.includedModeDeclarationGroupSets

    def addExclusiveAreaPolicy(self, value: Optional[SwcExclusiveAreaPolicy]) -> "SwcInternalBehavior":
        """
        Adds an exclusiveAreaPolicy (options how to generate the ExclusiveArea
        related APIs). A None value is a no-op and does not append to
        exclusiveAreaPolicies.
        """
        if value is not None:
            self.exclusiveAreaPolicies.append(value)
        return self

    def getExclusiveAreaPolicies(self) -> List[SwcExclusiveAreaPolicy]:
        """Gets the exclusiveAreaPolicy objects owned by this behavior."""
        return self.exclusiveAreaPolicies

    def createOperationInvokedEvent(self, short_name: str) -> OperationInvokedEvent:
        """Creates (or returns an existing) OperationInvokedEvent RTEEvent registered to this behavior."""
        if not self.IsElementExists(short_name):
            event = OperationInvokedEvent(self, short_name)
            self.addElement(event)
        return self.getElement(short_name, OperationInvokedEvent)

    def createTimingEvent(self, short_name: str) -> TimingEvent:
        """Creates (or returns an existing) TimingEvent RTEEvent registered to this behavior."""
        if not self.IsElementExists(short_name):
            event = TimingEvent(self, short_name)
            self.addElement(event)
        return self.getElement(short_name, TimingEvent)

    def createInitEvent(self, short_name: str) -> InitEvent:
        """Creates (or returns an existing) InitEvent RTEEvent registered to this behavior."""
        if not self.IsElementExists(short_name):
            event = InitEvent(self, short_name)
            self.addElement(event)
        return self.getElement(short_name, InitEvent)

    def createAsynchronousServerCallReturnsEvent(self, short_name: str) -> AsynchronousServerCallReturnsEvent:
        """Creates (or returns an existing) AsynchronousServerCallReturnsEvent RTEEvent registered to this behavior."""
        if not self.IsElementExists(short_name):
            event = AsynchronousServerCallReturnsEvent(self, short_name)
            self.addElement(event)
        return self.getElement(short_name, AsynchronousServerCallReturnsEvent)

    def createDataReceivedEvent(self, short_name: str) -> DataReceivedEvent:
        """Creates (or returns an existing) DataReceivedEvent RTEEvent registered to this behavior."""
        if not self.IsElementExists(short_name):
            event = DataReceivedEvent(self, short_name)
            self.addElement(event)
        return self.getElement(short_name, DataReceivedEvent)

    def createSwcModeSwitchEvent(self, short_name: str) -> SwcModeSwitchEvent:
        """Creates (or returns an existing) SwcModeSwitchEvent RTEEvent registered to this behavior."""
        if not self.IsElementExists(short_name):
            event = SwcModeSwitchEvent(self, short_name)
            self.addElement(event)
        return self.getElement(short_name, SwcModeSwitchEvent)

    def createInternalTriggerOccurredEvent(self, short_name: str) -> InternalTriggerOccurredEvent:
        """Creates (or returns an existing) InternalTriggerOccurredEvent RTEEvent registered to this behavior."""
        if not self.IsElementExists(short_name):
            event = InternalTriggerOccurredEvent(self, short_name)
            self.addElement(event)
        return self.getElement(short_name, InternalTriggerOccurredEvent)

    def createModeSwitchedAckEvent(self, short_name: str) -> ModeSwitchedAckEvent:
        """Creates (or returns an existing) ModeSwitchedAckEvent RTEEvent registered to this behavior."""
        if not self.IsElementExists(short_name):
            event = ModeSwitchedAckEvent(self, short_name)
            self.addElement(event)
        return self.getElement(short_name, ModeSwitchedAckEvent)

    def createBackgroundEvent(self, short_name: str) -> BackgroundEvent:
        """Creates (or returns an existing) BackgroundEvent RTEEvent registered to this behavior."""
        if not self.IsElementExists(short_name):
            event = BackgroundEvent(self, short_name)
            self.addElement(event)
        return self.getElement(short_name, BackgroundEvent)

    def createDataSendCompletedEvent(self, short_name: str) -> DataSendCompletedEvent:
        """Creates (or returns an existing) DataSendCompletedEvent RTEEvent registered to this behavior."""
        if not self.IsElementExists(short_name):
            event = DataSendCompletedEvent(self, short_name)
            self.addElement(event)
        return self.getElement(short_name, DataSendCompletedEvent)

    def createSwcServiceDependency(self, short_name: str) -> SwcServiceDependency:
        """Creates (or returns an existing) SwcServiceDependency defining AUTOSAR Service requirements."""
        if not self.IsElementExists(short_name):
            event = SwcServiceDependency(self, short_name)
            self.addElement(event)
        return self.getElement(short_name, SwcServiceDependency)

    def getRteEvents(self) -> List[RTEEvent]:
        """Gets all RTEEvents specified for this SwcInternalBehavior, sorted by short name."""
        return sorted(filter(lambda c: isinstance(c, RTEEvent), self.elements), key=lambda e: e.short_name)

    def getOperationInvokedEvents(self) -> List[OperationInvokedEvent]:
        """Gets the OperationInvokedEvent RTEEvents owned by this behavior, sorted by short name."""
        return sorted(filter(lambda c: isinstance(c, OperationInvokedEvent), self.elements), key=lambda e: e.short_name)

    def getInitEvents(self) -> List[InitEvent]:
        """Gets the InitEvent RTEEvents owned by this behavior, sorted by short name."""
        return sorted(filter(lambda c: isinstance(c, InitEvent), self.elements), key=lambda e: e.short_name)

    def getTimingEvents(self) -> List[TimingEvent]:
        """Gets the TimingEvent RTEEvents owned by this behavior, sorted by short name."""
        return sorted(filter(lambda c: isinstance(c, TimingEvent), self.elements), key=lambda e: e.short_name)

    def getDataReceivedEvents(self) -> List[DataReceivedEvent]:
        """Gets the DataReceivedEvent RTEEvents owned by this behavior, sorted by short name."""
        return sorted(filter(lambda c: isinstance(c, DataReceivedEvent), self.elements), key=lambda e: e.short_name)

    def getSwcModeSwitchEvents(self) -> List[SwcModeSwitchEvent]:
        """Gets the SwcModeSwitchEvent RTEEvents owned by this behavior, sorted by short name."""
        return sorted(filter(lambda c: isinstance(c, SwcModeSwitchEvent), self.elements), key=lambda e: e.short_name)

    def getInternalTriggerOccurredEvents(self) -> List[InternalTriggerOccurredEvent]:
        """Gets the InternalTriggerOccurredEvent RTEEvents owned by this behavior, sorted by short name."""
        return sorted(filter(lambda c: isinstance(c, InternalTriggerOccurredEvent), self.elements), key=lambda e: e.short_name)

    def getModeSwitchedAckEvents(self) -> List[ModeSwitchedAckEvent]:
        """Gets the ModeSwitchedAckEvent RTEEvents owned by this behavior, sorted by short name."""
        return sorted(filter(lambda c: isinstance(c, ModeSwitchedAckEvent), self.elements), key=lambda e: e.short_name)

    def getBackgroundEvents(self) -> List[BackgroundEvent]:
        """Gets the BackgroundEvent RTEEvents owned by this behavior, sorted by short name."""
        return sorted(filter(lambda c: isinstance(c, BackgroundEvent), self.elements), key=lambda e: e.short_name)

    def getDataSendCompletedEvents(self) -> List[DataSendCompletedEvent]:
        """Gets the DataSendCompletedEvent RTEEvents owned by this behavior, sorted by short name."""
        return sorted(filter(lambda c: isinstance(c, DataSendCompletedEvent), self.elements), key=lambda e: e.short_name)

    def getSwcServiceDependencies(self) -> List[SwcServiceDependency]:
        """Gets the SwcServiceDependency objects defining AUTOSAR Service requirements, sorted by short name."""
        return sorted(filter(lambda c: isinstance(c, SwcServiceDependency), self.elements), key=lambda e: e.short_name)

    def getEvent(self, short_name: str) -> RTEEvent:
        """Gets the RTEEvent with the given short name from this behavior."""
        return self.getElement(short_name, RTEEvent)

    def getVariableDataPrototypes(self) -> List[VariableDataPrototype]:
        """Gets all VariableDataPrototype instances owned by this behavior, sorted by short name."""
        return sorted(filter(lambda c: isinstance(c, VariableDataPrototype), self.elements), key=lambda e: e.short_name)

    def createRunnableEntity(self, short_name: str) -> RunnableEntity:
        """Creates (or returns an existing) RunnableEntity specified for this SwcInternalBehavior."""
        if not self.IsElementExists(short_name):
            runnable = RunnableEntity(self, short_name)
            self.addElement(runnable)
        return self.getElement(short_name)

    def getRunnableEntities(self) -> List[RunnableEntity]:
        """Gets the RunnableEntity objects owned by this behavior, sorted by short name."""
        return sorted(filter(lambda c: isinstance(c, RunnableEntity), self.elements), key=lambda r: r.short_name)

    def getRunnableEntity(self, short_name: str) -> RunnableEntity:
        """Gets the RunnableEntity with the given short name from this behavior."""
        return self.getElement(short_name, RunnableEntity)

    def getSupportsMultipleInstantiation(self) -> Optional[Boolean]:
        """
        Indicates whether the corresponding software-component can be multiply
        instantiated on one ECU.
        """
        return self.supportsMultipleInstantiation

    def setSupportsMultipleInstantiation(self, value: Optional[Boolean]) -> "SwcInternalBehavior":
        """
        Indicates whether the corresponding software-component can be multiply
        instantiated on one ECU. A None value is a no-op and does not overwrite
        an existing supportsMultipleInstantiation.
        """
        if value is not None:
            self.supportsMultipleInstantiation = value
        return self

    def addInstantiationDataDefProps(self, value: Optional[InstantiationDataDefProps]) -> "SwcInternalBehavior":
        """
        Adds an InstantiationDataDefProps applying additional SwDataDefProps to
        a particular instantiation. A None value is a no-op and does not append
        to instantiationDataDefProps.
        """
        if value is not None:
            self.instantiationDataDefProps.append(value)
        return self

    def getInstantiationDataDefPropss(self) -> List[InstantiationDataDefProps]:
        """Gets the InstantiationDataDefProps objects owned by this behavior."""
        return self.instantiationDataDefProps

    def addVariationPointProxy(self, value: Optional[VariationPointProxy]) -> "SwcInternalBehavior":
        """
        Adds a VariationPointProxy (proxy of a variation point in the C/C++
        implementation). A None value is a no-op and does not append to
        variationPointProxies.
        """
        if value is not None:
            self.variationPointProxies.append(value)
        return self

    def getVariationPointProxies(self) -> List[VariationPointProxy]:
        """Gets the VariationPointProxy objects owned by this behavior."""
        return self.variationPointProxies
