from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventCom import (
    TDEventCom,
    TDEventISignal,
    TDEventISignalTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class TestTDEventISignal:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_base_is_td_event_com(self):
        assert issubclass(TDEventISignal, TDEventCom)

    def test_defaults(self):
        parent = self._parent()
        event = TDEventISignal(parent, "ISig1")
        assert event.getISignalRef() is None
        assert event.getPhysicalChannelRef() is None
        assert event.getTdEventType() is None

    def test_set_get_i_signal_ref(self):
        parent = self._parent()
        event = TDEventISignal(parent, "ISig1")
        ref = RefType().setValue("/AUTOSAR/ISig").setDest("I-SIGNAL")
        assert event.setISignalRef(ref) is event
        assert event.getISignalRef() is ref

    def test_set_get_physical_channel_ref(self):
        parent = self._parent()
        event = TDEventISignal(parent, "ISig1")
        ref = RefType().setValue("/AUTOSAR/Channel").setDest("PHYSICAL-CHANNEL")
        assert event.setPhysicalChannelRef(ref) is event
        assert event.getPhysicalChannelRef() is ref

    def test_set_get_td_event_type(self):
        parent = self._parent()
        event = TDEventISignal(parent, "ISig1")
        enum = TDEventISignalTypeEnum()
        enum.value = TDEventISignalTypeEnum.ISIGNAL_AVAILABLE_FOR_RTE
        assert event.setTdEventType(enum) is event
        assert event.getTdEventType() is enum

    def test_set_none_noop(self):
        parent = self._parent()
        event = TDEventISignal(parent, "ISig1")
        ref = RefType().setValue("/AUTOSAR/ISig").setDest("I-SIGNAL")
        event.setISignalRef(ref)
        event.setISignalRef(None)
        assert event.getISignalRef() is ref
