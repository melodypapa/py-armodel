import ast
import inspect
import sys
from typing import List, Optional, get_type_hints

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Integer, PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayCommunication import FlexrayAbsolutelyScheduledTiming, FlexrayFrame, FlexrayFrameTriggering
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology import FlexrayCluster, FlexrayCommunicationConnector, FlexrayCommunicationController
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import Frame, FrameTriggering
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommunicationCluster, CommunicationConnector, CommunicationController, CommunicationCycle, CycleCounter

NOTE_FLEXRAY_FRAME_TRIGGERING = (
    "FlexRay specific attributes to the FrameTriggering\n"
    "\n"
    "[constr_9124] Existence of FlexrayFrameTriggering.allowDynamicLSduLength: For each FlexrayFrameTriggering, "
    "the attribute allowDynamicLSduLength shall exist at the time when the System Description is complete.\n"
    "\n"
    "[constr_9125] Existence of FlexrayFrameTriggering.payloadPreambleIndicator: For each FlexrayFrameTriggering, "
    "the attribute payloadPreambleIndicator shall exist at the time when the System Description is complete."
)
NOTE_FLEXRAY_ABSOLUTELY_SCHEDULED_TIMING = (
    "Each frame in FlexRay is identified by its slot id and communication cycle. "
    "A description is provided by the usage of AbsolutelyScheduledTiming. "
    "In the static segment a frame can be sent multiple times within one communication cycle. "
    "For describing this case multiple AbsolutelyScheduledTimings have to be used. "
    "The main use case would be that a frame is sent twice within one communication cycle.\n"
    "\n"
    "[constr_9126] Existence of FlexrayAbsolutelyScheduledTiming.slotID: For each FlexrayAbsolutelyScheduledTiming, "
    "the attribute slotID shall exist at the time when the System Description is complete.\n"
    "\n"
    "[constr_9127] Existence of FlexrayAbsolutelyScheduledTiming.communicationCycle: For each "
    "FlexrayAbsolutelyScheduledTiming, the aggregation of CommunicationCycle in the role communicationCycle "
    "shall exist at the time when the System Description is complete."
)


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
        assert frame.short_name == "test_flexray_frame"

    def test_flexray_frame_creation(self):
        """Test FlexrayFrame class creation to ensure the __init__ method is covered."""
        parent = MockParent()
        frame = FlexrayFrame(parent, "test_frame")

        # Verify that the frame was created properly
        assert frame.short_name == "test_frame"
        assert frame.parent == parent

class TestFlexrayAbsolutelyScheduledTiming:
    """Test cases for FlexrayAbsolutelyScheduledTiming (Table 6.82, p.423)."""

    MEMBERS = ["communicationCycle", "slotID"]

    def _init_annotations(self):
        src = inspect.getsource(sys.modules[FlexrayAbsolutelyScheduledTiming.__module__])
        tree = ast.parse(src)
        cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "FlexrayAbsolutelyScheduledTiming")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        return [n.target.attr for n in init.body if isinstance(n, ast.AnnAssign) and isinstance(n.target, ast.Attribute)]

    def test_initialization(self):
        timing = FlexrayAbsolutelyScheduledTiming()

        assert isinstance(timing, ARObject)
        assert timing.getCommunicationCycle() is None
        assert timing.getSlotID() is None

    def test_member_order(self):
        assert self._init_annotations() == self.MEMBERS

    def test_init_has_no_docstring(self):
        assert FlexrayAbsolutelyScheduledTiming.__init__.__doc__ is None

    def test_get_set_communication_cycle(self):
        timing = FlexrayAbsolutelyScheduledTiming()
        counter = CycleCounter()
        counter.setCycleCounter(Integer().setValue("3"))

        assert timing == timing.setCommunicationCycle(counter)
        assert timing.getCommunicationCycle() is counter

        assert timing == timing.setCommunicationCycle(None)
        assert timing.getCommunicationCycle() is counter

    def test_get_set_slot_id(self):
        timing = FlexrayAbsolutelyScheduledTiming()
        slot = PositiveInteger().setValue("10")

        assert timing == timing.setSlotID(slot)
        assert timing.getSlotID() is slot
        assert timing.getSlotID().getValue() == 10

        assert timing == timing.setSlotID(None)
        assert timing.getSlotID() is slot

    def test_type_annotations(self):
        hints = get_type_hints(FlexrayAbsolutelyScheduledTiming.getCommunicationCycle)
        assert hints["return"] == Optional[CommunicationCycle]

        hints = get_type_hints(FlexrayAbsolutelyScheduledTiming.setCommunicationCycle)
        assert hints["value"] == Optional[CommunicationCycle]
        assert hints["return"] == FlexrayAbsolutelyScheduledTiming

        hints = get_type_hints(FlexrayAbsolutelyScheduledTiming.getSlotID)
        assert hints["return"] == Optional[PositiveInteger]

        hints = get_type_hints(FlexrayAbsolutelyScheduledTiming.setSlotID)
        assert hints["value"] == Optional[PositiveInteger]
        assert hints["return"] == FlexrayAbsolutelyScheduledTiming

        src = inspect.getsource(sys.modules[FlexrayAbsolutelyScheduledTiming.__module__])
        tree = ast.parse(src)
        cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "FlexrayAbsolutelyScheduledTiming")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = {}
        for node in ast.walk(init):
            if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Attribute):
                annotations[node.target.attr] = ast.get_source_segment(src, node.annotation)
        assert annotations["communicationCycle"] == "Optional[CommunicationCycle]"
        assert annotations["slotID"] == "Optional[PositiveInteger]"

    def test_class_docstring_note(self):
        assert inspect.cleandoc(FlexrayAbsolutelyScheduledTiming.__doc__) == NOTE_FLEXRAY_ABSOLUTELY_SCHEDULED_TIMING


