import inspect

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    TpPort,
    UdpTp,
)

CLASS_NOTE = """Content Model for UDP configuration."""


class TestUdpTp:
    """Test cases for UdpTp (Table 6.128, p.459)."""

    def _obj(self):
        return UdpTp()

    def test_initialization_defaults(self):
        obj = self._obj()
        assert obj.getUdpTpPort() is None

    def test_setters_round_trip_and_none_noop(self):
        obj = self._obj()
        item = TpPort()
        assert obj.setUdpTpPort(item) is obj
        assert obj.getUdpTpPort() is item
        obj.setUdpTpPort(None)
        assert obj.getUdpTpPort() is item

    def test_class_docstring_note(self):
        assert inspect.cleandoc(UdpTp.__doc__).split("\n\n")[0] == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        obj = self._obj()
        assert inspect.cleandoc(obj.getUdpTpPort.__doc__) == "Udp Port configuration."
        assert inspect.cleandoc(obj.setUdpTpPort.__doc__).split("\n")[0] == "Udp Port configuration."
