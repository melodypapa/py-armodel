from abc import ABCMeta
from typing import List
from ....M2.AUTOSARTemplates.CommonStructure.ResourceConsumption import ResourceConsumption
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject import AutosarEngineeringObject
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable, PackageableElement, Referrable
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType, ARLiteral, String
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class ImplementationProps(Referrable, metaclass = ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == ImplementationProps:
            raise NotImplementedError("ImplementationProps is an abstract class.")
        
        super().__init__(parent, short_name)

        self.symbol = None                          # type: ARLiteral

    def getSymbol(self):
        return self.symbol

    def setSymbol(self, value):
        self.symbol = value
        return self


class Code(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.artifactDescriptors = []          # type: List[AutosarEngineeringObject]
        self.callbackHeaderRefs = []            # type: List[RefType]

    def addArtifactDescriptor(self, desc: AutosarEngineeringObject):
        self.artifactDescriptors.append(desc)
        return self

    def getArtifactDescriptors(self, category:str = "") -> List[AutosarEngineeringObject]:
        if (category == ""):
            return self.artifactDescriptors
        else:
            return list(filter(lambda a: a.getCategory().getText() == category, self.artifactDescriptors))

class Compiler(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.name = None                                    # type: String
        self.options = None                                 # type: String
        self.vendor = None                                  # type: String
        self.version = None                                 # type: String

    def getName(self):
        return self.name

    def setName(self, value):
        self.name = value
        return self

    def getOptions(self):
        return self.options

    def setOptions(self, value):
        self.options = value
        return self

    def getVendor(self):
        return self.vendor

    def setVendor(self, value):
        self.vendor = value
        return self

    def getVersion(self):
        return self.version

    def setVersion(self, value):
        self.version = value
        return self
    
class DependencyOnArtifact(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # type: AutosarEngineeringObject
        self.artifactDescriptor = None
        self.usage = None                                   # type: DependencyUsageEnum

    def getArtifactDescriptor(self):
        return self.artifactDescriptor

    def setArtifactDescriptor(self, value):
        self.artifactDescriptor = value
        return self

    def getUsage(self):
        return self.usage

    def setUsage(self, value):
        self.usage = value
        return self


class Implementation(PackageableElement, metaclass = ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == Implementation:
            raise NotImplementedError("Implementation is an abstract class.")

        super().__init__(parent, short_name)

        self.buildActionManifestRef = None                  # type: RefType
        self.codeDescriptors = []                           # type: List[Code]
        self.compilers = []                                 # type: List[Compiler]
        self.generatedArtifacts = []                        # type: List[DependencyOnArtifact]
        self.hwElementRefs = []                             # type: List[RefType]
        self.linkers = []                                   # type: List[Linker]
        self.mcSupport = None
        self.programmingLanguage = None                     # type: ProgramminglanguageEnum
        self.requiredArtifacts = []                         # type: List[DependencyOnArtifact]
        self.requiredGeneratorTools = []                    # type: List[DependencyOnArtifact]
        self.resourceConsumption = None                     # type: ResourceConsumption
        self.swcBswMappingRef = None                        # type: RefType
        self.swVersion = []                                 # type: RevisionLabelString
        self.usedCodeGenerator = None                       # type: String
        self.vendorId = 0                                   # type: PositiveInteger

    def getBuildActionManifestRef(self):
        return self.buildActionManifestRef

    def setBuildActionManifestRef(self, value):
        self.buildActionManifestRef = value
        return self

    def getCodeDescriptors(self)-> List[Code]:
        return list(filter(lambda a : isinstance(a, Code), self.elements.values()))

    def createCodeDescriptor(self, short_name: str) -> Code:
        if (short_name not in self.elements):
            code_descriptor = Code(self, short_name)
            self.addElement(code_descriptor)
            self.codeDescriptors.append(code_descriptor)
        return self.getElement(short_name)

    def getCompilers(self):
        return self.compilers

    def setCompilers(self, value):
        self.compilers = value
        return self

    def getGeneratedArtifacts(self):
        return self.generatedArtifacts

    def setGeneratedArtifacts(self, value):
        self.generatedArtifacts = value
        return self

    def getHwElementRefs(self):
        return self.hwElementRefs

    def setHwElementRefs(self, value):
        self.hwElementRefs = value
        return self

    def getLinkers(self):
        return self.linkers

    def setLinkers(self, value):
        self.linkers = value
        return self

    def getMcSupport(self):
        return self.mcSupport

    def setMcSupport(self, value):
        self.mcSupport = value
        return self

    def getProgrammingLanguage(self):
        return self.programmingLanguage

    def setProgrammingLanguage(self, value):
        self.programmingLanguage = value
        return self

    def getRequiredArtifacts(self):
        return self.requiredArtifacts

    def setRequiredArtifacts(self, value):
        self.requiredArtifacts = value
        return self

    def getRequiredGeneratorTools(self):
        return self.requiredGeneratorTools

    def setRequiredGeneratorTools(self, value):
        self.requiredGeneratorTools = value
        return self

    def getResourceConsumption(self):
        return self.resourceConsumption

    def createResourceConsumption(self, short_name: str) -> ResourceConsumption:
        if (short_name not in self.elements):
            consumption = ResourceConsumption(self, short_name)
            self.addElement(consumption)
            self.resourceConsumption = consumption
        return self.getElement(short_name)

    def getSwcBswMappingRef(self):
        return self.swcBswMappingRef

    def setSwcBswMappingRef(self, value):
        self.swcBswMappingRef = value
        return self

    def getSwVersion(self):
        return self.swVersion

    def setSwVersion(self, value):
        self.swVersion = value
        return self

    def getUsedCodeGenerator(self):
        return self.usedCodeGenerator

    def setUsedCodeGenerator(self, value):
        self.usedCodeGenerator = value
        return self

    def getVendorId(self):
        return self.vendorId

    def setVendorId(self, value):
        self.vendorId = value
        return self


    

    
