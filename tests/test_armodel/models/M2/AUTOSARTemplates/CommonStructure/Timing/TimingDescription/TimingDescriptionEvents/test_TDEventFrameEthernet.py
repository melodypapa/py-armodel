from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventCom import (
    TDEventCom,
    TDEventFrameEthernet,
    TDEventFrameEthernetTypeEnum,
    TDHeaderIdRange,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    RefType,
)


class TestTDEventFrameEthernet:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_base_is_td_event_com(self):
        assert issubclass(TDEventFrameEthernet, TDEventCom)

    def test_defaults(self):
        parent = self._parent()
        event = TDEventFrameEthernet(parent, "Eth1")
        assert event.getStaticSocketConnectionRef() is None
        assert event.getTdEventType() is None
        assert event.getTdHeaderIdFilter() == []
        assert event.getTdPduTriggeringFilterRefs() == []

    def test_set_get_static_socket_connection_ref(self):
        parent = self._parent()
        event = TDEventFrameEthernet(parent, "Eth1")
        ref = RefType().setValue("/AUTOSAR/Socket").setDest("STATIC-SOCKET-CONNECTION")
        assert event.setStaticSocketConnectionRef(ref) is event
        assert event.getStaticSocketConnectionRef() is ref

    def test_set_get_td_event_type(self):
        parent = self._parent()
        event = TDEventFrameEthernet(parent, "Eth1")
        enum = TDEventFrameEthernetTypeEnum()
        enum.value = TDEventFrameEthernetTypeEnum.FRAME_ETHERNET_QUEUED_FOR_TRANSMISSION
        assert event.setTdEventType(enum) is event
        assert event.getTdEventType() is enum

    def test_add_td_header_id_filter(self):
        parent = self._parent()
        event = TDEventFrameEthernet(parent, "Eth1")
        rng = TDHeaderIdRange()
        rng.setMinHeaderId(Integer().setValue("5"))
        rng.setMaxHeaderId(Integer().setValue("10"))
        assert event.addTDHeaderIdFilter(rng) is event
        assert event.getTdHeaderIdFilter() == [rng]
        assert event.getTdHeaderIdFilter()[0].getMinHeaderId().getValue() == 5

    def test_add_td_pdu_triggering_filter_ref(self):
        parent = self._parent()
        event = TDEventFrameEthernet(parent, "Eth1")
        ref = RefType().setValue("/AUTOSAR/Pdu").setDest("PDU-TRIGGERING")
        assert event.addTdPduTriggeringFilterRef(ref) is event
        assert event.getTdPduTriggeringFilterRefs() == [ref]

    def test_set_none_noop(self):
        parent = self._parent()
        event = TDEventFrameEthernet(parent, "Eth1")
        ref = RefType().setValue("/AUTOSAR/Socket").setDest("STATIC-SOCKET-CONNECTION")
        event.setStaticSocketConnectionRef(ref)
        event.setStaticSocketConnectionRef(None)
        assert event.getStaticSocketConnectionRef() is ref
