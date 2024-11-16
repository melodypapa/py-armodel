from abc import ABCMeta
from typing import List
from .ResourceConsumption import ResourceConsumption
from ..GenericStructure.GeneralTemplateClasses.EngineeringObject import AutosarEngineeringObject
from ..GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable, PackageableElement, Referrable
from ..GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARNumerical, RefType, ARLiteral
from ..GenericStructure.GeneralTemplateClasses.ArObject import ARObject


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
