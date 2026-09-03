"""
This module contains classes for representing AUTOSAR Basic Software (BSW) interfaces.
BSW interfaces define how BSW modules interact with other software components,
including dependencies, module entries, and client-server interfaces.
"""

from typing import List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import AtpBlueprintable
from armodel.models.M2.MSR.DataDictionary.ServiceProcessTask import SwServiceArg
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable, Referrable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Identifier, NameToken, RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, AREnum


class BswEntryKindEnum(AREnum):
    """
    Denotes the mechanism by which the entry into the Bsw module shall be called.
    """

    # BswEntryKindEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 4.2, p.34
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on BswModuleEntry.bswEntryKind
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    # This BswModuleEntry specifies an abstract signature of C-functions. The signature needs to be implemented by concrete BswModuleEntrys Tags: atp.EnumerationLiteralIndex=0
    ABSTRACT = "abstract"

    # This BswModuleEntry specifies a concrete C-function with its signature. Tags: atp.EnumerationLiteralIndex=1
    CONCRETE = "concrete"

    def __init__(self):
        super().__init__([BswEntryKindEnum.ABSTRACT, BswEntryKindEnum.CONCRETE])


class BswCallType(AREnum):
    """
    Denotes the mechanism by which the entry into the Bsw module shall be called.
    """

    # BswCallType method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 4.4, p.36
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on BswModuleEntry.callType
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    # Callback (i.e. the caller specifies the signature) Tags: atp.EnumerationLiteralIndex=0
    CALLBACK = "callback"

    # Callout - provide defined means to extend the functionality of an existing module. In this case caller specifies the signature. Tags: atp.EnumerationLiteralIndex=4
    CALLOUT = "callout"

    # Interrupt routine Tags: atp.EnumerationLiteralIndex=1
    INTERRUPT = "interrupt"

    # Regular API call Tags: atp.EnumerationLiteralIndex=2
    REGULAR = "regular"

    # Called by the scheduler Tags: atp.EnumerationLiteralIndex=3
    SCHEDULED = "scheduled"

    def __init__(self):
        super().__init__([BswCallType.CALLBACK, BswCallType.CALLOUT, BswCallType.INTERRUPT, BswCallType.REGULAR, BswCallType.SCHEDULED])


class BswExecutionContext(AREnum):
    """
    Specifies the execution context required or guaranteed for the call associated with this service.
    """

    # BswExecutionContext method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 4.3, p.34
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on BswModuleEntry.executionContext
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    # Context of an OS "hook" routine always Tags: atp.EnumerationLiteralIndex=0
    HOOK = "hook"

    # CAT1 interrupt context always Tags: atp.EnumerationLiteralIndex=1
    INTERRUPT_CAT_1 = "interruptCat1"

    # CAT2 interrupt context always Tags: atp.EnumerationLiteralIndex=2
    INTERRUPT_CAT_2 = "interruptCat2"

    # Task context always Tags: atp.EnumerationLiteralIndex=3
    TASK = "task"

    # The execution context is not specified by the API Tags: atp.EnumerationLiteralIndex=4
    UNSPECIFIED = "unspecified"

    def __init__(self):
        super().__init__([BswExecutionContext.HOOK, BswExecutionContext.INTERRUPT_CAT_1, BswExecutionContext.INTERRUPT_CAT_2, BswExecutionContext.TASK, BswExecutionContext.UNSPECIFIED])


class SwServiceImplPolicyEnum(AREnum):
    """
    This specifies the legal values for the implementation policies for services (in AUTOSAR: BswModule Entry-s).
    """

    # SwServiceImplPolicyEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 4.5, p.36
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on BswModuleEntry.swServiceImplPolicy
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    # inline service definition. Tags: atp.EnumerationLiteralIndex=0
    INLINE = "inline"

    # The service (in AUTOSAR: BswModuleEntry) is implemented in a way that it either resolves to an inline function or to a standard function depending on conditions set at a later point in time. The following two values are standardized (to be used for code sections only and exclusively to each other): • INLINE - The code section is declared with the keyword "inline". • LOCAL_INLINE - The code section is declared with the keyword "static inline". In both cases (INLINE and LOCAL_INLINE) the inline expansion depends on the compiler. Depending on this, the code section either corresponds to an actual section in memory or is put into the section of the caller. Tags: atp.EnumerationLiteralIndex=1
    INLINE_CONDITIONAL = "inlineConditional"

    # macro service definition. Tags: atp.EnumerationLiteralIndex=2
    MACRO = "macro"

    # Standard service and default value, if nothing is defined. Tags: atp.EnumerationLiteralIndex=3
    STANDARD = "standard"

    def __init__(self):
        super().__init__([SwServiceImplPolicyEnum.INLINE, SwServiceImplPolicyEnum.INLINE_CONDITIONAL, SwServiceImplPolicyEnum.MACRO, SwServiceImplPolicyEnum.STANDARD])


