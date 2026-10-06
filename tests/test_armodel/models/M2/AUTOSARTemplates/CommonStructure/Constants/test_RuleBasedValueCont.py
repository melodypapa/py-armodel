import typing

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import (
    RuleBasedValueCont,
    RuleBasedValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import ValueList

CLASS_NOTE = "This represents the values of a compound primitive (CURVE, MAP, CUBOID, CUBE_4, CUBE_5, BLK) or an array."

RULE_BASED_VALUES_NOTE = (
    "This represents the rule based value specification for the array or compound primitive "
    "(CURVE, MAP, CUBOID, CUBE_4, CUBE_5, VAL_BLK). "
    "Stereotypes: atpSplitable Tags: atp.Splitkey=ruleBasedValues xml.roleElement=true xml.roleWrapperElement=false "
    "xml.sequenceOffset=80 xml.typeWrapperElement=false"
)
SW_ARRAYSIZE_NOTE = (
    "This attribute defines the size of each dimension for compound primitives CURVE, MAP, CUBOID, CUBE_4, "
    "CUBE_5, COM_AXIS, RES_AXIS, VAL_BLK. For each dimension one value has to be defined, e.g. one in case of "
    "COM_AXIS and two or more in case of MAP. Tags: xml.sequenceOffset=40"
)
UNIT_NOTE = "This represents the physical unit of the provided values. Tags: xml.sequenceOffset=30"


class TestRuleBasedValueCont:
    def test_inheritance(self):
        cont = RuleBasedValueCont()
        assert isinstance(cont, ARObject)

    def test_initialization(self):
        cont = RuleBasedValueCont()
        assert cont.getRuleBasedValues() is None
        assert cont.getSwArraysize() is None
        assert cont.getUnitRef() is None

    def test_class_docstring_verbatim(self):
        docstring = RuleBasedValueCont.__doc__ or ""
        assert docstring.strip().startswith(CLASS_NOTE)
        assert "[constr_1924]" in docstring
        assert "[constr_2058]" in docstring

    def test_get_set_rule_based_values(self):
        cont = RuleBasedValueCont()
        value = RuleBasedValueSpecification()

        assert cont.setRuleBasedValues(value) is cont
        assert cont.getRuleBasedValues() is value

        cont.setRuleBasedValues(None)
        assert cont.getRuleBasedValues() is value

    def test_get_set_sw_arraysize(self):
        cont = RuleBasedValueCont()
        value = ValueList()

        assert cont.setSwArraysize(value) is cont
        assert cont.getSwArraysize() is value

        cont.setSwArraysize(None)
        assert cont.getSwArraysize() is value

    def test_get_set_unit_ref(self):
        cont = RuleBasedValueCont()
        ref = RefType().setValue("/Unit/SomeUnit")

        assert cont.setUnitRef(ref) is cont
        assert cont.getUnitRef() is ref

        cont.setUnitRef(None)
        assert cont.getUnitRef() is ref

    def test_accessor_type_annotations(self):
        assert typing.get_type_hints(RuleBasedValueCont.setRuleBasedValues)["value"] == typing.Optional[RuleBasedValueSpecification]
        assert typing.get_type_hints(RuleBasedValueCont.getRuleBasedValues)["return"] == typing.Optional[RuleBasedValueSpecification]

        assert typing.get_type_hints(RuleBasedValueCont.setSwArraysize)["value"] == typing.Optional[ValueList]
        assert typing.get_type_hints(RuleBasedValueCont.getSwArraysize)["return"] == typing.Optional[ValueList]

        assert typing.get_type_hints(RuleBasedValueCont.setUnitRef)["value"] == typing.Optional[RefType]
        assert typing.get_type_hints(RuleBasedValueCont.getUnitRef)["return"] == typing.Optional[RefType]

    def test_member_docstrings_verbatim(self):
        cont = RuleBasedValueCont()
        assert (cont.getRuleBasedValues.__doc__ or "").strip() == RULE_BASED_VALUES_NOTE
        assert (cont.setRuleBasedValues.__doc__ or "").strip().split("\n")[0] == RULE_BASED_VALUES_NOTE
        assert (cont.getSwArraysize.__doc__ or "").strip() == SW_ARRAYSIZE_NOTE
        assert (cont.setSwArraysize.__doc__ or "").strip().split("\n")[0] == SW_ARRAYSIZE_NOTE
        assert (cont.getUnitRef.__doc__ or "").strip() == UNIT_NOTE
        assert (cont.setUnitRef.__doc__ or "").strip().split("\n")[0] == UNIT_NOTE
