from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection import TpConnection
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import J1939TpConnection, J1939TpPg


class TestJ1939TpConnection:
    """Test class for J1939TpConnection (R23-11, Table 6.268, p.625)."""

    def test_initialization(self):
        """
        Test J1939TpConnection initialization and field defaults.
        """
        connection = J1939TpConnection()

        assert connection is not None
        assert isinstance(connection, TpConnection)

        assert connection.getBroadcast() is None
        assert connection.getBufferRatio() is None
        assert connection.getCancellation() is None
        assert connection.getDataPduRef() is None
        assert connection.getDynamicBs() is None
        assert connection.getFlowControlPduRefs() == []
        assert connection.getMaxBs() is None
        assert connection.getMaxExpBs() is None
        assert connection.getReceiverRefs() == []
        assert connection.getRetry() is None
        assert connection.getTpPgs() == []
        assert connection.getTransmitterRef() is None

    def test_get_set_broadcast(self):
        connection = J1939TpConnection()
        value = Boolean()
        value.setValue(True)

        result = connection.setBroadcast(value)
        assert result is connection
        assert connection.getBroadcast() is value
        connection.setBroadcast(None)
        assert connection.getBroadcast() is value

    def test_get_set_buffer_ratio(self):
        connection = J1939TpConnection()
        ratio = PositiveInteger()
        ratio.setValue("75")

        result = connection.setBufferRatio(ratio)
        assert result is connection
        assert connection.getBufferRatio() is ratio
        connection.setBufferRatio(None)
        assert connection.getBufferRatio() is ratio

    def test_get_set_cancellation(self):
        connection = J1939TpConnection()
        value = Boolean()
        value.setValue(True)

        result = connection.setCancellation(value)
        assert result is connection
        assert connection.getCancellation() is value
        connection.setCancellation(None)
        assert connection.getCancellation() is value

    def test_get_set_data_pdu_ref(self):
        connection = J1939TpConnection()
        ref = RefType()
        ref.setValue("/Pdus/DataPdu")

        result = connection.setDataPduRef(ref)
        assert result is connection
        assert connection.getDataPduRef() is ref
        connection.setDataPduRef(None)
        assert connection.getDataPduRef() is ref

    def test_get_set_dynamic_bs(self):
        connection = J1939TpConnection()
        value = Boolean()
        value.setValue(True)

        result = connection.setDynamicBs(value)
        assert result is connection
        assert connection.getDynamicBs() is value
        connection.setDynamicBs(None)
        assert connection.getDynamicBs() is value

    def test_flow_control_pdu_refs(self):
        connection = J1939TpConnection()
        ref1 = RefType()
        ref1.setValue("/Pdus/FlowControlPdu1")
        ref2 = RefType()
        ref2.setValue("/Pdus/FlowControlPdu2")

        result = connection.addFlowControlPduRef(ref1)
        assert result is connection
        assert ref1 in connection.getFlowControlPduRefs()
        connection.addFlowControlPduRef(ref2)
        assert len(connection.getFlowControlPduRefs()) == 2

        connection.addFlowControlPduRef(None)
        assert len(connection.getFlowControlPduRefs()) == 2

    def test_get_set_max_bs(self):
        connection = J1939TpConnection()
        value = PositiveInteger()
        value.setValue("8")

        result = connection.setMaxBs(value)
        assert result is connection
        assert connection.getMaxBs() is value
        connection.setMaxBs(None)
        assert connection.getMaxBs() is value

    def test_get_set_max_exp_bs(self):
        connection = J1939TpConnection()
        value = PositiveInteger()
        value.setValue("16")

        result = connection.setMaxExpBs(value)
        assert result is connection
        assert connection.getMaxExpBs() is value
        connection.setMaxExpBs(None)
        assert connection.getMaxExpBs() is value

    def test_receiver_refs(self):
        connection = J1939TpConnection()
        ref1 = RefType()
        ref1.setValue("/System/J1939TpConfig1/Node1")

        result = connection.addReceiverRef(ref1)
        assert result is connection
        assert ref1 in connection.getReceiverRefs()

        connection.addReceiverRef(None)
        assert len(connection.getReceiverRefs()) == 1

    def test_get_set_retry(self):
        connection = J1939TpConnection()
        value = Boolean()
        value.setValue(True)

        result = connection.setRetry(value)
        assert result is connection
        assert connection.getRetry() is value
        connection.setRetry(None)
        assert connection.getRetry() is value

    def test_tp_pgs(self):
        connection = J1939TpConnection()
        pg = J1939TpPg()

        result = connection.addTpPg(pg)
        assert result is connection
        assert pg in connection.getTpPgs()
        assert len(connection.getTpPgs()) == 1

        connection.addTpPg(None)
        assert len(connection.getTpPgs()) == 1

    def test_get_set_transmitter_ref(self):
        connection = J1939TpConnection()
        ref = RefType()
        ref.setValue("/System/J1939TpConfig1/Node0")

        result = connection.setTransmitterRef(ref)
        assert result is connection
        assert connection.getTransmitterRef() is ref
        connection.setTransmitterRef(None)
        assert connection.getTransmitterRef() is ref

    def test_ident(self):
        connection = J1939TpConnection()
        ident = connection.createTpConnectionIdent("Ident")

        assert connection.getIdent() is ident
        duplicate = connection.createTpConnectionIdent("Ident")
        assert duplicate is ident