class BswModuleDependency(Identifiable, VariationPointCapable):
    """
    Represents a dependency relationship between BSW modules.
    This class defines how one BSW module depends on services from another module.
    """

    # BswModuleDependency method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getTargetModuleId            [x] impl  [x] docstring  [x] test
    # [x] setTargetModuleId            [x] impl  [x] docstring  [x] test
    # [x] getTargetModuleRef           [x] impl  [x] docstring  [x] test
    # [x] setTargetModuleRef           [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the BSW module dependency with a parent and short name.

        Args:
            parent: The parent ARObject that contains this dependency
            short_name: The unique short name of this dependency
        """
        super().__init__(parent, short_name)

        # AUTOSAR identifier of the target module; optional as target may be
        # identified by targetModuleRef instead.
        self.targetModuleId: Optional[PositiveInteger] = None
        # Reference to the target module; identifies target without needing
        # its description.
        self.targetModuleRef: Optional[RefType] = None

    def getTargetModuleId(self) -> Optional[PositiveInteger]:
        """
        Gets the AUTOSAR identifier of the target module.

        Returns:
            Positive integer representing the target module ID, or None
        """
        return self.targetModuleId

    def setTargetModuleId(self, value: Optional[PositiveInteger]) -> "BswModuleDependency":
        """
        Sets the AUTOSAR identifier of the target module.
        Only sets the value if it is not None.

        Args:
            value: The target module ID to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.targetModuleId = value
        return self

    def getTargetModuleRef(self) -> Optional[RefType]:
        """
        Gets the reference to the target module.

        Returns:
            RefType to the target module, or None
        """
        return self.targetModuleRef

    def setTargetModuleRef(self, value: Optional[RefType]) -> "BswModuleDependency":
        """
        Sets the reference to the target module.
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
    This class represents a single API entry (C-function prototype) into the BSW module or cluster. The name of the C-function is equal to the short name of this element with one exception: In case of multiple instances of a module on the same CPU, special rules for "infixes" apply, see description of class BswImplementation.
    """

    # BswModuleEntry method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 4.1, p.33
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] createArgument               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getArguments                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setBswEntryKind              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getBswEntryKind              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setCallType                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getCallType                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setExecutionContext          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getExecutionContext          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setFunctionPrototypeEmitter  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getFunctionPrototypeEmitter  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setIsReentrant               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getIsReentrant               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setIsSynchronous             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getIsSynchronous             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createReturnType             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getReturnType                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRole                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRole                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setServiceId                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getServiceId                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSwServiceImplPolicy        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSwServiceImplPolicy        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # An argument belonging to this BswModuleEntry.
        self.arguments: List[SwServiceArg] = []

        # This describes whether the entry is concrete or abstract. If the attribute is missing the entry is considered as concrete.
        self.bswEntryKind: Optional[BswEntryKindEnum] = None

        # The type of call associated with this service.
        self.callType: Optional[BswCallType] = None

        # Specifies the execution context which is required (in case of entries into this module) or guaranteed (in case of entries called from this module) for this service.
        self.executionContext: Optional[BswExecutionContext] = None

        # This attribute is used to control the generation of function prototypes. If set to "RTE", the RTE generates the function prototypes in the Module Interlink Header File.
        self.functionPrototypeEmitter: Optional[NameToken] = None

        # Reentrancy from the viewpoint of function callers: • true: Enables the service to be invoked again, before the service has finished. • false: It is prohibited to invoke the service again before is has finished.
        self.isReentrant: Optional[Boolean] = None

        # Synchronicity from the viewpoint of function callers: • true: This calls a synchronous service, i.e. the service is completed when the call returns. • false: The service (on semantical level) may not be complete when the call returns.
        self.isSynchronous: Optional[Boolean] = None

        # The return type belonging to this bswModuleEntry.
        self.returnType: Optional[SwServiceArg] = None

        # Specifies the role of the entry in the given context. It shall be equal to the standardized name of the service call, especially in cases where no ServiceIdentifier is specified, e.g. for callbacks. Note that the ShortName is not always sufficient because it maybe vendor specific (e.g. for callbacks which can have more than one instance).
        self.role: Optional[Identifier] = None

        # Refers to the service identifier of the Standardized Interfaces of AUTOSAR basic software. For non-standardized interfaces, it can optionally be used for proprietary identification.
        self.serviceId: Optional[PositiveInteger] = None

        # Denotes the implementation policy as a standard function call, inline function or macro. This has to be specified on interface level because it determines the signature of the call.
        self.swServiceImplPolicy: Optional[SwServiceImplPolicyEnum] = None

    def getArguments(self) -> List[SwServiceArg]:
        """
        An argument belonging to this BswModuleEntry.
        """
        return self.arguments

    def createArgument(self, short_name: str) -> SwServiceArg:
        """
        An argument belonging to this BswModuleEntry.

        Args:
            short_name: The short name for the new argument

        Returns:
            The created SwServiceArg instance
        """
        if not self.IsElementExists(short_name, SwServiceArg):
            arg = SwServiceArg(self, short_name)
            self.addElement(arg)
            self.arguments.append(arg)
        return self.getElement(short_name, SwServiceArg)

    def getBswEntryKind(self) -> Optional[BswEntryKindEnum]:
        """
        This describes whether the entry is concrete or abstract. If the attribute is missing the entry is considered as concrete.
        """
        return self.bswEntryKind

    def setBswEntryKind(self, value: Optional[BswEntryKindEnum]) -> "BswModuleEntry":
        """
        This describes whether the entry is concrete or abstract. If the attribute is missing the entry is considered as concrete.
        A None value is a no-op and does not overwrite an existing bswEntryKind.
        """
        if value is not None:
            self.bswEntryKind = value
        return self

    def getCallType(self) -> Optional[BswCallType]:
        """
        The type of call associated with this service.
        """
        return self.callType

    def setCallType(self, value: Optional[BswCallType]) -> "BswModuleEntry":
        """
        The type of call associated with this service.
        A None value is a no-op and does not overwrite an existing callType.
        """
        if value is not None:
            self.callType = value
        return self

    def getExecutionContext(self) -> Optional[BswExecutionContext]:
        """
        Specifies the execution context which is required (in case of entries into this module) or guaranteed (in case of entries called from this module) for this service.
        """
        return self.executionContext

    def setExecutionContext(self, value: Optional[BswExecutionContext]) -> "BswModuleEntry":
        """
        Specifies the execution context which is required (in case of entries into this module) or guaranteed (in case of entries called from this module) for this service.
        A None value is a no-op and does not overwrite an existing executionContext.
        """
        if value is not None:
            self.executionContext = value
        return self

    def getFunctionPrototypeEmitter(self) -> Optional[NameToken]:
        """
        This attribute is used to control the generation of function prototypes. If set to "RTE", the RTE generates the function prototypes in the Module Interlink Header File.
        """
        return self.functionPrototypeEmitter

    def setFunctionPrototypeEmitter(self, value: Optional[NameToken]) -> "BswModuleEntry":
        """
        This attribute is used to control the generation of function prototypes. If set to "RTE", the RTE generates the function prototypes in the Module Interlink Header File.
        A None value is a no-op and does not overwrite an existing functionPrototypeEmitter.
        """
        if value is not None:
            self.functionPrototypeEmitter = value
        return self

    def getIsReentrant(self) -> Optional[Boolean]:
        """
        Reentrancy from the viewpoint of function callers: • true: Enables the service to be invoked again, before the service has finished. • false: It is prohibited to invoke the service again before is has finished.
        """
        return self.isReentrant

    def setIsReentrant(self, value: Optional[Boolean]) -> "BswModuleEntry":
        """
        Reentrancy from the viewpoint of function callers: • true: Enables the service to be invoked again, before the service has finished. • false: It is prohibited to invoke the service again before is has finished.
        A None value is a no-op and does not overwrite an existing isReentrant.
        """
        if value is not None:
            self.isReentrant = value
        return self

    def getIsSynchronous(self) -> Optional[Boolean]:
        """
        Synchronicity from the viewpoint of function callers: • true: This calls a synchronous service, i.e. the service is completed when the call returns. • false: The service (on semantical level) may not be complete when the call returns.
        """
        return self.isSynchronous

    def setIsSynchronous(self, value: Optional[Boolean]) -> "BswModuleEntry":
        """
        Synchronicity from the viewpoint of function callers: • true: This calls a synchronous service, i.e. the service is completed when the call returns. • false: The service (on semantical level) may not be complete when the call returns.
        A None value is a no-op and does not overwrite an existing isSynchronous.
        """
        if value is not None:
            self.isSynchronous = value
        return self

    def getReturnType(self) -> Optional[SwServiceArg]:
        """
        The return type belonging to this bswModuleEntry.
        """
        return self.returnType

    def createReturnType(self, short_name: str) -> SwServiceArg:
        """
        The return type belonging to this bswModuleEntry.

        Args:
            short_name: The short name for the new return type

        Returns:
            The created SwServiceArg instance
        """
        if not self.IsElementExists(short_name, SwServiceArg):
            arg = SwServiceArg(self, short_name)
            self.addElement(arg)
            self.returnType = arg
        return self.getElement(short_name, SwServiceArg)

    def getRole(self) -> Optional[Identifier]:
        """
        Specifies the role of the entry in the given context. It shall be equal to the standardized name of the service call, especially in cases where no ServiceIdentifier is specified, e.g. for callbacks. Note that the ShortName is not always sufficient because it maybe vendor specific (e.g. for callbacks which can have more than one instance).
        """
        return self.role

    def setRole(self, value: Optional[Identifier]) -> "BswModuleEntry":
        """
        Specifies the role of the entry in the given context. It shall be equal to the standardized name of the service call, especially in cases where no ServiceIdentifier is specified, e.g. for callbacks. Note that the ShortName is not always sufficient because it maybe vendor specific (e.g. for callbacks which can have more than one instance).
        A None value is a no-op and does not overwrite an existing role.
        """
        if value is not None:
            self.role = value
        return self

    def getServiceId(self) -> Optional[PositiveInteger]:
        """
        Refers to the service identifier of the Standardized Interfaces of AUTOSAR basic software. For non-standardized interfaces, it can optionally be used for proprietary identification.
        """
        return self.serviceId

    def setServiceId(self, value: Optional[PositiveInteger]) -> "BswModuleEntry":
        """
        Refers to the service identifier of the Standardized Interfaces of AUTOSAR basic software. For non-standardized interfaces, it can optionally be used for proprietary identification.
        A None value is a no-op and does not overwrite an existing serviceId.
        """
        if value is not None:
            self.serviceId = value
        return self

    def getSwServiceImplPolicy(self) -> Optional[SwServiceImplPolicyEnum]:
        """
        Denotes the implementation policy as a standard function call, inline function or macro. This has to be specified on interface level because it determines the signature of the call.
        """
        return self.swServiceImplPolicy

    def setSwServiceImplPolicy(self, value: Optional[SwServiceImplPolicyEnum]) -> "BswModuleEntry":
        """
        Denotes the implementation policy as a standard function call, inline function or macro. This has to be specified on interface level because it determines the signature of the call.
        A None value is a no-op and does not overwrite an existing swServiceImplPolicy.
        """
        if value is not None:
            self.swServiceImplPolicy = value
        return self

    def __str__(self) -> str:
        return "BswModuleEntry(%s)" % self.short_name


