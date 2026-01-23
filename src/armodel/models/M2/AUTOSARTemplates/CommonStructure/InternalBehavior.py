"""
This module contains classes for representing AUTOSAR internal behavior structures
in the CommonStructure module. Internal behavior classes define executable entities,
exclusive areas, and event handling mechanisms within AUTOSAR components and BSW modules.
"""

from abc import ABC
from enum import Enum
from typing import List
from ....M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARFloat, RefType
from ....M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import ParameterDataPrototype, VariableDataPrototype


class ReentrancyLevelEnum(Enum):
    """
    Enumeration for reentrancy levels in AUTOSAR executable entities.
    Defines whether an executable entity can be executed concurrently from multiple contexts.
    """
    # Enum value for multicore reentrant executable entities
    ENUM_MULTICORE_REENTRANT = "multicoreReentrant"
    # Enum value for non-reentrant executable entities
    ENUM_NON_REENTRANT = "nonReentrant"
    # Enum value for single core reentrant executable entities
    ENUM_SINGLE_CORE_REENTRANT = "singleCoreReentrant"


class ExclusiveArea(Identifiable):
    """
    Represents an exclusive area in AUTOSAR models.
    Exclusive areas define critical sections that must not be executed concurrently,
    typically used for protecting shared resources in multithreaded environments.
    """
    
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
    Abstract base class for executable entities in AUTOSAR models.
    Executable entities represent pieces of executable code that can be triggered by events
    and may have specific execution requirements like exclusive areas or reentrancy levels.
    """
    
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

        # List of activation reasons for this executable entity
        self.activationReasons: List = []                 
        # List of references to exclusive areas this entity can enter
        self.canEnterExclusiveAreaRefs: List[RefType] = []         
        # Minimum interval between consecutive starts of this entity (in seconds)
        self.minimumStartInterval: ARFloat = None            
        # Reentrancy level of this executable entity
        self.reentrancyLevel: ReentrancyLevelEnum = None                 
        # Reference to the software address method for this entity
        self.swAddrMethodRef: RefType = None                 

    def getActivationReasons(self):
        """
        Gets the list of activation reasons for this executable entity.
        
        Returns:
            List of ExecutableEntityActivationReason instances
        """
        return self.activationReasons

    def addActivationReason(self, value):
        """
        Adds an activation reason to this executable entity.
        
        Args:
            value: The activation reason to add
            
        Returns:
            self for method chaining
        """
        self.activationReasons.append(value)
        return self

    def getMinimumStartInterval(self):
        """
        Gets the minimum interval between consecutive starts of this entity (in seconds).
        
        Returns:
            ARFloat: The minimum start interval
        """
        return self.minimumStartInterval

    def setMinimumStartInterval(self, value):
        """
        Sets the minimum interval between consecutive starts of this entity (in seconds).
        Only sets the value if it is not None.
        
        Args:
            value: The minimum start interval to set
            
        Returns:
            self for method chaining
        """
        self.minimumStartInterval = value
        return self

    def getReentrancyLevel(self):
        """
        Gets the reentrancy level of this executable entity.
        
        Returns:
            ReentrancyLevelEnum: The reentrancy level
        """
        return self.reentrancyLevel

    def setReentrancyLevel(self, value):
        """
        Sets the reentrancy level of this executable entity.
        Only sets the value if it is not None.
        
        Args:
            value: The reentrancy level to set
            
        Returns:
            self for method chaining
        """
        self.reentrancyLevel = value
        return self

    def getSwAddrMethodRef(self):
        """
        Gets the reference to the software address method for this entity.
        
        Returns:
            RefType: The software address method reference
        """
        return self.swAddrMethodRef

    def setSwAddrMethodRef(self, value):
        """
        Sets the reference to the software address method for this entity.
        Only sets the value if it is not None.
        
        Args:
            value: The software address method reference to set
            
        Returns:
            self for method chaining
        """
        self.swAddrMethodRef = value
        return self

    @property
    def minimumStartIntervalMs(self) -> int:
        """
        Gets the minimum start interval in milliseconds (converted from seconds).
        This is a computed property that converts the minimum start interval from seconds to milliseconds.
        
        Returns:
            int: The minimum start interval in milliseconds, or None if not set
        """
        if self.minimumStartInterval is not None:
            return int(self.minimumStartInterval.getValue() * 1000)
        return None

    def addCanEnterExclusiveAreaRef(self, ref: RefType):
        """
        Adds a reference to an exclusive area that this entity can enter.
        
        Args:
            ref: The reference to the exclusive area
        """
        self.canEnterExclusiveAreaRefs.append(ref)

    def getCanEnterExclusiveAreaRefs(self):
        """
        Gets the list of references to exclusive areas this entity can enter.
        
        Returns:
            List of RefType instances
        """
        return self.canEnterExclusiveAreaRefs


class InternalBehavior(AtpStructureElement, ABC):
    """
    Abstract base class for internal behavior in AUTOSAR models.
    Internal behavior defines the internal structure of software components or BSW modules,
    including executable entities, memory areas, and data type mappings.
    """
    
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
        self.exclusiveAreas: List['ExclusiveArea'] = []                            
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
        if (short_name not in self.elements):
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
        if (short_name not in self.elements):
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
        if (short_name not in self.elements):
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
