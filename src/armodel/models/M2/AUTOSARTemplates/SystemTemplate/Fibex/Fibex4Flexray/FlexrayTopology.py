from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Float, Integer, PositiveInteger
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveUnlimitedInteger, RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommunicationCluster, CommunicationConnector
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommunicationController


class FlexrayCommunicationController(CommunicationController):
    """FlexRay bus specific communication port attributes."""

    # FlexrayCommunicationController method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.30, p.86
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getAcceptedStartupRange        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setAcceptedStartupRange        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getAllowHaltDueToClock         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setAllowHaltDueToClock         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getAllowPassiveToActive        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setAllowPassiveToActive        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getClusterDriftDamping         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setClusterDriftDamping         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDecodingCorrection          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDecodingCorrection          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDelayCompensationA          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDelayCompensationA          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDelayCompensationB          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDelayCompensationB          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getExternalSync                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setExternalSync                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getExternOffsetCorrection      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setExternOffsetCorrection      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getExternRateCorrection        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setExternRateCorrection        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getFallBackInternal            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setFallBackInternal            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] createFlexrayFifo              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getFlexrayFifos                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getKeySlotID                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setKeySlotID                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getKeySlotOnlyEnabled          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setKeySlotOnlyEnabled          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getKeySlotUsedForStartUp       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setKeySlotUsedForStartUp       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getKeySlotUsedForSync          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setKeySlotUsedForSync          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getLatestTX                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setLatestTX                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getListenTimeout               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setListenTimeout               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMacroInitialOffsetA         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMacroInitialOffsetA         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMacroInitialOffsetB         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMacroInitialOffsetB         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMaximumDynamicPayloadLength [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMaximumDynamicPayloadLength [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMicroInitialOffsetA         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMicroInitialOffsetA         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMicroInitialOffsetB         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMicroInitialOffsetB         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMicroPerCycle               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMicroPerCycle               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMicrotickDuration           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMicrotickDuration           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getNmVectorEarlyUpdate         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setNmVectorEarlyUpdate         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getOffsetCorrectionOut         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setOffsetCorrectionOut         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRateCorrectionOut           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRateCorrectionOut           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSamplesPerMicrotick         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSamplesPerMicrotick         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSecondKeySlotId             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSecondKeySlotId             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTwoKeySlotMode              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTwoKeySlotMode              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getWakeUpPattern               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setWakeUpPattern               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        # Spec verified: R23-11
        super().__init__(parent, short_name)

        # Expanded range of measured clock deviation allowed for startup frames during integration. Unit:microtick
        self.acceptedStartupRange: Optional[Integer] = None

        # Boolean flag that controls the transition to the POC:halt state due to a clock synchronization errors.
        self.allowHaltDueToClock: Optional[Boolean] = None

        # Number of consecutive even/odd cycle pairs that must have valid clock correction terms before the Communication Controller will be allowed to transition from the POC:normal passive state to POC:normal active state. If set to 0, the Communication Controller is not allowed to transition from POC:normal passive state.
        self.allowPassiveToActive: Optional[Integer] = None

        # The cluster drift damping factor used in clock synchronization rate correction in microticks
        self.clusterDriftDamping: Optional[Integer] = None

        # Value used by the receiver to calculate the difference between primary time reference point and secondary time reference point. Unit: Microticks (pDecodingCorrection)
        self.decodingCorrection: Optional[Integer] = None

        # Value used to compensate for reception delays on channel A Unit: Microticks. This optional parameter shall only be filled out if channel A is used.
        self.delayCompensationA: Optional[Integer] = None

        # Value used to compensate for reception delays on channel B. Unit: Microticks. This optional parameter shall only be filled out if channel B is used.
        self.delayCompensationB: Optional[Integer] = None

        # Flag indicating whether the node is externally synchronized (operating as Time Gateway Sink in an TT-E Time Triggered External Sync cluster) or locally synchronized.
        self.externalSync: Optional[Boolean] = None

        # Fixed amount added or subtracted to the calculated offset correction term to facilitate external offset correction, expressed in node-local microticks.
        self.externOffsetCorrection: Optional[Integer] = None

        # Fixed amount added or subtracted to the calculated rate correction term to facilitate external rate correction, expressed in node-local microticks.
        self.externRateCorrection: Optional[Integer] = None

        # Flag indicating whether a Time Gateway Sink node will switch to local clock operation when synchronization with the Time Gateway Source node is lost (pFallBackInternal = true) or will instead go to POC:ready (pFallBackInternal = false).
        self.fallBackInternal: Optional[Boolean] = None

        # One First In First Out (FIFO) queued receive structure, defining the admittance criteria to the FIFO.
        self.flexrayFifos: List["FlexrayFifoConfiguration"] = []

        # ID of the slot used to transmit the startup frame, sync frame, or designated single slot frame. If the attributes keySlotUsedForStartUp, keySlotUsedForSync, or keySlotOnlyEnabled are set to true the key slot value is mandatory.
        self.keySlotID: Optional[PositiveInteger] = None

        # Flag indicating whether or not the node shall enter key slot only mode following startup.
        self.keySlotOnlyEnabled: Optional[Boolean] = None

        # Flag indicating whether the Key Slot is used to transmit a startup frame.
        self.keySlotUsedForStartUp: Optional[Boolean] = None

        # Flag indicating whether the Key Slot is used to transmit a sync frame.
        self.keySlotUsedForSync: Optional[Boolean] = None

        # The number of the last minislot in which a transmission can start in the dynamic segment for the respective node
        self.latestTX: Optional[Integer] = None

        # Value for the startup listen timeout and wakeup listen timeout. Although this is a node local parameter, the real time equivalent of this value should be the same for all nodes in the cluster. Unit: Microticks
        self.listenTimeout: Optional[Integer] = None

        # Integer number of macroticks between the static slot boundary and the closest macrotick boundary of the secondary time reference point based on the nominal macrotick duration. (pMacroInitialOffset). This optional parameter shall only be filled out if channel A is used.
        self.macroInitialOffsetA: Optional[Integer] = None

        # Integer number of macroticks between the static slot boundary and the closest macrotick boundary of the secondary time reference point based on the nominal macrotick duration. (pMacroInitialOffset). This optional parameter shall only be filled out if channel B is used.
        self.macroInitialOffsetB: Optional[Integer] = None

        # Maximum payload length for the dynamic channel of a frame in 16 bit WORDS.
        self.maximumDynamicPayloadLength: Optional[Integer] = None

        # Number of microticks between the closest macrotick boundary described by gMacroInitialOffset and the secondary time reference point. The parameter depends on pDelayCompensationA and therefore it has to be set independently for each channel. This optional parameter shall only be filled out if channel A is used.
        self.microInitialOffsetA: Optional[Integer] = None

        # Number of microticks between the closest macrotick boundary described by gMacroInitialOffset and the secondary time reference point. The parameter depends on pDelayCompensationB and therefore it has to be set independently for each channel. This optional parameter shall only be filled out if channel B is used.
        self.microInitialOffsetB: Optional[Integer] = None

        # The nominal number of microticks in a communication cycle
        self.microPerCycle: Optional[Integer] = None

        # Duration of a microtick. This attribute can be derived from samplePerMicrotick and gdSampleClockPeriod. Unit: seconds
        self.microtickDuration: Optional[TimeValue] = None

        # Flag indicating when the update of the Network Management Vector in the CHI shall take place. If set to false, the update shall take place after the NIT. If set to true, the update shall take place after the end of the static segment.
        self.nmVectorEarlyUpdate: Optional[Boolean] = None

        # Magnitude of the maximum permissible offset correction value. Unit:microtick (pOffsetCorrectionOut)
        self.offsetCorrectionOut: Optional[Integer] = None

        # Magnitude of the maximum permissible rate correction value and the maximum drift offset between two nodes operating with unsynchronized clocks for one communication cycle. Unit:Microticks (pRateCorrectionOut) Remarks: This parameter maps to FlexRay Protocol 2.1 Rev. A parameter pdMaxDrift.
        self.rateCorrectionOut: Optional[Integer] = None

        # Number of samples per microtick
        self.samplesPerMicrotick: Optional[Integer] = None

        # ID of the second Key slot, in which a second startup frame shall be sent in TT-L Time Triggered Local Master Sync or TT-E Time Triggered External Sync mode. If this parameter is set to zero the node does not have a second key slot.
        self.secondKeySlotId: Optional[PositiveInteger] = None

        # Flag indicating whether node operates as a startup node in a TT-E Time Triggered External Sync or TT-L Time Triggered Local Master Sync cluster.
        self.twoKeySlotMode: Optional[Boolean] = None

        # Number of repetitions of the Tx-wakeup symbol to be sent during the CC_WakeupSend state of this Node in the cluster
        self.wakeUpPattern: Optional[Integer] = None

    def getAcceptedStartupRange(self):
        """Expanded range of measured clock deviation allowed for startup frames during integration. Unit:microtick"""
        return self.acceptedStartupRange

    def setAcceptedStartupRange(self, value):
        """Expanded range of measured clock deviation allowed for startup frames during integration. Unit:microtick
        A None value is a no-op and does not overwrite an existing acceptedStartupRange."""
        if value is not None:
            self.acceptedStartupRange = value
        return self

    def getAllowHaltDueToClock(self):
        """Boolean flag that controls the transition to the POC:halt state due to a clock synchronization errors."""
        return self.allowHaltDueToClock

    def setAllowHaltDueToClock(self, value):
        """Boolean flag that controls the transition to the POC:halt state due to a clock synchronization errors.
        A None value is a no-op and does not overwrite an existing allowHaltDueToClock."""
        if value is not None:
            self.allowHaltDueToClock = value
        return self

    def getAllowPassiveToActive(self):
        """Number of consecutive even/odd cycle pairs that must have valid clock correction terms before the Communication Controller will be allowed to transition from the POC:normal passive state to POC:normal active state. If set to 0, the Communication Controller is not allowed to transition from POC:normal passive state."""
        return self.allowPassiveToActive

    def setAllowPassiveToActive(self, value):
        """Number of consecutive even/odd cycle pairs that must have valid clock correction terms before the Communication Controller will be allowed to transition from the POC:normal passive state to POC:normal active state. If set to 0, the Communication Controller is not allowed to transition from POC:normal passive state.
        A None value is a no-op and does not overwrite an existing allowPassiveToActive."""
        if value is not None:
            self.allowPassiveToActive = value
        return self

    def getClusterDriftDamping(self):
        """The cluster drift damping factor used in clock synchronization rate correction in microticks"""
        return self.clusterDriftDamping

    def setClusterDriftDamping(self, value):
        """The cluster drift damping factor used in clock synchronization rate correction in microticks
        A None value is a no-op and does not overwrite an existing clusterDriftDamping."""
        if value is not None:
            self.clusterDriftDamping = value
        return self

    def getDecodingCorrection(self):
        """Value used by the receiver to calculate the difference between primary time reference point and secondary time reference point. Unit: Microticks (pDecodingCorrection)"""
        return self.decodingCorrection

    def setDecodingCorrection(self, value):
        """Value used by the receiver to calculate the difference between primary time reference point and secondary time reference point. Unit: Microticks (pDecodingCorrection)
        A None value is a no-op and does not overwrite an existing decodingCorrection."""
        if value is not None:
            self.decodingCorrection = value
        return self

    def getDelayCompensationA(self):
        """Value used to compensate for reception delays on channel A Unit: Microticks. This optional parameter shall only be filled out if channel A is used."""
        return self.delayCompensationA

    def setDelayCompensationA(self, value):
        """Value used to compensate for reception delays on channel A Unit: Microticks. This optional parameter shall only be filled out if channel A is used.
        A None value is a no-op and does not overwrite an existing delayCompensationA."""
        if value is not None:
            self.delayCompensationA = value
        return self

    def getDelayCompensationB(self):
        """Value used to compensate for reception delays on channel B. Unit: Microticks. This optional parameter shall only be filled out if channel B is used."""
        return self.delayCompensationB

    def setDelayCompensationB(self, value):
        """Value used to compensate for reception delays on channel B. Unit: Microticks. This optional parameter shall only be filled out if channel B is used.
        A None value is a no-op and does not overwrite an existing delayCompensationB."""
        if value is not None:
            self.delayCompensationB = value
        return self

    def getExternalSync(self):
        """Flag indicating whether the node is externally synchronized (operating as Time Gateway Sink in an TT-E Time Triggered External Sync cluster) or locally synchronized."""
        return self.externalSync

    def setExternalSync(self, value):
        """Flag indicating whether the node is externally synchronized (operating as Time Gateway Sink in an TT-E Time Triggered External Sync cluster) or locally synchronized.
        A None value is a no-op and does not overwrite an existing externalSync."""
        if value is not None:
            self.externalSync = value
        return self

    def getExternOffsetCorrection(self):
        """Fixed amount added or subtracted to the calculated offset correction term to facilitate external offset correction, expressed in node-local microticks."""
        return self.externOffsetCorrection

    def setExternOffsetCorrection(self, value):
        """Fixed amount added or subtracted to the calculated offset correction term to facilitate external offset correction, expressed in node-local microticks.
        A None value is a no-op and does not overwrite an existing externOffsetCorrection."""
        if value is not None:
            self.externOffsetCorrection = value
        return self

    def getExternRateCorrection(self):
        """Fixed amount added or subtracted to the calculated rate correction term to facilitate external rate correction, expressed in node-local microticks."""
        return self.externRateCorrection

    def setExternRateCorrection(self, value):
        """Fixed amount added or subtracted to the calculated rate correction term to facilitate external rate correction, expressed in node-local microticks.
        A None value is a no-op and does not overwrite an existing externRateCorrection."""
        if value is not None:
            self.externRateCorrection = value
        return self

    def getFallBackInternal(self):
        """Flag indicating whether a Time Gateway Sink node will switch to local clock operation when synchronization with the Time Gateway Source node is lost (pFallBackInternal = true) or will instead go to POC:ready (pFallBackInternal = false)."""
        return self.fallBackInternal

    def setFallBackInternal(self, value):
        """Flag indicating whether a Time Gateway Sink node will switch to local clock operation when synchronization with the Time Gateway Source node is lost (pFallBackInternal = true) or will instead go to POC:ready (pFallBackInternal = false).
        A None value is a no-op and does not overwrite an existing fallBackInternal."""
        if value is not None:
            self.fallBackInternal = value
        return self

    def createFlexrayFifo(self) -> "FlexrayFifoConfiguration":
        """One First In First Out (FIFO) queued receive structure, defining the admittance criteria to the FIFO."""
        fifo = FlexrayFifoConfiguration()
        self.flexrayFifos.append(fifo)
        return fifo

    def getFlexrayFifos(self) -> List["FlexrayFifoConfiguration"]:
        """One First In First Out (FIFO) queued receive structure, defining the admittance criteria to the FIFO."""
        return self.flexrayFifos

    def getKeySlotID(self):
        """ID of the slot used to transmit the startup frame, sync frame, or designated single slot frame. If the attributes keySlotUsedForStartUp, keySlotUsedForSync, or keySlotOnlyEnabled are set to true the key slot value is mandatory."""
        return self.keySlotID

    def setKeySlotID(self, value):
        """ID of the slot used to transmit the startup frame, sync frame, or designated single slot frame. If the attributes keySlotUsedForStartUp, keySlotUsedForSync, or keySlotOnlyEnabled are set to true the key slot value is mandatory.
        A None value is a no-op and does not overwrite an existing keySlotID."""
        if value is not None:
            self.keySlotID = value
        return self

    def getKeySlotOnlyEnabled(self):
        """Flag indicating whether or not the node shall enter key slot only mode following startup."""
        return self.keySlotOnlyEnabled

    def setKeySlotOnlyEnabled(self, value):
        """Flag indicating whether or not the node shall enter key slot only mode following startup.
        A None value is a no-op and does not overwrite an existing keySlotOnlyEnabled."""
        if value is not None:
            self.keySlotOnlyEnabled = value
        return self

    def getKeySlotUsedForStartUp(self):
        """Flag indicating whether the Key Slot is used to transmit a startup frame."""
        return self.keySlotUsedForStartUp

    def setKeySlotUsedForStartUp(self, value):
        """Flag indicating whether the Key Slot is used to transmit a startup frame.
        A None value is a no-op and does not overwrite an existing keySlotUsedForStartUp."""
        if value is not None:
            self.keySlotUsedForStartUp = value
        return self

    def getKeySlotUsedForSync(self):
        """Flag indicating whether the Key Slot is used to transmit a sync frame."""
        return self.keySlotUsedForSync

    def setKeySlotUsedForSync(self, value):
        """Flag indicating whether the Key Slot is used to transmit a sync frame.
        A None value is a no-op and does not overwrite an existing keySlotUsedForSync."""
        if value is not None:
            self.keySlotUsedForSync = value
        return self

    def getLatestTX(self):
        """The number of the last minislot in which a transmission can start in the dynamic segment for the respective node"""
        return self.latestTX

    def setLatestTX(self, value):
        """The number of the last minislot in which a transmission can start in the dynamic segment for the respective node
        A None value is a no-op and does not overwrite an existing latestTX."""
        if value is not None:
            self.latestTX = value
        return self

    def getListenTimeout(self):
        """Value for the startup listen timeout and wakeup listen timeout. Although this is a node local parameter, the real time equivalent of this value should be the same for all nodes in the cluster. Unit: Microticks"""
        return self.listenTimeout

    def setListenTimeout(self, value):
        """Value for the startup listen timeout and wakeup listen timeout. Although this is a node local parameter, the real time equivalent of this value should be the same for all nodes in the cluster. Unit: Microticks
        A None value is a no-op and does not overwrite an existing listenTimeout."""
        if value is not None:
            self.listenTimeout = value
        return self

    def getMacroInitialOffsetA(self):
        """Integer number of macroticks between the static slot boundary and the closest macrotick boundary of the secondary time reference point based on the nominal macrotick duration. (pMacroInitialOffset). This optional parameter shall only be filled out if channel A is used."""
        return self.macroInitialOffsetA

    def setMacroInitialOffsetA(self, value):
        """Integer number of macroticks between the static slot boundary and the closest macrotick boundary of the secondary time reference point based on the nominal macrotick duration. (pMacroInitialOffset). This optional parameter shall only be filled out if channel A is used.
        A None value is a no-op and does not overwrite an existing macroInitialOffsetA."""
        if value is not None:
            self.macroInitialOffsetA = value
        return self

    def getMacroInitialOffsetB(self):
        """Integer number of macroticks between the static slot boundary and the closest macrotick boundary of the secondary time reference point based on the nominal macrotick duration. (pMacroInitialOffset). This optional parameter shall only be filled out if channel B is used."""
        return self.macroInitialOffsetB

    def setMacroInitialOffsetB(self, value):
        """Integer number of macroticks between the static slot boundary and the closest macrotick boundary of the secondary time reference point based on the nominal macrotick duration. (pMacroInitialOffset). This optional parameter shall only be filled out if channel B is used.
        A None value is a no-op and does not overwrite an existing macroInitialOffsetB."""
        if value is not None:
            self.macroInitialOffsetB = value
        return self

    def getMaximumDynamicPayloadLength(self):
        """Maximum payload length for the dynamic channel of a frame in 16 bit WORDS."""
        return self.maximumDynamicPayloadLength

    def setMaximumDynamicPayloadLength(self, value):
        """Maximum payload length for the dynamic channel of a frame in 16 bit WORDS.
        A None value is a no-op and does not overwrite an existing maximumDynamicPayloadLength."""
        if value is not None:
            self.maximumDynamicPayloadLength = value
        return self

    def getMicroInitialOffsetA(self):
        """Number of microticks between the closest macrotick boundary described by gMacroInitialOffset and the secondary time reference point. The parameter depends on pDelayCompensationA and therefore it has to be set independently for each channel. This optional parameter shall only be filled out if channel A is used."""
        return self.microInitialOffsetA

    def setMicroInitialOffsetA(self, value):
        """Number of microticks between the closest macrotick boundary described by gMacroInitialOffset and the secondary time reference point. The parameter depends on pDelayCompensationA and therefore it has to be set independently for each channel. This optional parameter shall only be filled out if channel A is used.
        A None value is a no-op and does not overwrite an existing microInitialOffsetA."""
        if value is not None:
            self.microInitialOffsetA = value
        return self

    def getMicroInitialOffsetB(self):
        """Number of microticks between the closest macrotick boundary described by gMacroInitialOffset and the secondary time reference point. The parameter depends on pDelayCompensationB and therefore it has to be set independently for each channel. This optional parameter shall only be filled out if channel B is used."""
        return self.microInitialOffsetB

    def setMicroInitialOffsetB(self, value):
        """Number of microticks between the closest macrotick boundary described by gMacroInitialOffset and the secondary time reference point. The parameter depends on pDelayCompensationB and therefore it has to be set independently for each channel. This optional parameter shall only be filled out if channel B is used.
        A None value is a no-op and does not overwrite an existing microInitialOffsetB."""
        if value is not None:
            self.microInitialOffsetB = value
        return self

    def getMicroPerCycle(self):
        """The nominal number of microticks in a communication cycle"""
        return self.microPerCycle

    def setMicroPerCycle(self, value):
        """The nominal number of microticks in a communication cycle
        A None value is a no-op and does not overwrite an existing microPerCycle."""
        if value is not None:
            self.microPerCycle = value
        return self

    def getMicrotickDuration(self):
        """Duration of a microtick. This attribute can be derived from samplePerMicrotick and gdSampleClockPeriod. Unit: seconds"""
        return self.microtickDuration

    def setMicrotickDuration(self, value):
        """Duration of a microtick. This attribute can be derived from samplePerMicrotick and gdSampleClockPeriod. Unit: seconds
        A None value is a no-op and does not overwrite an existing microtickDuration."""
        if value is not None:
            self.microtickDuration = value
        return self

    def getNmVectorEarlyUpdate(self):
        """Flag indicating when the update of the Network Management Vector in the CHI shall take place. If set to false, the update shall take place after the NIT. If set to true, the update shall take place after the end of the static segment."""
        return self.nmVectorEarlyUpdate

    def setNmVectorEarlyUpdate(self, value):
        """Flag indicating when the update of the Network Management Vector in the CHI shall take place. If set to false, the update shall take place after the NIT. If set to true, the update shall take place after the end of the static segment.
        A None value is a no-op and does not overwrite an existing nmVectorEarlyUpdate."""
        if value is not None:
            self.nmVectorEarlyUpdate = value
        return self

    def getOffsetCorrectionOut(self):
        """Magnitude of the maximum permissible offset correction value. Unit:microtick (pOffsetCorrectionOut)"""
        return self.offsetCorrectionOut

    def setOffsetCorrectionOut(self, value):
        """Magnitude of the maximum permissible offset correction value. Unit:microtick (pOffsetCorrectionOut)
        A None value is a no-op and does not overwrite an existing offsetCorrectionOut."""
        if value is not None:
            self.offsetCorrectionOut = value
        return self

    def getRateCorrectionOut(self):
        """Magnitude of the maximum permissible rate correction value and the maximum drift offset between two nodes operating with unsynchronized clocks for one communication cycle. Unit:Microticks (pRateCorrectionOut) Remarks: This parameter maps to FlexRay Protocol 2.1 Rev. A parameter pdMaxDrift."""
        return self.rateCorrectionOut

    def setRateCorrectionOut(self, value):
        """Magnitude of the maximum permissible rate correction value and the maximum drift offset between two nodes operating with unsynchronized clocks for one communication cycle. Unit:Microticks (pRateCorrectionOut) Remarks: This parameter maps to FlexRay Protocol 2.1 Rev. A parameter pdMaxDrift.
        A None value is a no-op and does not overwrite an existing rateCorrectionOut."""
        if value is not None:
            self.rateCorrectionOut = value
        return self

    def getSamplesPerMicrotick(self):
        """Number of samples per microtick"""
        return self.samplesPerMicrotick

    def setSamplesPerMicrotick(self, value):
        """Number of samples per microtick
        A None value is a no-op and does not overwrite an existing samplesPerMicrotick."""
        if value is not None:
            self.samplesPerMicrotick = value
        return self

    def getSecondKeySlotId(self):
        """ID of the second Key slot, in which a second startup frame shall be sent in TT-L Time Triggered Local Master Sync or TT-E Time Triggered External Sync mode. If this parameter is set to zero the node does not have a second key slot."""
        return self.secondKeySlotId

    def setSecondKeySlotId(self, value):
        """ID of the second Key slot, in which a second startup frame shall be sent in TT-L Time Triggered Local Master Sync or TT-E Time Triggered External Sync mode. If this parameter is set to zero the node does not have a second key slot.
        A None value is a no-op and does not overwrite an existing secondKeySlotId."""
        if value is not None:
            self.secondKeySlotId = value
        return self

    def getTwoKeySlotMode(self):
        """Flag indicating whether node operates as a startup node in a TT-E Time Triggered External Sync or TT-L Time Triggered Local Master Sync cluster."""
        return self.twoKeySlotMode

    def setTwoKeySlotMode(self, value):
        """Flag indicating whether node operates as a startup node in a TT-E Time Triggered External Sync or TT-L Time Triggered Local Master Sync cluster.
        A None value is a no-op and does not overwrite an existing twoKeySlotMode."""
        if value is not None:
            self.twoKeySlotMode = value
        return self

    def getWakeUpPattern(self):
        """Number of repetitions of the Tx-wakeup symbol to be sent during the CC_WakeupSend state of this Node in the cluster"""
        return self.wakeUpPattern

    def setWakeUpPattern(self, value):
        """Number of repetitions of the Tx-wakeup symbol to be sent during the CC_WakeupSend state of this Node in the cluster
        A None value is a no-op and does not overwrite an existing wakeUpPattern."""
        if value is not None:
            self.wakeUpPattern = value
        return self


class FlexrayCommunicationConnector(CommunicationConnector):
    """
    Defines a FlexRay communication connector that links FlexRay controllers
    to communication channels, specifying NM (Network Management) timing
    and PNC (Partial Network Cluster) properties for FlexRay communication.
    """

    # FlexrayCommunicationConnector method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getNmReadySleepTime          [x] impl  [ ] docstring  [ ] test
    # [ ] setNmReadySleepTime          [x] impl  [ ] docstring  [ ] test
    # [ ] getPncFilterDataMask         [x] impl  [ ] docstring  [ ] test
    # [ ] setPncFilterDataMask         [x] impl  [ ] docstring  [ ] test
    # [ ] getWakeUpChannel             [x] impl  [ ] docstring  [ ] test
    # [ ] setWakeUpChannel             [x] impl  [ ] docstring  [ ] test

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

    # FlexrayCluster method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getActionPointOffset         [x] impl  [ ] docstring  [ ] test
    # [ ] setActionPointOffset         [x] impl  [ ] docstring  [ ] test
    # [ ] getBit                       [x] impl  [ ] docstring  [ ] test
    # [ ] setBit                       [x] impl  [ ] docstring  [ ] test
    # [ ] getCasRxLowMax               [x] impl  [ ] docstring  [ ] test
    # [ ] setCasRxLowMax               [x] impl  [ ] docstring  [ ] test
    # [ ] getColdStartAttempts         [x] impl  [ ] docstring  [ ] test
    # [ ] setColdStartAttempts         [x] impl  [ ] docstring  [ ] test
    # [ ] getCycle                     [x] impl  [ ] docstring  [ ] test
    # [ ] setCycle                     [x] impl  [ ] docstring  [ ] test
    # [ ] getCycleCountMax             [x] impl  [ ] docstring  [ ] test
    # [ ] setCycleCountMax             [x] impl  [ ] docstring  [ ] test
    # [ ] getDetectNitError            [x] impl  [ ] docstring  [ ] test
    # [ ] setDetectNitError            [x] impl  [ ] docstring  [ ] test
    # [ ] getDynamicSlotIdlePhase      [x] impl  [ ] docstring  [ ] test
    # [ ] setDynamicSlotIdlePhase      [x] impl  [ ] docstring  [ ] test
    # [ ] getIgnoreAfterTx             [x] impl  [ ] docstring  [ ] test
    # [ ] setIgnoreAfterTx             [x] impl  [ ] docstring  [ ] test
    # [ ] getListenNoise               [x] impl  [ ] docstring  [ ] test
    # [ ] setListenNoise               [x] impl  [ ] docstring  [ ] test
    # [ ] getMacroPerCycle             [x] impl  [ ] docstring  [ ] test
    # [ ] setMacroPerCycle             [x] impl  [ ] docstring  [ ] test
    # [ ] getMacrotickDuration         [x] impl  [ ] docstring  [ ] test
    # [ ] setMacrotickDuration         [x] impl  [ ] docstring  [ ] test
    # [ ] getMaxWithoutClockCorrectionFatal [x] impl  [ ] docstring  [ ] test
    # [ ] setMaxWithoutClockCorrectionFatal [x] impl  [ ] docstring  [ ] test
    # [ ] getMaxWithoutClockCorrectionPassive [x] impl  [ ] docstring  [ ] test
    # [ ] setMaxWithoutClockCorrectionPassive [x] impl  [ ] docstring  [ ] test
    # [ ] getMinislotActionPointOffset [x] impl  [ ] docstring  [ ] test
    # [ ] setMinislotActionPointOffset [x] impl  [ ] docstring  [ ] test
    # [ ] getMinislotDuration          [x] impl  [ ] docstring  [ ] test
    # [ ] setMinislotDuration          [x] impl  [ ] docstring  [ ] test
    # [ ] getNetworkIdleTime           [x] impl  [ ] docstring  [ ] test
    # [ ] setNetworkIdleTime           [x] impl  [ ] docstring  [ ] test
    # [ ] getNetworkManagementVectorLength [x] impl  [ ] docstring  [ ] test
    # [ ] setNetworkManagementVectorLength [x] impl  [ ] docstring  [ ] test
    # [ ] getNumberOfMinislots         [x] impl  [ ] docstring  [ ] test
    # [ ] setNumberOfMinislots         [x] impl  [ ] docstring  [ ] test
    # [ ] getNumberOfStaticSlots       [x] impl  [ ] docstring  [ ] test
    # [ ] setNumberOfStaticSlots       [x] impl  [ ] docstring  [ ] test
    # [ ] getOffsetCorrectionStart     [x] impl  [ ] docstring  [ ] test
    # [ ] setOffsetCorrectionStart     [x] impl  [ ] docstring  [ ] test
    # [ ] getPayloadLengthStatic       [x] impl  [ ] docstring  [ ] test
    # [ ] setPayloadLengthStatic       [x] impl  [ ] docstring  [ ] test
    # [ ] getSafetyMargin              [x] impl  [ ] docstring  [ ] test
    # [ ] setSafetyMargin              [x] impl  [ ] docstring  [ ] test
    # [ ] getSampleClockPeriod         [x] impl  [ ] docstring  [ ] test
    # [ ] setSampleClockPeriod         [x] impl  [ ] docstring  [ ] test
    # [ ] getStaticSlotDuration        [x] impl  [ ] docstring  [ ] test
    # [ ] setStaticSlotDuration        [x] impl  [ ] docstring  [ ] test
    # [ ] getSymbolWindow              [x] impl  [ ] docstring  [ ] test
    # [ ] setSymbolWindow              [x] impl  [ ] docstring  [ ] test
    # [ ] getSymbolWindowActionPointOffset [x] impl  [ ] docstring  [ ] test
    # [ ] setSymbolWindowActionPointOffset [x] impl  [ ] docstring  [ ] test
    # [ ] getSyncFrameIdCountMax       [x] impl  [ ] docstring  [ ] test
    # [ ] setSyncFrameIdCountMax       [x] impl  [ ] docstring  [ ] test
    # [ ] getTranceiverStandbyDelay    [x] impl  [ ] docstring  [ ] test
    # [ ] setTranceiverStandbyDelay    [x] impl  [ ] docstring  [ ] test
    # [ ] getTransmissionStartSequenceDuration [x] impl  [ ] docstring  [ ] test
    # [ ] setTransmissionStartSequenceDuration [x] impl  [ ] docstring  [ ] test
    # [ ] getWakeupRxIdle              [x] impl  [ ] docstring  [ ] test
    # [ ] setWakeupRxIdle              [x] impl  [ ] docstring  [ ] test
    # [ ] getWakeupRxLow               [x] impl  [ ] docstring  [ ] test
    # [ ] setWakeupRxLow               [x] impl  [ ] docstring  [ ] test
    # [ ] getWakeupRxWindow            [x] impl  [ ] docstring  [ ] test
    # [ ] setWakeupRxWindow            [x] impl  [ ] docstring  [ ] test
    # [ ] getWakeupTxActive            [x] impl  [ ] docstring  [ ] test
    # [ ] setWakeupTxActive            [x] impl  [ ] docstring  [ ] test
    # [ ] getWakeupTxIdle              [x] impl  [ ] docstring  [ ] test
    # [ ] setWakeupTxIdle              [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.actionPointOffset = None  # type: Integer
        self.bit = None  # type: TimeValue
        self.casRxLowMax = None  # type: Integer
        self.coldStartAttempts = None  # type: Integer
        self.cycle = None  # type: TimeValue
        self.cycleCountMax = None  # type: Integer
        self.detectNitError = None  # type: Boolean
        self.dynamicSlotIdlePhase = None  # type: Integer
        self.ignoreAfterTx = None  # type: Integer
        self.listenNoise = None  # type: Integer
        self.macroPerCycle = None  # type: Integer
        self.macrotickDuration = None  # type: TimeValue
        self.maxWithoutClockCorrectionFatal = None  # type: Integer
        self.maxWithoutClockCorrectionPassive = None  # type: Integer
        self.minislotActionPointOffset = None  # type: Integer
        self.minislotDuration = None  # type: Integer
        self.networkIdleTime = None  # type: Integer
        self.networkManagementVectorLength = None  # type: Integer
        self.numberOfMinislots = None  # type: Integer
        self.numberOfStaticSlots = None  # type: Integer
        self.offsetCorrectionStart = None  # type: Integer
        self.payloadLengthStatic = None  # type: Integer
        self.safetyMargin = None  # type: Integer
        self.sampleClockPeriod = None  # type: TimeValue
        self.staticSlotDuration = None  # type: Integer
        self.symbolWindow = None  # type: Integer
        self.symbolWindowActionPointOffset = None  # type: Integer
        self.syncFrameIdCountMax = None  # type: Integer
        self.tranceiverStandbyDelay = None  # type: Float
        self.transmissionStartSequenceDuration = None  # type: Integer
        self.wakeupRxIdle = None  # type: Integer
        self.wakeupRxLow = None  # type: Integer
        self.wakeupRxWindow = None  # type: Integer
        self.wakeupTxActive = None  # type: Integer
        self.wakeupTxIdle = None  # type: Integer

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


class FlexrayFifoRange(ARObject):
    """FIFO Frame Id range acceptance criteria."""

    # FlexrayFifoRange method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.32, p.87
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getRangeMax  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRangeMax  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRangeMin  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRangeMin  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # Max Range.
        self.rangeMax: Optional[Integer] = None

        # Min Range.
        self.rangeMin: Optional[Integer] = None

    def getRangeMax(self) -> Optional[Integer]:
        """Max Range."""
        return self.rangeMax

    def setRangeMax(self, value: Optional[Integer]) -> "FlexrayFifoRange":
        """Max Range.
        A None value is a no-op and does not overwrite an existing rangeMax."""
        if value is not None:
            self.rangeMax = value
        return self

    def getRangeMin(self) -> Optional[Integer]:
        """Min Range."""
        return self.rangeMin

    def setRangeMin(self, value: Optional[Integer]) -> "FlexrayFifoRange":
        """Min Range.
        A None value is a no-op and does not overwrite an existing rangeMin."""
        if value is not None:
            self.rangeMin = value
        return self


class FlexrayFifoConfiguration(ARObject):
    """One First In First Out (FIFO) queued receive structure, defining the admittance criteria to the FIFO, and mandating the ability to admit messages into the FIFO based on Message Id filtering criteria."""

    # FlexrayFifoConfiguration method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.31, p.87
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getAdmitWithoutMessageId        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setAdmitWithoutMessageId        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getBaseCycle                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setBaseCycle                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getChannelRef                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setChannelRef                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getCycleRepetition              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setCycleRepetition              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getFifoDepth                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setFifoDepth                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getFlexrayFifoRanges            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createFlexrayFifoRange          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMsgIdMask                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMsgIdMask                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMsgIdMatch                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMsgIdMatch                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # Boolean configuration which determines whether or not frames received in the dynamic segment that don't contain a message ID will be admitted into the FIFO.
        self.admitWithoutMessageId: Optional[Boolean] = None

        # FIFO cycle counter acceptance criteria.
        self.baseCycle: Optional[Integer] = None

        # Fifo channel admittance criteria.
        self.channelRef: Optional[RefType] = None

        # FIFO cycle counter acceptance criteria.
        self.cycleRepetition: Optional[Integer] = None

        # FrFifoDepth configures the maximum number of rx-frames which can be contained in the FIFO.
        self.fifoDepth: Optional[Integer] = None

        # FIFO Frame Id range acceptance criteria.
        self.fifoRange: List[FlexrayFifoRange] = []

        # FIFO message identifier acceptance criteria (Mask filter).
        self.msgIdMask: Optional[Integer] = None

        # FIFO message identifier acceptance criteria (Match filter).
        self.msgIdMatch: Optional[Integer] = None

    def getAdmitWithoutMessageId(self) -> Optional[Boolean]:
        """Boolean configuration which determines whether or not frames received in the dynamic segment that don't contain a message ID will be admitted into the FIFO."""
        return self.admitWithoutMessageId

    def setAdmitWithoutMessageId(self, value: Optional[Boolean]) -> "FlexrayFifoConfiguration":
        """Boolean configuration which determines whether or not frames received in the dynamic segment that don't contain a message ID will be admitted into the FIFO.
        A None value is a no-op and does not overwrite an existing admitWithoutMessageId."""
        if value is not None:
            self.admitWithoutMessageId = value
        return self

    def getBaseCycle(self) -> Optional[Integer]:
        """FIFO cycle counter acceptance criteria."""
        return self.baseCycle

    def setBaseCycle(self, value: Optional[Integer]) -> "FlexrayFifoConfiguration":
        """FIFO cycle counter acceptance criteria.
        A None value is a no-op and does not overwrite an existing baseCycle."""
        if value is not None:
            self.baseCycle = value
        return self

    def getChannelRef(self) -> Optional[RefType]:
        """Fifo channel admittance criteria."""
        return self.channelRef

    def setChannelRef(self, value: Optional[RefType]) -> "FlexrayFifoConfiguration":
        """Fifo channel admittance criteria.
        A None value is a no-op and does not overwrite an existing channelRef."""
        if value is not None:
            self.channelRef = value
        return self

    def getCycleRepetition(self) -> Optional[Integer]:
        """FIFO cycle counter acceptance criteria."""
        return self.cycleRepetition

    def setCycleRepetition(self, value: Optional[Integer]) -> "FlexrayFifoConfiguration":
        """FIFO cycle counter acceptance criteria.
        A None value is a no-op and does not overwrite an existing cycleRepetition."""
        if value is not None:
            self.cycleRepetition = value
        return self

    def getFifoDepth(self) -> Optional[Integer]:
        """FrFifoDepth configures the maximum number of rx-frames which can be contained in the FIFO."""
        return self.fifoDepth

    def setFifoDepth(self, value: Optional[Integer]) -> "FlexrayFifoConfiguration":
        """FrFifoDepth configures the maximum number of rx-frames which can be contained in the FIFO.
        A None value is a no-op and does not overwrite an existing fifoDepth."""
        if value is not None:
            self.fifoDepth = value
        return self

    def getFlexrayFifoRanges(self) -> List[FlexrayFifoRange]:
        """FIFO Frame Id range acceptance criteria."""
        return self.fifoRange

    def createFlexrayFifoRange(self) -> FlexrayFifoRange:
        """FIFO Frame Id range acceptance criteria."""
        fifo_range = FlexrayFifoRange()
        self.fifoRange.append(fifo_range)
        return fifo_range

    def getMsgIdMask(self) -> Optional[Integer]:
        """FIFO message identifier acceptance criteria (Mask filter)."""
        return self.msgIdMask

    def setMsgIdMask(self, value: Optional[Integer]) -> "FlexrayFifoConfiguration":
        """FIFO message identifier acceptance criteria (Mask filter).
        A None value is a no-op and does not overwrite an existing msgIdMask."""
        if value is not None:
            self.msgIdMask = value
        return self

    def getMsgIdMatch(self) -> Optional[Integer]:
        """FIFO message identifier acceptance criteria (Match filter)."""
        return self.msgIdMatch

    def setMsgIdMatch(self, value: Optional[Integer]) -> "FlexrayFifoConfiguration":
        """FIFO message identifier acceptance criteria (Match filter).
        A None value is a no-op and does not overwrite an existing msgIdMatch."""
        if value is not None:
            self.msgIdMatch = value
        return self
