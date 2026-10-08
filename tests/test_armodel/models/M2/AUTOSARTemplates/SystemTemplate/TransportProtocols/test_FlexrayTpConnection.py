import typing
from inspect import cleandoc
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection import TpConnection, TpConnectionIdent
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import FlexrayTpConnection


def _ref(value, dest):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _bool(value):
    boolean = Boolean()
    boolean.setValue(value)
    return boolean


class Test_FlexrayTpConnection:
    # Table 6.241, p.594 — attribute Notes verbatim from the markdown
    NOTE_BANDWIDTH_LIMITATION = "Specifies whether the connection requires a bandwidth limitation or not."
    NOTE_DIRECT_TP_SDUs = "Reference to the IPdu that is segmented by the Transport Protocol."
    NOTE_MULTICAST = "TP address for 1:n connections."
    NOTE_RECEIVER = "The target of the TP connection."
    NOTE_REVERSED_TP_SDUs = (
        "Reference to the IPdu that is segmented by the Transport Protocol. "
        "If support of both sending and receiving is used, this association references the IPdu used for the additional second direction."
    )
    NOTE_RX_PDU_POOL = (
        "A connection has a reference to a set of NPdus (FrTpRx PduPool) which are defined for receiving data via this particular connection. "
        "The following constraint is valid only for the System Extract/ECU Extract: "
        "In case this connection is applied to the transmitter the rxPduPool holds the actually received NPdus. "
        "In case this connection is applied to the receiver the rxPduPool holds the actually sent NPdus."
    )
    NOTE_TP_CONNECTION_CONTROL = "Reference to the connection control."
    NOTE_TRANSMITTER = "The source of the TP connection."
    NOTE_TX_PDU_POOL = (
        "A connection has a reference to a set of NPdus (FrTpTx PduPool) which are defined for sending data via this particular connection. "
        "The following constraint is valid only for the System Extract/ECU Extract: "
        "In case this connection is applied to the transmitter the txPduPool holds the actually sent NPdus. "
        "In case this connection is applied to the receiver the txPduPool holds the actually received NPdus."
    )

    def test_docstring_is_spec_note_verbatim(self):
        # Table 6.241, p.594 — class Note verbatim from the markdown + table constraints appended
        note = (
            "A connection identifies the sender and the receiver of this particular communication. The FlexRayTp module routes a Pdu through this connection. "
            "In a System Description the references to the PduPools are mandatory. In an ECU Extract these references can be optional: "
            "On unicast connections these references are always mandatory. On multicast the txPduPool is mandatory on the sender side. "
            "The rxPduPool is mandatory on the receiver side. On Gateway ECUs both references are mandatory."
        )
        constrs = [
            "[constr_9231] Existence of FlexrayTpConnection.directTpSdu: For each FlexrayTpConnection, the reference to IPdu in the role directTpSdu shall exist at the time when the System Description is complete.",
            "[constr_9233] Existence of FlexrayTpConnection.receiver: For each FlexrayTpConnection, the reference to FlexrayTpNode in the role receiver shall exist at least once at the time when the System Description is complete.",
            "[constr_9234] Existence of FlexrayTpConnection.tpConnectionControl: For each FlexrayTpConnection, the reference to FlexrayTpConnectionControl in the role tpConnectionControl shall exist at the time when the System Description is complete.",
            "[constr_9235] Existence of FlexrayTpConnection.transmitter: For each FlexrayTpConnection, the reference to FlexrayTpNode in the role transmitter shall exist at the time when the System Description is complete.",
        ]
        expected = note + "\n\n" + "\n\n".join(constrs)
        assert cleandoc(FlexrayTpConnection.__doc__) == expected

    def test_init_has_no_docstring(self):
        assert FlexrayTpConnection.__init__.__doc__ is None

    def test_heritage(self):
        connection = FlexrayTpConnection()
        assert isinstance(connection, TpConnection)
        assert connection.getIdent() is None

    def test_initialization(self):
        # spec displayed order: bandwidthLimitation, directTpSdu, multicast, receiver `*`,
        # reversedTpSdu, rxPduPool, tpConnectionControl, transmitter, txPduPool
        connection = FlexrayTpConnection()
        assert connection.getBandwidthLimitation() is None
        assert connection.getDirectTpSduRef() is None
        assert connection.getMulticastRef() is None
        assert connection.getReceiverRefs() == []
        assert connection.getReversedTpSduRef() is None
        assert connection.getRxPduPoolRef() is None
        assert connection.getTpConnectionControlRef() is None
        assert connection.getTransmitterRef() is None
        assert connection.getTxPduPoolRef() is None

    def test_get_set_bandwidth_limitation(self):
        connection = FlexrayTpConnection()
        value = _bool("true")
        assert connection.setBandwidthLimitation(value) is connection
        assert connection.getBandwidthLimitation() is value
        connection.setBandwidthLimitation(None)
        assert connection.getBandwidthLimitation() is value

    def test_get_set_direct_tp_sdu_ref(self):
        connection = FlexrayTpConnection()
        value = _ref("/Pdus/Direct", "I-PDU")
        assert connection.setDirectTpSduRef(value) is connection
        assert connection.getDirectTpSduRef() is value
        connection.setDirectTpSduRef(None)
        assert connection.getDirectTpSduRef() is value

    def test_get_set_multicast_ref(self):
        connection = FlexrayTpConnection()
        value = _ref("/TpConfigs/Addr", "TP-ADDRESS")
        assert connection.setMulticastRef(value) is connection
        assert connection.getMulticastRef() is value
        connection.setMulticastRef(None)
        assert connection.getMulticastRef() is value

    def test_add_get_receiver_refs(self):
        connection = FlexrayTpConnection()
        ref1 = _ref("/Nodes/Rx1", "FLEXRAY-TP-NODE")
        ref2 = _ref("/Nodes/Rx2", "FLEXRAY-TP-NODE")
        assert connection.addReceiverRef(ref1) is connection
        assert connection.getReceiverRefs() == [ref1]
        connection.addReceiverRef(ref2)
        assert connection.getReceiverRefs() == [ref1, ref2]
        connection.addReceiverRef(None)
        assert connection.getReceiverRefs() == [ref1, ref2]

    def test_get_set_reversed_tp_sdu_ref(self):
        connection = FlexrayTpConnection()
        value = _ref("/Pdus/Reversed", "I-PDU")
        assert connection.setReversedTpSduRef(value) is connection
        assert connection.getReversedTpSduRef() is value
        connection.setReversedTpSduRef(None)
        assert connection.getReversedTpSduRef() is value

    def test_get_set_rx_pdu_pool_ref(self):
        connection = FlexrayTpConnection()
        value = _ref("/PduPools/Rx", "FLEXRAY-TP-PDU-POOL")
        assert connection.setRxPduPoolRef(value) is connection
        assert connection.getRxPduPoolRef() is value
        connection.setRxPduPoolRef(None)
        assert connection.getRxPduPoolRef() is value

    def test_get_set_tp_connection_control_ref(self):
        connection = FlexrayTpConnection()
        value = _ref("/Controls/C1", "FLEXRAY-TP-CONNECTION-CONTROL")
        assert connection.setTpConnectionControlRef(value) is connection
        assert connection.getTpConnectionControlRef() is value
        connection.setTpConnectionControlRef(None)
        assert connection.getTpConnectionControlRef() is value

    def test_get_set_transmitter_ref(self):
        connection = FlexrayTpConnection()
        value = _ref("/Nodes/Tx", "FLEXRAY-TP-NODE")
        assert connection.setTransmitterRef(value) is connection
        assert connection.getTransmitterRef() is value
        connection.setTransmitterRef(None)
        assert connection.getTransmitterRef() is value

    def test_get_set_tx_pdu_pool_ref(self):
        connection = FlexrayTpConnection()
        value = _ref("/PduPools/Tx", "FLEXRAY-TP-PDU-POOL")
        assert connection.setTxPduPoolRef(value) is connection
        assert connection.getTxPduPoolRef() is value
        connection.setTxPduPoolRef(None)
        assert connection.getTxPduPoolRef() is value

    def test_type_hints_pins(self):
        for getter, setter in [
            ("getDirectTpSduRef", "setDirectTpSduRef"),
            ("getMulticastRef", "setMulticastRef"),
            ("getReversedTpSduRef", "setReversedTpSduRef"),
            ("getRxPduPoolRef", "setRxPduPoolRef"),
            ("getTpConnectionControlRef", "setTpConnectionControlRef"),
            ("getTransmitterRef", "setTransmitterRef"),
            ("getTxPduPoolRef", "setTxPduPoolRef"),
        ]:
            assert typing.get_type_hints(getattr(FlexrayTpConnection, getter)).get("return") == Optional[RefType]
            assert typing.get_type_hints(getattr(FlexrayTpConnection, setter)).get("value") == Optional[RefType]
            assert typing.get_type_hints(getattr(FlexrayTpConnection, setter)).get("return") is FlexrayTpConnection
        assert typing.get_type_hints(FlexrayTpConnection.getBandwidthLimitation).get("return") == Optional[Boolean]
        assert typing.get_type_hints(FlexrayTpConnection.setBandwidthLimitation).get("value") == Optional[Boolean]
        assert typing.get_type_hints(FlexrayTpConnection.setBandwidthLimitation).get("return") is FlexrayTpConnection
        assert typing.get_type_hints(FlexrayTpConnection.getReceiverRefs).get("return") == List[RefType]
        assert typing.get_type_hints(FlexrayTpConnection.addReceiverRef).get("value") == Optional[RefType]
        assert typing.get_type_hints(FlexrayTpConnection.addReceiverRef).get("return") is FlexrayTpConnection

    def test_ident_factory(self):
        connection = FlexrayTpConnection()
        ident = connection.createTpConnectionIdent("FrIdent")
        assert isinstance(ident, TpConnectionIdent)
        assert connection.getIdent() is ident
        assert connection.createTpConnectionIdent("other") is ident

    def test_variation_point_capable(self):
        connection = FlexrayTpConnection()
        assert connection.getVariationPoint() is None
