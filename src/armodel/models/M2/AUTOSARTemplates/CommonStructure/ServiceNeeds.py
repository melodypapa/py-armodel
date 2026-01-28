"""
This module contains classes for representing AUTOSAR service needs structures
in the CommonStructure module. Service needs define requirements for various
services such as NV block management, diagnostic services, cryptographic services, etc.
"""

from abc import ABC
from typing import List
from ....M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.InstanceRefsUsage import AutosarParameterRef
from ....M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AutosarVariableRef import AutosarVariableRef
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, RefType, AREnum, Boolean, ARLiteral
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DiagRequirementIdString, Integer, PositiveInteger
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String, TimeValue


class RoleBasedDataAssignment(ARObject):
    """
    Represents a role-based data assignment in AUTOSAR models.
    This class defines how data elements are assigned based on their role in service interactions.
    """
    
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
    # Status control through API calls
    API = "api"
    # Status control through NV RAM manager
    NV_RAM_MANAGER = "nvRamManager"

    def __init__(self):
        """
        Initializes the RamBlockStatusControlEnum with all possible values.
        """
        super().__init__((
            RamBlockStatusControlEnum.API,
            RamBlockStatusControlEnum.NV_RAM_MANAGER,
        ))


class NvBlockNeedsReliabilityEnum(AREnum):
    """
    Enumeration for NV block needs reliability levels in AUTOSAR models.
    Defines the type of error protection used for NV block management.
    """
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
        super().__init__((
            NvBlockNeedsReliabilityEnum.ERROR_CORRECTION,
            NvBlockNeedsReliabilityEnum.ERROR_DETECTION,
            NvBlockNeedsReliabilityEnum.NO_PROTECTION,
        ))


class NvBlockNeedsWritingPriorityEnum(AREnum):
    """
    Enumeration for NV block needs writing priorities in AUTOSAR models.
    Defines the priority level for writing operations to NV blocks.
    """
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
        super().__init__((
            NvBlockNeedsWritingPriorityEnum.HIGH,
            NvBlockNeedsWritingPriorityEnum.LOW,
            NvBlockNeedsWritingPriorityEnum.MEDIUM,
        ))


class NvBlockNeeds(ServiceNeeds):
    """
    Represents NV (Non-Volatile) block needs in AUTOSAR models.
    This class defines requirements for managing non-volatile memory blocks including
    CRC calculation, write protection, and various storage strategies.
    """
    
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
    Represents a role-based data type assignment in AUTOSAR models.
    This class defines how implementation data types are assigned based on their role in service interactions.
    """
    
    def __init__(self):
        """
        Initializes the RoleBasedDataTypeAssignment with default values.
        """
        super().__init__()

        # Role identifier for this data type assignment
        self.role: Identifier = None                                
        # Reference to the used implementation data type
        self.usedImplementationDataTypeRef: RefType = None       

    def getRole(self):
        """
        Gets the role identifier for this data type assignment.
        
        Returns:
            Identifier: The role identifier
        """
        return self.role

    def setRole(self, value):
        """
        Sets the role identifier for this data type assignment.
        Only sets the value if it is not None.
        
        Args:
            value: The role identifier to set
            
        Returns:
            self for method chaining
        """
        self.role = value
        return self

    def getUsedImplementationDataTypeRef(self):
        """
        Gets the reference to the used implementation data type.
        
        Returns:
            RefType: The implementation data type reference
        """
        return self.usedImplementationDataTypeRef

    def setUsedImplementationDataTypeRef(self, value):
        """
        Sets the reference to the used implementation data type.
        Only sets the value if it is not None.
        
        Args:
            value: The implementation data type reference to set
            
        Returns:
            self for method chaining
        """
        self.usedImplementationDataTypeRef = value
        return self


class ServiceDiagnosticRelevanceEnum(AREnum):
    """
    Enumeration for service diagnostic relevance in AUTOSAR models.
    Defines the diagnostic relevance of services (currently empty as per specification).
    """
    
    def __init__(self):
        """
        Initializes the ServiceDiagnosticRelevanceEnum with empty values list.
        """
        super().__init__([])
    

class ServiceDependency(Identifiable, ABC):
    """
    Represents a service dependency in AUTOSAR models.
    This class defines dependencies on services along with their data type assignments and diagnostic relevance.
    """

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the ServiceDependency with a parent and short name.
        Raises TypeError if this abstract class is instantiated directly.

        Args:
            parent: The parent ARObject that contains this service dependency
            short_name: The unique short name of this service dependency
        """
        if type(self) is ServiceDependency:
            raise TypeError("ServiceDependency is an abstract class.")
        super().__init__(parent, short_name)

        # List of role-based data type assignments for this service dependency
        self.assignedDataTypes: List[RoleBasedDataTypeAssignment] = []                                 
        # Diagnostic relevance of this service dependency
        self.diagnosticRelevance: ServiceDiagnosticRelevanceEnum = None                             
        # Symbolic name properties for this service dependency
        self.symbolicNameProps = None                               

    def getAssignedDataTypes(self):
        """
        Gets the list of role-based data type assignments for this service dependency.
        
        Returns:
            List of RoleBasedDataTypeAssignment instances
        """
        return self.assignedDataTypes

    def addAssignedDataType(self, value):
        """
        Adds a role-based data type assignment to this service dependency.
        
        Args:
            value: The data type assignment to add
            
        Returns:
            self for method chaining
        """
        self.assignedDataTypes.append(value)
        return self

    def getDiagnosticRelevance(self):
        """
        Gets the diagnostic relevance of this service dependency.
        
        Returns:
            ServiceDiagnosticRelevanceEnum: The diagnostic relevance
        """
        return self.diagnosticRelevance

    def setDiagnosticRelevance(self, value):
        """
        Sets the diagnostic relevance of this service dependency.
        Only sets the value if it is not None.
        
        Args:
            value: The diagnostic relevance to set
            
        Returns:
            self for method chaining
        """
        self.diagnosticRelevance = value
        return self

    def getSymbolicNameProps(self):
        """
        Gets the symbolic name properties for this service dependency.
        
        Returns:
            SymbolicNameProps: The symbolic name properties
        """
        return self.symbolicNameProps

    def setSymbolicNameProps(self, value):
        """
        Sets the symbolic name properties for this service dependency.
        Only sets the value if it is not None.
        
        Args:
            value: The symbolic name properties to set
            
        Returns:
            self for method chaining
        """
        self.symbolicNameProps = value
        return self


