"""
Test suite for FlexrayTopology classes in AUTOSAR System Template.

This module contains comprehensive unit tests for FlexRay communication topology classes
including FlexRay clusters, communication controllers, connectors, and related components.
Each test validates the functionality, inheritance, and setter/getter methods
of the respective classes.
"""

import pytest
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology import (
    FlexrayCommunicationController,
    FlexrayCommunicationConnector,
    FlexrayCluster
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommunicationController, CommunicationConnector


class MockParent(ARObject):
    """
    Mock parent class for testing purposes.
    
    This class extends ARObject to provide a concrete implementation
    that can be used as a parent for testing classes that require
    an ARObject instance during initialization.
    """
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
        Test the FlexrayCommunicationController class initialization and methods.
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
        
        # Test setting values
        controller.setAcceptedStartupRange(5)
        controller.setAllowHaltDueToClock(True)
        controller.setKeySlotID(2)
        controller.setKeySlotOnlyEnabled(False)
        
        assert controller.getAcceptedStartupRange() == 5
        assert controller.getAllowHaltDueToClock() is True
        assert controller.getKeySlotID() == 2
        assert controller.getKeySlotOnlyEnabled() is False

    def test_flexray_communication_connector(self):
        """
        Test the FlexrayCommunicationConnector class initialization and methods.
        """
        parent = MockParent()
        connector = FlexrayCommunicationConnector(parent, "TestConnector")
        
        assert connector.getShortName() == "TestConnector"
        assert isinstance(connector, CommunicationConnector)
        assert connector.getNmReadySleepTime() is None
        assert connector.getPncFilterDataMask() is None
        assert connector.getWakeUpChannel() is None
        
        # Test setting values
        connector.setNmReadySleepTime(10.5)
        connector.setPncFilterDataMask(255)
        connector.setWakeUpChannel(True)
        
        assert connector.getNmReadySleepTime() == 10.5
        assert connector.getPncFilterDataMask() == 255
        assert connector.getWakeUpChannel() is True

    def test_flexray_cluster(self):
        """
        Test the FlexrayCluster class initialization and methods.
        """
        parent = MockParent()
        cluster = FlexrayCluster(parent, "TestCluster")
        
        assert cluster.getShortName() == "TestCluster"
        assert isinstance(cluster, Identifiable)
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
        
        # Test setting values
        cluster.setActionPointOffset(10)
        cluster.setBit(25.0)
        cluster.setColdStartAttempts(5)
        cluster.setCycle(100.0)
        
        assert cluster.getActionPointOffset() == 10
        assert cluster.getBit() == 25.0
        assert cluster.getColdStartAttempts() == 5
        assert cluster.getCycle() == 100.0