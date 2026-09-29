import typing
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection import TpConnection, TpConnectionIdent
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import LinTpConnection


def _ref(value, dest):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _time(value):
    time_value = TimeValue()
    time_value.setValue(value)
    return time_value


class Test_LinTpConnection:
    # Table 6.261, p.616 — attribute Notes verbatim from the markdown
    NOTE_DATA_PDU = (
        "Reference to an NPdu (Single Frame, First Frame or Consecutive Frame). "
        "The Single Frame network protocol data unit (SF N_PDU) shall be sent out by the sending network entity and can be received by one or multiple receiving network entities. "
        "The Single Frame (SF N_PDU) shall be sent out to transfer a service data unit that can be transferred via a single service request to the data link layer. This network protocol data unit shall be sent to transfer unsegmented messages. "
        "The First Frame network protocol data unit (FF N_PDU) identifies the first network protocol data unit (N_PDU) of a segmented message transmitted by a network sending entity and received by a receiving network entity. "
        "The Consecutive Frame network protocol data unit (CF N_PDU) transfers segments (N_Data) of the service data unit message data (<MessageData>). "
        "All network protocol data units (N_PDUs) transmitted by the sending entity after the First Frame network protocol data unit (FF N_PDU) shall be encoded as Consecutive Frames network protocol data units (CF N_PDUs)."
    )
    NOTE_FLOW_CONTROL = (
        "Reference to the Flow Control NPdu. "
        "The Flow Control network protocol data unit (FC N_PDU) is identified by the Flow Control protocol control information (FC N_PCI). "
        "The Flow Control network protocol data unit (FC N_PDU) instructs a sending network entity to start, stop or resume transmission of CF N_PDUs. "
        "The Flow Control network protocol data unit shall be sent by the receiving network layer entity to the sending network layer entity, when ready to receive more data, after correct reception of: "
        "a) First Frame network protocol data unit (FF N_PDU) "
        "b) the last Consecutive Frame network protocol data unit (CF N_PDU) of a block of Consecutive Frames (CF N_ PDU) if further Consecutive Frame network protocol data unit (CF N_PDU) need(s) to be sent."
    )
    NOTE_LIN_TP_NSDU = "Reference to the IPdu that is segmented by the Transport Protocol."
    NOTE_MULTICAST = "TP address for 1:n connections."
    NOTE_RECEIVER = "The target of the TP connection."
    NOTE_TIMEOUT_AS = "Time for transmission of the LIN frame (any N-PDU) on the sender side. Specified in seconds."
    NOTE_TIMEOUT_CR = (
        "This attribute defines the timeout value for waiting for a CF or FF-x (in case of retry) after receiving the last CF or after sending an FC or AF on the receiver side. Specified in seconds."
    )
    NOTE_TIMEOUT_CS = "The attribute timeoutCs represents the time (in seconds) which elapses between the transmit request of a CF N-PDU until the transmit request of the next CF N-PDU."
    NOTE_TRANSMITTER = "The source of the TP connection."

    def test_docstring_is_spec_note_verbatim(self):
        # Table 6.261, p.616 — class Note verbatim from the markdown + table constraints appended
        note = (
            "A LinTP channel represents an internal path for the transmission or reception of a Pdu via LinTp "
            "and describes the sender and the receiver of this particular communication. "
            "LinTp supports (per Lin Cluster) the configuration of one Rx Tp-SDU and one Tx Tp-SDU per NAD "
            "the LinMaster uses to address one or more of its Lin Slaves. "
            "To support this an arbitrary number of LinTp Connections shall be described."
        )
        constrs = [
            "[constr_9260] Existence of LinTpConnection.dataPdu: For each LinTpConnection, the reference to NPdu in the role dataPdu shall exist at the time when the System Description is complete.",
            "[constr_9261] Existence of LinTpConnection.linTpNSdu: For each LinTpConnection, the reference to IPdu in the role linTpNSdu shall exist at the time when the System Description is complete.",
            "[constr_9262] Existence of LinTpConnection.receiver: For each LinTpConnection, at least one reference to LinTpNode in the role receiver shall exist at the time when the System Description is complete.",
            "[constr_9263] Existence of LinTpConnection.transmitter: For each LinTpConnection, the reference to LinTpNode in the role transmitter shall exist at the time when the System Description is complete.",
            "[constr_5377] IPdu shall only be referenced once from a LinTpConnection in the role linTpNSdu on a LinCluster: "
            "Each IPdu that is referenced in the role linTpNSdu from a LinTpConnection that is aggregated by a LinTpConfig that references a LinCluster "
            "shall not be referenced in the role linTpNSdu from a different LinTpConnection that is aggregated by a LinTpConfig that references the same LinCluster.",
        ]
        expected = note + "\n\n" + "\n\n".join(constrs)
        assert LinTpConnection.__doc__.strip() == expected

    def test_init_has_no_docstring(self):
        assert LinTpConnection.__init__.__doc__ is None

    def test_heritage(self):
        connection = LinTpConnection()
        assert isinstance(connection, TpConnection)
        assert connection.getIdent() is None

    def test_initialization(self):
        # spec displayed order: dataPdu, flowControl, linTpNSdu, multicast, receiver `*`,
        # timeoutAs, timeoutCr, timeoutCs, transmitter
        connection = LinTpConnection()
        assert connection.getDataPduRef() is None
        assert connection.getFlowControlRef() is None
        assert connection.getLinTpNSduRef() is None
        assert connection.getMulticastRef() is None
        assert connection.getReceiverRefs() == []
        assert connection.getTimeoutAs() is None
        assert connection.getTimeoutCr() is None
        assert connection.getTimeoutCs() is None
        assert connection.getTransmitterRef() is None

    def test_get_set_data_pdu_ref(self):
        connection = LinTpConnection()
        value = _ref("/Pdus/Data", "N-PDU")
        assert connection.setDataPduRef(value) is connection
        assert connection.getDataPduRef() is value
        connection.setDataPduRef(None)
        assert connection.getDataPduRef() is value

    def test_get_set_flow_control_ref(self):
        connection = LinTpConnection()
        value = _ref("/Pdus/FlowControl", "N-PDU")
        assert connection.setFlowControlRef(value) is connection
        assert connection.getFlowControlRef() is value
        connection.setFlowControlRef(None)
        assert connection.getFlowControlRef() is value

    def test_get_set_lin_tp_n_sdu_ref(self):
        connection = LinTpConnection()
        value = _ref("/Pdus/NSdu", "I-PDU")
        assert connection.setLinTpNSduRef(value) is connection
        assert connection.getLinTpNSduRef() is value
        connection.setLinTpNSduRef(None)
        assert connection.getLinTpNSduRef() is value

    def test_get_set_multicast_ref(self):
        connection = LinTpConnection()
        value = _ref("/TpConfigs/Addr", "TP-ADDRESS")
        assert connection.setMulticastRef(value) is connection
        assert connection.getMulticastRef() is value
        connection.setMulticastRef(None)
        assert connection.getMulticastRef() is value

    def test_add_get_receiver_refs(self):
        connection = LinTpConnection()
        ref1 = _ref("/Nodes/Rx1", "LIN-TP-NODE")
        ref2 = _ref("/Nodes/Rx2", "LIN-TP-NODE")
        assert connection.addReceiverRef(ref1) is connection
        assert connection.getReceiverRefs() == [ref1]
        connection.addReceiverRef(ref2)
        assert connection.getReceiverRefs() == [ref1, ref2]
        connection.addReceiverRef(None)
        assert connection.getReceiverRefs() == [ref1, ref2]

    def test_get_set_timeout_as(self):
        connection = LinTpConnection()
        value = _time("0.1")
        assert connection.setTimeoutAs(value) is connection
        assert connection.getTimeoutAs() is value
        connection.setTimeoutAs(None)
        assert connection.getTimeoutAs() is value

    def test_get_set_timeout_cr(self):
        connection = LinTpConnection()
        value = _time("1.5")
        assert connection.setTimeoutCr(value) is connection
        assert connection.getTimeoutCr() is value
        connection.setTimeoutCr(None)
        assert connection.getTimeoutCr() is value

    def test_get_set_timeout_cs(self):
        connection = LinTpConnection()
        value = _time("0.05")
        assert connection.setTimeoutCs(value) is connection
        assert connection.getTimeoutCs() is value
        connection.setTimeoutCs(None)
        assert connection.getTimeoutCs() is value

    def test_get_set_transmitter_ref(self):
        connection = LinTpConnection()
        value = _ref("/Nodes/Tx", "LIN-TP-NODE")
        assert connection.setTransmitterRef(value) is connection
        assert connection.getTransmitterRef() is value
        connection.setTransmitterRef(None)
        assert connection.getTransmitterRef() is value

    def test_type_hints_pins(self):
        for getter, setter in [
            ("getDataPduRef", "setDataPduRef"),
            ("getFlowControlRef", "setFlowControlRef"),
            ("getLinTpNSduRef", "setLinTpNSduRef"),
            ("getMulticastRef", "setMulticastRef"),
            ("getTransmitterRef", "setTransmitterRef"),
        ]:
            assert typing.get_type_hints(getattr(LinTpConnection, getter)).get("return") == Optional[RefType]
            assert typing.get_type_hints(getattr(LinTpConnection, setter)).get("value") == Optional[RefType]
            assert typing.get_type_hints(getattr(LinTpConnection, setter)).get("return") is LinTpConnection
        for getter, setter in [
            ("getTimeoutAs", "setTimeoutAs"),
            ("getTimeoutCr", "setTimeoutCr"),
            ("getTimeoutCs", "setTimeoutCs"),
        ]:
            assert typing.get_type_hints(getattr(LinTpConnection, getter)).get("return") == Optional[TimeValue]
            assert typing.get_type_hints(getattr(LinTpConnection, setter)).get("value") == Optional[TimeValue]
            assert typing.get_type_hints(getattr(LinTpConnection, setter)).get("return") is LinTpConnection
        assert typing.get_type_hints(LinTpConnection.getReceiverRefs).get("return") == List[RefType]
        assert typing.get_type_hints(LinTpConnection.addReceiverRef).get("value") == Optional[RefType]
        assert typing.get_type_hints(LinTpConnection.addReceiverRef).get("return") is LinTpConnection

    def test_ident_factory(self):
        connection = LinTpConnection()
        ident = connection.createTpConnectionIdent("LinIdent")
        assert isinstance(ident, TpConnectionIdent)
        assert connection.getIdent() is ident
        assert connection.createTpConnectionIdent("LinIdent") is ident

    def test_variation_point_capable(self):
        connection = LinTpConnection()
        assert hasattr(connection, "getVariationPoint")
