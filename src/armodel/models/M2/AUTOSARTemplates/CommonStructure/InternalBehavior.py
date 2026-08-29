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
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation import ImplementationProps
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, TimeValue, RefType, AREnum
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
    Prevents an executable entity running in the area from being preempted.
    """

    # ExclusiveArea method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 5.16, p.82
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class ExecutableEntity(Identifiable, ABC):
    """
    Abstraction of executable code.
    """

    # ExecutableEntity method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 5.3, p.70
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] createActivationReason           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getActivationReasons             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addActivationReason              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getCanEnterRefs                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addCanEnterRef                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getExclusiveAreaNestingOrderRefs [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addExclusiveAreaNestingOrderRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMinimumStartInterval          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMinimumStartInterval          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] minimumStartIntervalMs           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getReentrancyLevel               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setReentrancyLevel               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRunsInsideRefs                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addRunsInsideRef                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSwAddrMethodRef               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSwAddrMethodRef               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is ExecutableEntity:
            raise TypeError("ExecutableEntity is an abstract class.")

        super().__init__(parent, short_name)

        # If the ExecutableEntity provides at least one activation Reason element the RTE resp. BSW Scheduler shall provide means to read the activation vector of this executable entity execution. If no activationReason element is provided the feature of being able to determine the activating RTEEvent is disabled for this ExecutableEntity.
        self.activationReasons: List[ExecutableEntityActivationReason] = []

        # This means that the executable entity can enter/leave the referenced exclusive area through explicit API calls. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=canEnter.exclusiveArea, canEnter.variation Point.shortLabel vh.latestBindingTime=preCompileTime
        self.canEnterRefs: List[RefType] = []

        # This represents the set of ExclusiveAreaNestingOrders recognized by this ExecutableEntity.
        self.exclusiveAreaNestingOrderRefs: List[RefType] = []

        # Specifies the time in seconds by which two consecutive starts of an ExecutableEntity are guaranteed to be separated.
        self.minimumStartInterval: Optional[TimeValue] = None

        # The reentrancy level of this ExecutableEntity. See the documentation of the enumeration type ReentrancyLevel Enum for details. Please note that nonReentrant interfaces can have also reentrant or multicoreReentrant implementations, and reentrant interfaces can also have multicoreReentrant implementations.
        self.reentrancyLevel: Optional[ReentrancyLevelEnum] = None

        # The executable entity runs completely inside the referenced exclusive area. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=runsInside.exclusiveArea, runs Inside.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        self.runsInsideRefs: List[RefType] = []

        # Addressing method related to this code entity. Via an association to the same SwAddrMethod, it can be specified that several code entities (even of different modules or components) shall be located in the same memory without already specifying the memory section itself.
        self.swAddrMethodRef: Optional[RefType] = None

    def createActivationReason(self, short_name: str) -> "ExecutableEntityActivationReason":
        """
        Creates (or returns an existing) ExecutableEntityActivationReason
        aggregated by this executable entity.

        Args:
            short_name: The short name of the activation reason

        Returns:
            The created ExecutableEntityActivationReason instance
        """
        if not self.IsElementExists(short_name):
            reason = ExecutableEntityActivationReason(self, short_name)
            self.addElement(reason)
            self.activationReasons.append(reason)
        return self.getElement(short_name)

    def getActivationReasons(self) -> List["ExecutableEntityActivationReason"]:
        """
        Gets the activation reasons. If the ExecutableEntity provides at least one activation Reason element the RTE resp. BSW Scheduler shall provide means to read the activation vector of this executable entity execution. If no activationReason element is provided the feature of being able to determine the activating RTEEvent is disabled for this ExecutableEntity.

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
        Gets the references to exclusive areas. This means that the executable entity can enter/leave the referenced exclusive area through explicit API calls. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=canEnter.exclusiveArea, canEnter.variation Point.shortLabel vh.latestBindingTime=preCompileTime

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
        Gets the references to exclusive area nesting orders. This represents the set of ExclusiveAreaNestingOrders recognized by this ExecutableEntity.

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
        Gets the minimum start interval. Specifies the time in seconds by which two consecutive starts of an ExecutableEntity are guaranteed to be separated.

        Returns:
            TimeValue: The minimum start interval
        """
        return self.minimumStartInterval

    def setMinimumStartInterval(self, value: Optional[TimeValue]) -> "ExecutableEntity":
        """
        Sets the minimum start interval. Specifies the time in seconds by which two consecutive starts of an ExecutableEntity are guaranteed to be separated.
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
        Gets the reentrancy level. The reentrancy level of this ExecutableEntity. See the documentation of the enumeration type ReentrancyLevel Enum for details. Please note that nonReentrant interfaces can have also reentrant or multicoreReentrant implementations, and reentrant interfaces can also have multicoreReentrant implementations.

        Returns:
            ReentrancyLevelEnum: The reentrancy level
        """
        return self.reentrancyLevel

    def setReentrancyLevel(self, value: Optional[ReentrancyLevelEnum]) -> "ExecutableEntity":
        """
        Sets the reentrancy level. The reentrancy level of this ExecutableEntity. See the documentation of the enumeration type ReentrancyLevel Enum for details. Please note that nonReentrant interfaces can have also reentrant or multicoreReentrant implementations, and reentrant interfaces can also have multicoreReentrant implementations.
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
        Gets the references to exclusive areas. The executable entity runs completely inside the referenced exclusive area. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=runsInside.exclusiveArea, runs Inside.variationPoint.shortLabel vh.latestBindingTime=preCompileTime

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
        Gets the software address method reference. Addressing method related to this code entity. Via an association to the same SwAddrMethod, it can be specified that several code entities (even of different modules or components) shall be located in the same memory without already specifying the memory section itself.

        Returns:
            RefType: The software address method reference
        """
        return self.swAddrMethodRef

    def setSwAddrMethodRef(self, value: Optional[RefType]) -> "ExecutableEntity":
        """
        Sets the software address method reference. Addressing method related to this code entity. Via an association to the same SwAddrMethod, it can be specified that several code entities (even of different modules or components) shall be located in the same memory without already specifying the memory section itself.
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
    Common base class (abstract) for the internal behavior of both software
    components and basic software modules/clusters.
    """

    # InternalBehavior method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 5.1, p.65
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] createConstantMemory            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getConstantMemories             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addConstantValueMappingRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getConstantValueMappingRefs     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addDataTypeMappingRef           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDataTypeMappingRefs          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createExclusiveArea             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getExclusiveAreas               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createExclusiveAreaNestingOrder [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getExclusiveAreaNestingOrders   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createStaticMemory              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getStaticMemories               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is InternalBehavior:
            raise TypeError("InternalBehavior is an abstract class.")
        super().__init__(parent, short_name)

        # Describes a read only memory object containing characteristic value(s) implemented by this InternalBehavior. The shortName of ParameterDataPrototype has to be equal to the 'C' identifier of the described constant. The characteristic value(s) might be shared between SwComponentPrototypes of the same SwComponentType. The aggregation of constantMemory is subject to variability with the purpose to support variability in the software component or module implementations. Typically different algorithms in the implementation are requiring different number of memory objects. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=constantMemory.shortName, constantMemory.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        self.constantMemories: List[ParameterDataPrototype] = []

        # Reference to the ConstantSpecificationMapping to be applied for the particular InternalBehavior Stereotypes: atpSplitable Tags: atp.Splitkey=constantValueMapping
        self.constantValueMappingRefs: List[RefType] = []

        # Reference to the DataTypeMapping to be applied for the particular InternalBehavior Stereotypes: atpSplitable Tags: atp.Splitkey=dataTypeMapping
        self.dataTypeMappingRefs: List[RefType] = []

        # This specifies an ExclusiveArea for this InternalBehavior. The exclusiveArea is local to the component resp. module. The aggregation of ExclusiveAreas is subject to variability. Note: the number of ExclusiveAreas might vary due to the conditional existence of RunnableEntities or BswModuleEntities. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=exclusiveArea.shortName, exclusiveArea.variationPoint.shortLabel
        self.exclusiveAreas: List["ExclusiveArea"] = []

        # This represents the set of ExclusiveAreaNestingOrder owned by the InternalBehavior. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=exclusiveAreaNestingOrder.shortName, exclusiveAreaNestingOrder.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        self.exclusiveAreaNestingOrders: List["ExclusiveAreaNestingOrder"] = []

        # Describes a read and writeable static memory object representing measurerment variables implemented by this software component. The term "static" is used in the meaning of "non-temporary" and does not necessarily specify a linker encapsulation. This kind of memory is only supported if supportsMultipleInstantiation is FALSE. The shortName of the VariableDataPrototype has to be equal with the 'C' identifier of the described variable. The aggregation of staticMemory is subject to variability with the purpose to support variability in the software component's implementations. Typically different algorithms in the implementation are requiring different number of memory objects. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=staticMemory.shortName, staticMemory.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        self.staticMemories: List[VariableDataPrototype] = []

    def createConstantMemory(self, short_name: str) -> ParameterDataPrototype:
        if short_name not in self.elements:
            prototype = ParameterDataPrototype(self, short_name)
            self.addElement(prototype)
            self.constantMemories.append(prototype)
        return self.getElement(short_name)

    def getConstantMemories(self) -> List[ParameterDataPrototype]:
        """
        Describes a read only memory object containing characteristic value(s) implemented by this InternalBehavior. The shortName of ParameterDataPrototype has to be equal to the 'C' identifier of the described constant. The characteristic value(s) might be shared between SwComponentPrototypes of the same SwComponentType. The aggregation of constantMemory is subject to variability with the purpose to support variability in the software component or module implementations. Typically different algorithms in the implementation are requiring different number of memory objects. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=constantMemory.shortName, constantMemory.variationPoint.shortLabel vh.latestBindingTime=preCompileTime

        Returns:
            List of ParameterDataPrototype instances
        """
        return self.constantMemories

    def addConstantValueMappingRef(self, value: RefType) -> "InternalBehavior":
        """
        Reference to the ConstantSpecificationMapping to be applied for the particular InternalBehavior Stereotypes: atpSplitable Tags: atp.Splitkey=constantValueMapping
        Only adds the value if it is not None.

        Args:
            value: The ConstantSpecificationMappingSet reference to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.constantValueMappingRefs.append(value)
        return self

    def getConstantValueMappingRefs(self) -> List[RefType]:
        """
        Reference to the ConstantSpecificationMapping to be applied for the particular InternalBehavior Stereotypes: atpSplitable Tags: atp.Splitkey=constantValueMapping

        Returns:
            List of RefType instances
        """
        return self.constantValueMappingRefs

    def addDataTypeMappingRef(self, value: RefType) -> "InternalBehavior":
        """
        Reference to the DataTypeMapping to be applied for the particular InternalBehavior Stereotypes: atpSplitable Tags: atp.Splitkey=dataTypeMapping
        Only adds the value if it is not None.

        Args:
            value: The DataTypeMappingSet reference to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.dataTypeMappingRefs.append(value)
        return self

    def getDataTypeMappingRefs(self) -> List[RefType]:
        """
        Reference to the DataTypeMapping to be applied for the particular InternalBehavior Stereotypes: atpSplitable Tags: atp.Splitkey=dataTypeMapping

        Returns:
            List of RefType instances
        """
        return self.dataTypeMappingRefs

    def createExclusiveArea(self, short_name: str) -> "ExclusiveArea":
        """
        This specifies an ExclusiveArea for this InternalBehavior. The exclusiveArea is local to the component resp. module. The aggregation of ExclusiveAreas is subject to variability. Note: the number of ExclusiveAreas might vary due to the conditional existence of RunnableEntities or BswModuleEntities. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=exclusiveArea.shortName, exclusiveArea.variationPoint.shortLabel

        Args:
            short_name: The short name of the exclusive area

        Returns:
            The created (or existing) ExclusiveArea instance
        """
        if short_name not in self.elements:
            area = ExclusiveArea(self, short_name)
            self.addElement(area)
            self.exclusiveAreas.append(area)
        return self.getElement(short_name)

    def getExclusiveAreas(self) -> List["ExclusiveArea"]:
        """
        This specifies an ExclusiveArea for this InternalBehavior. The exclusiveArea is local to the component resp. module. The aggregation of ExclusiveAreas is subject to variability. Note: the number of ExclusiveAreas might vary due to the conditional existence of RunnableEntities or BswModuleEntities. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=exclusiveArea.shortName, exclusiveArea.variationPoint.shortLabel

        Returns:
            List of ExclusiveArea instances
        """
        return self.exclusiveAreas

    def createExclusiveAreaNestingOrder(self, short_name: str) -> "ExclusiveAreaNestingOrder":
        """
        This represents the set of ExclusiveAreaNestingOrder owned by the InternalBehavior. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=exclusiveAreaNestingOrder.shortName, exclusiveAreaNestingOrder.variationPoint.shortLabel vh.latestBindingTime=preCompileTime

        Args:
            short_name: The short name of the exclusive area nesting order

        Returns:
            The created (or existing) ExclusiveAreaNestingOrder instance
        """
        if short_name not in self.elements:
            nesting_order = ExclusiveAreaNestingOrder(self, short_name)
            self.addElement(nesting_order)
            self.exclusiveAreaNestingOrders.append(nesting_order)
        return self.getElement(short_name)

    def getExclusiveAreaNestingOrders(self) -> List["ExclusiveAreaNestingOrder"]:
        """
        This represents the set of ExclusiveAreaNestingOrder owned by the InternalBehavior. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=exclusiveAreaNestingOrder.shortName, exclusiveAreaNestingOrder.variationPoint.shortLabel vh.latestBindingTime=preCompileTime

        Returns:
            List of ExclusiveAreaNestingOrder instances
        """
        return self.exclusiveAreaNestingOrders

    def createStaticMemory(self, short_name: str) -> VariableDataPrototype:
        """
        Describes a read and writeable static memory object representing measurerment variables implemented by this software component. The term "static" is used in the meaning of "non-temporary" and does not necessarily specify a linker encapsulation. This kind of memory is only supported if supportsMultipleInstantiation is FALSE. The shortName of the VariableDataPrototype has to be equal with the 'C' identifier of the described variable. The aggregation of staticMemory is subject to variability with the purpose to support variability in the software component's implementations. Typically different algorithms in the implementation are requiring different number of memory objects. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=staticMemory.shortName, staticMemory.variationPoint.shortLabel vh.latestBindingTime=preCompileTime

        Args:
            short_name: The short name of the static memory

        Returns:
            The created (or existing) VariableDataPrototype instance
        """
        if short_name not in self.elements:
            prototype = VariableDataPrototype(self, short_name)
            self.addElement(prototype)
            self.staticMemories.append(prototype)
        return self.getElement(short_name)

    def getStaticMemories(self) -> List[VariableDataPrototype]:
        """
        Describes a read and writeable static memory object representing measurerment variables implemented by this software component. The term "static" is used in the meaning of "non-temporary" and does not necessarily specify a linker encapsulation. This kind of memory is only supported if supportsMultipleInstantiation is FALSE. The shortName of the VariableDataPrototype has to be equal with the 'C' identifier of the described variable. The aggregation of staticMemory is subject to variability with the purpose to support variability in the software component's implementations. Typically different algorithms in the implementation are requiring different number of memory objects. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=staticMemory.shortName, staticMemory.variationPoint.shortLabel vh.latestBindingTime=preCompileTime

        Returns:
            List of VariableDataPrototype instances
        """
        return self.staticMemories


class AbstractEvent(Identifiable, ABC):
    """
    This meta-class represents the abstract ability to model an event that can be taken to implement application software or basic software in AUTOSAR.
    """

    # AbstractEvent method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.8, p.541
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getActivationReasonRepresentationRef [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setActivationReasonRepresentationRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AbstractEvent:
            raise TypeError("AbstractEvent is an abstract class.")
        super().__init__(parent, short_name)

        # If the activationReasonRepresentation is referenced from the enclosing AbstractEvent this shall be taken as an indication that the latter contributes to the activating vector of this ExecutableEntity that owns the referenced ExecutableEntityActivationReason.
        self.activationReasonRepresentationRef: Optional[RefType] = None

    def getActivationReasonRepresentationRef(self) -> Optional[RefType]:
        """
        If the activationReasonRepresentation is referenced from the enclosing AbstractEvent this shall be taken as an indication that the latter contributes to the activating vector of this ExecutableEntity that owns the referenced ExecutableEntityActivationReason.
        """
        return self.activationReasonRepresentationRef

    def setActivationReasonRepresentationRef(self, value: Optional[RefType]):
        """
        If the activationReasonRepresentation is referenced from the enclosing AbstractEvent this shall be taken as an indication that the latter contributes to the activating vector of this ExecutableEntity that owns the referenced ExecutableEntityActivationReason.
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
    This meta-class represents the ability to define a nesting order of ExclusiveAreas. A nesting order (that may occur in the executable code) is formally defined to be able to analyze the resource locking behavior.
    """

    # ExclusiveAreaNestingOrder method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 5.19, p.84
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getExclusiveAreaRefs    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addExclusiveAreaRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents a specific scenario of how Exclusive Areas can be used in terms of the nesting order.
        self.exclusiveAreaRefs: List[RefType] = []

    def getExclusiveAreaRefs(self) -> List[RefType]:
        """
        This represents a specific scenario of how Exclusive Areas can be used in terms of the nesting order.

        Returns:
            List of RefType instances
        """
        return self.exclusiveAreaRefs

    def addExclusiveAreaRef(self, value: RefType) -> "ExclusiveAreaNestingOrder":
        """
        This represents a specific scenario of how Exclusive Areas can be used in terms of the nesting order.
        Only adds the value if it is not None.

        Args:
            value: The exclusive area reference to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.exclusiveAreaRefs.append(value)
        return self


