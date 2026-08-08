"""
This module contains classes for representing AUTOSAR internal behavior structures
in the CommonStructure module. Internal behavior classes define executable entities,
exclusive areas, and event handling mechanisms within AUTOSAR components and BSW modules.
"""

from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable, Referrable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import ParameterDataPrototype, VariableDataPrototype


class ReentrancyLevelEnum(AREnum):
    """
    Specifies if and in which kinds of environments an entity is reentrant.
    """

    # ReentrancyLevelEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 5.5, p.73
    # [x] __init__                     [x] impl  [x] docstring  [x] test

    # Unlimited concurrent execution of this entity is possible, including
    # preemption and parallel execution on multi core systems.
    # Tags: atp.EnumerationLiteralIndex=0
    MULTICORE_REENTRANT = "multicoreReentrant"

    # Concurrent execution of this entity is not possible.
    # Tags: atp.EnumerationLiteralIndex=1
    NON_REENTRANT = "nonReentrant"

    # Pseudo-concurrent execution (i.e. preemption) of this entity is possible
    # on single core systems. Tags: atp.EnumerationLiteralIndex=2
    SINGLE_CORE_REENTRANT = "singleCoreReentrant"

    def __init__(self):
        """
        Initializes the ReentrancyLevelEnum with valid values.
        """
        super().__init__(
            (
                ReentrancyLevelEnum.MULTICORE_REENTRANT,
                ReentrancyLevelEnum.NON_REENTRANT,
                ReentrancyLevelEnum.SINGLE_CORE_REENTRANT,
            )
        )


