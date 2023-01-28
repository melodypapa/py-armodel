from abc import ABCMeta
from typing import List
from .general_structure import AtpStructureElement, ARObject, ARElement
from .common_structure import ExecutableEntity, ModeDeclarationGroupPrototype, InternalBehavior, Identifiable
from .ar_ref import RefType

class BswModuleEntity(ExecutableEntity, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == BswModuleEntity:
            raise NotImplementedError("BswModuleEntity is an abstract class.")
        super().__init__(parent, short_name)

        self.accessed_mode_group_refs = []          # Ref ModeDeclarationGroupPrototype     *
        self.activation_point_refs = []             # Ref BswInternalTriggeringPoint        *
        self.implemented_entry_ref = None           # type: RefType
        self.managed_mode_group_refs = []           # Ref ModeDeclarationGroupPrototype     *

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

        self.starts_on_event_ref = None         # type: RefType 

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
        
        self.period = 0.0

class BswDataReceivedEvent(BswScheduleEvent):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.data_ref = None                # type: RefType

class BswInternalTriggerOccurredEvent(BswScheduleEvent):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.event_source_ref = None        # type: RefType

class BswInternalBehavior(InternalBehavior):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

    def createBswCalledEntity(self, short_name: str) -> BswCalledEntity:
        if (short_name not in self.elements):
            event = BswCalledEntity(self, short_name)
            self.elements[short_name] = event
        return self.elements[short_name]

    def getBswCalledEntities(self) -> List[BswCalledEntity]:
        return list(filter(lambda a: isinstance(a, BswCalledEntity), self.elements.values()))

    def createBswSchedulableEntity(self, short_name: str) -> BswSchedulableEntity:
        if (short_name not in self.elements):
            event = BswSchedulableEntity(self, short_name)
            self.elements[short_name] = event
        return self.elements[short_name]

    def getBswSchedulableEntities(self) -> List[BswSchedulableEntity]:
        return list(filter(lambda a: isinstance(a, BswSchedulableEntity), self.elements.values()))

    def createBswModeSwitchEvent(self, short_name: str) -> BswModeSwitchEvent:
        if (short_name not in self.elements):
            event = BswModeSwitchEvent(self, short_name)
            self.elements[short_name] = event
        return self.elements[short_name]

    def getBswModeSwitchEvents(self) -> List[BswModeSwitchEvent]:
        return list(filter(lambda a: isinstance(a, BswModeSwitchEvent), self.elements.values()))

    def createBswTimingEvent(self, short_name: str) -> BswTimingEvent:
        if (short_name not in self.elements):
            event = BswTimingEvent(self, short_name)
            self.elements[short_name] = event
        return self.elements[short_name]

    def getBswTimingEvents(self) -> List[BswTimingEvent]:
        return list(filter(lambda a: isinstance(a, BswTimingEvent), self.elements.values()))

    def createBswDataReceivedEvent(self, short_name: str) -> BswDataReceivedEvent:
        if (short_name not in self.elements):
            event = BswDataReceivedEvent(self, short_name)
            self.elements[short_name] = event
        return self.elements[short_name]

    def getBswDataReceivedEvents(self) -> List[BswDataReceivedEvent]:
        return list(filter(lambda a: isinstance(a, BswDataReceivedEvent), self.elements.values()))

    def createBswInternalTriggerOccurredEvent(self, short_name: str) -> BswInternalTriggerOccurredEvent:
        if (short_name not in self.elements):
            event = BswInternalTriggerOccurredEvent(self, short_name)
            self.elements[short_name] = event
        return self.elements[short_name]

    def getBswInternalTriggerOccurredEvents(self) -> List[BswInternalTriggerOccurredEvent]:
        return list(filter(lambda a: isinstance(a, BswInternalTriggerOccurredEvent), self.elements.values()))

class BswModuleDescription(AtpStructureElement):
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
        self.module_id = 0
        # PROVIDED-ENTRYS
        self.implemented_entry_refs = []                # type: List[RefType]

        self.provided_mode_groups   = {}                # ModeDeclarationGroupPrototype         *
        self.required_mode_groups   = {}                # ModeDeclarationGroupPrototype         * 

    @property
    def category(self) -> str:
        return self._category

    @category.setter
    def category(self, value:str):
        if value not in ("BSW_MODULE", "BSW_CLUSTER", "LIBRARY"):
            raise ValueError("Invalid category <%s> of BswModuleDescription <%s>" % (value, self.short_name))
        self._category = value

    def createProvidedModeGroup(self, short_name: str) -> ModeDeclarationGroupPrototype:
        if (short_name not in self.elements):
            prototype = ModeDeclarationGroupPrototype(self, short_name)
            self.elements[short_name] = prototype
            self.provided_mode_groups[short_name] = prototype
        return self.elements[short_name]

    def getProvidedModeGroups(self) -> List[ModeDeclarationGroupPrototype]:
        return sorted(self.provided_mode_groups.values(), key=lambda v: v.short_name) 

    def createRequiredModeGroup(self, short_name: str) -> ModeDeclarationGroupPrototype:
        if (short_name not in self.elements):
            prototype = ModeDeclarationGroupPrototype(self, short_name)
            self.elements[short_name] = prototype
            self.required_mode_groups[short_name] = property
        return self.elements[short_name]

    def getRequiredModeGroups(self) -> List[ModeDeclarationGroupPrototype]:
        return sorted(self.required_mode_groups.values(), key=lambda v: v.short_name) 

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

        self.service_id = None                  # type: int
        self.is_reentrant = None                # type: bool
        self.is_synchronous = None              # type: bool
        self.call_type = None                   # type: str
        self._execution_context = None          # type: str
        self._sw_service_impl_policy = None     # type: str

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