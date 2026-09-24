"""Model tests for the AttributeValueVariationPoint family.

AttributeValueVariationPoint is an abstract <<atpMixedString>> base that carries
four shared XML-attribute members (bindingTime, blueprintValue, sd, shortLabel)
plus the mixed-string content (provided by the AtpMixedString base). AbstractNumericalVariationPoint
is a second abstract base for the numerical branch. Concrete subclasses are
attribute-less beyond what they inherit (Limit adds intervalType). These tests
verify instantiation, the abstract-class guards, and full member coverage for
every class in scope.
"""

import typing

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AtpMixedString import AtpMixedString
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

# Table 7.2 attribute Notes without the trailing "Tags:" suffix (the stamped
# getter/setter docstring form carries the Note text only).
NOTES = {
    "bindingTime": (
        "This is the binding time in which the attribute value needs to be bound. "
        "If this attribute is missing, the attribute is not a variation point. "
        "In particular this means that It needs to be a single value according to the type specified in the pure model. "
        "It is an error if it is still a formula."
    ),
    "blueprintValue": "This represents a description that documents how the value shall be defined when deriving objects from the blueprint.",
    "sd": "This special data is provided to allow synchronization of Attribute value variation points with variant management systems. The usage is subject of agreement between the involved parties.",
    "shortLabel": "This allows to identify the variation point. It is also intended to allow RTE support for CompileTime Variation points.",
}


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
            assert instance.getMixedString() is None
            if isinstance(instance, LimitValueVariationPoint):
                assert instance.getIntervalType() is None


class TestAttributeValueVariationPointMembers:
    """Every class must expose all four shared members plus the AtpMixedString
    mixed content (per the user-given scope: 'check the member of each class are checked')."""

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
            assert isinstance(instance, AtpMixedString)
            assert instance.setMixedString("123") is instance
            assert instance.getMixedString() == "123"
            instance.setMixedString(None)
            assert instance.getMixedString() == "123"


class TestLimitValueVariationPointMembers:
    def test_interval_type_round_trip_and_chaining(self):
        limit = LimitValueVariationPoint()
        assert limit.setIntervalType(IntervalTypeEnum.CLOSED) is limit
        assert limit.getIntervalType() is IntervalTypeEnum.CLOSED
        limit.setIntervalType(None)
        assert limit.getIntervalType() is IntervalTypeEnum.CLOSED


class TestAttributeValueVariationPointSpecContract:
    """Table 7.2 (AUTOSAR_FO_TPS_GenericStructureTemplate, p.210) spec contract
    for the AttributeValueVariationPoint base itself."""

    def test_class_docstring_verbatim(self):
        """
        Test that the class docstring is the Table 7.2 Note verbatim (XSD group
        documentation L7821 confirms "SwSystemconstDependentFormula" as one word).
        """
        assert AttributeValueVariationPoint.__doc__.strip() == (
            "This class represents the ability to derive the value of the Attribute " "from a system constant (by SwSystemconstDependentFormula). It also provides a bindingTime."
        )

    def test_init_has_no_docstring(self):
        """
        Test that __init__ has no docstring (spec Notes live in inline member comments).
        """
        assert AttributeValueVariationPoint.__init__.__doc__ is None

    def test_binding_time_typed_binding_time_enum(self):
        """
        Test that bindingTime is typed BindingTimeEnum per Table 7.2 (getter/setter annotations).
        """
        getter_hints = typing.get_type_hints(AttributeValueVariationPoint.getBindingTime)
        assert getter_hints.get("return") == typing.Optional[BindingTimeEnum]

        setter_hints = typing.get_type_hints(AttributeValueVariationPoint.setBindingTime)
        assert setter_hints.get("value") == typing.Optional[BindingTimeEnum]
        assert setter_hints.get("return") is AttributeValueVariationPoint

    def test_blueprint_value_typed_string(self):
        """
        Test that blueprintValue is typed String per Table 7.2 (getter/setter annotations).
        """
        getter_hints = typing.get_type_hints(AttributeValueVariationPoint.getBlueprintValue)
        assert getter_hints.get("return") == typing.Optional[String]

        setter_hints = typing.get_type_hints(AttributeValueVariationPoint.setBlueprintValue)
        assert setter_hints.get("value") == typing.Optional[String]
        assert setter_hints.get("return") is AttributeValueVariationPoint

    def test_sd_typed_string(self):
        """
        Test that sd is typed String per Table 7.2 (getter/setter annotations).
        """
        getter_hints = typing.get_type_hints(AttributeValueVariationPoint.getSd)
        assert getter_hints.get("return") == typing.Optional[String]

        setter_hints = typing.get_type_hints(AttributeValueVariationPoint.setSd)
        assert setter_hints.get("value") == typing.Optional[String]
        assert setter_hints.get("return") is AttributeValueVariationPoint

    def test_short_label_typed_primitive_identifier(self):
        """
        Test that shortLabel is typed PrimitiveIdentifier per Table 7.2 (getter/setter annotations).
        """
        getter_hints = typing.get_type_hints(AttributeValueVariationPoint.getShortLabel)
        assert getter_hints.get("return") == typing.Optional[PrimitiveIdentifier]

        setter_hints = typing.get_type_hints(AttributeValueVariationPoint.setShortLabel)
        assert setter_hints.get("value") == typing.Optional[PrimitiveIdentifier]
        assert setter_hints.get("return") is AttributeValueVariationPoint

    def test_getter_docstrings_are_notes_without_tags(self):
        """
        Test that every getter docstring is the Table 7.2 Note verbatim without the Tags suffix.
        """
        assert AttributeValueVariationPoint.getBindingTime.__doc__.strip() == NOTES["bindingTime"]
        assert AttributeValueVariationPoint.getBlueprintValue.__doc__.strip() == NOTES["blueprintValue"]
        assert AttributeValueVariationPoint.getSd.__doc__.strip() == NOTES["sd"]
        assert AttributeValueVariationPoint.getShortLabel.__doc__.strip() == NOTES["shortLabel"]

    def test_setter_docstrings_are_notes_with_none_noop(self):
        """
        Test that every setter docstring is the Table 7.2 Note plus the None-no-op sentence.
        """
        for attr, getter in [
            ("bindingTime", "getBindingTime"),
            ("blueprintValue", "getBlueprintValue"),
            ("sd", "getSd"),
            ("shortLabel", "getShortLabel"),
        ]:
            setter = getattr(AttributeValueVariationPoint, "set" + getter[3:])
            assert setter.__doc__.strip() == ("%s A None value is a no-op and does not overwrite an existing %s." % (NOTES[attr], attr))
