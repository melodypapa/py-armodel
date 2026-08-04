"""
This module contains classes for representing AUTOSAR Basic Software (BSW) interfaces.
BSW interfaces define how BSW modules interact with other software components,
including dependencies, module entries, and client-server interfaces.
"""

from typing import List, Optional
from enum import Enum

from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpBlueprintable
from armodel.models.M2.MSR.DataDictionary.ServiceProcessTask import SwServiceArg
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import ServiceNeeds
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable, Referrable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARNumerical, Boolean, Identifier, NameToken, RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger


class BswEntryKindEnum(str, Enum):
    """
    Enumeration for BSW Entry Kind values.
    Defines the types of entries that can exist in BSW modules.
    """
    # BswEntryKindEnum method parity checklist:
    # (no methods)

    # Function entry type for BSW module entries
    FUNCTION = "FUNCTION"


class BswCallType(str, Enum):
    """
    Enumeration for BSW Call Type values.
    Defines how BSW module entries can be called (synchronously or asynchronously).
    """
    # BswCallType method parity checklist:
    # (no methods)

    # Synchronous call type - caller waits for completion
    SYNCHRONOUS = "SYNCHRONOUS"
    # Asynchronous call type - caller does not wait for completion
    ASYNCHRONOUS = "ASYNCHRONOUS"


class BswExecutionContext(str, Enum):
    """
    Enumeration for BSW Execution Context values.
    Defines where BSW module entries can execute in the system.
    """
    # BswExecutionContext method parity checklist:
    # (no methods)

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


class SwServiceImplPolicyEnum(str, Enum):
    """
    Enumeration for SW Service Implementation Policy values.
    Defines how software service implementations should be generated in code.
    """
    # SwServiceImplPolicyEnum method parity checklist:
    # (no methods)

    # Implementation should be inlined
    INLINE = "INLINE"
    # Implementation should be inlined conditionally based on configuration
    INLINE_CONDITIONAL = "INLINE-CONDITIONAL"
    # Implementation should be generated as a macro
    MACRO = "MACRO"
    # Standard implementation (not inlined)
    STANDARD = "STANDARD"


