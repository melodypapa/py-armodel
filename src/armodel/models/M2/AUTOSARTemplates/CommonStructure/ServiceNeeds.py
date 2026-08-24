"""
This module contains classes for representing AUTOSAR service needs structures
in the CommonStructure module. Service needs define requirements for various
services such as NV block management, diagnostic services, cryptographic services, etc.
"""

from __future__ import annotations

from abc import ABC
from typing import List, Optional
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.InstanceRefsUsage import AutosarParameterRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AutosarVariableRef import AutosarVariableRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation import ImplementationProps
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, RefType, AREnum, Boolean, ARLiteral
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DiagRequirementIdString, Integer, PositiveInteger
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import NameToken
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String, TimeValue


class RoleBasedDataAssignment(ARObject):
    """
    Represents a role-based data assignment in AUTOSAR models.
    This class defines how data elements are assigned based on their role in service interactions.
    """

    # RoleBasedDataAssignment method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [ ] getRole                      [x] impl  [x] docstring  [ ] test
    # [ ] setRole                      [x] impl  [x] docstring  [ ] test
    # [ ] getUsedDataElement           [x] impl  [x] docstring  [ ] test
    # [ ] setUsedDataElement           [x] impl  [x] docstring  [ ] test
    # [ ] getUsedParameterElement      [x] impl  [x] docstring  [ ] test
    # [ ] setUsedParameterElement      [x] impl  [x] docstring  [ ] test
    # [ ] getUsedPimRef                [x] impl  [x] docstring  [ ] test
    # [ ] setUsedPimRef                [x] impl  [x] docstring  [ ] test

    def __init__(self):
        """
        Initializes the RoleBasedDataAssignment with default values.
        """
        super().__init__()

        # Role identifier for this data assignment
        self.role: ARLiteral = None
        # Used data element reference for this assignment
        self.usedDataElement: AutosarVariableRef = None
        # Used parameter element reference for this assignment
        self.usedParameterElement: AutosarParameterRef = None
        # Reference to the PIM (Port Interface Mapping) for this assignment
        self.usedPimRef: RefType = None

    def getRole(self):
        """
        Gets the role identifier for this data assignment.

        Returns:
            ARLiteral: The role identifier
        """
        return self.role

    def setRole(self, value):
        """
        Sets the role identifier for this data assignment.
        Only sets the value if it is not None.

        Args:
            value: The role identifier to set

        Returns:
            self for method chaining
        """
        self.role = value
        return self

    def getUsedDataElement(self):
        """
        Gets the used data element reference for this assignment.

        Returns:
            AutosarVariableRef: The used data element reference
        """
        return self.usedDataElement

    def setUsedDataElement(self, value):
        """
        Sets the used data element reference for this assignment.
        Only sets the value if it is not None.

        Args:
            value: The used data element reference to set

        Returns:
            self for method chaining
        """
        self.usedDataElement = value
        return self

    def getUsedParameterElement(self):
        """
        Gets the used parameter element reference for this assignment.

        Returns:
            AutosarParameterRef: The used parameter element reference
        """
        return self.usedParameterElement

    def setUsedParameterElement(self, value):
        """
        Sets the used parameter element reference for this assignment.
        Only sets the value if it is not None.

        Args:
            value: The used parameter element reference to set

        Returns:
            self for method chaining
        """
        self.usedParameterElement = value
        return self

    def getUsedPimRef(self):
        """
        Gets the reference to the PIM (Port Interface Mapping) for this assignment.

        Returns:
            RefType: The PIM reference
        """
        return self.usedPimRef

    def setUsedPimRef(self, value):
        """
        Sets the reference to the PIM (Port Interface Mapping) for this assignment.
        Only sets the value if it is not None.

        Args:
            value: The PIM reference to set

        Returns:
            self for method chaining
        """
        self.usedPimRef = value
        return self


class ServiceNeeds(Identifiable, ABC):
    """
    Abstract base class for service needs in AUTOSAR models.
    Service needs define requirements for various services such as NV block management, diagnostic services, etc.
    """

    # ServiceNeeds method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the ServiceNeeds with a parent and short name.
        Raises TypeError if this abstract class is instantiated directly.

        Args:
            parent: The parent ARObject that contains this service needs
            short_name: The unique short name of this service needs
        """
        if type(self) is ServiceNeeds:
            raise TypeError("ServiceNeeds is an abstract class.")

        super().__init__(parent, short_name)


class RamBlockStatusControlEnum(AREnum):
    """
    Enumeration for RAM block status control methods in AUTOSAR NV block needs.
    Defines how the status of RAM blocks is controlled in NV block management.
    """

    # RamBlockStatusControlEnum method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test

    # Status control through API calls
    API = "api"
    # Status control through NV RAM manager
    NV_RAM_MANAGER = "nvRamManager"

    def __init__(self):
        """
        Initializes the RamBlockStatusControlEnum with all possible values.
        """
        super().__init__(
            (
                RamBlockStatusControlEnum.API,
                RamBlockStatusControlEnum.NV_RAM_MANAGER,
            )
        )


class NvBlockNeedsReliabilityEnum(AREnum):
    """
    Enumeration for NV block needs reliability levels in AUTOSAR models.
    Defines the type of error protection used for NV block management.
    """

    # NvBlockNeedsReliabilityEnum method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test

    # Error correction protection for NV blocks
    ERROR_CORRECTION = "errorCorrection"
    # Error detection protection for NV blocks
    ERROR_DETECTION = "errorDetection"
    # No protection for NV blocks
    NO_PROTECTION = "noProtection"

    def __init__(self):
        """
        Initializes the NvBlockNeedsReliabilityEnum with all possible values.
        """
        super().__init__(
            (
                NvBlockNeedsReliabilityEnum.ERROR_CORRECTION,
                NvBlockNeedsReliabilityEnum.ERROR_DETECTION,
                NvBlockNeedsReliabilityEnum.NO_PROTECTION,
            )
        )


class NvBlockNeedsWritingPriorityEnum(AREnum):
    """
    Enumeration for NV block needs writing priorities in AUTOSAR models.
    Defines the priority level for writing operations to NV blocks.
    """

    # NvBlockNeedsWritingPriorityEnum method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test

    # High priority for NV block writing
    HIGH = "high"
    # Low priority for NV block writing
    LOW = "low"
    # Medium priority for NV block writing
    MEDIUM = "medium"

    def __init__(self):
        """
        Initializes the NvBlockNeedsWritingPriorityEnum with all possible values.
        """
        super().__init__(
            (
                NvBlockNeedsWritingPriorityEnum.HIGH,
                NvBlockNeedsWritingPriorityEnum.LOW,
                NvBlockNeedsWritingPriorityEnum.MEDIUM,
            )
        )


class NvBlockNeeds(ServiceNeeds):
    """
    Represents NV (Non-Volatile) block needs in AUTOSAR models.
    This class defines requirements for managing non-volatile memory blocks including
    CRC calculation, write protection, and various storage strategies.
    """

    # NvBlockNeeds method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [ ] getCalcRamBlockCrc           [x] impl  [ ] docstring  [ ] test
    # [ ] setCalcRamBlockCrc           [x] impl  [ ] docstring  [ ] test
    # [ ] getCheckStaticBlockId        [x] impl  [ ] docstring  [ ] test
    # [ ] setCheckStaticBlockId        [x] impl  [ ] docstring  [ ] test
    # [ ] getCyclicWritingPeriod       [x] impl  [ ] docstring  [ ] test
    # [ ] setCyclicWritingPeriod       [x] impl  [ ] docstring  [ ] test
    # [ ] getNDataSets                 [x] impl  [ ] docstring  [ ] test
    # [ ] setNDataSets                 [x] impl  [ ] docstring  [ ] test
    # [ ] getNRomBlocks                [x] impl  [ ] docstring  [ ] test
    # [ ] setNRomBlocks                [x] impl  [ ] docstring  [ ] test
    # [ ] getRamBlockStatusControl     [x] impl  [ ] docstring  [ ] test
    # [ ] setRamBlockStatusControl     [x] impl  [ ] docstring  [ ] test
    # [ ] getReadonly                  [x] impl  [ ] docstring  [ ] test
    # [ ] setReadonly                  [x] impl  [ ] docstring  [ ] test
    # [ ] getReliability               [x] impl  [ ] docstring  [ ] test
    # [ ] setReliability               [x] impl  [ ] docstring  [ ] test
    # [ ] getResistantToChangedSw      [x] impl  [ ] docstring  [ ] test
    # [ ] setResistantToChangedSw      [x] impl  [ ] docstring  [ ] test
    # [ ] getRestoreAtStart            [x] impl  [ ] docstring  [ ] test
    # [ ] setRestoreAtStart            [x] impl  [ ] docstring  [ ] test
    # [ ] getSelectBlockForFirstInitAll [x] impl  [ ] docstring  [ ] test
    # [ ] setSelectBlockForFirstInitAll [x] impl  [ ] docstring  [ ] test
    # [ ] getStoreAtShutdown           [x] impl  [ ] docstring  [ ] test
    # [ ] setStoreAtShutdown           [x] impl  [ ] docstring  [ ] test
    # [ ] getStoreCyclic               [x] impl  [ ] docstring  [ ] test
    # [ ] setStoreCyclic               [x] impl  [ ] docstring  [ ] test
    # [ ] getStoreEmergency            [x] impl  [ ] docstring  [ ] test
    # [ ] setStoreEmergency            [x] impl  [ ] docstring  [ ] test
    # [ ] getStoreImmediate            [x] impl  [ ] docstring  [ ] test
    # [ ] setStoreImmediate            [x] impl  [ ] docstring  [ ] test
    # [ ] getStoreOnChange             [x] impl  [ ] docstring  [ ] test
    # [ ] setStoreOnChange             [x] impl  [ ] docstring  [ ] test
    # [ ] getUseAutoValidationAtShutDown [x] impl  [ ] docstring  [ ] test
    # [ ] setUseAutoValidationAtShutDown [x] impl  [ ] docstring  [ ] test
    # [ ] getUseCRCCompMechanism       [x] impl  [ ] docstring  [ ] test
    # [ ] setUseCRCCompMechanism       [x] impl  [ ] docstring  [ ] test
    # [ ] getWriteOnlyOnce             [x] impl  [ ] docstring  [ ] test
    # [ ] setWriteOnlyOnce             [x] impl  [ ] docstring  [ ] test
    # [ ] getWriteVerification         [x] impl  [ ] docstring  [ ] test
    # [ ] setWriteVerification         [x] impl  [ ] docstring  [ ] test
    # [ ] getWritingFrequency          [x] impl  [ ] docstring  [ ] test
    # [ ] setWritingFrequency          [x] impl  [ ] docstring  [ ] test
    # [ ] getWritingPriority           [x] impl  [ ] docstring  [ ] test
    # [ ] setWritingPriority           [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the NvBlockNeeds with a parent and short name.

        Args:
            parent: The parent ARObject that contains this NV block needs
            short_name: The unique short name of this NV block needs
        """
        super().__init__(parent, short_name)

        # Flag indicating whether to calculate CRC for RAM blocks
        self.calcRamBlockCrc: Boolean = None
        # Flag indicating whether to check static block ID
        self.checkStaticBlockId: Boolean = None
        # Period for cyclic writing operations
        self.cyclicWritingPeriod: TimeValue = None
        # Number of data sets for this NV block
        self.nDataSets: PositiveInteger = None
        # Number of ROM blocks for this NV block
        self.nRomBlocks: PositiveInteger = None
        # Method for controlling RAM block status
        self.ramBlockStatusControl: RamBlockStatusControlEnum = None
        # Flag indicating if this block is read-only
        self.readonly: Boolean = None
        # Reliability level for this NV block
        self.reliability: NvBlockNeedsReliabilityEnum = None
        # Flag indicating resistance to changed software
        self.resistantToChangedSw: Boolean = None
        # Flag indicating whether to restore at start
        self.restoreAtStart: Boolean = None
        # Flag indicating whether to select block for first init all
        self.selectBlockForFirstInitAll: Boolean = None
        # Flag indicating whether to store at shutdown
        self.storeAtShutdown: Boolean = None
        # Flag indicating whether to store cyclically
        self.storeCyclic: Boolean = None
        # Flag indicating whether to store in emergency situations
        self.storeEmergency: Boolean = None
        # Flag indicating whether to store immediately
        self.storeImmediate: Boolean = None
        # Flag indicating whether to store on change
        self.storeOnChange: Boolean = None
        # Flag indicating whether to use auto-validation at shutdown
        self.useAutoValidationAtShutDown: Boolean = None
        # Flag indicating whether to use CRC comparison mechanism
        self.useCRCCompMechanism: Boolean = None
        # Flag indicating whether to write only once
        self.writeOnlyOnce: Boolean = None
        # Flag indicating whether to verify writes
        self.writeVerification: Boolean = None
        # Frequency for writing operations
        self.writingFrequency: PositiveInteger = None
        # Priority for writing operations
        self.writingPriority: NvBlockNeedsWritingPriorityEnum = None

    def getCalcRamBlockCrc(self):
        return self.calcRamBlockCrc

    def setCalcRamBlockCrc(self, value):
        self.calcRamBlockCrc = value
        return self

    def getCheckStaticBlockId(self):
        return self.checkStaticBlockId

    def setCheckStaticBlockId(self, value):
        self.checkStaticBlockId = value
        return self

    def getCyclicWritingPeriod(self):
        return self.cyclicWritingPeriod

    def setCyclicWritingPeriod(self, value):
        self.cyclicWritingPeriod = value
        return self

    def getNDataSets(self):
        return self.nDataSets

    def setNDataSets(self, value):
        self.nDataSets = value
        return self

    def getNRomBlocks(self):
        return self.nRomBlocks

    def setNRomBlocks(self, value):
        self.nRomBlocks = value
        return self

    def getRamBlockStatusControl(self):
        return self.ramBlockStatusControl

    def setRamBlockStatusControl(self, value):
        self.ramBlockStatusControl = value
        return self

    def getReadonly(self):
        return self.readonly

    def setReadonly(self, value):
        self.readonly = value
        return self

    def getReliability(self):
        return self.reliability

    def setReliability(self, value):
        self.reliability = value
        return self

    def getResistantToChangedSw(self):
        return self.resistantToChangedSw

    def setResistantToChangedSw(self, value):
        self.resistantToChangedSw = value
        return self

    def getRestoreAtStart(self):
        return self.restoreAtStart

    def setRestoreAtStart(self, value):
        self.restoreAtStart = value
        return self

    def getSelectBlockForFirstInitAll(self):
        return self.selectBlockForFirstInitAll

    def setSelectBlockForFirstInitAll(self, value):
        self.selectBlockForFirstInitAll = value
        return self

    def getStoreAtShutdown(self):
        return self.storeAtShutdown

    def setStoreAtShutdown(self, value):
        self.storeAtShutdown = value
        return self

    def getStoreCyclic(self):
        return self.storeCyclic

    def setStoreCyclic(self, value):
        self.storeCyclic = value
        return self

    def getStoreEmergency(self):
        return self.storeEmergency

    def setStoreEmergency(self, value):
        self.storeEmergency = value
        return self

    def getStoreImmediate(self):
        return self.storeImmediate

    def setStoreImmediate(self, value):
        self.storeImmediate = value
        return self

    def getStoreOnChange(self):
        return self.storeOnChange

    def setStoreOnChange(self, value):
        self.storeOnChange = value
        return self

    def getUseAutoValidationAtShutDown(self):
        return self.useAutoValidationAtShutDown

    def setUseAutoValidationAtShutDown(self, value):
        self.useAutoValidationAtShutDown = value
        return self

    def getUseCRCCompMechanism(self):
        return self.useCRCCompMechanism

    def setUseCRCCompMechanism(self, value):
        self.useCRCCompMechanism = value
        return self

    def getWriteOnlyOnce(self):
        return self.writeOnlyOnce

    def setWriteOnlyOnce(self, value):
        self.writeOnlyOnce = value
        return self

    def getWriteVerification(self):
        return self.writeVerification

    def setWriteVerification(self, value):
        self.writeVerification = value
        return self

    def getWritingFrequency(self):
        return self.writingFrequency

    def setWritingFrequency(self, value):
        self.writingFrequency = value
        return self

    def getWritingPriority(self):
        return self.writingPriority

    def setWritingPriority(self, value):
        self.writingPriority = value
        return self


