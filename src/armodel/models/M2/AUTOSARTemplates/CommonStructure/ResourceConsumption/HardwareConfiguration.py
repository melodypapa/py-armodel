from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class HardwareConfiguration(ARObject):
    def __init__(self):
        super().__init__()

        self.additionalInformation = None                       # type: String
        self.processorMode = None                               # type: String
        self.processorSpeed = None                              # type: String

    def getAdditionalInformation(self):
        return self.additionalInformation

    def setAdditionalInformation(self, value):
        self.additionalInformation = value
        return self

    def getProcessorMode(self):
        return self.processorMode

    def setProcessorMode(self, value):
        self.processorMode = value
        return self

    def getProcessorSpeed(self):
        return self.processorSpeed

    def setProcessorSpeed(self, value):
        self.processorSpeed = value
        return self

        