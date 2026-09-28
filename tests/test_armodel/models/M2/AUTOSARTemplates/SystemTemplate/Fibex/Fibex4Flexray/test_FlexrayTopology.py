import inspect
from typing import List, Optional, get_type_hints

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Float, Integer, PositiveInteger, RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology import (
    FlexrayCluster,
    FlexrayCommunicationConnector,
    FlexrayCommunicationController,
    FlexrayFifoConfiguration,
    FlexrayFifoRange,
    FlexrayPhysicalChannel,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommunicationCluster, CommunicationConnector, CommunicationController, FlexrayChannelName, PhysicalChannel


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class TestFlexrayTopology:
    """
    Test class for FlexrayTopology module functionality.
    This class contains test methods for validating the behavior of
    FlexRay communication topology classes, including their initialization,
    inheritance relationships, and property accessors.
    """

    def test_flexray_cluster(self):
        """
        Test the FlexrayCluster class initialization and methods with method chaining and None handling.
        """
        parent = MockParent()
        cluster = FlexrayCluster(parent, "TestCluster")

        assert cluster.getShortName() == "TestCluster"
        assert isinstance(cluster, CommunicationCluster)
        assert cluster.getActionPointOffset() is None
        assert cluster.getBit() is None
        assert cluster.getCasRxLowMax() is None
        assert cluster.getColdStartAttempts() is None
        assert cluster.getCycle() is None
        assert cluster.getCycleCountMax() is None
        assert cluster.getDetectNitError() is None
        assert cluster.getDynamicSlotIdlePhase() is None
        assert cluster.getIgnoreAfterTx() is None
        assert cluster.getListenNoise() is None
        assert cluster.getMacroPerCycle() is None
        assert cluster.getMacrotickDuration() is None
        assert cluster.getMaxWithoutClockCorrectionFatal() is None
        assert cluster.getMaxWithoutClockCorrectionPassive() is None
        assert cluster.getMinislotActionPointOffset() is None
        assert cluster.getMinislotDuration() is None
        assert cluster.getNetworkIdleTime() is None
        assert cluster.getNetworkManagementVectorLength() is None
        assert cluster.getNumberOfMinislots() is None
        assert cluster.getNumberOfStaticSlots() is None
        assert cluster.getOffsetCorrectionStart() is None
        assert cluster.getPayloadLengthStatic() is None
        assert cluster.getSafetyMargin() is None
        assert cluster.getSampleClockPeriod() is None
        assert cluster.getStaticSlotDuration() is None
        assert cluster.getSymbolWindow() is None
        assert cluster.getSymbolWindowActionPointOffset() is None
        assert cluster.getSyncFrameIdCountMax() is None
        assert cluster.getTranceiverStandbyDelay() is None
        assert cluster.getTransmissionStartSequenceDuration() is None
        assert cluster.getWakeupRxIdle() is None
        assert cluster.getWakeupRxLow() is None
        assert cluster.getWakeupRxWindow() is None
        assert cluster.getWakeupTxActive() is None
        assert cluster.getWakeupTxIdle() is None

        # Test setter/getter methods with method chaining - with None values
        assert cluster == cluster.setActionPointOffset(None)
        assert cluster.getActionPointOffset() is None

        assert cluster == cluster.setBit(None)
        assert cluster.getBit() is None

        assert cluster == cluster.setCasRxLowMax(None)
        assert cluster.getCasRxLowMax() is None

        assert cluster == cluster.setColdStartAttempts(None)
        assert cluster.getColdStartAttempts() is None

        assert cluster == cluster.setCycle(None)
        assert cluster.getCycle() is None

        assert cluster == cluster.setCycleCountMax(None)
        assert cluster.getCycleCountMax() is None

        assert cluster == cluster.setDetectNitError(None)
        assert cluster.getDetectNitError() is None

        assert cluster == cluster.setDynamicSlotIdlePhase(None)
        assert cluster.getDynamicSlotIdlePhase() is None

        assert cluster == cluster.setIgnoreAfterTx(None)
        assert cluster.getIgnoreAfterTx() is None

        assert cluster == cluster.setListenNoise(None)
        assert cluster.getListenNoise() is None

        assert cluster == cluster.setMacroPerCycle(None)
        assert cluster.getMacroPerCycle() is None

        assert cluster == cluster.setMacrotickDuration(None)
        assert cluster.getMacrotickDuration() is None

        assert cluster == cluster.setMaxWithoutClockCorrectionFatal(None)
        assert cluster.getMaxWithoutClockCorrectionFatal() is None

        assert cluster == cluster.setMaxWithoutClockCorrectionPassive(None)
        assert cluster.getMaxWithoutClockCorrectionPassive() is None

        assert cluster == cluster.setMinislotActionPointOffset(None)
        assert cluster.getMinislotActionPointOffset() is None

        assert cluster == cluster.setMinislotDuration(None)
        assert cluster.getMinislotDuration() is None

        assert cluster == cluster.setNetworkIdleTime(None)
        assert cluster.getNetworkIdleTime() is None

        assert cluster == cluster.setNetworkManagementVectorLength(None)
        assert cluster.getNetworkManagementVectorLength() is None

        assert cluster == cluster.setNumberOfMinislots(None)
        assert cluster.getNumberOfMinislots() is None

        assert cluster == cluster.setNumberOfStaticSlots(None)
        assert cluster.getNumberOfStaticSlots() is None

        assert cluster == cluster.setOffsetCorrectionStart(None)
        assert cluster.getOffsetCorrectionStart() is None

        assert cluster == cluster.setPayloadLengthStatic(None)
        assert cluster.getPayloadLengthStatic() is None

        assert cluster == cluster.setSafetyMargin(None)
        assert cluster.getSafetyMargin() is None

        assert cluster == cluster.setSampleClockPeriod(None)
        assert cluster.getSampleClockPeriod() is None

        assert cluster == cluster.setStaticSlotDuration(None)
        assert cluster.getStaticSlotDuration() is None

        assert cluster == cluster.setSymbolWindow(None)
        assert cluster.getSymbolWindow() is None

        assert cluster == cluster.setSymbolWindowActionPointOffset(None)
        assert cluster.getSymbolWindowActionPointOffset() is None

        assert cluster == cluster.setSyncFrameIdCountMax(None)
        assert cluster.getSyncFrameIdCountMax() is None

        assert cluster == cluster.setTranceiverStandbyDelay(None)
        assert cluster.getTranceiverStandbyDelay() is None

        assert cluster == cluster.setTransmissionStartSequenceDuration(None)
        assert cluster.getTransmissionStartSequenceDuration() is None

        assert cluster == cluster.setWakeupRxIdle(None)
        assert cluster.getWakeupRxIdle() is None

        assert cluster == cluster.setWakeupRxLow(None)
        assert cluster.getWakeupRxLow() is None

        assert cluster == cluster.setWakeupRxWindow(None)
        assert cluster.getWakeupRxWindow() is None

        assert cluster == cluster.setWakeupTxActive(None)
        assert cluster.getWakeupTxActive() is None

        assert cluster == cluster.setWakeupTxIdle(None)
        assert cluster.getWakeupTxIdle() is None

        # Test setter/getter methods with method chaining - with actual values
        cluster.setActionPointOffset(10)
        assert cluster.getActionPointOffset() == 10
        assert cluster == cluster.setActionPointOffset(10)

        cluster.setBit(25.0)
        assert cluster.getBit() == 25.0
        assert cluster == cluster.setBit(25.0)

        cluster.setColdStartAttempts(5)
        assert cluster.getColdStartAttempts() == 5
        assert cluster == cluster.setColdStartAttempts(5)

        cluster.setCycle(100.0)
        assert cluster.getCycle() == 100.0
        assert cluster == cluster.setCycle(100.0)

        cluster.setDetectNitError(True)
        assert cluster.getDetectNitError() is True
        assert cluster == cluster.setDetectNitError(True)

        cluster.setDynamicSlotIdlePhase(15)
        assert cluster.getDynamicSlotIdlePhase() == 15
        assert cluster == cluster.setDynamicSlotIdlePhase(15)

        cluster.setMacroPerCycle(200)
        assert cluster.getMacroPerCycle() == 200
        assert cluster == cluster.setMacroPerCycle(200)

        cluster.setMacrotickDuration(1000.0)
        assert cluster.getMacrotickDuration() == 1000.0
        assert cluster == cluster.setMacrotickDuration(1000.0)

        cluster.setNumberOfMinislots(100)
        assert cluster.getNumberOfMinislots() == 100
        assert cluster == cluster.setNumberOfMinislots(100)

        cluster.setNumberOfStaticSlots(50)
        assert cluster.getNumberOfStaticSlots() == 50
        assert cluster == cluster.setNumberOfStaticSlots(50)

        cluster.setSafetyMargin(5)
        assert cluster.getSafetyMargin() == 5
        assert cluster == cluster.setSafetyMargin(5)

        cluster.setStaticSlotDuration(10)
        assert cluster.getStaticSlotDuration() == 10
        assert cluster == cluster.setStaticSlotDuration(10)

        cluster.setSymbolWindow(20)
        assert cluster.getSymbolWindow() == 20
        assert cluster == cluster.setSymbolWindow(20)

        cluster.setSyncFrameIdCountMax(10)
        assert cluster.getSyncFrameIdCountMax() == 10
        assert cluster == cluster.setSyncFrameIdCountMax(10)

        cluster.setTranceiverStandbyDelay(0.5)
        assert cluster.getTranceiverStandbyDelay() == 0.5
        assert cluster == cluster.setTranceiverStandbyDelay(0.5)

        cluster.setTransmissionStartSequenceDuration(25)
        assert cluster.getTransmissionStartSequenceDuration() == 25
        assert cluster == cluster.setTransmissionStartSequenceDuration(25)

        cluster.setWakeupRxIdle(100)
        assert cluster.getWakeupRxIdle() == 100
        assert cluster == cluster.setWakeupRxIdle(100)

        cluster.setWakeupRxLow(200)
        assert cluster.getWakeupRxLow() == 200
        assert cluster == cluster.setWakeupRxLow(200)

        cluster.setWakeupRxWindow(300)
        assert cluster.getWakeupRxWindow() == 300
        assert cluster == cluster.setWakeupRxWindow(300)

        cluster.setWakeupTxActive(400)
        assert cluster.getWakeupTxActive() == 400
        assert cluster == cluster.setWakeupTxActive(400)

        cluster.setWakeupTxIdle(500)
        assert cluster.getWakeupTxIdle() == 500
        assert cluster == cluster.setWakeupTxIdle(500)

        # Test remaining setter methods to ensure 100% coverage
        cluster.setCasRxLowMax(100)
        assert cluster.getCasRxLowMax() == 100

        cluster.setCycleCountMax(10)
        assert cluster.getCycleCountMax() == 10

        cluster.setIgnoreAfterTx(15)
        assert cluster.getIgnoreAfterTx() == 15

        cluster.setListenNoise(20)
        assert cluster.getListenNoise() == 20

        cluster.setMinislotActionPointOffset(25)
        assert cluster.getMinislotActionPointOffset() == 25

        cluster.setMinislotDuration(30)
        assert cluster.getMinislotDuration() == 30

        cluster.setNetworkIdleTime(35)
        assert cluster.getNetworkIdleTime() == 35

        cluster.setNetworkManagementVectorLength(40)
        assert cluster.getNetworkManagementVectorLength() == 40

        cluster.setOffsetCorrectionStart(45)
        assert cluster.getOffsetCorrectionStart() == 45

        cluster.setPayloadLengthStatic(50)
        assert cluster.getPayloadLengthStatic() == 50

        cluster.setSampleClockPeriod(55.0)
        assert cluster.getSampleClockPeriod() == 55.0

        cluster.setSymbolWindowActionPointOffset(60)
        assert cluster.getSymbolWindowActionPointOffset() == 60

        # Ensure the two remaining methods are specifically tested for 100% coverage
        cluster.setMaxWithoutClockCorrectionFatal(65)
        assert cluster.getMaxWithoutClockCorrectionFatal() == 65
        assert cluster == cluster.setMaxWithoutClockCorrectionFatal(65)

        cluster.setMaxWithoutClockCorrectionPassive(35)
        assert cluster.getMaxWithoutClockCorrectionPassive() == 35
        assert cluster == cluster.setMaxWithoutClockCorrectionPassive(35)


class TestFlexrayFifoRange:
    def test_flexray_fifo_range_defaults(self):
        fifo_range = FlexrayFifoRange()
        assert isinstance(fifo_range, ARObject)
        assert fifo_range.getRangeMax() is None
        assert fifo_range.getRangeMin() is None

    def test_flexray_fifo_range_setters(self):
        fifo_range = FlexrayFifoRange()
        assert fifo_range == fifo_range.setRangeMax(200)
        assert fifo_range.getRangeMax() == 200
        assert fifo_range == fifo_range.setRangeMin(100)
        assert fifo_range.getRangeMin() == 100

    def test_flexray_fifo_range_none_noop(self):
        fifo_range = FlexrayFifoRange()
        fifo_range.setRangeMax(200)
        fifo_range.setRangeMin(100)
        fifo_range.setRangeMax(None)
        fifo_range.setRangeMin(None)
        assert fifo_range.getRangeMax() == 200
        assert fifo_range.getRangeMin() == 100


class TestFlexrayFifoConfiguration:
    def test_defaults(self):
        config = FlexrayFifoConfiguration()
        assert isinstance(config, ARObject)
        assert config.getAdmitWithoutMessageId() is None
        assert config.getBaseCycle() is None
        assert config.getChannelRef() is None
        assert config.getCycleRepetition() is None
        assert config.getFifoDepth() is None
        assert config.getFlexrayFifoRanges() == []
        assert config.getMsgIdMask() is None
        assert config.getMsgIdMatch() is None

    def test_setters(self):
        config = FlexrayFifoConfiguration()
        assert config == config.setAdmitWithoutMessageId(True)
        assert config.getAdmitWithoutMessageId() is True
        assert config == config.setBaseCycle(2)
        assert config.getBaseCycle() == 2
        assert config == config.setCycleRepetition(4)
        assert config.getCycleRepetition() == 4
        assert config == config.setFifoDepth(8)
        assert config.getFifoDepth() == 8
        assert config == config.setMsgIdMask(16)
        assert config.getMsgIdMask() == 16
        assert config == config.setMsgIdMatch(32)
        assert config.getMsgIdMatch() == 32

    def test_channel_ref_setter(self):
        config = FlexrayFifoConfiguration()
        ref = RefType()
        ref.setValue("/FlexrayCluster/ChannelA")
        assert config == config.setChannelRef(ref)
        assert config.getChannelRef() is ref

    def test_create_fifo_range(self):
        config = FlexrayFifoConfiguration()
        range_1 = config.createFlexrayFifoRange()
        range_1.setRangeMax(200)
        range_2 = config.createFlexrayFifoRange()
        assert config.getFlexrayFifoRanges() == [range_1, range_2]

    def test_none_noop(self):
        config = FlexrayFifoConfiguration()
        config.setBaseCycle(2)
        config.setBaseCycle(None)
        assert config.getBaseCycle() == 2


FLEXRAY_COMMUNICATION_CONNECTOR_CLASS_NOTE = (
    "FlexRay specific attributes to the CommunicationConnector\n" "\n" "[constr_3508] Value of nmReadySleepTime: The nmReadySleepTime value shall be a multiple of cycle * nmRepetitionCycle."
)
NM_READY_SLEEP_TIME_NOTE = "The value of this attribute influences the shutdown behavior of the FlexRay NM. FrNm switches to bus sleep mode nmReadySleepTime seconds after the completion of the last repetition cycle containing a NM vote."
WAKE_UP_CHANNEL_NOTE = "Referenced channel used by the node to send a wakeup pattern. (pWakeupChannel)"


class TestFlexrayCommunicationConnector:
    def _make(self) -> FlexrayCommunicationConnector:
        return FlexrayCommunicationConnector(MockParent(), "test_flexray_comm_connector")

    def _assert_docstring(self, method, note, attr_name=None):
        expected = note if attr_name is None else note + "\nA None value is a no-op and does not overwrite an existing %s." % attr_name
        assert method.__doc__ is not None
        assert inspect.cleandoc(method.__doc__).strip() == expected

    def test_initialization(self):
        connector = self._make()

        assert connector.getShortName() == "test_flexray_comm_connector"
        assert isinstance(connector, CommunicationConnector)
        assert connector.getNmReadySleepTime() is None
        assert connector.getWakeUpChannel() is None
        assert not hasattr(connector, "getPncFilterDataMask")

    def test_class_docstring_is_spec_note(self):
        assert inspect.cleandoc(FlexrayCommunicationConnector.__doc__).strip() == FLEXRAY_COMMUNICATION_CONNECTOR_CLASS_NOTE

    def test_init_has_no_docstring(self):
        assert FlexrayCommunicationConnector.__init__.__doc__ is None

    def test_member_order_matches_spec(self):
        source = inspect.getsource(FlexrayCommunicationConnector.__init__)
        assert source.index("self.nmReadySleepTime:") < source.index("self.wakeUpChannel:")

    def test_get_set_nm_ready_sleep_time(self):
        connector = self._make()

        assert connector.getNmReadySleepTime() is None

        seconds = Float()
        seconds.setValue("10.5")
        assert connector == connector.setNmReadySleepTime(seconds)
        assert connector.getNmReadySleepTime() == seconds

        assert connector == connector.setNmReadySleepTime(None)
        assert connector.getNmReadySleepTime() == seconds

        getter_hints = get_type_hints(FlexrayCommunicationConnector.getNmReadySleepTime)
        assert getter_hints.get("return") == Optional[Float]

        setter_hints = get_type_hints(FlexrayCommunicationConnector.setNmReadySleepTime)
        assert setter_hints.get("value") == Optional[Float]
        assert setter_hints.get("return") is FlexrayCommunicationConnector

    def test_nm_ready_sleep_time_docstrings_are_spec_note(self):
        self._assert_docstring(FlexrayCommunicationConnector.getNmReadySleepTime, NM_READY_SLEEP_TIME_NOTE)
        self._assert_docstring(FlexrayCommunicationConnector.setNmReadySleepTime, NM_READY_SLEEP_TIME_NOTE, "nmReadySleepTime")

    def test_get_set_wake_up_channel(self):
        connector = self._make()

        assert connector.getWakeUpChannel() is None

        flag = Boolean()
        flag.setValue(True)
        assert connector == connector.setWakeUpChannel(flag)
        assert connector.getWakeUpChannel() == flag

        assert connector == connector.setWakeUpChannel(None)
        assert connector.getWakeUpChannel() == flag

        getter_hints = get_type_hints(FlexrayCommunicationConnector.getWakeUpChannel)
        assert getter_hints.get("return") == Optional[Boolean]

        setter_hints = get_type_hints(FlexrayCommunicationConnector.setWakeUpChannel)
        assert setter_hints.get("value") == Optional[Boolean]
        assert setter_hints.get("return") is FlexrayCommunicationConnector

    def test_wake_up_channel_docstrings_are_spec_note(self):
        self._assert_docstring(FlexrayCommunicationConnector.getWakeUpChannel, WAKE_UP_CHANNEL_NOTE)
        self._assert_docstring(FlexrayCommunicationConnector.setWakeUpChannel, WAKE_UP_CHANNEL_NOTE, "wakeUpChannel")


FLEXRAY_COMMUNICATION_CONTROLLER_CLASS_NOTE = "FlexRay bus specific communication port attributes."
ACCEPTED_STARTUP_RANGE_NOTE = "Expanded range of measured clock deviation allowed for startup frames during integration. Unit:microtick"
ALLOW_HALT_DUE_TO_CLOCK_NOTE = "Boolean flag that controls the transition to the POC:halt state due to a clock synchronization errors. If set to true, the Communication Controller is allowed to transition to POC:halt. If set to false, the Communication Controller will not transition to the POC:halt state but will enter or remain in the normal POC (passive State)."
ALLOW_PASSIVE_TO_ACTIVE_NOTE = "Number of consecutive even/odd cycle pairs that shall have valid clock correction terms before the Communication Controller will be allowed to transition from the POC:normal passive state to POC:normal active state. If set to 0, the Communication Controller is not allowed to transition from POC:norm"
CLUSTER_DRIFT_DAMPING_NOTE = "The cluster drift damping factor used in clock synchronization rate correction in microticks"
DECODING_CORRECTION_NOTE = "Value used by the receiver to calculate the difference between primary time reference point and secondary time reference point. Unit: Microticks (pDecodingCorrection)"
DELAY_COMPENSATION_A_NOTE = "Value used to compensate for reception delays on channel A Unit: Microticks. This optional parameter shall only be filled out if channel A is used."
DELAY_COMPENSATION_B_NOTE = "Value used to compensate for reception delays on channel B. Unit: Microticks. This optional parameter shall only be filled out if channel B is used."
EXTERNAL_SYNC_NOTE = "Flag indicating whether the node is externally synchronized (operating as Time Gateway Sink in an TT-E Time Triggered External Sync cluster) or locally synchronized."
EXTERN_OFFSET_CORRECTION_NOTE = "Fixed amount added or subtracted to the calculated offset correction term to facilitate external offset correction, expressed in node-local microticks."
EXTERN_RATE_CORRECTION_NOTE = "Fixed amount added or subtracted to the calculated rate correction term to facilitate external rate correction, expressed in node-local microticks."
FALL_BACK_INTERNAL_NOTE = "Flag indicating whether a Time Gateway Sink node will switch to local clock operation when synchronization with the Time Gateway Source node is lost (pFallBackInternal = true) or will instead go to POC:ready (pFallBackInternal = false)."
FLEXRAY_FIFO_NOTE = "One First In First Out (FIFO) queued receive structure, defining the admittance criteria to the FIFO."
KEY_SLOT_ID_NOTE = "ID of the slot used to transmit the startup frame, sync frame, or designated single slot frame. If the attributes keySlotUsedForStartUp, keySlotUsedForSync, or keySlotOnlyEnabled are set to true the key slot value is mandatory."
KEY_SLOT_ONLY_ENABLED_NOTE = "Flag indicating whether or not the node shall enter key slot only mode following startup."
KEY_SLOT_USED_FOR_START_UP_NOTE = "Flag indicating whether the Key Slot is used to transmit a startup frame."
KEY_SLOT_USED_FOR_SYNC_NOTE = "Flag indicating whether the Key Slot is used to transmit a sync frame."
LATEST_TX_NOTE = "The number of the last minislot in which a transmission can start in the dynamic segment for the respective node"
LISTEN_TIMEOUT_NOTE = "Value for the startup listen timeout and wakeup listen timeout. Although this is a node local parameter, the real time equivalent of this value should be the same for all nodes in the cluster. Unit: Microticks"
MACRO_INITIAL_OFFSET_A_NOTE = "Integer number of macroticks between the static slot boundary and the closest macrotick boundary of the secondary time reference point based on the nominal macrotick duration. (pMacroInitialOffset). This optional parameter shall only be filled out if channel A is used."
MACRO_INITIAL_OFFSET_B_NOTE = "Integer number of macroticks between the static slot boundary and the closest macrotick boundary of the secondary time reference point based on the nominal macrotick duration. (pMacroInitialOffset). This optional parameter shall only be filled out if channel B is used."
MAXIMUM_DYNAMIC_PAYLOAD_LENGTH_NOTE = "Maximum payload length for the dynamic channel of a frame in 16 bit WORDS."
MICRO_INITIAL_OFFSET_A_NOTE = "Number of microticks between the closest macrotick boundary described by gMacroInitialOffset and the secondary time reference point. The parameter depends on pDelayCompensationA and therefore it has to be set independently for each channel. This optional parameter shall only be filled out if channel A is used."
MICRO_INITIAL_OFFSET_B_NOTE = "Number of microticks between the closest macrotick boundary described by gMacroInitialOffset and the secondary time reference point. The parameter depends on pDelayCompensationB and therefore it has to be set independently for each channel. This optional parameter shall only be filled out if channel B is used."
MICRO_PER_CYCLE_NOTE = "The nominal number of microticks in a communication cycle"
MICROTICK_DURATION_NOTE = "Duration of a microtick. This attribute can be derived from samplePerMicrotick and gdSampleClockPeriod. Unit: seconds"
NM_VECTOR_EARLY_UPDATE_NOTE = "Flag indicating when the update of the Network Management Vector in the CHI shall take place. If set to false, the update shall take place after the NIT. If set to true, the update shall take place after the end of the static segment."
OFFSET_CORRECTION_OUT_NOTE = "Magnitude of the maximum permissible offset correction value. Unit:microtick (pOffsetCorrectionOut)"
RATE_CORRECTION_OUT_NOTE = "Magnitude of the maximum permissible rate correction value and the maximum drift offset between two nodes operating with unsynchronized clocks for one communication cycle. Unit:Microticks (pRateCorrectionOut) Remarks: This parameter maps to FlexRay Protocol 2.1 Rev. A parameter pdMaxDrift."
SAMPLES_PER_MICROTICK_NOTE = "Number of samples per microtick"
SECOND_KEY_SLOT_ID_NOTE = "ID of the second Key slot, in which a second startup frame shall be sent in TT-L Time Triggered Local Master Sync or TT-E Time Triggered External Sync mode. If this parameter is set to zero the node does not have a second key slot."
TWO_KEY_SLOT_MODE_NOTE = "Flag indicating whether node operates as a startup node in a TT-E Time Triggered External Sync or TT-L Time Triggered Local Master Sync cluster."
WAKE_UP_PATTERN_NOTE = "Number of repetitions of the Tx-wakeup symbol to be sent during the CC_WakeupSend state of this Node in the cluster"


class TestFlexrayCommunicationController:
    def _make(self) -> FlexrayCommunicationController:
        return FlexrayCommunicationController(MockParent(), "test_flexray_comm_controller")

    def _assert_docstring(self, method, note, attr_name=None):
        expected = note if attr_name is None else note + "\nA None value is a no-op and does not overwrite an existing %s." % attr_name
        assert method.__doc__ is not None
        assert inspect.cleandoc(method.__doc__).strip() == expected

    def _pin(self, getter, setter, typ, owner):
        getter_hints = get_type_hints(getter)
        assert getter_hints.get("return") == typ
        setter_hints = get_type_hints(setter)
        assert setter_hints.get("value") == typ
        assert setter_hints.get("return") is owner

    def test_initialization(self):
        controller = self._make()

        assert controller.getShortName() == "test_flexray_comm_controller"
        assert isinstance(controller, CommunicationController)
        assert controller.getAcceptedStartupRange() is None
        assert controller.getAllowHaltDueToClock() is None
        assert controller.getAllowPassiveToActive() is None
        assert controller.getClusterDriftDamping() is None
        assert controller.getDecodingCorrection() is None
        assert controller.getDelayCompensationA() is None
        assert controller.getDelayCompensationB() is None
        assert controller.getExternalSync() is None
        assert controller.getExternOffsetCorrection() is None
        assert controller.getExternRateCorrection() is None
        assert controller.getFallBackInternal() is None
        assert controller.getFlexrayFifos() == []
        assert controller.getKeySlotID() is None
        assert controller.getKeySlotOnlyEnabled() is None
        assert controller.getKeySlotUsedForStartUp() is None
        assert controller.getKeySlotUsedForSync() is None
        assert controller.getLatestTX() is None
        assert controller.getListenTimeout() is None
        assert controller.getMacroInitialOffsetA() is None
        assert controller.getMacroInitialOffsetB() is None
        assert controller.getMaximumDynamicPayloadLength() is None
        assert controller.getMicroInitialOffsetA() is None
        assert controller.getMicroInitialOffsetB() is None
        assert controller.getMicroPerCycle() is None
        assert controller.getMicrotickDuration() is None
        assert controller.getNmVectorEarlyUpdate() is None
        assert controller.getOffsetCorrectionOut() is None
        assert controller.getRateCorrectionOut() is None
        assert controller.getSamplesPerMicrotick() is None
        assert controller.getSecondKeySlotId() is None
        assert controller.getTwoKeySlotMode() is None
        assert controller.getWakeUpPattern() is None

    def test_class_docstring_is_spec_note(self):
        assert inspect.cleandoc(FlexrayCommunicationController.__doc__).strip() == FLEXRAY_COMMUNICATION_CONTROLLER_CLASS_NOTE

    def test_init_has_no_docstring(self):
        assert FlexrayCommunicationController.__init__.__doc__ is None

    def test_member_order_matches_spec(self):
        source = inspect.getsource(FlexrayCommunicationController.__init__)
        order = [
            "self.acceptedStartupRange:",
            "self.allowHaltDueToClock:",
            "self.allowPassiveToActive:",
            "self.clusterDriftDamping:",
            "self.decodingCorrection:",
            "self.delayCompensationA:",
            "self.delayCompensationB:",
            "self.externalSync:",
            "self.externOffsetCorrection:",
            "self.externRateCorrection:",
            "self.fallBackInternal:",
            "self.flexrayFifos:",
            "self.keySlotID:",
            "self.keySlotOnlyEnabled:",
            "self.keySlotUsedForStartUp:",
            "self.keySlotUsedForSync:",
            "self.latestTX:",
            "self.listenTimeout:",
            "self.macroInitialOffsetA:",
            "self.macroInitialOffsetB:",
            "self.maximumDynamicPayloadLength:",
            "self.microInitialOffsetA:",
            "self.microInitialOffsetB:",
            "self.microPerCycle:",
            "self.microtickDuration:",
            "self.nmVectorEarlyUpdate:",
            "self.offsetCorrectionOut:",
            "self.rateCorrectionOut:",
            "self.samplesPerMicrotick:",
            "self.secondKeySlotId:",
            "self.twoKeySlotMode:",
            "self.wakeUpPattern:",
        ]
        indexes = [source.index(member) for member in order]
        assert indexes == sorted(indexes)

    def test_wake_up_by_controller_supported_base_properties(self):
        controller = self._make()

        assert controller.getWakeUpByControllerSupported() is None

        flag = Boolean()
        flag.setValue(True)
        assert controller == controller.setWakeUpByControllerSupported(flag)
        assert controller.getWakeUpByControllerSupported() == flag

        assert controller == controller.setWakeUpByControllerSupported(None)
        assert controller.getWakeUpByControllerSupported() == flag

        self._pin(CommunicationController.getWakeUpByControllerSupported, CommunicationController.setWakeUpByControllerSupported, Optional[Boolean], CommunicationController)

    def test_create_flexray_fifo_factory_removed(self):
        assert not hasattr(FlexrayCommunicationController, "createFlexrayFifo")

    def test_get_set_accepted_startup_range(self):
        controller = self._make()
        value = Integer().setValue("4")
        assert controller == controller.setAcceptedStartupRange(value)
        assert controller.getAcceptedStartupRange() == value
        assert controller == controller.setAcceptedStartupRange(None)
        assert controller.getAcceptedStartupRange() == value
        self._pin(FlexrayCommunicationController.getAcceptedStartupRange, FlexrayCommunicationController.setAcceptedStartupRange, Optional[Integer], FlexrayCommunicationController)

    def test_accepted_startup_range_docstrings_are_spec_note(self):
        self._assert_docstring(FlexrayCommunicationController.getAcceptedStartupRange, ACCEPTED_STARTUP_RANGE_NOTE)
        self._assert_docstring(FlexrayCommunicationController.setAcceptedStartupRange, ACCEPTED_STARTUP_RANGE_NOTE, "acceptedStartupRange")

    def test_get_set_allow_halt_due_to_clock(self):
        controller = self._make()
        value = Boolean().setValue(True)
        assert controller == controller.setAllowHaltDueToClock(value)
        assert controller.getAllowHaltDueToClock() == value
        assert controller == controller.setAllowHaltDueToClock(None)
        assert controller.getAllowHaltDueToClock() == value
        self._pin(FlexrayCommunicationController.getAllowHaltDueToClock, FlexrayCommunicationController.setAllowHaltDueToClock, Optional[Boolean], FlexrayCommunicationController)

    def test_allow_halt_due_to_clock_docstrings_are_spec_note(self):
        self._assert_docstring(FlexrayCommunicationController.getAllowHaltDueToClock, ALLOW_HALT_DUE_TO_CLOCK_NOTE)
        self._assert_docstring(FlexrayCommunicationController.setAllowHaltDueToClock, ALLOW_HALT_DUE_TO_CLOCK_NOTE, "allowHaltDueToClock")

    def test_get_set_allow_passive_to_active(self):
        controller = self._make()
        value = Integer().setValue("3")
        assert controller == controller.setAllowPassiveToActive(value)
        assert controller.getAllowPassiveToActive() == value
        assert controller == controller.setAllowPassiveToActive(None)
        assert controller.getAllowPassiveToActive() == value
        self._pin(FlexrayCommunicationController.getAllowPassiveToActive, FlexrayCommunicationController.setAllowPassiveToActive, Optional[Integer], FlexrayCommunicationController)

    def test_allow_passive_to_active_docstrings_are_spec_note(self):
        self._assert_docstring(FlexrayCommunicationController.getAllowPassiveToActive, ALLOW_PASSIVE_TO_ACTIVE_NOTE)
        self._assert_docstring(FlexrayCommunicationController.setAllowPassiveToActive, ALLOW_PASSIVE_TO_ACTIVE_NOTE, "allowPassiveToActive")

    def test_get_set_cluster_drift_damping(self):
        controller = self._make()
        value = Integer().setValue("4")
        assert controller == controller.setClusterDriftDamping(value)
        assert controller.getClusterDriftDamping() == value
        assert controller == controller.setClusterDriftDamping(None)
        assert controller.getClusterDriftDamping() == value
        self._pin(FlexrayCommunicationController.getClusterDriftDamping, FlexrayCommunicationController.setClusterDriftDamping, Optional[Integer], FlexrayCommunicationController)

    def test_cluster_drift_damping_docstrings_are_spec_note(self):
        self._assert_docstring(FlexrayCommunicationController.getClusterDriftDamping, CLUSTER_DRIFT_DAMPING_NOTE)
        self._assert_docstring(FlexrayCommunicationController.setClusterDriftDamping, CLUSTER_DRIFT_DAMPING_NOTE, "clusterDriftDamping")

    def test_get_set_decoding_correction(self):
        controller = self._make()
        value = Integer().setValue("5")
        assert controller == controller.setDecodingCorrection(value)
        assert controller.getDecodingCorrection() == value
        assert controller == controller.setDecodingCorrection(None)
        assert controller.getDecodingCorrection() == value
        self._pin(FlexrayCommunicationController.getDecodingCorrection, FlexrayCommunicationController.setDecodingCorrection, Optional[Integer], FlexrayCommunicationController)

    def test_decoding_correction_docstrings_are_spec_note(self):
        self._assert_docstring(FlexrayCommunicationController.getDecodingCorrection, DECODING_CORRECTION_NOTE)
        self._assert_docstring(FlexrayCommunicationController.setDecodingCorrection, DECODING_CORRECTION_NOTE, "decodingCorrection")

    def test_get_set_delay_compensation_a(self):
        controller = self._make()
        value = Integer().setValue("6")
        assert controller == controller.setDelayCompensationA(value)
        assert controller.getDelayCompensationA() == value
        assert controller == controller.setDelayCompensationA(None)
        assert controller.getDelayCompensationA() == value
        self._pin(FlexrayCommunicationController.getDelayCompensationA, FlexrayCommunicationController.setDelayCompensationA, Optional[Integer], FlexrayCommunicationController)

    def test_delay_compensation_a_docstrings_are_spec_note(self):
        self._assert_docstring(FlexrayCommunicationController.getDelayCompensationA, DELAY_COMPENSATION_A_NOTE)
        self._assert_docstring(FlexrayCommunicationController.setDelayCompensationA, DELAY_COMPENSATION_A_NOTE, "delayCompensationA")

    def test_get_set_delay_compensation_b(self):
        controller = self._make()
        value = Integer().setValue("7")
        assert controller == controller.setDelayCompensationB(value)
        assert controller.getDelayCompensationB() == value
        assert controller == controller.setDelayCompensationB(None)
        assert controller.getDelayCompensationB() == value
        self._pin(FlexrayCommunicationController.getDelayCompensationB, FlexrayCommunicationController.setDelayCompensationB, Optional[Integer], FlexrayCommunicationController)

    def test_delay_compensation_b_docstrings_are_spec_note(self):
        self._assert_docstring(FlexrayCommunicationController.getDelayCompensationB, DELAY_COMPENSATION_B_NOTE)
        self._assert_docstring(FlexrayCommunicationController.setDelayCompensationB, DELAY_COMPENSATION_B_NOTE, "delayCompensationB")

    def test_get_set_external_sync(self):
        controller = self._make()
        value = Boolean().setValue(True)
        assert controller == controller.setExternalSync(value)
        assert controller.getExternalSync() == value
        assert controller == controller.setExternalSync(None)
        assert controller.getExternalSync() == value
        self._pin(FlexrayCommunicationController.getExternalSync, FlexrayCommunicationController.setExternalSync, Optional[Boolean], FlexrayCommunicationController)

    def test_external_sync_docstrings_are_spec_note(self):
        self._assert_docstring(FlexrayCommunicationController.getExternalSync, EXTERNAL_SYNC_NOTE)
        self._assert_docstring(FlexrayCommunicationController.setExternalSync, EXTERNAL_SYNC_NOTE, "externalSync")

    def test_get_set_extern_offset_correction(self):
        controller = self._make()
        value = Integer().setValue("8")
        assert controller == controller.setExternOffsetCorrection(value)
        assert controller.getExternOffsetCorrection() == value
        assert controller == controller.setExternOffsetCorrection(None)
        assert controller.getExternOffsetCorrection() == value
        self._pin(FlexrayCommunicationController.getExternOffsetCorrection, FlexrayCommunicationController.setExternOffsetCorrection, Optional[Integer], FlexrayCommunicationController)

    def test_extern_offset_correction_docstrings_are_spec_note(self):
        self._assert_docstring(FlexrayCommunicationController.getExternOffsetCorrection, EXTERN_OFFSET_CORRECTION_NOTE)
        self._assert_docstring(FlexrayCommunicationController.setExternOffsetCorrection, EXTERN_OFFSET_CORRECTION_NOTE, "externOffsetCorrection")

    def test_get_set_extern_rate_correction(self):
        controller = self._make()
        value = Integer().setValue("9")
        assert controller == controller.setExternRateCorrection(value)
        assert controller.getExternRateCorrection() == value
        assert controller == controller.setExternRateCorrection(None)
        assert controller.getExternRateCorrection() == value
        self._pin(FlexrayCommunicationController.getExternRateCorrection, FlexrayCommunicationController.setExternRateCorrection, Optional[Integer], FlexrayCommunicationController)

    def test_extern_rate_correction_docstrings_are_spec_note(self):
        self._assert_docstring(FlexrayCommunicationController.getExternRateCorrection, EXTERN_RATE_CORRECTION_NOTE)
        self._assert_docstring(FlexrayCommunicationController.setExternRateCorrection, EXTERN_RATE_CORRECTION_NOTE, "externRateCorrection")

    def test_get_set_fall_back_internal(self):
        controller = self._make()
        value = Boolean().setValue(True)
        assert controller == controller.setFallBackInternal(value)
        assert controller.getFallBackInternal() == value
        assert controller == controller.setFallBackInternal(None)
        assert controller.getFallBackInternal() == value
        self._pin(FlexrayCommunicationController.getFallBackInternal, FlexrayCommunicationController.setFallBackInternal, Optional[Boolean], FlexrayCommunicationController)

    def test_fall_back_internal_docstrings_are_spec_note(self):
        self._assert_docstring(FlexrayCommunicationController.getFallBackInternal, FALL_BACK_INTERNAL_NOTE)
        self._assert_docstring(FlexrayCommunicationController.setFallBackInternal, FALL_BACK_INTERNAL_NOTE, "fallBackInternal")

    def test_add_flexray_fifo(self):
        controller = self._make()
        assert controller.getFlexrayFifos() == []

        fifo = FlexrayFifoConfiguration()
        assert controller == controller.addFlexrayFifo(fifo)
        assert controller.getFlexrayFifos() == [fifo]

        fifo2 = FlexrayFifoConfiguration()
        controller.addFlexrayFifo(fifo2)
        assert controller.getFlexrayFifos() == [fifo, fifo2]

        controller.addFlexrayFifo(None)
        assert controller.getFlexrayFifos() == [fifo, fifo2]

        add_hints = get_type_hints(FlexrayCommunicationController.addFlexrayFifo)
        assert add_hints.get("value") == Optional[FlexrayFifoConfiguration]
        assert add_hints.get("return") is FlexrayCommunicationController

        getter_hints = get_type_hints(FlexrayCommunicationController.getFlexrayFifos)
        assert getter_hints.get("return") == List[FlexrayFifoConfiguration]

    def test_flexray_fifo_docstrings_are_spec_note(self):
        add_expected = FLEXRAY_FIFO_NOTE + "\nA None value is a no-op and does not extend the flexrayFifos."
        assert inspect.cleandoc(FlexrayCommunicationController.addFlexrayFifo.__doc__).strip() == add_expected
        self._assert_docstring(FlexrayCommunicationController.getFlexrayFifos, FLEXRAY_FIFO_NOTE)

    def test_get_set_key_slot_id(self):
        controller = self._make()
        value = PositiveInteger().setValue("2")
        assert controller == controller.setKeySlotID(value)
        assert controller.getKeySlotID() == value
        assert controller == controller.setKeySlotID(None)
        assert controller.getKeySlotID() == value
        self._pin(FlexrayCommunicationController.getKeySlotID, FlexrayCommunicationController.setKeySlotID, Optional[PositiveInteger], FlexrayCommunicationController)

    def test_key_slot_id_docstrings_are_spec_note(self):
        self._assert_docstring(FlexrayCommunicationController.getKeySlotID, KEY_SLOT_ID_NOTE)
        self._assert_docstring(FlexrayCommunicationController.setKeySlotID, KEY_SLOT_ID_NOTE, "keySlotID")

    def test_get_set_key_slot_only_enabled(self):
        controller = self._make()
        value = Boolean().setValue(True)
        assert controller == controller.setKeySlotOnlyEnabled(value)
        assert controller.getKeySlotOnlyEnabled() == value
        assert controller == controller.setKeySlotOnlyEnabled(None)
        assert controller.getKeySlotOnlyEnabled() == value
        self._pin(FlexrayCommunicationController.getKeySlotOnlyEnabled, FlexrayCommunicationController.setKeySlotOnlyEnabled, Optional[Boolean], FlexrayCommunicationController)

    def test_key_slot_only_enabled_docstrings_are_spec_note(self):
        self._assert_docstring(FlexrayCommunicationController.getKeySlotOnlyEnabled, KEY_SLOT_ONLY_ENABLED_NOTE)
        self._assert_docstring(FlexrayCommunicationController.setKeySlotOnlyEnabled, KEY_SLOT_ONLY_ENABLED_NOTE, "keySlotOnlyEnabled")

    def test_get_set_key_slot_used_for_start_up(self):
        controller = self._make()
        value = Boolean().setValue(True)
        assert controller == controller.setKeySlotUsedForStartUp(value)
        assert controller.getKeySlotUsedForStartUp() == value
        assert controller == controller.setKeySlotUsedForStartUp(None)
        assert controller.getKeySlotUsedForStartUp() == value
        self._pin(FlexrayCommunicationController.getKeySlotUsedForStartUp, FlexrayCommunicationController.setKeySlotUsedForStartUp, Optional[Boolean], FlexrayCommunicationController)

    def test_key_slot_used_for_start_up_docstrings_are_spec_note(self):
        self._assert_docstring(FlexrayCommunicationController.getKeySlotUsedForStartUp, KEY_SLOT_USED_FOR_START_UP_NOTE)
        self._assert_docstring(FlexrayCommunicationController.setKeySlotUsedForStartUp, KEY_SLOT_USED_FOR_START_UP_NOTE, "keySlotUsedForStartUp")

    def test_get_set_key_slot_used_for_sync(self):
        controller = self._make()
        value = Boolean().setValue(True)
        assert controller == controller.setKeySlotUsedForSync(value)
        assert controller.getKeySlotUsedForSync() == value
        assert controller == controller.setKeySlotUsedForSync(None)
        assert controller.getKeySlotUsedForSync() == value
        self._pin(FlexrayCommunicationController.getKeySlotUsedForSync, FlexrayCommunicationController.setKeySlotUsedForSync, Optional[Boolean], FlexrayCommunicationController)

    def test_key_slot_used_for_sync_docstrings_are_spec_note(self):
        self._assert_docstring(FlexrayCommunicationController.getKeySlotUsedForSync, KEY_SLOT_USED_FOR_SYNC_NOTE)
        self._assert_docstring(FlexrayCommunicationController.setKeySlotUsedForSync, KEY_SLOT_USED_FOR_SYNC_NOTE, "keySlotUsedForSync")

    def test_get_set_latest_tx(self):
        controller = self._make()
        value = Integer().setValue("10")
        assert controller == controller.setLatestTX(value)
        assert controller.getLatestTX() == value
        assert controller == controller.setLatestTX(None)
        assert controller.getLatestTX() == value
        self._pin(FlexrayCommunicationController.getLatestTX, FlexrayCommunicationController.setLatestTX, Optional[Integer], FlexrayCommunicationController)

    def test_latest_tx_docstrings_are_spec_note(self):
        self._assert_docstring(FlexrayCommunicationController.getLatestTX, LATEST_TX_NOTE)
        self._assert_docstring(FlexrayCommunicationController.setLatestTX, LATEST_TX_NOTE, "latestTX")

    def test_get_set_listen_timeout(self):
        controller = self._make()
        value = Integer().setValue("11")
        assert controller == controller.setListenTimeout(value)
        assert controller.getListenTimeout() == value
        assert controller == controller.setListenTimeout(None)
        assert controller.getListenTimeout() == value
        self._pin(FlexrayCommunicationController.getListenTimeout, FlexrayCommunicationController.setListenTimeout, Optional[Integer], FlexrayCommunicationController)

    def test_listen_timeout_docstrings_are_spec_note(self):
        self._assert_docstring(FlexrayCommunicationController.getListenTimeout, LISTEN_TIMEOUT_NOTE)
        self._assert_docstring(FlexrayCommunicationController.setListenTimeout, LISTEN_TIMEOUT_NOTE, "listenTimeout")

    def test_get_set_macro_initial_offset_a(self):
        controller = self._make()
        value = Integer().setValue("12")
        assert controller == controller.setMacroInitialOffsetA(value)
        assert controller.getMacroInitialOffsetA() == value
        assert controller == controller.setMacroInitialOffsetA(None)
        assert controller.getMacroInitialOffsetA() == value
        self._pin(FlexrayCommunicationController.getMacroInitialOffsetA, FlexrayCommunicationController.setMacroInitialOffsetA, Optional[Integer], FlexrayCommunicationController)

    def test_macro_initial_offset_a_docstrings_are_spec_note(self):
        self._assert_docstring(FlexrayCommunicationController.getMacroInitialOffsetA, MACRO_INITIAL_OFFSET_A_NOTE)
        self._assert_docstring(FlexrayCommunicationController.setMacroInitialOffsetA, MACRO_INITIAL_OFFSET_A_NOTE, "macroInitialOffsetA")

    def test_get_set_macro_initial_offset_b(self):
        controller = self._make()
        value = Integer().setValue("13")
        assert controller == controller.setMacroInitialOffsetB(value)
        assert controller.getMacroInitialOffsetB() == value
        assert controller == controller.setMacroInitialOffsetB(None)
        assert controller.getMacroInitialOffsetB() == value
        self._pin(FlexrayCommunicationController.getMacroInitialOffsetB, FlexrayCommunicationController.setMacroInitialOffsetB, Optional[Integer], FlexrayCommunicationController)

    def test_macro_initial_offset_b_docstrings_are_spec_note(self):
        self._assert_docstring(FlexrayCommunicationController.getMacroInitialOffsetB, MACRO_INITIAL_OFFSET_B_NOTE)
        self._assert_docstring(FlexrayCommunicationController.setMacroInitialOffsetB, MACRO_INITIAL_OFFSET_B_NOTE, "macroInitialOffsetB")

    def test_get_set_maximum_dynamic_payload_length(self):
        controller = self._make()
        value = Integer().setValue("14")
        assert controller == controller.setMaximumDynamicPayloadLength(value)
        assert controller.getMaximumDynamicPayloadLength() == value
        assert controller == controller.setMaximumDynamicPayloadLength(None)
        assert controller.getMaximumDynamicPayloadLength() == value
        self._pin(FlexrayCommunicationController.getMaximumDynamicPayloadLength, FlexrayCommunicationController.setMaximumDynamicPayloadLength, Optional[Integer], FlexrayCommunicationController)

    def test_maximum_dynamic_payload_length_docstrings_are_spec_note(self):
        self._assert_docstring(FlexrayCommunicationController.getMaximumDynamicPayloadLength, MAXIMUM_DYNAMIC_PAYLOAD_LENGTH_NOTE)
        self._assert_docstring(FlexrayCommunicationController.setMaximumDynamicPayloadLength, MAXIMUM_DYNAMIC_PAYLOAD_LENGTH_NOTE, "maximumDynamicPayloadLength")

    def test_get_set_micro_initial_offset_a(self):
        controller = self._make()
        value = Integer().setValue("15")
        assert controller == controller.setMicroInitialOffsetA(value)
        assert controller.getMicroInitialOffsetA() == value
        assert controller == controller.setMicroInitialOffsetA(None)
        assert controller.getMicroInitialOffsetA() == value
        self._pin(FlexrayCommunicationController.getMicroInitialOffsetA, FlexrayCommunicationController.setMicroInitialOffsetA, Optional[Integer], FlexrayCommunicationController)

    def test_micro_initial_offset_a_docstrings_are_spec_note(self):
        self._assert_docstring(FlexrayCommunicationController.getMicroInitialOffsetA, MICRO_INITIAL_OFFSET_A_NOTE)
        self._assert_docstring(FlexrayCommunicationController.setMicroInitialOffsetA, MICRO_INITIAL_OFFSET_A_NOTE, "microInitialOffsetA")

    def test_get_set_micro_initial_offset_b(self):
        controller = self._make()
        value = Integer().setValue("16")
        assert controller == controller.setMicroInitialOffsetB(value)
        assert controller.getMicroInitialOffsetB() == value
        assert controller == controller.setMicroInitialOffsetB(None)
        assert controller.getMicroInitialOffsetB() == value
        self._pin(FlexrayCommunicationController.getMicroInitialOffsetB, FlexrayCommunicationController.setMicroInitialOffsetB, Optional[Integer], FlexrayCommunicationController)

    def test_micro_initial_offset_b_docstrings_are_spec_note(self):
        self._assert_docstring(FlexrayCommunicationController.getMicroInitialOffsetB, MICRO_INITIAL_OFFSET_B_NOTE)
        self._assert_docstring(FlexrayCommunicationController.setMicroInitialOffsetB, MICRO_INITIAL_OFFSET_B_NOTE, "microInitialOffsetB")

    def test_get_set_micro_per_cycle(self):
        controller = self._make()
        value = Integer().setValue("17")
        assert controller == controller.setMicroPerCycle(value)
        assert controller.getMicroPerCycle() == value
        assert controller == controller.setMicroPerCycle(None)
        assert controller.getMicroPerCycle() == value
        self._pin(FlexrayCommunicationController.getMicroPerCycle, FlexrayCommunicationController.setMicroPerCycle, Optional[Integer], FlexrayCommunicationController)

    def test_micro_per_cycle_docstrings_are_spec_note(self):
        self._assert_docstring(FlexrayCommunicationController.getMicroPerCycle, MICRO_PER_CYCLE_NOTE)
        self._assert_docstring(FlexrayCommunicationController.setMicroPerCycle, MICRO_PER_CYCLE_NOTE, "microPerCycle")

    def test_get_set_microtick_duration(self):
        controller = self._make()
        value = TimeValue().setValue("0.05")
        assert controller == controller.setMicrotickDuration(value)
        assert controller.getMicrotickDuration() == value
        assert controller == controller.setMicrotickDuration(None)
        assert controller.getMicrotickDuration() == value
        self._pin(FlexrayCommunicationController.getMicrotickDuration, FlexrayCommunicationController.setMicrotickDuration, Optional[TimeValue], FlexrayCommunicationController)

    def test_microtick_duration_docstrings_are_spec_note(self):
        self._assert_docstring(FlexrayCommunicationController.getMicrotickDuration, MICROTICK_DURATION_NOTE)
        self._assert_docstring(FlexrayCommunicationController.setMicrotickDuration, MICROTICK_DURATION_NOTE, "microtickDuration")

    def test_get_set_nm_vector_early_update(self):
        controller = self._make()
        value = Boolean().setValue(True)
        assert controller == controller.setNmVectorEarlyUpdate(value)
        assert controller.getNmVectorEarlyUpdate() == value
        assert controller == controller.setNmVectorEarlyUpdate(None)
        assert controller.getNmVectorEarlyUpdate() == value
        self._pin(FlexrayCommunicationController.getNmVectorEarlyUpdate, FlexrayCommunicationController.setNmVectorEarlyUpdate, Optional[Boolean], FlexrayCommunicationController)

    def test_nm_vector_early_update_docstrings_are_spec_note(self):
        self._assert_docstring(FlexrayCommunicationController.getNmVectorEarlyUpdate, NM_VECTOR_EARLY_UPDATE_NOTE)
        self._assert_docstring(FlexrayCommunicationController.setNmVectorEarlyUpdate, NM_VECTOR_EARLY_UPDATE_NOTE, "nmVectorEarlyUpdate")

    def test_get_set_offset_correction_out(self):
        controller = self._make()
        value = Integer().setValue("18")
        assert controller == controller.setOffsetCorrectionOut(value)
        assert controller.getOffsetCorrectionOut() == value
        assert controller == controller.setOffsetCorrectionOut(None)
        assert controller.getOffsetCorrectionOut() == value
        self._pin(FlexrayCommunicationController.getOffsetCorrectionOut, FlexrayCommunicationController.setOffsetCorrectionOut, Optional[Integer], FlexrayCommunicationController)

    def test_offset_correction_out_docstrings_are_spec_note(self):
        self._assert_docstring(FlexrayCommunicationController.getOffsetCorrectionOut, OFFSET_CORRECTION_OUT_NOTE)
        self._assert_docstring(FlexrayCommunicationController.setOffsetCorrectionOut, OFFSET_CORRECTION_OUT_NOTE, "offsetCorrectionOut")

    def test_get_set_rate_correction_out(self):
        controller = self._make()
        value = Integer().setValue("19")
        assert controller == controller.setRateCorrectionOut(value)
        assert controller.getRateCorrectionOut() == value
        assert controller == controller.setRateCorrectionOut(None)
        assert controller.getRateCorrectionOut() == value
        self._pin(FlexrayCommunicationController.getRateCorrectionOut, FlexrayCommunicationController.setRateCorrectionOut, Optional[Integer], FlexrayCommunicationController)

    def test_rate_correction_out_docstrings_are_spec_note(self):
        self._assert_docstring(FlexrayCommunicationController.getRateCorrectionOut, RATE_CORRECTION_OUT_NOTE)
        self._assert_docstring(FlexrayCommunicationController.setRateCorrectionOut, RATE_CORRECTION_OUT_NOTE, "rateCorrectionOut")

    def test_get_set_samples_per_microtick(self):
        controller = self._make()
        value = Integer().setValue("20")
        assert controller == controller.setSamplesPerMicrotick(value)
        assert controller.getSamplesPerMicrotick() == value
        assert controller == controller.setSamplesPerMicrotick(None)
        assert controller.getSamplesPerMicrotick() == value
        self._pin(FlexrayCommunicationController.getSamplesPerMicrotick, FlexrayCommunicationController.setSamplesPerMicrotick, Optional[Integer], FlexrayCommunicationController)

    def test_samples_per_microtick_docstrings_are_spec_note(self):
        self._assert_docstring(FlexrayCommunicationController.getSamplesPerMicrotick, SAMPLES_PER_MICROTICK_NOTE)
        self._assert_docstring(FlexrayCommunicationController.setSamplesPerMicrotick, SAMPLES_PER_MICROTICK_NOTE, "samplesPerMicrotick")

    def test_get_set_second_key_slot_id(self):
        controller = self._make()
        value = PositiveInteger().setValue("21")
        assert controller == controller.setSecondKeySlotId(value)
        assert controller.getSecondKeySlotId() == value
        assert controller == controller.setSecondKeySlotId(None)
        assert controller.getSecondKeySlotId() == value
        self._pin(FlexrayCommunicationController.getSecondKeySlotId, FlexrayCommunicationController.setSecondKeySlotId, Optional[PositiveInteger], FlexrayCommunicationController)

    def test_second_key_slot_id_docstrings_are_spec_note(self):
        self._assert_docstring(FlexrayCommunicationController.getSecondKeySlotId, SECOND_KEY_SLOT_ID_NOTE)
        self._assert_docstring(FlexrayCommunicationController.setSecondKeySlotId, SECOND_KEY_SLOT_ID_NOTE, "secondKeySlotId")

    def test_get_set_two_key_slot_mode(self):
        controller = self._make()
        value = Boolean().setValue(True)
        assert controller == controller.setTwoKeySlotMode(value)
        assert controller.getTwoKeySlotMode() == value
        assert controller == controller.setTwoKeySlotMode(None)
        assert controller.getTwoKeySlotMode() == value
        self._pin(FlexrayCommunicationController.getTwoKeySlotMode, FlexrayCommunicationController.setTwoKeySlotMode, Optional[Boolean], FlexrayCommunicationController)

    def test_two_key_slot_mode_docstrings_are_spec_note(self):
        self._assert_docstring(FlexrayCommunicationController.getTwoKeySlotMode, TWO_KEY_SLOT_MODE_NOTE)
        self._assert_docstring(FlexrayCommunicationController.setTwoKeySlotMode, TWO_KEY_SLOT_MODE_NOTE, "twoKeySlotMode")

    def test_get_set_wake_up_pattern(self):
        controller = self._make()
        value = Integer().setValue("22")
        assert controller == controller.setWakeUpPattern(value)
        assert controller.getWakeUpPattern() == value
        assert controller == controller.setWakeUpPattern(None)
        assert controller.getWakeUpPattern() == value
        self._pin(FlexrayCommunicationController.getWakeUpPattern, FlexrayCommunicationController.setWakeUpPattern, Optional[Integer], FlexrayCommunicationController)

    def test_wake_up_pattern_docstrings_are_spec_note(self):
        self._assert_docstring(FlexrayCommunicationController.getWakeUpPattern, WAKE_UP_PATTERN_NOTE)
        self._assert_docstring(FlexrayCommunicationController.setWakeUpPattern, WAKE_UP_PATTERN_NOTE, "wakeUpPattern")


FLEXRAY_PHYSICAL_CHANNEL_CLASS_NOTE = (
    "FlexRay specific attributes to the physicalChannel\n"
    "\n"
    "[constr_3018] Number of FlexRay channels: A FlexrayCluster shall use either one FlexrayPhysicalChannel with channelName set to either channelA or channelB or else two FlexrayPhysicalChannels with one channelName channelA and one channelName channelB.\n"
    "\n"
    "[constr_5448] Existence of channelName: For each FlexrayPhysicalChannel, the attribute channelName shall exist at the time when the System Description is complete."
)
CHANNEL_NAME_NOTE = "Name of the channel (Channel A or Channel B)."


class TestFlexrayPhysicalChannel:
    def _make(self) -> FlexrayPhysicalChannel:
        return FlexrayPhysicalChannel(MockParent(), "test_flexray_physical_channel")

    def _assert_docstring(self, method, note, attr_name=None):
        expected = note if attr_name is None else note + "\nA None value is a no-op and does not overwrite an existing %s." % attr_name
        assert method.__doc__ is not None
        assert inspect.cleandoc(method.__doc__).strip() == expected

    def test_initialization(self):
        channel = self._make()

        assert channel.getShortName() == "test_flexray_physical_channel"
        assert isinstance(channel, PhysicalChannel)
        assert channel.getChannelName() is None

    def test_class_docstring_is_spec_note(self):
        assert inspect.cleandoc(FlexrayPhysicalChannel.__doc__).strip() == FLEXRAY_PHYSICAL_CHANNEL_CLASS_NOTE

    def test_init_has_no_docstring(self):
        assert FlexrayPhysicalChannel.__init__.__doc__ is None

    def test_member_order_matches_spec(self):
        source = inspect.getsource(FlexrayPhysicalChannel.__init__)
        assert "self.channelName: Optional[FlexrayChannelName] = None" in source

    def test_get_set_channel_name(self):
        channel = self._make()

        assert channel.getChannelName() is None

        value = FlexrayChannelName().setValue(FlexrayChannelName.CHANNEL_A)
        assert channel == channel.setChannelName(value)
        assert channel.getChannelName() == value
        assert channel.getChannelName().getValue() == "channelA"

        assert channel == channel.setChannelName(None)
        assert channel.getChannelName() == value

        getter_hints = get_type_hints(FlexrayPhysicalChannel.getChannelName)
        assert getter_hints.get("return") == Optional[FlexrayChannelName]

        setter_hints = get_type_hints(FlexrayPhysicalChannel.setChannelName)
        assert setter_hints.get("value") == Optional[FlexrayChannelName]
        assert setter_hints.get("return") is FlexrayPhysicalChannel

    def test_channel_name_docstrings_are_spec_note(self):
        self._assert_docstring(FlexrayPhysicalChannel.getChannelName, CHANNEL_NAME_NOTE)
        self._assert_docstring(FlexrayPhysicalChannel.setChannelName, CHANNEL_NAME_NOTE, "channelName")
