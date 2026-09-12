"""Tests for inline attribute enumerations."""

from armodel.models.M2.MSR.Documentation.TextModel.InlineAttributeEnums import ResolutionPolicyEnum


class TestResolutionPolicyEnum:
    def test_resolution_policy_literals(self):
        enum = ResolutionPolicyEnum()

        assert enum.validateEnumValue(ResolutionPolicyEnum.NO_SLOPPY)
        assert enum.validateEnumValue(ResolutionPolicyEnum.SLOPPY)
        assert ResolutionPolicyEnum.NO_SLOPPY == "NO-SLOPPY"
        assert ResolutionPolicyEnum.SLOPPY == "SLOPPY"

        enum.setValue(ResolutionPolicyEnum.SLOPPY)
        assert enum.getValue() == "SLOPPY"
