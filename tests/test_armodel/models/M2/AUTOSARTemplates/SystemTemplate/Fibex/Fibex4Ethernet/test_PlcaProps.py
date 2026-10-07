"""Model tests for PlcaProps (R23-11 CP_TPS_SystemTemplate, Table 3.117, p.169)."""

import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import PlcaProps

CLASS_NOTE = "This meta-class allows to configure the PLCA (Physical Layer Collision Avoidance) in case 10-BASE-T1S Ethernet is used and PLCA is enabled on the CouplingPort (PHY)."

MEMBER_NOTES = {
    "plcaLocalNodeId": "This attribute defines the node ID when the PLCA mode for 10BASE-T1S is used.",
    "plcaMaxBurstCount": "Defines maximum packets allowed to be transmitted within a TO. This configuration can be different from one ECU to another within the PLCA mixed segment.",
    "plcaMaxBurstTimer": "Limits the burst frames in bit time. This configuration can be different from one ECU to another within the PLCA mixed segment. For PLCA burst mode to work properly this timer should be set greater than one IPG.",
}

MEMBERS = [
    "plcaLocalNodeId",
    "plcaMaxBurstCount",
    "plcaMaxBurstTimer",
]


class TestPlcaProps:
    """Spec-sync tests for PlcaProps (Table 3.117, p.169)."""

    def _make(self) -> PlcaProps:
        return PlcaProps()

    def _value(self, member):
        value = PositiveInteger()
        value.setValue("4")
        return value

    def test_inheritance(self):
        assert issubclass(PlcaProps, ARObject)

    def test_initialization_defaults(self):
        obj = self._make()
        for member in MEMBERS:
            assert getattr(obj, "get%s%s" % (member[0].upper(), member[1:]))() is None

    def test_get_set_round_trip_and_none_noop(self):
        obj = self._make()
        for member in MEMBERS:
            getter = getattr(obj, "get%s%s" % (member[0].upper(), member[1:]))
            setter = getattr(obj, "set%s%s" % (member[0].upper(), member[1:]))
            value = self._value(member)
            assert setter(value) is obj
            assert getter() is value
            setter(None)
            assert getter() is value

    def test_member_order_matches_spec(self):
        source = inspect.getsource(PlcaProps.__init__)
        indexes = [source.index("self.%s:" % member) for member in MEMBERS]
        assert indexes == sorted(indexes)

    def test_class_docstring_is_spec_note(self):
        assert PlcaProps.__doc__.strip() == CLASS_NOTE

    def test_init_has_no_docstring(self):
        assert PlcaProps.__init__.__doc__ is None

    def test_accessor_docstrings_are_spec_notes(self):
        obj = self._make()
        for member in MEMBERS:
            getter = getattr(obj, "get%s%s" % (member[0].upper(), member[1:]))
            setter = getattr(obj, "set%s%s" % (member[0].upper(), member[1:]))
            noop = "A None value is a no-op and does not overwrite an existing %s." % member
            assert getter.__doc__.strip() == MEMBER_NOTES[member], member
            assert inspect.cleandoc(setter.__doc__).strip() == MEMBER_NOTES[member] + "\n\n" + noop, member