class DiagnosticAudienceEnum(AREnum):
    """
    Enumeration for diagnostic audiences in AUTOSAR models.
    Defines the target audience for diagnostic information and services.
    """
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
        super().__init__((
            DiagnosticAudienceEnum.AFTER_MARKET,
            DiagnosticAudienceEnum.AFTER_SALES,
            DiagnosticAudienceEnum.DEVELOPMENT,
            DiagnosticAudienceEnum.MANUFACTURING,
            DiagnosticAudienceEnum.SUPPLIER,
        ))


class DiagnosticServiceRequestCallbackTypeEnum(AREnum):
    """
    Enumeration for diagnostic service request callback types in AUTOSAR models.
    Defines who handles diagnostic service request callbacks (manufacturer or supplier).
    """
    # Callback type handled by manufacturer
    REQUEST_CALLBACK_TYPE_MANUFACTURER = "requestCallbackTypeManufacturer"
    # Callback type handled by supplier
    REQUEST_CALLBACK_TYPE_SUPPLIER = "requestCallbackTypeSupplier"

    def __init__(self):
        """
        Initializes the DiagnosticServiceRequestCallbackTypeEnum with all possible values.
        """
        super().__init__((
            DiagnosticServiceRequestCallbackTypeEnum.REQUEST_CALLBACK_TYPE_MANUFACTURER,
            DiagnosticServiceRequestCallbackTypeEnum.REQUEST_CALLBACK_TYPE_SUPPLIER,
        ))


class DiagnosticCapabilityElement(ServiceNeeds, ABC):
    """
    Abstract base class for diagnostic capability elements in AUTOSAR models.
    This class defines common properties for diagnostic capabilities including audiences, requirements, and security access levels.
    """
    
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
    # Asynchronous diagnostic routine
    ASYNCHRONOUS = "asynchronous"
    # Synchronous diagnostic routine
    SYNCHRONOUS = "synchronous"

    def __init__(self):
        """
        Initializes the DiagnosticRoutineTypeEnum with all possible values.
        """
        super().__init__((
            DiagnosticRoutineTypeEnum.ASYNCHRONOUS,
            DiagnosticRoutineTypeEnum.SYNCHRONOUS,
        ))


class DiagnosticCommunicationManagerNeeds(DiagnosticCapabilityElement):
    """
    Represents diagnostic communication manager needs in AUTOSAR models.
    This class defines requirements for the diagnostic communication manager including callback types.
    """
    
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
        super().__init__((
            DiagnosticValueAccessEnum.READ_ONLY,
            DiagnosticValueAccessEnum.READ_WRITE,
            DiagnosticValueAccessEnum.WRITE_ONLY,
        ))


