import inspect

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    MacAddressString,
    MacMulticastGroup,
)

CLASS_NOTE = """Per EthernetCluster globally defined MacMulticastGroup. One sender can handle many receivers simultaneously if the receivers have all the same macMulticastAddress. The addresses need to be unique for the particular EthernetCluster."""


class TestMacMulticastGroup:
    """Test cases for MacMulticastGroup (Table 3.48, p.104)."""

    def _obj(self):
        return MacMulticastGroup(None, "Obj")

    def test_initialization_defaults(self):
        obj = self._obj()
        assert obj.getMacMulticastAddress() is None

    def test_setters_round_trip_and_none_noop(self):
        obj = self._obj()
        item = MacAddressString()
        assert obj.setMacMulticastAddress(item) is obj
        assert obj.getMacMulticastAddress() is item
        obj.setMacMulticastAddress(None)
        assert obj.getMacMulticastAddress() is item

    def test_class_docstring_note(self):
        assert inspect.cleandoc(MacMulticastGroup.__doc__).split("\n\n")[0] == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        obj = self._obj()
        assert inspect.cleandoc(obj.getMacMulticastAddress.__doc__) == "A multicast MAC address (Media Access Control address) is a identifier for a group of hosts in a network."
        assert inspect.cleandoc(obj.setMacMulticastAddress.__doc__).split("\n")[0] == "A multicast MAC address (Media Access Control address) is a identifier for a group of hosts in a network."
