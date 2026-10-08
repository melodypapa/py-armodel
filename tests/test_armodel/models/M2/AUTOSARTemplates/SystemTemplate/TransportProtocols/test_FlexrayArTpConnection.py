import typing
from inspect import cleandoc
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection import TpConnection, TpConnectionIdent
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import FlexrayArTpConnection


def _ref(value, dest):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _integer(value):
    integer = Integer()
    integer.setValue(value)
    return integer


class Test_FlexrayArTpConnection:
    # Table 6.248, p.603 — attribute Notes verbatim from the markdown
    NOTE_CONNECTION_PRIO_PDUS = "This parameter defines the number of PDUs that shall be reserved for this connection when it is active. The range is 1-255."
    NOTE_DIRECT_TP_SDUs = (
        "Reference to the IPdu that is segmented by the Transport Protocol. "
        "The source address of the transmitted NPdu is determined by the configured source Communication Connector. "
        "The target address of the transmitted NPdu is determined by the configured target Communication Connector."
    )
    NOTE_MULTICAST = "TP address for 1:n connections."
    NOTE_REVERSED_TP_SDUs = (
        "Reference to the IPdu that is segmented by the Transport Protocol. "
        "If support of both sending and receiving is used, this association references the IPdu used for the additional second direction. "
        "The source address of the transmitted NPdu is determined by the configured target Communication Connector. "
        "The target address of the transmitted NPdu is determined by the configured source Communication Connector."
    )
    NOTE_SOURCE = "The source of the TP connection."
    NOTE_TARGET = "The target of the TP connection."

    def test_docstring_is_spec_note_verbatim(self):
        # Table 6.248, p.603 — class Note verbatim from the markdown + table constraints appended
        note = "A connection within a channel identifies the sender and the receiver of this particular communication. " "The FlexRay Autosar Tp module routes a Pdu through this connection."
        constrs = [
            "[constr_9244] Existence of FlexrayArTpConnection.directTpSdu: For each FlexrayArTpConnection, the reference to IPdu in the role directTpSdu shall exist at the time when the System Description is complete.",
            "[constr_9245] Existence of FlexrayArTpConnection.source: For each FlexrayArTpConnection, the reference to FlexrayArTpNode in the role source shall exist at the time when the System Description is complete.",
            "[constr_9246] Existence of FlexrayArTpConnection.target: For each FlexrayArTpConnection, at least one reference to FlexrayArTpNode in the role target shall exist at the time when the System Description is complete.",
        ]
        expected = note + "\n\n" + "\n\n".join(constrs)
        assert cleandoc(FlexrayArTpConnection.__doc__) == expected

    def test_init_has_no_docstring(self):
        assert FlexrayArTpConnection.__init__.__doc__ is None

    def test_heritage(self):
        connection = FlexrayArTpConnection()
        assert isinstance(connection, TpConnection)
        assert connection.getIdent() is None

    def test_initialization(self):
        # spec displayed order: connectionPrioPdus, directTpSdu, multicast, reversedTpSdu, source, target `*`
        connection = FlexrayArTpConnection()
        assert connection.getConnectionPrioPdus() is None
        assert connection.getDirectTpSduRef() is None
        assert connection.getMulticastRef() is None
        assert connection.getReversedTpSduRef() is None
        assert connection.getSourceRef() is None
        assert connection.getTargetRefs() == []

    def test_get_set_connection_prio_pdus(self):
        connection = FlexrayArTpConnection()
        value = _integer("8")
        assert connection.setConnectionPrioPdus(value) is connection
        assert connection.getConnectionPrioPdus() is value
        connection.setConnectionPrioPdus(None)
        assert connection.getConnectionPrioPdus() is value

    def test_get_set_direct_tp_sdu_ref(self):
        connection = FlexrayArTpConnection()
        value = _ref("/Pdus/Direct", "I-PDU")
        assert connection.setDirectTpSduRef(value) is connection
        assert connection.getDirectTpSduRef() is value
        connection.setDirectTpSduRef(None)
        assert connection.getDirectTpSduRef() is value

    def test_get_set_multicast_ref(self):
        connection = FlexrayArTpConnection()
        value = _ref("/TpAddresses/Addr", "TP-ADDRESS")
        assert connection.setMulticastRef(value) is connection
        assert connection.getMulticastRef() is value
        connection.setMulticastRef(None)
        assert connection.getMulticastRef() is value

    def test_get_set_reversed_tp_sdu_ref(self):
        connection = FlexrayArTpConnection()
        value = _ref("/Pdus/Reversed", "I-PDU")
        assert connection.setReversedTpSduRef(value) is connection
        assert connection.getReversedTpSduRef() is value
        connection.setReversedTpSduRef(None)
        assert connection.getReversedTpSduRef() is value

    def test_get_set_source_ref(self):
        connection = FlexrayArTpConnection()
        value = _ref("/TpNodes/Source", "FLEXRAY-AR-TP-NODE")
        assert connection.setSourceRef(value) is connection
        assert connection.getSourceRef() is value
        connection.setSourceRef(None)
        assert connection.getSourceRef() is value

    def test_add_get_target_refs(self):
        connection = FlexrayArTpConnection()
        ref1 = _ref("/TpNodes/Tgt1", "FLEXRAY-AR-TP-NODE")
        ref2 = _ref("/TpNodes/Tgt2", "FLEXRAY-AR-TP-NODE")
        assert connection.addTargetRef(ref1) is connection
        assert connection.getTargetRefs() == [ref1]
        connection.addTargetRef(ref2)
        assert connection.getTargetRefs() == [ref1, ref2]
        connection.addTargetRef(None)
        assert connection.getTargetRefs() == [ref1, ref2]

    def test_type_hints_pins(self):
        for getter, setter in [
            ("getDirectTpSduRef", "setDirectTpSduRef"),
            ("getMulticastRef", "setMulticastRef"),
            ("getReversedTpSduRef", "setReversedTpSduRef"),
            ("getSourceRef", "setSourceRef"),
        ]:
            assert typing.get_type_hints(getattr(FlexrayArTpConnection, getter)).get("return") == Optional[RefType]
            assert typing.get_type_hints(getattr(FlexrayArTpConnection, setter)).get("value") == Optional[RefType]
            assert typing.get_type_hints(getattr(FlexrayArTpConnection, setter)).get("return") is FlexrayArTpConnection
        assert typing.get_type_hints(FlexrayArTpConnection.getConnectionPrioPdus).get("return") == Optional[Integer]
        assert typing.get_type_hints(FlexrayArTpConnection.setConnectionPrioPdus).get("value") == Optional[Integer]
        assert typing.get_type_hints(FlexrayArTpConnection.setConnectionPrioPdus).get("return") is FlexrayArTpConnection
        assert typing.get_type_hints(FlexrayArTpConnection.getTargetRefs).get("return") == List[RefType]
        assert typing.get_type_hints(FlexrayArTpConnection.addTargetRef).get("value") == Optional[RefType]
        assert typing.get_type_hints(FlexrayArTpConnection.addTargetRef).get("return") is FlexrayArTpConnection

    def test_ident_factory(self):
        connection = FlexrayArTpConnection()
        ident = connection.createTpConnectionIdent("FrArIdent")
        assert isinstance(ident, TpConnectionIdent)
        assert connection.getIdent() is ident
        assert connection.createTpConnectionIdent("other") is ident

    def test_not_variation_point_capable(self):
        # XSD group FLEXRAY-AR-TP-CONNECTION carries no VARIATION-POINT element
        assert not hasattr(FlexrayArTpConnection, "getVariationPoint")
