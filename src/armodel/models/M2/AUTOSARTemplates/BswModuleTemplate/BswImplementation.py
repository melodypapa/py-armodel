from ..GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ..GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, RefType
from ..CommonStructure.Implementation import Implementation
from typing import List

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