class DiagnosticProcessingStyleEnum(AREnum):
    """
    Enumeration for diagnostic processing styles in AUTOSAR models.
    Defines how diagnostic processing is handled (synchronously, asynchronously, etc.).
    """
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
        super().__init__((
            DiagnosticProcessingStyleEnum.PROCESSING_STYLE_ASYNCHRONOUS,
            DiagnosticProcessingStyleEnum.PROCESSING_STYLE_ASYNCHRONOUS_WITH_ERROR,
            DiagnosticProcessingStyleEnum.PROCESSING_STYLE_SYNCHRONOUS,
        ))


class DiagnosticValueNeeds(DiagnosticCapabilityElement):
    """
    Represents diagnostic value needs in AUTOSAR models.
    This class defines requirements for diagnostic values including access permissions, length, and processing style.
    """
    
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
    Represents diagnostic event needs in AUTOSAR models.
    This class defines requirements for diagnostic events including debounce algorithms, FID references, and DTC information.
    """
    
    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the DiagnosticEventNeeds with a parent and short name.
        
        Args:
            parent: The parent ARObject that contains this diagnostic event needs
            short_name: The unique short name of this diagnostic event needs
        """
        super().__init__(parent, short_name)

        # List of FID (Function Identifier) references for deferring this diagnostic event
        self.deferringFidRefs: List[RefType] = []                                     
        # Debounce algorithm for this diagnostic event
        self.diagEventDebounceAlgorithm: DiagEventDebounceAlgorithm = None                         
        # FID reference for inhibiting this diagnostic event
        self.inhibitingFidRef: RefType = None                                   
        # Secondary FID reference for inhibiting this diagnostic event
        self.inhibitingSecondaryFidRef: RefType = None                           
        # Flag indicating if prestored freeze frame is stored in NVM
        self.prestoredFreezeframeStoredInNvm: Boolean = None                     
        # Flag indicating if this event uses monitor data
        self.usesMonitorData: Boolean = None                                     
        # Type of diagnostic trouble code (DTC) for this event (as ARLiteral)
        self.dtcKind: ARLiteral = None                                             
        # UDS (Unified Diagnostic Services) DTC number for this event
        self.udsDtcNumber: Integer = None                                        

    def getDeferringFidRefs(self):
        """
        Gets the list of FID (Function Identifier) references for deferring this diagnostic event.
        
        Returns:
            List of RefType instances
        """
        return self.deferringFidRefs

    def addDeferringFidRef(self, value):
        """
        Adds a FID (Function Identifier) reference for deferring this diagnostic event.
        
        Args:
            value: The FID reference to add
            
        Returns:
            self for method chaining
        """
        self.deferringFidRefs.append(value)
        return self
    
    def getDiagEventDebounceAlgorithm(self):
        """
        Gets the debounce algorithm for this diagnostic event.
        
        Returns:
            DiagEventDebounceAlgorithm: The debounce algorithm
        """
        return self.diagEventDebounceAlgorithm

    def createDiagEventDebounceCounterBased(self, short_name: str):
        """
        Creates and adds a counter-based debounce algorithm for this diagnostic event.
        
        Args:
            short_name: The short name for the new counter-based debounce algorithm
            
        Returns:
            The created DiagEventDebounceCounterBased instance
        """
        if (short_name not in self.elements):
            algorithm = DiagEventDebounceCounterBased(self, short_name)
            self.addElement(algorithm)
            self.diagEventDebounceAlgorithm = algorithm
        return self.getElement(short_name)
    
    def createDiagEventDebounceMonitorInternal(self, short_name: str):
        """
        Creates and adds an internal monitor-based debounce algorithm for this diagnostic event.
        
        Args:
            short_name: The short name for the new internal monitor debounce algorithm
            
        Returns:
            The created DiagEventDebounceMonitorInternal instance
        """
        if (short_name not in self.elements):
            algorithm = DiagEventDebounceMonitorInternal(self, short_name)
            self.addElement(algorithm)
            self.diagEventDebounceAlgorithm = algorithm
        return self.getElement(short_name)

    def createDiagEventDebounceTimeBased(self, short_name: str):
        """
        Creates and adds a time-based debounce algorithm for this diagnostic event.
        
        Args:
            short_name: The short name for the new time-based debounce algorithm
            
        Returns:
            The created DiagEventDebounceTimeBased instance
        """
        if (short_name not in self.elements):
            algorithm = DiagEventDebounceTimeBased(self, short_name)
            self.addElement(algorithm)
            self.diagEventDebounceAlgorithm = algorithm
        return self.getElement(short_name)
    
    def getInhibitingFidRef(self):
        """
        Gets the FID reference for inhibiting this diagnostic event.
        
        Returns:
            RefType: The inhibiting FID reference
        """
        return self.inhibitingFidRef

    def setInhibitingFidRef(self, value):
        """
        Sets the FID reference for inhibiting this diagnostic event.
        Only sets the value if it is not None.
        
        Args:
            value: The inhibiting FID reference to set
            
        Returns:
            self for method chaining
        """
        self.inhibitingFidRef = value
        return self

    def getInhibitingSecondaryFidRef(self):
        """
        Gets the secondary FID reference for inhibiting this diagnostic event.
        
        Returns:
            RefType: The secondary inhibiting FID reference
        """
        return self.inhibitingSecondaryFidRef

    def setInhibitingSecondaryFidRef(self, value):
        """
        Sets the secondary FID reference for inhibiting this diagnostic event.
        Only sets the value if it is not None.
        
        Args:
            value: The secondary inhibiting FID reference to set
            
        Returns:
            self for method chaining
        """
        self.inhibitingSecondaryFidRef = value
        return self

    def getPrestoredFreezeframeStoredInNvm(self):
        """
        Gets the flag indicating if prestored freeze frame is stored in NVM.
        
        Returns:
            Boolean: The prestored freeze frame flag
        """
        return self.prestoredFreezeframeStoredInNvm

    def setPrestoredFreezeframeStoredInNvm(self, value):
        """
        Sets the flag indicating if prestored freeze frame is stored in NVM.
        Only sets the value if it is not None.
        
        Args:
            value: The prestored freeze frame flag to set
            
        Returns:
            self for method chaining
        """
        self.prestoredFreezeframeStoredInNvm = value
        return self

    def getUsesMonitorData(self):
        """
        Gets the flag indicating if this event uses monitor data.
        
        Returns:
            Boolean: The use monitor data flag
        """
        return self.usesMonitorData

    def setUsesMonitorData(self, value):
        """
        Sets the flag indicating if this event uses monitor data.
        Only sets the value if it is not None.
        
        Args:
            value: The use monitor data flag to set
            
        Returns:
            self for method chaining
        """
        self.usesMonitorData = value
        return self

    def getDtcKind(self):
        """
        Gets the type of diagnostic trouble code (DTC) for this event (as ARLiteral).
        
        Returns:
            ARLiteral: The DTC kind
        """
        return self.dtcKind

    def setDtcKind(self, value):
        """
        Sets the type of diagnostic trouble code (DTC) for this event (as ARLiteral).
        Only sets the value if it is not None.
        
        Args:
            value: The DTC kind to set
            
        Returns:
            self for method chaining
        """
        self.dtcKind = value
        return self

    def getUdsDtcNumber(self):
        """
        Gets the UDS (Unified Diagnostic Services) DTC number for this event.
        
        Returns:
            Integer: The UDS DTC number
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
        self.udsDtcNumber = value
        return self


class CryptoServiceNeeds(ServiceNeeds):
    """
    Represents cryptographic service needs in AUTOSAR models.
    This class defines requirements for cryptographic services including algorithm information and key management.
    """
    
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
    Represents Communication Manager user needs in AUTOSAR models.
    This class defines requirements for Communication Manager services.
    """
    
    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the ComMgrUserNeeds with a parent and short name.
        
        Args:
            parent: The parent ARObject that contains this COM manager user needs
            short_name: The unique short name of this COM manager user needs
        """
        super().__init__(parent, short_name)


class CryptoKeyManagementNeeds(ServiceNeeds):
    """
    Represents Cryptographic Key Management needs in AUTOSAR models.
    This class defines requirements for cryptographic key management services.
    """
    
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
    
    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the CryptoServiceJobNeeds with a parent and short name.
        
        Args:
            parent: The parent ARObject that contains this crypto service job needs
            short_name: The unique short name of this crypto service job needs
        """
        super().__init__(parent, short_name)


