import typing

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import (
    AbstractRuleBasedValueSpecification,
    ApplicationRuleBasedValueSpecification,
    CompositeRuleBasedValueArgument,
    RuleBasedAxisCont,
    RuleBasedValueCont,
    ValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier

CLASS_NOTE = (
    "This meta-class represents rule based values for DataPrototypes typed by ApplicationDataTypes "
    "(ApplicationArrayDataType or a compound ApplicationPrimitiveDataType which also boils down to an array-nature)."
)

CATEGORY_NOTE = "This represents the category of the RuleBasedValue Specification Tags: xml.sequenceOffset=-20"
SW_AXIS_CONT_NOTE = (
    "This represents the axis values of a Compound Primitive Data Type (curve or map). The first swAxisCont "
    "describes the x-axis, the second sw AxisCont describes the y-axis, the third swAxisCont describes the "
    "z-axis. In addition to this, the axis can be denoted in swAxisIndex."
)
SW_VALUE_CONT_NOTE = "This represents the values of an array or Compound Primitive Data Type. " "Stereotypes: atpSplitable Tags: atp.Splitkey=swValueCont"


class TestApplicationRuleBasedValueSpecification:
    def test_inheritance(self):
        spec = ApplicationRuleBasedValueSpecification()
        assert isinstance(spec, AbstractRuleBasedValueSpecification)
        assert isinstance(spec, CompositeRuleBasedValueArgument)
        assert isinstance(spec, ValueSpecification)

    def test_initialization(self):
        spec = ApplicationRuleBasedValueSpecification()
        assert spec.getCategory() is None
        assert spec.getSwAxisConts() == []
        assert spec.getSwValueCont() is None

    def test_class_docstring_verbatim(self):
        docstring = ApplicationRuleBasedValueSpecification.__doc__ or ""
        assert docstring.strip().startswith(CLASS_NOTE)
        assert "[constr_1922]" in docstring

    def test_get_set_category(self):
        spec = ApplicationRuleBasedValueSpecification()
        category = Identifier().setValue("ARRAY")

        assert spec.setCategory(category) is spec
        assert spec.getCategory() is category

        spec.setCategory(None)
        assert spec.getCategory() is category

    def test_add_get_sw_axis_conts(self):
        spec = ApplicationRuleBasedValueSpecification()
        first = RuleBasedAxisCont()
        second = RuleBasedAxisCont()

        assert spec.addSwAxisCont(first) is spec
        assert spec.addSwAxisCont(second) is spec
        assert spec.getSwAxisConts() == [first, second]

        spec.addSwAxisCont(None)
        assert spec.getSwAxisConts() == [first, second]

    def test_get_set_sw_value_cont(self):
        spec = ApplicationRuleBasedValueSpecification()
        cont = RuleBasedValueCont()

        assert spec.setSwValueCont(cont) is spec
        assert spec.getSwValueCont() is cont

        spec.setSwValueCont(None)
        assert spec.getSwValueCont() is cont

    def test_accessor_type_annotations(self):
        assert typing.get_type_hints(ApplicationRuleBasedValueSpecification.setCategory)["value"] == typing.Optional[Identifier]
        assert typing.get_type_hints(ApplicationRuleBasedValueSpecification.getCategory)["return"] == typing.Optional[Identifier]

        add_hints = typing.get_type_hints(ApplicationRuleBasedValueSpecification.addSwAxisCont)
        assert add_hints["value"] == typing.Optional[RuleBasedAxisCont]
        assert typing.get_type_hints(ApplicationRuleBasedValueSpecification.getSwAxisConts)["return"] == typing.List[RuleBasedAxisCont]

        assert typing.get_type_hints(ApplicationRuleBasedValueSpecification.setSwValueCont)["value"] == typing.Optional[RuleBasedValueCont]
        assert typing.get_type_hints(ApplicationRuleBasedValueSpecification.getSwValueCont)["return"] == typing.Optional[RuleBasedValueCont]

    def test_member_docstrings_verbatim(self):
        spec = ApplicationRuleBasedValueSpecification()
        assert (spec.getCategory.__doc__ or "").strip() == CATEGORY_NOTE
        assert (spec.setCategory.__doc__ or "").strip().split("\n")[0] == CATEGORY_NOTE
        assert (spec.getSwAxisConts.__doc__ or "").strip() == SW_AXIS_CONT_NOTE
        assert (spec.addSwAxisCont.__doc__ or "").strip().split("\n")[0] == SW_AXIS_CONT_NOTE
        assert (spec.getSwValueCont.__doc__ or "").strip() == SW_VALUE_CONT_NOTE
        assert (spec.setSwValueCont.__doc__ or "").strip().split("\n")[0] == SW_VALUE_CONT_NOTE
