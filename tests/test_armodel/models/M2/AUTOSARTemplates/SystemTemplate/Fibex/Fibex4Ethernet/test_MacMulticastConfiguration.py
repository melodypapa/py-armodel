import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    MacMulticastConfiguration,
    NetworkEndpointAddress,
)

CLASS_NOTE = "References a per cluster globally defined MAC-Multicast-Group."


class TestMacMulticastConfiguration:
    """Test cases for MacMulticastConfiguration (Table 6.141, p.467)."""

    def _obj(self):
        return MacMulticastConfiguration()

    def test_initialization_defaults(self):
        obj = self._obj()
        assert obj.getMacMulticastGroupRef() is None

    def test_get_set_mac_multicast_group_ref(self):
        obj = self._obj()
        value = RefType()
        value.setValue("/EthernetCluster/Group")
        assert obj.setMacMulticastGroupRef(value) is obj
        assert obj.getMacMulticastGroupRef() is value
        assert obj.getMacMulticastGroupRef().getValue() == "/EthernetCluster/Group"
        obj.setMacMulticastGroupRef(None)
        assert obj.getMacMulticastGroupRef() is value

    def test_inheritance(self):
        obj = self._obj()
        assert isinstance(obj, NetworkEndpointAddress)
        assert isinstance(obj, ARObject)

    def test_class_docstring_note(self):
        assert inspect.cleandoc(MacMulticastConfiguration.__doc__) == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        obj = self._obj()
        assert inspect.cleandoc(obj.getMacMulticastGroupRef.__doc__) == "Reference to a macMulticastGroup."
        assert inspect.cleandoc(obj.setMacMulticastGroupRef.__doc__).split("\n")[0] == "Reference to a macMulticastGroup."