class DevelopmentError(ARObject):
    """
    Represents a development error in AUTOSAR models.
    This class defines information about development errors for error handling.
    """
    
    def __init__(self):
        """
        Initializes the DevelopmentError with default values.
        """
        super().__init__()
        self.errorCode: Integer = None
        self.errorDescription: String = None

    def getErrorCode(self):
        return self.errorCode

    def setErrorCode(self, value):
        self.errorCode = value
        return self

    def getErrorDescription(self):
        return self.errorDescription

    def setErrorDescription(self, value):
        self.errorDescription = value
        return self


class DiagnosticComponentNeeds(ServiceNeeds):
    """
    Represents Diagnostic Component needs in AUTOSAR models.
    This class defines requirements for diagnostic component services.
    """
    
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
    Enumeration for diagnostic denominator condition types.
    """
    
    DENOMINATOR_OFF = "denominator-off"
    DENOMINATOR_ON = "denominator-on"

    def __init__(self):
        super().__init__((
            DiagnosticDenominatorConditionEnum.DENOMINATOR_OFF,
            DiagnosticDenominatorConditionEnum.DENOMINATOR_ON,
        ))


class DiagnosticEnableConditionNeeds(ServiceNeeds):
    """
    Represents Diagnostic Enable Condition needs in AUTOSAR models.
    This class defines requirements for diagnostic enable condition services.
    """
    
    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the DiagnosticEnableConditionNeeds with a parent and short name.
        
        Args:
            parent: The parent ARObject that contains this diagnostic enable condition needs
            short_name: The unique short name of this diagnostic enable condition needs
        """
        super().__init__(parent, short_name)


