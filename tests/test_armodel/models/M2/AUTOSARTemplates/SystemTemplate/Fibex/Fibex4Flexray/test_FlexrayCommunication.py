import pytest

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayCommunication import (
    FlexrayFrame,
    FlexrayAbsolutelyScheduledTiming,
    FlexrayFrameTriggering
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import Frame, FrameTriggering
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class Test_Fibex4FlexrayCommunication:
    """Test cases for Fibex4Flexray Communication classes."""
    
    def test_FlexrayFrame(self):
        """Test FlexrayFrame class functionality."""
        parent = MockParent()
        frame = FlexrayFrame(parent, "test_flexray_frame")

        assert isinstance(frame, Frame)

    def test_FlexrayAbsolutelyScheduledTiming(self):
        """Test FlexrayAbsolutelyScheduledTiming class functionality."""
        timing = FlexrayAbsolutelyScheduledTiming()

        assert isinstance(timing, ARObject)
        
        # Test default values
        assert timing.getCommunicationCycle() is None
        assert timing.getSlotID() is None
        
        # Test setter/getter methods
        timing.setCommunicationCycle("cycle1")
        assert timing.getCommunicationCycle() == "cycle1"
        
        timing.setSlotID(10)
        assert timing.getSlotID() == 10

    def test_FlexrayAbsolutelyScheduledTiming_none_handling(self):
        """Test FlexrayAbsolutelyScheduledTiming None value handling to achieve 100% coverage."""
        timing = FlexrayAbsolutelyScheduledTiming()

        # Test setting None keeps original value (which is None) - tests if value is not None logic
        result = timing.setCommunicationCycle(None)
        assert result == timing
        assert timing.getCommunicationCycle() is None

        result = timing.setSlotID(None)
        assert result == timing
        assert timing.getSlotID() is None

        # Test setting actual values then setting back to None (should not change value)
        timing.setCommunicationCycle("test_cycle")
        assert timing.getCommunicationCycle() == "test_cycle"
        result = timing.setCommunicationCycle(None)
        assert result == timing
        # Value should remain unchanged since None was passed
        assert timing.getCommunicationCycle() == "test_cycle"


        timing.setSlotID(42)
        assert timing.getSlotID() == 42
        result = timing.setSlotID(None)
        assert result == timing
        # Value should remain unchanged since None was passed
        assert timing.getSlotID() == 42

    def test_FlexrayFrameTriggering(self):
        """Test FlexrayFrameTriggering class functionality."""
        parent = MockParent()
        triggering = FlexrayFrameTriggering(parent, "test_flexray_frame_triggering")

        assert isinstance(triggering, FrameTriggering)
        
        # Test default values
        assert triggering.getAbsolutelyScheduledTimings() == []
        assert triggering.getAllowDynamicLSduLength() is None
        assert triggering.getMessageId() is None
        assert triggering.getPayloadPreambleIndicator() is None
        
        # Test setter/getter methods
        triggering.setAllowDynamicLSduLength(True)
        assert triggering.getAllowDynamicLSduLength() is True
        
        triggering.setMessageId(42)
        assert triggering.getMessageId() == 42
        
        # Test adding absolutely scheduled timings
        timing = FlexrayAbsolutelyScheduledTiming()
        triggering.addAbsolutelyScheduledTiming(timing)
        assert triggering.getAbsolutelyScheduledTimings() == [timing]

    def test_FlexrayFrameTriggering_none_handling(self):
        """Test FlexrayFrameTriggering None value handling to achieve 100% coverage."""
        parent = MockParent()
        triggering = FlexrayFrameTriggering(parent, "test_flexray_frame_triggering")

        # Test setting None keeps original value (which is None) - tests if value is not None logic
        result = triggering.setAllowDynamicLSduLength(None)
        assert result == triggering
        assert triggering.getAllowDynamicLSduLength() is None

        result = triggering.setMessageId(None)
        assert result == triggering
        assert triggering.getMessageId() is None

        result = triggering.setPayloadPreambleIndicator(None)
        assert result == triggering
        assert triggering.getPayloadPreambleIndicator() is None

        # Test setting actual values then setting back to None (should not change value)
        triggering.setAllowDynamicLSduLength(True)
        assert triggering.getAllowDynamicLSduLength() is True
        result = triggering.setAllowDynamicLSduLength(None)
        assert result == triggering
        # Value should remain unchanged since None was passed
        assert triggering.getAllowDynamicLSduLength() is True

        triggering.setMessageId(123)
        assert triggering.getMessageId() == 123
        result = triggering.setMessageId(None)
        assert result == triggering
        # Value should remain unchanged since None was passed
        assert triggering.getMessageId() == 123

        # Test addAbsolutelyScheduledTiming with None (should not add to list)
        original_timings = triggering.getAbsolutelyScheduledTimings()
        result = triggering.addAbsolutelyScheduledTiming(None)
        assert result == triggering
        # The list should remain unchanged since None was passed
        assert triggering.getAbsolutelyScheduledTimings() == original_timings


from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology import (
    FlexrayCommunicationController,
    FlexrayCommunicationConnector,
    FlexrayCluster
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommunicationController, CommunicationConnector, CommunicationCluster


class Test_Fibex4FlexrayTopology:
    """Test cases for Fibex4Flexray Topology classes."""
    
    def test_FlexrayCommunicationController(self):
        """Test FlexrayCommunicationController class functionality."""
        parent = MockParent()
        controller = FlexrayCommunicationController(parent, "test_flexray_comm_controller")

        assert isinstance(controller, CommunicationController)
        
        # Test default values
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
        
        # Test setter/getter methods
        controller.setKeySlotID(10)
        assert controller.getKeySlotID() == 10
        
        controller.setAllowHaltDueToClock(True)
        assert controller.getAllowHaltDueToClock() is True

    def test_FlexrayCommunicationConnector(self):
        """Test FlexrayCommunicationConnector class functionality."""
        parent = MockParent()
        connector = FlexrayCommunicationConnector(parent, "test_flexray_comm_connector")

        assert isinstance(connector, CommunicationConnector)
        
        # Test default values
        assert connector.getNmReadySleepTime() is None
        assert connector.getPncFilterDataMask() is None
        assert connector.getWakeUpChannel() is None
        
        # Test setter/getter methods
        connector.setNmReadySleepTime(10.5)
        assert connector.getNmReadySleepTime() == 10.5

    def test_FlexrayCluster(self):
        """Test FlexrayCluster class functionality."""
        parent = MockParent()
        cluster = FlexrayCluster(parent, "test_flexray_cluster")

        assert isinstance(cluster, CommunicationCluster)
        
        # Test default values
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
        
        # Test setter/getter methods
        cluster.setColdStartAttempts(5)
        assert cluster.getColdStartAttempts() == 5