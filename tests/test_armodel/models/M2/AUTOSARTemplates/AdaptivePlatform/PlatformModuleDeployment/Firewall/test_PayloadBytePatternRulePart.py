import inspect
import typing
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall import PayloadBytePatternRulePart
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger


def _pos_int(value):
    p = PositiveInteger()
    p.setValue(value)
    return p


class TestPayloadBytePatternRulePart:
    def test_defaults_in_spec_displayed_order(self):
        obj = PayloadBytePatternRulePart()
        assert isinstance(obj, ARObject)
        assert obj.getOffset() is None
        assert obj.getValue() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        assert PayloadBytePatternRulePart.__doc__.strip() == "Configuration of one byte in the datagram, Tags: atp.Status=candidate"

    def test_get_set_round_trip_and_none_noop(self):
        obj = PayloadBytePatternRulePart()
        offset = _pos_int(34)
        value = _pos_int(255)

        assert obj.setOffset(offset) is obj
        assert obj.setValue(value) is obj

        assert obj.getOffset() is offset
        assert obj.getValue() is value

        obj.setOffset(None)
        obj.setValue(None)
        assert obj.getOffset() is offset
        assert obj.getValue() is value

    def test_docstrings_are_spec_note_verbatim(self):
        offset_note = "This attribute defines the byte offset in the datagram (start byte of the Ethernet frame, i.e. offset 0 corresponds to the first byte of the destination MAC address)."
        assert inspect.cleandoc(PayloadBytePatternRulePart.getOffset.__doc__) == offset_note
        assert inspect.cleandoc(PayloadBytePatternRulePart.setOffset.__doc__) == offset_note + "\nA None value is a no-op and does not overwrite an existing offset."
        value_note = "This attribute defines the byteValue (0..255) in the datagram."
        assert inspect.cleandoc(PayloadBytePatternRulePart.getValue.__doc__) == value_note
        assert inspect.cleandoc(PayloadBytePatternRulePart.setValue.__doc__) == value_note + "\nA None value is a no-op and does not overwrite an existing value."

    def test_get_type_hints_pins(self):
        hints = typing.get_type_hints(PayloadBytePatternRulePart.setOffset)
        assert hints["return"] is PayloadBytePatternRulePart
        assert hints["value"] == Optional[PositiveInteger]
        hints = typing.get_type_hints(PayloadBytePatternRulePart.setValue)
        assert hints["return"] is PayloadBytePatternRulePart
        assert hints["value"] == Optional[PositiveInteger]
