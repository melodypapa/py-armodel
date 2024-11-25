from abc import ABCMeta

from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Float, Integer, PositiveInteger, PositiveUnlimitedInteger
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ......M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommunicationConnector, CommunicationController

class AbstractCanCommunicationControllerAttributes(ARObject, metaclass = ABCMeta):
    def __init__(self):
        super().__init__()

        self.canControllerFdAttributes = None                           # type: CanControllerFdConfiguration
        self.canControllerFdRequirements = None                         # type: CanControllerFdConfigurationRequirements
        self.canControllerXlAttributes = None                           # type: CanControllerXlConfiguration
        self.canControllerXlRequirements = None                         # type: CanControllerXlConfigurationRequirements

    def getCanControllerFdAttributes(self):
        return self.canControllerFdAttributes

    def setCanControllerFdAttributes(self, value):
        self.canControllerFdAttributes = value
        return self

    def getCanControllerFdRequirements(self):
        return self.canControllerFdRequirements

    def setCanControllerFdRequirements(self, value):
        self.canControllerFdRequirements = value
        return self

    def getCanControllerXlAttributes(self):
        return self.canControllerXlAttributes

    def setCanControllerXlAttributes(self, value):
        self.canControllerXlAttributes = value
        return self

    def getCanControllerXlRequirements(self):
        return self.canControllerXlRequirements

    def setCanControllerXlRequirements(self, value):
        self.canControllerXlRequirements = value
        return self

class CanControllerConfigurationRequirements(AbstractCanCommunicationControllerAttributes):
    def __init__(self):
        super().__init__()

        self.maxNumberOfTimeQuantaPerBit = None                         # type: Integer
        self.maxSamplePoint = None                                      # type: Float
        self.maxSyncJumpWidth = None                                    # type: Float
        self.minNumberOfTimeQuantaPerBit = None                         # type: Integer
        self.minSamplePoint = None                                      # type: Float
        self.minSyncJumpWidth = None                                    # type: Float

    def getMaxNumberOfTimeQuantaPerBit(self):
        return self.maxNumberOfTimeQuantaPerBit

    def setMaxNumberOfTimeQuantaPerBit(self, value):
        self.maxNumberOfTimeQuantaPerBit = value
        return self

    def getMaxSamplePoint(self):
        return self.maxSamplePoint

    def setMaxSamplePoint(self, value):
        self.maxSamplePoint = value
        return self

    def getMaxSyncJumpWidth(self):
        return self.maxSyncJumpWidth

    def setMaxSyncJumpWidth(self, value):
        self.maxSyncJumpWidth = value
        return self

    def getMinNumberOfTimeQuantaPerBit(self):
        return self.minNumberOfTimeQuantaPerBit

    def setMinNumberOfTimeQuantaPerBit(self, value):
        self.minNumberOfTimeQuantaPerBit = value
        return self

    def getMinSamplePoint(self):
        return self.minSamplePoint

    def setMinSamplePoint(self, value):
        self.minSamplePoint = value
        return self

    def getMinSyncJumpWidth(self):
        return self.minSyncJumpWidth

    def setMinSyncJumpWidth(self, value):
        self.minSyncJumpWidth = value
        return self



class AbstractCanCommunicationController(CommunicationController, metaclass = ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == AbstractCanCommunicationController:
            raise NotImplementedError("AbstractCanCommunicationController is an abstract class.")
        
        super().__init__(parent, short_name)

        self.canControllerAttributes = None                             # type: AbstractCanCommunicationControllerAttributes

    def getCanControllerAttributes(self):
        return self.canControllerAttributes

    def setCanControllerAttributes(self, value):
        self.canControllerAttributes = value
        return self

class CanCommunicationController(AbstractCanCommunicationController):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

class AbstractCanCommunicationConnector(CommunicationConnector, metaclass = ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == AbstractCanCommunicationConnector:
            raise NotImplementedError("AbstractCanCommunicationConnector is an abstract class.")
        
        super().__init__(parent, short_name)

class CanCommunicationConnector(AbstractCanCommunicationConnector):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)  

        # type: PositiveInteger
        self.pncWakeupCanId = None
        self.pncWakeupCanIdExtended = None                          # type: Boolean
        # type: PositiveInteger
        self.pncWakeupCanIdMask = None
        # type: PositiveUnlimitedInteger
        self.pncWakeupDataMask = None
        # type: PositiveInteger
        self.pncWakeupDlc = None

    def getPncWakeupCanId(self):
        return self.pncWakeupCanId

    def setPncWakeupCanId(self, value):
        self.pncWakeupCanId = value
        return self

    def getPncWakeupCanIdExtended(self):
        return self.pncWakeupCanIdExtended

    def setPncWakeupCanIdExtended(self, value):
        self.pncWakeupCanIdExtended = value
        return self

    def getPncWakeupCanIdMask(self):
        return self.pncWakeupCanIdMask

    def setPncWakeupCanIdMask(self, value):
        self.pncWakeupCanIdMask = value
        return self

    def getPncWakeupDataMask(self):
        return self.pncWakeupDataMask

    def setPncWakeupDataMask(self, value):
        self.pncWakeupDataMask = value
        return self

    def getPncWakeupDlc(self):
        return self.pncWakeupDlc

    def setPncWakeupDlc(self, value):
        self.pncWakeupDlc = value
        return self
