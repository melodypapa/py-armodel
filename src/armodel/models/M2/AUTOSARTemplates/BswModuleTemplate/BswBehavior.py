from abc import ABCMeta
from typing import List

from ....M2.MSR.DataDictionary.DataDefProperties import SwImplPolicyEnum
from ....M2.AUTOSARTemplates.CommonStructure.InternalBehavior import ExecutableEntity
from ....M2.AUTOSARTemplates.CommonStructure.InternalBehavior import InternalBehavior
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARBoolean, AREnum, ARFloat, ARNumerical, Boolean
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, String, TimeValue
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Referrable
from ....M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import VariableDataPrototype
from ....M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.IncludedDataTypes import IncludedDataTypeSet
from ....M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ModeDeclarationGroup import IncludedModeDeclarationGroupSet


class BswModuleCallPoint(Referrable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.contextLimitationRefs = []                 # type: List[RefType]

    def getContextLimitationRefs(self):
        return self.contextLimitationRefs

    def addContextLimitationRef(self, value):
        self.contextLimitationRefs.append(value)
        return self


class BswAsynchronousServerCallPoint(BswModuleCallPoint):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.calledEntryRef = None                                          # type: RefType

    def getCalledEntryRef(self):
        return self.calledEntryRef

    def setCalledEntryRef(self, value):
        if value is not None:
            self.calledEntryRef = value
        return self


class BswDirectCallPoint(BswModuleCallPoint):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.calledEntryRef = None                                          # type: RefType
        self.calledFromWithinExclusiveAreaRef = None                        # type: RefType

    def getCalledEntryRef(self):
        return self.calledEntryRef

    def setCalledEntryRef(self, value):
        if value is not None:
            self.calledEntryRef = value
        return self

    def getCalledFromWithinExclusiveAreaRef(self):
        return self.calledFromWithinExclusiveAreaRef

    def setCalledFromWithinExclusiveAreaRef(self, value):
        if value is not None:
            self.calledFromWithinExclusiveAreaRef = value
        return self
    

class BswSynchronousServerCallPoint(BswModuleCallPoint):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.calledEntryRef = None                                          # type: RefType
        self.calledFromWithinExclusiveAreaRef = None                        # type: RefType

    def getCalledEntryRef(self):
        return self.calledEntryRef

    def setCalledEntryRef(self, value):
        if value is not None:
            self.calledEntryRef = value
        return self

    def getCalledFromWithinExclusiveAreaRef(self):
        return self.calledFromWithinExclusiveAreaRef

    def setCalledFromWithinExclusiveAreaRef(self, value):
        if value is not None:
            self.calledFromWithinExclusiveAreaRef = value
        return self


class BswAsynchronousServerCallResultPoint(BswModuleCallPoint):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.asynchronousServerCallPointRef = None                          # type: RefType


class BswVariableAccess(Referrable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.accessedVariableRef = None                     # type: RefType
        self.contextLimitationRefs = []                     # type: List[RefType]

    def getAccessedVariableRef(self):
        return self.accessedVariableRef

    def setAccessedVariableRef(self, value):
        self.accessedVariableRef = value
        return self

    def getContextLimitationRefs(self):
        return self.contextLimitationRefs

    def addContextLimitationRef(self, value):
        self.contextLimitationRefs.append(value)
        return self


class BswModuleEntity(ExecutableEntity, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is BswModuleEntity:
            raise NotImplementedError("BswModuleEntity is an abstract class.")
        super().__init__(parent, short_name)

        self.accessedModeGroupRefs = []                 # type: List[RefType]
        self.activationPointRefs = []                   # type: List[RefType]
        self.callPoints = []                            # type: List[BswModuleCallPoint]
        self.dataReceivePoints = []                     # type: List[BswVariableAccess]
        self.dataSendPoints = []                        # type: List[BswVariableAccess]
        self.implementedEntryRef = None                 # type: RefType
        self.issuedTriggerRefs = []                     # type: List[RefType]
        self.managedModeGroupRefs = []                  # type: List[RefType]
        self.schedulerNamePrefixRef = None              # type: List[RefType]

    def getAccessedModeGroupRefs(self):
        return self.accessedModeGroupRefs

    def addAccessedModeGroupRef(self, value):
        if value is not None:
            self.accessedModeGroupRefs.append(value)
        return self

    def getActivationPointRefs(self):
        return self.activationPointRefs

    def addActivationPointRef(self, value):
        if value is not None:
            self.activationPointRefs.append(value)
        return self

    def getCallPoints(self):
        return self.callPoints

    def createBswAsynchronousServerCallPoint(self, short_name):
        if (not self.IsElementExists(short_name)):
            access = BswAsynchronousServerCallPoint(self, short_name)
            self.addElement(access)
            self.callPoints.append(access)
        return self.getElement(short_name)

    def getDataReceivePoints(self):
        return self.dataReceivePoints

    def createDataReceivePoint(self, short_name: str) -> BswVariableAccess:
        if (not self.IsElementExists(short_name)):
            access = BswVariableAccess(self, short_name)
            self.addElement(access)
            self.dataReceivePoints.append(access)
        return self.getElement(short_name, BswVariableAccess)

    def getDataSendPoints(self):
        return self.dataSendPoints

    def createDataSendPoint(self, short_name: str) -> BswVariableAccess:
        if (not self.IsElementExists(short_name)):
            access = BswVariableAccess(self, short_name)
            self.addElement(access)
            self.dataSendPoints.append(access)
        return self.getElement(short_name, BswVariableAccess)

    def getImplementedEntryRef(self):
        return self.implementedEntryRef

    def setImplementedEntryRef(self, value):
        if value is not None:
            self.implementedEntryRef = value
        return self

    def getIssuedTriggerRefs(self):
        return self.issuedTriggerRefs

    def addIssuedTriggerRef(self, value):
        if value is not None:
            self.issuedTriggerRefs.append(value)
        return self

    def getManagedModeGroupRefs(self):
        return self.managedModeGroupRefs

    def addManagedModeGroupRef(self, value):
        if value is not None:
            self.managedModeGroupRefs.append(value)
        return self

    def getSchedulerNamePrefixRef(self):
        return self.schedulerNamePrefixRef

    def setSchedulerNamePrefixRef(self, value):
        if value is not None:
            self.schedulerNamePrefixRef = value
        return self


class BswCalledEntity(BswModuleEntity):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class BswSchedulableEntity(BswModuleEntity):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class BswInterruptCategory(AREnum):
    CAT1 = "cat1"
    CAT2 = "cat2"

    def __init__(self):
        super().__init__((
            BswInterruptCategory.CAT1,
            BswInterruptCategory.CAT2,
        ))


class BswInterruptEntity(BswModuleEntity):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.interruptCategory = None               # type: BswInterruptCategory
        self.interruptSource = None                 # type: String

    def getInterruptCategory(self):
        return self.interruptCategory

    def setInterruptCategory(self, value):
        self.interruptCategory = value
        return self

    def getInterruptSource(self):
        return self.interruptSource

    def setInterruptSource(self, value):
        self.interruptSource = value
        return self


class BswEvent(Identifiable, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is BswEvent:
            raise NotImplementedError("BswEvent is an abstract class.")
        super().__init__(parent, short_name)

        self.startsOnEventRef = None                    # type: RefType

    def getStartsOnEventRef(self):
        return self.startsOnEventRef

    def setStartsOnEventRef(self, value):
        self.startsOnEventRef = value
        return self


class BswOperationInvokedEvent(BswEvent):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.entryRef = None                            # type: RefType

    def getEntryRef(self):
        return self.entryRef

    def setEntryRef(self, value):
        if value is not None:
            self.entryRef = value
        return self


class BswScheduleEvent(BswEvent, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is BswScheduleEvent:
            raise NotImplementedError("BswScheduleEvent is an abstract class.")
        super().__init__(parent, short_name)


class BswModeSwitchEvent(BswScheduleEvent):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.activation = None

    def getActivation(self):
        return self.activation

    def setActivation(self, value):
        self.activation = value
        return self


class BswTimingEvent(BswScheduleEvent):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.period = None          # type: TimeValue

    def getPeriod(self):
        return self.period

    def setPeriod(self, value):
        if not (value is None and self.period is not None):
            self.period = value
        return self

    @property
    def periodMs(self) -> int:
        if self.period is not None:
            return int(self.period.value * 1000)
        return None


class BswDataReceivedEvent(BswScheduleEvent):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.dataRef = None                # type: RefType

    def getDataRef(self):
        return self.dataRef

    def setDataRef(self, value):
        self.dataRef = value
        return self


class BswInternalTriggerOccurredEvent(BswScheduleEvent):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.eventSourceRef = None                # type: RefType

    def getEventSourceRef(self):
        return self.eventSourceRef

    def setEventSourceRef(self, value):
        self.eventSourceRef = value
        return self
    

class BswModeSwitchAckRequest(ARObject):
    def __init__(self):
        super().__init__()

        self.timeout = None                         # type: ARFloat

    def getTimeout(self):
        return self.timeout

    def setTimeout(self, value):
        self.timeout = value
        return self


class BswModeSenderPolicy(ARObject):
    def __init__(self):
        super().__init__()

        self.ack_request = None                     # type: BswModeSwitchAckRequest
        self.enhanced_mode_api = None               # type: ARBoolean
        self._provided_mode_group_ref = None        # type: RefType
        self._queue_length = None                   # type: ARNumerical

    def setProvidedModeGroupRef(self, ref: RefType):
        self._provided_mode_group_ref = ref
        return self

    def getProvidedModeGroupRef(self) -> RefType:
        return self._provided_mode_group_ref

    def setQueueLength(self, length: any):
        if isinstance(length, ARNumerical):
            self._queue_length = length
        elif isinstance(length, int):
            self._queue_length = ARNumerical()
            self._queue_length.setValue(length)
        else:
            raise ValueError("Unsupported type <%s>" % type(length))

    def getQueueLength(self) -> ARNumerical:
        return self._queue_length


class BswBackgroundEvent(BswScheduleEvent):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)


class BswOsTaskExecutionEvent(BswScheduleEvent):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)


class BswExternalTriggerOccurredEvent(BswScheduleEvent):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.triggerRef = None                                                  # type: RefType

    def getTriggerRef(self):
        return self.triggerRef

    def setTriggerRef(self, value):
        if value is not None:
            self.triggerRef = value
        return self

    
class BswApiOptions(ARObject, metaclass=ABCMeta):
    def __init__(self):
        if type(self) is BswApiOptions:
            raise NotImplementedError("BswApiOptions is an abstract class.")

        super().__init__()

        self.enableTakeAddress = None                                           # type: Boolean

    def getEnableTakeAddress(self):
        return self.enableTakeAddress

    def setEnableTakeAddress(self, value):
        if value is not None:
            self.enableTakeAddress = value
        return self


class BswDataReceptionPolicy(BswApiOptions, metaclass=ABCMeta):
    def __init__(self):
        if type(self) is BswDataReceptionPolicy:
            raise NotImplementedError("BswDataReceptionPolicy is an abstract class.")

        super().__init__()

        self.receivedDataRef = None                                             # type: RefType

    def getReceivedDataRef(self):
        return self.receivedDataRef

    def setReceivedDataRef(self, value):
        if value is not None:
            self.receivedDataRef = value
        return self


class BswQueuedDataReceptionPolicy(BswDataReceptionPolicy):
    def __init__(self):
        super().__init__()

        self.queueLength = None                                                 # type: PositiveInteger

    def getQueueLength(self):
        return self.queueLength

    def setQueueLength(self, value):
        if value is not None:
            self.queueLength = value
        return self


class BswInternalTriggeringPoint(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.swImplPolicy = None                                                # type: SwImplPolicyEnum

    def getSwImplPolicy(self):
        return self.swImplPolicy

    def setSwImplPolicy(self, value):
        if value is not None:
            self.swImplPolicy = value
        return self


class BswInternalBehavior(InternalBehavior):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.arTypedPerInstanceMemories = []                                    # type: List[VariableDataPrototype]
        self.bswPerInstanceMemoryPolicies = []                                  # type: List[BswPerInstanceMemoryPolicy]
        self.clientPolicies = []                                                # type: List[BswClientPolicy]
        self.distinguishedPartitions = []                                       # type: List[BswDistinguishedPartition]
        self.entities = []                                                      # type: List[BswModuleEntity]
        self.events = []                                                        # type: List[BswEvent]
        self.exclusiveAreaPolicies = []                                         # type: List[BswExclusiveAreaPolicy]
        self.includedDataTypeSets = []                                          # type: List[IncludedDataTypeSet]
        self.includedModeDeclarationGroupSets = []                              # type: List[IncludedModeDeclarationGroupSet]
        self.internalTriggeringPoints = []                                      # type: List[BswInternalTriggeringPoint]
        self.internalTriggeringPointPolicies = []                               # type: List[BswInternalTriggeringPointPolicy]
        self.modeReceiverPolicies = []                                          # type: List[BswModeReceiverPolicy]
        self.modeSenderPolicies = []                                            # type: List[BswModeSenderPolicy]
        self.parameterPolicies = []                                              # type: List[BswParameterPolicy]
        self.perInstanceParameters = []                                         # type: List[ParameterDataPrototype]
        self.receptionPolicies = []                                             # type: List[BswDataReceptionPolicy]
        self.releasedTriggerPolicies = []                                       # type: List[BswReleasedTriggerPolicy]
        self.schedulerNamePrefixes = []                                         # type: List[BswSchedulerNamePrefix]
        self.sendPolicies = []                                                  # type: List[BswDataSendPolicy]
        self.serviceDependencies = []                                           # type: List[BswServiceDependency]
        self.triggerDirectImplementations = []                                  # type: List[BswTriggerDirectImplementation]
        self.variationPointProxies = []                                         # type: List[VariationPointProxy]

    def getArTypedPerInstanceMemories(self):
        return self.arTypedPerInstanceMemories

    def setArTypedPerInstanceMemories(self, value):
        if value is not None:
            self.arTypedPerInstanceMemories = value
        return self

    def getBswPerInstanceMemoryPolicies(self):
        return self.bswPerInstanceMemoryPolicies

    def setBswPerInstanceMemoryPolicies(self, value):
        if value is not None:
            self.bswPerInstanceMemoryPolicies = value
        return self

    def getClientPolicies(self):
        return self.clientPolicies

    def setClientPolicies(self, value):
        if value is not None:
            self.clientPolicies = value
        return self

    def getDistinguishedPartitions(self):
        return self.distinguishedPartitions

    def setDistinguishedPartitions(self, value):
        if value is not None:
            self.distinguishedPartitions = value
        return self

    def getExclusiveAreaPolicies(self):
        return self.exclusiveAreaPolicies

    def setExclusiveAreaPolicies(self, value):
        if value is not None:
            self.exclusiveAreaPolicies = value
        return self

    def getInternalTriggeringPoints(self):
        return self.internalTriggeringPoints

    def createBswInternalTriggeringPoint(self, short_name: str) -> BswInternalTriggeringPoint:
        if not self.IsElementExists(short_name):
            entity = BswInternalTriggeringPoint(self, short_name)
            self.addElement(entity)
            self.internalTriggeringPoints.append(entity)
        return self.getElement(short_name)

    def getInternalTriggeringPointPolicies(self):
        return self.internalTriggeringPointPolicies

    def setInternalTriggeringPointPolicies(self, value):
        if value is not None:
            self.internalTriggeringPointPolicies = value
        return self

    def getModeReceiverPolicies(self):
        return self.modeReceiverPolicies

    def setModeSenderPolicies(self, value):
        if value is not None:
            self.modeSenderPolicies = value
        return self

    def getParameterPolicies(self):
        return self.parameterPolicies

    def setParameterPolicies(self, value):
        if value is not None:
            self.parameterPolicies = value
        return self

    def getPerInstanceParameters(self):
        return self.perInstanceParameters

    def setPerInstanceParameters(self, value):
        if value is not None:
            self.perInstanceParameters = value
        return self

    def getReceptionPolicies(self):
        return self.receptionPolicies

    def addReceptionPolicy(self, value):
        if value is not None:
            self.receptionPolicies.append(value)
        return self

    def getReleasedTriggerPolicies(self):
        return self.releasedTriggerPolicies

    def setReleasedTriggerPolicies(self, value):
        if value is not None:
            self.releasedTriggerPolicies = value
        return self

    def getSchedulerNamePrefixes(self):
        return self.schedulerNamePrefixes

    def setSchedulerNamePrefixes(self, value):
        if value is not None:
            self.schedulerNamePrefixes = value
        return self

    def getSendPolicies(self):
        return self.sendPolicies

    def setSendPolicies(self, value):
        if value is not None:
            self.sendPolicies = value
        return self

    def getServiceDependencies(self):
        return self.serviceDependencies

    def setServiceDependencies(self, value):
        if value is not None:
            self.serviceDependencies = value
        return self

    def getTriggerDirectImplementations(self):
        return self.triggerDirectImplementations

    def setTriggerDirectImplementations(self, value):
        if value is not None:
            self.triggerDirectImplementations = value
        return self

    def getVariationPointProxies(self):
        return self.variationPointProxies

    def setVariationPointProxies(self, value):
        if value is not None:
            self.variationPointProxies = value
        return self
    
    def addModeSenderPolicy(self, policy: BswModeSenderPolicy):
        self.modeReceiverPolicies.append(policy)

    def getModeSenderPolicies(self) -> List[BswModeSenderPolicy]:
        return self.modeReceiverPolicies

    def createBswCalledEntity(self, short_name: str) -> BswCalledEntity:
        if not self.IsElementExists(short_name):
            entity = BswCalledEntity(self, short_name)
            self.addElement(entity)
            self.entities.append(entity)
        return self.getElement(short_name)

    def getBswCalledEntities(self) -> List[BswCalledEntity]:
        return list(filter(lambda a: isinstance(a, BswCalledEntity), self.elements))

    def createBswSchedulableEntity(self, short_name: str) -> BswSchedulableEntity:
        if not self.IsElementExists(short_name):
            entity = BswSchedulableEntity(self, short_name)
            self.addElement(entity)
            self.entities.append(entity)
        return self.getElement(short_name)

    def getBswSchedulableEntities(self) -> List[BswSchedulableEntity]:
        return list(filter(lambda a: isinstance(a, BswSchedulableEntity), self.elements))
    
    def createBswInterruptEntity(self, short_name: str) -> BswInterruptEntity:
        if not self.IsElementExists(short_name):
            entity = BswInterruptEntity(self, short_name)
            self.addElement(entity)
            self.entities.append(entity)
        return self.getElement(short_name)

    def getBswInterruptEntities(self) -> List[BswInterruptEntity]:
        return list(filter(lambda a: isinstance(a, BswInterruptEntity), self.elements))

    def getBswModuleEntities(self) -> List[BswModuleEntity]:
        return list(filter(lambda a: isinstance(a, BswModuleEntity), self.elements))

    def createBswModeSwitchEvent(self, short_name: str) -> BswModeSwitchEvent:
        if not self.IsElementExists(short_name):
            event = BswModeSwitchEvent(self, short_name)
            self.addElement(event)
            self.events.append(event)
        return self.getElement(short_name)

    def getBswModeSwitchEvents(self) -> List[BswModeSwitchEvent]:
        return list(filter(lambda a: isinstance(a, BswModeSwitchEvent), self.elements))

    def createBswTimingEvent(self, short_name: str) -> BswTimingEvent:
        if not self.IsElementExists(short_name):
            event = BswTimingEvent(self, short_name)
            self.addElement(event)
            self.events.append(event)
        return self.getElement(short_name)

    def getBswTimingEvents(self) -> List[BswTimingEvent]:
        return list(filter(lambda a: isinstance(a, BswTimingEvent), self.elements))

    def createBswDataReceivedEvent(self, short_name: str) -> BswDataReceivedEvent:
        if not self.IsElementExists(short_name):
            event = BswDataReceivedEvent(self, short_name)
            self.addElement(event)
            self.events.append(event)
        return self.getElement(short_name)

    def getBswDataReceivedEvents(self) -> List[BswDataReceivedEvent]:
        return list(filter(lambda a: isinstance(a, BswDataReceivedEvent), self.elements))

    def createBswInternalTriggerOccurredEvent(self, short_name: str) -> BswInternalTriggerOccurredEvent:
        if not self.IsElementExists(short_name):
            event = BswInternalTriggerOccurredEvent(self, short_name)
            self.addElement(event)
            self.events.append(event)
        return self.getElement(short_name)
    
    def getBswInternalTriggerOccurredEvents(self) -> List[BswInternalTriggerOccurredEvent]:
        return list(filter(lambda a: isinstance(a, BswInternalTriggerOccurredEvent), self.elements))
    
    def createBswExternalTriggerOccurredEvent(self, short_name: str) -> BswExternalTriggerOccurredEvent:
        if not self.IsElementExists(short_name):
            event = BswExternalTriggerOccurredEvent(self, short_name)
            self.addElement(event)
            self.events.append(event)
        return self.getElement(short_name)
    
    def getBswOperationInvokedEvents(self) -> List[BswOperationInvokedEvent]:
        return list(filter(lambda a: isinstance(a, BswOperationInvokedEvent), self.elements))
    
    def createBswOperationInvokedEvent(self, short_name: str) -> BswOperationInvokedEvent:
        if not self.IsElementExists(short_name):
            event = BswOperationInvokedEvent(self, short_name)
            self.addElement(event)
            self.events.append(event)
        return self.getElement(short_name)
    
    def getBswExternalTriggerOccurredEvents(self) -> List[BswExternalTriggerOccurredEvent]:
        return list(filter(lambda a: isinstance(a, BswExternalTriggerOccurredEvent), self.elements))
    
    def createBswBackgroundEvent(self, short_name: str) -> BswBackgroundEvent:
        if not self.IsElementExists(short_name):
            event = BswBackgroundEvent(self, short_name)
            self.addElement(event)
            self.events.append(event)
        return self.getElement(short_name)
    
    def getBswBackgroundEvents(self) -> List[BswBackgroundEvent]:
        return list(filter(lambda a: isinstance(a, BswBackgroundEvent), self.elements))

    def getBswEvents(self) -> List[BswEvent]:
        return list(filter(lambda a: isinstance(a, BswEvent), self.elements))

    def addIncludedModeDeclarationGroupSet(self, group_set: IncludedModeDeclarationGroupSet):
        self.includedModeDeclarationGroupSets.append(group_set)

    def getIncludedModeDeclarationGroupSets(self) -> List[IncludedModeDeclarationGroupSet]:
        return self.includedModeDeclarationGroupSets

    def addIncludedDataTypeSet(self, type_set: IncludedDataTypeSet):
        self.includedDataTypeSets.append(type_set)

    def getIncludedDataTypeSets(self) -> List[IncludedDataTypeSet]:
        return self.includedDataTypeSets

    