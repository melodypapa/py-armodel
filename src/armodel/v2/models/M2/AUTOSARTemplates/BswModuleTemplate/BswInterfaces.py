"""
This module contains classes for representing AUTOSAR Basic Software (BSW) interfaces.
BSW interfaces define how BSW modules interact with other software components,
including dependencies, module entries, and client-server interfaces.
"""

from typing import List, Union

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    ServiceNeeds,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import (
    AtpBlueprintable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
    Referrable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    ARNumerical,
    Boolean,
    Identifier,
    NameToken,
    PositiveInteger,
    RefType,
)
from armodel.v2.models.M2.MSR.DataDictionary.ServiceProcessTask import (
    SwServiceArg,
    SwServiceImplPolicyEnum,
)


class BswEntryKindEnum(AREnum):
    """
    Enumeration for BSW Entry Kind values.
    Defines the types of entries that can exist in BSW modules.
    """
    # Function entry type for BSW module entries
    FUNCTION = "FUNCTION"

    def __init__(self) -> None:
        super().__init__((
            BswEntryKindEnum.FUNCTION,
        ))


class BswCallType(AREnum):
    """
    Enumeration for BSW Call Type values.
    Defines how BSW module entries can be called (synchronously or asynchronously).
    """
    # Synchronous call type - caller waits for completion
    SYNCHRONOUS = "SYNCHRONOUS"
    # Asynchronous call type - caller does not wait for completion
    ASYNCHRONOUS = "ASYNCHRONOUS"

    def __init__(self) -> None:
        super().__init__((
            BswCallType.SYNCHRONOUS,
            BswCallType.ASYNCHRONOUS,
        ))


class BswExecutionContext(AREnum):
    """
    Enumeration for BSW Execution Context values.
    Defines where BSW module entries can execute in the system.
    """
    # Execution in a hook function context
    HOOK = "HOOK"
    # Execution in interrupt category 1 context (high priority)
    INTERRUPT_CAT_1 = "INTERRUPT-CAT-1"
    # Execution in interrupt category 2 context (medium priority)
    INTERRUPT_CAT_2 = "INTERRUPT-CAT-2"
    # Execution in a task context
    TASK = "TASK"
    # Execution context is unspecified
    UNSPECIFIED = "UNSPECIFIED"

    def __init__(self) -> None:
        super().__init__((
            BswExecutionContext.HOOK,
            BswExecutionContext.INTERRUPT_CAT_1,
            BswExecutionContext.INTERRUPT_CAT_2,
            BswExecutionContext.TASK,
            BswExecutionContext.UNSPECIFIED,
        ))


