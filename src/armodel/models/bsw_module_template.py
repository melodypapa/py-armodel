from abc import ABCMeta
from typing import Dict, List

from .internal_behavior import IncludedDataTypeSet, InternalBehavior
from .general_structure import AtpStructureElement, ARObject, ARElement
from .ar_object import ARBoolean, ARFloat, ARLiteral, ARNumerical, ARPositiveInteger
from .common_structure import ExecutableEntity, IncludedModeDeclarationGroupSet, ModeDeclarationGroupPrototype, Identifiable
from .ar_ref import RefType

class BswModuleEntity(ExecutableEntity, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == BswModuleEntity:
            raise NotImplementedError("BswModuleEntity is an abstract class.")
        super().__init__(parent, short_name)

        self.accessedModeGroupRefs = []                 # type: List[RefType]
        self.activationPointRefs = []                   # type: List[RefType]
        self.implementedEntryRef = None                 # type: RefType
        self.managedModeGroupRefs = []                  # type: List[RefType]

    def getAccessedModeGroupRefs(self):
        return self.accessedModeGroupRefs

    def addAccessedModeGroupRefs(self, value):
        self.accessedModeGroupRefs.append(value)
        return self

    def getActivationPointRefs(self):
        return self.activationPointRefs

    def addActivationPointRefs(self, value):
        self.activationPointRefs.append(value)
        return self

    def getImplementedEntryRef(self):
        return self.implementedEntryRef

    def setImplementedEntryRef(self, value):
        self.implementedEntryRef = value
        return self

    def addManagedModeGroupRef(self, ref: RefType):
        self.managedModeGroupRefs.append(ref)

    def getManagedModeGroupRefs(self) -> List[RefType]:
        return self.managedModeGroupRefs

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

class BswModuleDescription(ARElement):
    '''
        Root element for the description of a single BSW module or BSW cluster. In case it
        describes a BSW module, the short name of this element equals the name of the
        BSW module.
        
        **attributes**:
         module_id              : MODULE-ID  
         implemented_entry_refs : PROVIDED-ENTRYS
    '''
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # MODULE-ID
        self.module_id = None                           # type: ARPositiveInteger           
        # PROVIDED-ENTRYS
        self._implementedEntryRefs = []                 # type: List[RefType]

        self.providedModeGroups   = {}                  # type: Dict[str, ModeDeclarationGroupPrototype]
        self.requiredModeGroups   = {}                  # type: Dict[str, ModeDeclarationGroupPrototype] 

    def addImplementedEntry(self, entry_ref: RefType):
        self._implementedEntryRefs.append(entry_ref)

    def getImplementedEntries(self) -> List[RefType]:
        return self._implementedEntryRefs

    #@property
    #def category(self) -> str:
    #    return ARElement.getCategory(self)

    #@category.setter
    #def category(self, value:str):
    #    if value is None:
    #        return
    #    if value not in ("BSW_MODULE", "BSW_CLUSTER", "LIBRARY"):
    #        raise ValueError("Invalid category <%s> of BswModuleDescription <%s>" % (value, self.short_name))
    #    ARElement.setCategory(self, value)

    def createProvidedModeGroup(self, short_name: str) -> ModeDeclarationGroupPrototype:
        if (short_name not in self.elements):
            prototype = ModeDeclarationGroupPrototype(self, short_name)
            self.elements[short_name] = prototype
            self.providedModeGroups[short_name] = prototype
        return self.elements[short_name]

    def getProvidedModeGroups(self) -> List[ModeDeclarationGroupPrototype]:
        return sorted(self.providedModeGroups.values(), key=lambda v: v.short_name) 

    def createRequiredModeGroup(self, short_name: str) -> ModeDeclarationGroupPrototype:
        if (short_name not in self.elements):
            prototype = ModeDeclarationGroupPrototype(self, short_name)
            self.elements[short_name] = prototype
            self.requiredModeGroups[short_name] = property
        return self.elements[short_name]

    def getRequiredModeGroups(self) -> List[ModeDeclarationGroupPrototype]:
        return sorted(self.requiredModeGroups.values(), key=lambda v: v.short_name) 

    def createBswInternalBehavior(self, short_name: str) -> BswInternalBehavior:
        '''
            Create the INTERNAL-BEHAVIORS tag
        '''
        if (short_name not in self.elements):
            prototype = BswInternalBehavior(self, short_name)
            self.elements[short_name] = prototype
        return self.elements[short_name]

    def getBswInternalBehaviors(self) -> List[BswInternalBehavior]:
        return list(filter(lambda a: isinstance(a, BswInternalBehavior), self.elements.values()))

class BswModuleEntry(ARElement):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.service_id = None                      # type: ARNumerical
        self.is_reentrant = None                    # type: ARBoolean
        self.is_synchronous = None                  # type: ARBoolean
        self.call_type = None                       # type: ARLiteral
        self._execution_context = None              # type: ARLiteral
        self._sw_service_impl_policy = None         # type: ARLiteral

    @property
    def execution_context(self):
        return self._execution_context

    @execution_context.setter
    def execution_context(self, value):
        if value.upper() not in ("HOOK", "INTERRUPT-CAT-1", "INTERRUPT-CAT-2", "TASK", "UNSPECIFIED"):
            raise ValueError("Invalid execution context <%s> of BswModuleEntry <%s>" % (value, self.short_name))
        self._execution_context = value

    @property
    def sw_service_impl_policy(self):
        return self._sw_service_impl_policy

    @sw_service_impl_policy.setter
    def sw_service_impl_policy(self, value):
        if value.upper() not in ("INLINE", "INLINE-CONDITIONAL", "MACRO", "STANDARD"):
            raise ValueError("Invalid SwServiceImplPolicy <%s> of BswModuleEntry <%s>" % (value, self.short_name))
        self._sw_service_impl_policy = value

    def __str__(self) -> str:
        result = []
        result.append("short_name             : %s" % self.short_name)
        if self.service_id != None:
            result.append("service_id             : %d" % self.service_id)
        if self.is_reentrant != None:
            result.append("is_reentrant           : %s" % self.is_reentrant)
        if self.is_synchronous != None:
            result.append("is_synchronous         : %s" % self.is_synchronous)
        if self.call_type != None:
            result.append("call_type              : %s" % self.call_type)
        if self.execution_context != None:
            result.append("execution_context      : %s" % self.execution_context)
        if self.sw_service_impl_policy != None:
            result.append("sw_service_impl_policy : %s" % self.sw_service_impl_policy)
            
        return "\n".join(result)