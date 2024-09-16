from abc import ABCMeta
from typing import List
from .ar_object import ARLiteral, ARNumerical, ARObject
from .general_structure import PackageableElement, Identifiable
from .common_structure import ResourceConsumption
from .ar_ref import RefType

class EngineeringObject(ARObject, metaclass=ABCMeta):
    def __init__(self):
        if type(self) == EngineeringObject:
            raise NotImplementedError("EngineeringObject is an abstract class.")

        super().__init__()

        self.category = None                # type: ARLiteral
        self.domain = None                  # type: ARLiteral
        self.revision_label = None           # type: ARLiteral
        self.short_label = None              # type: ARLiteral

    def setCategory(self, category: any):
        if isinstance(category, ARLiteral):
            self.category = category
        else:
            self.category = ARLiteral()
            self.category.setValue(str(category))
        return self
    
    def getCategory(self) -> ARLiteral:
        return self.category
    
    def setDomain(self, domain: ARLiteral):
        self.domain = domain
        return self
    
    def getDomain(self) -> ARLiteral:
        return self.domain
    
    def setRevisionLabel(self, revision_label: ARLiteral):
        self.revision_label = revision_label
        return self
    
    def getRevisionLabel(self) -> ARLiteral:
        return self.revision_label
    
    def setShortLabel(self, label: ARLiteral):
        self.short_label = label
        return self
    
    def getShortLabel(self) -> ARLiteral:
        return self.short_label

class AutosarEngineeringObject(EngineeringObject):
    def __init__(self):
        super().__init__()

class Code(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self._artifactDescriptors = []          # type: List[AutosarEngineeringObject]
        self.callbackHeaderRefs = []            # type: List[RefType]

    def addArtifactDescriptor(self, desc: AutosarEngineeringObject):
        self._artifactDescriptors.append(desc)

    def getArtifactDescriptors(self, category:str = "") -> List[AutosarEngineeringObject]:
        if (category == ""):
            return self._artifactDescriptors
        else:
            return list(filter(lambda a: a.getCategory().getText() == category, self._artifactDescriptors))

class Implementation(PackageableElement, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str) -> None:
        if type(self) == Implementation:
            raise NotImplementedError("Implementation is an abstract class.")

        super().__init__(parent, short_name)

        self.build_action_manifest_ref = None               # type: RefType
        self.compilers = None                           
        self.generated_artifacts = None          
        self.hw_element_refs = []                           # type: List[RefType]
        self.linker = []                      
        self.mc_support = None                           
        self.programming_language = None                    # type: ARLiteral
        self.required_artifacts = []           
        self.required_generator_tools = []
        self.resource_consumption = None                    # type: ResourceConsumption
        self.sw_version = ""                                # type: ARLiteral
        self.swc_bsw_mapping_ref = None                     # type: RefType
        self.used_code_generator = None                     # type: ARLiteral
        self.vendor_id = 0                                  # type: ARNumerical

    def createCodeDescriptor(self, short_name: str) -> Code:
        if (short_name not in self.elements):
            sw_component = Code(self, short_name)
            self.elements[short_name] = sw_component
        return self.elements[short_name]

    def getCodeDescriptors(self)-> List[Code]:
        return list(filter(lambda a : isinstance(a, Code), self.elements.values()))

    def setResourceConsumption(self, consumption: ResourceConsumption):
        self.elements[consumption.short_name] = consumption
        self.resource_consumption = consumption
        return self
    
    def getResourceConsumption(self) -> ResourceConsumption:
        return self.resource_consumption

class BswImplementation(Implementation):
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.ar_release_version = None                      # type: ARLiteral
        self.behavior_ref = None                            # type: RefType
        self.preconfiguredConfigurationRef = []             # type: List[RefType]
        self.recommendedConfigurationRef = []               # type: List[RefType]
        self.vendorApiInfix = None                          # type: str
        self._vendorSpecificModuleDefRef = []               # type: List[RefType]

    def addVendorSpecificModuleDefRef(self, ref: RefType):
        self._vendorSpecificModuleDefRef.append(ref)

    def getVendorSpecificModuleDefRefs(self):
        return self._vendorSpecificModuleDefRef
    
class SwcImplementation(Implementation):
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.behavior_ref = None                        # type: RefType
        self.per_instance_memory_size = None
        self.required_rte_vendor = ""
        