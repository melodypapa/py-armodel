import typing

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import (
    RuleBasedAxisCont,
    RuleBasedValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.MSR.DataDictionary.CalibrationParameter import CalprmAxisCategoryEnum
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import ValueList
from armodel.models.M2.MSR.DataDictionary.RecordLayout import AxisIndexType

CLASS_NOTE = (
    "This represents the values for the axis of a compound primitive (curve, map). For standard and fix axes, "
    "SwAxisCont contains the values of the axis directly. The axis values of SwAxisCont with the category "
    "COM_AXIS, RES_AXIS are for display only. For editing and processing, only the values in the related "
    "GroupAxis are binding."
)

CATEGORY_NOTE = "This category specifies the particular axis types: " "\u2022 STD_AXIS \u2022 COM_AXIS \u2022 RES_AXIS (swArraysize necessary) Tags: xml.sequenceOffset=20"
RULE_BASED_VALUES_NOTE = (
    "This represents the rule based value specification for the axis of a compound primitive (curve, map). "
    "Tags: xml.roleElement=true xml.roleWrapperElement=false xml.sequenceOffset=80 xml.typeWrapperElement=false"
)
SW_ARRAYSIZE_NOTE = "For multidimensional compound primitives (curve, map ...) it is necessary to know the dimensions." "They are specified using swArraySize. Tags: xml.sequenceOffset=40"
SW_AXIS_INDEX_NOTE = (
    "This property allows to explicitly assign the axis contents to a particular axis. It is specified by "
    "numbers where 1 corresponds to the x-axis. It is also possible to derive the axis association from the "
    "sequence of the parent. Tags: xml.sequenceOffset=50"
)
UNIT_NOTE = "This represents the physical unit of the provided values. Tags: xml.sequenceOffset=30"


class TestRuleBasedAxisCont:
    def test_inheritance(self):
        spec = RuleBasedAxisCont()
        assert isinstance(spec, ARObject)

    def test_initialization(self):
        spec = RuleBasedAxisCont()
        assert spec.getCategory() is None
        assert spec.getRuleBasedValues() is None
        assert spec.getSwArraysize() is None
        assert spec.getSwAxisIndex() is None
        assert spec.getUnitRef() is None

    def test_class_docstring_verbatim(self):
        docstring = RuleBasedAxisCont.__doc__ or ""
        assert docstring.strip().startswith(CLASS_NOTE)
        assert "[constr_1923]" in docstring
        assert "[constr_2057]" in docstring

    def test_get_set_category(self):
        spec = RuleBasedAxisCont()
        category = CalprmAxisCategoryEnum().setValue(CalprmAxisCategoryEnum.STD_AXIS)

        assert spec.setCategory(category) is spec
        assert spec.getCategory() is category

        spec.setCategory(None)
        assert spec.getCategory() is category

    def test_get_set_rule_based_values(self):
        spec = RuleBasedAxisCont()
        value = RuleBasedValueSpecification()

        assert spec.setRuleBasedValues(value) is spec
        assert spec.getRuleBasedValues() is value

        spec.setRuleBasedValues(None)
        assert spec.getRuleBasedValues() is value

    def test_get_set_sw_arraysize(self):
        spec = RuleBasedAxisCont()
        value = ValueList()

        assert spec.setSwArraysize(value) is spec
        assert spec.getSwArraysize() is value

        spec.setSwArraysize(None)
        assert spec.getSwArraysize() is value

    def test_get_set_sw_axis_index(self):
        spec = RuleBasedAxisCont()
        index = AxisIndexType().setValue("1")

        assert spec.setSwAxisIndex(index) is spec
        assert spec.getSwAxisIndex() is index

        spec.setSwAxisIndex(None)
        assert spec.getSwAxisIndex() is index

    def test_get_set_unit_ref(self):
        spec = RuleBasedAxisCont()
        ref = RefType().setValue("/Unit/SomeUnit")

        assert spec.setUnitRef(ref) is spec
        assert spec.getUnitRef() is ref

        spec.setUnitRef(None)
        assert spec.getUnitRef() is ref

    def test_accessor_type_annotations(self):
        assert typing.get_type_hints(RuleBasedAxisCont.setCategory)["value"] == typing.Optional[CalprmAxisCategoryEnum]
        assert typing.get_type_hints(RuleBasedAxisCont.getCategory)["return"] == typing.Optional[CalprmAxisCategoryEnum]

        assert typing.get_type_hints(RuleBasedAxisCont.setRuleBasedValues)["value"] == typing.Optional[RuleBasedValueSpecification]
        assert typing.get_type_hints(RuleBasedAxisCont.getRuleBasedValues)["return"] == typing.Optional[RuleBasedValueSpecification]

        assert typing.get_type_hints(RuleBasedAxisCont.setSwArraysize)["value"] == typing.Optional[ValueList]
        assert typing.get_type_hints(RuleBasedAxisCont.getSwArraysize)["return"] == typing.Optional[ValueList]

        assert typing.get_type_hints(RuleBasedAxisCont.setSwAxisIndex)["value"] == typing.Optional[AxisIndexType]
        assert typing.get_type_hints(RuleBasedAxisCont.getSwAxisIndex)["return"] == typing.Optional[AxisIndexType]

        assert typing.get_type_hints(RuleBasedAxisCont.setUnitRef)["value"] == typing.Optional[RefType]
        assert typing.get_type_hints(RuleBasedAxisCont.getUnitRef)["return"] == typing.Optional[RefType]

    def test_member_docstrings_verbatim(self):
        spec = RuleBasedAxisCont()
        assert (spec.getCategory.__doc__ or "").strip() == CATEGORY_NOTE
        assert (spec.setCategory.__doc__ or "").strip().split("\n")[0] == CATEGORY_NOTE
        assert (spec.getRuleBasedValues.__doc__ or "").strip() == RULE_BASED_VALUES_NOTE
        assert (spec.setRuleBasedValues.__doc__ or "").strip().split("\n")[0] == RULE_BASED_VALUES_NOTE
        assert (spec.getSwArraysize.__doc__ or "").strip() == SW_ARRAYSIZE_NOTE
        assert (spec.setSwArraysize.__doc__ or "").strip().split("\n")[0] == SW_ARRAYSIZE_NOTE
        assert (spec.getSwAxisIndex.__doc__ or "").strip() == SW_AXIS_INDEX_NOTE
        assert (spec.setSwAxisIndex.__doc__ or "").strip().split("\n")[0] == SW_AXIS_INDEX_NOTE
        assert (spec.getUnitRef.__doc__ or "").strip() == UNIT_NOTE
        assert (spec.setUnitRef.__doc__ or "").strip().split("\n")[0] == UNIT_NOTE
