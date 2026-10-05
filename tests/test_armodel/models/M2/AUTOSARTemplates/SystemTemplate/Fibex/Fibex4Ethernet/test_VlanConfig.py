import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    VlanConfig,
)

CLASS_NOTE = """VLAN Configuration attributes"""


class TestVlanConfig:
    """Test cases for VlanConfig (Table 3.50, p.106)."""

    def _obj(self):
        return VlanConfig(None, "Obj")

    def test_initialization_defaults(self):
        obj = self._obj()
        assert obj.getVlanIdentifier() is None

    def test_setters_round_trip_and_none_noop(self):
        obj = self._obj()
        value = PositiveInteger().setValue("7")
        assert obj.setVlanIdentifier(value) is obj
        assert obj.getVlanIdentifier() is value
        obj.setVlanIdentifier(None)
        assert obj.getVlanIdentifier() is value

    def test_class_docstring_note(self):
        assert inspect.cleandoc(VlanConfig.__doc__).split("\n\n")[0] == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        obj = self._obj()
        assert inspect.cleandoc(obj.getVlanIdentifier.__doc__) == "A VLAN is identified by this attribute according to IEEE 802.1Q. The allowed values range is from 0..4095."
        assert inspect.cleandoc(obj.setVlanIdentifier.__doc__).split("\n")[0] == "A VLAN is identified by this attribute according to IEEE 802.1Q. The allowed values range is from 0..4095."