class DiagnosticEventManagerNeeds(ServiceNeeds):
    """
    Represents Diagnostic Event Manager needs in AUTOSAR models.
    This class defines requirements for diagnostic event manager services.
    """
    
    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the DiagnosticEventManagerNeeds with a parent and short name.
        
        Args:
            parent: The parent ARObject that contains this diagnostic event manager needs
            short_name: The unique short name of this diagnostic event manager needs
        """
        super().__init__(parent, short_name)


class DiagnosticIoControlNeeds(ServiceNeeds):
    """
    Represents Diagnostic I/O Control needs in AUTOSAR models.
    This class defines requirements for diagnostic input/output control services.
    """
    
    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the DiagnosticIoControlNeeds with a parent and short name.
        
        Args:
            parent: The parent ARObject that contains this diagnostic I/O control needs
            short_name: The unique short name of this diagnostic I/O control needs
        """
        super().__init__(parent, short_name)


class DiagnosticMonitorUpdateKindEnum(AREnum):
    """
    Enumeration for diagnostic monitor update kinds.
    """
    
    IMMEDIATE = "immediate"
    ON_REQUEST = "on-request"

    def __init__(self):
        super().__init__((
            DiagnosticMonitorUpdateKindEnum.IMMEDIATE,
            DiagnosticMonitorUpdateKindEnum.ON_REQUEST,
        ))


class DiagnosticOperationCycleNeeds(ServiceNeeds):
    """
    Represents Diagnostic Operation Cycle needs in AUTOSAR models.
    This class defines requirements for diagnostic operation cycle services.
    """
    
    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the DiagnosticOperationCycleNeeds with a parent and short name.
        
        Args:
            parent: The parent ARObject that contains this diagnostic operation cycle needs
            short_name: The unique short name of this diagnostic operation cycle needs
        """
        super().__init__(parent, short_name)


class DiagnosticRequestFileTransferNeeds(ServiceNeeds):
    """
    Represents Diagnostic Request File Transfer needs in AUTOSAR models.
    This class defines requirements for diagnostic file transfer services.
    """
    
    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the DiagnosticRequestFileTransferNeeds with a parent and short name.
        
        Args:
            parent: The parent ARObject that contains this diagnostic request file transfer needs
            short_name: The unique short name of this diagnostic request file transfer needs
        """
        super().__init__(parent, short_name)


class DiagnosticStorageConditionNeeds(ServiceNeeds):
    """
    Represents Diagnostic Storage Condition needs in AUTOSAR models.
    This class defines requirements for diagnostic storage condition services.
    """
    
    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the DiagnosticStorageConditionNeeds with a parent and short name.
        
        Args:
            parent: The parent ARObject that contains this diagnostic storage condition needs
            short_name: The unique short name of this diagnostic storage condition needs
        """
        super().__init__(parent, short_name)


class DiagnosticUploadDownloadNeeds(ServiceNeeds):
    """
    Represents Diagnostic Upload/Download needs in AUTOSAR models.
    This class defines requirements for diagnostic upload and download services.
    """
    
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
    
    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the DoIpPowerModeStatusNeeds with a parent and short name.
        
        Args:
            parent: The parent ARObject that contains this DoIP power mode status needs
            short_name: The unique short name of this DoIP power mode status needs
        """
        super().__init__(parent, short_name)


