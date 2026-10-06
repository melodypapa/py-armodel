import inspect

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    SwitchStreamFilterActionPortModificationEnum,
)

CLASS_NOTE = "Definition how the SwitchStreamFilterActionPortModification is applied. Tags: atp.Status=candidate"


class TestSwitchStreamFilterActionPortModificationEnum:
    """Test cases for SwitchStreamFilterActionPortModificationEnum (CP_TPS_SystemTemplate Table 3.94, p.140, R23-11)."""

    def test_member_presence_and_values(self):
        assert SwitchStreamFilterActionPortModificationEnum.EXTEND == "EXTEND"
        assert SwitchStreamFilterActionPortModificationEnum.OVERWRITE == "OVERWRITE"
        assert list(SwitchStreamFilterActionPortModificationEnum().getEnumValues()) == ["EXTEND", "OVERWRITE"]

    def test_instantiability_round_trip(self):
        extend = SwitchStreamFilterActionPortModificationEnum().setValue(SwitchStreamFilterActionPortModificationEnum.EXTEND)
        assert extend.getValue() == SwitchStreamFilterActionPortModificationEnum.EXTEND

        overwrite = SwitchStreamFilterActionPortModificationEnum().setValue(SwitchStreamFilterActionPortModificationEnum.OVERWRITE)
        assert overwrite.getValue() == SwitchStreamFilterActionPortModificationEnum.OVERWRITE

    def test_class_docstring_note(self):
        assert inspect.cleandoc(SwitchStreamFilterActionPortModificationEnum.__doc__) == CLASS_NOTE