class BswModuleDependency(Identifiable):
    """
    Represents a dependency relationship between BSW modules.
    This class defines how one BSW module depends on services from another module.
    """

    def __init__(self, parent: ARObject, short_name: str) -> None:
        """
        Initializes the BSW module dependency with a parent and short name.

        Args:
            parent: The parent ARObject that contains this dependency
            short_name: The unique short name of this dependency
        """
        super().__init__(parent, short_name)

        # List of service needs that this dependency requires
        self.serviceItems: List[ServiceNeeds] = []
        # Unique identifier for the target module in the dependency
        self.targetModuleId: Union[Union[PositiveInteger, None] , None] = None
        # Reference to the target module in the dependency
        self.targetModuleRef: Union[Union[RefType, None] , None] = None

    def getServiceItems(self):
        """
        Gets the list of service needs that this dependency requires.

        Returns:
            List of ServiceNeeds instances
        """
        return self.serviceItems

    def setServiceItems(self, value):
        """
        Sets the list of service needs that this dependency requires.
        Only sets the value if it is not None.

        Args:
            value: List of ServiceNeeds instances to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.serviceItems = value
        return self

    def getTargetModuleId(self):
        """
        Gets the unique identifier for the target module in the dependency.

        Returns:
            Positive integer representing the target module ID
        """
        return self.targetModuleId

    def setTargetModuleId(self, value):
        """
        Sets the unique identifier for the target module in the dependency.
        Only sets the value if it is not None.

        Args:
            value: The target module ID to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.targetModuleId = value
        return self

    def getTargetModuleRef(self):
        """
        Gets the reference to the target module in the dependency.

        Returns:
            RefType to the target module
        """
        return self.targetModuleRef

    def setTargetModuleRef(self, value):
        """
        Sets the reference to the target module in the dependency.
        Only sets the value if it is not None.

        Args:
            value: The target module reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.targetModuleRef = value
        return self


class BswModuleEntry(AtpBlueprintable):
    """
    Represents an entry point in a BSW module.
    This class defines how BSW module functions can be accessed and executed.
    """

    def __init__(self, parent: ARObject, short_name: str) -> None:
        """
        Initializes the BSW module entry with a parent and short name.

        Args:
            parent: The parent ARObject that contains this entry
            short_name: The unique short name of this entry
        """
        super().__init__(parent, short_name)

        # List of arguments for this module entry
        self.arguments: List[SwServiceArg] = []
        # Kind of BSW entry (e.g., FUNCTION)
        self.bswEntryKind: Union[Union[BswEntryKindEnum, None] , None] = None
        # Call type (synchronous or asynchronous)
        self.callType: Union[Union[BswCallType, None] , None] = None
        # Execution context where this entry runs
        self.executionContext: Union[Union[BswExecutionContext, None] , None] = None
        # Function prototype emitter name token
        self.functionPrototypeEmitter: Union[Union[NameToken, None] , None] = None
        # Flag indicating if this entry is reentrant (can be called concurrently)
        self.isReentrant: Union[Union[Boolean, None] , None] = None
        # Flag indicating if this entry is synchronous
        self.isSynchronous: Union[Union[Boolean, None] , None] = None
        # Return type of this entry
        self.returnType: Union[Union[SwServiceArg, None] , None] = None
        # Role identifier for this entry
        self.role: Union[Union[Identifier, None] , None] = None
        # Service identifier for this entry
        self.serviceId: Union[Union[ARNumerical, None] , None] = None
        # Software service implementation policy
        self.swServiceImplPolicy: Union[Union[SwServiceImplPolicyEnum, None] , None] = None

    def getArguments(self):
        """
        Gets the list of arguments for this module entry.

        Returns:
            List of SwServiceArg instances
        """
        return self.arguments

    def createArgument(self, short_name: str) -> SwServiceArg:
        """
        Creates and adds an argument to this module entry.

        Args:
            short_name: The short name for the new argument

        Returns:
            The created SwServiceArg instance
        """
        if (short_name not in self.elements):
            arg = SwServiceArg(self, short_name)
            self.addElement(arg)
            self.arguments.append(arg)
        return self.getElement(short_name)

    def getBswEntryKind(self):
        """
        Gets the kind of BSW entry.

        Returns:
            BswEntryKindEnum value
        """
        return self.bswEntryKind

    def setBswEntryKind(self, value):
        """
        Sets the kind of BSW entry.

        Args:
            value: The BswEntryKindEnum value to set

        Returns:
            self for method chaining
        """
        self.bswEntryKind = value
        return self

    def getCallType(self):
        """
        Gets the call type for this module entry.

        Returns:
            BswCallType value
        """
        return self.callType

    def setCallType(self, value):
        """
        Sets the call type for this module entry.

        Args:
            value: The BswCallType value to set

        Returns:
            self for method chaining
        """
        self.callType = value
        return self

    def getExecutionContext(self):
        """
        Gets the execution context for this module entry.

        Returns:
            BswExecutionContext value
        """
        return self.executionContext

    def setExecutionContext(self, value):
        """
        Sets the execution context for this module entry.
        Validates that the value is one of the allowed execution contexts.

        Args:
            value: The BswExecutionContext value to set

        Returns:
            self for method chaining

        Raises:
            ValueError: If the execution context is not valid
        """
        if value.upper() not in ("HOOK", "INTERRUPT-CAT-1", "INTERRUPT-CAT-2", "TASK", "UNSPECIFIED"):
            raise ValueError("Invalid execution context <%s> of BswModuleEntry <%s>" % (value, self.short_name))
        self.executionContext = value
        return self

    def getFunctionPrototypeEmitter(self):
        """
        Gets the function prototype emitter name token.

        Returns:
            NameToken for the function prototype emitter
        """
        return self.functionPrototypeEmitter

    def setFunctionPrototypeEmitter(self, value):
        """
        Sets the function prototype emitter name token.

        Args:
            value: The NameToken to set

        Returns:
            self for method chaining
        """
        self.functionPrototypeEmitter = value
        return self

    def getIsReentrant(self):
        """
        Gets the reentrant flag for this module entry.

        Returns:
            Boolean indicating if this entry is reentrant
        """
        return self.isReentrant

    def setIsReentrant(self, value):
        """
        Sets the reentrant flag for this module entry.

        Args:
            value: The reentrant flag to set

        Returns:
            self for method chaining
        """
        self.isReentrant = value
        return self

    def getIsSynchronous(self):
        """
        Gets the synchronous flag for this module entry.

        Returns:
            Boolean indicating if this entry is synchronous
        """
        return self.isSynchronous

    def setIsSynchronous(self, value):
        """
        Sets the synchronous flag for this module entry.

        Args:
            value: The synchronous flag to set

        Returns:
            self for method chaining
        """
        self.isSynchronous = value
        return self

    def getReturnType(self):
        """
        Gets the return type for this module entry.

        Returns:
            SwServiceArg instance representing the return type
        """
        return self.returnType

    def createReturnType(self, short_name: str) -> SwServiceArg:
        """
        Creates and sets the return type for this module entry.

        Args:
            short_name: The short name for the new return type

        Returns:
            The created SwServiceArg instance
        """
        if (short_name not in self.elements):
            arg = SwServiceArg(self, short_name)
            self.addElement(arg)
            self.returnType = arg
        return self.getElement(short_name)

    def getRole(self):
        """
        Gets the role identifier for this module entry.

        Returns:
            Identifier for the role
        """
        return self.role

    def setRole(self, value):
        """
        Sets the role identifier for this module entry.

        Args:
            value: The role identifier to set

        Returns:
            self for method chaining
        """
        self.role = value
        return self

    def getServiceId(self):
        """
        Gets the service identifier for this module entry.

        Returns:
            ARNumerical representing the service ID
        """
        return self.serviceId

    def setServiceId(self, value):
        """
        Sets the service identifier for this module entry.

        Args:
            value: The service ID to set

        Returns:
            self for method chaining
        """
        self.serviceId = value
        return self

    def getSwServiceImplPolicy(self):
        """
        Gets the software service implementation policy for this module entry.

        Returns:
            SwServiceImplPolicyEnum value
        """
        return self.swServiceImplPolicy

    def setSwServiceImplPolicy(self, value):
        """
        Sets the software service implementation policy for this module entry.
        Validates that the value is one of the allowed implementation policies.

        Args:
            value: The SwServiceImplPolicyEnum value to set

        Returns:
            self for method chaining

        Raises:
            ValueError: If the implementation policy is not valid
        """
        if value.upper() not in ("INLINE", "INLINE-CONDITIONAL", "MACRO", "STANDARD"):
            raise ValueError("Invalid SwServiceImplPolicy <%s> of BswModuleEntry <%s>" % (value, self.short_name))
        self.swServiceImplPolicy = value
        return self

    def __str__(self) -> str:
        """
        Returns a string representation of this BSW module entry.
        Shows the key properties of the entry in a formatted way.

        Returns:
            Formatted string representation of the BSW module entry
        """
        result = []

        result.append("short_name             : %s" % self.short_name)
        if self.serviceId is not None:
            result.append("service_id             : %d" % self.serviceId.getValue())
        if self.isReentrant is not None:
            result.append("is_reentrant           : %s" % self.isReentrant)
        if self.isSynchronous is not None:
            result.append("is_synchronous         : %s" % self.isSynchronous)
        if self.callType is not None:
            result.append("call_type              : %s" % self.callType)
        if self.executionContext is not None:
            result.append("execution_context      : %s" % self.executionContext)
        if self.swServiceImplPolicy is not None:
            result.append("sw_service_impl_policy : %s" % self.swServiceImplPolicy)

        return "\n".join(result)


class BswModuleClientServerEntry(Referrable):
    """
    Represents a client-server entry in a BSW module.
    This class defines how BSW modules implement client-server communication patterns.
    """

    def __init__(self, parent: ARObject, short_name: str) -> None:
        """
        Initializes the BSW module client-server entry with a parent and short name.

        Args:
            parent: The parent ARObject that contains this client-server entry
            short_name: The unique short name of this client-server entry
        """
        super().__init__(parent, short_name)

        # Reference to the encapsulated entry that this client-server entry wraps
        self.encapsulatedEntryRef: Union[Union[RefType, None] , None] = None
        # Flag indicating if this client-server entry is reentrant
        self.isReentrant: Union[Union[Boolean, None] , None] = None
        # Flag indicating if this client-server entry is synchronous
        self.isSynchronous: Union[Union[Boolean, None] , None] = None

    def getEncapsulatedEntryRef(self):
        """
        Gets the reference to the encapsulated entry that this client-server entry wraps.

        Returns:
            RefType to the encapsulated entry
        """
        return self.encapsulatedEntryRef

    def setEncapsulatedEntryRef(self, value):
        """
        Sets the reference to the encapsulated entry that this client-server entry wraps.
        Only sets the value if it is not None.

        Args:
            value: The encapsulated entry reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.encapsulatedEntryRef = value
        return self

    def getIsReentrant(self):
        """
        Gets the reentrant flag for this client-server entry.

        Returns:
            Boolean indicating if this entry is reentrant
        """
        return self.isReentrant

    def setIsReentrant(self, value):
        """
        Sets the reentrant flag for this client-server entry.
        Only sets the value if it is not None.

        Args:
            value: The reentrant flag to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.isReentrant = value
        return self

    def getIsSynchronous(self):
        """
        Gets the synchronous flag for this client-server entry.

        Returns:
            Boolean indicating if this entry is synchronous
        """
        return self.isSynchronous

    def setIsSynchronous(self, value):
        """
        Sets the synchronous flag for this client-server entry.
        Only sets the value if it is not None.

        Args:
            value: The synchronous flag to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.isSynchronous = value
        return self

