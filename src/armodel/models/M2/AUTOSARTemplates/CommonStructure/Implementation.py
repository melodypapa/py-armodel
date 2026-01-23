"""
This module contains classes for representing AUTOSAR implementation structures
in the CommonStructure module. Implementation classes define software implementations
including code descriptors, compilers, dependencies, and resource consumption information.
"""

from abc import ABC
from typing import List
from ....M2.AUTOSARTemplates.CommonStructure.ResourceConsumption import ResourceConsumption
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject import AutosarEngineeringObject
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable, PackageableElement, Referrable, ARElement
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType, ARLiteral, String, RevisionLabelString
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class ImplementationProps(Referrable, ABC):
    """
    Abstract base class for implementation properties in AUTOSAR models.
    This class serves as a base for defining properties of implementations such as symbols and identifiers.
    """

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the ImplementationProps with a parent and short name.
        Raises TypeError if this abstract class is instantiated directly.

        Args:
            parent: The parent ARObject that contains this implementation properties
            short_name: The unique short name of this implementation properties
        """
        if type(self) is ImplementationProps:
            raise TypeError("ImplementationProps is an abstract class.")
        
        super().__init__(parent, short_name)

        # Symbol associated with this implementation properties
        self.symbol: ARLiteral = None                         

    def getSymbol(self):
        """
        Gets the symbol associated with this implementation properties.
        
        Returns:
            ARLiteral: The symbol
        """
        return self.symbol

    def setSymbol(self, value):
        """
        Sets the symbol associated with this implementation properties.
        
        Args:
            value: The symbol to set
            
        Returns:
            self for method chaining
        """
        self.symbol = value
        return self


class Code(Identifiable):
    """
    Represents code descriptor in AUTOSAR models.
    This class contains information about code artifacts and their properties used in implementations.
    """
    
    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the Code with a parent and short name.
        
        Args:
            parent: The parent ARObject that contains this code descriptor
            short_name: The unique short name of this code descriptor
        """
        super().__init__(parent, short_name)

        # List of artifact descriptors for this code
        self.artifactDescriptors: List[AutosarEngineeringObject] = []          
        # List of callback header references for this code
        self.callbackHeaderRefs: List[RefType] = []            

    def addArtifactDescriptor(self, desc: AutosarEngineeringObject):
        """
        Adds an artifact descriptor to this code descriptor.
        
        Args:
            desc: The artifact descriptor to add
            
        Returns:
            self for method chaining
        """
        self.artifactDescriptors.append(desc)
        return self

    def getArtifactDescriptors(self, category: str = "") -> List[AutosarEngineeringObject]:
        """
        Gets the list of artifact descriptors, optionally filtered by category.
        
        Args:
            category: Optional category to filter descriptors by (returns all if empty)
            
        Returns:
            List of AutosarEngineeringObject instances matching the criteria
        """
        if (category == ""):
            return self.artifactDescriptors
        else:
            return list(filter(lambda a: a.getCategory().getText() == category, self.artifactDescriptors))


class Compiler(Identifiable):
    """
    Represents a compiler in AUTOSAR models.
    This class contains information about compiler configuration used in implementations.
    """
    
    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the Compiler with a parent and short name.
        
        Args:
            parent: The parent ARObject that contains this compiler
            short_name: The unique short name of this compiler
        """
        super().__init__(parent, short_name)

        # Name of the compiler
        self.name: String = None                                    
        # Options used with the compiler
        self.options: String = None                                 
        # Vendor information for the compiler
        self.vendor: String = None                                  
        # Version of the compiler
        self.version: String = None                                 

    def getName(self):
        """
        Gets the name of the compiler.
        
        Returns:
            String: The compiler name
        """
        return self.name

    def setName(self, value):
        """
        Sets the name of the compiler.
        
        Args:
            value: The compiler name to set
            
        Returns:
            self for method chaining
        """
        self.name = value
        return self

    def getOptions(self):
        """
        Gets the options used with the compiler.
        
        Returns:
            String: The compiler options
        """
        return self.options

    def setOptions(self, value):
        """
        Sets the options used with the compiler.
        
        Args:
            value: The compiler options to set
            
        Returns:
            self for method chaining
        """
        self.options = value
        return self

    def getVendor(self):
        """
        Gets the vendor information for the compiler.
        
        Returns:
            String: The compiler vendor
        """
        return self.vendor

    def setVendor(self, value):
        """
        Sets the vendor information for the compiler.
        
        Args:
            value: The compiler vendor to set
            
        Returns:
            self for method chaining
        """
        self.vendor = value
        return self

    def getVersion(self):
        """
        Gets the version of the compiler.
        
        Returns:
            String: The compiler version
        """
        return self.version

    def setVersion(self, value):
        """
        Sets the version of the compiler.
        
        Args:
            value: The compiler version to set
            
        Returns:
            self for method chaining
        """
        self.version = value
        return self


class DependencyOnArtifact(Identifiable):
    """
    Represents a dependency on an artifact in AUTOSAR models.
    This class defines dependencies on artifacts required by implementations such as compilers, linkers, etc.
    """
    
    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the DependencyOnArtifact with a parent and short name.
        
        Args:
            parent: The parent ARObject that contains this dependency
            short_name: The unique short name of this dependency
        """
        super().__init__(parent, short_name)

        # Artifact descriptor that this dependency references
        self.artifactDescriptor: AutosarEngineeringObject = None
        # Usage type of this dependency
        self.usage = None                                   

    def getArtifactDescriptor(self):
        """
        Gets the artifact descriptor that this dependency references.
        
        Returns:
            AutosarEngineeringObject: The artifact descriptor
        """
        return self.artifactDescriptor

    def setArtifactDescriptor(self, value):
        """
        Sets the artifact descriptor that this dependency references.
        
        Args:
            value: The artifact descriptor to set
            
        Returns:
            self for method chaining
        """
        self.artifactDescriptor = value
        return self

    def getUsage(self):
        """
        Gets the usage type of this dependency.
        
        Returns:
            DependencyUsageEnum: The usage type
        """
        return self.usage

    def setUsage(self, value):
        """
        Sets the usage type of this dependency.
        
        Args:
            value: The usage type to set
            
        Returns:
            self for method chaining
        """
        self.usage = value
        return self