class DoIpRoutingActivationAuthenticationNeeds(ServiceNeeds):
    """
    Represents DoIP Routing Activation Authentication needs in AUTOSAR models.
    This class defines requirements for DoIP (Diagnostics over IP) routing activation authentication services.
    """
    
    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the DoIpRoutingActivationAuthenticationNeeds with a parent and short name.
        
        Args:
            parent: The parent ARObject that contains this DoIP routing activation authentication needs
            short_name: The unique short name of this DoIP routing activation authentication needs
        """
        super().__init__(parent, short_name)


class DoIpRoutingActivationConfirmationNeeds(ServiceNeeds):
    """
    Represents DoIP Routing Activation Confirmation needs in AUTOSAR models.
    This class defines requirements for DoIP (Diagnostics over IP) routing activation confirmation services.
    """
    
    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the DoIpRoutingActivationConfirmationNeeds with a parent and short name.
        
        Args:
            parent: The parent ARObject that contains this DoIP routing activation confirmation needs
            short_name: The unique short name of this DoIP routing activation confirmation needs
        """
        super().__init__(parent, short_name)


class DoIpServiceNeeds(ServiceNeeds):
    """
    Represents DoIP Service needs in AUTOSAR models.
    This class defines requirements for DoIP (Diagnostics over IP) services.
    """
    
    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the DoIpServiceNeeds with a parent and short name.
        
        Args:
            parent: The parent ARObject that contains this DoIP service needs
            short_name: The unique short name of this DoIP service needs
        """
        super().__init__(parent, short_name)


class ErrorTracerNeeds(ServiceNeeds):
    """
    Represents Error Tracer needs in AUTOSAR models.
    This class defines requirements for error tracing services.
    """
    
    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the ErrorTracerNeeds with a parent and short name.
        
        Args:
            parent: The parent ARObject that contains this error tracer needs
            short_name: The unique short name of this error tracer needs
        """
        super().__init__(parent, short_name)


class EventAcceptanceStatusEnum(AREnum):
    """
    Enumeration for event acceptance status types.
    """
    
    ACCEPTED = "accepted"
    REJECTED = "rejected"

    def __init__(self):
        super().__init__((
            EventAcceptanceStatusEnum.ACCEPTED,
            EventAcceptanceStatusEnum.REJECTED,
        ))


class FunctionInhibitionAvailabilityNeeds(ServiceNeeds):
    """
    Represents Function Inhibition Availability needs in AUTOSAR models.
    This class defines requirements for function inhibition availability services.
    """
    
    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the FunctionInhibitionAvailabilityNeeds with a parent and short name.
        
        Args:
            parent: The parent ARObject that contains this function inhibition availability needs
            short_name: The unique short name of this function inhibition availability needs
        """
        super().__init__(parent, short_name)


class FunctionInhibitionNeeds(ServiceNeeds):
    """
    Represents Function Inhibition needs in AUTOSAR models.
    This class defines requirements for function inhibition services.
    """
    
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
    Represents IDS Manager needs in AUTOSAR models.
    This class defines requirements for IDS (Intrusion Detection System) manager services.
    """
    
    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the IdsMgrNeeds with a parent and short name.
        
        Args:
            parent: The parent ARObject that contains this IDS manager needs
            short_name: The unique short name of this IDS manager needs
        """
        super().__init__(parent, short_name)


class IndicatorStatusNeeds(ServiceNeeds):
    """
    Represents Indicator Status needs in AUTOSAR models.
    This class defines requirements for indicator status services.
    """
    
    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the IndicatorStatusNeeds with a parent and short name.
        
        Args:
            parent: The parent ARObject that contains this indicator status needs
            short_name: The unique short name of this indicator status needs
        """
        super().__init__(parent, short_name)


