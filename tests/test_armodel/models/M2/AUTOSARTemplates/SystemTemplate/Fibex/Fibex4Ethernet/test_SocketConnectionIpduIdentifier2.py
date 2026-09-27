import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetCommunication import (
    SocketConnectionIpduIdentifier,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    PduCollectionSemanticsEnum,
    PduCollectionTriggerEnum,
)

CLASS_NOTE = """An Identifier is required in case of one port per ECU communication where multiple Pdus are transmitted over the same connection. If only one IPdu is transmitted over the connetion this attribute can be ignored."""


class TestSocketConnectionIpduIdentifier:
    """Test cases for SocketConnectionIpduIdentifier (R4.3.1 Table 6.122, p.321)."""

    def _obj(self):
        return SocketConnectionIpduIdentifier()

    def test_initialization_defaults(self):
        obj = self._obj()
        assert obj.getHeaderId() is None
        assert obj.getPduCollectionPduTimeout() is None
        assert obj.getPduCollectionSemantics() is None
        assert obj.getPduCollectionTrigger() is None
        assert obj.getPduTriggeringRef() is None
        assert obj.getRoutingGroupRefs() == []

    def test_setters_round_trip_and_none_noop(self):
        obj = self._obj()
        assert obj.setHeaderId(7) is obj
        assert obj.getHeaderId() == 7
        obj.setHeaderId(None)
        assert obj.getHeaderId() == 7

        timeout = TimeValue()
        assert obj.setPduCollectionPduTimeout(timeout) is obj
        assert obj.getPduCollectionPduTimeout() is timeout

        assert obj.setPduCollectionSemantics(PduCollectionSemanticsEnum.QUEUED) is obj
        assert obj.getPduCollectionSemantics() == PduCollectionSemanticsEnum.QUEUED
        obj.setPduCollectionSemantics(None)
        assert obj.getPduCollectionSemantics() == PduCollectionSemanticsEnum.QUEUED

        assert obj.setPduCollectionTrigger(PduCollectionTriggerEnum.ALWAYS) is obj
        assert obj.getPduCollectionTrigger() == PduCollectionTriggerEnum.ALWAYS

        ref = RefType()
        ref.value = "/triggering"
        assert obj.setPduTriggeringRef(ref) is obj
        assert obj.getPduTriggeringRef() is ref

        other = RefType()
        other.value = "/rg"
        assert obj.setRoutingGroupRefs([other]) is obj
        assert obj.getRoutingGroupRefs() == [other]
        obj.setRoutingGroupRefs(None)
        assert obj.getRoutingGroupRefs() == [other]

    def test_class_docstring_note(self):
        assert inspect.cleandoc(SocketConnectionIpduIdentifier.__doc__).split("\n\n")[0] == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        obj = self._obj()

        assert inspect.cleandoc(obj.getHeaderId.__doc__) == "If multiple Pdus are transmitted over the same connection this headerId can be used to distinguish between the different Pdus."
        assert (
            inspect.cleandoc(obj.getPduCollectionPduTimeout.__doc__)
            == "Defines the timeout in seconds the PDU collection shall be transmitted at the latest after this PDU has been put into the buffer."
        )
        assert (
            inspect.cleandoc(obj.getPduCollectionSemantics.__doc__)
            == 'Specifies if the referenced PduTriggering shall be collected using a queued (i.e. all PDU instances) or last-is-best (i.e. only the last PDU instance) semantics. If this attribute is not present the behavior of "queued" is assumed.'
        )
        assert (
            inspect.cleandoc(obj.getPduCollectionTrigger.__doc__)
            == "Defines whether the referenced Pdu contributes to the triggering of the socket transmission if Pdu collection is enabled for this socket."
        )
        assert inspect.cleandoc(obj.getPduTriggeringRef.__doc__) == "Reference to a Pdu that is mapped to a socket connection."
        assert inspect.cleandoc(obj.getRoutingGroupRefs.__doc__) == "Reference to RoutingGroups that can be enabled or disabled."