class ExclusiveArea(Identifiable):
    """
    Represents an exclusive area in AUTOSAR models.
    Exclusive areas define critical sections that must not be executed concurrently,
    typically used for protecting shared resources in multithreaded environments.
    """

    # ExclusiveArea method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the ExclusiveArea with a parent and short name.

        Args:
            parent: The parent ARObject that contains this exclusive area
            short_name: The unique short name of this exclusive area
        """
        super().__init__(parent, short_name)


class ExecutableEntity(Identifiable, ABC):
    """
    Abstraction of executable code.
    Executable entities represent pieces of executable code that can be
    triggered by events and may have specific execution requirements like
    exclusive areas or reentrancy levels.
    """

    # ExecutableEntity method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 5.3, p.70
    # [x] __init__                         [x] impl  [x] docstring  [x] test
    # [x] getActivationReasons             [x] impl  [x] docstring  [x] test
    # [x] addActivationReason              [x] impl  [x] docstring  [x] test
    # [x] getCanEnterRefs                 [x] impl  [x] docstring  [x] test
    # [x] addCanEnterRef                  [x] impl  [x] docstring  [x] test
    # [x] getExclusiveAreaNestingOrderRefs [x] impl  [x] docstring  [x] test
    # [x] addExclusiveAreaNestingOrderRef  [x] impl  [x] docstring  [x] test
    # [x] getMinimumStartInterval          [x] impl  [x] docstring  [x] test
    # [x] setMinimumStartInterval          [x] impl  [x] docstring  [x] test
    # [x] minimumStartIntervalMs           [x] impl  [x] docstring  [x] test
    # [x] getReentrancyLevel               [x] impl  [x] docstring  [x] test
    # [x] setReentrancyLevel               [x] impl  [x] docstring  [x] test
    # [x] getRunsInsideRefs                [x] impl  [x] docstring  [x] test
    # [x] addRunsInsideRef                 [x] impl  [x] docstring  [x] test
    # [x] getSwAddrMethodRef               [x] impl  [x] docstring  [x] test
    # [x] setSwAddrMethodRef               [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the ExecutableEntity with a parent and short name.
        Raises TypeError if this abstract class is instantiated directly.

        Args:
            parent: The parent ARObject that contains this executable entity
            short_name: The unique short name of this executable entity
        """
        if type(self) is ExecutableEntity:
            raise TypeError("ExecutableEntity is an abstract class.")

        super().__init__(parent, short_name)

        # If at least one activation reason is provided the RTE resp. BSW
        # Scheduler provides means to read the activation vector of this
        # executable entity execution.
        self.activationReasons: List["ExecutableEntityActivationReason"] = []

        # The executable entity can enter/leave the referenced exclusive area
        # through explicit API calls.
        self.canEnterRefs: List[RefType] = []

        # The set of ExclusiveAreaNestingOrders recognized by this
        # ExecutableEntity.
        self.exclusiveAreaNestingOrderRefs: List[RefType] = []

        # Specifies the time in seconds by which two consecutive starts of an
        # ExecutableEntity are guaranteed to be separated.
        self.minimumStartInterval: Optional[TimeValue] = None

        # The reentrancy level of this ExecutableEntity.
        self.reentrancyLevel: Optional[ReentrancyLevelEnum] = None

        # The executable entity runs completely inside the referenced exclusive
        # area.
        self.runsInsideRefs: List[RefType] = []

        # Addressing method related to this code entity; several code entities
        # sharing the same SwAddrMethod shall be located in the same memory
        # without specifying the memory section itself.
        self.swAddrMethodRef: Optional[RefType] = None

    def getActivationReasons(self) -> List["ExecutableEntityActivationReason"]:
        """
        Gets the activation reasons of this executable entity; if at least one
        activation reason is provided the RTE resp. BSW Scheduler provides
        means to read the activation vector of this entity execution.

        Returns:
            List of ExecutableEntityActivationReason instances
        """
        return self.activationReasons

    def addActivationReason(self, value: "ExecutableEntityActivationReason") -> "ExecutableEntity":
        """
        Adds an activation reason to this executable entity.

        Args:
            value: The activation reason to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.activationReasons.append(value)
        return self

    def getCanEnterRefs(self) -> List[RefType]:
        """
        Gets the references to exclusive areas that this executable entity can
        enter/leave through explicit API calls.

        Returns:
            List of RefType instances
        """
        return self.canEnterRefs

    def addCanEnterRef(self, value: RefType) -> "ExecutableEntity":
        """
        Adds a reference to an exclusive area that this executable entity can
        enter/leave through explicit API calls.

        Args:
            value: The exclusive area reference to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.canEnterRefs.append(value)
        return self

    def getExclusiveAreaNestingOrderRefs(self) -> List[RefType]:
        """
        Gets the set of ExclusiveAreaNestingOrders recognized by this
        executable entity.

        Returns:
            List of RefType instances
        """
        return self.exclusiveAreaNestingOrderRefs

    def addExclusiveAreaNestingOrderRef(self, value: RefType) -> "ExecutableEntity":
        """
        Adds a reference to an ExclusiveAreaNestingOrder recognized by this
        executable entity.

        Args:
            value: The ExclusiveAreaNestingOrder reference to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.exclusiveAreaNestingOrderRefs.append(value)
        return self

    def getMinimumStartInterval(self) -> Optional[TimeValue]:
        """
        Gets the time in seconds by which two consecutive starts of an
        executable entity are guaranteed to be separated.

        Returns:
            TimeValue: The minimum start interval
        """
        return self.minimumStartInterval

    def setMinimumStartInterval(self, value: Optional[TimeValue]) -> "ExecutableEntity":
        """
        Sets the time in seconds by which two consecutive starts of an
        executable entity are guaranteed to be separated.
        Only sets the value if it is not None.

        Args:
            value: The minimum start interval to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.minimumStartInterval = value
        return self

    @property
    def minimumStartIntervalMs(self) -> Optional[int]:
        """
        Gets the minimum start interval in milliseconds (from seconds).

        Returns:
            int: The minimum start interval in milliseconds, or None if not set
        """
        if self.minimumStartInterval is not None:
            return int(self.minimumStartInterval.getValue() * 1000)
        return None

    def getReentrancyLevel(self) -> Optional[ReentrancyLevelEnum]:
        """
        Gets the reentrancy level of this executable entity.

        Returns:
            ReentrancyLevelEnum: The reentrancy level
        """
        return self.reentrancyLevel

    def setReentrancyLevel(self, value: Optional[ReentrancyLevelEnum]) -> "ExecutableEntity":
        """
        Sets the reentrancy level of this executable entity.
        Only sets the value if it is not None.

        Args:
            value: The reentrancy level to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.reentrancyLevel = value
        return self

    def getRunsInsideRefs(self) -> List[RefType]:
        """
        Gets the references to exclusive areas that this executable entity runs
        completely inside.

        Returns:
            List of RefType instances
        """
        return self.runsInsideRefs

    def addRunsInsideRef(self, value: RefType) -> "ExecutableEntity":
        """
        Adds a reference to an exclusive area that this executable entity runs
        completely inside.

        Args:
            value: The exclusive area reference to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.runsInsideRefs.append(value)
        return self

    def getSwAddrMethodRef(self) -> Optional[RefType]:
        """
        Gets the addressing method related to this code entity; several code
        entities sharing the same SwAddrMethod shall be located in the same
        memory without specifying the memory section itself.

        Returns:
            RefType: The software address method reference
        """
        return self.swAddrMethodRef

    def setSwAddrMethodRef(self, value: Optional[RefType]) -> "ExecutableEntity":
        """
        Sets the addressing method related to this code entity.
        Only sets the value if it is not None.

        Args:
            value: The software address method reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.swAddrMethodRef = value
        return self


class InternalBehavior(AtpStructureElement, ABC):
    """
    Abstract base class for internal behavior in AUTOSAR models.
    Internal behavior defines the internal structure of software components or BSW modules,
    including executable entities, memory areas, and data type mappings.
    """

    # InternalBehavior method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test
    # [x] createConstantMemory         [x] impl  [x] docstring  [x] test
    # [x] getConstantMemories          [x] impl  [x] docstring  [x] test
    # [x] addDataTypeMappingRef        [x] impl  [x] docstring  [x] test
    # [x] getDataTypeMappingRefs       [x] impl  [x] docstring  [x] test
    # [x] createExclusiveArea          [x] impl  [x] docstring  [x] test
    # [x] getExclusiveAreas            [x] impl  [x] docstring  [x] test
    # [x] getStaticMemories            [x] impl  [x] docstring  [x] test
    # [x] createStaticMemory           [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the InternalBehavior with a parent and short name.
        Raises TypeError if this abstract class is instantiated directly.

        Args:
            parent: The parent ARObject that contains this internal behavior
            short_name: The unique short name of this internal behavior
        """
        if type(self) is InternalBehavior:
            raise TypeError("InternalBehavior is an abstract class.")
        super().__init__(parent, short_name)

        # List of constant memories (parameter data prototypes) in this internal behavior
        self.constantMemories: List[ParameterDataPrototype] = []
        # List of constant value mapping references for this internal behavior
        self.constantValueMappingRefs: List[RefType] = []
        # List of data type mapping references for this internal behavior
        self.dataTypeMappingRefs: List[RefType] = []
        # List of exclusive areas defined in this internal behavior
        self.exclusiveAreas: List["ExclusiveArea"] = []
        # List of exclusive area nesting orders for this internal behavior
        self.exclusiveAreaNestingOrders: List = []
        # List of static memories (variable data prototypes) in this internal behavior
        self.staticMemories: List[VariableDataPrototype] = []

    def createConstantMemory(self, short_name: str) -> ParameterDataPrototype:
        """
        Creates and adds a ParameterDataPrototype to this internal behavior's constant memories.

        Args:
            short_name: The short name for the new parameter data prototype

        Returns:
            The created ParameterDataPrototype instance
        """
        if short_name not in self.elements:
            prototype = ParameterDataPrototype(self, short_name)
            self.addElement(prototype)
            self.constantMemories.append(prototype)
        return self.getElement(short_name)

    def getConstantMemories(self) -> List[ParameterDataPrototype]:
        """
        Gets the list of constant memories (parameter data prototypes) in this internal behavior.

        Returns:
            List of ParameterDataPrototype instances
        """
        return self.constantMemories

    def addDataTypeMappingRef(self, ref: RefType):
        """
        Adds a data type mapping reference to this internal behavior.

        Args:
            ref: The data type mapping reference to add
        """
        self.dataTypeMappingRefs.append(ref)

    def getDataTypeMappingRefs(self) -> List[RefType]:
        """
        Gets the list of data type mapping references for this internal behavior.

        Returns:
            List of RefType instances
        """
        return self.dataTypeMappingRefs

    def createExclusiveArea(self, short_name: str) -> ExclusiveArea:
        """
        Creates and adds an ExclusiveArea to this internal behavior's exclusive areas.

        Args:
            short_name: The short name for the new exclusive area

        Returns:
            The created ExclusiveArea instance
        """
        if short_name not in self.elements:
            area = ExclusiveArea(self, short_name)
            self.addElement(area)
            self.exclusiveAreas.append(area)
        return self.getElement(short_name)

    def getExclusiveAreas(self) -> List[ExclusiveArea]:
        """
        Gets the list of exclusive areas defined in this internal behavior.

        Returns:
            List of ExclusiveArea instances
        """
        return list(filter(lambda c: isinstance(c, ExclusiveArea), self.elements))

    def getStaticMemories(self):
        """
        Gets the list of static memories (variable data prototypes) in this internal behavior.

        Returns:
            List of VariableDataPrototype instances
        """
        return self.staticMemories

    def createStaticMemory(self, short_name: str) -> VariableDataPrototype:
        """
        Creates and adds a VariableDataPrototype to this internal behavior's static memories.

        Args:
            short_name: The short name for the new variable data prototype

        Returns:
            The created VariableDataPrototype instance
        """
        if short_name not in self.elements:
            prototype = VariableDataPrototype(self, short_name)
            self.addElement(prototype)
            self.staticMemories.append(prototype)
        return self.getElement(short_name)