class BswModuleDependency(Identifiable):
    """
    Represents a dependency relationship between BSW modules.
    This class defines how one BSW module depends on services from another module.
    """
    # BswModuleDependency method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [ ] getServiceItems              [x] impl  [x] docstring  [ ] test
    # [ ] setServiceItems              [x] impl  [x] docstring  [ ] test
    # [ ] getTargetModuleId            [x] impl  [x] docstring  [ ] test
    # [ ] setTargetModuleId            [x] impl  [x] docstring  [ ] test
    # [ ] getTargetModuleRef           [x] impl  [x] docstring  [ ] test
    # [ ] setTargetModuleRef           [x] impl  [x] docstring  [ ] test

    
    def __init__(self, parent: ARObject, short_name: str):
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
        self.targetModuleId: PositiveInteger = None                  
        # Reference to the target module in the dependency
        self.targetModuleRef: RefType = None                 

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
    Represents a single API entry (C-function prototype) into the BSW module or cluster.
    The name of the C-function is equal to the short name of this element.
    """
    # BswModuleEntry method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getArguments                 [x] impl  [x] docstring  [x] test
    # [x] createArgument               [x] impl  [x] docstring  [x] test
    # [x] getBswEntryKind              [x] impl  [x] docstring  [x] test
    # [x] setBswEntryKind              [x] impl  [x] docstring  [x] test
    # [x] getCallType                  [x] impl  [x] docstring  [x] test
    # [x] setCallType                  [x] impl  [x] docstring  [x] test
    # [x] getExecutionContext          [x] impl  [x] docstring  [x] test
    # [x] setExecutionContext          [x] impl  [x] docstring  [x] test
    # [x] getFunctionPrototypeEmitter  [x] impl  [x] docstring  [x] test
    # [x] setFunctionPrototypeEmitter  [x] impl  [x] docstring  [x] test
    # [x] getIsReentrant               [x] impl  [x] docstring  [x] test
    # [x] setIsReentrant               [x] impl  [x] docstring  [x] test
    # [x] getIsSynchronous             [x] impl  [x] docstring  [x] test
    # [x] setIsSynchronous             [x] impl  [x] docstring  [x] test
    # [x] getReturnType                [x] impl  [x] docstring  [x] test
    # [x] createReturnType             [x] impl  [x] docstring  [x] test
    # [x] getRole                      [x] impl  [x] docstring  [x] test
    # [x] setRole                      [x] impl  [x] docstring  [x] test
    # [x] getServiceId                 [x] impl  [x] docstring  [x] test
    # [x] setServiceId                 [x] impl  [x] docstring  [x] test
    # [x] getSwServiceImplPolicy       [x] impl  [x] docstring  [x] test
    # [x] setSwServiceImplPolicy       [x] impl  [x] docstring  [x] test
    # [x] __str__                      [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the BSW module entry with a parent and short name.

        Args:
            parent: The parent ARObject that contains this entry
            short_name: The unique short name of this entry
        """
        super().__init__(parent, short_name)

        # An argument belonging to this BswModuleEntry.
        self.arguments: List[SwServiceArg] = []

        # This describes whether the entry is concrete or abstract.
        # If the attribute is missing the entry is considered as concrete.
        self.bswEntryKind: BswEntryKindEnum = None

        # The type of call associated with this service.
        self.callType: BswCallType = None

        # Specifies the execution context which is required (in case of entries into this
        # module) or guaranteed (in case of entries called from this module) for this service.
        self.executionContext: BswExecutionContext = None

        # This attribute is used to control the generation of function prototypes.
        # If set to "RTE", the RTE generates the function prototypes in the Module
        # Interlink Header File.
        self.functionPrototypeEmitter: NameToken = None

        # Reentrancy from the viewpoint of function callers:
        # - true: Enables the service to be invoked again, before the service has finished.
        # - false: It is prohibited to invoke the service again before it has finished.
        self.isReentrant: Boolean = None

        # Synchronicity from the viewpoint of function callers:
        # - true: This calls a synchronous service, i.e. the service is completed when the
        #   call returns.
        # - false: The service (on semantical level) may not be complete when the call
        #   returns.
        self.isSynchronous: Boolean = None

        # The return type belonging to this BswModuleEntry.
        self.returnType: SwServiceArg = None

        # Specifies the role of the entry in the given context. It shall be equal to the
        # standardized name of the service call, especially in cases where no
        # ServiceIdentifier is specified, e.g. for callbacks.
        self.role: Identifier = None

        # Refers to the service identifier of the Standardized Interfaces of AUTOSAR basic
        # software. For non-standardized interfaces, it can optionally be used for
        # proprietary identification.
        self.serviceId: ARNumerical = None

        # Denotes the implementation policy as a standard function call, inline function
        # or macro. This has to be specified on interface level because it determines the
        # signature of the call.
        self.swServiceImplPolicy: SwServiceImplPolicyEnum = None

    def getArguments(self) -> List[SwServiceArg]:
        """
        Gets the list of arguments belonging to this BswModuleEntry.

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

    def getBswEntryKind(self) -> Optional[BswEntryKindEnum]:
        """
        Gets whether the entry is concrete or abstract.
        If the attribute is missing the entry is considered as concrete.

        Returns:
            BswEntryKindEnum value
        """
        return self.bswEntryKind

    def setBswEntryKind(self, value: BswEntryKindEnum) -> "BswModuleEntry":
        """
        Sets whether the entry is concrete or abstract.
        If the attribute is missing the entry is considered as concrete.
        Only sets the value if it is not None.

        Args:
            value: The BswEntryKindEnum value to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.bswEntryKind = value
        return self

    def getCallType(self) -> Optional[BswCallType]:
        """
        Gets the type of call associated with this service.

        Returns:
            BswCallType value
        """
        return self.callType

    def setCallType(self, value: BswCallType) -> "BswModuleEntry":
        """
        Sets the type of call associated with this service.
        Only sets the value if it is not None.

        Args:
            value: The BswCallType value to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.callType = value
        return self

    def getExecutionContext(self) -> Optional[BswExecutionContext]:
        """
        Gets the execution context which is required (in case of entries into this module)
        or guaranteed (in case of entries called from this module) for this service.

        Returns:
            BswExecutionContext value
        """
        return self.executionContext

    def setExecutionContext(self, value: BswExecutionContext) -> "BswModuleEntry":
        """
        Sets the execution context which is required (in case of entries into this module)
        or guaranteed (in case of entries called from this module) for this service.
        Validates that the value is one of the allowed execution contexts.
        Only sets the value if it is not None.

        Args:
            value: The BswExecutionContext value to set

        Returns:
            self for method chaining

        Raises:
            ValueError: If the execution context is not valid
        """
        if value is not None:
            if value.upper() not in ("HOOK", "INTERRUPT-CAT-1", "INTERRUPT-CAT-2", "TASK", "UNSPECIFIED"):
                raise ValueError("Invalid execution context <%s> of BswModuleEntry <%s>" % (value, self.short_name))
            self.executionContext = value
        return self

    def getFunctionPrototypeEmitter(self) -> Optional[NameToken]:
        """
        Gets the function prototype emitter used to control the generation of function
        prototypes. If set to "RTE", the RTE generates the function prototypes in the
        Module Interlink Header File.

        Returns:
            NameToken for the function prototype emitter
        """
        return self.functionPrototypeEmitter

    def setFunctionPrototypeEmitter(self, value: NameToken) -> "BswModuleEntry":
        """
        Sets the function prototype emitter used to control the generation of function
        prototypes. If set to "RTE", the RTE generates the function prototypes in the
        Module Interlink Header File.
        Only sets the value if it is not None.

        Args:
            value: The NameToken to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.functionPrototypeEmitter = value
        return self

    def getIsReentrant(self) -> Optional[Boolean]:
        """
        Gets the reentrancy flag from the viewpoint of function callers.

        Returns:
            Boolean indicating if this entry is reentrant
        """
        return self.isReentrant

    def setIsReentrant(self, value: Boolean) -> "BswModuleEntry":
        """
        Sets the reentrancy flag from the viewpoint of function callers.
        Only sets the value if it is not None.

        Args:
            value: The reentrant flag to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.isReentrant = value
        return self

    def getIsSynchronous(self) -> Optional[Boolean]:
        """
        Gets the synchronicity flag from the viewpoint of function callers.

        Returns:
            Boolean indicating if this entry is synchronous
        """
        return self.isSynchronous

    def setIsSynchronous(self, value: Boolean) -> "BswModuleEntry":
        """
        Sets the synchronicity flag from the viewpoint of function callers.
        Only sets the value if it is not None.

        Args:
            value: The synchronous flag to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.isSynchronous = value
        return self

    def getReturnType(self) -> Optional[SwServiceArg]:
        """
        Gets the return type belonging to this BswModuleEntry.

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

    def getRole(self) -> Optional[Identifier]:
        """
        Gets the role of the entry in the given context.
        It shall be equal to the standardized name of the service call.

        Returns:
            Identifier for the role
        """
        return self.role

    def setRole(self, value: Identifier) -> "BswModuleEntry":
        """
        Sets the role of the entry in the given context.
        It shall be equal to the standardized name of the service call.
        Only sets the value if it is not None.

        Args:
            value: The role identifier to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.role = value
        return self

    def getServiceId(self) -> Optional[ARNumerical]:
        """
        Gets the service identifier of the Standardized Interfaces of AUTOSAR basic
        software. For non-standardized interfaces, it can optionally be used for
        proprietary identification.

        Returns:
            ARNumerical representing the service ID
        """
        return self.serviceId

    def setServiceId(self, value: ARNumerical) -> "BswModuleEntry":
        """
        Sets the service identifier of the Standardized Interfaces of AUTOSAR basic
        software. For non-standardized interfaces, it can optionally be used for
        proprietary identification.
        Only sets the value if it is not None.

        Args:
            value: The service ID to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.serviceId = value
        return self

    def getSwServiceImplPolicy(self) -> Optional[SwServiceImplPolicyEnum]:
        """
        Gets the implementation policy as a standard function call, inline function or
        macro. This has to be specified on interface level because it determines the
        signature of the call.

        Returns:
            SwServiceImplPolicyEnum value
        """
        return self.swServiceImplPolicy

    def setSwServiceImplPolicy(self, value: SwServiceImplPolicyEnum) -> "BswModuleEntry":
        """
        Sets the implementation policy as a standard function call, inline function or
        macro. This has to be specified on interface level because it determines the
        signature of the call.
        Validates that the value is one of the allowed implementation policies.
        Only sets the value if it is not None.

        Args:
            value: The SwServiceImplPolicyEnum value to set

        Returns:
            self for method chaining

        Raises:
            ValueError: If the implementation policy is not valid
        """
        if value is not None:
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
    # BswModuleClientServerEntry method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [ ] getEncapsulatedEntryRef      [x] impl  [x] docstring  [ ] test
    # [ ] setEncapsulatedEntryRef      [x] impl  [x] docstring  [ ] test
    # [ ] getIsReentrant               [x] impl  [x] docstring  [ ] test
    # [ ] setIsReentrant               [x] impl  [x] docstring  [ ] test
    # [ ] getIsSynchronous             [x] impl  [x] docstring  [ ] test
    # [ ] setIsSynchronous             [x] impl  [x] docstring  [ ] test

    
    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the BSW module client-server entry with a parent and short name.
        
        Args:
            parent: The parent ARObject that contains this client-server entry
            short_name: The unique short name of this client-server entry
        """
        super().__init__(parent, short_name)

        # Reference to the encapsulated entry that this client-server entry wraps
        self.encapsulatedEntryRef: RefType = None                        
        # Flag indicating if this client-server entry is reentrant
        self.isReentrant: Boolean = None                                
        # Flag indicating if this client-server entry is synchronous
        self.isSynchronous: Boolean = None                              

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
