from ..GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ..GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, Identifier, RefType
from ..CommonStructure.Implementation import Implementation
from typing import List

class BswImplementation(Implementation):
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.arReleaseVersion = None                        # type: RevisionLabelString
        self.behaviorRef = None                             # type: RefType
        self.preconfiguredConfigurationRefs = []            # type: List[RefType]
        self.recommendedConfigurationRefs = []              # type: List[RefType]
        self.vendorApiInfix = None                          # type: Identifier
        self.vendorSpecificModuleDefRefs = []               # type: List[RefType]

    def getArReleaseVersion(self):
        return self.arReleaseVersion

    def setArReleaseVersion(self, value):
        self.arReleaseVersion = value
        return self

    def getBehaviorRef(self):
        return self.behaviorRef

    def setBehaviorRef(self, value):
        self.behaviorRef = value
        return self

    def getPreconfiguredConfigurationRefs(self):
        return self.preconfiguredConfigurationRefs

    def addPreconfiguredConfigurationRef(self, value):
        self.preconfiguredConfigurationRefs.append(value)
        return self

    def getRecommendedConfigurationRefs(self):
        return self.recommendedConfigurationRefs

    def addRecommendedConfigurationRef(self, value):
        self.recommendedConfigurationRefs.append(value)
        return self

    def getVendorApiInfix(self):
        return self.vendorApiInfix

    def setVendorApiInfix(self, value):
        self.vendorApiInfix = value
        return self

    def getVendorSpecificModuleDefRefs(self):
        return self.vendorSpecificModuleDefRefs

    def addVendorSpecificModuleDefRef(self, value):
        self.vendorSpecificModuleDefRefs.append(value)
        return self


   