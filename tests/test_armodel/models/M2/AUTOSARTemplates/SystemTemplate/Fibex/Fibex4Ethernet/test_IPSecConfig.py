import inspect

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    IPSecConfig,
    RefType,
)

CLASS_NOTE = """IPsec is a protocol that is designed to provide "end-to-end" cryptographically-based security for IP network connections."""


class TestIPSecConfig:
    """Test cases for IPSecConfig (Table 6.221, p.571)."""

    def _obj(self):
        return IPSecConfig()

    def test_initialization_defaults(self):
        obj = self._obj()
        assert obj.getIpSecConfigPropsRef() is None

    def test_setters_round_trip_and_none_noop(self):
        obj = self._obj()
        item = RefType()
        assert obj.setIpSecConfigPropsRef(item) is obj
        assert obj.getIpSecConfigPropsRef() is item
        obj.setIpSecConfigPropsRef(None)
        assert obj.getIpSecConfigPropsRef() is item

    def test_class_docstring_note(self):
        assert inspect.cleandoc(IPSecConfig.__doc__).split("\n\n")[0] == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        obj = self._obj()
        assert inspect.cleandoc(obj.getIpSecConfigPropsRef.__doc__) == "Global IPsec configuration settings that are valid for all IPSecRules that are defined on the NetworkEndpoint."
        assert inspect.cleandoc(obj.setIpSecConfigPropsRef.__doc__).split("\n")[0] == "Global IPsec configuration settings that are valid for all IPSecRules that are defined on the NetworkEndpoint."
