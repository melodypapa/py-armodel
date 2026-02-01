from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Float, Integer, PositiveInteger
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveUnlimitedInteger, TimeValue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommunicationCluster, CommunicationConnector
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommunicationController


class FlexrayCommunicationController(CommunicationController):
    """
    Represents a FlexRay communication controller in the system,
    defining properties for FlexRay network communication including
    startup parameters, timing, and synchronization settings for
    time-triggered communication.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.acceptedStartupRange: Integer = None
        self.allowHaltDueToClock: Boolean = None
        self.allowPassiveToActive: Integer = None
        self.clusterDriftDamping: Integer = None
        self.decodingCorrection: Integer = None
        self.delayCompensationA: Integer = None
        self.delayCompensationB: Integer = None
        self.externOffsetCorrection: Integer = None
        self.externRateCorrection: Integer = None
        self.externalSync: Boolean = None
        self.fallBackInternal: Boolean = None
        self.flexrayFifos = []
        self.keySlotID: PositiveInteger = None
        self.keySlotOnlyEnabled: Boolean = None
        self.keySlotUsedForStartUp: Boolean = None
        self.keySlotUsedForSync: Boolean = None
        self.latestTX: Integer = None
        self.listenTimeout: Integer = None
        self.macroInitialOffsetA: Integer = None
        self.macroInitialOffsetB: Integer = None
        self.maximumDynamicPayloadLength: Integer = None
        self.microInitialOffsetA: Integer = None
        self.microInitialOffsetB: Integer = None
        self.microPerCycle: Integer = None
        self.microtickDuration: TimeValue = None
        self.nmVectorEarlyUpdate: Boolean = None
        self.offsetCorrectionOut: Integer = None
        self.rateCorrectionOut: Integer = None
        self.samplesPerMicrotick: Integer = None
        self.secondKeySlotId: PositiveInteger = None
        self.twoKeySlotMode: Boolean = None
        self.wakeUpPattern: Integer = None

    def getAcceptedStartupRange(self):
        return self.acceptedStartupRange

    def setAcceptedStartupRange(self, value):
        if value is not None:
            self.acceptedStartupRange = value
        return self

    def getAllowHaltDueToClock(self):
        return self.allowHaltDueToClock

    def setAllowHaltDueToClock(self, value):
        if value is not None:
            self.allowHaltDueToClock = value
        return self

    def getAllowPassiveToActive(self):
        return self.allowPassiveToActive

    def setAllowPassiveToActive(self, value):
        if value is not None:
            self.allowPassiveToActive = value
        return self

    def getClusterDriftDamping(self):
        return self.clusterDriftDamping

    def setClusterDriftDamping(self, value):
        if value is not None:
            self.clusterDriftDamping = value
        return self

    def getDecodingCorrection(self):
        return self.decodingCorrection

    def setDecodingCorrection(self, value):
        if value is not None:
            self.decodingCorrection = value
        return self

    def getDelayCompensationA(self):
        return self.delayCompensationA

    def setDelayCompensationA(self, value):
        if value is not None:
            self.delayCompensationA = value
        return self

    def getDelayCompensationB(self):
        return self.delayCompensationB

    def setDelayCompensationB(self, value):
        if value is not None:
            self.delayCompensationB = value
        return self

    def getExternOffsetCorrection(self):
        return self.externOffsetCorrection

    def setExternOffsetCorrection(self, value):
        if value is not None:
            self.externOffsetCorrection = value
        return self

    def getExternRateCorrection(self):
        return self.externRateCorrection

    def setExternRateCorrection(self, value):
        if value is not None:
            self.externRateCorrection = value
        return self

    def getExternalSync(self):
        return self.externalSync

    def setExternalSync(self, value):
        if value is not None:
            self.externalSync = value
        return self

    def getFallBackInternal(self):
        return self.fallBackInternal

    def setFallBackInternal(self, value):
        if value is not None:
            self.fallBackInternal = value
        return self

    def getFlexrayFifos(self):
        return self.flexrayFifos

    def setFlexrayFifos(self, value):
        if value is not None:
            self.flexrayFifos = value
        return self

    def getKeySlotID(self):
        return self.keySlotID

    def setKeySlotID(self, value):
        if value is not None:
            self.keySlotID = value
        return self

    def getKeySlotOnlyEnabled(self):
        return self.keySlotOnlyEnabled

    def setKeySlotOnlyEnabled(self, value):
        if value is not None:
            self.keySlotOnlyEnabled = value
        return self

    def getKeySlotUsedForStartUp(self):
        return self.keySlotUsedForStartUp

    def setKeySlotUsedForStartUp(self, value):
        if value is not None:
            self.keySlotUsedForStartUp = value
        return self

    def getKeySlotUsedForSync(self):
        return self.keySlotUsedForSync

    def setKeySlotUsedForSync(self, value):
        if value is not None:
            self.keySlotUsedForSync = value
        return self

    def getLatestTX(self):
        return self.latestTX

    def setLatestTX(self, value):
        if value is not None:
            self.latestTX = value
        return self

    def getListenTimeout(self):
        return self.listenTimeout

    def setListenTimeout(self, value):
        if value is not None:
            self.listenTimeout = value
        return self

    def getMacroInitialOffsetA(self):
        return self.macroInitialOffsetA

    def setMacroInitialOffsetA(self, value):
        if value is not None:
            self.macroInitialOffsetA = value
        return self

    def getMacroInitialOffsetB(self):
        return self.macroInitialOffsetB

    def setMacroInitialOffsetB(self, value):
        if value is not None:
            self.macroInitialOffsetB = value
        return self

    def getMaximumDynamicPayloadLength(self):
        return self.maximumDynamicPayloadLength

    def setMaximumDynamicPayloadLength(self, value):
        if value is not None:
            self.maximumDynamicPayloadLength = value
        return self

    def getMicroInitialOffsetA(self):
        return self.microInitialOffsetA

    def setMicroInitialOffsetA(self, value):
        if value is not None:
            self.microInitialOffsetA = value
        return self

    def getMicroInitialOffsetB(self):
        return self.microInitialOffsetB

    def setMicroInitialOffsetB(self, value):
        if value is not None:
            self.microInitialOffsetB = value
        return self

    def getMicroPerCycle(self):
        return self.microPerCycle

    def setMicroPerCycle(self, value):
        if value is not None:
            self.microPerCycle = value
        return self

    def getMicrotickDuration(self):
        return self.microtickDuration

    def setMicrotickDuration(self, value):
        if value is not None:
            self.microtickDuration = value
        return self

    def getNmVectorEarlyUpdate(self):
        return self.nmVectorEarlyUpdate

    def setNmVectorEarlyUpdate(self, value):
        if value is not None:
            self.nmVectorEarlyUpdate = value
        return self

    def getOffsetCorrectionOut(self):
        return self.offsetCorrectionOut

    def setOffsetCorrectionOut(self, value):
        if value is not None:
            self.offsetCorrectionOut = value
        return self

    def getRateCorrectionOut(self):
        return self.rateCorrectionOut

    def setRateCorrectionOut(self, value):
        if value is not None:
            self.rateCorrectionOut = value
        return self

    def getSamplesPerMicrotick(self):
        return self.samplesPerMicrotick

    def setSamplesPerMicrotick(self, value):
        if value is not None:
            self.samplesPerMicrotick = value
        return self

    def getSecondKeySlotId(self):
        return self.secondKeySlotId

    def setSecondKeySlotId(self, value):
        if value is not None:
            self.secondKeySlotId = value
        return self

    def getTwoKeySlotMode(self):
        return self.twoKeySlotMode

    def setTwoKeySlotMode(self, value):
        if value is not None:
            self.twoKeySlotMode = value
        return self

    def getWakeUpPattern(self):
        return self.wakeUpPattern

    def setWakeUpPattern(self, value):
        if value is not None:
            self.wakeUpPattern = value
        return self


class FlexrayCommunicationConnector(CommunicationConnector):
    """
    Defines a FlexRay communication connector that links FlexRay controllers
    to communication channels, specifying NM (Network Management) timing
    and PNC (Partial Network Cluster) properties for FlexRay communication.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.nmReadySleepTime: Float = None
        self.pncFilterDataMask: PositiveUnlimitedInteger = None
        self.wakeUpChannel: Boolean = None

    def getNmReadySleepTime(self):
        return self.nmReadySleepTime

    def setNmReadySleepTime(self, value):
        if value is not None:
            self.nmReadySleepTime = value
        return self

    def getPncFilterDataMask(self):
        return self.pncFilterDataMask

    def setPncFilterDataMask(self, value):
        if value is not None:
            self.pncFilterDataMask = value
        return self

    def getWakeUpChannel(self):
        return self.wakeUpChannel

    def setWakeUpChannel(self, value):
        if value is not None:
            self.wakeUpChannel = value
        return self