class J1939DcmDm19Support(ServiceNeeds):
    """
    Represents J1939 DCM DM19 Support needs in AUTOSAR models.
    This class defines requirements for J1939 diagnostic communication manager DM19 support.
    """
    
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
    Enumeration for maximum communication mode types.
    """
    
    FULL_COMMUNICATION = "full-communication"
    NO_COMMUNICATION = "no-communication"
    SILENT_COMMUNICATION = "silent-communication"

    def __init__(self):
        super().__init__((
            MaxCommModeEnum.FULL_COMMUNICATION,
            MaxCommModeEnum.NO_COMMUNICATION,
            MaxCommModeEnum.SILENT_COMMUNICATION,
        ))


class ObdControlServiceNeeds(ServiceNeeds):
    """
    Represents OBD Control Service needs in AUTOSAR models.
    This class defines requirements for On-Board Diagnostics control services.
    """
    
    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the ObdControlServiceNeeds with a parent and short name.
        
        Args:
            parent: The parent ARObject that contains this OBD control service needs
            short_name: The unique short name of this OBD control service needs
        """
        super().__init__(parent, short_name)


class ObdInfoServiceNeeds(ServiceNeeds):
    """
    Represents OBD Info Service needs in AUTOSAR models.
    This class defines requirements for On-Board Diagnostics information services.
    """
    
    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the ObdInfoServiceNeeds with a parent and short name.
        
        Args:
            parent: The parent ARObject that contains this OBD info service needs
            short_name: The unique short name of this OBD info service needs
        """
        super().__init__(parent, short_name)


class ObdMonitorServiceNeeds(ServiceNeeds):
    """
    Represents OBD Monitor Service needs in AUTOSAR models.
    This class defines requirements for On-Board Diagnostics monitor services.
    """
    
    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the ObdMonitorServiceNeeds with a parent and short name.
        
        Args:
            parent: The parent ARObject that contains this OBD monitor service needs
            short_name: The unique short name of this OBD monitor service needs
        """
        super().__init__(parent, short_name)


class ObdPidServiceNeeds(ServiceNeeds):
    """
    Represents OBD PID Service needs in AUTOSAR models.
    This class defines requirements for On-Board Diagnostics PID (Parameter ID) services.
    """
    
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
    Enumeration for OBD ratio connection kind types.
    """
    
    LOGICAL_AND = "logical-and"
    LOGICAL_OR = "logical-or"

    def __init__(self):
        super().__init__((
            ObdRatioConnectionKindEnum.LOGICAL_AND,
            ObdRatioConnectionKindEnum.LOGICAL_OR,
        ))


class ObdRatioDenominatorNeeds(ServiceNeeds):
    """
    Represents OBD Ratio Denominator needs in AUTOSAR models.
    This class defines requirements for On-Board Diagnostics ratio denominator services.
    """
    
    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the ObdRatioDenominatorNeeds with a parent and short name.
        
        Args:
            parent: The parent ARObject that contains this OBD ratio denominator needs
            short_name: The unique short name of this OBD ratio denominator needs
        """
        super().__init__(parent, short_name)


class ObdRatioServiceNeeds(ServiceNeeds):
    """
    Represents OBD Ratio Service needs in AUTOSAR models.
    This class defines requirements for On-Board Diagnostics ratio services.
    """
    
    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the ObdRatioServiceNeeds with a parent and short name.
        
        Args:
            parent: The parent ARObject that contains this OBD ratio service needs
            short_name: The unique short name of this OBD ratio service needs
        """
        super().__init__(parent, short_name)


class OperationCycleTypeEnum(AREnum):
    """
    Enumeration for operation cycle type.
    """
    
    ALL_CYCLES = "all-cycles"
    IGNITION_CYCLE = "ignition-cycle"
    POWER_CYCLE = "power-cycle"

    def __init__(self):
        super().__init__((
            OperationCycleTypeEnum.ALL_CYCLES,
            OperationCycleTypeEnum.IGNITION_CYCLE,
            OperationCycleTypeEnum.POWER_CYCLE,
        ))


class RuntimeError(ARObject):
    """
    Represents a runtime error in AUTOSAR models.
    This class defines information about runtime errors for error handling.
    """
    
    def __init__(self):
        """
        Initializes the RuntimeError with default values.
        """
        super().__init__()
        self.errorCode: Integer = None
        self.errorDescription: String = None

    def getErrorCode(self):
        return self.errorCode

    def setErrorCode(self, value):
        self.errorCode = value
        return self

    def getErrorDescription(self):
        return self.errorDescription

    def setErrorDescription(self, value):
        self.errorDescription = value
        return self


class SecureOnBoardCommunicationNeeds(ServiceNeeds):
    """
    Represents Secure On-Board Communication needs in AUTOSAR models.
    This class defines requirements for secure on-board communication services (SecOC).
    """
    
    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the SecureOnBoardCommunicationNeeds with a parent and short name.
        
        Args:
            parent: The parent ARObject that contains this secure on-board communication needs
            short_name: The unique short name of this secure on-board communication needs
        """
        super().__init__(parent, short_name)