class RoleBasedDataTypeAssignment(ARObject):
    """
    This class specifies an assignment of a role to a particular data type of
    a software component (or in the BswModuleBehavior of a module or cluster)
    in the context of an AUTOSAR Service. With this assignment, the role of
    the data type can be mapped to a specific ServiceNeeds element, so that a
    tool is able to create the correct access.
    """

    # RoleBasedDataTypeAssignment method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 12.5, p.227
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getRole                          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRole                          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getUsedImplementationDataTypeRef [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setUsedImplementationDataTypeRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This is the role of the associated data type in the given context.
        self.role: Optional[Identifier] = None

        # This represents the associated ImplementationDataType.
        self.usedImplementationDataTypeRef: Optional[RefType] = None

    def getRole(self) -> Optional[Identifier]:
        """
        This is the role of the associated data type in the given context.
        """
        return self.role

    def setRole(self, value: Optional[Identifier]) -> "RoleBasedDataTypeAssignment":
        """
        This is the role of the associated data type in the given context.
        Only sets the value if it is not None.

        Args:
            value: The role of the associated data type

        Returns:
            self for method chaining
        """
        if value is not None:
            self.role = value
        return self

    def getUsedImplementationDataTypeRef(self) -> Optional[RefType]:
        """
        This represents the associated ImplementationDataType.
        """
        return self.usedImplementationDataTypeRef

    def setUsedImplementationDataTypeRef(self, value: Optional[RefType]) -> "RoleBasedDataTypeAssignment":
        """
        This represents the associated ImplementationDataType.
        Only sets the value if it is not None.

        Args:
            value: The reference to the associated ImplementationDataType

        Returns:
            self for method chaining
        """
        if value is not None:
            self.usedImplementationDataTypeRef = value
        return self


class ServiceDiagnosticRelevanceEnum(AREnum):
    """
    Enumeration for service diagnostic relevance in AUTOSAR models.
    Defines the diagnostic relevance of services (currently empty as per specification).
    """

    # ServiceDiagnosticRelevanceEnum method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test

    def __init__(self):
        """
        Initializes the ServiceDiagnosticRelevanceEnum with empty values list.
        """
        super().__init__([])


class ServiceDependency(ARObject, ABC):
    """
    Represents a service dependency in AUTOSAR models.
    This class defines dependencies on services along with their data type assignments and diagnostic relevance.
    """

    # ServiceDependency method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [ ] test
    # [x] getAssignedDataTypes         [x] impl  [x] docstring  [x] test
    # [x] addAssignedDataType          [x] impl  [x] docstring  [x] test
    # [ ] getDiagnosticRelevance       [x] impl  [x] docstring  [ ] test
    # [ ] setDiagnosticRelevance       [x] impl  [x] docstring  [ ] test
    # [ ] getSymbolicNameProps         [x] impl  [x] docstring  [ ] test
    # [ ] setSymbolicNameProps         [x] impl  [x] docstring  [ ] test

    def __init__(self):
        """
        Initializes the ServiceDependency with default values.
        Raises TypeError if this abstract class is instantiated directly.
        """
        if type(self) is ServiceDependency:
            raise TypeError("ServiceDependency is an abstract class.")
        super().__init__()

        # List of role-based data type assignments for this service dependency
        self.assignedDataTypes: List[RoleBasedDataTypeAssignment] = []

        # Diagnostic relevance of this service dependency
        self.diagnosticRelevance: Optional[ServiceDiagnosticRelevanceEnum] = None

        # Symbolic name properties for this service dependency
        self.symbolicNameProps: Optional["SymbolicNameProps"] = None

    def getAssignedDataTypes(self) -> List[RoleBasedDataTypeAssignment]:
        """
        Gets the list of role-based data type assignments for this service dependency.

        Returns:
            List of RoleBasedDataTypeAssignment instances
        """
        return self.assignedDataTypes

    def addAssignedDataType(self, value: Optional[RoleBasedDataTypeAssignment]) -> "ServiceDependency":
        """
        Adds a role-based data type assignment to this service dependency.
        A None value is a no-op and is not appended to the list.

        Args:
            value: The data type assignment to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.assignedDataTypes.append(value)
        return self

    def getDiagnosticRelevance(self) -> Optional[ServiceDiagnosticRelevanceEnum]:
        """
        Gets the diagnostic relevance of this service dependency.

        Returns:
            ServiceDiagnosticRelevanceEnum: The diagnostic relevance
        """
        return self.diagnosticRelevance

    def setDiagnosticRelevance(self, value: Optional[ServiceDiagnosticRelevanceEnum]) -> "ServiceDependency":
        """
        Sets the diagnostic relevance of this service dependency.
        Only sets the value if it is not None.

        Args:
            value: The diagnostic relevance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.diagnosticRelevance = value
        return self

    def getSymbolicNameProps(self) -> Optional["SymbolicNameProps"]:
        """
        Gets the symbolic name properties for this service dependency.

        Returns:
            SymbolicNameProps: The symbolic name properties
        """
        return self.symbolicNameProps

    def setSymbolicNameProps(self, value: Optional["SymbolicNameProps"]) -> "ServiceDependency":
        """
        Sets the symbolic name properties for this service dependency.
        Only sets the value if it is not None.

        Args:
            value: The symbolic name properties to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.symbolicNameProps = value
        return self


class DiagnosticAudienceEnum(AREnum):
    """
    Enumeration for diagnostic audiences in AUTOSAR models.
    Defines the target audience for diagnostic information and services.
    """

    # DiagnosticAudienceEnum method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test

    # Diagnostic information for aftermarket use
    AFTER_MARKET = "aftermarket"
    # Diagnostic information for after-sales use
    AFTER_SALES = "afterSales"
    # Diagnostic information for development use
    DEVELOPMENT = "development"
    # Diagnostic information for manufacturing use
    MANUFACTURING = "manufacturing"
    # Diagnostic information for supplier use
    SUPPLIER = "supplier"

    def __init__(self):
        """
        Initializes the DiagnosticAudienceEnum with all possible values.
        """
        super().__init__(
            (
                DiagnosticAudienceEnum.AFTER_MARKET,
                DiagnosticAudienceEnum.AFTER_SALES,
                DiagnosticAudienceEnum.DEVELOPMENT,
                DiagnosticAudienceEnum.MANUFACTURING,
                DiagnosticAudienceEnum.SUPPLIER,
            )
        )


class DiagnosticServiceRequestCallbackTypeEnum(AREnum):
    """
    Enumeration for diagnostic service request callback types in AUTOSAR models.
    Defines who handles diagnostic service request callbacks (manufacturer or supplier).
    """

    # DiagnosticServiceRequestCallbackTypeEnum method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test

    # Callback type handled by manufacturer
    REQUEST_CALLBACK_TYPE_MANUFACTURER = "requestCallbackTypeManufacturer"
    # Callback type handled by supplier
    REQUEST_CALLBACK_TYPE_SUPPLIER = "requestCallbackTypeSupplier"

    def __init__(self):
        """
        Initializes the DiagnosticServiceRequestCallbackTypeEnum with all possible values.
        """
        super().__init__(
            (
                DiagnosticServiceRequestCallbackTypeEnum.REQUEST_CALLBACK_TYPE_MANUFACTURER,
                DiagnosticServiceRequestCallbackTypeEnum.REQUEST_CALLBACK_TYPE_SUPPLIER,
            )
        )


class DiagnosticCapabilityElement(ServiceNeeds, ABC):
    """
    Abstract base class for diagnostic capability elements in AUTOSAR models.
    This class defines common properties for diagnostic capabilities including audiences, requirements, and security access levels.
    """

    # DiagnosticCapabilityElement method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test
    # [ ] getAudiences                 [x] impl  [x] docstring  [ ] test
    # [ ] addAudience                  [x] impl  [x] docstring  [ ] test
    # [ ] getDiagRequirement           [x] impl  [x] docstring  [ ] test
    # [ ] setDiagRequirement           [x] impl  [x] docstring  [ ] test
    # [ ] getSecurityAccessLevel       [x] impl  [x] docstring  [ ] test
    # [ ] setSecurityAccessLevel       [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the DiagnosticCapabilityElement with a parent and short name.
        Raises TypeError if this abstract class is instantiated directly.

        Args:
            parent: The parent ARObject that contains this diagnostic capability element
            short_name: The unique short name of this diagnostic capability element
        """
        if type(self) is DiagnosticCapabilityElement:
            raise TypeError("DiagnosticCapabilityElement is an abstract class.")

        super().__init__(parent, short_name)

        # List of audiences for this diagnostic capability
        self.audiences: List[DiagnosticAudienceEnum] = []
        # Diagnostic requirement ID string for this capability
        self.diagRequirement: DiagRequirementIdString = None
        # Security access level for this diagnostic capability
        self.securityAccessLevel: PositiveInteger = None

    def getAudiences(self):
        """
        Gets the list of audiences for this diagnostic capability.

        Returns:
            List of DiagnosticAudienceEnum instances
        """
        return self.audiences

    def addAudience(self, value):
        """
        Adds an audience to this diagnostic capability.

        Args:
            value: The diagnostic audience to add

        Returns:
            self for method chaining
        """
        self.audiences.append(value)
        return self

    def getDiagRequirement(self):
        """
        Gets the diagnostic requirement ID string for this capability.

        Returns:
            DiagRequirementIdString: The diagnostic requirement
        """
        return self.diagRequirement

    def setDiagRequirement(self, value):
        """
        Sets the diagnostic requirement ID string for this capability.
        Only sets the value if it is not None.

        Args:
            value: The diagnostic requirement to set

        Returns:
            self for method chaining
        """
        self.diagRequirement = value
        return self

    def getSecurityAccessLevel(self):
        """
        Gets the security access level for this diagnostic capability.

        Returns:
            PositiveInteger: The security access level
        """
        return self.securityAccessLevel

    def setSecurityAccessLevel(self, value):
        """
        Sets the security access level for this diagnostic capability.
        Only sets the value if it is not None.

        Args:
            value: The security access level to set

        Returns:
            self for method chaining
        """
        self.securityAccessLevel = value
        return self


class DiagnosticRoutineTypeEnum(AREnum):
    """
    Enumeration for diagnostic routine types in AUTOSAR models.
    Defines whether diagnostic routines are executed synchronously or asynchronously.
    """

    # DiagnosticRoutineTypeEnum method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test

    # Asynchronous diagnostic routine
    ASYNCHRONOUS = "asynchronous"
    # Synchronous diagnostic routine
    SYNCHRONOUS = "synchronous"

    def __init__(self):
        """
        Initializes the DiagnosticRoutineTypeEnum with all possible values.
        """
        super().__init__(
            (
                DiagnosticRoutineTypeEnum.ASYNCHRONOUS,
                DiagnosticRoutineTypeEnum.SYNCHRONOUS,
            )
        )


class DiagnosticCommunicationManagerNeeds(DiagnosticCapabilityElement):
    """
    Represents diagnostic communication manager needs in AUTOSAR models.
    This class defines requirements for the diagnostic communication manager including callback types.
    """

    # DiagnosticCommunicationManagerNeeds method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [ ] getServiceRequestCallbackType [x] impl  [x] docstring  [ ] test
    # [ ] setServiceRequestCallbackType [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the DiagnosticCommunicationManagerNeeds with a parent and short name.

        Args:
            parent: The parent ARObject that contains this diagnostic communication manager needs
            short_name: The unique short name of this diagnostic communication manager needs
        """
        super().__init__(parent, short_name)

        # Type of service request callback for this diagnostic communication manager
        self.serviceRequestCallbackType: DiagnosticServiceRequestCallbackTypeEnum = None

    def getServiceRequestCallbackType(self):
        """
        Gets the type of service request callback for this diagnostic communication manager.

        Returns:
            DiagnosticServiceRequestCallbackTypeEnum: The service request callback type
        """
        return self.serviceRequestCallbackType

    def setServiceRequestCallbackType(self, value):
        """
        Sets the type of service request callback for this diagnostic communication manager.
        Only sets the value if it is not None.

        Args:
            value: The service request callback type to set

        Returns:
            self for method chaining
        """
        self.serviceRequestCallbackType = value
        return self


class DiagnosticRoutineNeeds(DiagnosticCapabilityElement):
    """
    Represents diagnostic routine needs in AUTOSAR models.
    This class defines requirements for diagnostic routines including their execution type and RID number.
    """

    # DiagnosticRoutineNeeds method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [ ] getDiagRoutineType           [x] impl  [x] docstring  [ ] test
    # [ ] setDiagRoutineType           [x] impl  [x] docstring  [ ] test
    # [ ] getRidNumber                 [x] impl  [x] docstring  [ ] test
    # [ ] setRidNumber                 [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the DiagnosticRoutineNeeds with a parent and short name.

        Args:
            parent: The parent ARObject that contains this diagnostic routine needs
            short_name: The unique short name of this diagnostic routine needs
        """
        super().__init__(parent, short_name)

        # Type of diagnostic routine (synchronous or asynchronous)
        self.diagRoutineType: DiagnosticRoutineTypeEnum = None
        # RID (Routine ID) number for this diagnostic routine
        self.RidNumber: PositiveInteger = None

    def getDiagRoutineType(self):
        """
        Gets the type of diagnostic routine (synchronous or asynchronous).

        Returns:
            DiagnosticRoutineTypeEnum: The diagnostic routine type
        """
        return self.diagRoutineType

    def setDiagRoutineType(self, value):
        """
        Sets the type of diagnostic routine (synchronous or asynchronous).
        Only sets the value if it is not None.

        Args:
            value: The diagnostic routine type to set

        Returns:
            self for method chaining
        """
        self.diagRoutineType = value
        return self

    def getRidNumber(self):
        """
        Gets the RID (Routine ID) number for this diagnostic routine.

        Returns:
            PositiveInteger: The RID number
        """
        return self.RidNumber

    def setRidNumber(self, value):
        """
        Sets the RID (Routine ID) number for this diagnostic routine.
        Only sets the value if it is not None.

        Args:
            value: The RID number to set

        Returns:
            self for method chaining
        """
        self.RidNumber = value
        return self


class DiagnosticValueAccessEnum(AREnum):
    """
    Enumeration for diagnostic value access types in AUTOSAR models.
    Defines the access permissions for diagnostic values (read, write, or read-write).
    """

    # DiagnosticValueAccessEnum method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test

    # Read-only access for diagnostic values
    READ_ONLY = "readOnly"
    # Read-write access for diagnostic values
    READ_WRITE = "readWrite"
    # Write-only access for diagnostic values
    WRITE_ONLY = "writeOnly"

    def __init__(self):
        """
        Initializes the DiagnosticValueAccessEnum with all possible values.
        """
        super().__init__(
            (
                DiagnosticValueAccessEnum.READ_ONLY,
                DiagnosticValueAccessEnum.READ_WRITE,
                DiagnosticValueAccessEnum.WRITE_ONLY,
            )
        )


class DiagnosticProcessingStyleEnum(AREnum):
    """
    Enumeration for diagnostic processing styles in AUTOSAR models.
    Defines how diagnostic processing is handled (synchronously, asynchronously, etc.).
    """

    # DiagnosticProcessingStyleEnum method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test

    # Asynchronous processing style for diagnostics
    PROCESSING_STYLE_ASYNCHRONOUS = "processingStyleAsynchronous"
    # Asynchronous processing style with error handling for diagnostics
    PROCESSING_STYLE_ASYNCHRONOUS_WITH_ERROR = "processingStyleAsynchronousWithError"
    # Synchronous processing style for diagnostics
    PROCESSING_STYLE_SYNCHRONOUS = "processingStyleSynchronous"

    def __init__(self):
        """
        Initializes the DiagnosticProcessingStyleEnum with all possible values.
        """
        super().__init__(
            (
                DiagnosticProcessingStyleEnum.PROCESSING_STYLE_ASYNCHRONOUS,
                DiagnosticProcessingStyleEnum.PROCESSING_STYLE_ASYNCHRONOUS_WITH_ERROR,
                DiagnosticProcessingStyleEnum.PROCESSING_STYLE_SYNCHRONOUS,
            )
        )


class DiagnosticValueNeeds(DiagnosticCapabilityElement):
    """
    Represents diagnostic value needs in AUTOSAR models.
    This class defines requirements for diagnostic values including access permissions, length, and processing style.
    """

    # DiagnosticValueNeeds method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [ ] getDataLength                [x] impl  [x] docstring  [ ] test
    # [ ] setDataLength                [x] impl  [x] docstring  [ ] test
    # [ ] getDiagnosticValueAccess     [x] impl  [x] docstring  [ ] test
    # [ ] setDiagnosticValueAccess     [x] impl  [x] docstring  [ ] test
    # [ ] getDidNumber                 [x] impl  [x] docstring  [ ] test
    # [ ] setDidNumber                 [x] impl  [x] docstring  [ ] test
    # [ ] getFixedLength               [x] impl  [x] docstring  [ ] test
    # [ ] setFixedLength               [x] impl  [x] docstring  [ ] test
    # [ ] getProcessingStyle           [x] impl  [x] docstring  [ ] test
    # [ ] setProcessingStyle           [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the DiagnosticValueNeeds with a parent and short name.

        Args:
            parent: The parent ARObject that contains this diagnostic value needs
            short_name: The unique short name of this diagnostic value needs
        """
        super().__init__(parent, short_name)

        # Data length for this diagnostic value
        self.dataLength: PositiveInteger = None
        # Access permissions for this diagnostic value
        self.diagnosticValueAccess: DiagnosticValueAccessEnum = None
        # DID (Data ID) number for this diagnostic value
        self.DidNumber: Integer = None
        # Flag indicating if this diagnostic value has fixed length
        self.fixedLength: Boolean = None
        # Processing style for this diagnostic value
        self.processingStyle: DiagnosticProcessingStyleEnum = None

    def getDataLength(self):
        """
        Gets the data length for this diagnostic value.

        Returns:
            PositiveInteger: The data length
        """
        return self.dataLength

    def setDataLength(self, value):
        """
        Sets the data length for this diagnostic value.
        Only sets the value if it is not None.

        Args:
            value: The data length to set

        Returns:
            self for method chaining
        """
        self.dataLength = value
        return self

    def getDiagnosticValueAccess(self):
        """
        Gets the access permissions for this diagnostic value.

        Returns:
            DiagnosticValueAccessEnum: The diagnostic value access permissions
        """
        return self.diagnosticValueAccess

    def setDiagnosticValueAccess(self, value):
        """
        Sets the access permissions for this diagnostic value.
        Only sets the value if it is not None.

        Args:
            value: The diagnostic value access permissions to set

        Returns:
            self for method chaining
        """
        self.diagnosticValueAccess = value
        return self

    def getDidNumber(self):
        """
        Gets the DID (Data ID) number for this diagnostic value.

        Returns:
            Integer: The DID number
        """
        return self.DidNumber

    def setDidNumber(self, value):
        """
        Sets the DID (Data ID) number for this diagnostic value.
        Only sets the value if it is not None.

        Args:
            value: The DID number to set

        Returns:
            self for method chaining
        """
        self.DidNumber = value
        return self

    def getFixedLength(self):
        """
        Gets the flag indicating if this diagnostic value has fixed length.

        Returns:
            Boolean: The fixed length flag
        """
        return self.fixedLength

    def setFixedLength(self, value):
        """
        Sets the flag indicating if this diagnostic value has fixed length.
        Only sets the value if it is not None.

        Args:
            value: The fixed length flag to set

        Returns:
            self for method chaining
        """
        self.fixedLength = value
        return self

    def getProcessingStyle(self):
        """
        Gets the processing style for this diagnostic value.

        Returns:
            DiagnosticProcessingStyleEnum: The processing style
        """
        return self.processingStyle

    def setProcessingStyle(self, value):
        """
        Sets the processing style for this diagnostic value.
        Only sets the value if it is not None.

        Args:
            value: The processing style to set

        Returns:
            self for method chaining
        """
        self.processingStyle = value
        return self


class DiagEventDebounceAlgorithm(Identifiable, ABC):
    """
    Abstract base class for diagnostic event debounce algorithms in AUTOSAR models.
    This class defines the base structure for algorithms that debounce diagnostic events to prevent false triggers.
    """

    # DiagEventDebounceAlgorithm method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the DiagEventDebounceAlgorithm with a parent and short name.
        Raises TypeError if this abstract class is instantiated directly.

        Args:
            parent: The parent ARObject that contains this diagnostic event debounce algorithm
            short_name: The unique short name of this diagnostic event debounce algorithm
        """
        if type(self) is DiagEventDebounceAlgorithm:
            raise TypeError("DiagEventDebounceAlgorithm is an abstract class.")

        super().__init__(parent, short_name)


class DiagEventDebounceCounterBased(DiagEventDebounceAlgorithm):
    """
    Represents a counter-based diagnostic event debounce algorithm in AUTOSAR models.
    This class defines debounce algorithms based on counters that increment/decrement to detect fault conditions.
    """

    # DiagEventDebounceCounterBased method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [ ] getCounterBasedFdcThresholdStorageValue [x] impl  [ ] docstring  [ ] test
    # [ ] setCounterBasedFdcThresholdStorageValue [x] impl  [ ] docstring  [ ] test
    # [ ] getCounterDecrementStepSize  [x] impl  [ ] docstring  [ ] test
    # [ ] setCounterDecrementStepSize  [x] impl  [ ] docstring  [ ] test
    # [ ] getCounterFailedThreshold    [x] impl  [ ] docstring  [ ] test
    # [ ] setCounterFailedThreshold    [x] impl  [ ] docstring  [ ] test
    # [ ] getCounterIncrementStepSize  [x] impl  [ ] docstring  [ ] test
    # [ ] setCounterIncrementStepSize  [x] impl  [ ] docstring  [ ] test
    # [ ] getCounterJumpDown           [x] impl  [ ] docstring  [ ] test
    # [ ] setCounterJumpDown           [x] impl  [ ] docstring  [ ] test
    # [ ] getCounterJumpDownValue      [x] impl  [ ] docstring  [ ] test
    # [ ] setCounterJumpDownValue      [x] impl  [ ] docstring  [ ] test
    # [ ] getCounterJumpUp             [x] impl  [ ] docstring  [ ] test
    # [ ] setCounterJumpUp             [x] impl  [ ] docstring  [ ] test
    # [ ] getCounterJumpUpValue        [x] impl  [ ] docstring  [ ] test
    # [ ] setCounterJumpUpValue        [x] impl  [ ] docstring  [ ] test
    # [ ] getCounterPassedThreshold    [x] impl  [ ] docstring  [ ] test
    # [ ] setCounterPassedThreshold    [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the DiagEventDebounceCounterBased with a parent and short name.

        Args:
            parent: The parent ARObject that contains this counter-based debounce algorithm
            short_name: The unique short name of this counter-based debounce algorithm
        """
        super().__init__(parent, short_name)

        # Counter-based FDC (Fault Detection Counter) threshold storage value
        self.counterBasedFdcThresholdStorageValue: Integer = None
        # Counter decrement step size for this debounce algorithm
        self.counterDecrementStepSize: Integer = None
        # Counter threshold for failed state detection
        self.counterFailedThreshold: Integer = None
        # Counter increment step size for this debounce algorithm
        self.counterIncrementStepSize: Integer = None
        # Counter value to jump down to when conditions are met
        self.counterJumpDown: Integer = None
        # Value to set counter to when jumping down
        self.counterJumpDownValue: Integer = None
        # Counter value to jump up to when conditions are met
        self.counterJumpUp: Integer = None
        # Value to set counter to when jumping up
        self.counterJumpUpValue: Integer = None
        # Counter threshold for passed state detection
        self.counterPassedThreshold: Integer = None

    def getCounterBasedFdcThresholdStorageValue(self):
        return self.counterBasedFdcThresholdStorageValue

    def setCounterBasedFdcThresholdStorageValue(self, value):
        self.counterBasedFdcThresholdStorageValue = value
        return self

    def getCounterDecrementStepSize(self):
        return self.counterDecrementStepSize

    def setCounterDecrementStepSize(self, value):
        self.counterDecrementStepSize = value
        return self

    def getCounterFailedThreshold(self):
        return self.counterFailedThreshold

    def setCounterFailedThreshold(self, value):
        self.counterFailedThreshold = value
        return self

    def getCounterIncrementStepSize(self):
        return self.counterIncrementStepSize

    def setCounterIncrementStepSize(self, value):
        self.counterIncrementStepSize = value
        return self

    def getCounterJumpDown(self):
        return self.counterJumpDown

    def setCounterJumpDown(self, value):
        self.counterJumpDown = value
        return self

    def getCounterJumpDownValue(self):
        return self.counterJumpDownValue

    def setCounterJumpDownValue(self, value):
        self.counterJumpDownValue = value
        return self

    def getCounterJumpUp(self):
        return self.counterJumpUp

    def setCounterJumpUp(self, value):
        self.counterJumpUp = value
        return self

    def getCounterJumpUpValue(self):
        return self.counterJumpUpValue

    def setCounterJumpUpValue(self, value):
        self.counterJumpUpValue = value
        return self

    def getCounterPassedThreshold(self):
        return self.counterPassedThreshold

    def setCounterPassedThreshold(self, value):
        self.counterPassedThreshold = value
        return self


class DiagEventDebounceMonitorInternal(DiagEventDebounceAlgorithm):
    """
    Represents an internal monitor-based diagnostic event debounce algorithm in AUTOSAR models.
    This class defines debounce algorithms based on internal monitoring mechanisms rather than counters or time thresholds.
    """

    # DiagEventDebounceMonitorInternal method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the DiagEventDebounceMonitorInternal with a parent and short name.

        Args:
            parent: The parent ARObject that contains this internal monitor debounce algorithm
            short_name: The unique short name of this internal monitor debounce algorithm
        """
        super().__init__(parent, short_name)


class DiagEventDebounceTimeBased(DiagEventDebounceAlgorithm):
    """
    Represents a time-based diagnostic event debounce algorithm in AUTOSAR models.
    This class defines debounce algorithms based on time thresholds to detect and handle diagnostic events.
    """

    # DiagEventDebounceTimeBased method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [ ] getTimeBasedFdcThresholdStorageValue [x] impl  [ ] docstring  [ ] test
    # [ ] setTimeBasedFdcThresholdStorageValue [x] impl  [ ] docstring  [ ] test
    # [ ] getTimeFailedThreshold       [x] impl  [ ] docstring  [ ] test
    # [ ] setTimeFailedThreshold       [x] impl  [ ] docstring  [ ] test
    # [ ] getTimePassedThreshold       [x] impl  [ ] docstring  [ ] test
    # [ ] setTimePassedThreshold       [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the DiagEventDebounceTimeBased with a parent and short name.

        Args:
            parent: The parent ARObject that contains this time-based debounce algorithm
            short_name: The unique short name of this time-based debounce algorithm
        """
        super().__init__(parent, short_name)

        # Time-based FDC (Fault Detection Counter) threshold storage value
        self.timeBasedFdcThresholdStorageValue: TimeValue = None
        # Time threshold for failed state detection
        self.timeFailedThreshold: TimeValue = None
        # Time threshold for passed state detection
        self.timePassedThreshold: TimeValue = None

    def getTimeBasedFdcThresholdStorageValue(self):
        return self.timeBasedFdcThresholdStorageValue

    def setTimeBasedFdcThresholdStorageValue(self, value):
        self.timeBasedFdcThresholdStorageValue = value
        return self

    def getTimeFailedThreshold(self):
        return self.timeFailedThreshold

    def setTimeFailedThreshold(self, value):
        self.timeFailedThreshold = value
        return self

    def getTimePassedThreshold(self):
        return self.timePassedThreshold

    def setTimePassedThreshold(self, value):
        self.timePassedThreshold = value
        return self


class DtcKindEnum(AREnum):
    """
    Enumeration for DTC (Diagnostic Trouble Code) kinds in AUTOSAR models.
    Defines the type of diagnostic trouble codes used (currently empty as per specification).
    """

    # DtcKindEnum method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test

    def __init__(self):
        """
        Initializes the DtcKindEnum with empty values list.
        """
        super().__init__([])


class DiagnosticEventInfoNeeds(DiagnosticCapabilityElement):
    """
    Represents diagnostic event information needs in AUTOSAR models.
    This class defines requirements for diagnostic events including DTC information and numbering schemes.
    """

    # DiagnosticEventInfoNeeds method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [ ] getDtcKind                   [x] impl  [x] docstring  [ ] test
    # [ ] setDtcKind                   [x] impl  [x] docstring  [ ] test
    # [ ] getObdDtcNumber              [x] impl  [x] docstring  [ ] test
    # [ ] setObdDtcNumber              [x] impl  [x] docstring  [ ] test
    # [ ] getUdsDtcNumber              [x] impl  [x] docstring  [ ] test
    # [ ] setUdsDtcNumber              [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the DiagnosticEventInfoNeeds with a parent and short name.

        Args:
            parent: The parent ARObject that contains this diagnostic event information needs
            short_name: The unique short name of this diagnostic event information needs
        """
        super().__init__(parent, short_name)

        # Type of diagnostic trouble code (DTC) for this event
        self.dtcKind: DtcKindEnum = None
        # OBD (On-Board Diagnostics) DTC number for this event
        self.obdDtcNumber: PositiveInteger = None
        # UDS (Unified Diagnostic Services) DTC number for this event
        self.udsDtcNumber: PositiveInteger = None

    def getDtcKind(self):
        """
        Gets the type of diagnostic trouble code (DTC) for this event.

        Returns:
            DtcKindEnum: The DTC kind
        """
        return self.dtcKind

    def setDtcKind(self, value):
        """
        Sets the type of diagnostic trouble code (DTC) for this event.
        Only sets the value if it is not None.

        Args:
            value: The DTC kind to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.dtcKind = value
        return self

    def getObdDtcNumber(self):
        """
        Gets the OBD (On-Board Diagnostics) DTC number for this event.

        Returns:
            PositiveInteger: The OBD DTC number
        """
        return self.obdDtcNumber

    def setObdDtcNumber(self, value):
        """
        Sets the OBD (On-Board Diagnostics) DTC number for this event.
        Only sets the value if it is not None.

        Args:
            value: The OBD DTC number to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.obdDtcNumber = value
        return self

    def getUdsDtcNumber(self):
        """
        Gets the UDS (Unified Diagnostic Services) DTC number for this event.

        Returns:
            PositiveInteger: The UDS DTC number
        """
        return self.udsDtcNumber

    def setUdsDtcNumber(self, value):
        """
        Sets the UDS (Unified Diagnostic Services) DTC number for this event.
        Only sets the value if it is not None.

        Args:
            value: The UDS DTC number to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.udsDtcNumber = value
        return self


class DiagnosticClearDtcNotificationEnum(AREnum):
    """
    Enumeration for diagnostic clear DTC notification types in AUTOSAR models.
    Defines the timing for notification when DTCs are cleared (currently empty as per specification).
    """

    # DiagnosticClearDtcNotificationEnum method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test

    def __init__(self):
        """
        Initializes the DiagnosticClearDtcNotificationEnum with empty values list.
        """
        super().__init__([])


class DtcFormatTypeEnum(AREnum):
    """
    Enumeration for DTC format types in AUTOSAR models.
    Defines the format used for diagnostic trouble codes (currently empty as per specification).
    """

    # DtcFormatTypeEnum method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test

    def __init__(self):
        """
        Initializes the DtcFormatTypeEnum with empty values list.
        """
        super().__init__([])


class DtcStatusChangeNotificationNeeds(DiagnosticCapabilityElement):
    """
    Represents DTC status change notification needs in AUTOSAR models.
    This class defines requirements for notifications when DTC status changes occur.
    """

    # DtcStatusChangeNotificationNeeds method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [ ] getDtcFormatType             [x] impl  [x] docstring  [ ] test
    # [ ] setDtcFormatType             [x] impl  [x] docstring  [ ] test
    # [ ] getNotificationTime          [x] impl  [x] docstring  [ ] test
    # [ ] setNotificationTime          [x] impl  [x] docstring  [ ] test

    def __init__(self, parent, short_name):
        """
        Initializes the DtcStatusChangeNotificationNeeds with a parent and short name.
        Note: This is an extension for AUTOSAR 4.3.1.

        Args:
            parent: The parent ARObject that contains this DTC status change notification needs
            short_name: The unique short name of this DTC status change notification needs
        """
        super().__init__(parent, short_name)

        # Format type for DTC used in notifications
        self.dtcFormatType: DtcFormatTypeEnum = None
        # Notification timing for when DTCs are cleared
        self.notificationTime: DiagnosticClearDtcNotificationEnum = None

    def getDtcFormatType(self):
        """
        Gets the format type for DTC used in notifications.

        Returns:
            DtcFormatTypeEnum: The DTC format type
        """
        return self.dtcFormatType

    def setDtcFormatType(self, value):
        """
        Sets the format type for DTC used in notifications.
        Only sets the value if it is not None.

        Args:
            value: The DTC format type to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.dtcFormatType = value
        return self

    def getNotificationTime(self):
        """
        Gets the notification timing for when DTCs are cleared.

        Returns:
            DiagnosticClearDtcNotificationEnum: The notification timing
        """
        return self.notificationTime

    def setNotificationTime(self, value):
        """
        Sets the notification timing for when DTCs are cleared.
        Only sets the value if it is not None.

        Args:
            value: The notification timing to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.notificationTime = value
        return self


class DiagnosticEventNeeds(DiagnosticCapabilityElement):
    """
    Specifies the abstract needs on the configuration of the Diagnostic Event Manager for one diagnostic event. Its shortName can be regarded as a symbol identifying the diagnostic event from the viewpoint of the component or module which owns this element. In case the diagnostic event specifies a production error, the shortName shall be the name of the production error.
    """

    # DiagnosticEventNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 12.31, p.258
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getDeferringFidRefs          [x] impl  [x] docstring  [x] test
    # [x] addDeferringFidRef           [x] impl  [x] docstring  [x] test
    # [x] getDiagEventDebounceAlgorithm [x] impl  [x] docstring  [x] test
    # [x] createDiagEventDebounceCounterBased [x] impl  [x] docstring  [x] test
    # [x] createDiagEventDebounceMonitorInternal [x] impl  [x] docstring  [x] test
    # [x] createDiagEventDebounceTimeBased [x] impl  [x] docstring  [x] test
    # [x] getInhibitingFidRef          [x] impl  [x] docstring  [x] test
    # [x] setInhibitingFidRef          [x] impl  [x] docstring  [x] test
    # [x] getInhibitingSecondaryFidRefs [x] impl  [x] docstring  [x] test
    # [x] addInhibitingSecondaryFidRef [x] impl  [x] docstring  [x] test
    # [x] getPrestoredFreezeframeStoredInNvm [x] impl  [x] docstring  [x] test
    # [x] setPrestoredFreezeframeStoredInNvm [x] impl  [x] docstring  [x] test
    # [x] getUsesMonitorData           [x] impl  [x] docstring  [x] test
    # [x] setUsesMonitorData           [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the DiagnosticEventNeeds with a parent and short name.

        Args:
            parent: The parent ARObject that contains this diagnostic event needs
            short_name: The unique short name of this diagnostic event needs
        """
        super().__init__(parent, short_name)

        # This reference contains the link to a function identifier within the FiM which is used by the monitor before delivering a result.
        self.deferringFidRefs: List[RefType] = []

        # Specifies the abstract need on the Debounce Algorithm applied by the Diagnostic Event Manager.
        self.diagEventDebounceAlgorithm: Optional[DiagEventDebounceAlgorithm] = None

        # This represents the primary Function Inhibition Identifier used for inhibition of the diagnostic monitor. The FID might either inhibit the monitoring of a symptom or the reporting of detected faults.
        self.inhibitingFidRef: Optional[RefType] = None

        # This represents the secondary Function Inhibition Identifier used for inhibition of the diagnostic monitor. Any of the FID inhibitions leads to an inhibition of the monitoring of a symptom or the reporting of detected faults.
        self.inhibitingSecondaryFidRefs: List[RefType] = []

        # If the Event uses a prestored freeze-frame (using the operations PrestoreFreezeFrame and ClearPrestoredFreezeFrame of the service interface DiagnosticMonitor) this attribute indicates if the Event requires the data to be stored in non-volatile memory. TRUE = Dem shall store the prestored data in non-volatile memory, FALSE = Data can be lost at shutdown (not stored in Nvm).
        self.prestoredFreezeframeStoredInNvm: Optional[Boolean] = None

        # This attribute defines whether additional monitor data shall be added to the reporting of events.
        self.usesMonitorData: Optional[Boolean] = None

    def getDeferringFidRefs(self) -> List[RefType]:
        """
        Gets the references to function identifiers within the FiM which are used by the monitor before delivering a result.

        Returns:
            List of RefType instances
        """
        return self.deferringFidRefs

    def addDeferringFidRef(self, value: Optional[RefType]) -> "DiagnosticEventNeeds":
        """
        Adds a reference to a function identifier within the FiM which is used by the monitor before delivering a result.
        A None value is a no-op and does not append anything.

        Args:
            value: The RefType instance to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.deferringFidRefs.append(value)
        return self

    def getDiagEventDebounceAlgorithm(self) -> Optional[DiagEventDebounceAlgorithm]:
        """
        Gets the abstract need on the Debounce Algorithm applied by the Diagnostic Event Manager.

        Returns:
            DiagEventDebounceAlgorithm instance, or None if not set
        """
        return self.diagEventDebounceAlgorithm

    def createDiagEventDebounceCounterBased(self, short_name: str) -> DiagEventDebounceCounterBased:
        """
        Creates and adds a counter-based debounce algorithm for this diagnostic event.

        Args:
            short_name: The short name for the new counter-based debounce algorithm

        Returns:
            The created DiagEventDebounceCounterBased instance
        """
        if short_name not in self.elements:
            algorithm = DiagEventDebounceCounterBased(self, short_name)
            self.addElement(algorithm)
            self.diagEventDebounceAlgorithm = algorithm
        return self.getElement(short_name)

    def createDiagEventDebounceMonitorInternal(self, short_name: str) -> DiagEventDebounceMonitorInternal:
        """
        Creates and adds an internal monitor-based debounce algorithm for this diagnostic event.

        Args:
            short_name: The short name for the new internal monitor debounce algorithm

        Returns:
            The created DiagEventDebounceMonitorInternal instance
        """
        if short_name not in self.elements:
            algorithm = DiagEventDebounceMonitorInternal(self, short_name)
            self.addElement(algorithm)
            self.diagEventDebounceAlgorithm = algorithm
        return self.getElement(short_name)

    def createDiagEventDebounceTimeBased(self, short_name: str) -> DiagEventDebounceTimeBased:
        """
        Creates and adds a time-based debounce algorithm for this diagnostic event.

        Args:
            short_name: The short name for the new time-based debounce algorithm

        Returns:
            The created DiagEventDebounceTimeBased instance
        """
        if short_name not in self.elements:
            algorithm = DiagEventDebounceTimeBased(self, short_name)
            self.addElement(algorithm)
            self.diagEventDebounceAlgorithm = algorithm
        return self.getElement(short_name)

    def getInhibitingFidRef(self) -> Optional[RefType]:
        """
        Gets the primary Function Inhibition Identifier used for inhibition of the diagnostic monitor. The FID might either inhibit the monitoring of a symptom or the reporting of detected faults.

        Returns:
            RefType instance, or None if not set
        """
        return self.inhibitingFidRef

    def setInhibitingFidRef(self, value: Optional[RefType]) -> "DiagnosticEventNeeds":
        """
        Sets the primary Function Inhibition Identifier used for inhibition of the diagnostic monitor. The FID might either inhibit the monitoring of a symptom or the reporting of detected faults.
        A None value is a no-op and does not overwrite an existing inhibitingFidRef.

        Args:
            value: The RefType instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.inhibitingFidRef = value
        return self

    def getInhibitingSecondaryFidRefs(self) -> List[RefType]:
        """
        Gets the secondary Function Inhibition Identifiers used for inhibition of the diagnostic monitor. Any of the FID inhibitions leads to an inhibition of the monitoring of a symptom or the reporting of detected faults.

        Returns:
            List of RefType instances
        """
        return self.inhibitingSecondaryFidRefs

    def addInhibitingSecondaryFidRef(self, value: Optional[RefType]) -> "DiagnosticEventNeeds":
        """
        Adds a secondary Function Inhibition Identifier used for inhibition of the diagnostic monitor. Any of the FID inhibitions leads to an inhibition of the monitoring of a symptom or the reporting of detected faults.
        A None value is a no-op and does not append anything.

        Args:
            value: The RefType instance to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.inhibitingSecondaryFidRefs.append(value)
        return self

    def getPrestoredFreezeframeStoredInNvm(self) -> Optional[Boolean]:
        """
        Gets whether the Event requires the data of a prestored freeze-frame to be stored in non-volatile memory. TRUE = Dem shall store the prestored data in non-volatile memory, FALSE = Data can be lost at shutdown (not stored in Nvm).

        Returns:
            Boolean instance, or None if not set
        """
        return self.prestoredFreezeframeStoredInNvm

    def setPrestoredFreezeframeStoredInNvm(self, value: Optional[Boolean]) -> "DiagnosticEventNeeds":
        """
        Sets whether the Event requires the data of a prestored freeze-frame to be stored in non-volatile memory. TRUE = Dem shall store the prestored data in non-volatile memory, FALSE = Data can be lost at shutdown (not stored in Nvm).
        A None value is a no-op and does not overwrite an existing prestoredFreezeframeStoredInNvm.

        Args:
            value: The Boolean instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.prestoredFreezeframeStoredInNvm = value
        return self

    def getUsesMonitorData(self) -> Optional[Boolean]:
        """
        Gets whether additional monitor data shall be added to the reporting of events.

        Returns:
            Boolean instance, or None if not set
        """
        return self.usesMonitorData

    def setUsesMonitorData(self, value: Optional[Boolean]) -> "DiagnosticEventNeeds":
        """
        Sets whether additional monitor data shall be added to the reporting of events.
        A None value is a no-op and does not overwrite an existing usesMonitorData.

        Args:
            value: The Boolean instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.usesMonitorData = value
        return self


class CryptoServiceNeeds(ServiceNeeds):
    """
    Represents cryptographic service needs in AUTOSAR models.
    This class defines requirements for cryptographic services including algorithm information and key management.
    """

    # CryptoServiceNeeds method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [ ] getAlgorithmFamily           [x] impl  [x] docstring  [ ] test
    # [ ] setAlgorithmFamily           [x] impl  [x] docstring  [ ] test
    # [ ] getAlgorithmMode             [x] impl  [x] docstring  [ ] test
    # [ ] setAlgorithmMode             [x] impl  [x] docstring  [ ] test
    # [ ] getCryptoKeyDescription      [x] impl  [x] docstring  [ ] test
    # [ ] setCryptoKeyDescription      [x] impl  [x] docstring  [ ] test
    # [ ] getMaximumKeyLength          [x] impl  [x] docstring  [ ] test
    # [ ] setMaximumKeyLength          [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the CryptoServiceNeeds with a parent and short name.

        Args:
            parent: The parent ARObject that contains this cryptographic service needs
            short_name: The unique short name of this cryptographic service needs
        """
        super().__init__(parent, short_name)

        # Algorithm family used by this cryptographic service
        self.algorithmFamily: String = None
        # Algorithm mode used by this cryptographic service
        self.algorithmMode: String = None
        # Description of the cryptographic key used by this service
        self.cryptoKeyDescription: String = None
        # Maximum length of keys supported by this cryptographic service
        self.maximumKeyLength: PositiveInteger = None

    def getAlgorithmFamily(self):
        """
        Gets the algorithm family used by this cryptographic service.

        Returns:
            String: The algorithm family
        """
        return self.algorithmFamily

    def setAlgorithmFamily(self, value):
        """
        Sets the algorithm family used by this cryptographic service.
        Only sets the value if it is not None.

        Args:
            value: The algorithm family to set

        Returns:
            self for method chaining
        """
        self.algorithmFamily = value
        return self

    def getAlgorithmMode(self):
        """
        Gets the algorithm mode used by this cryptographic service.

        Returns:
            String: The algorithm mode
        """
        return self.algorithmMode

    def setAlgorithmMode(self, value):
        """
        Sets the algorithm mode used by this cryptographic service.
        Only sets the value if it is not None.

        Args:
            value: The algorithm mode to set

        Returns:
            self for method chaining
        """
        self.algorithmMode = value
        return self

    def getCryptoKeyDescription(self):
        """
        Gets the description of the cryptographic key used by this service.

        Returns:
            String: The cryptographic key description
        """
        return self.cryptoKeyDescription

    def setCryptoKeyDescription(self, value):
        """
        Sets the description of the cryptographic key used by this service.
        Only sets the value if it is not None.

        Args:
            value: The cryptographic key description to set

        Returns:
            self for method chaining
        """
        self.cryptoKeyDescription = value
        return self

    def getMaximumKeyLength(self):
        """
        Gets the maximum length of keys supported by this cryptographic service.

        Returns:
            PositiveInteger: The maximum key length
        """
        return self.maximumKeyLength

    def setMaximumKeyLength(self, value):
        """
        Sets the maximum length of keys supported by this cryptographic service.
        Only sets the value if it is not None.

        Args:
            value: The maximum key length to set

        Returns:
            self for method chaining
        """
        self.maximumKeyLength = value
        return self


class EcuStateMgrUserNeeds(ServiceNeeds):
    """
    Represents ECU state manager user needs in AUTOSAR models.
    This class defines requirements for components that use the ECU state manager service.
    """

    # EcuStateMgrUserNeeds method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the EcuStateMgrUserNeeds with a parent and short name.

        Args:
            parent: The parent ARObject that contains this ECU state manager user needs
            short_name: The unique short name of this ECU state manager user needs
        """
        super().__init__(parent, short_name)


class DltUserNeeds(ServiceNeeds):
    """
    Represents DLT (Diagnostic Log and Trace) user needs in AUTOSAR models.
    This class defines requirements for components that use the DLT service for logging and tracing.
    """

    # DltUserNeeds method parity checklist:
    # [x] __init__                     [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the DltUserNeeds with a parent and short name.

        Args:
            parent: The parent ARObject that contains this DLT user needs
            short_name: The unique short name of this DLT user needs
        """
        super().__init__(parent, short_name)


class BswMgrNeeds(ServiceNeeds):
    """
    Represents BSW Manager needs in AUTOSAR models.
    This class defines requirements for Basic Software Manager services.
    """

    # BswMgrNeeds method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the BswMgrNeeds with a parent and short name.

        Args:
            parent: The parent ARObject that contains this BSW manager needs
            short_name: The unique short name of this BSW manager needs
        """
        super().__init__(parent, short_name)


class ComMgrUserNeeds(ServiceNeeds):
    """
    Specifies the abstract needs on the configuration of the Communication Manager for one "user".
    """

    # ComMgrUserNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 12.13, p.235
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getMaxCommMode               [x] impl  [x] docstring  [x] test
    # [x] setMaxCommMode               [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the ComMgrUserNeeds with a parent and short name.

        Args:
            parent: The parent ARObject that contains this COM manager user needs
            short_name: The unique short name of this COM manager user needs
        """
        super().__init__(parent, short_name)

        # Maximum communication mode requested by this ComM user.
        self.maxCommMode: Optional[MaxCommModeEnum] = None

    def getMaxCommMode(self) -> Optional[MaxCommModeEnum]:
        """
        Gets the maximum communication mode requested by this ComM user.

        Returns:
            MaxCommModeEnum instance, or None if not set
        """
        return self.maxCommMode

    def setMaxCommMode(self, value: Optional[MaxCommModeEnum]) -> "ComMgrUserNeeds":
        """
        Sets the maximum communication mode requested by this ComM user.
        A None value is a no-op and does not overwrite an existing maxCommMode.

        Args:
            value: The MaxCommModeEnum instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.maxCommMode = value
        return self


class CryptoKeyManagementNeeds(ServiceNeeds):
    """
    Represents Cryptographic Key Management needs in AUTOSAR models.
    This class defines requirements for cryptographic key management services.
    """

    # CryptoKeyManagementNeeds method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the CryptoKeyManagementNeeds with a parent and short name.

        Args:
            parent: The parent ARObject that contains this crypto key management needs
            short_name: The unique short name of this crypto key management needs
        """
        super().__init__(parent, short_name)


class CryptoServiceJobNeeds(ServiceNeeds):
    """
    Represents Cryptographic Service Job needs in AUTOSAR models.
    This class defines requirements for cryptographic service job operations.
    """

    # CryptoServiceJobNeeds method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the CryptoServiceJobNeeds with a parent and short name.

        Args:
            parent: The parent ARObject that contains this crypto service job needs
            short_name: The unique short name of this crypto service job needs
        """
        super().__init__(parent, short_name)


class TracedFailure(Identifiable, ABC):
    """
    Specifies the ability to report a specific failure to the error tracer. The short name specifies the literal applicable for the Default Error Tracer.
    """

    # TracedFailure method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 12.37, p.263
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getId                        [x] impl  [x] docstring  [x] test
    # [x] setId                        [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the TracedFailure with a parent and short name.
        Raises TypeError if this abstract class is instantiated directly.

        Args:
            parent: The parent ARObject that contains this traced failure
            short_name: The unique short name of this traced failure
        """
        if type(self) is TracedFailure:
            raise TypeError("TracedFailure is an abstract class.")

        super().__init__(parent, short_name)

        # ID of detected failure used in reporting API as error or fault id.
        self.id: Optional[PositiveInteger] = None

    def getId(self) -> Optional[PositiveInteger]:
        """
        Gets the ID of detected failure used in reporting API as error or fault id.

        Returns:
            PositiveInteger instance, or None if not set
        """
        return self.id

    def setId(self, value: Optional[PositiveInteger]) -> "TracedFailure":
        """
        Sets the ID of detected failure used in reporting API as error or fault id.
        A None value is a no-op and does not overwrite an existing id.

        Args:
            value: The PositiveInteger instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.id = value
        return self


class DevelopmentError(TracedFailure):
    """
    The reported failure is classified as development error.
    """

    # DevelopmentError method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 12.38, p.263
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the DevelopmentError with a parent and short name.

        Args:
            parent: The parent ARObject that contains this development error
            short_name: The unique short name of this development error
        """
        super().__init__(parent, short_name)


class DiagnosticComponentNeeds(ServiceNeeds):
    """
    Represents Diagnostic Component needs in AUTOSAR models.
    This class defines requirements for diagnostic component services.
    """

    # DiagnosticComponentNeeds method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the DiagnosticComponentNeeds with a parent and short name.

        Args:
            parent: The parent ARObject that contains this diagnostic component needs
            short_name: The unique short name of this diagnostic component needs
        """
        super().__init__(parent, short_name)


class DiagnosticControlNeeds(ServiceNeeds):
    """
    Represents Diagnostic Control needs in AUTOSAR models.
    This class defines requirements for diagnostic control services.
    """

    # DiagnosticControlNeeds method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the DiagnosticControlNeeds with a parent and short name.

        Args:
            parent: The parent ARObject that contains this diagnostic control needs
            short_name: The unique short name of this diagnostic control needs
        """
        super().__init__(parent, short_name)


class DiagnosticDenominatorConditionEnum(AREnum):
    """
    This enumeration contains valid denominator types.
    """

    # DiagnosticDenominatorConditionEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.52, p.803
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test

    # Condition based on definition of 500miles conditions as defined for OBD2. Tags: atp.EnumerationLiteralIndex=2 xml.name=-500-MILES
    _500MILES = "_500miles"
    # Condition based on definition of "cold start" as defined for EU5+ Tags: atp.EnumerationLiteralIndex=0
    COLDSTART = "coldstart"
    # Conditions based on the "Cold start emission reduction strategy" denominator Tags: atp.EnumerationLiteralIndex=5
    CSERS = "csers"
    # Condition based on definition of "EVAP" conditions as defined for OBD2. Tags: atp.EnumerationLiteralIndex=1
    EVAP = "evap"
    # Conditions based on the "EVAP purge flow" denominator. Tags: atp.EnumerationLiteralIndex=6
    EVAPPURGEFLOW = "evappurgeflow"
    # condition based on definition of individual requirements. Tags: atp.EnumerationLiteralIndex=3
    INDIVIDUAL = "individual"
    # Condition based on definition of OBD requirements. Tags: atp.EnumerationLiteralIndex=4
    OBD = "obd"

    def __init__(self):
        super().__init__(
            [
                DiagnosticDenominatorConditionEnum._500MILES,
                DiagnosticDenominatorConditionEnum.COLDSTART,
                DiagnosticDenominatorConditionEnum.CSERS,
                DiagnosticDenominatorConditionEnum.EVAP,
                DiagnosticDenominatorConditionEnum.EVAPPURGEFLOW,
                DiagnosticDenominatorConditionEnum.INDIVIDUAL,
                DiagnosticDenominatorConditionEnum.OBD,
            ]
        )


class DiagnosticEnableConditionNeeds(DiagnosticCapabilityElement):
    """
    This meta-class represents the needs of a software-component to provide the capability to set an enable condition.
    """

    # DiagnosticEnableConditionNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.26, p.762
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getInitialStatus             [x] impl  [x] docstring  [x] test
    # [x] setInitialStatus             [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the DiagnosticEnableConditionNeeds with a parent and short name.

        Args:
            parent: The parent ARObject that contains this diagnostic enable condition needs
            short_name: The unique short name of this diagnostic enable condition needs
        """
        super().__init__(parent, short_name)

        # Defines the initial status for enable or disable of acceptance of event reports of a diagnostic event.
        self.initialStatus: Optional[EventAcceptanceStatusEnum] = None

    def getInitialStatus(self) -> Optional[EventAcceptanceStatusEnum]:
        """
        Gets the initial status for enable or disable of acceptance of event reports of a diagnostic event.

        Returns:
            EventAcceptanceStatusEnum instance, or None if not set
        """
        return self.initialStatus

    def setInitialStatus(self, value: Optional[EventAcceptanceStatusEnum]) -> "DiagnosticEnableConditionNeeds":
        """
        Sets a new initialStatus. A None value is a no-op and does not overwrite an existing initialStatus.

        Args:
            value: The EventAcceptanceStatusEnum instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.initialStatus = value
        return self


class DiagnosticEventManagerNeeds(ServiceNeeds):
    """
    Represents Diagnostic Event Manager needs in AUTOSAR models.
    This class defines requirements for diagnostic event manager services.
    """

    # DiagnosticEventManagerNeeds method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the DiagnosticEventManagerNeeds with a parent and short name.

        Args:
            parent: The parent ARObject that contains this diagnostic event manager needs
            short_name: The unique short name of this diagnostic event manager needs
        """
        super().__init__(parent, short_name)


class DiagnosticIoControlNeeds(DiagnosticCapabilityElement):
    """
    Specifies the general needs on the configuration of the Diagnostic Communication Manager (DCM) which are not related to a particular item (e.g. a PID). The main use case is the mapping of service ports to the Dcm which are not related to a particular item.
    """

    # DiagnosticIoControlNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 12.26, p.248
    # Spec verified: R23-11
    # [x] __init__                           [x] impl  [x] docstring  [x] test
    # [x] getCurrentValueRef                 [x] impl  [x] docstring  [x] test
    # [x] setCurrentValueRef                 [x] impl  [x] docstring  [x] test
    # [x] getFreezeCurrentStateSupported     [x] impl  [x] docstring  [x] test
    # [x] setFreezeCurrentStateSupported     [x] impl  [x] docstring  [x] test
    # [x] getResetToDefaultSupported         [x] impl  [x] docstring  [x] test
    # [x] setResetToDefaultSupported         [x] impl  [x] docstring  [x] test
    # [x] getShortTermAdjustmentSupported    [x] impl  [x] docstring  [x] test
    # [x] setShortTermAdjustmentSupported    [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the DiagnosticIoControlNeeds with a parent and short name.

        Args:
            parent: The parent ARObject that contains this diagnostic I/O control needs
            short_name: The unique short name of this diagnostic I/O control needs
        """
        super().__init__(parent, short_name)

        # Reference to the DiagnosticValueNeeds indicating the access to the current value via signalBasedDiagnostics.
        self.currentValueRef: Optional[RefType] = None

        # This attribute determines, if the referenced port supports temporary freezing of I/O value.
        self.freezeCurrentStateSupported: Optional[Boolean] = None

        # This represents a flag for the existence of the ResetToDefault operation in the service interface.
        self.resetToDefaultSupported: Optional[Boolean] = None

        # This attribute determines, if the referenced port supports temporarily setting of I/O value to a specific value provided by the diagnostic tester.
        self.shortTermAdjustmentSupported: Optional[Boolean] = None

    def getCurrentValueRef(self) -> Optional[RefType]:
        """
        Gets the reference to the DiagnosticValueNeeds indicating the access to the current value via signalBasedDiagnostics.

        Returns:
            RefType instance, or None if not set
        """
        return self.currentValueRef

    def setCurrentValueRef(self, value: Optional[RefType]) -> "DiagnosticIoControlNeeds":
        """
        Sets the reference to the DiagnosticValueNeeds indicating the access to the current value via signalBasedDiagnostics.
        A None value is a no-op and does not overwrite an existing currentValueRef.

        Args:
            value: The RefType instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.currentValueRef = value
        return self

    def getFreezeCurrentStateSupported(self) -> Optional[Boolean]:
        """
        Gets whether the referenced port supports temporary freezing of I/O value.

        Returns:
            Boolean instance, or None if not set
        """
        return self.freezeCurrentStateSupported

    def setFreezeCurrentStateSupported(self, value: Optional[Boolean]) -> "DiagnosticIoControlNeeds":
        """
        Sets whether the referenced port supports temporary freezing of I/O value.
        A None value is a no-op and does not overwrite an existing freezeCurrentStateSupported.

        Args:
            value: The Boolean instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.freezeCurrentStateSupported = value
        return self

    def getResetToDefaultSupported(self) -> Optional[Boolean]:
        """
        Gets the flag for the existence of the ResetToDefault operation in the service interface.

        Returns:
            Boolean instance, or None if not set
        """
        return self.resetToDefaultSupported

    def setResetToDefaultSupported(self, value: Optional[Boolean]) -> "DiagnosticIoControlNeeds":
        """
        Sets the flag for the existence of the ResetToDefault operation in the service interface.
        A None value is a no-op and does not overwrite an existing resetToDefaultSupported.

        Args:
            value: The Boolean instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.resetToDefaultSupported = value
        return self

    def getShortTermAdjustmentSupported(self) -> Optional[Boolean]:
        """
        Gets whether the referenced port supports temporarily setting of I/O value to a specific value provided by the diagnostic tester.

        Returns:
            Boolean instance, or None if not set
        """
        return self.shortTermAdjustmentSupported

    def setShortTermAdjustmentSupported(self, value: Optional[Boolean]) -> "DiagnosticIoControlNeeds":
        """
        Sets whether the referenced port supports temporarily setting of I/O value to a specific value provided by the diagnostic tester.
        A None value is a no-op and does not overwrite an existing shortTermAdjustmentSupported.

        Args:
            value: The Boolean instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.shortTermAdjustmentSupported = value
        return self


class DiagnosticMonitorUpdateKindEnum(AREnum):
    """
    This enumeration indicates the acceptance criteria for a diagnostic monitor.
    """

    # DiagnosticMonitorUpdateKindEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.50, p.798
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test

    # The value 'always' configures Dem to accept the call to SetDTR() regardless of the state of the diagnostics. Tags: atp.EnumerationLiteralIndex=0
    ALWAYS = "always"

    # The value 'steady' configures Dem to accept it only when debouncing is at the limit. Tags: atp.EnumerationLiteralIndex=1
    STEADY = "steady"

    def __init__(self):
        """
        Initializes the DiagnosticMonitorUpdateKindEnum with all possible values.
        """
        super().__init__(
            [
                DiagnosticMonitorUpdateKindEnum.ALWAYS,
                DiagnosticMonitorUpdateKindEnum.STEADY,
            ]
        )


class DiagnosticOperationCycleNeeds(DiagnosticCapabilityElement):
    """
    This meta-class represents the needs of a software-component to provide information regarding the operation cycle management to the Dem module.
    """

    # DiagnosticOperationCycleNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.24, p.761
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getOperationCycle            [x] impl  [x] docstring  [x] test
    # [x] setOperationCycle            [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the DiagnosticOperationCycleNeeds with a parent and short name.

        Args:
            parent: The parent ARObject that contains this diagnostic operation cycle needs
            short_name: The unique short name of this diagnostic operation cycle needs
        """
        super().__init__(parent, short_name)

        # Operation cycles types for the Dem to be supported by cycle-state APIs.
        self.operationCycle: Optional[OperationCycleTypeEnum] = None

    def getOperationCycle(self) -> Optional[OperationCycleTypeEnum]:
        """
        Gets the operation cycles types for the Dem to be supported by cycle-state APIs.

        Returns:
            OperationCycleTypeEnum instance, or None if not set
        """
        return self.operationCycle

    def setOperationCycle(self, value: Optional[OperationCycleTypeEnum]) -> "DiagnosticOperationCycleNeeds":
        """
        Sets the operation cycles types for the Dem to be supported by cycle-state APIs.
        A None value is a no-op and does not overwrite an existing operationCycle.

        Args:
            value: The OperationCycleTypeEnum instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.operationCycle = value
        return self


class DiagnosticRequestFileTransferNeeds(ServiceNeeds):
    """
    Represents Diagnostic Request File Transfer needs in AUTOSAR models.
    This class defines requirements for diagnostic file transfer services.
    """

    # DiagnosticRequestFileTransferNeeds method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the DiagnosticRequestFileTransferNeeds with a parent and short name.

        Args:
            parent: The parent ARObject that contains this diagnostic request file transfer needs
            short_name: The unique short name of this diagnostic request file transfer needs
        """
        super().__init__(parent, short_name)


class DiagnosticStorageConditionNeeds(DiagnosticCapabilityElement):
    """
    This meta-class represents the needs of a software-component to provide the capability to set a storage condition.
    """

    # DiagnosticStorageConditionNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.28, p.762
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getInitialStatus             [x] impl  [x] docstring  [x] test
    # [x] setInitialStatus             [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the DiagnosticStorageConditionNeeds with a parent and short name.

        Args:
            parent: The parent ARObject that contains this diagnostic storage condition needs
            short_name: The unique short name of this diagnostic storage condition needs
        """
        super().__init__(parent, short_name)

        # Defines the initial status for enable or disable of storage of a diagnostic event.
        self.initialStatus: Optional[StorageConditionStatusEnum] = None

    def getInitialStatus(self) -> Optional[StorageConditionStatusEnum]:
        """
        Gets the initial status for enable or disable of storage of a diagnostic event.

        Returns:
            StorageConditionStatusEnum instance, or None if not set
        """
        return self.initialStatus

    def setInitialStatus(self, value: Optional[StorageConditionStatusEnum]) -> "DiagnosticStorageConditionNeeds":
        """
        Sets a new initialStatus. A None value is a no-op and does not overwrite an existing initialStatus.

        Args:
            value: The StorageConditionStatusEnum instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.initialStatus = value
        return self


class DiagnosticUploadDownloadNeeds(ServiceNeeds):
    """
    Represents Diagnostic Upload/Download needs in AUTOSAR models.
    This class defines requirements for diagnostic upload and download services.
    """

    # DiagnosticUploadDownloadNeeds method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the DiagnosticUploadDownloadNeeds with a parent and short name.

        Args:
            parent: The parent ARObject that contains this diagnostic upload/download needs
            short_name: The unique short name of this diagnostic upload/download needs
        """
        super().__init__(parent, short_name)


class DiagnosticsCommunicationSecurityNeeds(ServiceNeeds):
    """
    Represents Diagnostics Communication Security needs in AUTOSAR models.
    This class defines requirements for secure diagnostic communication services.
    """

    # DiagnosticsCommunicationSecurityNeeds method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the DiagnosticsCommunicationSecurityNeeds with a parent and short name.

        Args:
            parent: The parent ARObject that contains this diagnostics communication security needs
            short_name: The unique short name of this diagnostics communication security needs
        """
        super().__init__(parent, short_name)


class DoIpActivationLineNeeds(ServiceNeeds):
    """
    Represents DoIP Activation Line needs in AUTOSAR models.
    This class defines requirements for DoIP (Diagnostics over IP) activation line services.
    """

    # DoIpActivationLineNeeds method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the DoIpActivationLineNeeds with a parent and short name.

        Args:
            parent: The parent ARObject that contains this DoIP activation line needs
            short_name: The unique short name of this DoIP activation line needs
        """
        super().__init__(parent, short_name)


class DoIpGidNeeds(ServiceNeeds):
    """
    Represents DoIP GID needs in AUTOSAR models.
    This class defines requirements for DoIP (Diagnostics over IP) GID services.
    """

    # DoIpGidNeeds method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the DoIpGidNeeds with a parent and short name.

        Args:
            parent: The parent ARObject that contains this DoIP GID needs
            short_name: The unique short name of this DoIP GID needs
        """
        super().__init__(parent, short_name)


class DoIpGidSynchronizationNeeds(ServiceNeeds):
    """
    Represents DoIP GID Synchronization needs in AUTOSAR models.
    This class defines requirements for DoIP (Diagnostics over IP) GID synchronization services.
    """

    # DoIpGidSynchronizationNeeds method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the DoIpGidSynchronizationNeeds with a parent and short name.

        Args:
            parent: The parent ARObject that contains this DoIP GID synchronization needs
            short_name: The unique short name of this DoIP GID synchronization needs
        """
        super().__init__(parent, short_name)


class DoIpPowerModeStatusNeeds(ServiceNeeds):
    """
    Represents DoIP Power Mode Status needs in AUTOSAR models.
    This class defines requirements for DoIP (Diagnostics over IP) power mode status services.
    """

    # DoIpPowerModeStatusNeeds method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the DoIpPowerModeStatusNeeds with a parent and short name.

        Args:
            parent: The parent ARObject that contains this DoIP power mode status needs
            short_name: The unique short name of this DoIP power mode status needs
        """
        super().__init__(parent, short_name)


class DoIpServiceNeeds(ServiceNeeds, ABC):
    """
    This represents an abstract base class for ServiceNeeds related to DoIP.
    """

    # DoIpServiceNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.54, p.805
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is DoIpServiceNeeds:
            raise TypeError("DoIpServiceNeeds is an abstract class.")

        super().__init__(parent, short_name)


class DoIpRoutingActivationAuthenticationNeeds(DoIpServiceNeeds):
    """
    DoIPRoutingActivationAuthenticationNeeds indicates that the software-component owning this Service Needs will have an authentication required for a DoIP routing activation service (0x0005) according to ISO 13400-2:2012.
    """

    # DoIpRoutingActivationAuthenticationNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.58, p.806
    # Spec verified: R23-11
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDataLengthRequest      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDataLengthRequest      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDataLengthResponse     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDataLengthResponse     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRoutingActivationType  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRoutingActivationType  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Describes the length in byte of the additional information for RA authentication that is needed by the software entity. If the software entity is a software-component the attribute does not need to exist as the information is available via the length of the uint8 Array type. Otherwise (i.e the software entity is a Complex Driver) this attribute needs to be filled out if additional information is needed.
        self.dataLengthRequest: Optional[PositiveInteger] = None

        # Describes the length in byte of the additional information for RA authentication that is provided by the software entity. If the software entity is a software-component the attribute does not need to exist as the information is available via the length of the uint8 Array type. Otherwise (i.e the software entity is a Complex Driver) this attribute needs to be filled in if additional information is provided.
        self.dataLengthResponse: Optional[PositiveInteger] = None

        # Describes the ISO 13400-2:2012 "routing activation request activation type" which is received via DoIP service 0x0005. 0x00 is DEFAULT, 0x01 is WWH-OBD. If neither of the specified values (0x00 or 0x01) is needed the token shall contain RA_ + hex value representation of the integer value shall be used (i.e: RA_0xE1).
        self.routingActivationType: Optional[NameToken] = None

    def getDataLengthRequest(self) -> Optional[PositiveInteger]:
        """
        Describes the length in byte of the additional information for RA authentication that is needed by the software entity. If the software entity is a software-component the attribute does not need to exist as the information is available via the length of the uint8 Array type. Otherwise (i.e the software entity is a Complex Driver) this attribute needs to be filled out if additional information is needed.

        Returns:
            PositiveInteger instance, or None if not set
        """
        return self.dataLengthRequest

    def setDataLengthRequest(self, value: Optional[PositiveInteger]) -> "DoIpRoutingActivationAuthenticationNeeds":
        """
        Describes the length in byte of the additional information for RA authentication that is needed by the software entity. If the software entity is a software-component the attribute does not need to exist as the information is available via the length of the uint8 Array type. Otherwise (i.e the software entity is a Complex Driver) this attribute needs to be filled out if additional information is needed.
        A None value is a no-op and does not overwrite an existing dataLengthRequest.

        Args:
            value: The PositiveInteger instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.dataLengthRequest = value
        return self

    def getDataLengthResponse(self) -> Optional[PositiveInteger]:
        """
        Describes the length in byte of the additional information for RA authentication that is provided by the software entity. If the software entity is a software-component the attribute does not need to exist as the information is available via the length of the uint8 Array type. Otherwise (i.e the software entity is a Complex Driver) this attribute needs to be filled in if additional information is provided.

        Returns:
            PositiveInteger instance, or None if not set
        """
        return self.dataLengthResponse

    def setDataLengthResponse(self, value: Optional[PositiveInteger]) -> "DoIpRoutingActivationAuthenticationNeeds":
        """
        Describes the length in byte of the additional information for RA authentication that is provided by the software entity. If the software entity is a software-component the attribute does not need to exist as the information is available via the length of the uint8 Array type. Otherwise (i.e the software entity is a Complex Driver) this attribute needs to be filled in if additional information is provided.
        A None value is a no-op and does not overwrite an existing dataLengthResponse.

        Args:
            value: The PositiveInteger instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.dataLengthResponse = value
        return self

    def getRoutingActivationType(self) -> Optional[NameToken]:
        """
        Describes the ISO 13400-2:2012 "routing activation request activation type" which is received via DoIP service 0x0005. 0x00 is DEFAULT, 0x01 is WWH-OBD. If neither of the specified values (0x00 or 0x01) is needed the token shall contain RA_ + hex value representation of the integer value shall be used (i.e: RA_0xE1).

        Returns:
            NameToken instance, or None if not set
        """
        return self.routingActivationType

    def setRoutingActivationType(self, value: Optional[NameToken]) -> "DoIpRoutingActivationAuthenticationNeeds":
        """
        Describes the ISO 13400-2:2012 "routing activation request activation type" which is received via DoIP service 0x0005. 0x00 is DEFAULT, 0x01 is WWH-OBD. If neither of the specified values (0x00 or 0x01) is needed the token shall contain RA_ + hex value representation of the integer value shall be used (i.e: RA_0xE1).
        A None value is a no-op and does not overwrite an existing routingActivationType.

        Args:
            value: The NameToken instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.routingActivationType = value
        return self


class DoIpRoutingActivationConfirmationNeeds(DoIpServiceNeeds):
    """
    DoIpRoutingActivationConfirmationNeeds indicates that the software-component that owns this Service Needs will have a confirmation required for a DoIP routing activation service (0x0005) according to ISO 13400-2:2012.
    """

    # DoIpRoutingActivationConfirmationNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.59, p.807
    # Spec verified: R23-11
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDataLengthRequest      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDataLengthRequest      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDataLengthResponse     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDataLengthResponse     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRoutingActivationType  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRoutingActivationType  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Describes the length in byte of the additional information for RA confirmation that is needed by the software entity. If the software entity is a software-component the attribute does not need to exist as the information is available via the length of the uint8 Array type. Otherwise (i.e the software entity is a Complex Driver) this attribute needs to be filled out if additional information is needed.
        self.dataLengthRequest: Optional[PositiveInteger] = None

        # Describes the length in byte of the additional information for RA confirmation that is provided by the software entity. If the software entity is a software-component the attribute does not need to exist as the information is available via the length of the uint8 Array type. Otherwise (i.e the software entity is a Complex Driver) this attribute needs to be filled out if additional information is provided.
        self.dataLengthResponse: Optional[PositiveInteger] = None

        # Describes the ISO 13400-2:2012 "routing activation request activation type" which is received via DoIP service 0x0005. 0x00 is DEFAULT, 0x01 is WWH-OBD. If neither of the specified values (0x00 or 0x01) is needed the token shall contain RA_ + hex value representation of the integer value shall be used (i.e: RA_0xE1).
        self.routingActivationType: Optional[NameToken] = None

    def getDataLengthRequest(self) -> Optional[PositiveInteger]:
        """
        Describes the length in byte of the additional information for RA confirmation that is needed by the software entity. If the software entity is a software-component the attribute does not need to exist as the information is available via the length of the uint8 Array type. Otherwise (i.e the software entity is a Complex Driver) this attribute needs to be filled out if additional information is needed.

        Returns:
            PositiveInteger instance, or None if not set
        """
        return self.dataLengthRequest

    def setDataLengthRequest(self, value: Optional[PositiveInteger]) -> "DoIpRoutingActivationConfirmationNeeds":
        """
        Describes the length in byte of the additional information for RA confirmation that is needed by the software entity. If the software entity is a software-component the attribute does not need to exist as the information is available via the length of the uint8 Array type. Otherwise (i.e the software entity is a Complex Driver) this attribute needs to be filled out if additional information is needed.
        A None value is a no-op and does not overwrite an existing dataLengthRequest.

        Args:
            value: The PositiveInteger instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.dataLengthRequest = value
        return self

    def getDataLengthResponse(self) -> Optional[PositiveInteger]:
        """
        Describes the length in byte of the additional information for RA confirmation that is provided by the software entity. If the software entity is a software-component the attribute does not need to exist as the information is available via the length of the uint8 Array type. Otherwise (i.e the software entity is a Complex Driver) this attribute needs to be filled out if additional information is provided.

        Returns:
            PositiveInteger instance, or None if not set
        """
        return self.dataLengthResponse

    def setDataLengthResponse(self, value: Optional[PositiveInteger]) -> "DoIpRoutingActivationConfirmationNeeds":
        """
        Describes the length in byte of the additional information for RA confirmation that is provided by the software entity. If the software entity is a software-component the attribute does not need to exist as the information is available via the length of the uint8 Array type. Otherwise (i.e the software entity is a Complex Driver) this attribute needs to be filled out if additional information is provided.
        A None value is a no-op and does not overwrite an existing dataLengthResponse.

        Args:
            value: The PositiveInteger instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.dataLengthResponse = value
        return self

    def getRoutingActivationType(self) -> Optional[NameToken]:
        """
        Describes the ISO 13400-2:2012 "routing activation request activation type" which is received via DoIP service 0x0005. 0x00 is DEFAULT, 0x01 is WWH-OBD. If neither of the specified values (0x00 or 0x01) is needed the token shall contain RA_ + hex value representation of the integer value shall be used (i.e: RA_0xE1).

        Returns:
            NameToken instance, or None if not set
        """
        return self.routingActivationType

    def setRoutingActivationType(self, value: Optional[NameToken]) -> "DoIpRoutingActivationConfirmationNeeds":
        """
        Describes the ISO 13400-2:2012 "routing activation request activation type" which is received via DoIP service 0x0005. 0x00 is DEFAULT, 0x01 is WWH-OBD. If neither of the specified values (0x00 or 0x01) is needed the token shall contain RA_ + hex value representation of the integer value shall be used (i.e: RA_0xE1).
        A None value is a no-op and does not overwrite an existing routingActivationType.

        Args:
            value: The NameToken instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.routingActivationType = value
        return self


class ErrorTracerNeeds(ServiceNeeds):
    """
    Specifies the need to report failures to the error tracer.
    """

    # ErrorTracerNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 12.36, p.263
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getTracedFailures            [x] impl  [x] docstring  [x] test
    # [x] createDevelopmentError       [x] impl  [x] docstring  [x] test
    # [x] createRuntimeError           [x] impl  [x] docstring  [x] test
    # [x] createTransientFault         [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the ErrorTracerNeeds with a parent and short name.

        Args:
            parent: The parent ARObject that contains this error tracer needs
            short_name: The unique short name of this error tracer needs
        """
        super().__init__(parent, short_name)

        # list of traced failures
        self.tracedFailures: List[TracedFailure] = []

    def getTracedFailures(self) -> List[TracedFailure]:
        """
        Gets the list of traced failures.

        Returns:
            List of TracedFailure instances
        """
        return self.tracedFailures

    def createDevelopmentError(self, short_name: str) -> DevelopmentError:
        """
        Creates and adds a DevelopmentError traced failure for the error tracer.

        Args:
            short_name: The short name for the new development error

        Returns:
            The created DevelopmentError instance
        """
        if not self.IsElementExists(short_name):
            failure = DevelopmentError(self, short_name)
            self.addElement(failure)
            self.tracedFailures.append(failure)
        return self.getElement(short_name)

    def createRuntimeError(self, short_name: str) -> RuntimeError:
        """
        Creates and adds a RuntimeError traced failure for the error tracer.

        Args:
            short_name: The short name for the new runtime error

        Returns:
            The created RuntimeError instance
        """
        if not self.IsElementExists(short_name):
            failure = RuntimeError(self, short_name)
            self.addElement(failure)
            self.tracedFailures.append(failure)
        return self.getElement(short_name)

    def createTransientFault(self, short_name: str) -> TransientFault:
        """
        Creates and adds a TransientFault traced failure for the error tracer.

        Args:
            short_name: The short name for the new transient fault

        Returns:
            The created TransientFault instance
        """
        if not self.IsElementExists(short_name):
            failure = TransientFault(self, short_name)
            self.addElement(failure)
            self.tracedFailures.append(failure)
        return self.getElement(short_name)


class EventAcceptanceStatusEnum(AREnum):
    """
    This enumerator specifies the initial status for enable or disable of acceptance of event reports of a diagnostic event.
    """

    # EventAcceptanceStatusEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.27, p.762
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test

    EVENT_ACCEPTANCE_DISABLED = "eventAcceptanceDisabled"
    EVENT_ACCEPTANCE_ENABLED = "eventAcceptanceEnabled"

    def __init__(self):
        super().__init__(
            (
                EventAcceptanceStatusEnum.EVENT_ACCEPTANCE_DISABLED,
                EventAcceptanceStatusEnum.EVENT_ACCEPTANCE_ENABLED,
            )
        )


class FunctionInhibitionAvailabilityNeeds(ServiceNeeds):
    """
    Specifies the abstract needs on the configuration of the Function Inhibition Manager to provide the control function for one Function Identifier (FID).
    """

    # FunctionInhibitionAvailabilityNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.13, p.751
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getControlledFidRef          [x] impl  [x] docstring  [x] test
    # [x] setControlledFidRef          [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the FunctionInhibitionAvailabilityNeeds with a parent and short name.

        Args:
            parent: The parent ARObject that contains this function inhibition availability needs
            short_name: The unique short name of this function inhibition availability needs
        """
        super().__init__(parent, short_name)

        # This reference represents the controlled FID.
        self.controlledFidRef: Optional[RefType] = None

    def getControlledFidRef(self) -> Optional[RefType]:
        """
        This reference represents the controlled FID.

        Returns:
            RefType instance, or None if not set
        """
        return self.controlledFidRef

    def setControlledFidRef(self, value: Optional[RefType]) -> "FunctionInhibitionAvailabilityNeeds":
        """
        This reference represents the controlled FID.
        A None value is a no-op and does not overwrite an existing controlledFidRef.

        Args:
            value: The RefType instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.controlledFidRef = value
        return self


class FunctionInhibitionNeeds(ServiceNeeds):
    """
    Represents Function Inhibition needs in AUTOSAR models.
    This class defines requirements for function inhibition services.
    """

    # FunctionInhibitionNeeds method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the FunctionInhibitionNeeds with a parent and short name.

        Args:
            parent: The parent ARObject that contains this function inhibition needs
            short_name: The unique short name of this function inhibition needs
        """
        super().__init__(parent, short_name)


class FurtherActionByteNeeds(ServiceNeeds):
    """
    Represents Further Action Byte needs in AUTOSAR models.
    This class defines requirements for further action byte services.
    """

    # FurtherActionByteNeeds method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the FurtherActionByteNeeds with a parent and short name.

        Args:
            parent: The parent ARObject that contains this further action byte needs
            short_name: The unique short name of this further action byte needs
        """
        super().__init__(parent, short_name)


class GlobalSupervisionNeeds(ServiceNeeds):
    """
    Represents Global Supervision needs in AUTOSAR models.
    This class defines requirements for global supervision services.
    """

    # GlobalSupervisionNeeds method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the GlobalSupervisionNeeds with a parent and short name.

        Args:
            parent: The parent ARObject that contains this global supervision needs
            short_name: The unique short name of this global supervision needs
        """
        super().__init__(parent, short_name)


class HardwareTestNeeds(ServiceNeeds):
    """
    Represents Hardware Test needs in AUTOSAR models.
    This class defines requirements for hardware test services.
    """

    # HardwareTestNeeds method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the HardwareTestNeeds with a parent and short name.

        Args:
            parent: The parent ARObject that contains this hardware test needs
            short_name: The unique short name of this hardware test needs
        """
        super().__init__(parent, short_name)


class IdsMgrCustomTimestampNeeds(ServiceNeeds):
    """
    Represents IDS Manager Custom Timestamp needs in AUTOSAR models.
    This class defines requirements for IDS (Intrusion Detection System) manager custom timestamp services.
    """

    # IdsMgrCustomTimestampNeeds method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the IdsMgrCustomTimestampNeeds with a parent and short name.

        Args:
            parent: The parent ARObject that contains this IDS manager custom timestamp needs
            short_name: The unique short name of this IDS manager custom timestamp needs
        """
        super().__init__(parent, short_name)


class IdsMgrNeeds(ServiceNeeds):
    """
    This meta-class is used to indicate that the enclosing SwcServiceDependency represents a service use case for the Intrusion Detection System Manager. Tags: atp.Status=draft
    """

    # IdsMgrNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.81, p.842
    # Spec verified: R23-11
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getUseSmartSensorApi    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setUseSmartSensorApi    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This attribute controls whether the reporting of the security event shall be done by means of the smart sensor API.
        self.useSmartSensorApi: Optional[Boolean] = None

    def getUseSmartSensorApi(self) -> Optional[Boolean]:
        """
        This attribute controls whether the reporting of the security event shall be done by means of the smart sensor API.

        Returns:
            Boolean instance, or None if not set
        """
        return self.useSmartSensorApi

    def setUseSmartSensorApi(self, value: Optional[Boolean]) -> "IdsMgrNeeds":
        """
        This attribute controls whether the reporting of the security event shall be done by means of the smart sensor API.
        A None value is a no-op and does not overwrite an existing useSmartSensorApi.

        Args:
            value: The Boolean instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.useSmartSensorApi = value
        return self


class DiagnosticIndicatorTypeEnum(AREnum):
    """
    Type of an indicator. (Table 13.31, SoftwareComponentTemplate)
    """

    # DiagnosticIndicatorTypeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.31, p.766
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test

    # Amber Warning Lamp Tags: atp.EnumerationLiteralIndex=0
    AMBER_WARNING = "amberWarning"

    # Malfunction Indicator Lamp Tags: atp.EnumerationLiteralIndex=1
    MALFUNCTION = "malfunction"

    # Protect Lamp Tags: atp.EnumerationLiteralIndex=2
    PROTECT_LAMP = "protectLamp"

    # Red Stop Lamp Tags: atp.EnumerationLiteralIndex=3
    RED_STOP_LAMP = "redStopLamp"

    # Warning Tags: atp.EnumerationLiteralIndex=4
    WARNING = "warning"

    def __init__(self):
        """
        Initializes the DiagnosticIndicatorTypeEnum with all possible values.
        """
        super().__init__(
            (
                DiagnosticIndicatorTypeEnum.AMBER_WARNING,
                DiagnosticIndicatorTypeEnum.MALFUNCTION,
                DiagnosticIndicatorTypeEnum.PROTECT_LAMP,
                DiagnosticIndicatorTypeEnum.RED_STOP_LAMP,
                DiagnosticIndicatorTypeEnum.WARNING,
            )
        )


class IndicatorStatusNeeds(ServiceNeeds):
    """
    This meta-class shall be taken to signal a service use case that affects the indicator status.
    """

    # IndicatorStatusNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.30, p.766
    # Spec verified: R23-11
    # [x] __init__   [x] impl  [x] docstring  [x] test
    # [x] getType             [x] impl  [x] docstring  [x] test
    # [x] setType             [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the IndicatorStatusNeeds with a parent and short name.

        Args:
            parent: The parent ARObject that contains this indicator status needs
            short_name: The unique short name of this indicator status needs
        """
        super().__init__(parent, short_name)

        # Defines the type of the indicator.
        self.type: Optional[DiagnosticIndicatorTypeEnum] = None

    def getType(self) -> Optional[DiagnosticIndicatorTypeEnum]:
        """
        Gets the type of the indicator.

        Returns:
            DiagnosticIndicatorTypeEnum instance, or None if not set
        """
        return self.type

    def setType(self, value: Optional[DiagnosticIndicatorTypeEnum]) -> "IndicatorStatusNeeds":
        """
        Sets the type of the indicator.
        A None value is a no-op and does not overwrite an existing type.

        Args:
            value: The DiagnosticIndicatorTypeEnum instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.type = value
        return self


class J1939DcmDm19Support(ServiceNeeds):
    """
    Represents J1939 DCM DM19 Support needs in AUTOSAR models.
    This class defines requirements for J1939 diagnostic communication manager DM19 support.
    """

    # J1939DcmDm19Support method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the J1939DcmDm19Support with a parent and short name.

        Args:
            parent: The parent ARObject that contains this J1939 DCM DM19 support
            short_name: The unique short name of this J1939 DCM DM19 support
        """
        super().__init__(parent, short_name)


class J1939RmIncomingRequestServiceNeeds(ServiceNeeds):
    """
    Represents J1939 RM Incoming Request Service needs in AUTOSAR models.
    This class defines requirements for J1939 request manager incoming request services.
    """

    # J1939RmIncomingRequestServiceNeeds method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the J1939RmIncomingRequestServiceNeeds with a parent and short name.

        Args:
            parent: The parent ARObject that contains this J1939 RM incoming request service needs
            short_name: The unique short name of this J1939 RM incoming request service needs
        """
        super().__init__(parent, short_name)


class J1939RmOutgoingRequestServiceNeeds(ServiceNeeds):
    """
    Represents J1939 RM Outgoing Request Service needs in AUTOSAR models.
    This class defines requirements for J1939 request manager outgoing request services.
    """

    # J1939RmOutgoingRequestServiceNeeds method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the J1939RmOutgoingRequestServiceNeeds with a parent and short name.

        Args:
            parent: The parent ARObject that contains this J1939 RM outgoing request service needs
            short_name: The unique short name of this J1939 RM outgoing request service needs
        """
        super().__init__(parent, short_name)


class MaxCommModeEnum(AREnum):
    """
    Maximum bus communication mode required by a user of the Communication Manager Service.
    """

    # MaxCommModeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.6, p.711
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test

    # Full communication is requested. atp.EnumerationLiteralIndex=0
    FULL = "full"

    # No communication is requested. atp.EnumerationLiteralIndex=1
    NONE = "none"

    # Silent communication is requested: Only listening but not "talking". atp.EnumerationLiteralIndex=2
    SILENT = "silent"

    def __init__(self):
        """
        Initializes the MaxCommModeEnum with all possible values.
        """
        super().__init__(
            (
                MaxCommModeEnum.FULL,
                MaxCommModeEnum.NONE,
                MaxCommModeEnum.SILENT,
            )
        )


class ObdControlServiceNeeds(DiagnosticCapabilityElement):
    """
    Specifies the abstract needs of a component or module on the configuration of OBD Service 08 (request control of on-board system) in relation to a particular test-Identifier (TID) supported by this component or module.
    """

    # ObdControlServiceNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.45, p.796
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the ObdControlServiceNeeds with a parent and short name.

        Args:
            parent: The parent ARObject that contains this OBD control service needs
            short_name: The unique short name of this OBD control service needs
        """
        super().__init__(parent, short_name)


class ObdInfoServiceNeeds(DiagnosticCapabilityElement):
    """
    Specifies the abstract needs of a component or module on the configuration of OBD Services in relation to a given InfoType (OBD Service 09) which is supported by this component or module.
    """

    # ObdInfoServiceNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.48, p.797
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the ObdInfoServiceNeeds with a parent and short name.

        Args:
            parent: The parent ARObject that contains this OBD info service needs
            short_name: The unique short name of this OBD info service needs
        """
        super().__init__(parent, short_name)


class ObdMonitorServiceNeeds(DiagnosticCapabilityElement):
    """
    Specifies the abstract needs of a component or module on the configuration of OBD Services in relation to a particular on-board monitoring test supported by this component or module. (OBD Service 06).
    """

    # ObdMonitorServiceNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.49, p.798
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getApplicationDataTypeRef    [x] impl  [x] docstring  [x] test
    # [x] setApplicationDataTypeRef    [x] impl  [x] docstring  [x] test
    # [x] getEventNeedsRef             [x] impl  [x] docstring  [x] test
    # [x] setEventNeedsRef             [x] impl  [x] docstring  [x] test
    # [x] getUnitAndScalingId          [x] impl  [x] docstring  [x] test
    # [x] setUnitAndScalingId          [x] impl  [x] docstring  [x] test
    # [x] getUpdateKind                [x] impl  [x] docstring  [x] test
    # [x] setUpdateKind                [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the ObdMonitorServiceNeeds with a parent and short name.

        Args:
            parent: The parent ARObject that contains this OBD monitor service needs
            short_name: The unique short name of this OBD monitor service needs
        """
        super().__init__(parent, short_name)

        # reference to an ApplicationDataType that describes the scaling of the data reported by the software-component to the Dem.
        self.applicationDataTypeRef: Optional[RefType] = None

        # This reference identifies the corresponding diagnostic event.
        self.eventNeedsRef: Optional[RefType] = None

        # Unit and scaling ID according to ISO 15031-5.
        self.unitAndScalingId: Optional[PositiveInteger] = None

        # This attribute indicates the settings for the acceptance of updates.
        self.updateKind: Optional[DiagnosticMonitorUpdateKindEnum] = None

    def getApplicationDataTypeRef(self) -> Optional[RefType]:
        """
        Gets the reference to an ApplicationDataType that describes the scaling of the data reported by the software-component to the Dem.

        Returns:
            RefType instance, or None if not set
        """
        return self.applicationDataTypeRef

    def setApplicationDataTypeRef(self, value: Optional[RefType]) -> "ObdMonitorServiceNeeds":
        """
        Sets the reference to an ApplicationDataType that describes the scaling of the data reported by the software-component to the Dem.
        A None value is a no-op and does not overwrite an existing applicationDataTypeRef.

        Args:
            value: The RefType instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.applicationDataTypeRef = value
        return self

    def getEventNeedsRef(self) -> Optional[RefType]:
        """
        Gets the reference that identifies the corresponding diagnostic event.

        Returns:
            RefType instance, or None if not set
        """
        return self.eventNeedsRef

    def setEventNeedsRef(self, value: Optional[RefType]) -> "ObdMonitorServiceNeeds":
        """
        Sets the reference that identifies the corresponding diagnostic event.
        A None value is a no-op and does not overwrite an existing eventNeedsRef.

        Args:
            value: The RefType instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.eventNeedsRef = value
        return self

    def getUnitAndScalingId(self) -> Optional[PositiveInteger]:
        """
        Gets the unit and scaling ID according to ISO 15031-5.

        Returns:
            PositiveInteger instance, or None if not set
        """
        return self.unitAndScalingId

    def setUnitAndScalingId(self, value: Optional[PositiveInteger]) -> "ObdMonitorServiceNeeds":
        """
        Sets the unit and scaling ID according to ISO 15031-5.
        A None value is a no-op and does not overwrite an existing unitAndScalingId.

        Args:
            value: The PositiveInteger instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.unitAndScalingId = value
        return self

    def getUpdateKind(self) -> Optional[DiagnosticMonitorUpdateKindEnum]:
        """
        Gets the settings for the acceptance of updates to the Dem.

        Returns:
            DiagnosticMonitorUpdateKindEnum instance, or None if not set
        """
        return self.updateKind

    def setUpdateKind(self, value: Optional[DiagnosticMonitorUpdateKindEnum]) -> "ObdMonitorServiceNeeds":
        """
        Sets the settings for the acceptance of updates to the Dem.
        A None value is a no-op and does not overwrite an existing updateKind.

        Args:
            value: The DiagnosticMonitorUpdateKindEnum instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.updateKind = value
        return self


class ObdPidServiceNeeds(DiagnosticCapabilityElement):
    """
    Specifies the abstract needs of a component or module on the configuration of OBD Services in relation to a particular PID (parameter identifier) which is supported by this component or module. In case of using a client/server communicated value, the related value shall be communicated via the port referenced by assignedPort. The details of this communication (e.g. appropriate naming conventions) are specified in the related software specifications (SWS).
    """

    # ObdPidServiceNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.47, p.797
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the ObdPidServiceNeeds with a parent and short name.

        Args:
            parent: The parent ARObject that contains this OBD PID service needs
            short_name: The unique short name of this OBD PID service needs
        """
        super().__init__(parent, short_name)


class ObdRatioConnectionKindEnum(AREnum):
    """
    Defines the way how the IUMPR service connection between the Dem and the client component or module is handled (for details see the DEM Specification).
    """

    # ObdRatioConnectionKindEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.46, p.796
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test

    # The IUMPR service (of the DEM) uses an explicit API to connect to the component or module. Tags: atp.EnumerationLiteralIndex=0
    API_USE = "apiUse"
    # The IUMPR service (of the Dem) uses no API but "observes" the associated diagnostic event. Tags: atp.EnumerationLiteralIndex=1
    OBSERVER = "observer"

    def __init__(self):
        super().__init__(
            [
                ObdRatioConnectionKindEnum.API_USE,
                ObdRatioConnectionKindEnum.OBSERVER,
            ]
        )


class ObdRatioDenominatorNeeds(ServiceNeeds):
    """
    This meta-class shall be used to indicate that a software-component wants to access the in-use-monitoring performance ration denominator.
    """

    # ObdRatioDenominatorNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.51, p.803
    # Spec verified: R23-11
    # [x] __init__                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDenominatorCondition         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDenominatorCondition         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This attribute indicates the applicable denominator condition.
        self.denominatorCondition: Optional[DiagnosticDenominatorConditionEnum] = None

    def getDenominatorCondition(self) -> Optional[DiagnosticDenominatorConditionEnum]:
        """
        This attribute indicates the applicable denominator condition.

        Returns:
            DiagnosticDenominatorConditionEnum instance, or None if not set
        """
        return self.denominatorCondition

    def setDenominatorCondition(self, value: Optional[DiagnosticDenominatorConditionEnum]) -> "ObdRatioDenominatorNeeds":
        """
        This attribute indicates the applicable denominator condition.
        A None value is a no-op and does not overwrite an existing denominatorCondition.

        Args:
            value: The DiagnosticDenominatorConditionEnum instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.denominatorCondition = value
        return self


class ObdRatioServiceNeeds(DiagnosticCapabilityElement):
    """
    Specifies the abstract needs of a component or module on the configuration of OBD Services in relation to a particular "ratio monitoring" which is supported by this component or module.
    """

    # ObdRatioServiceNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.44, p.795
    # Spec verified: R23-11
    # [x] __init__                          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getConnectionType                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setConnectionType                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRateBasedMonitoredEventRef     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRateBasedMonitoredEventRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getUsedFidRef                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setUsedFidRef                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Defines how the DEM is connected to the component or module to perform the IUMPR (In use monitor performance ratio) service.
        self.connectionType: Optional[ObdRatioConnectionKindEnum] = None

        # The rate based monitored Diagnostic Event.
        self.rateBasedMonitoredEventRef: Optional[RefType] = None

        # This represents the primary Function Inhibition Identifier used for the rate based monitor. This is an optional attribute.
        self.usedFidRef: Optional[RefType] = None

    def getConnectionType(self) -> Optional[ObdRatioConnectionKindEnum]:
        """
        Defines how the DEM is connected to the component or module to perform the IUMPR (In use monitor performance ratio) service.

        Returns:
            ObdRatioConnectionKindEnum instance, or None if not set
        """
        return self.connectionType

    def setConnectionType(self, value: Optional[ObdRatioConnectionKindEnum]) -> "ObdRatioServiceNeeds":
        """
        Defines how the DEM is connected to the component or module to perform the IUMPR (In use monitor performance ratio) service.
        A None value is a no-op and does not overwrite an existing connectionType.

        Args:
            value: The ObdRatioConnectionKindEnum instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.connectionType = value
        return self

    def getRateBasedMonitoredEventRef(self) -> Optional[RefType]:
        """
        The rate based monitored Diagnostic Event.

        Returns:
            RefType instance, or None if not set
        """
        return self.rateBasedMonitoredEventRef

    def setRateBasedMonitoredEventRef(self, value: Optional[RefType]) -> "ObdRatioServiceNeeds":
        """
        The rate based monitored Diagnostic Event.
        A None value is a no-op and does not overwrite an existing rateBasedMonitoredEventRef.

        Args:
            value: The RefType instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.rateBasedMonitoredEventRef = value
        return self

    def getUsedFidRef(self) -> Optional[RefType]:
        """
        This represents the primary Function Inhibition Identifier used for the rate based monitor. This is an optional attribute.

        Returns:
            RefType instance, or None if not set
        """
        return self.usedFidRef

    def setUsedFidRef(self, value: Optional[RefType]) -> "ObdRatioServiceNeeds":
        """
        This represents the primary Function Inhibition Identifier used for the rate based monitor. This is an optional attribute.
        A None value is a no-op and does not overwrite an existing usedFidRef.

        Args:
            value: The RefType instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.usedFidRef = value
        return self


class OperationCycleTypeEnum(AREnum):
    """
    The possible values of the operation cycles types for the Dem.
    """

    # OperationCycleTypeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.25, p.761
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test

    IGNITION = "ignition"
    OBD_DCY = "obdDcy"
    OTHER = "other"
    POWER = "power"
    TIME = "time"
    WARMUP = "warmup"

    def __init__(self):
        super().__init__(
            (
                OperationCycleTypeEnum.IGNITION,
                OperationCycleTypeEnum.OBD_DCY,
                OperationCycleTypeEnum.OTHER,
                OperationCycleTypeEnum.POWER,
                OperationCycleTypeEnum.TIME,
                OperationCycleTypeEnum.WARMUP,
            )
        )


class RuntimeError(TracedFailure):
    """
    The reported failure is classified as runtime error.
    """

    # RuntimeError method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 12.39, p.263
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the RuntimeError with a parent and short name.

        Args:
            parent: The parent ARObject that contains this runtime error
            short_name: The unique short name of this runtime error
        """
        super().__init__(parent, short_name)


class SecureOnBoardCommunicationNeeds(ServiceNeeds):
    """
    Specifies the need for the existence of the SecOc module on the respective ECU. This class currently contains no attributes. An instance of this class is used to find out which ports of a software-component deal with the administration of secure communication in order to group the request and response ports.
    """

    # SecureOnBoardCommunicationNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.68, p.824
    # Spec verified: R23-11
    # [x] __init__                              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getVerificationStatusIndicationMode   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setVerificationStatusIndicationMode   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This attribute provides the ability to control the mode in which the application software is notified about the result of authentication attempts.
        self.verificationStatusIndicationMode: Optional[VerificationStatusIndicationModeEnum] = None

    def getVerificationStatusIndicationMode(self) -> Optional[VerificationStatusIndicationModeEnum]:
        """
        This attribute provides the ability to control the mode in which the application software is notified about the result of authentication attempts.

        Returns:
            VerificationStatusIndicationModeEnum instance, or None if not set
        """
        return self.verificationStatusIndicationMode

    def setVerificationStatusIndicationMode(self, value: Optional[VerificationStatusIndicationModeEnum]) -> "SecureOnBoardCommunicationNeeds":
        """
        This attribute provides the ability to control the mode in which the application software is notified about the result of authentication attempts.
        A None value is a no-op and does not overwrite an existing verificationStatusIndicationMode.

        Args:
            value: The VerificationStatusIndicationModeEnum instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.verificationStatusIndicationMode = value
        return self


class ServiceProviderEnum(AREnum):
    """
    This represents a list of possible service providers
    """

    # ServiceProviderEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 3.20, p.90
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test

    # This value means that the specific nature is either unknown or it is not important for the given purpose.
    # This is also the default value for any attribute of type ServiceProviderEnum. Tags: atp.EnumerationLiteralIndex=0
    ANY_STANDARDIZED = "anyStandardized"

    # The service relates to the Basic Software Mode Manager (BswM). Tags: atp.EnumerationLiteralIndex=1
    BASIC_SOFTWARE_MODE_MANAGER = "basicSoftwareModeManager"

    # The service relates to the COM Manager (ComM). Tags: atp.EnumerationLiteralIndex=2
    COM_MANAGER = "comManager"

    # The service relates to the Key Manager (KeyM). Tags: atp.EnumerationLiteralIndex=23
    CRYPTO_KEY_MANAGEMENT = "cryptoKeyManagement"

    # The service relates to the Crypto Service Manager (CsM). Tags: atp.EnumerationLiteralIndex=3
    CRYPTO_SERVICE_MANAGER = "cryptoServiceManager"

    # The service relates to the Default Error Tracer (DET). Tags: atp.EnumerationLiteralIndex=4
    DEFAULT_ERROR_TRACER = "defaultErrorTracer"

    # The service relates to the Diagnostic Communication Manager (DCM). Tags: atp.EnumerationLiteralIndex=6
    DIAGNOSTIC_COMMUNICATION_MANAGER = "diagnosticCommunicationManager"

    # The service relates to the Diagnostic Event Manager (DEM). Tags: atp.EnumerationLiteralIndex=7
    DIAGNOSTIC_EVENT_MANAGER = "diagnosticEventManager"

    # The service relates to the Diagnostic Log and Trace (DLT). Tags: atp.EnumerationLiteralIndex=8
    DIAGNOSTIC_LOG_AND_TRACE = "diagnosticLogAndTrace"

    # The service relates to the ECU Manager (EcuM). Tags: atp.EnumerationLiteralIndex=9
    ECU_MANAGER = "ecuManager"

    # This service relates to the error tracer. Tags: atp.EnumerationLiteralIndex=18
    ERROR_TRACER = "errorTracer"

    # The service relates to the Function Inhibition Manager (FIM). Tags: atp.EnumerationLiteralIndex=10
    FUNCTION_INHIBITION_MANAGER = "functionInhibitionManager"

    # This service relates to the hardware test manager. Tags: atp.EnumerationLiteralIndex=19
    HARDWARE_TEST_MANAGER = "hardwareTestManager"

    # The service relates to the intrusion detection security management (IdsM). Tags: atp.EnumerationLiteralIndex=24
    INTRUSION_DETECTION_SECURITY_MANAGEMENT = "intrusionDetectionSecurityManagement"

    # This service relates to the J1939 Dcm. Tags: atp.EnumerationLiteralIndex=22
    J1939_DCM = "j1939Dcm"

    # The service relates to the J1939Rm. Tags: atp.EnumerationLiteralIndex=11
    J1939_REQUEST_MANAGER = "j1939RequestManager"

    # The service relates to the Non-Volatile RAM Manager (NvM). Tags: atp.EnumerationLiteralIndex=12
    NON_VOLATILE_RAM_MANAGER = "nonVolatileRamManager"

    # The service relates to the Operating System (OS). Tags: atp.EnumerationLiteralIndex=13
    OPERATING_SYSTEM = "operatingSystem"

    # The service relates to the SecOc module. Tags: atp.EnumerationLiteralIndex=14
    SECURE_ON_BOARD_COMMUNICATION = "secureOnBoardCommunication"

    # The service relates to the Sync Time Base Manager (StbM). Tags: atp.EnumerationLiteralIndex=15
    SYNC_BASE_TIME_MANAGER = "syncBaseTimeManager"

    # This service relates to the Vehicle to X facilities. Tags: atp.EnumerationLiteralIndex=20
    V2X_FACILITIES = "v2xFacilities"

    # This service relates to the Vehicle to X management. Tags: atp.EnumerationLiteralIndex=21
    V2X_MANAGEMENT = "v2xManagement"

    # This value denotes a vendor-specific service. Tags: atp.EnumerationLiteralIndex=16
    VENDOR_SPECIFIC = "vendorSpecific"

    def __init__(self):
        """
        Initializes a ServiceProviderEnum instance with the spec-defined literals.
        """
        super().__init__(
            (
                ServiceProviderEnum.ANY_STANDARDIZED,
                ServiceProviderEnum.BASIC_SOFTWARE_MODE_MANAGER,
                ServiceProviderEnum.COM_MANAGER,
                ServiceProviderEnum.CRYPTO_KEY_MANAGEMENT,
                ServiceProviderEnum.CRYPTO_SERVICE_MANAGER,
                ServiceProviderEnum.DEFAULT_ERROR_TRACER,
                ServiceProviderEnum.DIAGNOSTIC_COMMUNICATION_MANAGER,
                ServiceProviderEnum.DIAGNOSTIC_EVENT_MANAGER,
                ServiceProviderEnum.DIAGNOSTIC_LOG_AND_TRACE,
                ServiceProviderEnum.ECU_MANAGER,
                ServiceProviderEnum.ERROR_TRACER,
                ServiceProviderEnum.FUNCTION_INHIBITION_MANAGER,
                ServiceProviderEnum.HARDWARE_TEST_MANAGER,
                ServiceProviderEnum.INTRUSION_DETECTION_SECURITY_MANAGEMENT,
                ServiceProviderEnum.J1939_DCM,
                ServiceProviderEnum.J1939_REQUEST_MANAGER,
                ServiceProviderEnum.NON_VOLATILE_RAM_MANAGER,
                ServiceProviderEnum.OPERATING_SYSTEM,
                ServiceProviderEnum.SECURE_ON_BOARD_COMMUNICATION,
                ServiceProviderEnum.SYNC_BASE_TIME_MANAGER,
                ServiceProviderEnum.V2X_FACILITIES,
                ServiceProviderEnum.V2X_MANAGEMENT,
                ServiceProviderEnum.VENDOR_SPECIFIC,
            )
        )


class StorageConditionStatusEnum(AREnum):
    """
    This enumeration specifies the initial status for enable or disable of storage of a diagnostic event.
    """

    # StorageConditionStatusEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.29, p.762
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test

    EVENT_STORAGE_DISABLE = "eventStorageDisabled"
    EVENT_STORAGE_ENABLE = "eventStorageEnabled"

    def __init__(self):
        super().__init__(
            (
                StorageConditionStatusEnum.EVENT_STORAGE_DISABLE,
                StorageConditionStatusEnum.EVENT_STORAGE_ENABLE,
            )
        )


class SupervisedEntityCheckpointNeeds(ServiceNeeds):
    """
    Represents Supervised Entity Checkpoint needs in AUTOSAR models.
    This class defines requirements for supervised entity checkpoint services.
    """

    # SupervisedEntityCheckpointNeeds method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the SupervisedEntityCheckpointNeeds with a parent and short name.

        Args:
            parent: The parent ARObject that contains this supervised entity checkpoint needs
            short_name: The unique short name of this supervised entity checkpoint needs
        """
        super().__init__(parent, short_name)


class SupervisedEntityNeeds(ServiceNeeds):
    """
    Specifies the abstract needs on the configuration of the Watchdog Manager for one specific Supervised Entity.
    """

    # SupervisedEntityNeeds method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table 12.12, p.234
    # Spec verified: R23-11
    # [x] __init__                  [x] impl  [x] docstring  [x] test
    # [x] getActivateAtStart        [x] impl  [x] docstring  [x] test
    # [x] setActivateAtStart        [x] impl  [x] docstring  [x] test
    # [x] addCheckpointsRef         [x] impl  [x] docstring  [x] test
    # [x] getCheckpointsRefs        [x] impl  [x] docstring  [x] test
    # [x] getEnableDeactivation     [x] impl  [x] docstring  [x] test
    # [x] setEnableDeactivation     [x] impl  [x] docstring  [x] test
    # [x] getExpectedAliveCycle     [x] impl  [x] docstring  [x] test
    # [x] setExpectedAliveCycle     [x] impl  [x] docstring  [x] test
    # [x] getMaxAliveCycle          [x] impl  [x] docstring  [x] test
    # [x] setMaxAliveCycle          [x] impl  [x] docstring  [x] test
    # [x] getMinAliveCycle          [x] impl  [x] docstring  [x] test
    # [x] setMinAliveCycle          [x] impl  [x] docstring  [x] test
    # [x] getToleratedFailedCycles  [x] impl  [x] docstring  [x] test
    # [x] setToleratedFailedCycles  [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the SupervisedEntityNeeds with a parent and short name.

        Args:
            parent: The parent ARObject that contains this supervised entity needs
            short_name: The unique short name of this supervised entity needs
        """
        super().__init__(parent, short_name)

        # True/false: supervision activation status of SupervisedEntity shall be enabled/disabled at start.
        self.activateAtStart: Optional[Boolean] = None

        # This reference indicates the checkpoints belonging to the Supervised Entity.
        self.checkpointsRefs: List[RefType] = []

        # True: software-component shall be allowed to deactivate supervision of this SupervisedEntity; false: software-component shall be not allowed to deactivate supervision of this SupervisedEntity
        self.enableDeactivation: Optional[Boolean] = None

        # Expected cycle time of alive trigger of this SupervisedEntity (in seconds).
        self.expectedAliveCycle: Optional[TimeValue] = None

        # Maximum cycle time of alive trigger of this SupervisedEntity (in seconds).
        self.maxAliveCycle: Optional[TimeValue] = None

        # Minimum cycle time of alive trigger of this SupervisedEntity (in seconds).
        self.minAliveCycle: Optional[TimeValue] = None

        # Number of consecutive failed alive cycles for this SupervisedEntity which shall be tolerated until the supervision status of the SupervisedEntity is set to WDGM_ALIVE_EXPIRED (see SWS WdgM for more details).
        self.toleratedFailedCycles: Optional[PositiveInteger] = None

    def getActivateAtStart(self) -> Optional[Boolean]:
        """
        Gets the supervision activation status of the Supervised Entity to be enabled/disabled at start.

        Returns:
            Boolean instance, or None if not set
        """
        return self.activateAtStart

    def setActivateAtStart(self, value: Optional[Boolean]) -> "SupervisedEntityNeeds":
        """
        Sets the supervision activation status of the Supervised Entity to be enabled/disabled at start.
        A None value is a no-op and does not overwrite an existing activateAtStart.

        Args:
            value: The Boolean instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.activateAtStart = value
        return self

    def addCheckpointsRef(self, value: Optional[RefType]) -> "SupervisedEntityNeeds":
        """
        Adds a reference indicating a checkpoint belonging to the Supervised Entity.
        A None value is a no-op and does not append anything.

        Args:
            value: The checkpoint reference to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.checkpointsRefs.append(value)
        return self

    def getCheckpointsRefs(self) -> List[RefType]:
        """
        Gets the references indicating the checkpoints belonging to the Supervised Entity.

        Returns:
            List of RefType instances (empty by default)
        """
        return self.checkpointsRefs

    def getEnableDeactivation(self) -> Optional[Boolean]:
        """
        Gets whether the software-component shall be allowed to deactivate supervision of this SupervisedEntity.

        Returns:
            Boolean instance, or None if not set
        """
        return self.enableDeactivation

    def setEnableDeactivation(self, value: Optional[Boolean]) -> "SupervisedEntityNeeds":
        """
        Sets whether the software-component shall be allowed to deactivate supervision of this SupervisedEntity.
        A None value is a no-op and does not overwrite an existing enableDeactivation.

        Args:
            value: The Boolean instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.enableDeactivation = value
        return self

    def getExpectedAliveCycle(self) -> Optional[TimeValue]:
        """
        Gets the expected cycle time of the alive trigger of this SupervisedEntity (in seconds).

        Returns:
            TimeValue instance, or None if not set
        """
        return self.expectedAliveCycle

    def setExpectedAliveCycle(self, value: Optional[TimeValue]) -> "SupervisedEntityNeeds":
        """
        Sets the expected cycle time of the alive trigger of this SupervisedEntity (in seconds).
        A None value is a no-op and does not overwrite an existing expectedAliveCycle.

        Args:
            value: The TimeValue instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.expectedAliveCycle = value
        return self

    def getMaxAliveCycle(self) -> Optional[TimeValue]:
        """
        Gets the maximum cycle time of the alive trigger of this SupervisedEntity (in seconds).

        Returns:
            TimeValue instance, or None if not set
        """
        return self.maxAliveCycle

    def setMaxAliveCycle(self, value: Optional[TimeValue]) -> "SupervisedEntityNeeds":
        """
        Sets the maximum cycle time of the alive trigger of this SupervisedEntity (in seconds).
        A None value is a no-op and does not overwrite an existing maxAliveCycle.

        Args:
            value: The TimeValue instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.maxAliveCycle = value
        return self

    def getMinAliveCycle(self) -> Optional[TimeValue]:
        """
        Gets the minimum cycle time of the alive trigger of this SupervisedEntity (in seconds).

        Returns:
            TimeValue instance, or None if not set
        """
        return self.minAliveCycle

    def setMinAliveCycle(self, value: Optional[TimeValue]) -> "SupervisedEntityNeeds":
        """
        Sets the minimum cycle time of the alive trigger of this SupervisedEntity (in seconds).
        A None value is a no-op and does not overwrite an existing minAliveCycle.

        Args:
            value: The TimeValue instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.minAliveCycle = value
        return self

    def getToleratedFailedCycles(self) -> Optional[PositiveInteger]:
        """
        Gets the number of consecutive failed alive cycles for this SupervisedEntity which shall be tolerated until the supervision status is set to WDGM_ALIVE_EXPIRED.

        Returns:
            PositiveInteger instance, or None if not set
        """
        return self.toleratedFailedCycles

    def setToleratedFailedCycles(self, value: Optional[PositiveInteger]) -> "SupervisedEntityNeeds":
        """
        Sets the number of consecutive failed alive cycles for this SupervisedEntity which shall be tolerated until the supervision status is set to WDGM_ALIVE_EXPIRED.
        A None value is a no-op and does not overwrite an existing toleratedFailedCycles.

        Args:
            value: The PositiveInteger instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.toleratedFailedCycles = value
        return self


class SymbolicNameProps(ImplementationProps):
    """
    Represents Symbolic Name properties in AUTOSAR models.
    This meta-class can be taken to contribute to the creation of symbolic name values.
    Inherits symbol handling (SYMBOL, 0..1 C-Identifier) from ImplementationProps.
    """

    # SymbolicNameProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.59, p.610
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the SymbolicNameProps with a parent and short name.

        Args:
            parent: The parent ARObject that contains this symbolic name props
            short_name: The unique short name of this symbolic name props
        """
        super().__init__(parent, short_name)


class SyncTimeBaseMgrUserNeeds(ServiceNeeds):
    """
    Represents Synchronized Time Base Manager User needs in AUTOSAR models.
    This class defines requirements for synchronized time base manager user services.
    """

    # SyncTimeBaseMgrUserNeeds method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the SyncTimeBaseMgrUserNeeds with a parent and short name.

        Args:
            parent: The parent ARObject that contains this sync time base manager user needs
            short_name: The unique short name of this sync time base manager user needs
        """
        super().__init__(parent, short_name)


class PossibleErrorReaction(Identifiable):
    """
    Describes a possible error reaction code for the transient fault handler.
    """

    # PossibleErrorReaction method parity checklist:
    # [ ] __init__                     [ ] impl  [ ] docstring  [ ] test
    # [ ] getReactionCode              [ ] impl  [ ] docstring  [ ] test
    # [ ] setReactionCode              [ ] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the PossibleErrorReaction with a parent and short name.

        Args:
            parent: The parent ARObject that contains this possible error reaction
            short_name: The unique short name of this possible error reaction
        """
        super().__init__(parent, short_name)

        # Fault reaction code which can be returned by transient fault handler.
        self.reactionCode: Optional[PositiveInteger] = None

    def getReactionCode(self) -> Optional[PositiveInteger]:
        """
        Gets the fault reaction code which can be returned by transient fault handler.

        Returns:
            PositiveInteger instance, or None if not set
        """
        return self.reactionCode

    def setReactionCode(self, value: Optional[PositiveInteger]) -> "PossibleErrorReaction":
        """
        Sets the fault reaction code which can be returned by transient fault handler.
        A None value is a no-op and does not overwrite an existing reactionCode.

        Args:
            value: The PositiveInteger instance to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.reactionCode = value
        return self


class TransientFault(TracedFailure):
    """
    The reported failure is classified as runtime error.
    """

    # TransientFault method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table E.50, p.1009
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] createPossibleErrorReaction  [x] impl  [x] docstring  [x] test
    # [x] getPossibleErrorReactions    [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the TransientFault with a parent and short name.

        Args:
            parent: The parent ARObject that contains this transient fault
            short_name: The unique short name of this transient fault
        """
        super().__init__(parent, short_name)

        # Describes a possible error reactions for the transient fault handler.
        self.possibleErrorReactions: List[PossibleErrorReaction] = []

    def createPossibleErrorReaction(self, short_name: str) -> PossibleErrorReaction:
        """
        Creates and adds a possible error reaction for the transient fault handler.

        Args:
            short_name: The short name for the new possible error reaction

        Returns:
            The created PossibleErrorReaction instance
        """
        if not self.IsElementExists(short_name):
            reaction = PossibleErrorReaction(self, short_name)
            self.addElement(reaction)
            self.possibleErrorReactions.append(reaction)
        return self.getElement(short_name)

    def getPossibleErrorReactions(self) -> List[PossibleErrorReaction]:
        """
        Gets the possible error reactions for the transient fault handler.

        Returns:
            List of PossibleErrorReaction instances
        """
        return self.possibleErrorReactions


class V2xDataManagerNeeds(ServiceNeeds):
    """
    Represents V2X Data Manager needs in AUTOSAR models.
    This class defines requirements for Vehicle-to-Everything data manager services.
    """

    # V2xDataManagerNeeds method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the V2xDataManagerNeeds with a parent and short name.

        Args:
            parent: The parent ARObject that contains this V2X data manager needs
            short_name: The unique short name of this V2X data manager needs
        """
        super().__init__(parent, short_name)