class ExecutableEntityActivationReason(ImplementationProps):
    """
    This meta-class represents the ability to define the reason for the
    activation of the enclosing Executable Entity.
    """

    # ExecutableEntityActivationReason method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table D.30, p.315
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getBitPosition  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setBitPosition  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the ExecutableEntityActivationReason with a parent and
        short name.
        """
        super().__init__(parent, short_name)

        # This attribute allows for defining the position of the enclosing
        # ExecutableEntityActivationReason in the activation vector.
        # [constr_1226, constr_1939]
        self.bitPosition: Optional[PositiveInteger] = None

    def getBitPosition(self) -> Optional[PositiveInteger]:
        """
        Gets the position of the enclosing ExecutableEntityActivationReason in
        the activation vector. [constr_1226, constr_1939]

        Returns:
            PositiveInteger: The bit position in the activation vector
        """
        return self.bitPosition

    def setBitPosition(self, value: Optional[PositiveInteger]) -> "ExecutableEntityActivationReason":
        """
        Sets the position of the enclosing ExecutableEntityActivationReason in
        the activation vector. A None value is a no-op and does not overwrite
        an existing bitPosition. [constr_1226, constr_1939]

        Args:
            value: The bit position in the activation vector

        Returns:
            self for method chaining
        """
        if value is not None:
            self.bitPosition = value
        return self