class Implementation(ARElement, ABC):
    """
    Abstract base class for implementations in AUTOSAR models.
    This class serves as a base for defining software implementations including code, compilers, dependencies, and resource consumption information.
    """

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the Implementation with a parent and short name.
        Raises TypeError if this abstract class is instantiated directly.

        Args:
            parent: The parent ARObject that contains this implementation
            short_name: The unique short name of this implementation
        """
        if type(self) is Implementation:
            raise TypeError("Implementation is an abstract class.")

        super().__init__(parent, short_name)

        # Reference to the build action manifest for this implementation
        self.buildActionManifestRef: RefType = None                 
        # List of code descriptors for this implementation
        self.codeDescriptors: List['Code'] = []                           
        # List of compilers used in this implementation
        self.compilers: List['Compiler'] = []                                 
        # List of generated artifacts for this implementation
        self.generatedArtifacts: List['DependencyOnArtifact'] = []                        
        # List of hardware element references for this implementation
        self.hwElementRefs: List[RefType] = []                             
        # List of linkers used in this implementation
        self.linkers: List = []                                   
        # Microcontroller support information for this implementation
        self.mcSupport = None
        # Programming language used in this implementation
        self.programmingLanguage = None                     
        # List of required artifacts for this implementation
        self.requiredArtifacts: List['DependencyOnArtifact'] = []                         
        # List of required generator tools for this implementation
        self.requiredGeneratorTools: List['DependencyOnArtifact'] = []                    
        # Resource consumption information for this implementation
        self.resourceConsumption: ResourceConsumption = None                     
        # Reference to software component/BSW mapping for this implementation
        self.swcBswMappingRef: RefType = None                        
        # Software version information for this implementation
        self.swVersion: List[RevisionLabelString] = []                                 
        # Code generator used for this implementation
        self.usedCodeGenerator: String = None                       
        # Vendor ID for this implementation
        self.vendorId: PositiveInteger = 0                                   

    def getBuildActionManifestRef(self):
        """
        Gets the reference to the build action manifest for this implementation.
        
        Returns:
            RefType: The build action manifest reference
        """
        return self.buildActionManifestRef

    def setBuildActionManifestRef(self, value):
        """
        Sets the reference to the build action manifest for this implementation.
        
        Args:
            value: The build action manifest reference to set
            
        Returns:
            self for method chaining
        """
        self.buildActionManifestRef = value
        return self

    def getCodeDescriptors(self) -> List['Code']:
        """
        Gets all code descriptors from the elements list in this implementation.
        
        Returns:
            List of Code instances in this implementation
        """
        return list(filter(lambda a: isinstance(a, Code), self.elements))

    def createCodeDescriptor(self, short_name: str) -> 'Code':
        """
        Creates and adds a Code descriptor to this implementation.
        
        Args:
            short_name: The short name for the new code descriptor
            
        Returns:
            The created Code instance
        """
        if (short_name not in self.elements):
            code_descriptor = Code(self, short_name)
            self.addElement(code_descriptor)
            self.codeDescriptors.append(code_descriptor)
        return self.getElement(short_name)

    def getCompilers(self):
        """
        Gets the list of compilers used in this implementation.
        
        Returns:
            List of Compiler instances
        """
        return self.compilers

    def setCompilers(self, value):
        """
        Sets the list of compilers used in this implementation.
        Only sets the value if it is not None.
        
        Args:
            value: The list of compilers to set
            
        Returns:
            self for method chaining
        """
        self.compilers = value
        return self

    def getGeneratedArtifacts(self):
        """
        Gets the list of generated artifacts for this implementation.
        
        Returns:
            List of DependencyOnArtifact instances
        """
        return self.generatedArtifacts

    def setGeneratedArtifacts(self, value):
        """
        Sets the list of generated artifacts for this implementation.
        Only sets the value if it is not None.
        
        Args:
            value: The list of generated artifacts to set
            
        Returns:
            self for method chaining
        """
        self.generatedArtifacts = value
        return self

    def getHwElementRefs(self):
        """
        Gets the list of hardware element references for this implementation.
        
        Returns:
            List of RefType instances
        """
        return self.hwElementRefs

    def setHwElementRefs(self, value):
        """
        Sets the list of hardware element references for this implementation.
        Only sets the value if it is not None.
        
        Args:
            value: The list of hardware element references to set
            
        Returns:
            self for method chaining
        """
        self.hwElementRefs = value
        return self

    def getLinkers(self):
        """
        Gets the list of linkers used in this implementation.
        
        Returns:
            List of Linker instances
        """
        return self.linkers

    def setLinkers(self, value):
        """
        Sets the list of linkers used in this implementation.
        Only sets the value if it is not None.
        
        Args:
            value: The list of linkers to set
            
        Returns:
            self for method chaining
        """
        self.linkers = value
        return self

    def getMcSupport(self):
        """
        Gets the microcontroller support information for this implementation.
        
        Returns:
            Microcontroller support information
        """
        return self.mcSupport

    def setMcSupport(self, value):
        """
        Sets the microcontroller support information for this implementation.
        
        Args:
            value: The microcontroller support information to set
            
        Returns:
            self for method chaining
        """
        self.mcSupport = value
        return self

    def getProgrammingLanguage(self):
        """
        Gets the programming language used in this implementation.
        
        Returns:
            ProgramminglanguageEnum: The programming language
        """
        return self.programmingLanguage

    def setProgrammingLanguage(self, value):
        """
        Sets the programming language used in this implementation.
        Only sets the value if it is not None.
        
        Args:
            value: The programming language to set
            
        Returns:
            self for method chaining
        """
        self.programmingLanguage = value
        return self

    def getRequiredArtifacts(self):
        """
        Gets the list of required artifacts for this implementation.
        
        Returns:
            List of DependencyOnArtifact instances
        """
        return self.requiredArtifacts

    def setRequiredArtifacts(self, value):
        """
        Sets the list of required artifacts for this implementation.
        Only sets the value if it is not None.
        
        Args:
            value: The list of required artifacts to set
            
        Returns:
            self for method chaining
        """
        self.requiredArtifacts = value
        return self

    def getRequiredGeneratorTools(self):
        """
        Gets the list of required generator tools for this implementation.
        
        Returns:
            List of DependencyOnArtifact instances
        """
        return self.requiredGeneratorTools

    def setRequiredGeneratorTools(self, value):
        """
        Sets the list of required generator tools for this implementation.
        Only sets the value if it is not None.
        
        Args:
            value: The list of required generator tools to set
            
        Returns:
            self for method chaining
        """
        self.requiredGeneratorTools = value
        return self

    def getResourceConsumption(self):
        """
        Gets the resource consumption information for this implementation.
        
        Returns:
            ResourceConsumption: The resource consumption information
        """
        return self.resourceConsumption

    def createResourceConsumption(self, short_name: str) -> ResourceConsumption:
        """
        Creates and adds a ResourceConsumption to this implementation.
        
        Args:
            short_name: The short name for the new resource consumption
            
        Returns:
            The created ResourceConsumption instance
        """
        if (short_name not in self.elements):
            consumption = ResourceConsumption(self, short_name)
            self.addElement(consumption)
            self.resourceConsumption = consumption
        return self.getElement(short_name)

    def getSwcBswMappingRef(self):
        """
        Gets the reference to software component/BSW mapping for this implementation.
        
        Returns:
            RefType: The SWC/BSW mapping reference
        """
        return self.swcBswMappingRef

    def setSwcBswMappingRef(self, value):
        """
        Sets the reference to software component/BSW mapping for this implementation.
        Only sets the value if it is not None.
        
        Args:
            value: The SWC/BSW mapping reference to set
            
        Returns:
            self for method chaining
        """
        self.swcBswMappingRef = value
        return self

    def getSwVersion(self):
        """
        Gets the software version information for this implementation.
        
        Returns:
            RevisionLabelString: The software version information
        """
        return self.swVersion

    def setSwVersion(self, value):
        """
        Sets the software version information for this implementation.
        Only sets the value if it is not None.
        
        Args:
            value: The software version information to set
            
        Returns:
            self for method chaining
        """
        self.swVersion = value
        return self

    def getUsedCodeGenerator(self):
        """
        Gets the code generator used for this implementation.
        
        Returns:
            String: The used code generator
        """
        return self.usedCodeGenerator

    def setUsedCodeGenerator(self, value):
        """
        Sets the code generator used for this implementation.
        Only sets the value if it is not None.
        
        Args:
            value: The used code generator to set
            
        Returns:
            self for method chaining
        """
        self.usedCodeGenerator = value
        return self

    def getVendorId(self):
        """
        Gets the vendor ID for this implementation.
        
        Returns:
            PositiveInteger: The vendor ID
        """
        return self.vendorId

    def setVendorId(self, value):
        """
        Sets the vendor ID for this implementation.
        Only sets the value if it is not None.
        
        Args:
            value: The vendor ID to set
            
        Returns:
            self for method chaining
        """
        self.vendorId = value
        return self


    

    
