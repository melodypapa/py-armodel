import inspect

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    GenericTp,
    String,
)

CLASS_NOTE = """Content Model for a generic transport protocol."""


class TestGenericTp:
    """Test cases for GenericTp (Table 6.126, p.459)."""

    def _obj(self):
        return GenericTp(None, "Obj")

    def test_initialization_defaults(self):
        obj = self._obj()
        assert obj.getTpAddress() is None
        assert obj.getTpTechnology() is None

    def test_setters_round_trip_and_none_noop(self):
        obj = self._obj()
        item = String()
        assert obj.setTpAddress(item) is obj
        assert obj.getTpAddress() is item
        obj.setTpAddress(None)
        assert obj.getTpAddress() is item
        item = String()
        assert obj.setTpTechnology(item) is obj
        assert obj.getTpTechnology() is item
        obj.setTpTechnology(None)
        assert obj.getTpTechnology() is item

    def test_class_docstring_note(self):
        assert inspect.cleandoc(GenericTp.__doc__).split("\n\n")[0] == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        obj = self._obj()
        assert inspect.cleandoc(obj.getTpAddress.__doc__) == "Transport Protocol dependent Address."
        assert inspect.cleandoc(obj.setTpAddress.__doc__).split("\n")[0] == "Transport Protocol dependent Address."
        assert inspect.cleandoc(obj.getTpTechnology.__doc__) == "Name of the used Transport Protocol."
        assert inspect.cleandoc(obj.setTpTechnology.__doc__).split("\n")[0] == "Name of the used Transport Protocol."
