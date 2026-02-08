"""
This module contains classes for representing AUTOSAR Basic Software (BSW) module behavior.
BSW behavior describes how BSW modules execute, including their entities, events, and execution policies.

These classes are used to model:
- BSW module entities and their call points
- Different types of events that trigger execution
- Variable access patterns and data policies
- Internal behavior of BSW modules
"""

from abc import ABC
from typing import List

from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import (
    AbstractEvent,
    ExecutableEntity,
    InternalBehavior,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import (
    ModeActivationKind,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARBoolean,
    AREnum,
    ARFloat,
    ARNumerical,
    Boolean,
    PositiveInteger,
    RefType,
    String,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import (
    VariableDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.IncludedDataTypes import (
    IncludedDataTypeSet,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ModeDeclarationGroup import (
    IncludedModeDeclarationGroupSet,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import (
    SwImplPolicyEnum,
)


class BswModuleCallPoint(Referrable, ABC):
    """
    Represents a call point for a BSW module, which defines how the module can be called.
    This is an abstract base class for different types of call points.
    """

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the BswModuleCallPoint with a parent and short name.
        Raises TypeError if this abstract class is instantiated directly.

        Args:
            parent: The parent ARObject that contains this call point
            short_name: The unique short name of this call point
        """
        if type(self) is BswModuleCallPoint:
            raise TypeError("BswModuleCallPoint is an abstract class.")
        super().__init__(parent, short_name)

        # List of context limitation references that apply to this call point
        self.contextLimitationRefs: List[RefType] = []

    def getContextLimitationRefs(self):
        """
        Gets the list of context limitation references for this call point.

        Returns:
            List of context limitation references
        """
        return self.contextLimitationRefs

    def addContextLimitationRef(self, value):
        """
        Adds a context limitation reference to this call point.

        Args:
            value: The context limitation reference to add

        Returns:
            self for method chaining
        """
        self.contextLimitationRefs.append(value)
        return self


class BswAsynchronousServerCallPoint(BswModuleCallPoint):
    """
    Represents an asynchronous server call point in a BSW module.
    This call point is used when the server operation is executed asynchronously.
    """

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the BswAsynchronousServerCallPoint with a parent and short name.

        Args:
            parent: The parent ARObject that contains this call point
            short_name: The unique short name of this call point
        """
        super().__init__(parent, short_name)

        # Reference to the entry that is called by this asynchronous call point
        self.calledEntryRef: RefType = None

    def getCalledEntryRef(self):
        """
        Gets the reference to the entry that is called by this call point.

        Returns:
            Reference to the called entry
        """
        return self.calledEntryRef

    def setCalledEntryRef(self, value):
        """
        Sets the reference to the entry that is called by this call point.
        Only sets the value if it is not None.

        Args:
            value: The entry reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.calledEntryRef = value
        return self


class BswDirectCallPoint(BswModuleCallPoint):
    """
    Represents a direct call point in a BSW module.
    This call point is used for direct synchronous calls to BSW module entries.
    """

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the BswDirectCallPoint with a parent and short name.

        Args:
            parent: The parent ARObject that contains this call point
            short_name: The unique short name of this call point
        """
        super().__init__(parent, short_name)

        # Reference to the entry that is called by this direct call point
        self.calledEntryRef: RefType = None
        # Reference to an exclusive area from which this call is made
        self.calledFromWithinExclusiveAreaRef: RefType = None

    def getCalledEntryRef(self):
        """
        Gets the reference to the entry that is called by this direct call point.

        Returns:
            Reference to the called entry
        """
        return self.calledEntryRef

    def setCalledEntryRef(self, value):
        """
        Sets the reference to the entry that is called by this direct call point.
        Only sets the value if it is not None.

        Args:
            value: The entry reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.calledEntryRef = value
        return self

    def getCalledFromWithinExclusiveAreaRef(self):
        """
        Gets the reference to the exclusive area from which this call is made.

        Returns:
            Reference to the exclusive area
        """
        return self.calledFromWithinExclusiveAreaRef

    def setCalledFromWithinExclusiveAreaRef(self, value):
        """
        Sets the reference to the exclusive area from which this call is made.
        Only sets the value if it is not None.

        Args:
            value: The exclusive area reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.calledFromWithinExclusiveAreaRef = value
        return self


class BswSynchronousServerCallPoint(BswModuleCallPoint):
    """
    Represents a synchronous server call point in a BSW module.
    This call point is used when the server operation is executed synchronously.
    """

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the BswSynchronousServerCallPoint with a parent and short name.

        Args:
            parent: The parent ARObject that contains this call point
            short_name: The unique short name of this call point
        """
        super().__init__(parent, short_name)

        # Reference to the entry that is called by this synchronous call point
        self.calledEntryRef: RefType = None
        # Reference to an exclusive area from which this call is made
        self.calledFromWithinExclusiveAreaRef: RefType = None

    def getCalledEntryRef(self):
        """
        Gets the reference to the entry that is called by this synchronous call point.

        Returns:
            Reference to the called entry
        """
        return self.calledEntryRef

    def setCalledEntryRef(self, value):
        """
        Sets the reference to the entry that is called by this synchronous call point.
        Only sets the value if it is not None.

        Args:
            value: The entry reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.calledEntryRef = value
        return self

    def getCalledFromWithinExclusiveAreaRef(self):
        """
        Gets the reference to the exclusive area from which this call is made.

        Returns:
            Reference to the exclusive area
        """
        return self.calledFromWithinExclusiveAreaRef

    def setCalledFromWithinExclusiveAreaRef(self, value):
        """
        Sets the reference to the exclusive area from which this call is made.
        Only sets the value if it is not None.

        Args:
            value: The exclusive area reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.calledFromWithinExclusiveAreaRef = value
        return self


class BswAsynchronousServerCallResultPoint(BswModuleCallPoint):
    """
    Represents a result point for an asynchronous server call in a BSW module.
    This defines where the result of the asynchronous call is handled.
    """

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the BswAsynchronousServerCallResultPoint with a parent and short name.

        Args:
            parent: The parent ARObject that contains this call point
            short_name: The unique short name of this call point
        """
        super().__init__(parent, short_name)

        # Reference to the asynchronous server call point
        self.asynchronousServerCallPointRef: RefType = None


class BswVariableAccess(Referrable):
    """
    Represents access to a variable by a BSW module entity.
    This class defines how a BSW module accesses variables during execution.
    """

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the BswVariableAccess with a parent and short name.

        Args:
            parent: The parent ARObject that contains this variable access
            short_name: The unique short name of this variable access
        """
        super().__init__(parent, short_name)

        # Reference to the variable being accessed
        self.accessedVariableRef: RefType = None
        # List of context limitation references that apply to this variable access
        self.contextLimitationRefs: List[RefType] = []

    def getAccessedVariableRef(self):
        """
        Gets the reference to the variable being accessed.

        Returns:
            Reference to the accessed variable
        """
        return self.accessedVariableRef

    def setAccessedVariableRef(self, value):
        """
        Sets the reference to the variable being accessed.

        Args:
            value: The variable reference to set

        Returns:
            self for method chaining
        """
        self.accessedVariableRef = value
        return self

    def getContextLimitationRefs(self):
        """
        Gets the list of context limitation references for this variable access.

        Returns:
            List of context limitation references
        """
        return self.contextLimitationRefs

    def addContextLimitationRef(self, value):
        """
        Adds a context limitation reference to this variable access.

        Args:
            value: The context limitation reference to add

        Returns:
            self for method chaining
        """
        self.contextLimitationRefs.append(value)
        return self


class BswDistinguishedPartition(Referrable):
    """
    Each instance of this meta-class represents an abstract partition in which context
    the code of the enclosing BswModuleBehavior can be executed. The intended use case
    is to distinguish between several partitions in order to implement different behavior
    per partition, for example to behave either as a master or satellite in a multicore
    ECU with shared BSW code.
    """

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the BswDistinguishedPartition with a parent and short name.

        Args:
            parent: The parent ARObject that contains this distinguished partition
            short_name: The unique short name of this distinguished partition
        """
        super().__init__(parent, short_name)


class BswModuleEntity(ExecutableEntity, ABC):
    """
    Abstract base class for BSW module entities.
    A BSW module entity represents an executable piece of code in a BSW module.
    """

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the BSW module entity with a parent and short name.
        Raises TypeError if this abstract class is instantiated directly.

        Args:
            parent: The parent ARObject that contains this entity
            short_name: The unique short name of this entity
        """
        if type(self) is BswModuleEntity:
            raise TypeError("BswModuleEntity is an abstract class.")
        super().__init__(parent, short_name)

        # List of mode group references that this entity accesses
        self.accessedModeGroupRefs: List[RefType] = []
        # List of activation point references for this entity
        self.activationPointRefs: List[RefType] = []
        # List of call points associated with this entity
        self.callPoints: List[BswModuleCallPoint] = []
        # List of variable access points for data reception
        self.dataReceivePoints: List[BswVariableAccess] = []
        # List of variable access points for data sending
        self.dataSendPoints: List[BswVariableAccess] = []
        # Reference to the entry implemented by this entity
        self.implementedEntryRef: RefType = None
        # List of trigger references issued by this entity
        self.issuedTriggerRefs: List[RefType] = []
        # List of mode group references managed by this entity
        self.managedModeGroupRefs: List[RefType] = []
        # List of scheduler name prefix references
        self.schedulerNamePrefixRef: List[RefType] = None

    def getAccessedModeGroupRefs(self):
        """
        Gets the list of mode group references that this entity accesses.

        Returns:
            List of mode group references
        """
        return self.accessedModeGroupRefs

    def addAccessedModeGroupRef(self, value):
        """
        Adds a mode group reference to the list of accessed mode groups.
        Only adds the value if it is not None.

        Args:
            value: The mode group reference to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.accessedModeGroupRefs.append(value)
        return self

    def getActivationPointRefs(self):
        """
        Gets the list of activation point references for this entity.

        Returns:
            List of activation point references
        """
        return self.activationPointRefs

    def addActivationPointRef(self, value):
        """
        Adds an activation point reference to the list of activation points.
        Only adds the value if it is not None.

        Args:
            value: The activation point reference to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.activationPointRefs.append(value)
        return self

    def getCallPoints(self):
        """
        Gets the list of call points associated with this entity.

        Returns:
            List of call points
        """
        return self.callPoints

    def createBswAsynchronousServerCallPoint(self, short_name):
        """
        Creates and adds a BswAsynchronousServerCallPoint to this entity.

        Args:
            short_name: The short name for the new call point

        Returns:
            The created BswAsynchronousServerCallPoint instance
        """
        if (not self.IsElementExists(short_name)):
            access = BswAsynchronousServerCallPoint(self, short_name)
            self.addElement(access)
            self.callPoints.append(access)
        return self.getElement(short_name)

    def createBswSynchronousServerCallPoint(self, short_name):
        """
        Creates and adds a BswSynchronousServerCallPoint to this entity.

        Args:
            short_name: The short name for the new call point

        Returns:
            The created BswSynchronousServerCallPoint instance
        """
        if (not self.IsElementExists(short_name)):
            access = BswSynchronousServerCallPoint(self, short_name)
            self.addElement(access)
            self.callPoints.append(access)
        return self.getElement(short_name)

    def getDataReceivePoints(self):
        """
        Gets the list of variable access points for data reception.

        Returns:
            List of data receive points
        """
        return self.dataReceivePoints

    def createDataReceivePoint(self, short_name: str) -> BswVariableAccess:
        """
        Creates and adds a BswVariableAccess for data reception to this entity.

        Args:
            short_name: The short name for the new data receive point

        Returns:
            The created BswVariableAccess instance
        """
        if (not self.IsElementExists(short_name)):
            access = BswVariableAccess(self, short_name)
            self.addElement(access)
            self.dataReceivePoints.append(access)
        return self.getElement(short_name, BswVariableAccess)

    def getDataSendPoints(self):
        """
        Gets the list of variable access points for data sending.

        Returns:
            List of data send points
        """
        return self.dataSendPoints

    def createDataSendPoint(self, short_name: str) -> BswVariableAccess:
        """
        Creates and adds a BswVariableAccess for data sending to this entity.

        Args:
            short_name: The short name for the new data send point

        Returns:
            The created BswVariableAccess instance
        """
        if (not self.IsElementExists(short_name)):
            access = BswVariableAccess(self, short_name)
            self.addElement(access)
            self.dataSendPoints.append(access)
        return self.getElement(short_name, BswVariableAccess)

    def getImplementedEntryRef(self):
        """
        Gets the reference to the entry implemented by this entity.

        Returns:
            Reference to the implemented entry
        """
        return self.implementedEntryRef

    def setImplementedEntryRef(self, value):
        """
        Sets the reference to the entry implemented by this entity.
        Only sets the value if it is not None.

        Args:
            value: The entry reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.implementedEntryRef = value
        return self

    def getIssuedTriggerRefs(self):
        """
        Gets the list of trigger references issued by this entity.

        Returns:
            List of issued trigger references
        """
        return self.issuedTriggerRefs

    def addIssuedTriggerRef(self, value):
        """
        Adds a trigger reference to the list of issued triggers.
        Only adds the value if it is not None.

        Args:
            value: The trigger reference to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.issuedTriggerRefs.append(value)
        return self

    def getManagedModeGroupRefs(self):
        """
        Gets the list of mode group references managed by this entity.

        Returns:
            List of managed mode group references
        """
        return self.managedModeGroupRefs

    def addManagedModeGroupRef(self, value):
        """
        Adds a mode group reference to the list of managed mode groups.
        Only adds the value if it is not None.

        Args:
            value: The mode group reference to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.managedModeGroupRefs.append(value)
        return self

    def getSchedulerNamePrefixRef(self):
        """
        Gets the list of scheduler name prefix references.

        Returns:
            List of scheduler name prefix references
        """
        return self.schedulerNamePrefixRef

    def setSchedulerNamePrefixRef(self, value):
        """
        Sets the list of scheduler name prefix references.
        Only sets the value if it is not None.

        Args:
            value: The scheduler name prefix references to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.schedulerNamePrefixRef = value
        return self


class BswCalledEntity(BswModuleEntity):
    """
    Represents a BSW module entity that can be called by other entities.
    This is typically used for BSW service functions that can be invoked.
    """

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the BswCalledEntity with a parent and short name.

        Args:
            parent: The parent ARObject that contains this entity
            short_name: The unique short name of this entity
        """
        super().__init__(parent, short_name)


class BswSchedulableEntity(BswModuleEntity):
    """
    Represents a BSW module entity that can be scheduled for execution.
    This is typically used for BSW functions that can be scheduled by the OS.
    """

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the BswSchedulableEntity with a parent and short name.

        Args:
            parent: The parent ARObject that contains this entity
            short_name: The unique short name of this entity
        """
        super().__init__(parent, short_name)


class BswInterruptCategory(AREnum):
    """
    Enumeration for BSW interrupt categories.
    Defines whether an interrupt is a Category 1 (CAT1) or Category 2 (CAT2) interrupt.
    """
    # Category 1 interrupt - directly handled by the OS
    CAT1 = "cat1"
    # Category 2 interrupt - handled by the interrupt service routine
    CAT2 = "cat2"

    def __init__(self):
        """
        Initializes the BswInterruptCategory with valid values.
        """
        super().__init__((
            BswInterruptCategory.CAT1,
            BswInterruptCategory.CAT2,
        ))


class BswInterruptEntity(BswModuleEntity):
    """
    Represents an interrupt entity in a BSW module.
    This defines how interrupt service routines are handled in the BSW module.
    """

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the BswInterruptEntity with a parent and short name.

        Args:
            parent: The parent ARObject that contains this interrupt entity
            short_name: The unique short name of this interrupt entity
        """
        super().__init__(parent, short_name)

        # Category of the interrupt (CAT1 or CAT2)
        self.interruptCategory: BswInterruptCategory = None
        # Source identifier for the interrupt
        self.interruptSource: String = None

    def getInterruptCategory(self):
        """
        Gets the interrupt category for this interrupt entity.

        Returns:
            The interrupt category (CAT1 or CAT2)
        """
        return self.interruptCategory

    def setInterruptCategory(self, value):
        """
        Sets the interrupt category for this interrupt entity.

        Args:
            value: The interrupt category to set

        Returns:
            self for method chaining
        """
        self.interruptCategory = value
        return self

    def getInterruptSource(self):
        """
        Gets the interrupt source identifier for this interrupt entity.

        Returns:
            The interrupt source identifier
        """
        return self.interruptSource

    def setInterruptSource(self, value):
        """
        Sets the interrupt source identifier for this interrupt entity.

        Args:
            value: The interrupt source identifier to set

        Returns:
            self for method chaining
        """
        self.interruptSource = value
        return self


class BswEvent(AbstractEvent, ABC):
    """
    Abstract base class for BSW events.
    BSW events trigger the execution of BSW module entities.
    """

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the BSW event with a parent and short name.
        Raises TypeError if this abstract class is instantiated directly.

        Args:
            parent: The parent ARObject that contains this event
            short_name: The unique short name of this event
        """
        if type(self) is BswEvent:
            raise TypeError("BswEvent is an abstract class.")
        super().__init__(parent, short_name)

        # Reference to the event that starts this event
        self.startsOnEventRef: RefType = None

    def getStartsOnEventRef(self):
        """
        Gets the reference to the event that starts this event.

        Returns:
            Reference to the starting event
        """
        return self.startsOnEventRef

    def setStartsOnEventRef(self, value):
        """
        Sets the reference to the event that starts this event.

        Args:
            value: The starting event reference to set

        Returns:
            self for method chaining
        """
        self.startsOnEventRef = value
        return self


class BswOperationInvokedEvent(BswEvent):
    """
    Represents an event that is triggered when a BSW operation is invoked.
    This event occurs when a client calls a BSW service function.
    """

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the BswOperationInvokedEvent with a parent and short name.

        Args:
            parent: The parent ARObject that contains this event
            short_name: The unique short name of this event
        """
        super().__init__(parent, short_name)

        # Reference to the entry that was invoked to trigger this event
        self.entryRef: RefType = None

    def getEntryRef(self):
        """
        Gets the reference to the entry that was invoked to trigger this event.

        Returns:
            Reference to the invoked entry
        """
        return self.entryRef

    def setEntryRef(self, value):
        """
        Sets the reference to the entry that was invoked to trigger this event.
        Only sets the value if it is not None.

        Args:
            value: The entry reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.entryRef = value
        return self


class BswScheduleEvent(BswEvent, ABC):
    """
    Abstract base class for BSW scheduled events.
    These events are scheduled for execution at specific times or conditions.
    """

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the BSW schedule event with a parent and short name.
        Raises TypeError if this abstract class is instantiated directly.

        Args:
            parent: The parent ARObject that contains this event
            short_name: The unique short name of this event
        """
        if type(self) is BswScheduleEvent:
            raise TypeError("BswScheduleEvent is an abstract class.")
        super().__init__(parent, short_name)


class BswModeSwitchEvent(BswScheduleEvent):
    """
    Represents an event that is triggered when a mode switch occurs.
    This event handles changes in system modes within BSW modules.
    """

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the BswModeSwitchEvent with a parent and short name.

        Args:
            parent: The parent ARObject that contains this event
            short_name: The unique short name of this event
        """
        super().__init__(parent, short_name)

        # Activation information for this mode switch event
        self.activation: ModeActivationKind = None

    def getActivation(self):
        """
        Gets the activation information for this mode switch event.

        Returns:
            Activation information
        """
        return self.activation

    def setActivation(self, value):
        """
        Sets the activation information for this mode switch event.

        Args:
            value: The activation information to set

        Returns:
            self for method chaining
        """
        self.activation = value
        return self


class BswModeSwitchedAckEvent(BswScheduleEvent):
    """
    Represents an event that is triggered when a mode switch acknowledgment occurs.
    This event handles the acknowledgment that a mode switch has been completed or confirmed
    within BSW modules.
    """

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the BswModeSwitchedAckEvent with a parent and short name.

        Args:
            parent: The parent ARObject that contains this event
            short_name: The unique short name of this event
        """
        super().__init__(parent, short_name)


class BswTimingEvent(BswScheduleEvent):
    """
    Represents a timing event in a BSW module.
    This event is triggered based on timing constraints (e.g., periodic execution).
    """

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the BswTimingEvent with a parent and short name.

        Args:
            parent: The parent ARObject that contains this event
            short_name: The unique short name of this event
        """
        super().__init__(parent, short_name)

        # Period of the timing event (how often it occurs)
        self.period: TimeValue = None

    def getPeriod(self):
        """
        Gets the period of this timing event.

        Returns:
            TimeValue representing the period
        """
        return self.period

    def setPeriod(self, value):
        """
        Sets the period of this timing event.
        Only sets the value if it's not None or if the current period is None.

        Args:
            value: The period to set

        Returns:
            self for method chaining
        """
        if not (value is None and self.period is not None):
            self.period = value
        return self

    @property
    def periodMs(self) -> int:
        """
        Gets the period of this timing event in milliseconds.

        Returns:
            Integer representing the period in milliseconds, or None if period is not set
        """
        if self.period is not None:
            return int(self.period.value * 1000)
        return None


class BswDataReceivedEvent(BswScheduleEvent):
    """
    Represents an event that is triggered when data is received by a BSW module.
    This event handles data reception from other modules or communication interfaces.
    """

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the BswDataReceivedEvent with a parent and short name.

        Args:
            parent: The parent ARObject that contains this event
            short_name: The unique short name of this event
        """
        super().__init__(parent, short_name)

        # Reference to the data that was received to trigger this event
        self.dataRef: RefType = None

    def getDataRef(self):
        """
        Gets the reference to the data that was received to trigger this event.

        Returns:
            Reference to the received data
        """
        return self.dataRef

    def setDataRef(self, value):
        """
        Sets the reference to the data that was received to trigger this event.

        Args:
            value: The data reference to set

        Returns:
            self for method chaining
        """
        self.dataRef = value
        return self


class BswInternalTriggerOccurredEvent(BswScheduleEvent):
    """
    Represents an event that is triggered by an internal trigger in a BSW module.
    This event occurs when a BSW module internally generates a trigger.
    """

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the BswInternalTriggerOccurredEvent with a parent and short name.

        Args:
            parent: The parent ARObject that contains this event
            short_name: The unique short name of this event
        """
        super().__init__(parent, short_name)

        # Reference to the event source that triggered this event
        self.eventSourceRef: RefType = None

    def getEventSourceRef(self):
        """
        Gets the reference to the event source that triggered this event.

        Returns:
            Reference to the event source
        """
        return self.eventSourceRef

    def setEventSourceRef(self, value):
        """
        Sets the reference to the event source that triggered this event.

        Args:
            value: The event source reference to set

        Returns:
            self for method chaining
        """
        self.eventSourceRef = value
        return self


class BswModeSwitchAckRequest(ARObject):
    """
    Represents an acknowledgment request for a mode switch operation.
    This is used in BSW modules to handle mode switch acknowledgments.
    """

    def __init__(self):
        """
        Initializes the BswModeSwitchAckRequest.
        """
        super().__init__()

        # Timeout value for the mode switch acknowledgment
        self.timeout: ARFloat = None

    def getTimeout(self):
        """
        Gets the timeout value for the mode switch acknowledgment.

        Returns:
            ARFloat representing the timeout value
        """
        return self.timeout

    def setTimeout(self, value):
        """
        Sets the timeout value for the mode switch acknowledgment.

        Args:
            value: The timeout value to set

        Returns:
            self for method chaining
        """
        self.timeout = value
        return self


class BswModeSenderPolicy(ARObject):
    """
    Represents the policy for a BSW mode sender.
    This defines how mode changes are sent and acknowledged in BSW modules.
    """

    def __init__(self):
        """
        Initializes the BswModeSenderPolicy.
        """
        super().__init__()

        # Acknowledgment request configuration for mode switch
        self.ack_request: BswModeSwitchAckRequest = None
        # Flag indicating if enhanced mode API is used
        self.enhanced_mode_api: ARBoolean = None
        # Reference to the provided mode group
        self._provided_mode_group_ref: RefType = None
        # Queue length for mode switch operations
        self._queue_length: ARNumerical = None

    def setProvidedModeGroupRef(self, ref: RefType):
        """
        Sets the reference to the provided mode group.

        Args:
            ref: The mode group reference to set

        Returns:
            self for method chaining
        """
        self._provided_mode_group_ref = ref
        return self

    def getProvidedModeGroupRef(self) -> RefType:
        """
        Gets the reference to the provided mode group.

        Returns:
            Reference to the provided mode group
        """
        return self._provided_mode_group_ref

    def setQueueLength(self, length: any):
        """
        Sets the queue length for mode switch operations.
        Can accept either ARNumerical or integer values.

        Args:
            length: The queue length value (ARNumerical or int)

        Returns:
            self for method chaining
        """
        if isinstance(length, ARNumerical):
            self._queue_length = length
        elif isinstance(length, int):
            self._queue_length = ARNumerical()
            self._queue_length.setValue(length)
        else:
            raise ValueError("Unsupported type <%s>" % type(length))

    def getQueueLength(self) -> ARNumerical:
        """
        Gets the queue length for mode switch operations.

        Returns:
            ARNumerical representing the queue length
        """
        return self._queue_length


class BswBackgroundEvent(BswScheduleEvent):
    """
    Represents a background event in a BSW module.
    This event runs in the background, typically with lower priority.
    """

    def __init__(self, parent, short_name):
        """
        Initializes the BswBackgroundEvent with a parent and short name.

        Args:
            parent: The parent ARObject that contains this event
            short_name: The unique short name of this event
        """
        super().__init__(parent, short_name)


class BswOsTaskExecutionEvent(BswScheduleEvent):
    """
    Represents an OS task execution event in a BSW module.
    This event is triggered when an OS task is executed.
    """

    def __init__(self, parent, short_name):
        """
        Initializes the BswOsTaskExecutionEvent with a parent and short name.

        Args:
            parent: The parent ARObject that contains this event
            short_name: The unique short name of this event
        """
        super().__init__(parent, short_name)


class BswExternalTriggerOccurredEvent(BswScheduleEvent):
    """
    Represents an event that is triggered by an external trigger in a BSW module.
    This event occurs when an external source generates a trigger.
    """

    def __init__(self, parent, short_name):
        """
        Initializes the BswExternalTriggerOccurredEvent with a parent and short name.

        Args:
            parent: The parent ARObject that contains this event
            short_name: The unique short name of this event
        """
        super().__init__(parent, short_name)

        # Reference to the external trigger that caused this event
        self.triggerRef: RefType = None

    def getTriggerRef(self):
        """
        Gets the reference to the external trigger that caused this event.

        Returns:
            Reference to the external trigger
        """
        return self.triggerRef

    def setTriggerRef(self, value):
        """
        Sets the reference to the external trigger that caused this event.
        Only sets the value if it is not None.

        Args:
            value: The trigger reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.triggerRef = value
        return self


class BswApiOptions(ARObject, ABC):
    """
    Abstract base class for BSW API options.
    Defines common options for BSW API implementations.
    """

    def __init__(self):
        """
        Initializes the BSW API options.
        Raises TypeError if this abstract class is instantiated directly.
        """
        if type(self) is BswApiOptions:
            raise TypeError("BswApiOptions is an abstract class.")

        super().__init__()

        # Flag indicating whether to enable taking addresses in the API
        self.enableTakeAddress: Boolean = None

    def getEnableTakeAddress(self):
        """
        Gets the enable take address flag.

        Returns:
            Boolean indicating whether take address is enabled
        """
        return self.enableTakeAddress

    def setEnableTakeAddress(self, value):
        """
        Sets the enable take address flag.
        Only sets the value if it is not None.

        Args:
            value: The boolean value to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.enableTakeAddress = value
        return self


class BswDataReceptionPolicy(BswApiOptions, ABC):
    """
    Abstract base class for BSW data reception policies.
    Defines how BSW modules receive data.
    """

    def __init__(self):
        """
        Initializes the BSW data reception policy.
        Raises TypeError if this abstract class is instantiated directly.
        """
        if type(self) is BswDataReceptionPolicy:
            raise TypeError("BswDataReceptionPolicy is an abstract class.")

        super().__init__()

        # Reference to the data being received
        self.receivedDataRef: RefType = None

    def getReceivedDataRef(self):
        """
        Gets the reference to the data being received.

        Returns:
            Reference to the received data
        """
        return self.receivedDataRef

    def setReceivedDataRef(self, value):
        """
        Sets the reference to the data being received.
        Only sets the value if it is not None.

        Args:
            value: The received data reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.receivedDataRef = value
        return self


class BswQueuedDataReceptionPolicy(BswDataReceptionPolicy):
    """
    Represents a queued data reception policy in a BSW module.
    This policy handles data reception using a queue mechanism.
    """

    def __init__(self):
        """
        Initializes the BswQueuedDataReceptionPolicy.
        """
        super().__init__()

        # Maximum queue length for received data
        self.queueLength: PositiveInteger = None

    def getQueueLength(self):
        """
        Gets the maximum queue length for received data.

        Returns:
            Positive integer representing the queue length
        """
        return self.queueLength

    def setQueueLength(self, value):
        """
        Sets the maximum queue length for received data.
        Only sets the value if it is not None.

        Args:
            value: The queue length value to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.queueLength = value
        return self


class BswInternalTriggeringPoint(Identifiable):
    """
    Represents an internal triggering point in a BSW module's internal behavior.
    This is used to define points from which triggers can be issued internally.
    """

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the BswInternalTriggeringPoint with a parent and short name.

        Args:
            parent: The parent ARObject that contains this triggering point
            short_name: The unique short name of this triggering point
        """
        super().__init__(parent, short_name)

        # Software implementation policy for this triggering point
        self.swImplPolicy: SwImplPolicyEnum = None

    def getSwImplPolicy(self):
        """
        Gets the software implementation policy for this triggering point.

        Returns:
            SwImplPolicyEnum value
        """
        return self.swImplPolicy

    def setSwImplPolicy(self, value):
        """
        Sets the software implementation policy for this triggering point.
        Only sets the value if it is not None.

        Args:
            value: The SwImplPolicyEnum value to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.swImplPolicy = value
        return self


class BswInternalBehavior(InternalBehavior):
    """
    Represents the internal behavior of a BSW module.
    This class contains all the entities, events, policies, and other behavioral elements
    that define how a BSW module operates internally.
    """

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the BswInternalBehavior with a parent and short name.

        Args:
            parent: The parent ARObject that contains this behavior
            short_name: The unique short name of this behavior
        """
        super().__init__(parent, short_name)

        # List of AUTOSAR typed per-instance memories
        self.arTypedPerInstanceMemories: List[VariableDataPrototype] = []
        # List of BSW per-instance memory policies
        self.bswPerInstanceMemoryPolicies = []
        # List of BSW client policies
        self.clientPolicies = []
        # List of BSW distinguished partitions
        self.distinguishedPartitions: List[BswDistinguishedPartition] = []
        # List of BSW module entities
        self.entities = []
        # List of BSW events
        self.events = []
        # List of BSW exclusive area policies
        self.exclusiveAreaPolicies = []
        # List of included data type sets
        self.includedDataTypeSets = []
        # List of included mode declaration group sets
        self.includedModeDeclarationGroupSets = []
        # List of BSW internal triggering points
        self.internalTriggeringPoints = []
        # List of BSW internal triggering point policies
        self.internalTriggeringPointPolicies = []
        # List of BSW mode receiver policies
        self.modeReceiverPolicies = []
        # List of BSW mode sender policies
        self.modeSenderPolicies = []
        # List of BSW parameter policies
        self.parameterPolicies = []
        # List of per-instance parameters
        self.perInstanceParameters = []
        # List of BSW data reception policies
        self.receptionPolicies = []
        # List of BSW released trigger policies
        self.releasedTriggerPolicies = []
        # List of BSW scheduler name prefixes
        self.schedulerNamePrefixes = []
        # List of BSW data send policies
        self.sendPolicies = []
        # List of BSW service dependencies
        self.serviceDependencies = []
        # List of BSW trigger direct implementations
        self.triggerDirectImplementations = []
        # List of variation point proxies
        self.variationPointProxies = []

    def getArTypedPerInstanceMemories(self):
        """
        Gets the list of AUTOSAR typed per-instance memories.

        Returns:
            List of VariableDataPrototype instances
        """
        return self.arTypedPerInstanceMemories

    def setArTypedPerInstanceMemories(self, value):
        """
        Sets the list of AUTOSAR typed per-instance memories.
        Only sets the value if it is not None.

        Args:
            value: The list of VariableDataPrototype instances to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.arTypedPerInstanceMemories = value
        return self

    def getBswPerInstanceMemoryPolicies(self):
        """
        Gets the list of BSW per-instance memory policies.

        Returns:
            List of BswPerInstanceMemoryPolicy instances
        """
        return self.bswPerInstanceMemoryPolicies

    def setBswPerInstanceMemoryPolicies(self, value):
        """
        Sets the list of BSW per-instance memory policies.
        Only sets the value if it is not None.

        Args:
            value: The list of BswPerInstanceMemoryPolicy instances to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.bswPerInstanceMemoryPolicies = value
        return self

    def getClientPolicies(self):
        """
        Gets the list of BSW client policies.

        Returns:
            List of BswClientPolicy instances
        """
        return self.clientPolicies

    def setClientPolicies(self, value):
        """
        Sets the list of BSW client policies.
        Only sets the value if it is not None.

        Args:
            value: The list of BswClientPolicy instances to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.clientPolicies = value
        return self

    def getDistinguishedPartitions(self):
        """
        Gets the list of BSW distinguished partitions.

        Returns:
            List of BswDistinguishedPartition instances
        """
        return self.distinguishedPartitions

    def setDistinguishedPartitions(self, value):
        """
        Sets the list of BSW distinguished partitions.
        Only sets the value if it is not None.

        Args:
            value: The list of BswDistinguishedPartition instances to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.distinguishedPartitions = value
        return self

    def getExclusiveAreaPolicies(self):
        """
        Gets the list of BSW exclusive area policies.

        Returns:
            List of BswExclusiveAreaPolicy instances
        """
        return self.exclusiveAreaPolicies

    def setExclusiveAreaPolicies(self, value):
        """
        Sets the list of BSW exclusive area policies.
        Only sets the value if it is not None.

        Args:
            value: The list of BswExclusiveAreaPolicy instances to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.exclusiveAreaPolicies = value
        return self

    def getInternalTriggeringPoints(self):
        """
        Gets the list of BSW internal triggering points.

        Returns:
            List of BswInternalTriggeringPoint instances
        """
        return self.internalTriggeringPoints

    def createBswInternalTriggeringPoint(self, short_name: str) -> BswInternalTriggeringPoint:
        """
        Creates and adds a BswInternalTriggeringPoint to this internal behavior.

        Args:
            short_name: The short name for the new triggering point

        Returns:
            The created BswInternalTriggeringPoint instance
        """
        if not self.IsElementExists(short_name):
            entity = BswInternalTriggeringPoint(self, short_name)
            self.addElement(entity)
            self.internalTriggeringPoints.append(entity)
        return self.getElement(short_name)

    def getInternalTriggeringPointPolicies(self):
        """
        Gets the list of BSW internal triggering point policies.

        Returns:
            List of BswInternalTriggeringPointPolicy instances
        """
        return self.internalTriggeringPointPolicies

    def setInternalTriggeringPointPolicies(self, value):
        """
        Sets the list of BSW internal triggering point policies.
        Only sets the value if it is not None.

        Args:
            value: The list of BswInternalTriggeringPointPolicy instances to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.internalTriggeringPointPolicies = value
        return self

    def getModeReceiverPolicies(self):
        """
        Gets the list of BSW mode receiver policies.

        Returns:
            List of BswModeReceiverPolicy instances
        """
        return self.modeReceiverPolicies

    def setModeSenderPolicies(self, value):
        """
        Sets the list of BSW mode sender policies.
        Only sets the value if it is not None.

        Args:
            value: The list of BswModeSenderPolicy instances to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.modeSenderPolicies = value
        return self

    def getParameterPolicies(self):
        """
        Gets the list of BSW parameter policies.

        Returns:
            List of BswParameterPolicy instances
        """
        return self.parameterPolicies

    def setParameterPolicies(self, value):
        """
        Sets the list of BSW parameter policies.
        Only sets the value if it is not None.

        Args:
            value: The list of BswParameterPolicy instances to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.parameterPolicies = value
        return self

    def getPerInstanceParameters(self):
        """
        Gets the list of per-instance parameters.

        Returns:
            List of ParameterDataPrototype instances
        """
        return self.perInstanceParameters

    def setPerInstanceParameters(self, value):
        """
        Sets the list of per-instance parameters.
        Only sets the value if it is not None.

        Args:
            value: The list of ParameterDataPrototype instances to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.perInstanceParameters = value
        return self

    def getReceptionPolicies(self):
        """
        Gets the list of BSW data reception policies.

        Returns:
            List of BswDataReceptionPolicy instances
        """
        return self.receptionPolicies

    def addReceptionPolicy(self, value):
        """
        Adds a BSW data reception policy to the list.
        Only adds the value if it is not None.

        Args:
            value: The BswDataReceptionPolicy instance to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.receptionPolicies.append(value)
        return self

    def getReleasedTriggerPolicies(self):
        """
        Gets the list of BSW released trigger policies.

        Returns:
            List of BswReleasedTriggerPolicy instances
        """
        return self.releasedTriggerPolicies

    def setReleasedTriggerPolicies(self, value):
        """
        Sets the list of BSW released trigger policies.
        Only sets the value if it is not None.

        Args:
            value: The list of BswReleasedTriggerPolicy instances to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.releasedTriggerPolicies = value
        return self

    def getSchedulerNamePrefixes(self):
        """
        Gets the list of BSW scheduler name prefixes.

        Returns:
            List of BswSchedulerNamePrefix instances
        """
        return self.schedulerNamePrefixes

    def setSchedulerNamePrefixes(self, value):
        """
        Sets the list of BSW scheduler name prefixes.
        Only sets the value if it is not None.

        Args:
            value: The list of BswSchedulerNamePrefix instances to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.schedulerNamePrefixes = value
        return self

    def getSendPolicies(self):
        """
        Gets the list of BSW data send policies.

        Returns:
            List of BswDataSendPolicy instances
        """
        return self.sendPolicies

    def setSendPolicies(self, value):
        """
        Sets the list of BSW data send policies.
        Only sets the value if it is not None.

        Args:
            value: The list of BswDataSendPolicy instances to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.sendPolicies = value
        return self

    def getServiceDependencies(self):
        """
        Gets the list of BSW service dependencies.

        Returns:
            List of BswServiceDependency instances
        """
        return self.serviceDependencies

    def setServiceDependencies(self, value):
        """
        Sets the list of BSW service dependencies.
        Only sets the value if it is not None.

        Args:
            value: The list of BswServiceDependency instances to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.serviceDependencies = value
        return self

    def getTriggerDirectImplementations(self):
        """
        Gets the list of BSW trigger direct implementations.

        Returns:
            List of BswTriggerDirectImplementation instances
        """
        return self.triggerDirectImplementations

    def setTriggerDirectImplementations(self, value):
        """
        Sets the list of BSW trigger direct implementations.
        Only sets the value if it is not None.

        Args:
            value: The list of BswTriggerDirectImplementation instances to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.triggerDirectImplementations = value
        return self

    def getVariationPointProxies(self):
        """
        Gets the list of variation point proxies.

        Returns:
            List of VariationPointProxy instances
        """
        return self.variationPointProxies

    def setVariationPointProxies(self, value):
        """
        Sets the list of variation point proxies.
        Only sets the value if it is not None.

        Args:
            value: The list of VariationPointProxy instances to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.variationPointProxies = value
        return self

    def addModeSenderPolicy(self, policy: BswModeSenderPolicy):
        """
        Adds a BSW mode sender policy to the list.
        Note: This method adds to modeReceiverPolicies instead of modeSenderPolicies,
        which might be an error in the original implementation.

        Args:
            policy: The BswModeSenderPolicy instance to add
        """
        self.modeReceiverPolicies.append(policy)

    def getModeSenderPolicies(self) -> List[BswModeSenderPolicy]:
        """
        Gets the list of BSW mode sender policies.
        Note: This method returns modeReceiverPolicies instead of modeSenderPolicies,
        which might be an error in the original implementation.

        Returns:
            List of BswModeSenderPolicy instances
        """
        return self.modeReceiverPolicies

    def createBswCalledEntity(self, short_name: str) -> BswCalledEntity:
        """
        Creates and adds a BswCalledEntity to this internal behavior.

        Args:
            short_name: The short name for the new called entity

        Returns:
            The created BswCalledEntity instance
        """
        if not self.IsElementExists(short_name):
            entity = BswCalledEntity(self, short_name)
            self.addElement(entity)
            self.entities.append(entity)
        return self.getElement(short_name)

    def getBswCalledEntities(self) -> List[BswCalledEntity]:
        """
        Gets all BswCalledEntity instances from the elements list.

        Returns:
            List of BswCalledEntity instances
        """
        return list(filter(lambda a: isinstance(a, BswCalledEntity), self.elements))

    def createBswSchedulableEntity(self, short_name: str) -> BswSchedulableEntity:
        """
        Creates and adds a BswSchedulableEntity to this internal behavior.

        Args:
            short_name: The short name for the new schedulable entity

        Returns:
            The created BswSchedulableEntity instance
        """
        if not self.IsElementExists(short_name):
            entity = BswSchedulableEntity(self, short_name)
            self.addElement(entity)
            self.entities.append(entity)
        return self.getElement(short_name)

    def getBswSchedulableEntities(self) -> List[BswSchedulableEntity]:
        """
        Gets all BswSchedulableEntity instances from the elements list.

        Returns:
            List of BswSchedulableEntity instances
        """
        return list(filter(lambda a: isinstance(a, BswSchedulableEntity), self.elements))

    def createBswInterruptEntity(self, short_name: str) -> BswInterruptEntity:
        """
        Creates and adds a BswInterruptEntity to this internal behavior.

        Args:
            short_name: The short name for the new interrupt entity

        Returns:
            The created BswInterruptEntity instance
        """
        if not self.IsElementExists(short_name):
            entity = BswInterruptEntity(self, short_name)
            self.addElement(entity)
            self.entities.append(entity)
        return self.getElement(short_name)

    def getBswInterruptEntities(self) -> List[BswInterruptEntity]:
        """
        Gets all BswInterruptEntity instances from the elements list.

        Returns:
            List of BswInterruptEntity instances
        """
        return list(filter(lambda a: isinstance(a, BswInterruptEntity), self.elements))

    def getBswModuleEntities(self) -> List[BswModuleEntity]:
        """
        Gets all BswModuleEntity instances from the elements list.

        Returns:
            List of BswModuleEntity instances
        """
        return list(filter(lambda a: isinstance(a, BswModuleEntity), self.elements))

    def createBswModeSwitchEvent(self, short_name: str) -> BswModeSwitchEvent:
        """
        Creates and adds a BswModeSwitchEvent to this internal behavior.

        Args:
            short_name: The short name for the new mode switch event

        Returns:
            The created BswModeSwitchEvent instance
        """
        if not self.IsElementExists(short_name):
            event = BswModeSwitchEvent(self, short_name)
            self.addElement(event)
            self.events.append(event)
        return self.getElement(short_name)

    def getBswModeSwitchEvents(self) -> List[BswModeSwitchEvent]:
        """
        Gets all BswModeSwitchEvent instances from the elements list.

        Returns:
            List of BswModeSwitchEvent instances
        """
        return list(filter(lambda a: isinstance(a, BswModeSwitchEvent), self.elements))

    def createBswTimingEvent(self, short_name: str) -> BswTimingEvent:
        """
        Creates and adds a BswTimingEvent to this internal behavior.

        Args:
            short_name: The short name for the new timing event

        Returns:
            The created BswTimingEvent instance
        """
        if not self.IsElementExists(short_name):
            event = BswTimingEvent(self, short_name)
            self.addElement(event)
            self.events.append(event)
        return self.getElement(short_name)

    def getBswTimingEvents(self) -> List[BswTimingEvent]:
        """
        Gets all BswTimingEvent instances from the elements list.

        Returns:
            List of BswTimingEvent instances
        """
        return list(filter(lambda a: isinstance(a, BswTimingEvent), self.elements))

    def createBswDataReceivedEvent(self, short_name: str) -> BswDataReceivedEvent:
        """
        Creates and adds a BswDataReceivedEvent to this internal behavior.

        Args:
            short_name: The short name for the new data received event

        Returns:
            The created BswDataReceivedEvent instance
        """
        if not self.IsElementExists(short_name):
            event = BswDataReceivedEvent(self, short_name)
            self.addElement(event)
            self.events.append(event)
        return self.getElement(short_name)

    def getBswDataReceivedEvents(self) -> List[BswDataReceivedEvent]:
        """
        Gets all BswDataReceivedEvent instances from the elements list.

        Returns:
            List of BswDataReceivedEvent instances
        """
        return list(filter(lambda a: isinstance(a, BswDataReceivedEvent), self.elements))

    def createBswInternalTriggerOccurredEvent(self, short_name: str) -> BswInternalTriggerOccurredEvent:
        """
        Creates and adds a BswInternalTriggerOccurredEvent to this internal behavior.

        Args:
            short_name: The short name for the new internal trigger event

        Returns:
            The created BswInternalTriggerOccurredEvent instance
        """
        if not self.IsElementExists(short_name):
            event = BswInternalTriggerOccurredEvent(self, short_name)
            self.addElement(event)
            self.events.append(event)
        return self.getElement(short_name)

    def getBswInternalTriggerOccurredEvents(self) -> List[BswInternalTriggerOccurredEvent]:
        """
        Gets all BswInternalTriggerOccurredEvent instances from the elements list.

        Returns:
            List of BswInternalTriggerOccurredEvent instances
        """
        return list(filter(lambda a: isinstance(a, BswInternalTriggerOccurredEvent), self.elements))

    def createBswExternalTriggerOccurredEvent(self, short_name: str) -> BswExternalTriggerOccurredEvent:
        """
        Creates and adds a BswExternalTriggerOccurredEvent to this internal behavior.

        Args:
            short_name: The short name for the new external trigger event

        Returns:
            The created BswExternalTriggerOccurredEvent instance
        """
        if not self.IsElementExists(short_name):
            event = BswExternalTriggerOccurredEvent(self, short_name)
            self.addElement(event)
            self.events.append(event)
        return self.getElement(short_name)

    def getBswOperationInvokedEvents(self) -> List[BswOperationInvokedEvent]:
        """
        Gets all BswOperationInvokedEvent instances from the elements list.

        Returns:
            List of BswOperationInvokedEvent instances
        """
        return list(filter(lambda a: isinstance(a, BswOperationInvokedEvent), self.elements))

    def createBswOperationInvokedEvent(self, short_name: str) -> BswOperationInvokedEvent:
        """
        Creates and adds a BswOperationInvokedEvent to this internal behavior.

        Args:
            short_name: The short name for the new operation invoked event

        Returns:
            The created BswOperationInvokedEvent instance
        """
        if not self.IsElementExists(short_name):
            event = BswOperationInvokedEvent(self, short_name)
            self.addElement(event)
            self.events.append(event)
        return self.getElement(short_name)

    def getBswExternalTriggerOccurredEvents(self) -> List[BswExternalTriggerOccurredEvent]:
        """
        Gets all BswExternalTriggerOccurredEvent instances from the elements list.

        Returns:
            List of BswExternalTriggerOccurredEvent instances
        """
        return list(filter(lambda a: isinstance(a, BswExternalTriggerOccurredEvent), self.elements))

    def createBswBackgroundEvent(self, short_name: str) -> BswBackgroundEvent:
        """
        Creates and adds a BswBackgroundEvent to this internal behavior.

        Args:
            short_name: The short name for the new background event

        Returns:
            The created BswBackgroundEvent instance
        """
        if not self.IsElementExists(short_name):
            event = BswBackgroundEvent(self, short_name)
            self.addElement(event)
            self.events.append(event)
        return self.getElement(short_name)

    def getBswBackgroundEvents(self) -> List[BswBackgroundEvent]:
        """
        Gets all BswBackgroundEvent instances from the elements list.

        Returns:
            List of BswBackgroundEvent instances
        """
        return list(filter(lambda a: isinstance(a, BswBackgroundEvent), self.elements))

    def getBswEvents(self) -> List[BswEvent]:
        """
        Gets all BswEvent instances from the elements list.

        Returns:
            List of BswEvent instances
        """
        return list(filter(lambda a: isinstance(a, BswEvent), self.elements))

    def addIncludedModeDeclarationGroupSet(self, group_set: IncludedModeDeclarationGroupSet):
        """
        Adds an included mode declaration group set to the list.

        Args:
            group_set: The IncludedModeDeclarationGroupSet instance to add
        """
        self.includedModeDeclarationGroupSets.append(group_set)

    def getIncludedModeDeclarationGroupSets(self) -> List[IncludedModeDeclarationGroupSet]:
        """
        Gets the list of included mode declaration group sets.

        Returns:
            List of IncludedModeDeclarationGroupSet instances
        """
        return self.includedModeDeclarationGroupSets

    def addIncludedDataTypeSet(self, type_set: IncludedDataTypeSet):
        """
        Adds an included data type set to the list.

        Args:
            type_set: The IncludedDataTypeSet instance to add
        """
        self.includedDataTypeSets.append(type_set)

    def getIncludedDataTypeSets(self) -> List[IncludedDataTypeSet]:
        """
        Gets the list of included data type sets.

        Returns:
            List of IncludedDataTypeSet instances
        """
        return self.includedDataTypeSets



# ========== Classes from subdirectory files ==========

"""
This module defines BSW asynchronous server call returns event in AUTOSAR.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class BswAsynchronousServerCallReturnsEvent(BswEvent):
    """
    Represents a BSW asynchronous server call returns event in AUTOSAR.
    This event occurs when an asynchronous server call returns.
    """

    def __init__(self):
        """
        Initializes the BswAsynchronousServerCallReturnsEvent with default values.
        """
        super().__init__()
        self.serverCallPointRef: RefType = None

    def getServerCallPointRef(self):
        return self.serverCallPointRef

    def setServerCallPointRef(self, value):
        self.serverCallPointRef = value
        return self

"""
This module defines BSW exclusive area policy in AUTOSAR.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)


class BswExclusiveAreaPolicy(AREnum):
    """
    Enumeration for BSW exclusive area policy.
    """

    NONE = "none"
    INTERNAL = "internal"
    EXTERNAL = "external"

    def __init__(self):
        super().__init__((
            BswExclusiveAreaPolicy.NONE,
            BswExclusiveAreaPolicy.INTERNAL,
            BswExclusiveAreaPolicy.EXTERNAL,
        ))

"""
This module defines BSW interrupt event in AUTOSAR.
"""


class BswInterruptEvent(BswEvent):
    """
    Represents a BSW interrupt event in AUTOSAR.
    This event occurs when an interrupt is triggered.
    """

    def __init__(self):
        """
        Initializes the BswInterruptEvent with default values.
        """
        super().__init__()

"""
This module defines BSW mode manager error event in AUTOSAR.
"""


class BswModeManagerErrorEvent(BswEvent):
    """
    Represents a BSW mode manager error event in AUTOSAR.
    This event occurs when a mode manager error is detected.
    """

    def __init__(self):
        """
        Initializes the BswModeManagerErrorEvent with default values.
        """
        super().__init__()

"""
This module defines BSW mode receiver policy in AUTOSAR.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)


class BswModeReceiverPolicy(AREnum):
    """
    Enumeration for BSW mode receiver policy.
    """

    NONE = "none"
    IMMEDIATE = "immediate"
    DEFERRED = "deferred"

    def __init__(self):
        super().__init__((
            BswModeReceiverPolicy.NONE,
            BswModeReceiverPolicy.IMMEDIATE,
            BswModeReceiverPolicy.DEFERRED,
        ))

"""
This module defines BSW scheduler name prefix in AUTOSAR.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class BswSchedulerNamePrefix(ARObject):
    """
    Represents a BSW scheduler name prefix in AUTOSAR.
    This class defines the prefix used for scheduler names.
    """

    def __init__(self):
        """
        Initializes the BswSchedulerNamePrefix with default values.
        """
        super().__init__()
        self.prefix: str = None

    def getPrefix(self):
        return self.prefix

    def setPrefix(self, value):
        self.prefix = value
        return self

"""
This module defines BSW service dependency in AUTOSAR.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class BswServiceDependency(ARObject):
    """
    Represents a BSW service dependency in AUTOSAR.
    This class defines dependencies between BSW services.
    """

    def __init__(self):
        """
        Initializes the BswServiceDependency with default values.
        """
        super().__init__()
        self.requiredServiceRef: RefType = None

    def getRequiredServiceRef(self):
        return self.requiredServiceRef

    def setRequiredServiceRef(self, value):
        self.requiredServiceRef = value
        return self

"""
This module defines BSW trigger direct implementation in AUTOSAR.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)


class BswTriggerDirectImplementation(AREnum):
    """
    Enumeration for BSW trigger direct implementation.
    """

    NOT_ALLOWED = "not-allowed"
    ALLOWED = "allowed"

    def __init__(self):
        super().__init__((
            BswTriggerDirectImplementation.NOT_ALLOWED,
            BswTriggerDirectImplementation.ALLOWED,
        ))

"""
This module defines role-based BSW module entry assignment in AUTOSAR.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
    RefType,
)


class RoleBasedBswModuleEntryAssignment(ARObject):
    """
    Represents a role-based BSW module entry assignment in AUTOSAR.
    This class defines how BSW module entries are assigned based on their role.
    """

    def __init__(self):
        """
        Initializes the RoleBasedBswModuleEntryAssignment with default values.
        """
        super().__init__()
        self.role: ARLiteral = None
        self.usedModuleEntryRef: RefType = None

    def getRole(self):
        return self.role

    def setRole(self, value):
        self.role = value
        return self

    def getUsedModuleEntryRef(self):
        return self.usedModuleEntryRef

    def setUsedModuleEntryRef(self, value):
        self.usedModuleEntryRef = value
        return self