class AbstractEvent(Identifiable, ABC):
    """
    Represents an abstract event in AUTOSAR models.
    Abstract events define the base structure for events that can trigger executable entities.
    They may have activation reason representations that define why the event occurred.
    """

    # AbstractEvent method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test
    # [x] getActivationReasonRepresentationRef [x] impl  [x] docstring  [x] test
    # [x] setActivationReasonRepresentationRef [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the AbstractEvent with a parent and short name.
        Raises TypeError if this abstract class is instantiated directly.

        Args:
            parent: The parent ARObject that contains this abstract event
            short_name: The unique short name of this abstract event
        """
        if type(self) is AbstractEvent:
            raise TypeError("AbstractEvent is an abstract class.")
        super().__init__(parent, short_name)

        # Reference to activation reason representation for this event
        self.activationReasonRepresentationRef: RefType = None

    def getActivationReasonRepresentationRef(self):
        """
        Gets the reference to activation reason representation for this event.

        Returns:
            RefType: The activation reason representation reference
        """
        return self.activationReasonRepresentationRef

    def setActivationReasonRepresentationRef(self, value):
        """
        Sets the reference to activation reason representation for this event.
        Only sets the value if it is not None.

        Args:
            value: The activation reason representation reference to set

        Returns:
            self for method chaining
        """
        self.activationReasonRepresentationRef = value
        return self


class ApiPrincipleEnum(AREnum):
    """
    Represents the ability to control the granularity of API generation.
    """

    # ApiPrincipleEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 5.18, p.83
    # [x] __init__                     [x] impl  [x] docstring  [x] test

    # The Rte or SchM API is provided for the whole software component / BSW
    # Module. Tags: atp.EnumerationLiteralIndex=0
    COMMON = "common"

    # The Rte or SchM API is provided for a specific ExecutableEntity of a
    # software component / BSW Module. Tags: atp.EnumerationLiteralIndex=1
    PER_EXECUTABLE = "perExecutable"

    def __init__(self):
        """
        Initializes the ApiPrincipleEnum with valid values.
        """
        super().__init__(
            (
                ApiPrincipleEnum.COMMON,
                ApiPrincipleEnum.PER_EXECUTABLE,
            )
        )


class ExclusiveAreaNestingOrder(Referrable):
    """
    This meta-class represents the ability to define a nesting order of
    ExclusiveAreas. A nesting order (that may occur in the executable code) is
    formally defined to be able to analyze the resource locking behavior.
    """

    # ExclusiveAreaNestingOrder method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 5.19, p.84
    # [x] __init__                [x] impl  [x] docstring  [x] test
    # [x] getExclusiveAreaRefs    [x] impl  [x] docstring  [x] test
    # [x] addExclusiveAreaRef     [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the ExclusiveAreaNestingOrder with a parent and short name.

        Args:
            parent: The parent ARObject that contains this nesting order
            short_name: The unique short name of this nesting order
        """
        super().__init__(parent, short_name)

        # This represents a specific scenario of how Exclusive Areas can be
        # used in terms of the nesting order. Spec attribute "exclusiveArea"
        # (ref, *, ordered).
        self.exclusiveAreaRefs: List[RefType] = []

    def getExclusiveAreaRefs(self) -> List[RefType]:
        """
        Gets the ordered references to ExclusiveAreas describing a specific
        scenario of how exclusive areas can be used in terms of the nesting
        order.

        Returns:
            List of RefType instances
        """
        return self.exclusiveAreaRefs

    def addExclusiveAreaRef(self, value: RefType) -> "ExclusiveAreaNestingOrder":
        """
        Adds an ordered reference to an ExclusiveArea describing a specific
        scenario of how exclusive areas can be used in terms of the nesting
        order.

        Args:
            value: The exclusive area reference to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.exclusiveAreaRefs.append(value)
        return self


class ExecutableEntityActivationReason(ARObject):
    """
    Represents the reason for executable entity activation in AUTOSAR.
    """

    # ExecutableEntityActivationReason method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test
    # [ ] getReason                    [x] impl  [ ] docstring  [ ] test
    # [ ] setReason                    [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        """
        Initializes the ExecutableEntityActivationReason with default values.
        """
        super().__init__()
        self.reason: str = None

    def getReason(self):
        return self.reason

    def setReason(self, value):
        self.reason = value
        return self
