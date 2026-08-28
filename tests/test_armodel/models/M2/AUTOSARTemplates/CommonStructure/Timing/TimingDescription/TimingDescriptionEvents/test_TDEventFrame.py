from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventCom import (
    TDEventCom,
    TDEventFrame,
    TDEventFrameTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class TestTDEventFrame:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_base_is_td_event_com(self):
        assert issubclass(TDEventFrame, TDEventCom)

    def test_defaults(self):
        parent = self._parent()
        event = TDEventFrame(parent, "Frame1")
        assert event.getFrameRef() is None
        assert event.getPhysicalChannelRef() is None
        assert event.getTdEventType() is None

    def test_set_get_frame_ref(self):
        parent = self._parent()
        event = TDEventFrame(parent, "Frame1")
        ref = RefType().setValue("/AUTOSAR/Frame").setDest("FRAME")
        assert event.setFrameRef(ref) is event
        assert event.getFrameRef() is ref

    def test_set_get_physical_channel_ref(self):
        parent = self._parent()
        event = TDEventFrame(parent, "Frame1")
        ref = RefType().setValue("/AUTOSAR/Channel").setDest("PHYSICAL-CHANNEL")
        assert event.setPhysicalChannelRef(ref) is event
        assert event.getPhysicalChannelRef() is ref

    def test_set_get_td_event_type(self):
        parent = self._parent()
        event = TDEventFrame(parent, "Frame1")
        enum = TDEventFrameTypeEnum()
        enum.value = TDEventFrameTypeEnum.FRAME_QUEUED_FOR_TRANSMISSION
        assert event.setTdEventType(enum) is event
        assert event.getTdEventType() is enum

    def test_set_none_noop(self):
        parent = self._parent()
        event = TDEventFrame(parent, "Frame1")
        ref = RefType().setValue("/AUTOSAR/Frame").setDest("FRAME")
        event.setFrameRef(ref)
        event.setFrameRef(None)
        assert event.getFrameRef() is ref
