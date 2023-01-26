from abc import ABCMeta
from typing import List
from . import PackageableElement, ARObject

class Implementation(PackageableElement, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)
        self.build_action_manifest = None       # 0..1   
        self.code_descriptor = None             # 1..*
        self.compiler = None                    # *
        self.generated_artifact = None          # *
        self.hw_element = None                  # *
        self.linker = None                      # *
        self.mc_support = None                   # 0..1
        self.programming_language = ""          # 1
        self.required_artifact = None           # *
        self.required_generator_tool = None     # *
        self.resource_consumption = None        # 1
        self.sw_version = ""                    # 1
        self.swc_bsw_mapping = None             # 0..1
        self.used_code_generator = ""           # 0..1
        self.vendor_id = 0                      # 1

class BswImplementation(Implementation):
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)
        self.revision_label_string = ""                 # 1
        self.behavior = None                            # 1
        self.preconfigured_configuration_ref = None     # *
        self.recommended_configuration_ref = None       # *
        self.vendor_api_infix = ""                      # 0..1
        self.vendor_specific_module_def_ref = None      # *