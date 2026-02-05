"""
This module contains classes for representing AUTOSAR port API options
in software component internal behavior templates.
"""

from armodel.models_v2.M2.AUTOSARTemplates.CommonStructure import ValueSpecification
from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARBoolean, RefType, TRefType
from typing import List

class PortDefinedArgumentValue(ARObject):
    def __init__(self):
        super().__init__()

        self.value: 'ValueSpecification' = None
        self.valueTypeTRef: 'TRefType' = None

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

        self.enableTakeAddress: ARBoolean = None
        self.errorHandling = None
        self.indirectAPI: ARBoolean = None
        self.portRef: RefType = None
        self.portArgValues: List['PortDefinedArgumentValue'] = []
        self.supportedFeatures = []
        self.transformerStatusForwarding = None

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
