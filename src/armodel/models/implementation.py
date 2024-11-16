from abc import ABCMeta
from typing import List

from .M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject import AutosarEngineeringObject
from .M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from .M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from .M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARNumerical
from .M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral
from .M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import PackageableElement
from .M2.AUTOSARTemplates.CommonStructure.ResourceConsumption import ResourceConsumption
from .M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

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
        