class FlexrayCluster(CommunicationCluster):
    """
    Defines a FlexRay communication cluster in the system topology,
    specifying timing parameters, slot configurations, and network
    management properties for FlexRay network communication.
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.actionPointOffset = None                       # type: Integer
        self.bit = None                                     # type: TimeValue
        self.casRxLowMax = None                             # type: Integer
        self.coldStartAttempts = None                       # type: Integer
        self.cycle = None                                   # type: TimeValue
        self.cycleCountMax = None                           # type: Integer
        self.detectNitError = None                          # type: Boolean
        self.dynamicSlotIdlePhase = None                    # type: Integer
        self.ignoreAfterTx = None                           # type: Integer
        self.listenNoise = None                             # type: Integer
        self.macroPerCycle = None                           # type: Integer
        self.macrotickDuration = None                       # type: TimeValue
        self.maxWithoutClockCorrectionFatal = None          # type: Integer
        self.maxWithoutClockCorrectionPassive = None        # type: Integer
        self.minislotActionPointOffset = None               # type: Integer
        self.minislotDuration = None                        # type: Integer
        self.networkIdleTime = None                         # type: Integer
        self.networkManagementVectorLength = None           # type: Integer
        self.numberOfMinislots = None                       # type: Integer
        self.numberOfStaticSlots = None                     # type: Integer
        self.offsetCorrectionStart = None                   # type: Integer
        self.payloadLengthStatic = None                     # type: Integer
        self.safetyMargin = None                            # type: Integer
        self.sampleClockPeriod = None                       # type: TimeValue
        self.staticSlotDuration = None                      # type: Integer
        self.symbolWindow = None                            # type: Integer
        self.symbolWindowActionPointOffset = None           # type: Integer
        self.syncFrameIdCountMax = None                     # type: Integer
        self.tranceiverStandbyDelay = None                  # type: Float
        self.transmissionStartSequenceDuration = None       # type: Integer
        self.wakeupRxIdle = None                            # type: Integer
        self.wakeupRxLow = None                             # type: Integer
        self.wakeupRxWindow = None                          # type: Integer
        self.wakeupTxActive = None                          # type: Integer
        self.wakeupTxIdle = None                            # type: Integer

    def getActionPointOffset(self):
        return self.actionPointOffset

    def setActionPointOffset(self, value):
        if value is not None:
            self.actionPointOffset = value
        return self

    def getBit(self):
        return self.bit

    def setBit(self, value):
        if value is not None:
            self.bit = value
        return self

    def getCasRxLowMax(self):
        return self.casRxLowMax

    def setCasRxLowMax(self, value):
        if value is not None:
            self.casRxLowMax = value
        return self

    def getColdStartAttempts(self):
        return self.coldStartAttempts

    def setColdStartAttempts(self, value):
        if value is not None:
            self.coldStartAttempts = value
        return self

    def getCycle(self):
        return self.cycle

    def setCycle(self, value):
        if value is not None:
            self.cycle = value
        return self

    def getCycleCountMax(self):
        return self.cycleCountMax

    def setCycleCountMax(self, value):
        if value is not None:
            self.cycleCountMax = value
        return self

    def getDetectNitError(self):
        return self.detectNitError

    def setDetectNitError(self, value):
        if value is not None:
            self.detectNitError = value
        return self

    def getDynamicSlotIdlePhase(self):
        return self.dynamicSlotIdlePhase

    def setDynamicSlotIdlePhase(self, value):
        if value is not None:
            self.dynamicSlotIdlePhase = value
        return self

    def getIgnoreAfterTx(self):
        return self.ignoreAfterTx

    def setIgnoreAfterTx(self, value):
        if value is not None:
            self.ignoreAfterTx = value
        return self

    def getListenNoise(self):
        return self.listenNoise

    def setListenNoise(self, value):
        if value is not None:
            self.listenNoise = value
        return self

    def getMacroPerCycle(self):
        return self.macroPerCycle

    def setMacroPerCycle(self, value):
        if value is not None:
            self.macroPerCycle = value
        return self

    def getMacrotickDuration(self):
        return self.macrotickDuration

    def setMacrotickDuration(self, value):
        if value is not None:
            self.macrotickDuration = value
        return self

    def getMaxWithoutClockCorrectionFatal(self):
        return self.maxWithoutClockCorrectionFatal

    def setMaxWithoutClockCorrectionFatal(self, value):
        if value is not None:
            self.maxWithoutClockCorrectionFatal = value
        return self

    def getMaxWithoutClockCorrectionPassive(self):
        return self.maxWithoutClockCorrectionPassive

    def setMaxWithoutClockCorrectionPassive(self, value):
        if value is not None:
            self.maxWithoutClockCorrectionPassive = value
        return self

    def getMinislotActionPointOffset(self):
        return self.minislotActionPointOffset

    def setMinislotActionPointOffset(self, value):
        if value is not None:
            self.minislotActionPointOffset = value
        return self

    def getMinislotDuration(self):
        return self.minislotDuration

    def setMinislotDuration(self, value):
        if value is not None:
            self.minislotDuration = value
        return self

    def getNetworkIdleTime(self):
        return self.networkIdleTime

    def setNetworkIdleTime(self, value):
        if value is not None:
            self.networkIdleTime = value
        return self

    def getNetworkManagementVectorLength(self):
        return self.networkManagementVectorLength

    def setNetworkManagementVectorLength(self, value):
        if value is not None:
            self.networkManagementVectorLength = value
        return self

    def getNumberOfMinislots(self):
        return self.numberOfMinislots

    def setNumberOfMinislots(self, value):
        if value is not None:
            self.numberOfMinislots = value
        return self

    def getNumberOfStaticSlots(self):
        return self.numberOfStaticSlots

    def setNumberOfStaticSlots(self, value):
        if value is not None:
            self.numberOfStaticSlots = value
        return self

    def getOffsetCorrectionStart(self):
        return self.offsetCorrectionStart

    def setOffsetCorrectionStart(self, value):
        if value is not None:
            self.offsetCorrectionStart = value
        return self

    def getPayloadLengthStatic(self):
        return self.payloadLengthStatic

    def setPayloadLengthStatic(self, value):
        if value is not None:
            self.payloadLengthStatic = value
        return self

    def getSafetyMargin(self):
        return self.safetyMargin

    def setSafetyMargin(self, value):
        if value is not None:
            self.safetyMargin = value
        return self

    def getSampleClockPeriod(self):
        return self.sampleClockPeriod

    def setSampleClockPeriod(self, value):
        if value is not None:
            self.sampleClockPeriod = value
        return self

    def getStaticSlotDuration(self):
        return self.staticSlotDuration

    def setStaticSlotDuration(self, value):
        if value is not None:
            self.staticSlotDuration = value
        return self

    def getSymbolWindow(self):
        return self.symbolWindow

    def setSymbolWindow(self, value):
        if value is not None:
            self.symbolWindow = value
        return self

    def getSymbolWindowActionPointOffset(self):
        return self.symbolWindowActionPointOffset

    def setSymbolWindowActionPointOffset(self, value):
        if value is not None:
            self.symbolWindowActionPointOffset = value
        return self

    def getSyncFrameIdCountMax(self):
        return self.syncFrameIdCountMax

    def setSyncFrameIdCountMax(self, value):
        if value is not None:
            self.syncFrameIdCountMax = value
        return self

    def getTranceiverStandbyDelay(self):
        return self.tranceiverStandbyDelay

    def setTranceiverStandbyDelay(self, value):
        if value is not None:
            self.tranceiverStandbyDelay = value
        return self

    def getTransmissionStartSequenceDuration(self):
        return self.transmissionStartSequenceDuration

    def setTransmissionStartSequenceDuration(self, value):
        if value is not None:
            self.transmissionStartSequenceDuration = value
        return self

    def getWakeupRxIdle(self):
        return self.wakeupRxIdle

    def setWakeupRxIdle(self, value):
        if value is not None:
            self.wakeupRxIdle = value
        return self

    def getWakeupRxLow(self):
        return self.wakeupRxLow

    def setWakeupRxLow(self, value):
        if value is not None:
            self.wakeupRxLow = value
        return self

    def getWakeupRxWindow(self):
        return self.wakeupRxWindow

    def setWakeupRxWindow(self, value):
        if value is not None:
            self.wakeupRxWindow = value
        return self

    def getWakeupTxActive(self):
        return self.wakeupTxActive

    def setWakeupTxActive(self, value):
        if value is not None:
            self.wakeupTxActive = value
        return self

    def getWakeupTxIdle(self):
        return self.wakeupTxIdle

    def setWakeupTxIdle(self, value):
        if value is not None:
            self.wakeupTxIdle = value
        return self