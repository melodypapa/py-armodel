from .....M2.AUTOSARTemplates.CommonStructure import ValueSpecification
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARBoolean, RefType, TRefType
from typing import List

class PortDefinedArgumentValue(ARObject):
    def __init__(self):
        super().__init__()

        self.value = None                       # type: ValueSpecification
        self.valueTypeTRef = None               # type: TRefType

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value
        return self

    def getValueTypeTRef(self):
        return self.valueTypeTRef

    def setValueTypeTRef(self, value):
        self.valueTypeTRef = value
        return self

class PortAPIOption(ARObject):
    def __init__(self):
        super().__init__()

        self.enableTakeAddress = None               # type: ARBoolean
        self.errorHandling = None                   # type: DataTransformationErrorHandlingEnum
        self.indirectAPI = None                     # type: ARBoolean
        self.portRef = None                         # type: RefType
        self.portArgValues = []                     # type: List[PortDefinedArgumentValue]
        self.supportedFeatures = []                 # type: List[SwcSupportedFeature]
        self.transformerStatusForwarding = None     # type: DataTransformationStatusForwardingEnum

    def getEnableTakeAddress(self):
        return self.enableTakeAddress

    def setEnableTakeAddress(self, value):
        self.enableTakeAddress = value
        return self

    def getErrorHandling(self):
        return self.errorHandling

    def setErrorHandling(self, value):
        self.errorHandling = value
        return self

    def getIndirectAPI(self):
        return self.indirectAPI

    def setIndirectAPI(self, value):
        self.indirectAPI = value
        return self

    def getPortRef(self):
        return self.portRef

    def setPortRef(self, value):
        self.portRef = value
        return self

    def getPortArgValues(self):
        return self.portArgValues

    def addPortArgValue(self, value):
        self.portArgValues.append(value)
        return self

    def getSupportedFeatures(self):
        return self.supportedFeatures

    def addSupportedFeature(self, value):
        self.supportedFeatures.append(value)
        return self

    def getTransformerStatusForwarding(self):
        return self.transformerStatusForwarding

    def setTransformerStatusForwarding(self, value):
        self.transformerStatusForwarding = value
        return self
