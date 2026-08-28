from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventCom import (
    TDEventCom,
    TDEventIPdu,
    TDEventIPduTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class TestTDEventIPdu:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_base_is_td_event_com(self):
        assert issubclass(TDEventIPdu, TDEventCom)

    def test_defaults(self):
        parent = self._parent()
        event = TDEventIPdu(parent, "IPdu1")
        assert event.getIPduRef() is None
        assert event.getPhysicalChannelRef() is None
        assert event.getTdEventType() is None

    def test_set_get_i_pdu_ref(self):
        parent = self._parent()
        event = TDEventIPdu(parent, "IPdu1")
        ref = RefType().setValue("/AUTOSAR/IPdu").setDest("I-PDU")
        assert event.setIPduRef(ref) is event
        assert event.getIPduRef() is ref

    def test_set_get_physical_channel_ref(self):
        parent = self._parent()
        event = TDEventIPdu(parent, "IPdu1")
        ref = RefType().setValue("/AUTOSAR/Channel").setDest("PHYSICAL-CHANNEL")
        assert event.setPhysicalChannelRef(ref) is event
        assert event.getPhysicalChannelRef() is ref

    def test_set_get_td_event_type(self):
        parent = self._parent()
        event = TDEventIPdu(parent, "IPdu1")
        enum = TDEventIPduTypeEnum()
        enum.value = TDEventIPduTypeEnum.IPDU_RECEIVED_BY_COM
        assert event.setTdEventType(enum) is event
        assert event.getTdEventType() is enum

    def test_set_none_noop(self):
        parent = self._parent()
        event = TDEventIPdu(parent, "IPdu1")
        ref = RefType().setValue("/AUTOSAR/IPdu").setDest("I-PDU")
        event.setIPduRef(ref)
        event.setIPduRef(None)
        assert event.getIPduRef() is ref
