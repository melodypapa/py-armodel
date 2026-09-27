import inspect

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    DoIpEntity,
    DoIpEntityRoleEnum,
)

CLASS_NOTE = """ECU providing this infrastructure service is a DoIP-Entity."""


class TestDoIpEntity:
    """Test cases for DoIpEntity (Table 6.150, p.471)."""

    def _obj(self):
        return DoIpEntity()

    def test_initialization_defaults(self):
        obj = self._obj()
        assert obj.getDoIpEntityRole() is None

    def test_setters_round_trip_and_none_noop(self):
        obj = self._obj()
        item = DoIpEntityRoleEnum()
        assert obj.setDoIpEntityRole(item) is obj
        assert obj.getDoIpEntityRole() is item
        obj.setDoIpEntityRole(None)
        assert obj.getDoIpEntityRole() is item

    def test_class_docstring_note(self):
        assert inspect.cleandoc(DoIpEntity.__doc__).split("\n\n")[0] == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        obj = self._obj()
        assert inspect.cleandoc(obj.getDoIpEntityRole.__doc__) == "Identifies the role in terms of DoIP this network-node has."
        assert inspect.cleandoc(obj.setDoIpEntityRole.__doc__).split("\n")[0] == "Identifies the role in terms of DoIP this network-node has."