# ========== Classes from subdirectory files ==========

"""
This module defines BSW entry relationship in AUTOSAR.
"""

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class BswEntryRelationship(ARObject):
    """
    Represents a BSW entry relationship in AUTOSAR.
    This class defines relationships between BSW entries.
    """


    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        """
        Initializes the BswEntryRelationship with default values.
        """
        super().__init__()
        self.relationType: Union[str, None] = None

    def getRelationType(self):
        return self.relationType

    def setRelationType(self, value):
        self.relationType = value
        return self

"""
This module defines BSW entry relationship enum in AUTOSAR.
"""

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)


class BswEntryRelationshipEnum(AREnum):
    """
    Enumeration for BSW entry relationship types.
    """

    READS = "reads"
    WRITES = "writes"
    CALLS = "calls"
    TRIGGERS = "triggers"

    def __init__(self) -> None:
        super().__init__((
            BswEntryRelationshipEnum.READS,
            BswEntryRelationshipEnum.WRITES,
            BswEntryRelationshipEnum.CALLS,
            BswEntryRelationshipEnum.TRIGGERS,
        ))

"""
This module defines BSW entry relationship set in AUTOSAR.
"""

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class BswEntryRelationshipSet(ARObject):
    """
    Represents a set of BSW entry relationships in AUTOSAR.
    """


    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        """
        Initializes the BswEntryRelationshipSet with default values.
        """
        super().__init__()
        self.relationships = []

    def addRelationship(self, relationship) -> None:
        self.relationships.append(relationship)

    def getRelationships(self):
        return self.relationships

