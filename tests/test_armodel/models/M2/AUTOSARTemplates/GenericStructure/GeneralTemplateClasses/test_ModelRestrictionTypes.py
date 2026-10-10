"""
Tests for the ModelRestrictionTypes module (FullBindingTimeEnum,
AbstractValueRestriction, AbstractVariationRestriction).
"""

from typing import List

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ModelRestrictionTypes import (
    AbstractValueRestriction,
    AbstractVariationRestriction,
    FullBindingTimeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Limit,
    PositiveInteger,
    RegularExpression,
)


class TestFullBindingTimeEnum:
    """
    Test class for FullBindingTimeEnum functionality (Table 4.39).
    """

    def test_initialization(self):
        enum = FullBindingTimeEnum()
        assert enum is not None
        assert enum._value is None

    def test_literal_members(self):
        assert FullBindingTimeEnum.BLUEPRINT_DERIVATION_TIME == "BLUEPRINT-DERIVATION-TIME"
        assert FullBindingTimeEnum.SYSTEM_DESIGN_TIME == "SYSTEM-DESIGN-TIME"
        assert FullBindingTimeEnum.CODE_GENERATION_TIME == "CODE-GENERATION-TIME"
        assert FullBindingTimeEnum.PRE_COMPILE_TIME == "PRE-COMPILE-TIME"
        assert FullBindingTimeEnum.LINK_TIME == "LINK-TIME"
        assert FullBindingTimeEnum.POST_BUILD == "POST-BUILD"

    def test_enum_values(self):
        enum = FullBindingTimeEnum()
        assert list(enum.getEnumValues()) == [
            "BLUEPRINT-DERIVATION-TIME",
            "SYSTEM-DESIGN-TIME",
            "CODE-GENERATION-TIME",
            "PRE-COMPILE-TIME",
            "LINK-TIME",
            "POST-BUILD",
        ]

    def test_set_value(self):
        enum = FullBindingTimeEnum().setValue(FullBindingTimeEnum.POST_BUILD)
        assert enum.getValue() == "POST-BUILD"


class TestAbstractValueRestriction:
    """
    Test class for AbstractValueRestriction functionality (Table 4.37).
    """

    def test_mixin_defaults(self):
        class _Derived(AbstractValueRestriction):
            pass

        obj = _Derived()
        assert obj.max is None
        assert obj.maxLength is None
        assert obj.min is None
        assert obj.minLength is None
        assert obj.pattern is None

    def test_member_round_trip(self):
        class _Derived(AbstractValueRestriction):
            pass

        obj = _Derived()
        assert obj.getMax() is None
        assert obj.getMaxLength() is None
        assert obj.getMin() is None
        assert obj.getMinLength() is None
        assert obj.getPattern() is None

        limit_max = Limit().setValue("10.0")
        limit_min = Limit().setValue("0.0")
        pattern = RegularExpression().setValue("[0-9]+")

        assert obj.setMax(limit_max) is obj
        assert obj.setMaxLength(PositiveInteger().setValue(5)) is obj
        assert obj.setMin(limit_min) is obj
        assert obj.setMinLength(PositiveInteger().setValue(1)) is obj
        assert obj.setPattern(pattern) is obj

        assert obj.getMax() is limit_max
        assert obj.getMaxLength().getValue() == 5
        assert obj.getMin() is limit_min
        assert obj.getMinLength().getValue() == 1
        assert obj.getPattern() is pattern


class TestAbstractVariationRestriction:
    """
    Test class for AbstractVariationRestriction functionality (Table 4.38).
    """

    def test_mixin_defaults(self):
        class _Derived(AbstractVariationRestriction):
            def __init__(self):
                super().__init__()
                self.validBindingTimes: List[FullBindingTimeEnum] = []

        obj = _Derived()
        assert obj.variation is None
        assert obj.validBindingTimes == []

    def test_member_round_trip(self):
        class _Derived(AbstractVariationRestriction):
            def __init__(self):
                super().__init__()
                self.validBindingTimes: List[FullBindingTimeEnum] = []

        obj = _Derived()
        assert obj.getVariation() is None
        assert obj.getValidBindingTimes() == []

        variation = Boolean().setValue(True)
        assert obj.setVariation(variation) is obj
        assert obj.getVariation() is variation

        assert obj.addValidBindingTime(FullBindingTimeEnum().setValue(FullBindingTimeEnum.POST_BUILD)) is obj
        assert obj.addValidBindingTime(FullBindingTimeEnum().setValue(FullBindingTimeEnum.PRE_COMPILE_TIME)) is obj
        assert len(obj.getValidBindingTimes()) == 2
        assert obj.getValidBindingTimes()[0].getValue() == "POST-BUILD"
        assert obj.getValidBindingTimes()[1].getValue() == "PRE-COMPILE-TIME"

        times = [FullBindingTimeEnum().setValue(FullBindingTimeEnum.LINK_TIME)]
        assert obj.setValidBindingTimes(times) is obj
        assert obj.getValidBindingTimes() is times


class TestAbstractVariationRestrictionInit:
    """The mixin must own its own per-instance initialization."""

    def test_mixin_init_runs_for_concrete_subclass(self):
        """
        Test that AbstractVariationRestriction defines its own __init__.

        The mixin sits after Referrable in the MRO, so it only initializes
        itself if Referrable dispatches cooperatively.
        """
        assert "__init__" in AbstractVariationRestriction.__dict__, "mixin must define its own __init__"

    def test_subclass_instances_do_not_share_the_default(self):
        """
        Test that two instances do not share the validBindingTimes list.

        A mutable class-level default would be shared by every instance, so one
        instance's addValidBindingTime would leak into another's list.
        """

        class _Concrete(AbstractVariationRestriction):
            def __init__(self):
                super().__init__()

        first, second = _Concrete(), _Concrete()
        first.addValidBindingTime(FullBindingTimeEnum().setValue(FullBindingTimeEnum.POST_BUILD))
        assert second.getValidBindingTimes() == [], "instances must not share the validBindingTimes list"
