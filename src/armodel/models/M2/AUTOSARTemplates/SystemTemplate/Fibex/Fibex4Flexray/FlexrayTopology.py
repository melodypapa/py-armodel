from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Float, Integer, PositiveInteger
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveUnlimitedInteger, RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommunicationCluster, CommunicationConnector, PhysicalChannel
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
    """FlexRay specific attributes to the physicalCluster"""

    # FlexrayCluster method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.29, p.81
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getActionPointOffset         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setActionPointOffset         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getBit                       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setBit                       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getCasRxLowMax               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setCasRxLowMax               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getColdStartAttempts         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setColdStartAttempts         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getCycle                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setCycle                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getCycleCountMax             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setCycleCountMax             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDetectNitError            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDetectNitError            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDynamicSlotIdlePhase      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDynamicSlotIdlePhase      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getIgnoreAfterTx             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setIgnoreAfterTx             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getListenNoise               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setListenNoise               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMacroPerCycle             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMacroPerCycle             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMacrotickDuration         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMacrotickDuration         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMaxWithoutClockCorrectionFatal [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMaxWithoutClockCorrectionFatal [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMaxWithoutClockCorrectionPassive [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMaxWithoutClockCorrectionPassive [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMinislotActionPointOffset [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMinislotActionPointOffset [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMinislotDuration          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMinislotDuration          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getNetworkIdleTime           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setNetworkIdleTime           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getNetworkManagementVectorLength [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setNetworkManagementVectorLength [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getNumberOfMinislots         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setNumberOfMinislots         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getNumberOfStaticSlots       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setNumberOfStaticSlots       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getOffsetCorrectionStart     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setOffsetCorrectionStart     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPayloadLengthStatic       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPayloadLengthStatic       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSafetyMargin              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSafetyMargin              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSampleClockPeriod         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSampleClockPeriod         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getStaticSlotDuration        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setStaticSlotDuration        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSymbolWindow              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSymbolWindow              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSymbolWindowActionPointOffset [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSymbolWindowActionPointOffset [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSyncFrameIdCountMax       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSyncFrameIdCountMax       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTranceiverStandbyDelay    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTranceiverStandbyDelay    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTransmissionStartSequenceDuration [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTransmissionStartSequenceDuration [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getWakeupRxIdle              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setWakeupRxIdle              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getWakeupRxLow               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setWakeupRxLow               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getWakeupRxWindow            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setWakeupRxWindow            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getWakeupTxActive            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setWakeupTxActive            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getWakeupTxIdle              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setWakeupTxIdle              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The offset of the action point in networks
        self.actionPointOffset: Optional[Integer] = None

        # Nominal bit time (= 1 / fx:SPEED). gdBit = cSamplesPer Bit * gdSampleClockPeriod. Unit: seconds (gdBit)
        self.bit: Optional[TimeValue] = None

        # Upper limit of the Collision Avoidance Symbol (CAS) acceptance window. Unit:bitDuration
        self.casRxLowMax: Optional[Integer] = None

        # The maximum number of times that a node in this cluster is permitted to attempt to start the cluster by initiating schedule synchronization
        self.coldStartAttempts: Optional[Integer] = None

        # Length of the cycle. Unit: seconds
        self.cycle: Optional[TimeValue] = None

        # Maximum cycle counter value in a given cluster. Remark: Set to 63 for FlexRay Protocol 2.1 Rev. A compliance.
        self.cycleCountMax: Optional[Integer] = None

        # Indicates whether NIT error status of each cluster shall be detected or not.
        self.detectNitError: Optional[Boolean] = None

        # The duration of the dynamic slot idle phase in minislots.
        self.dynamicSlotIdlePhase: Optional[Integer] = None

        # Duration for which the bitstrobing is paused after transmission [gdBit].
        self.ignoreAfterTx: Optional[Integer] = None

        # Upper limit for the start up and wake up listen timeout in the presence of noise. Expressed as a multiple of the cluster constant pdListenTimeout. Unit microticks
        self.listenNoise: Optional[Integer] = None

        # The number of macroticks in a communication cycle
        self.macroPerCycle: Optional[Integer] = None

        # Duration of the cluster wide nominal macrotick, expressed in s.
        self.macrotickDuration: Optional[TimeValue] = None

        # Threshold concerning vClockCorrectionFailedCounter. Defines the number of consecutive even/odd Cycle pairs with missing clock correction terms that will cause the protocol to transition from the POC:normal active or POC:normal passive state into the POC:halt state.
        self.maxWithoutClockCorrectionFatal: Optional[Integer] = None

        # Threshold concerning vClockCorrectionFailedCounter. Defines the number of consecutive even/odd Cycle pairs with missing clock correction terms that will cause the protocol to transition from the POC:normal active state to the POC:normal passive state.
        self.maxWithoutClockCorrectionPassive: Optional[Integer] = None

        # The Offset of the action point within a minislot. Unit: macroticks
        self.minislotActionPointOffset: Optional[Integer] = None

        # The duration of a minislot (dynamic segment). Unit: macroticks.
        self.minislotDuration: Optional[Integer] = None

        # The duration of the network idle time in macroticks
        self.networkIdleTime: Optional[Integer] = None

        # Length of the Network Management vector in a cluster [bytes]
        self.networkManagementVectorLength: Optional[Integer] = None

        # Number of Minislots in the dynamic segment.
        self.numberOfMinislots: Optional[Integer] = None

        # The number of static slots in the static segment.
        self.numberOfStaticSlots: Optional[Integer] = None

        # Start of the offset correction phase within the Network Idle Time (NIT), expressed as the number of macroticks from the start of cycle. Unit: macroticks
        self.offsetCorrectionStart: Optional[Integer] = None

        # Globally configured payload length of a static frame. Unit: 16-bit WORDS.
        self.payloadLengthStatic: Optional[Integer] = None

        # Additional timespan in macroticks which takes jitter into account to be able to set the JobListPointer to the next possible job which can be executed in case the FlexRay Job List Execution Function has be resynchronized.
        self.safetyMargin: Optional[Integer] = None

        # Sample clock period. Unit: seconds
        self.sampleClockPeriod: Optional[TimeValue] = None

        # The duration of a slot in the static segment. Unit: macroticks
        self.staticSlotDuration: Optional[Integer] = None

        # The duration of the symbol window. Unit: macroticks
        self.symbolWindow: Optional[Integer] = None

        # Number of macroticks the action point offset is from the beginning of the symbol window [Macroticks].
        self.symbolWindowActionPointOffset: Optional[Integer] = None

        # Maximum number of distinct syncframe identifiers present in a given cluster. This parameter maps to FlexRay Protocol 2.1 Rev. A parameter gSyncNodeMax.
        self.syncFrameIdCountMax: Optional[Integer] = None

        # The duration of timer t_TrcvStdbyDelay in seconds. The granularity of this parameter shall be restricted to full Flex Ray cycles (cycle). The transceiver status setting to STANDBY shall be delayed by this value. Not specifying a value or a value of 0 shall imply that the timer is not used.
        self.tranceiverStandbyDelay: Optional[Float] = None

        # Number of bits in the Transmission Start Sequence [gd Bits].
        self.transmissionStartSequenceDuration: Optional[Integer] = None

        # Number of bits used by the node to test the duration of the 'idle' or HIGH phase of a received wakeup. Unit:bit Duration Remarks: This parameter maps to FlexRay Protocol 2.1 Rev. A parameter gdWakeupSymbolRxIdle.
        self.wakeupRxIdle: Optional[Integer] = None

        # Number of bits used by the node to test the duration of the LOW phase of a received wakeup. Unit:bitDuration Remarks: This parameter maps to FlexRay Protocol 2.1 Rev. A parameter gdWakeupSymbolRxLow.
        self.wakeupRxLow: Optional[Integer] = None

        # The size of the window used to detect wakeups [gdBit]. Remarks: This parameter maps to FlexRay Protocol 2.1 Rev. A parameter gdWakeupSymbolRxWindow.
        self.wakeupRxWindow: Optional[Integer] = None

        # Number of bits used by the node to transmit the LOW phase of awakeup symbol and the HIGH and LOW phases of a WUDOP. Unit:bitDuration
        self.wakeupTxActive: Optional[Integer] = None

        # Number of bits used by the node to transmit the 'idle' part of a wakeup symbol. Unit: gDbit
        self.wakeupTxIdle: Optional[Integer] = None

    def getActionPointOffset(self) -> Optional[Integer]:
        """The offset of the action point in networks"""
        return self.actionPointOffset

    def setActionPointOffset(self, value: Optional[Integer]) -> "FlexrayCluster":
        """The offset of the action point in networks
        A None value is a no-op and does not overwrite an existing actionPointOffset."""
        if value is not None:
            self.actionPointOffset = value
        return self

    def getBit(self) -> Optional[TimeValue]:
        """Nominal bit time (= 1 / fx:SPEED). gdBit = cSamplesPer Bit * gdSampleClockPeriod. Unit: seconds (gdBit)"""
        return self.bit

    def setBit(self, value: Optional[TimeValue]) -> "FlexrayCluster":
        """Nominal bit time (= 1 / fx:SPEED). gdBit = cSamplesPer Bit * gdSampleClockPeriod. Unit: seconds (gdBit)
        A None value is a no-op and does not overwrite an existing bit."""
        if value is not None:
            self.bit = value
        return self

    def getCasRxLowMax(self) -> Optional[Integer]:
        """Upper limit of the Collision Avoidance Symbol (CAS) acceptance window. Unit:bitDuration"""
        return self.casRxLowMax

    def setCasRxLowMax(self, value: Optional[Integer]) -> "FlexrayCluster":
        """Upper limit of the Collision Avoidance Symbol (CAS) acceptance window. Unit:bitDuration
        A None value is a no-op and does not overwrite an existing casRxLowMax."""
        if value is not None:
            self.casRxLowMax = value
        return self

    def getColdStartAttempts(self) -> Optional[Integer]:
        """The maximum number of times that a node in this cluster is permitted to attempt to start the cluster by initiating schedule synchronization"""
        return self.coldStartAttempts

    def setColdStartAttempts(self, value: Optional[Integer]) -> "FlexrayCluster":
        """The maximum number of times that a node in this cluster is permitted to attempt to start the cluster by initiating schedule synchronization
        A None value is a no-op and does not overwrite an existing coldStartAttempts."""
        if value is not None:
            self.coldStartAttempts = value
        return self

    def getCycle(self) -> Optional[TimeValue]:
        """Length of the cycle. Unit: seconds"""
        return self.cycle

    def setCycle(self, value: Optional[TimeValue]) -> "FlexrayCluster":
        """Length of the cycle. Unit: seconds
        A None value is a no-op and does not overwrite an existing cycle."""
        if value is not None:
            self.cycle = value
        return self

    def getCycleCountMax(self) -> Optional[Integer]:
        """Maximum cycle counter value in a given cluster. Remark: Set to 63 for FlexRay Protocol 2.1 Rev. A compliance."""
        return self.cycleCountMax

    def setCycleCountMax(self, value: Optional[Integer]) -> "FlexrayCluster":
        """Maximum cycle counter value in a given cluster. Remark: Set to 63 for FlexRay Protocol 2.1 Rev. A compliance.
        A None value is a no-op and does not overwrite an existing cycleCountMax."""
        if value is not None:
            self.cycleCountMax = value
        return self

    def getDetectNitError(self) -> Optional[Boolean]:
        """Indicates whether NIT error status of each cluster shall be detected or not."""
        return self.detectNitError

    def setDetectNitError(self, value: Optional[Boolean]) -> "FlexrayCluster":
        """Indicates whether NIT error status of each cluster shall be detected or not.
        A None value is a no-op and does not overwrite an existing detectNitError."""
        if value is not None:
            self.detectNitError = value
        return self

    def getDynamicSlotIdlePhase(self) -> Optional[Integer]:
        """The duration of the dynamic slot idle phase in minislots."""
        return self.dynamicSlotIdlePhase

    def setDynamicSlotIdlePhase(self, value: Optional[Integer]) -> "FlexrayCluster":
        """The duration of the dynamic slot idle phase in minislots.
        A None value is a no-op and does not overwrite an existing dynamicSlotIdlePhase."""
        if value is not None:
            self.dynamicSlotIdlePhase = value
        return self

    def getIgnoreAfterTx(self) -> Optional[Integer]:
        """Duration for which the bitstrobing is paused after transmission [gdBit]."""
        return self.ignoreAfterTx

    def setIgnoreAfterTx(self, value: Optional[Integer]) -> "FlexrayCluster":
        """Duration for which the bitstrobing is paused after transmission [gdBit].
        A None value is a no-op and does not overwrite an existing ignoreAfterTx."""
        if value is not None:
            self.ignoreAfterTx = value
        return self

    def getListenNoise(self) -> Optional[Integer]:
        """Upper limit for the start up and wake up listen timeout in the presence of noise. Expressed as a multiple of the cluster constant pdListenTimeout. Unit microticks"""
        return self.listenNoise

    def setListenNoise(self, value: Optional[Integer]) -> "FlexrayCluster":
        """Upper limit for the start up and wake up listen timeout in the presence of noise. Expressed as a multiple of the cluster constant pdListenTimeout. Unit microticks
        A None value is a no-op and does not overwrite an existing listenNoise."""
        if value is not None:
            self.listenNoise = value
        return self

    def getMacroPerCycle(self) -> Optional[Integer]:
        """The number of macroticks in a communication cycle"""
        return self.macroPerCycle

    def setMacroPerCycle(self, value: Optional[Integer]) -> "FlexrayCluster":
        """The number of macroticks in a communication cycle
        A None value is a no-op and does not overwrite an existing macroPerCycle."""
        if value is not None:
            self.macroPerCycle = value
        return self

    def getMacrotickDuration(self) -> Optional[TimeValue]:
        """Duration of the cluster wide nominal macrotick, expressed in s."""
        return self.macrotickDuration

    def setMacrotickDuration(self, value: Optional[TimeValue]) -> "FlexrayCluster":
        """Duration of the cluster wide nominal macrotick, expressed in s.
        A None value is a no-op and does not overwrite an existing macrotickDuration."""
        if value is not None:
            self.macrotickDuration = value
        return self

    def getMaxWithoutClockCorrectionFatal(self) -> Optional[Integer]:
        """Threshold concerning vClockCorrectionFailedCounter. Defines the number of consecutive even/odd Cycle pairs with missing clock correction terms that will cause the protocol to transition from the POC:normal active or POC:normal passive state into the POC:halt state."""
        return self.maxWithoutClockCorrectionFatal

    def setMaxWithoutClockCorrectionFatal(self, value: Optional[Integer]) -> "FlexrayCluster":
        """Threshold concerning vClockCorrectionFailedCounter. Defines the number of consecutive even/odd Cycle pairs with missing clock correction terms that will cause the protocol to transition from the POC:normal active or POC:normal passive state into the POC:halt state.
        A None value is a no-op and does not overwrite an existing maxWithoutClockCorrectionFatal."""
        if value is not None:
            self.maxWithoutClockCorrectionFatal = value
        return self

    def getMaxWithoutClockCorrectionPassive(self) -> Optional[Integer]:
        """Threshold concerning vClockCorrectionFailedCounter. Defines the number of consecutive even/odd Cycle pairs with missing clock correction terms that will cause the protocol to transition from the POC:normal active state to the POC:normal passive state."""
        return self.maxWithoutClockCorrectionPassive

    def setMaxWithoutClockCorrectionPassive(self, value: Optional[Integer]) -> "FlexrayCluster":
        """Threshold concerning vClockCorrectionFailedCounter. Defines the number of consecutive even/odd Cycle pairs with missing clock correction terms that will cause the protocol to transition from the POC:normal active state to the POC:normal passive state.
        A None value is a no-op and does not overwrite an existing maxWithoutClockCorrectionPassive."""
        if value is not None:
            self.maxWithoutClockCorrectionPassive = value
        return self

    def getMinislotActionPointOffset(self) -> Optional[Integer]:
        """The Offset of the action point within a minislot. Unit: macroticks"""
        return self.minislotActionPointOffset

    def setMinislotActionPointOffset(self, value: Optional[Integer]) -> "FlexrayCluster":
        """The Offset of the action point within a minislot. Unit: macroticks
        A None value is a no-op and does not overwrite an existing minislotActionPointOffset."""
        if value is not None:
            self.minislotActionPointOffset = value
        return self

    def getMinislotDuration(self) -> Optional[Integer]:
        """The duration of a minislot (dynamic segment). Unit: macroticks."""
        return self.minislotDuration

    def setMinislotDuration(self, value: Optional[Integer]) -> "FlexrayCluster":
        """The duration of a minislot (dynamic segment). Unit: macroticks.
        A None value is a no-op and does not overwrite an existing minislotDuration."""
        if value is not None:
            self.minislotDuration = value
        return self

    def getNetworkIdleTime(self) -> Optional[Integer]:
        """The duration of the network idle time in macroticks"""
        return self.networkIdleTime

    def setNetworkIdleTime(self, value: Optional[Integer]) -> "FlexrayCluster":
        """The duration of the network idle time in macroticks
        A None value is a no-op and does not overwrite an existing networkIdleTime."""
        if value is not None:
            self.networkIdleTime = value
        return self

    def getNetworkManagementVectorLength(self) -> Optional[Integer]:
        """Length of the Network Management vector in a cluster [bytes]"""
        return self.networkManagementVectorLength

    def setNetworkManagementVectorLength(self, value: Optional[Integer]) -> "FlexrayCluster":
        """Length of the Network Management vector in a cluster [bytes]
        A None value is a no-op and does not overwrite an existing networkManagementVectorLength."""
        if value is not None:
            self.networkManagementVectorLength = value
        return self

    def getNumberOfMinislots(self) -> Optional[Integer]:
        """Number of Minislots in the dynamic segment."""
        return self.numberOfMinislots

    def setNumberOfMinislots(self, value: Optional[Integer]) -> "FlexrayCluster":
        """Number of Minislots in the dynamic segment.
        A None value is a no-op and does not overwrite an existing numberOfMinislots."""
        if value is not None:
            self.numberOfMinislots = value
        return self

    def getNumberOfStaticSlots(self) -> Optional[Integer]:
        """The number of static slots in the static segment."""
        return self.numberOfStaticSlots

    def setNumberOfStaticSlots(self, value: Optional[Integer]) -> "FlexrayCluster":
        """The number of static slots in the static segment.
        A None value is a no-op and does not overwrite an existing numberOfStaticSlots."""
        if value is not None:
            self.numberOfStaticSlots = value
        return self

    def getOffsetCorrectionStart(self) -> Optional[Integer]:
        """Start of the offset correction phase within the Network Idle Time (NIT), expressed as the number of macroticks from the start of cycle. Unit: macroticks"""
        return self.offsetCorrectionStart

    def setOffsetCorrectionStart(self, value: Optional[Integer]) -> "FlexrayCluster":
        """Start of the offset correction phase within the Network Idle Time (NIT), expressed as the number of macroticks from the start of cycle. Unit: macroticks
        A None value is a no-op and does not overwrite an existing offsetCorrectionStart."""
        if value is not None:
            self.offsetCorrectionStart = value
        return self

    def getPayloadLengthStatic(self) -> Optional[Integer]:
        """Globally configured payload length of a static frame. Unit: 16-bit WORDS."""
        return self.payloadLengthStatic

    def setPayloadLengthStatic(self, value: Optional[Integer]) -> "FlexrayCluster":
        """Globally configured payload length of a static frame. Unit: 16-bit WORDS.
        A None value is a no-op and does not overwrite an existing payloadLengthStatic."""
        if value is not None:
            self.payloadLengthStatic = value
        return self

    def getSafetyMargin(self) -> Optional[Integer]:
        """Additional timespan in macroticks which takes jitter into account to be able to set the JobListPointer to the next possible job which can be executed in case the FlexRay Job List Execution Function has be resynchronized."""
        return self.safetyMargin

    def setSafetyMargin(self, value: Optional[Integer]) -> "FlexrayCluster":
        """Additional timespan in macroticks which takes jitter into account to be able to set the JobListPointer to the next possible job which can be executed in case the FlexRay Job List Execution Function has be resynchronized.
        A None value is a no-op and does not overwrite an existing safetyMargin."""
        if value is not None:
            self.safetyMargin = value
        return self

    def getSampleClockPeriod(self) -> Optional[TimeValue]:
        """Sample clock period. Unit: seconds"""
        return self.sampleClockPeriod

    def setSampleClockPeriod(self, value: Optional[TimeValue]) -> "FlexrayCluster":
        """Sample clock period. Unit: seconds
        A None value is a no-op and does not overwrite an existing sampleClockPeriod."""
        if value is not None:
            self.sampleClockPeriod = value
        return self

    def getStaticSlotDuration(self) -> Optional[Integer]:
        """The duration of a slot in the static segment. Unit: macroticks"""
        return self.staticSlotDuration

    def setStaticSlotDuration(self, value: Optional[Integer]) -> "FlexrayCluster":
        """The duration of a slot in the static segment. Unit: macroticks
        A None value is a no-op and does not overwrite an existing staticSlotDuration."""
        if value is not None:
            self.staticSlotDuration = value
        return self

    def getSymbolWindow(self) -> Optional[Integer]:
        """The duration of the symbol window. Unit: macroticks"""
        return self.symbolWindow

    def setSymbolWindow(self, value: Optional[Integer]) -> "FlexrayCluster":
        """The duration of the symbol window. Unit: macroticks
        A None value is a no-op and does not overwrite an existing symbolWindow."""
        if value is not None:
            self.symbolWindow = value
        return self

    def getSymbolWindowActionPointOffset(self) -> Optional[Integer]:
        """Number of macroticks the action point offset is from the beginning of the symbol window [Macroticks]."""
        return self.symbolWindowActionPointOffset

    def setSymbolWindowActionPointOffset(self, value: Optional[Integer]) -> "FlexrayCluster":
        """Number of macroticks the action point offset is from the beginning of the symbol window [Macroticks].
        A None value is a no-op and does not overwrite an existing symbolWindowActionPointOffset."""
        if value is not None:
            self.symbolWindowActionPointOffset = value
        return self

    def getSyncFrameIdCountMax(self) -> Optional[Integer]:
        """Maximum number of distinct syncframe identifiers present in a given cluster. This parameter maps to FlexRay Protocol 2.1 Rev. A parameter gSyncNodeMax."""
        return self.syncFrameIdCountMax

    def setSyncFrameIdCountMax(self, value: Optional[Integer]) -> "FlexrayCluster":
        """Maximum number of distinct syncframe identifiers present in a given cluster. This parameter maps to FlexRay Protocol 2.1 Rev. A parameter gSyncNodeMax.
        A None value is a no-op and does not overwrite an existing syncFrameIdCountMax."""
        if value is not None:
            self.syncFrameIdCountMax = value
        return self

    def getTranceiverStandbyDelay(self) -> Optional[Float]:
        """The duration of timer t_TrcvStdbyDelay in seconds. The granularity of this parameter shall be restricted to full Flex Ray cycles (cycle). The transceiver status setting to STANDBY shall be delayed by this value. Not specifying a value or a value of 0 shall imply that the timer is not used."""
        return self.tranceiverStandbyDelay

    def setTranceiverStandbyDelay(self, value: Optional[Float]) -> "FlexrayCluster":
        """The duration of timer t_TrcvStdbyDelay in seconds. The granularity of this parameter shall be restricted to full Flex Ray cycles (cycle). The transceiver status setting to STANDBY shall be delayed by this value. Not specifying a value or a value of 0 shall imply that the timer is not used.
        A None value is a no-op and does not overwrite an existing tranceiverStandbyDelay."""
        if value is not None:
            self.tranceiverStandbyDelay = value
        return self

    def getTransmissionStartSequenceDuration(self) -> Optional[Integer]:
        """Number of bits in the Transmission Start Sequence [gd Bits]."""
        return self.transmissionStartSequenceDuration

    def setTransmissionStartSequenceDuration(self, value: Optional[Integer]) -> "FlexrayCluster":
        """Number of bits in the Transmission Start Sequence [gd Bits].
        A None value is a no-op and does not overwrite an existing transmissionStartSequenceDuration."""
        if value is not None:
            self.transmissionStartSequenceDuration = value
        return self

    def getWakeupRxIdle(self) -> Optional[Integer]:
        """Number of bits used by the node to test the duration of the 'idle' or HIGH phase of a received wakeup. Unit:bit Duration Remarks: This parameter maps to FlexRay Protocol 2.1 Rev. A parameter gdWakeupSymbolRxIdle."""
        return self.wakeupRxIdle

    def setWakeupRxIdle(self, value: Optional[Integer]) -> "FlexrayCluster":
        """Number of bits used by the node to test the duration of the 'idle' or HIGH phase of a received wakeup. Unit:bit Duration Remarks: This parameter maps to FlexRay Protocol 2.1 Rev. A parameter gdWakeupSymbolRxIdle.
        A None value is a no-op and does not overwrite an existing wakeupRxIdle."""
        if value is not None:
            self.wakeupRxIdle = value
        return self

    def getWakeupRxLow(self) -> Optional[Integer]:
        """Number of bits used by the node to test the duration of the LOW phase of a received wakeup. Unit:bitDuration Remarks: This parameter maps to FlexRay Protocol 2.1 Rev. A parameter gdWakeupSymbolRxLow."""
        return self.wakeupRxLow

    def setWakeupRxLow(self, value: Optional[Integer]) -> "FlexrayCluster":
        """Number of bits used by the node to test the duration of the LOW phase of a received wakeup. Unit:bitDuration Remarks: This parameter maps to FlexRay Protocol 2.1 Rev. A parameter gdWakeupSymbolRxLow.
        A None value is a no-op and does not overwrite an existing wakeupRxLow."""
        if value is not None:
            self.wakeupRxLow = value
        return self

    def getWakeupRxWindow(self) -> Optional[Integer]:
        """The size of the window used to detect wakeups [gdBit]. Remarks: This parameter maps to FlexRay Protocol 2.1 Rev. A parameter gdWakeupSymbolRxWindow."""
        return self.wakeupRxWindow

    def setWakeupRxWindow(self, value: Optional[Integer]) -> "FlexrayCluster":
        """The size of the window used to detect wakeups [gdBit]. Remarks: This parameter maps to FlexRay Protocol 2.1 Rev. A parameter gdWakeupSymbolRxWindow.
        A None value is a no-op and does not overwrite an existing wakeupRxWindow."""
        if value is not None:
            self.wakeupRxWindow = value
        return self

    def getWakeupTxActive(self) -> Optional[Integer]:
        """Number of bits used by the node to transmit the LOW phase of awakeup symbol and the HIGH and LOW phases of a WUDOP. Unit:bitDuration"""
        return self.wakeupTxActive

    def setWakeupTxActive(self, value: Optional[Integer]) -> "FlexrayCluster":
        """Number of bits used by the node to transmit the LOW phase of awakeup symbol and the HIGH and LOW phases of a WUDOP. Unit:bitDuration
        A None value is a no-op and does not overwrite an existing wakeupTxActive."""
        if value is not None:
            self.wakeupTxActive = value
        return self

    def getWakeupTxIdle(self) -> Optional[Integer]:
        """Number of bits used by the node to transmit the 'idle' part of a wakeup symbol. Unit: gDbit"""
        return self.wakeupTxIdle

    def setWakeupTxIdle(self, value: Optional[Integer]) -> "FlexrayCluster":
        """Number of bits used by the node to transmit the 'idle' part of a wakeup symbol. Unit: gDbit
        A None value is a no-op and does not overwrite an existing wakeupTxIdle."""
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


class FlexrayPhysicalChannel(PhysicalChannel):
    """
    Represents a FlexRay physical channel in the communication system,
    defining FlexRay-specific properties including channel name
    designation for dual-channel FlexRay communication.
    """

    # FlexrayPhysicalChannel method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getChannelName               [x] impl  [ ] docstring  [ ] test
    # [ ] setChannelName               [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.channelName = None  # type: FlexrayChannelName

    def getChannelName(self):
        return self.channelName

    def setChannelName(self, value):
        if value is not None:
            self.channelName = value
        return self
