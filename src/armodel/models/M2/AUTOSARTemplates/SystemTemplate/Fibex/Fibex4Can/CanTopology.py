from abc import ABCMeta

from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Float, Integer, PositiveInteger
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveUnlimitedInteger, TimeValue
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ......M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommunicationConnector, CommunicationController


class CanControllerFdConfiguration(ARObject):
    def __init__(self):
        super().__init__()

        self.paddingValue = None                                        # type: PositiveInteger
        self.propSeg = None                                             # type: PositiveInteger
        self.sspOffset = None                                           # type: PositiveInteger
        self.syncJumpWidth = None                                       # type: PositiveInteger
        self.timeSeg1 = None                                            # type: PositiveInteger
        self.timeSeg2 = None                                            # type: PositiveInteger
        self.txBitRateSwitch = None                                     # type: Boolean

    def getPaddingValue(self):
        return self.paddingValue

    def setPaddingValue(self, value):
        if value is not None:
            self.paddingValue = value
        return self

    def getPropSeg(self):
        return self.propSeg

    def setPropSeg(self, value):
        if value is not None:
            self.propSeg = value
        return self

    def getSspOffset(self):
        return self.sspOffset

    def setSspOffset(self, value):
        if value is not None:
            self.sspOffset = value
        return self

    def getSyncJumpWidth(self):
        return self.syncJumpWidth

    def setSyncJumpWidth(self, value):
        if value is not None:
            self.syncJumpWidth = value
        return self

    def getTimeSeg1(self):
        return self.timeSeg1

    def setTimeSeg1(self, value):
        if value is not None:
            self.timeSeg1 = value
        return self

    def getTimeSeg2(self):
        return self.timeSeg2

    def setTimeSeg2(self, value):
        if value is not None:
            self.timeSeg2 = value
        return self

    def getTxBitRateSwitch(self):
        return self.txBitRateSwitch

    def setTxBitRateSwitch(self, value):
        if value is not None:
            self.txBitRateSwitch = value
        return self


class CanControllerFdConfigurationRequirements(ARObject):
    def __init__(self):
        super().__init__()

        self.maxNumberOfTimeQuantaPerBit = None                         # type: Integer
        self.maxSamplePoint = None                                      # type: Float
        self.maxSyncJumpWidth = None                                    # type: Float
        self.maxTrcvDelayCompensationOffset = None                      # type: TimeValue
        self.minNumberOfTimeQuantaPerBit = None                         # type: Integer
        self.minSamplePoint = None                                      # type: Float
        self.minSyncJumpWidth = None                                    # type: Float
        self.minTrcvDelayCompensationOffset = None                      # type: TimeValue
        self.paddingValue = None                                        # type: PositiveInteger
        self.txBitRateSwitch = None                                     # type: Boolean

    def getMaxNumberOfTimeQuantaPerBit(self):
        return self.maxNumberOfTimeQuantaPerBit

    def setMaxNumberOfTimeQuantaPerBit(self, value):
        if value is not None:
            self.maxNumberOfTimeQuantaPerBit = value
        return self

    def getMaxSamplePoint(self):
        return self.maxSamplePoint

    def setMaxSamplePoint(self, value):
        if value is not None:
            self.maxSamplePoint = value
        return self

    def getMaxSyncJumpWidth(self):
        return self.maxSyncJumpWidth

    def setMaxSyncJumpWidth(self, value):
        if value is not None:
            self.maxSyncJumpWidth = value
        return self

    def getMaxTrcvDelayCompensationOffset(self):
        return self.maxTrcvDelayCompensationOffset

    def setMaxTrcvDelayCompensationOffset(self, value):
        if value is not None:
            self.maxTrcvDelayCompensationOffset = value
        return self

    def getMinNumberOfTimeQuantaPerBit(self):
        return self.minNumberOfTimeQuantaPerBit

    def setMinNumberOfTimeQuantaPerBit(self, value):
        if value is not None:
            self.minNumberOfTimeQuantaPerBit = value
        return self

    def getMinSamplePoint(self):
        return self.minSamplePoint

    def setMinSamplePoint(self, value):
        if value is not None:
            self.minSamplePoint = value
        return self

    def getMinSyncJumpWidth(self):
        return self.minSyncJumpWidth

    def setMinSyncJumpWidth(self, value):
        if value is not None:
            self.minSyncJumpWidth = value
        return self

    def getMinTrcvDelayCompensationOffset(self):
        return self.minTrcvDelayCompensationOffset

    def setMinTrcvDelayCompensationOffset(self, value):
        if value is not None:
            self.minTrcvDelayCompensationOffset = value
        return self

    def getPaddingValue(self):
        return self.paddingValue

    def setPaddingValue(self, value):
        if value is not None:
            self.paddingValue = value
        return self

    def getTxBitRateSwitch(self):
        return self.txBitRateSwitch

    def setTxBitRateSwitch(self, value):
        if value is not None:
            self.txBitRateSwitch = value
        return self


class AbstractCanCommunicationControllerAttributes(ARObject, metaclass=ABCMeta):
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


class AbstractCanCommunicationController(CommunicationController, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AbstractCanCommunicationController:
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


class AbstractCanCommunicationConnector(CommunicationConnector, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AbstractCanCommunicationConnector:
            raise NotImplementedError("AbstractCanCommunicationConnector is an abstract class.")
        
        super().__init__(parent, short_name)


class CanCommunicationConnector(AbstractCanCommunicationConnector):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.pncWakeupCanId = None                                  # type: PositiveInteger
        self.pncWakeupCanIdExtended = None                          # type: Boolean
        self.pncWakeupCanIdMask = None                              # type: PositiveInteger
        self.pncWakeupDataMask = None                               # type: PositiveUnlimitedInteger
        self.pncWakeupDlc = None                                    # type: PositiveInteger

    def getPncWakeupCanId(self):
        return self.pncWakeupCanId

    def setPncWakeupCanId(self, value):
        if value is not None:
            self.pncWakeupCanId = value
        return self

    def getPncWakeupCanIdExtended(self):
        return self.pncWakeupCanIdExtended

    def setPncWakeupCanIdExtended(self, value):
        if value is not None:
            self.pncWakeupCanIdExtended = value
        return self

    def getPncWakeupCanIdMask(self):
        return self.pncWakeupCanIdMask

    def setPncWakeupCanIdMask(self, value):
        if value is not None:
            self.pncWakeupCanIdMask = value
        return self

    def getPncWakeupDataMask(self):
        return self.pncWakeupDataMask

    def setPncWakeupDataMask(self, value):
        if value is not None:
            self.pncWakeupDataMask = value
        return self

    def getPncWakeupDlc(self):
        return self.pncWakeupDlc

    def setPncWakeupDlc(self, value):
        if value is not None:
            self.pncWakeupDlc = value
        return self
