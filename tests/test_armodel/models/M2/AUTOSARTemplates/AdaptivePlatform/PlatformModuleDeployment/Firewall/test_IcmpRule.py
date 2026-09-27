import inspect
import typing
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall import IcmpRule
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger

CHECKSUM_VERIFICATION_NOTE = "Defines whether a Icmp header checksum verification is performed or not."
CODE_NOTE = "Filter to match packets with the Icmp code."
TYPE_NOTE = "Filter to match packets with the Icmp type."


def _pos_int(value):
    p = PositiveInteger()
    p.setValue(value)
    return p


def _boolean(value):
    b = Boolean()
    b.setValue(value)
    return b


class TestIcmpRule:
    def test_defaults_in_spec_displayed_order(self):
        obj = IcmpRule()
        assert isinstance(obj, ARObject)
        assert obj.getChecksumVerification() is None
        assert obj.getCode() is None
        assert obj.getType() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        assert IcmpRule.__doc__.strip() == "Configuration of filter rules for ICMP (Internet Control Message Protocol). Tags: atp.Status=candidate"

    def test_docstrings_are_spec_note_verbatim(self):
        assert inspect.cleandoc(IcmpRule.getChecksumVerification.__doc__) == CHECKSUM_VERIFICATION_NOTE
        assert inspect.cleandoc(IcmpRule.setChecksumVerification.__doc__) == CHECKSUM_VERIFICATION_NOTE + "\nA None value is a no-op and does not overwrite an existing checksumVerification."
        assert inspect.cleandoc(IcmpRule.getCode.__doc__) == CODE_NOTE
        assert inspect.cleandoc(IcmpRule.setCode.__doc__) == CODE_NOTE + "\nA None value is a no-op and does not overwrite an existing code."
        assert inspect.cleandoc(IcmpRule.getType.__doc__) == TYPE_NOTE
        assert inspect.cleandoc(IcmpRule.setType.__doc__) == TYPE_NOTE + "\nA None value is a no-op and does not overwrite an existing type."

    def test_get_set_round_trip_and_none_noop(self):
        obj = IcmpRule()
        checksum_verification = _boolean(True)
        code = _pos_int(3)
        type_ = _pos_int(8)

        assert obj.setChecksumVerification(checksum_verification) is obj
        assert obj.setCode(code) is obj
        assert obj.setType(type_) is obj

        assert obj.getChecksumVerification() is checksum_verification
        assert obj.getCode() is code
        assert obj.getType() is type_

        obj.setChecksumVerification(None)
        obj.setCode(None)
        obj.setType(None)
        assert obj.getChecksumVerification() is checksum_verification
        assert obj.getCode() is code
        assert obj.getType() is type_

    def test_get_type_hints_pins(self):
        hints = typing.get_type_hints(IcmpRule.setChecksumVerification)
        assert hints["return"] is IcmpRule
        assert hints["value"] == Optional[Boolean]
        hints = typing.get_type_hints(IcmpRule.setCode)
        assert hints["return"] is IcmpRule
        assert hints["value"] == Optional[PositiveInteger]
        hints = typing.get_type_hints(IcmpRule.setType)
        assert hints["return"] is IcmpRule
        assert hints["value"] == Optional[PositiveInteger]
