"""Model tests for the AttributeValueVariationPoint family.

AttributeValueVariationPoint is an abstract <<atpMixedString>> base that carries
four shared XML-attribute members (bindingTime, blueprintValue, sd, shortLabel)
plus the mixed-string content (modeled as _text). AbstractNumericalVariationPoint
is a second abstract base for the numerical branch. Concrete subclasses are
attribute-less beyond what they inherit (Limit adds intervalType). These tests
verify instantiation, the abstract-class guards, and full member coverage for
every class in scope.
"""

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Enumerations import BindingTimeEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    IntervalTypeEnum,
    PrimitiveIdentifier,
    String,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.AttributeValueVariationPoints import (
    AbstractNumericalVariationPoint,
    AttributeValueVariationPoint,
    BooleanValueVariationPoint,
    FloatValueVariationPoint,
    IntegerValueVariationPoint,
    LimitValueVariationPoint,
    NumericalValueVariationPoint,
    PositiveIntegerValueVariationPoint,
    TimeValueValueVariationPoint,
    UnlimitedIntegerValueVariationPoint,
)

CONCRETE_BY_BASE = {
    "AttributeValueVariationPoint": [
        BooleanValueVariationPoint,
        FloatValueVariationPoint,
        IntegerValueVariationPoint,
        PositiveIntegerValueVariationPoint,
        TimeValueValueVariationPoint,
        UnlimitedIntegerValueVariationPoint,
    ],
    "AbstractNumericalVariationPoint": [
        NumericalValueVariationPoint,
        LimitValueVariationPoint,
    ],
}

ALL_CONCRETE = CONCRETE_BY_BASE["AttributeValueVariationPoint"] + CONCRETE_BY_BASE["AbstractNumericalVariationPoint"]


class TestAttributeValueVariationPointAbstractGuards:
    def test_base_is_abstract(self):
        with pytest.raises(TypeError):
            AttributeValueVariationPoint()

    def test_abstract_numerical_is_abstract(self):
        with pytest.raises(TypeError):
            AbstractNumericalVariationPoint()


class TestAttributeValueVariationPointInstantiation:
    def test_concrete_subclasses_are_instances_of_base(self):
        for subclass in ALL_CONCRETE:
            instance = subclass()
            assert isinstance(instance, AttributeValueVariationPoint)

    def test_numerical_branch_is_instance_of_abstract_numerical(self):
        for subclass in CONCRETE_BY_BASE["AbstractNumericalVariationPoint"]:
            instance = subclass()
            assert isinstance(instance, AbstractNumericalVariationPoint)

    def test_initial_members_are_none(self):
        for subclass in ALL_CONCRETE:
            instance = subclass()
            assert instance.getBindingTime() is None
            assert instance.getBlueprintValue() is None
            assert instance.getSd() is None
            assert instance.getShortLabel() is None
            assert instance.getText() is None
            if isinstance(instance, LimitValueVariationPoint):
                assert instance.getIntervalType() is None


class TestAttributeValueVariationPointMembers:
    """Every class must expose all four shared members plus _text (per the
    user-given scope: 'check the member of each class are checked')."""

    def test_binding_time_round_trip_and_chaining(self):
        for subclass in ALL_CONCRETE:
            instance = subclass()
            value = BindingTimeEnum().setValue("preCompileTime")
            assert instance.setBindingTime(value) is instance
            assert instance.getBindingTime() is value
            instance.setBindingTime(None)
            assert instance.getBindingTime() is value

    def test_blueprint_value_round_trip_and_chaining(self):
        for subclass in ALL_CONCRETE:
            instance = subclass()
            value = String()
            value.setValue("derive me")
            assert instance.setBlueprintValue(value) is instance
            assert instance.getBlueprintValue() is value
            instance.setBlueprintValue(None)
            assert instance.getBlueprintValue() is value

    def test_sd_round_trip_and_chaining(self):
        for subclass in ALL_CONCRETE:
            instance = subclass()
            value = String()
            value.setValue("sync id")
            assert instance.setSd(value) is instance
            assert instance.getSd() is value
            instance.setSd(None)
            assert instance.getSd() is value

    def test_short_label_round_trip_and_chaining(self):
        for subclass in ALL_CONCRETE:
            instance = subclass()
            value = PrimitiveIdentifier()
            value.setValue("vp_label")
            assert instance.setShortLabel(value) is instance
            assert instance.getShortLabel() is value
            instance.setShortLabel(None)
            assert instance.getShortLabel() is value

    def test_text_round_trip_and_chaining(self):
        for subclass in ALL_CONCRETE:
            instance = subclass()
            assert instance.setText("123") is instance
            assert instance.getText() == "123"
            instance.setText(None)
            assert instance.getText() == "123"


class TestLimitValueVariationPointMembers:
    def test_interval_type_round_trip_and_chaining(self):
        limit = LimitValueVariationPoint()
        assert limit.setIntervalType(IntervalTypeEnum.CLOSED) is limit
        assert limit.getIntervalType() is IntervalTypeEnum.CLOSED
        limit.setIntervalType(None)
        assert limit.getIntervalType() is IntervalTypeEnum.CLOSED