class TestFlexrayFrameTriggering:
    """Test cases for FlexrayFrameTriggering (Table 6.81, p.423)."""

    MEMBERS = ["absolutelyScheduledTimings", "allowDynamicLSduLength", "messageId", "payloadPreambleIndicator"]

    def _init_annotations(self):
        src = inspect.getsource(sys.modules[FlexrayFrameTriggering.__module__])
        tree = ast.parse(src)
        cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "FlexrayFrameTriggering")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        return [n.target.attr for n in init.body if isinstance(n, ast.AnnAssign) and isinstance(n.target, ast.Attribute)]

    def test_heritage(self):
        assert issubclass(FlexrayFrameTriggering, FrameTriggering)
        assert issubclass(FlexrayFrameTriggering, ARObject)

    def test_initialization(self):
        parent = MockParent()
        triggering = FlexrayFrameTriggering(parent, "ft")

        assert triggering.short_name == "ft"
        assert triggering.getAbsolutelyScheduledTimings() == []
        assert triggering.getAllowDynamicLSduLength() is None
        assert triggering.getMessageId() is None
        assert triggering.getPayloadPreambleIndicator() is None

    def test_member_order(self):
        assert self._init_annotations() == self.MEMBERS

    def test_init_has_no_docstring(self):
        assert FlexrayFrameTriggering.__init__.__doc__ is None

    def test_add_absolutely_scheduled_timing(self):
        parent = MockParent()
        triggering = FlexrayFrameTriggering(parent, "ft")
        first = FlexrayAbsolutelyScheduledTiming()
        second = FlexrayAbsolutelyScheduledTiming()

        assert triggering == triggering.addAbsolutelyScheduledTiming(first)
        assert triggering.getAbsolutelyScheduledTimings() == [first]

        triggering.addAbsolutelyScheduledTiming(second)
        assert triggering.getAbsolutelyScheduledTimings() == [first, second]

        assert triggering == triggering.addAbsolutelyScheduledTiming(None)
        assert triggering.getAbsolutelyScheduledTimings() == [first, second]

    def test_get_set_allow_dynamic_lsdu_length(self):
        parent = MockParent()
        triggering = FlexrayFrameTriggering(parent, "ft")
        value = Boolean().setValue(True)

        assert triggering == triggering.setAllowDynamicLSduLength(value)
        assert triggering.getAllowDynamicLSduLength() is value

        assert triggering == triggering.setAllowDynamicLSduLength(None)
        assert triggering.getAllowDynamicLSduLength() is value

    def test_get_set_message_id(self):
        parent = MockParent()
        triggering = FlexrayFrameTriggering(parent, "ft")
        value = PositiveInteger().setValue("1024")

        assert triggering == triggering.setMessageId(value)
        assert triggering.getMessageId() is value
        assert triggering.getMessageId().getValue() == 1024

        assert triggering == triggering.setMessageId(None)
        assert triggering.getMessageId() is value

    def test_get_set_payload_preamble_indicator(self):
        parent = MockParent()
        triggering = FlexrayFrameTriggering(parent, "ft")
        value = Boolean().setValue(True)

        assert triggering == triggering.setPayloadPreambleIndicator(value)
        assert triggering.getPayloadPreambleIndicator() is value

        assert triggering == triggering.setPayloadPreambleIndicator(None)
        assert triggering.getPayloadPreambleIndicator() is value

    def test_type_annotations(self):
        hints = get_type_hints(FlexrayFrameTriggering.getAbsolutelyScheduledTimings)
        assert hints["return"] == List[FlexrayAbsolutelyScheduledTiming]

        hints = get_type_hints(FlexrayFrameTriggering.addAbsolutelyScheduledTiming)
        assert hints["value"] == Optional[FlexrayAbsolutelyScheduledTiming]
        assert hints["return"] == FlexrayFrameTriggering

        hints = get_type_hints(FlexrayFrameTriggering.getAllowDynamicLSduLength)
        assert hints["return"] == Optional[Boolean]

        hints = get_type_hints(FlexrayFrameTriggering.setAllowDynamicLSduLength)
        assert hints["value"] == Optional[Boolean]
        assert hints["return"] == FlexrayFrameTriggering

        hints = get_type_hints(FlexrayFrameTriggering.getMessageId)
        assert hints["return"] == Optional[PositiveInteger]

        hints = get_type_hints(FlexrayFrameTriggering.setMessageId)
        assert hints["value"] == Optional[PositiveInteger]
        assert hints["return"] == FlexrayFrameTriggering

        hints = get_type_hints(FlexrayFrameTriggering.getPayloadPreambleIndicator)
        assert hints["return"] == Optional[Boolean]

        hints = get_type_hints(FlexrayFrameTriggering.setPayloadPreambleIndicator)
        assert hints["value"] == Optional[Boolean]
        assert hints["return"] == FlexrayFrameTriggering

        src = inspect.getsource(sys.modules[FlexrayFrameTriggering.__module__])
        tree = ast.parse(src)
        cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "FlexrayFrameTriggering")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = {}
        for node in ast.walk(init):
            if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Attribute):
                annotations[node.target.attr] = ast.get_source_segment(src, node.annotation)
        assert annotations["absolutelyScheduledTimings"] == "List[FlexrayAbsolutelyScheduledTiming]"
        assert annotations["allowDynamicLSduLength"] == "Optional[Boolean]"
        assert annotations["messageId"] == "Optional[PositiveInteger]"
        assert annotations["payloadPreambleIndicator"] == "Optional[Boolean]"

    def test_class_docstring_note(self):
        assert inspect.cleandoc(FlexrayFrameTriggering.__doc__) == NOTE_FLEXRAY_FRAME_TRIGGERING


class Test_FlexrayFrameSpec:
    """Spec contract of FlexrayFrame (AUTOSAR_CP_TPS_SystemTemplate, Table 6.80, p.422)."""

    def test_docstring_is_spec_note_verbatim(self):
        note = "FlexRay specific Frame element. Tags: atp.recommendedPackage=Frames"
        assert FlexrayFrame.__doc__.strip() == note

    def test_init_has_no_docstring(self):
        assert FlexrayFrame.__init__.__doc__ is None

    def test_heritage(self):
        assert issubclass(FlexrayFrame, Frame)
        assert issubclass(FlexrayFrame, ARObject)

    def test_concrete_instantiation(self):
        parent = MockParent()
        frame = FlexrayFrame(parent, "fr_frame")
        assert frame.short_name == "fr_frame"
        assert FlexrayFrame.__abstractmethods__ == frozenset() if hasattr(FlexrayFrame, "__abstractmethods__") else True


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