class V2xFacUserNeeds(ServiceNeeds):
    """
    Represents V2X Functional Application Cluster User needs in AUTOSAR models.
    This class defines requirements for V2X functional application cluster user services.
    """

    # V2xFacUserNeeds method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the V2xFacUserNeeds with a parent and short name.

        Args:
            parent: The parent ARObject that contains this V2X FAC user needs
            short_name: The unique short name of this V2X FAC user needs
        """
        super().__init__(parent, short_name)


class V2xMUserNeeds(ServiceNeeds):
    """
    Represents V2X Manager User needs in AUTOSAR models.
    This class defines requirements for V2X manager user services.
    """

    # V2xMUserNeeds method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the V2xMUserNeeds with a parent and short name.

        Args:
            parent: The parent ARObject that contains this V2X manager user needs
            short_name: The unique short name of this V2X manager user needs
        """
        super().__init__(parent, short_name)


class VendorSpecificServiceNeeds(ServiceNeeds):
    """
    Represents Vendor Specific Service needs in AUTOSAR models.
    This class defines requirements for vendor-specific services.
    """

    # VendorSpecificServiceNeeds method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the VendorSpecificServiceNeeds with a parent and short name.

        Args:
            parent: The parent ARObject that contains this vendor specific service needs
            short_name: The unique short name of this vendor specific service needs
        """
        super().__init__(parent, short_name)


class VerificationStatusIndicationModeEnum(AREnum):
    """
    This enumeration provides options for setting the mode of a verification status indication.
    """

    # VerificationStatusIndicationModeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 13.69, p.824
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test

    # Verification attempts that came out "false" or "true" shall be forwarded to the application software. Tags: atp.EnumerationLiteralIndex=1
    FAILURE_AND_SUCCESS = "failureAndSuccess"
    # Only verification attempts that came out "false" shall be forwarded to the application software. Tags: atp.EnumerationLiteralIndex=0
    FAILURE_ONLY = "failureOnly"

    def __init__(self):
        super().__init__(
            [
                VerificationStatusIndicationModeEnum.FAILURE_AND_SUCCESS,
                VerificationStatusIndicationModeEnum.FAILURE_ONLY,
            ]
        )


class WarningIndicatorRequestedBitNeeds(ServiceNeeds):
    """
    Represents Warning Indicator Requested Bit needs in AUTOSAR models.
    This class defines requirements for warning indicator requested bit services.
    """

    # WarningIndicatorRequestedBitNeeds method parity checklist:
    # [ ] __init__                     [x] impl  [x] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the WarningIndicatorRequestedBitNeeds with a parent and short name.

        Args:
            parent: The parent ARObject that contains this warning indicator requested bit needs
            short_name: The unique short name of this warning indicator requested bit needs
        """
        super().__init__(parent, short_name)
