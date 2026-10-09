import typing
from inspect import cleandoc
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import SomeipTpConnection


def _ref(value, dest):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


class Test_SomeipTpConnection:
    # Table 6.265, p.620 — attribute Note verbatim from the markdown
    NOTE_TP_CHANNEL = "Assignment of configuration properties valid for this SomeipTpConnection."
    NOTE_TP_SDUs = "Reference to an IPdu that is segmented by the Transport Protocol."
    NOTE_TRANSPORT_PDUs = "Reference to the segmented IPdu."

    def test_docstring_is_spec_note_verbatim(self):
        # Table 6.265, p.620 — class Note verbatim from the markdown + table constraints appended
        note = "A connection identifies the sender and the receiver of this particular communication. The SOME/IP TP module routes a Pdu through this connection."
        constrs = [
            "[constr_3328] SomeipTpConnection.transportPdu reference restriction: A PduTriggering that is referenced by a SomeipTpConnection in the role transportPdu shall reference a GeneralPurposeIPdu with category SOMEIP_SEGMENTED_IPDU in the role iPdu.",
            "[constr_3329] SomeipTpConnection.tpSdu reference restriction: A PduTriggering that is referenced by a SomeipTpConnection in the role tpSdu shall reference an IPdu in the role iPdu.",
            "[constr_3330] Same transportPdu shall not be used in different SomeipTpConnections: A PduTriggering that is referencing a GeneralPurposeIPdu with category SOMEIP_SEGMENTED_IPDU in the role iPdu shall be referenced at most once by a SomeipTpConnection in the role transportPdu.",
            "[constr_5378] PduTriggering shall only be referenced once from a SomeipTpConnection in the role tpSdu: Each PduTriggering that is referenced in the role tpSdu from a SomeipTpConnection shall not be referenced in the role tpSdu from a different SomeipTpConnection.",
        ]
        expected = note + "\n\n" + "\n\n".join(constrs)
        assert cleandoc(SomeipTpConnection.__doc__) == expected

    def test_init_has_no_docstring(self):
        assert SomeipTpConnection.__init__.__doc__ is None

    def test_heritage(self):
        connection = SomeipTpConnection()
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

        assert isinstance(connection, ARObject)

    def test_initialization(self):
        connection = SomeipTpConnection()
        assert connection.getTpChannelRef() is None
        assert connection.getTpSduRef() is None
        assert connection.getTransportPduRef() is None

    def test_get_set_tp_channel_ref(self):
        connection = SomeipTpConnection()
        ref = _ref("/TpConfigs/SomeipChan", "SOMEIP-TP-CHANNEL")
        assert connection.setTpChannelRef(ref) is connection
        assert connection.getTpChannelRef() is ref
        connection.setTpChannelRef(None)
        assert connection.getTpChannelRef() is ref

    def test_get_set_tp_sdu_ref(self):
        connection = SomeipTpConnection()
        ref = _ref("/PduTriggerings/TpSdu", "PDU-TRIGGERING")
        assert connection.setTpSduRef(ref) is connection
        assert connection.getTpSduRef() is ref
        connection.setTpSduRef(None)
        assert connection.getTpSduRef() is ref

    def test_get_set_transport_pdu_ref(self):
        connection = SomeipTpConnection()
        ref = _ref("/PduTriggerings/TransportPdu", "PDU-TRIGGERING")
        assert connection.setTransportPduRef(ref) is connection
        assert connection.getTransportPduRef() is ref
        connection.setTransportPduRef(None)
        assert connection.getTransportPduRef() is ref

    def test_type_hints_pins(self):
        assert typing.get_type_hints(SomeipTpConnection.getTpChannelRef).get("return") == Optional[RefType]
        assert typing.get_type_hints(SomeipTpConnection.setTpChannelRef).get("value") == Optional[RefType]
        assert typing.get_type_hints(SomeipTpConnection.setTpChannelRef).get("return") is SomeipTpConnection
        assert typing.get_type_hints(SomeipTpConnection.getTpSduRef).get("return") == Optional[RefType]
        assert typing.get_type_hints(SomeipTpConnection.setTpSduRef).get("value") == Optional[RefType]
        assert typing.get_type_hints(SomeipTpConnection.setTpSduRef).get("return") is SomeipTpConnection
        assert typing.get_type_hints(SomeipTpConnection.getTransportPduRef).get("return") == Optional[RefType]
        assert typing.get_type_hints(SomeipTpConnection.setTransportPduRef).get("value") == Optional[RefType]
        assert typing.get_type_hints(SomeipTpConnection.setTransportPduRef).get("return") is SomeipTpConnection

    def test_not_variation_point_capable(self):
        # XSD group SOMEIP-TP-CONNECTION carries no VARIATION-POINT element
        assert not hasattr(SomeipTpConnection, "getVariationPoint")
