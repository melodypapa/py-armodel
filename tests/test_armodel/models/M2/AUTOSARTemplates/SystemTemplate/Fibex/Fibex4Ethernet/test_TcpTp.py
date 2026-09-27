import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    TcpTp,
    TpPort,
)

CLASS_NOTE = """Content Model for TCP configuration."""


class TestTcpTp:
    """Test cases for TcpTp (Table 6.129, p.460)."""

    def _obj(self):
        return TcpTp(None, "Obj")

    def test_initialization_defaults(self):
        obj = self._obj()
        assert obj.getKeepAliveInterval() is None
        assert obj.getKeepAliveProbesMax() is None
        assert obj.getKeepAlives() is None
        assert obj.getKeepAliveTime() is None
        assert obj.getNaglesAlgorithm() is None
        assert obj.getReceiveWindowMin() is None
        assert obj.getTcpRetransmissionTimeout() is None
        assert obj.getTcpTpPort() is None

    def test_setters_round_trip_and_none_noop(self):
        obj = self._obj()
        item = TimeValue()
        assert obj.setKeepAliveInterval(item) is obj
        assert obj.getKeepAliveInterval() is item
        obj.setKeepAliveInterval(None)
        assert obj.getKeepAliveInterval() is item
        assert obj.setKeepAliveProbesMax(7) is obj
        assert obj.getKeepAliveProbesMax() == 7
        obj.setKeepAliveProbesMax(None)
        assert obj.getKeepAliveProbesMax() == 7
        flag = Boolean()
        flag.setValue(True)
        assert obj.setKeepAlives(flag) is obj
        assert obj.getKeepAlives() is flag
        obj.setKeepAlives(None)
        assert obj.getKeepAlives() is flag
        item = TimeValue()
        assert obj.setKeepAliveTime(item) is obj
        assert obj.getKeepAliveTime() is item
        obj.setKeepAliveTime(None)
        assert obj.getKeepAliveTime() is item
        flag = Boolean()
        flag.setValue(True)
        assert obj.setNaglesAlgorithm(flag) is obj
        assert obj.getNaglesAlgorithm() is flag
        obj.setNaglesAlgorithm(None)
        assert obj.getNaglesAlgorithm() is flag
        assert obj.setReceiveWindowMin(7) is obj
        assert obj.getReceiveWindowMin() == 7
        obj.setReceiveWindowMin(None)
        assert obj.getReceiveWindowMin() == 7
        item = TimeValue()
        assert obj.setTcpRetransmissionTimeout(item) is obj
        assert obj.getTcpRetransmissionTimeout() is item
        obj.setTcpRetransmissionTimeout(None)
        assert obj.getTcpRetransmissionTimeout() is item
        item = TpPort()
        assert obj.setTcpTpPort(item) is obj
        assert obj.getTcpTpPort() is item
        obj.setTcpTpPort(None)
        assert obj.getTcpTpPort() is item

    def test_class_docstring_note(self):
        assert inspect.cleandoc(TcpTp.__doc__).split("\n\n")[0] == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        obj = self._obj()
        assert inspect.cleandoc(obj.getKeepAliveInterval.__doc__) == "Specifies the interval in seconds between subsequent keepalive probes."
        assert inspect.cleandoc(obj.setKeepAliveInterval.__doc__).split("\n")[0] == "Specifies the interval in seconds between subsequent keepalive probes."
        assert inspect.cleandoc(obj.getKeepAliveProbesMax.__doc__) == "Maximum number of times that TCP retransmits an individual data segment before aborting the connection."
        assert inspect.cleandoc(obj.setKeepAliveProbesMax.__doc__).split("\n")[0] == "Maximum number of times that TCP retransmits an individual data segment before aborting the connection."
        assert inspect.cleandoc(obj.getKeepAlives.__doc__) == "Indicates if Keep-Alive messages are sent."
        assert inspect.cleandoc(obj.setKeepAlives.__doc__).split("\n")[0] == "Indicates if Keep-Alive messages are sent."
        assert inspect.cleandoc(obj.getKeepAliveTime.__doc__) == "Specifies the time in seconds between the last data packet sent and the first keepalive probe."
        assert inspect.cleandoc(obj.setKeepAliveTime.__doc__).split("\n")[0] == "Specifies the time in seconds between the last data packet sent and the first keepalive probe."
        assert inspect.cleandoc(obj.getNaglesAlgorithm.__doc__) == "Indicates if Nagle's Algorithm is used."
        assert inspect.cleandoc(obj.setNaglesAlgorithm.__doc__).split("\n")[0] == "Indicates if Nagle's Algorithm is used."
        assert inspect.cleandoc(obj.getReceiveWindowMin.__doc__) == "Minimum size of the TCP receive window in bytes."
        assert inspect.cleandoc(obj.setReceiveWindowMin.__doc__).split("\n")[0] == "Minimum size of the TCP receive window in bytes."
        assert (
            inspect.cleandoc(obj.getTcpRetransmissionTimeout.__doc__)
            == 'Defines the timeout in seconds before an unacknowledged TCP segment is sent again. If the tcp RetransmissionTimeout is not defined or set to "INF", no TCP segments shall be re-transmitted.'
        )
        assert (
            inspect.cleandoc(obj.setTcpRetransmissionTimeout.__doc__).split("\n")[0]
            == 'Defines the timeout in seconds before an unacknowledged TCP segment is sent again. If the tcp RetransmissionTimeout is not defined or set to "INF", no TCP segments shall be re-transmitted.'
        )
        assert inspect.cleandoc(obj.getTcpTpPort.__doc__) == "TCP Port configuration."
        assert inspect.cleandoc(obj.setTcpTpPort.__doc__).split("\n")[0] == "TCP Port configuration."
