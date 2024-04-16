from abc import ABCMeta
from typing import List
from .ar_object import ARObject
from .general_structure import PackageableElement, Identifiable
from .common_structure import ResourceConsumption
from .ar_ref import RefType

class EngineeringObject(ARObject, metaclass=ABCMeta):
    def __init__(self):
        if type(self) == EngineeringObject:
            raise NotImplementedError("EngineeringObject is an abstract class.")

        super().__init__()

        self.category = ""
        self.domain = None                  # type: str
        self.revision_label = None          # type: str
        self.short_label = ""               # type: str

class AutosarEngineeringObject(EngineeringObject):
    def __init__(self):
        super().__init__()

class Code(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.artifact_descriptors = []          # type: List[AutosarEngineeringObject]
        self.callback_header_refs = []          # type: List[RefType]

    def addArtifactDescriptor(self, desc: AutosarEngineeringObject):
        self.artifact_descriptors.append(desc)

    def getArtifactDescriptors(self, category:str = "") -> List[AutosarEngineeringObject]:
        if (category == ""):
            return self.artifact_descriptors
        else:
            return list(filter(lambda a: a.category == category, self.artifact_descriptors))

class Implementation(PackageableElement, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str) -> None:
        if type(self) == Implementation:
            raise NotImplementedError("Implementation is an abstract class.")

        super().__init__(parent, short_name)
        self.build_action_manifest = None       # 0..1   
        self.compiler = None                    # *
        self.generated_artifact = None          # *
        self.hw_element = None                  # *
        self.linker = None                      # *
        self.mc_support = None                   # 0..1
        self.programming_language = ""          # 1
        self.required_artifact = None           # *
        self.required_generator_tool = None     # *
        self.resource_consumption = None        # type: ResourceConsumption
        self.sw_version = ""                    # 1
        self.swc_bsw_mapping_ref = None         # type: RefType
        self.used_code_generator = ""           # 0..1
        self.vendor_id = 0                      # 1

    def createCodeDescriptor(self, short_name: str) -> Code:
        if (short_name not in self.elements):
            sw_component = Code(self, short_name)
            self.elements[short_name] = sw_component
        return self.elements[short_name]

    def getCodeDescriptors(self)-> List[Code]:
        return list(filter(lambda a : isinstance(a, Code), self.elements.values()))

class BswImplementation(Implementation):
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.ar_release_version = ""
        self.revision_label_string = ""                 # 1
        self.behavior_ref = None                        # type: RefType
        self.preconfigured_configuration_ref = None     # *
        self.recommended_configuration_ref = None       # *
        self.vendor_api_infix = ""                      # 0..1
        self.vendor_specific_module_def_ref = None      # *

class SwcImplementation(Implementation):
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.behavior_ref = None                        # type: RefType
        self.per_instance_memory_size = None
        self.required_rte_vendor = ""