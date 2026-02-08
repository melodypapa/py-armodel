from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology import (
    FlexrayCluster,
    FlexrayCommunicationConnector,
    FlexrayCommunicationController,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import (
    CommunicationCluster,
    CommunicationConnector,
    CommunicationController,
)


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

    def test_flexray_communication_controller(self):
        """
        Test the FlexrayCommunicationController class initialization and methods with method chaining and None handling.
        """
        parent = MockParent()
        controller = FlexrayCommunicationController(parent, "TestController")

        assert controller.getShortName() == "TestController"
        assert isinstance(controller, CommunicationController)
        assert controller.getAcceptedStartupRange() is None
        assert controller.getAllowHaltDueToClock() is None
        assert controller.getAllowPassiveToActive() is None
        assert controller.getClusterDriftDamping() is None
        assert controller.getDecodingCorrection() is None
        assert controller.getDelayCompensationA() is None
        assert controller.getDelayCompensationB() is None
        assert controller.getExternOffsetCorrection() is None
        assert controller.getExternRateCorrection() is None
        assert controller.getExternalSync() is None
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

        # Test setter/getter methods with method chaining - with None values
        assert controller == controller.setAcceptedStartupRange(None)
        assert controller.getAcceptedStartupRange() is None

        assert controller == controller.setAllowHaltDueToClock(None)
        assert controller.getAllowHaltDueToClock() is None

        assert controller == controller.setAllowPassiveToActive(None)
        assert controller.getAllowPassiveToActive() is None

        assert controller == controller.setClusterDriftDamping(None)
        assert controller.getClusterDriftDamping() is None

        assert controller == controller.setDecodingCorrection(None)
        assert controller.getDecodingCorrection() is None

        assert controller == controller.setDelayCompensationA(None)
        assert controller.getDelayCompensationA() is None

        assert controller == controller.setDelayCompensationB(None)
        assert controller.getDelayCompensationB() is None

        assert controller == controller.setExternOffsetCorrection(None)
        assert controller.getExternOffsetCorrection() is None

        assert controller == controller.setExternRateCorrection(None)
        assert controller.getExternRateCorrection() is None

        assert controller == controller.setExternalSync(None)
        assert controller.getExternalSync() is None

        assert controller == controller.setFallBackInternal(None)
        assert controller.getFallBackInternal() is None

        assert controller == controller.setFlexrayFifos(None)
        assert controller.getFlexrayFifos() == []  # Should remain empty list when None is passed to setter that expects a value to set

        assert controller == controller.setKeySlotID(None)
        assert controller.getKeySlotID() is None

        assert controller == controller.setKeySlotOnlyEnabled(None)
        assert controller.getKeySlotOnlyEnabled() is None

        assert controller == controller.setKeySlotUsedForStartUp(None)
        assert controller.getKeySlotUsedForStartUp() is None

        assert controller == controller.setKeySlotUsedForSync(None)
        assert controller.getKeySlotUsedForSync() is None

        assert controller == controller.setLatestTX(None)
        assert controller.getLatestTX() is None

        assert controller == controller.setListenTimeout(None)
        assert controller.getListenTimeout() is None

        assert controller == controller.setMacroInitialOffsetA(None)
        assert controller.getMacroInitialOffsetA() is None

        assert controller == controller.setMacroInitialOffsetB(None)
        assert controller.getMacroInitialOffsetB() is None

        assert controller == controller.setMaximumDynamicPayloadLength(None)
        assert controller.getMaximumDynamicPayloadLength() is None

        assert controller == controller.setMicroInitialOffsetA(None)
        assert controller.getMicroInitialOffsetA() is None

        assert controller == controller.setMicroInitialOffsetB(None)
        assert controller.getMicroInitialOffsetB() is None

        assert controller == controller.setMicroPerCycle(None)
        assert controller.getMicroPerCycle() is None

        assert controller == controller.setMicrotickDuration(None)
        assert controller.getMicrotickDuration() is None

        assert controller == controller.setNmVectorEarlyUpdate(None)
        assert controller.getNmVectorEarlyUpdate() is None

        assert controller == controller.setOffsetCorrectionOut(None)
        assert controller.getOffsetCorrectionOut() is None

        assert controller == controller.setRateCorrectionOut(None)
        assert controller.getRateCorrectionOut() is None

        assert controller == controller.setSamplesPerMicrotick(None)
        assert controller.getSamplesPerMicrotick() is None

        assert controller == controller.setSecondKeySlotId(None)
        assert controller.getSecondKeySlotId() is None

        assert controller == controller.setTwoKeySlotMode(None)
        assert controller.getTwoKeySlotMode() is None

        assert controller == controller.setWakeUpPattern(None)
        assert controller.getWakeUpPattern() is None

        # Test setter/getter methods with method chaining - with actual values
        controller.setAcceptedStartupRange(5)
        assert controller.getAcceptedStartupRange() == 5
        assert controller == controller.setAcceptedStartupRange(5)

        controller.setAllowHaltDueToClock(True)
        assert controller.getAllowHaltDueToClock() is True
        assert controller == controller.setAllowHaltDueToClock(True)

        controller.setKeySlotID(2)
        assert controller.getKeySlotID() == 2
        assert controller == controller.setKeySlotID(2)

        controller.setKeySlotOnlyEnabled(False)
        assert controller.getKeySlotOnlyEnabled() is False
        assert controller == controller.setKeySlotOnlyEnabled(False)

        controller.setFlexrayFifos(["fifo1", "fifo2"])
        assert "fifo1" in controller.getFlexrayFifos()
        assert controller == controller.setFlexrayFifos(["fifo1", "fifo2"])

        # Test all other setter methods with actual values to ensure 100% coverage
        controller.setAllowPassiveToActive(3)
        assert controller.getAllowPassiveToActive() == 3

        controller.setClusterDriftDamping(4)
        assert controller.getClusterDriftDamping() == 4

        controller.setDecodingCorrection(5)
        assert controller.getDecodingCorrection() == 5

        controller.setDelayCompensationA(6)
        assert controller.getDelayCompensationA() == 6

        controller.setDelayCompensationB(7)
        assert controller.getDelayCompensationB() == 7

        controller.setExternOffsetCorrection(8)
        assert controller.getExternOffsetCorrection() == 8

        controller.setExternRateCorrection(9)
        assert controller.getExternRateCorrection() == 9

        controller.setExternalSync(True)
        assert controller.getExternalSync() is True

        controller.setFallBackInternal(True)
        assert controller.getFallBackInternal() is True

        controller.setKeySlotUsedForStartUp(True)
        assert controller.getKeySlotUsedForStartUp() is True

        controller.setKeySlotUsedForSync(True)
        assert controller.getKeySlotUsedForSync() is True

        controller.setLatestTX(10)
        assert controller.getLatestTX() == 10

        controller.setListenTimeout(11)
        assert controller.getListenTimeout() == 11

        controller.setMacroInitialOffsetA(12)
        assert controller.getMacroInitialOffsetA() == 12

        controller.setMacroInitialOffsetB(13)
        assert controller.getMacroInitialOffsetB() == 13

        controller.setMaximumDynamicPayloadLength(14)
        assert controller.getMaximumDynamicPayloadLength() == 14

        controller.setMicroInitialOffsetA(15)
        assert controller.getMicroInitialOffsetA() == 15

        controller.setMicroInitialOffsetB(16)
        assert controller.getMicroInitialOffsetB() == 16

        controller.setMicroPerCycle(17)
        assert controller.getMicroPerCycle() == 17

        controller.setNmVectorEarlyUpdate(True)
        assert controller.getNmVectorEarlyUpdate() is True

        controller.setOffsetCorrectionOut(18)
        assert controller.getOffsetCorrectionOut() == 18

        controller.setRateCorrectionOut(19)
        assert controller.getRateCorrectionOut() == 19

        controller.setSamplesPerMicrotick(20)
        assert controller.getSamplesPerMicrotick() == 20

        controller.setSecondKeySlotId(21)
        assert controller.getSecondKeySlotId() == 21

        controller.setTwoKeySlotMode(True)
        assert controller.getTwoKeySlotMode() is True

        controller.setWakeUpPattern(22)
        assert controller.getWakeUpPattern() == 22

        controller.setMicrotickDuration(100.0)
        assert controller.getMicrotickDuration() == 100.0

    def test_flexray_communication_connector(self):
        """
        Test the FlexrayCommunicationConnector class initialization and methods with method chaining and None handling.
        """
        parent = MockParent()
        connector = FlexrayCommunicationConnector(parent, "TestConnector")

        assert connector.getShortName() == "TestConnector"
        assert isinstance(connector, CommunicationConnector)
        assert connector.getNmReadySleepTime() is None
        assert connector.getPncFilterDataMask() is None
        assert connector.getWakeUpChannel() is None

        # Test setter/getter methods with method chaining - with None values
        assert connector == connector.setNmReadySleepTime(None)
        assert connector.getNmReadySleepTime() is None

        assert connector == connector.setPncFilterDataMask(None)
        assert connector.getPncFilterDataMask() is None

        assert connector == connector.setWakeUpChannel(None)
        assert connector.getWakeUpChannel() is None

        # Test setter/getter methods with method chaining - with actual values
        connector.setNmReadySleepTime(10.5)
        assert connector.getNmReadySleepTime() == 10.5
        assert connector == connector.setNmReadySleepTime(10.5)

        connector.setPncFilterDataMask(255)
        assert connector.getPncFilterDataMask() == 255
        assert connector == connector.setPncFilterDataMask(255)

        connector.setWakeUpChannel(True)
        assert connector.getWakeUpChannel() is True
        assert connector == connector.setWakeUpChannel(True)

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
