import typing
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall import PayloadBytePatternRule, PayloadBytePatternRulePart
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


def _part(offset=0, value=0):
    part = PayloadBytePatternRulePart()
    part.setOffset(_pos_int(offset))
    part.setValue(_pos_int(value))
    return part


def _pos_int(value):
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger

    p = PositiveInteger()
    p.setValue(value)
    return p


class TestPayloadBytePatternRule:
    def test_defaults(self):
        obj = PayloadBytePatternRule()
        assert isinstance(obj, ARObject)
        assert obj.getPayloadBytePatternRuleParts() == []

    def test_class_docstring_is_spec_note_verbatim(self):
        assert PayloadBytePatternRule.__doc__.strip() == "Configuration of a generic firewall rule that defines the individual bytes of a message that shall match. Tags: atp.Status=candidate"

    def test_add_part_round_trip_and_none_noop(self):
        obj = PayloadBytePatternRule()
        part = _part(0, 255)

        assert obj.addPayloadBytePatternRulePart(part) is obj
        assert obj.getPayloadBytePatternRuleParts() == [part]

        obj.addPayloadBytePatternRulePart(None)
        assert obj.getPayloadBytePatternRuleParts() == [part]

    def test_add_multiple_parts_in_order(self):
        obj = PayloadBytePatternRule()
        part1 = _part(0, 17)
        part2 = _part(1, 42)

        obj.addPayloadBytePatternRulePart(part1)
        obj.addPayloadBytePatternRulePart(part2)

        assert obj.getPayloadBytePatternRuleParts() == [part1, part2]

    def test_get_type_hints_pins(self):
        hints = typing.get_type_hints(PayloadBytePatternRule.addPayloadBytePatternRulePart)
        assert hints["return"] is PayloadBytePatternRule
        assert hints["value"] == Optional[PayloadBytePatternRulePart]
