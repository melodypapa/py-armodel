from ....M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.IncludedDataTypes import IncludedDataTypeSet
from ....M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ModeDeclarationGroup import IncludedModeDeclarationGroupSet
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARBoolean, ARFloat, ARNumerical
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from ....M2.AUTOSARTemplates.CommonStructure.InternalBehavior import ExecutableEntity
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Referrable
from ....M2.AUTOSARTemplates.CommonStructure.InternalBehavior import InternalBehavior
from abc import ABCMeta
from typing import List

class BswModuleCallPoint(Referrable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.contextLimitationRefs = []                 # type: List[RefType]

    def getContextLimitationRefs(self):
        return self.contextLimitationRefs

    def addContextLimitationRef(self, value):
        self.contextLimitationRefs.append(value)
        return self
    
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

class BswModuleEntity(ExecutableEntity, metaclass = ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == BswModuleEntity:
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
        self.accessedModeGroupRefs.append(value)
        return self

    def getActivationPointRefs(self):
        return self.activationPointRefs

    def addActivationPointRef(self, value):
        self.activationPointRefs.append(value)
        return self

    def getCallPoints(self):
        return self.callPoints

    def addCallPoint(self, value):
        self.callPoints.append(value)
        return self

    def getDataReceivePoint(self):
        return self.dataReceivePoints

    def addDataReceivePoint(self, value):
        self.dataReceivePoints.append(value)
        return self

    def getDataSendPoints(self):
        return self.dataSendPoints

    def addDataSendPoint(self, value):
        self.dataSendPoints.append(value)
        return self

    def getImplementedEntryRef(self):
        return self.implementedEntryRef

    def setImplementedEntryRef(self, value):
        self.implementedEntryRef = value
        return self

    def getIssuedTriggerRefs(self):
        return self.issuedTriggerRefs

    def addIssuedTriggerRefs(self, value):
        self.issuedTriggerRefs(value)
        return self

    def getManagedModeGroupRefs(self):
        return self.managedModeGroupRefs

    def addManagedModeGroupRef(self, value):
        self.managedModeGroupRefs = value
        return self

    def getSchedulerNamePrefixRef(self):
        return self.schedulerNamePrefixRef

    def setSchedulerNamePrefixRef(self, value):
        self.schedulerNamePrefixRef = value
        return self


class BswCalledEntity(BswModuleEntity):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class BswSchedulableEntity(BswModuleEntity):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class BswInterruptEntity(BswModuleEntity):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self._interrupt_category = ""
        self.interrupt_source = ""

    @property
    def interrupt_category(self) -> str:
        return self._interrupt_category

    @interrupt_category.setter
    def interrupt_category(self, value):
        if (value.upper() not in ("CAT1", "CAT2")):
            raise ValueError("Invalid interrupt category <%s> of %s" % (value, self.short_name))
        self._interrupt_category = value


class BswEvent(Identifiable, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == BswEvent:
            raise NotImplementedError("BswEvent is an abstract class.")
        super().__init__(parent, short_name)

        self.startsOnEventRef = None                    # type: RefType 


class BswOperationInvokedEvent(BswEvent):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class BswScheduleEvent(BswEvent, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == BswScheduleEvent:
            raise NotImplementedError("BswScheduleEvent is an abstract class.")
        super().__init__(parent, short_name)


class BswModeSwitchEvent(BswScheduleEvent):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self._activation = ""

    @property
    def activation(self) -> str:
        return self._activation

    @activation.setter
    def activation(self, value: str):
        if (value not in ()):
            raise ValueError("Invalid activation <%s> of BswModeSwitchEvent <%s>" % (value, self.short_name))
        self._activation = value


class BswTimingEvent(BswScheduleEvent):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.period = None          # type: ARFloat

    @property
    def periodMs(self) -> int:
        if self.period is not None:
            return int(self.period.value * 1000)
        return None


class BswDataReceivedEvent(BswScheduleEvent):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.data_ref = None                # type: RefType


class BswInternalTriggerOccurredEvent(BswScheduleEvent):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.event_source_ref = None                # type: RefType


class BswModeSwitchAckRequest(ARObject):
    def __init__(self):
        super().__init__()

        self.timeout = None                         # type: ARFloat


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


class BswInternalBehavior(InternalBehavior):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.entities = []                                  # type: List[BswModuleEntity]
        self.events = []                                    # type: List[BswEvent]
        self.mode_sender_policies = []                      # type: List[BswModeSenderPolicy]
        self.included_mode_declaration_group_sets = []      # type: List[IncludedModeDeclarationGroupSet]
        self.included_data_type_sets = []                       # type: List[IncludedDataTypeSet]

    def addModeSenderPolicy(self, policy: BswModeSenderPolicy):
        self.mode_sender_policies.append(policy)

    def getModeSenderPolicies(self) -> List[BswModeSenderPolicy]:
        return self.mode_sender_policies

    def createBswCalledEntity(self, short_name: str) -> BswCalledEntity:
        if (short_name not in self.elements):
            event = BswCalledEntity(self, short_name)
            self.elements[short_name] = event
            self.entities.append(event)
        return self.elements[short_name]

    def getBswCalledEntities(self) -> List[BswCalledEntity]:
        return list(filter(lambda a: isinstance(a, BswCalledEntity), self.elements.values()))

    def createBswSchedulableEntity(self, short_name: str) -> BswSchedulableEntity:
        if (short_name not in self.elements):
            event = BswSchedulableEntity(self, short_name)
            self.elements[short_name] = event
            self.entities.append(event)
        return self.elements[short_name]

    def getBswSchedulableEntities(self) -> List[BswSchedulableEntity]:
        return list(filter(lambda a: isinstance(a, BswSchedulableEntity), self.elements.values()))

    def getBswModuleEntities(self) -> List[BswModuleEntity]:
        return list(filter(lambda a: isinstance(a, BswModuleEntity), self.elements.values()))

    def createBswModeSwitchEvent(self, short_name: str) -> BswModeSwitchEvent:
        if (short_name not in self.elements):
            event = BswModeSwitchEvent(self, short_name)
            self.elements[short_name] = event
            self.events.append(event)
        return self.elements[short_name]

    def getBswModeSwitchEvents(self) -> List[BswModeSwitchEvent]:
        return list(filter(lambda a: isinstance(a, BswModeSwitchEvent), self.elements.values()))

    def createBswTimingEvent(self, short_name: str) -> BswTimingEvent:
        if (short_name not in self.elements):
            event = BswTimingEvent(self, short_name)
            self.elements[short_name] = event
            self.events.append(event)
        return self.elements[short_name]

    def getBswTimingEvents(self) -> List[BswTimingEvent]:
        return list(filter(lambda a: isinstance(a, BswTimingEvent), self.elements.values()))

    def createBswDataReceivedEvent(self, short_name: str) -> BswDataReceivedEvent:
        if (short_name not in self.elements):
            event = BswDataReceivedEvent(self, short_name)
            self.elements[short_name] = event
            self.events.append(event)
        return self.elements[short_name]

    def getBswDataReceivedEvents(self) -> List[BswDataReceivedEvent]:
        return list(filter(lambda a: isinstance(a, BswDataReceivedEvent), self.elements.values()))

    def createBswInternalTriggerOccurredEvent(self, short_name: str) -> BswInternalTriggerOccurredEvent:
        if (short_name not in self.elements):
            event = BswInternalTriggerOccurredEvent(self, short_name)
            self.elements[short_name] = event
            self.events.append(event)
        return self.elements[short_name]

    def getBswInternalTriggerOccurredEvents(self) -> List[BswInternalTriggerOccurredEvent]:
        return list(filter(lambda a: isinstance(a, BswInternalTriggerOccurredEvent), self.elements.values()))

    def getBswEvents(self) -> List[BswEvent]:
        return list(filter(lambda a: isinstance(a, BswEvent), self.elements.values()))

    def addIncludedModeDeclarationGroupSet(self, group_set: IncludedModeDeclarationGroupSet):
        self.included_mode_declaration_group_sets.append(group_set)

    def getIncludedModeDeclarationGroupSets(self) -> List[IncludedModeDeclarationGroupSet]:
        return self.included_mode_declaration_group_sets

    def addIncludedDataTypeSet(self, type_set: IncludedDataTypeSet):
        self.included_data_type_sets.append(type_set)

    def getIncludedDataTypeSets(self) -> List[IncludedDataTypeSet]:
        return self.included_data_type_sets

    