class BswModuleClientServerEntry(Referrable, VariationPointCapable):
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


class BswEntryRelationshipEnum(AREnum):
    """
    Enumeration for BSW entry relationship types.
    Defines the type of relationship between two BswModuleEntrys.
    """

    # BswEntryRelationshipEnum method parity checklist:
    # (no methods)

    # Describes that the BswModuleEntry referenced as "to" needs to have
    # the same signature as the "abstract" BswModuleEntry referenced as
    # "from". Tags: atp.EnumerationLiteralIndex=0
    DERIVED_FROM = "derivedFrom"


class BswEntryRelationship(ARObject):
    """
    Describes a relationship between two BswModuleEntrys and the
    type of relationship.
    """

    # BswEntryRelationship method parity checklist:
    # [x] __init__                          [x] impl  [x] docstring  [ ] test
    # [x] getBswEntryRelationshipType       [x] impl  [x] docstring  [ ] test
    # [x] setBswEntryRelationshipType       [x] impl  [x] docstring  [ ] test
    # [x] getFromRef                        [x] impl  [x] docstring  [ ] test
    # [x] setFromRef                        [x] impl  [x] docstring  [ ] test
    # [x] getToRef                          [x] impl  [x] docstring  [ ] test
    # [x] setToRef                          [x] impl  [x] docstring  [ ] test

    def __init__(self):
        """
        Initializes the BswEntryRelationship with default values.
        """
        super().__init__()

        # Denotes the type of the relationship.
        self.bswEntryRelationshipType: Optional[BswEntryRelationshipEnum] = None

        # Type of relationship that refers to the abstract BswModuleEntry.
        # Please notice that in this case the bswEntryRelationshipType
        # shall be set to drivenFrom.
        self.fromRef: Optional[RefType] = None

        # Type of relationship that refers to the concrete BswModuleEntry.
        self.toRef: Optional[RefType] = None

    def getBswEntryRelationshipType(self) -> Optional[BswEntryRelationshipEnum]:
        """
        Gets the type of relationship between BSW entries. Denotes the
        type of the relationship.
        """
        return self.bswEntryRelationshipType

    def setBswEntryRelationshipType(self, value: Optional[BswEntryRelationshipEnum]) -> "BswEntryRelationship":
        """
        Sets the type of relationship between BSW entries. Only sets if
        value is not None. Returns self for method chaining.
        """
        if value is not None:
            self.bswEntryRelationshipType = value
        return self

    def getFromRef(self) -> Optional[RefType]:
        """
        Gets the reference to the abstract BswModuleEntry that is the
        source of the relationship. When this reference is present, the
        bswEntryRelationshipType shall be set to drivenFrom.
        """
        return self.fromRef

    def setFromRef(self, value: Optional[RefType]) -> "BswEntryRelationship":
        """
        Sets the reference to the abstract BswModuleEntry that is the
        source of the relationship. Only sets if value is not None.
        Returns self for method chaining.
        """
        if value is not None:
            self.fromRef = value
        return self

    def getToRef(self) -> Optional[RefType]:
        """
        Gets the reference to the concrete BswModuleEntry that is the
        target of the relationship.
        """
        return self.toRef

    def setToRef(self, value: Optional[RefType]) -> "BswEntryRelationship":
        """
        Sets the reference to the concrete BswModuleEntry that is the
        target of the relationship. Only sets if value is not None.
        Returns self for method chaining.
        """
        if value is not None:
            self.toRef = value
        return self


class BswEntryRelationshipSet(Identifiable):
    """
    Describes a set of relationships between two BswModuleEntrys.
    Tags: atp.recommendedPackage=BswEntryRelationshipSets
    """

    # BswEntryRelationshipSet method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [ ] test
    # [x] getBswEntryRelationships     [x] impl  [x] docstring  [ ] test
    # [x] addBswEntryRelationship      [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the BswEntryRelationshipSet with a parent and
        short name.

        Args:
            parent: The parent ARObject that contains this relationship set
            short_name: The unique short name of this relationship set
        """
        super().__init__(parent, short_name)

        # Relationship between two BswModuleEntrys.
        self.bswEntryRelationships: List[BswEntryRelationship] = []

    def getBswEntryRelationships(self) -> List[BswEntryRelationship]:
        """
        Gets the list of relationships between BSW entries.

        Returns:
            List of BswEntryRelationship instances
        """
        return self.bswEntryRelationships

    def addBswEntryRelationship(self, value: BswEntryRelationship) -> "BswEntryRelationshipSet":
        """
        Adds a relationship between BSW entries. Only adds if value is
        not None. Returns self for method chaining.

        Args:
            value: The BswEntryRelationship instance to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.bswEntryRelationships.append(value)
        return self