class ServiceProviderEnum(AREnum):
    """
    Enumeration for service provider types.
    """
    
    BSW = "bsw"
    RTE = "rte"
    SWC = "swc"

    def __init__(self):
        super().__init__((
            ServiceProviderEnum.BSW,
            ServiceProviderEnum.RTE,
            ServiceProviderEnum.SWC,
        ))


class StorageConditionStatusEnum(AREnum):
    """
    Enumeration for storage condition status types.
    """
    
    CONDITION_FALSE = "condition-false"
    CONDITION_TRUE = "condition-true"

    def __init__(self):
        super().__init__((
            StorageConditionStatusEnum.CONDITION_FALSE,
            StorageConditionStatusEnum.CONDITION_TRUE,
        ))


class SupervisedEntityCheckpointNeeds(ServiceNeeds):
    """
    Represents Supervised Entity Checkpoint needs in AUTOSAR models.
    This class defines requirements for supervised entity checkpoint services.
    """
    
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
    Represents Supervised Entity needs in AUTOSAR models.
    This class defines requirements for supervised entity services.
    """
    
    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the SupervisedEntityNeeds with a parent and short name.
        
        Args:
            parent: The parent ARObject that contains this supervised entity needs
            short_name: The unique short name of this supervised entity needs
        """
        super().__init__(parent, short_name)


class SymbolicNameProps(ARObject):
    """
    Represents Symbolic Name properties in AUTOSAR models.
    This class defines symbolic name properties for elements.
    """
    
    def __init__(self):
        """
        Initializes the SymbolicNameProps with default values.
        """
        super().__init__()
        self.symbolicName: String = None

    def getSymbolicName(self):
        return self.symbolicName

    def setSymbolicName(self, value):
        self.symbolicName = value
        return self


class SyncTimeBaseMgrUserNeeds(ServiceNeeds):
    """
    Represents Synchronized Time Base Manager User needs in AUTOSAR models.
    This class defines requirements for synchronized time base manager user services.
    """
    
    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the SyncTimeBaseMgrUserNeeds with a parent and short name.
        
        Args:
            parent: The parent ARObject that contains this sync time base manager user needs
            short_name: The unique short name of this sync time base manager user needs
        """
        super().__init__(parent, short_name)


class TracedFailure(ARObject):
    """
    Represents a Traced Failure in AUTOSAR models.
    This class defines information about traced failures for error handling.
    """
    
    def __init__(self):
        """
        Initializes the TracedFailure with default values.
        """
        super().__init__()
        self.failureCode: Integer = None
        self.failureDescription: String = None

    def getFailureCode(self):
        return self.failureCode

    def setFailureCode(self, value):
        self.failureCode = value
        return self

    def getFailureDescription(self):
        return self.failureDescription

    def setFailureDescription(self, value):
        self.failureDescription = value
        return self


class TransientFault(ARObject):
    """
    Represents a Transient Fault in AUTOSAR models.
    This class defines information about transient faults for error handling.
    """
    
    def __init__(self):
        """
        Initializes the TransientFault with default values.
        """
        super().__init__()
        self.faultCode: Integer = None
        self.faultDescription: String = None

    def getFaultCode(self):
        return self.faultCode

    def setFaultCode(self, value):
        self.faultCode = value
        return self

    def getFaultDescription(self):
        return self.faultDescription

    def setFaultDescription(self, value):
        self.faultDescription = value
        return self


class V2xDataManagerNeeds(ServiceNeeds):
    """
    Represents V2X Data Manager needs in AUTOSAR models.
    This class defines requirements for Vehicle-to-Everything data manager services.
    """
    
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
    Enumeration for verification status indication mode types.
    """
    
    DIRECT = "direct"
    INDIRECT = "indirect"

    def __init__(self):
        super().__init__((
            VerificationStatusIndicationModeEnum.DIRECT,
            VerificationStatusIndicationModeEnum.INDIRECT,
        ))


class WarningIndicatorRequestedBitNeeds(ServiceNeeds):
    """
    Represents Warning Indicator Requested Bit needs in AUTOSAR models.
    This class defines requirements for warning indicator requested bit services.
    """
    
    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the WarningIndicatorRequestedBitNeeds with a parent and short name.
        
        Args:
            parent: The parent ARObject that contains this warning indicator requested bit needs
            short_name: The unique short name of this warning indicator requested bit needs
        """
        super().__init__(parent, short_name)
