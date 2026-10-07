import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    RtpTp,
    TcpTp,
    UdpTp,
)

CLASS_NOTE = "RTP over UDP or over TCP as transport protocol."


class TestRtpTp:
    """Test cases for RtpTp (Table 6.130, p.460)."""

    def _obj(self):
        return RtpTp()

    def test_initialization_defaults(self):
        obj = self._obj()
        assert obj.getSsrc() is None
        assert obj.getTcpUdpConfig() is None

    def test_get_set_ssrc(self):
        obj = self._obj()
        value = PositiveInteger().setValue("1234")
        assert obj.setSsrc(value) is obj
        assert obj.getSsrc() is value
        assert obj.getSsrc().getValue() == 1234
        obj.setSsrc(None)
        assert obj.getSsrc() is value

    def test_get_set_tcp_udp_config_udp_tp(self):
        obj = self._obj()
        value = UdpTp()
        assert obj.setTcpUdpConfig(value) is obj
        assert obj.getTcpUdpConfig() is value
        obj.setTcpUdpConfig(None)
        assert obj.getTcpUdpConfig() is value

    def test_get_set_tcp_udp_config_tcp_tp(self):
        obj = self._obj()
        value = TcpTp()
        assert obj.setTcpUdpConfig(value) is obj
        assert obj.getTcpUdpConfig() is value

    def test_class_docstring_note(self):
        assert inspect.cleandoc(RtpTp.__doc__) == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        obj = self._obj()
        assert (
            inspect.cleandoc(obj.getSsrc.__doc__)
            == "Synchronization source identifier uniquely identifies the source of a stream. The synchronization sources within the same RTP session will be unique."
        )
        assert (
            inspect.cleandoc(obj.setSsrc.__doc__).split("\n")[0]
            == "Synchronization source identifier uniquely identifies the source of a stream. The synchronization sources within the same RTP session will be unique."
        )
        assert inspect.cleandoc(obj.getTcpUdpConfig.__doc__) == "Tcp or Udp Configuration."
        assert inspect.cleandoc(obj.setTcpUdpConfig.__doc__).split("\n")[0] == "Tcp or Udp Configuration."
