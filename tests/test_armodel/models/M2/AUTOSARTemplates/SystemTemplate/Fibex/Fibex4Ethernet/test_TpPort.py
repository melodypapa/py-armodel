import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    TpPort,
)

CLASS_NOTE = """Dynamic or direct assignment of a PortNumber."""


class TestTpPort:
    """Test cases for TpPort (Table 6.133, p.461)."""

    def _obj(self):
        return TpPort()

    def test_initialization_defaults(self):
        obj = self._obj()
        assert obj.getDynamicallyAssigned() is None
        assert obj.getPortNumber() is None

    def test_setters_round_trip_and_none_noop(self):
        obj = self._obj()
        item = Boolean()
        assert obj.setDynamicallyAssigned(item) is obj
        assert obj.getDynamicallyAssigned() is item
        obj.setDynamicallyAssigned(None)
        assert obj.getDynamicallyAssigned() is item
        number = PositiveInteger().setValue("7")
        assert obj.setPortNumber(number) is obj
        assert obj.getPortNumber() is number
        obj.setPortNumber(None)
        assert obj.getPortNumber() is number

    def test_class_docstring_note(self):
        assert inspect.cleandoc(TpPort.__doc__).split("\n\n")[0] == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        obj = self._obj()
        assert inspect.cleandoc(obj.getDynamicallyAssigned.__doc__) == "Indicates whether the source port is dynamically assigned. Tags: atp.Status=obsolete"
        assert inspect.cleandoc(obj.setDynamicallyAssigned.__doc__).split("\n")[0] == "Indicates whether the source port is dynamically assigned. Tags: atp.Status=obsolete"
        assert inspect.cleandoc(obj.getPortNumber.__doc__) == "Port Number."
        assert inspect.cleandoc(obj.setPortNumber.__doc__).split("\n")[0] == "Port Number."
