"""Model tests for DiagnosticExtract EnvironmentalCondition classes.

DiagnosticEnvironmentalCondition (Table 4.35, p.79) with its in-pass closure:
DiagnosticEnvConditionFormula (Table 4.36), DiagnosticLogicalOperatorEnum
(Table 4.37), DiagnosticEnvConditionFormulaPart (Table 4.38) and
DiagnosticEnvModeElement (Table 4.44).
"""

import inspect

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import TextValueSpecification
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import DiagnosticCommonElement
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.EnvironmentalCondition import (
    DiagnosticCompareTypeEnum,
    DiagnosticEnvBswModeElement,
    DiagnosticEnvCompareCondition,
    DiagnosticEnvConditionFormula,
    DiagnosticEnvConditionFormulaPart,
    DiagnosticEnvDataCondition,
    DiagnosticEnvDataElementCondition,
    DiagnosticEnvironmentalCondition,
    DiagnosticEnvModeCondition,
    DiagnosticEnvModeElement,
    DiagnosticEnvSwcModeElement,
    DiagnosticLogicalOperatorEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable, Referrable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, PositiveInteger, RefType
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps

ENV_CONDITION_NOTE = (
    "The meta-class DiagnosticEnvironmentalCondition formalizes the idea of a condition which is evaluated during runtime of the ECU by looking at "
    '"environmental" states (e.g. one such condition is that the vehicle is not driving, i.e. vehicle speed == 0). '
    "Tags: atp.recommendedPackage=DiagnosticEnvironmentalConditions"
)
FORMULA_NOTE = (
    "A DiagnosticEnvConditionFormula embodies the computation instruction that is to be evaluated at runtime to determine if the DiagnosticEnvironmentalCondition "
    "is currently present (i.e. the formula is evaluated to true) or not (otherwise). The formula itself consists of parts which are combined by the logical "
    "operations specified by DiagnosticEnvConditionFormula.op. If a diagnostic functionality cannot be executed because an environmental condition fails then the "
    "diagnostic stack shall send a negative response code (NRC) back to the client. The value of the NRC is directly related to the specific formula and is "
    "therefore formalized in the attribute DiagnosticEnvConditionFormula.nrcValue."
)
FORMULA_PART_NOTE = (
    "A DiagnosticEnvConditionFormulaPart can either be a atomic condition, e.g. a DiagnosticEnvCompareCondition, or a DiagnosticEnvConditionFormula, again, " "which allows arbitrary nesting."
)
MODE_ELEMENT_NOTE = (
    "All ModeDeclarations that are referenced in a DiagnosticEnvModeCondition shall be defined as a DiagnosticEnvModeElement of this DiagnosticEnvironmentalCondition. "
    "This concept keeps the ARXML clean: It avoids that the DiagnosticEnvConditionFormula is cluttered by lengthy InstanceRef definitions. Furthermore, it allows "
    "that an InstanceRef only needs to be defined once and can be used multiple times in the different DiagnosticEnvModeConditions."
)
LOGICAL_OPERATOR_ENUM_NOTE = "Logical AND and OR operation (&&, ||)"
COMPARE_TYPE_ENUM_NOTE = "Enumeration for the type of a comparison of values usually expressed by the following operators: ==, !=, <, <=, >, >="
FORMULA_ATTR_NOTE = "This attribute represents the formula part of the DiagnosticEnvironmentalCondition."
MODE_ELEMENT_ATTR_NOTE = "This aggregation contains a representation of ModeDeclarations in the context of a DiagnosticEnvironmentalCondition."
NRC_VALUE_NOTE = "This attribute represents the concrete NRC value that shall be returned if the condition fails."
OP_NOTE = "This attribute represents the concrete operator (supported operators: and, or) of the condition formula."
PART_NOTE = "This aggregation represents the collection of formula parts that can be combined by logical operators."


def _pkg():
    return AUTOSAR.getInstance().createARPackage("EnvConds")


def _norm(doc):
    return " ".join(doc.split())


class _ConcreteFormulaPart(DiagnosticEnvConditionFormulaPart):
    def __init__(self):
        super().__init__()


class _ConcreteModeElement(DiagnosticEnvModeElement):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)


class Test_DiagnosticEnvironmentalCondition:
    """Test cases for DiagnosticEnvironmentalCondition class (Table 4.35, p.79)."""

    def test_instantiation(self):
        condition = DiagnosticEnvironmentalCondition(_pkg(), "Cond1")
        assert condition.getShortName() == "Cond1"

    def test_is_diagnostic_common_element_subclass(self):
        assert issubclass(DiagnosticEnvironmentalCondition, DiagnosticCommonElement)
        assert issubclass(DiagnosticEnvironmentalCondition, ARObject)
        assert issubclass(DiagnosticEnvironmentalCondition, Identifiable)

    def test_class_docstring_is_spec_note_verbatim(self):
        assert DiagnosticEnvironmentalCondition.__doc__ == ENV_CONDITION_NOTE

    def test_init_has_no_docstring(self):
        assert DiagnosticEnvironmentalCondition.__init__.__doc__ is None

    def test_defaults_in_displayed_order(self):
        condition = DiagnosticEnvironmentalCondition(_pkg(), "Cond1")
        assert list(condition.__dict__.keys())[-2:] == ["formula", "modeElements"]
        assert condition.getFormula() is None
        assert condition.getModeElements() == []

    def test_formula_round_trip(self):
        condition = DiagnosticEnvironmentalCondition(_pkg(), "Cond1")
        formula = DiagnosticEnvConditionFormula()
        assert condition.setFormula(formula) is condition
        assert condition.getFormula() is formula

    def test_formula_setter_none_is_no_op(self):
        condition = DiagnosticEnvironmentalCondition(_pkg(), "Cond1")
        formula = DiagnosticEnvConditionFormula()
        condition.setFormula(formula)
        assert condition.setFormula(None) is condition
        assert condition.getFormula() is formula

    def test_add_mode_element_appends_and_returns_self(self):
        condition = DiagnosticEnvironmentalCondition(_pkg(), "Cond1")
        mode_element = _ConcreteModeElement(condition, "Mode1")
        assert condition.addModeElement(mode_element) is condition
        assert condition.getModeElements() == [mode_element]

    def test_add_mode_element_none_is_no_op(self):
        condition = DiagnosticEnvironmentalCondition(_pkg(), "Cond1")
        mode_element = _ConcreteModeElement(condition, "Mode1")
        condition.addModeElement(mode_element)
        assert condition.addModeElement(None) is condition
        assert condition.getModeElements() == [mode_element]

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        assert _norm(DiagnosticEnvironmentalCondition.getFormula.__doc__) == FORMULA_ATTR_NOTE
        assert _norm(DiagnosticEnvironmentalCondition.setFormula.__doc__) == (FORMULA_ATTR_NOTE + " A None value is a no-op and does not overwrite an existing formula.")
        assert _norm(DiagnosticEnvironmentalCondition.getModeElements.__doc__) == MODE_ELEMENT_ATTR_NOTE
        assert _norm(DiagnosticEnvironmentalCondition.addModeElement.__doc__) == (MODE_ELEMENT_ATTR_NOTE + " A None value is a no-op and does not extend the modeElements list.")


class Test_DiagnosticEnvConditionFormula:
    """Test cases for DiagnosticEnvConditionFormula class (Table 4.36, p.80)."""

    def test_instantiation(self):
        formula = DiagnosticEnvConditionFormula()
        assert isinstance(formula, DiagnosticEnvConditionFormula)

    def test_is_formula_part_subclass(self):
        assert issubclass(DiagnosticEnvConditionFormula, DiagnosticEnvConditionFormulaPart)
        assert issubclass(DiagnosticEnvConditionFormula, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        assert DiagnosticEnvConditionFormula.__doc__ == FORMULA_NOTE

    def test_init_has_no_docstring(self):
        assert DiagnosticEnvConditionFormula.__init__.__doc__ is None

    def test_defaults_in_displayed_order(self):
        formula = DiagnosticEnvConditionFormula()
        assert list(formula.__dict__.keys())[-3:] == ["nrcValue", "op", "parts"]
        assert formula.getNrcValue() is None
        assert formula.getOp() is None
        assert formula.getParts() == []

    def test_nrc_value_round_trip(self):
        formula = DiagnosticEnvConditionFormula()
        value = PositiveInteger().setValue(0x22)
        assert formula.setNrcValue(value) is formula
        assert formula.getNrcValue() is value

    def test_op_round_trip(self):
        formula = DiagnosticEnvConditionFormula()
        value = DiagnosticLogicalOperatorEnum().setValue(DiagnosticLogicalOperatorEnum.LOGICAL_OR)
        assert formula.setOp(value) is formula
        assert formula.getOp() is value

    def test_add_part_appends_and_returns_self(self):
        formula = DiagnosticEnvConditionFormula()
        part = _ConcreteFormulaPart()
        assert formula.addPart(part) is formula
        assert formula.getParts() == [part]

    def test_add_part_none_is_no_op(self):
        formula = DiagnosticEnvConditionFormula()
        part = _ConcreteFormulaPart()
        formula.addPart(part)
        assert formula.addPart(None) is formula
        assert formula.getParts() == [part]

    def test_nested_formula_as_part(self):
        formula = DiagnosticEnvConditionFormula()
        nested = DiagnosticEnvConditionFormula()
        formula.addPart(nested)
        assert formula.getParts() == [nested]

    def test_setter_none_is_no_op(self):
        formula = DiagnosticEnvConditionFormula()
        formula.setNrcValue(PositiveInteger().setValue(0x22))
        formula.setOp(DiagnosticLogicalOperatorEnum().setValue(DiagnosticLogicalOperatorEnum.LOGICAL_AND))
        assert formula.setNrcValue(None) is formula
        assert formula.setOp(None) is formula
        assert formula.getNrcValue().getValue() == 0x22
        assert formula.getOp().getValue() == "LOGICAL-AND"

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        assert _norm(DiagnosticEnvConditionFormula.getNrcValue.__doc__) == NRC_VALUE_NOTE
        assert _norm(DiagnosticEnvConditionFormula.setNrcValue.__doc__) == (NRC_VALUE_NOTE + " A None value is a no-op and does not overwrite an existing nrcValue.")
        assert _norm(DiagnosticEnvConditionFormula.getOp.__doc__) == OP_NOTE
        assert _norm(DiagnosticEnvConditionFormula.setOp.__doc__) == (OP_NOTE + " A None value is a no-op and does not overwrite an existing op.")
        assert _norm(DiagnosticEnvConditionFormula.getParts.__doc__) == PART_NOTE
        assert _norm(DiagnosticEnvConditionFormula.addPart.__doc__) == (PART_NOTE + " A None value is a no-op and does not extend the parts list.")


class Test_DiagnosticEnvConditionFormulaPart:
    """Test cases for DiagnosticEnvConditionFormulaPart class (Table 4.38, p.81)."""

    def test_is_abstract(self):
        with pytest.raises(TypeError):
            DiagnosticEnvConditionFormulaPart()

    def test_is_ar_object_subclass(self):
        assert issubclass(DiagnosticEnvConditionFormulaPart, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        assert DiagnosticEnvConditionFormulaPart.__doc__ == FORMULA_PART_NOTE

    def test_init_has_no_docstring(self):
        assert DiagnosticEnvConditionFormulaPart.__init__.__doc__ is None

    def test_has_no_spec_attributes(self):
        part = _ConcreteFormulaPart()
        assert not hasattr(part, "getCompareType")
        assert not hasattr(part, "getCompareValue")


class Test_DiagnosticEnvModeElement:
    """Test cases for DiagnosticEnvModeElement class (Table 4.44, p.83)."""

    def test_is_abstract(self):
        with pytest.raises(TypeError):
            DiagnosticEnvModeElement(_pkg(), "Mode1")

    def test_is_referrable_subclass(self):
        assert issubclass(DiagnosticEnvModeElement, Referrable)
        assert issubclass(DiagnosticEnvModeElement, ARObject)

    def test_concrete_subclass_initialization(self):
        mode_element = _ConcreteModeElement(_pkg(), "Mode1")
        assert mode_element.getShortName() == "Mode1"

    def test_class_docstring_is_spec_note_verbatim(self):
        assert DiagnosticEnvModeElement.__doc__ == MODE_ELEMENT_NOTE

    def test_init_has_no_docstring(self):
        assert DiagnosticEnvModeElement.__init__.__doc__ is None

    def test_has_no_spec_attributes(self):
        mode_element = _ConcreteModeElement(_pkg(), "Mode1")
        assert not hasattr(mode_element, "getModeIRef")


class Test_DiagnosticLogicalOperatorEnum:
    """Test cases for DiagnosticLogicalOperatorEnum (Table 4.37, p.81)."""

    def test_enum_values_are_xsd_wire_values(self):
        values = DiagnosticLogicalOperatorEnum().getEnumValues()
        assert values == ("LOGICAL-AND", "LOGICAL-OR")

    def test_literal_members(self):
        assert DiagnosticLogicalOperatorEnum.LOGICAL_AND == "LOGICAL-AND"
        assert DiagnosticLogicalOperatorEnum.LOGICAL_OR == "LOGICAL-OR"

    def test_instantiable_and_value_round_trip(self):
        enum_instance = DiagnosticLogicalOperatorEnum().setValue(DiagnosticLogicalOperatorEnum.LOGICAL_AND)
        assert enum_instance.getValue() == "LOGICAL-AND"

    def test_class_docstring_is_spec_note_verbatim(self):
        assert DiagnosticLogicalOperatorEnum.__doc__ == LOGICAL_OPERATOR_ENUM_NOTE

    def test_literal_declaration_order_follows_xsd_simple_type(self):
        # Literal descriptions + atp.EnumerationLiteralIndex tags are inline comments
        # in the class body (FirewallActionEnum precedent — class attributes cannot
        # carry docstrings).
        values = DiagnosticLogicalOperatorEnum().getEnumValues()
        assert values.index(DiagnosticLogicalOperatorEnum.LOGICAL_AND) == 0
        assert values.index(DiagnosticLogicalOperatorEnum.LOGICAL_OR) == 1


class Test_DiagnosticCompareTypeEnum:
    """Test cases for DiagnosticCompareTypeEnum (Table 4.40, p.83)."""

    def test_instantiation_and_displayed_order(self):
        enum = DiagnosticCompareTypeEnum()
        assert enum.getEnumValues() == (
            "isEqual",
            "isGreaterOrEqual",
            "isGreaterThan",
            "isLessOrEqual",
            "isLessThan",
            "isNotEqual",
        )

    def test_literal_members(self):
        assert DiagnosticCompareTypeEnum.IS_EQUAL == "isEqual"
        assert DiagnosticCompareTypeEnum.IS_GREATER_OR_EQUAL == "isGreaterOrEqual"
        assert DiagnosticCompareTypeEnum.IS_GREATER_THAN == "isGreaterThan"
        assert DiagnosticCompareTypeEnum.IS_LESS_OR_EQUAL == "isLessOrEqual"
        assert DiagnosticCompareTypeEnum.IS_LESS_THAN == "isLessThan"
        assert DiagnosticCompareTypeEnum.IS_NOT_EQUAL == "isNotEqual"

    def test_validate_enum_value(self):
        enum = DiagnosticCompareTypeEnum()
        assert enum.validateEnumValue("isEqual") is True
        assert enum.validateEnumValue("invalid") is False

    def test_instantiable_and_value_round_trip(self):
        enum = DiagnosticCompareTypeEnum()
        enum.setValue(DiagnosticCompareTypeEnum.IS_GREATER_THAN)
        assert enum.getValue() == "isGreaterThan"

    def test_class_docstring_is_spec_note_verbatim(self):
        assert DiagnosticCompareTypeEnum.__doc__ == COMPARE_TYPE_ENUM_NOTE


class Test_DiagnosticEnvCompareCondition:
    """Test cases for DiagnosticEnvCompareCondition (Table 4.39, p.82)."""

    def test_is_abstract(self):
        with pytest.raises(TypeError):
            DiagnosticEnvCompareCondition()

    def test_concrete_subclass_get_set_compare_type(self):
        class _ConcreteCompareCondition(DiagnosticEnvCompareCondition):
            pass

        condition = _ConcreteCompareCondition()
        compare_type = DiagnosticCompareTypeEnum().setValue(DiagnosticCompareTypeEnum.IS_GREATER_THAN)
        result = condition.setCompareType(compare_type)
        assert result is condition
        assert condition.getCompareType() == compare_type
        assert condition.setCompareType(None) is condition
        assert condition.getCompareType() == compare_type

    def test_compare_condition_round_trips_inside_formula(self):
        import xml.etree.cElementTree as ET

        from armodel.parser.arxml_parser import ARXMLParser
        from armodel.writer.arxml_writer import ARXMLWriter

        class _ConcreteCompareCondition(DiagnosticEnvCompareCondition):
            pass

        formula = DiagnosticEnvConditionFormula()
        condition = _ConcreteCompareCondition()
        condition.setCompareType(DiagnosticCompareTypeEnum().setValue(DiagnosticCompareTypeEnum.IS_EQUAL))
        formula.addPart(condition)

        # NOTE: the XSD formula PARTS choice wires only the CONCRETE condition elements
        # (DIAGNOSTIC-ENV-DATA-CONDITION etc.); the abstract CompareCondition has no own
        # element, so the reusable helpers are exercised directly here.
        parent = ET.Element("DIAGNOSTIC-ENV-COMPARE-CONDITION")
        ARXMLWriter().writeDiagnosticEnvCompareCondition(parent, condition)
        assert parent.find("COMPARE-TYPE").text == "IS-EQUAL"

        xml_text = ET.tostring(parent, encoding="unicode")
        reloaded = ET.fromstring("<ROOT xmlns='http://autosar.org/schema/r4.0'>%s</ROOT>" % xml_text)
        parsed = _ConcreteCompareCondition()
        ARXMLParser().readDiagnosticEnvCompareCondition(reloaded[0], parsed)
        assert parsed.getCompareType().getValue() == "isEqual"


class Test_DiagnosticEnvDataCondition:
    """Test cases for DiagnosticEnvDataCondition (Table 4.41, p.84)."""

    CLASS_DOCSTRING = (
        "A DiagnosticEnvDataCondition is an atomic condition that compares the current value of the referenced DiagnosticDataElement "
        "with a constant value defined by the ValueSpecification. All compareTypes are supported.\n"
        "\n"
        "[constr_1802] Existence of DiagnosticEnvDataCondition.compareValue: For each DiagnosticEnvDataCondition, that attribute "
        "compareValue shall exist at the time when the DEXT is complete.\n"
        "\n"
        "[constr_1803] Existence of DiagnosticEnvDataCondition.dataElement: For each DiagnosticEnvDataCondition, that attribute "
        "dataElement shall exist at the time when the DEXT is complete."
    )
    COMPARE_VALUE_NOTE = "This attribute represents a fixed compare value taken to evaluate the compare condition."
    DATA_ELEMENT_NOTE = "This reference represents the related diagnostic data element."

    def test_is_concrete(self):
        condition = DiagnosticEnvDataCondition()
        assert condition is not None

    def test_is_diagnostic_env_compare_condition_subclass(self):
        assert issubclass(DiagnosticEnvDataCondition, DiagnosticEnvCompareCondition)
        assert issubclass(DiagnosticEnvDataCondition, DiagnosticEnvConditionFormulaPart)
        assert issubclass(DiagnosticEnvDataCondition, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        assert inspect.cleandoc(DiagnosticEnvDataCondition.__doc__) == self.CLASS_DOCSTRING

    def test_init_has_no_docstring(self):
        assert DiagnosticEnvDataCondition.__init__.__doc__ is None

    def test_defaults(self):
        condition = DiagnosticEnvDataCondition()
        assert condition.getCompareValue() is None
        assert condition.getDataElementRef() is None
        assert condition.getCompareType() is None

    def test_get_set_compare_value(self):
        condition = DiagnosticEnvDataCondition()
        value_spec = TextValueSpecification()
        literal = ARLiteral()
        literal.setValue("42")
        value_spec.setValue(literal)
        assert condition.setCompareValue(value_spec) is condition
        assert condition.getCompareValue() is value_spec
        condition.setCompareValue(None)
        assert condition.getCompareValue() is value_spec

    def test_get_set_data_element_ref(self):
        condition = DiagnosticEnvDataCondition()
        ref = RefType()
        ref.setDest("DIAGNOSTIC-DATA-ELEMENT")
        ref.setValue("/AUTOSAR/DiagDataElements/Dde1")
        assert condition.setDataElementRef(ref) is condition
        assert condition.getDataElementRef() is ref
        condition.setDataElementRef(None)
        assert condition.getDataElementRef() is ref

    def test_inherited_compare_type(self):
        condition = DiagnosticEnvDataCondition()
        compare_type = DiagnosticCompareTypeEnum().setValue(DiagnosticCompareTypeEnum.IS_LESS_OR_EQUAL)
        condition.setCompareType(compare_type)
        assert condition.getCompareType() is compare_type

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        assert inspect.cleandoc(DiagnosticEnvDataCondition.getCompareValue.__doc__) == self.COMPARE_VALUE_NOTE
        assert inspect.cleandoc(DiagnosticEnvDataCondition.setCompareValue.__doc__) == (self.COMPARE_VALUE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing compareValue.")
        assert inspect.cleandoc(DiagnosticEnvDataCondition.getDataElementRef.__doc__) == self.DATA_ELEMENT_NOTE
        assert inspect.cleandoc(DiagnosticEnvDataCondition.setDataElementRef.__doc__) == (self.DATA_ELEMENT_NOTE + "\n\nA None value is a no-op and does not overwrite an existing dataElementRef.")


class Test_DiagnosticEnvDataElementCondition:
    """Test cases for DiagnosticEnvDataElementCondition (Table 4.42, p.85)."""

    CLASS_DOCSTRING = (
        "This meta-class represents the ability to formulate a diagnostic environment condition based on the value of a data element owned by the application software.\n"
        "\n"
        "[constr_10115] Existence of attributes of DiagnosticEnvDataElementCondition if the reference in the role dataPrototype exists: If the reference in the role "
        "DiagnosticEnvDataElementCondition.dataPrototype exists, then the aggregation in the role compareValue shall exist and the aggregation in the role "
        "swDataDefProps shall not exist at the time when the DEXT is complete.\n"
        "\n"
        "[constr_10116] Existence of attributes of DiagnosticEnvDataElementCondition if the reference in the role dataPrototype does not exist: If the reference in the "
        "role DiagnosticEnvDataElementCondition.dataPrototype does not exist, then the aggregations in the role compareValue and swDataDefProps shall exist at the "
        "time when the DEXT is complete.\n"
        "\n"
        "[constr_10117] Existence of attributes of DiagnosticEnvDataElementCondition.swDataDefProps: baseType 1, compuMethod 0..1, dataConstr 0..1. This rule shall be "
        "imposed at the time when the DEXT is complete."
    )
    COMPARE_VALUE_NOTE = "This aggregation represents the definition of the compare value against which the value taken from the application software shall be compared."
    DATA_PROTOTYPE_NOTE = "This instanceRef represent the ability to access a data element owned by the application software on the AUTOSAR classic platform. InstanceRef implemented by: DataPrototypeInSystemInstanceRef"
    SW_DATA_DEF_PROPS_NOTE = "Via this aggregation it is possible to describe the properties of the data that is obtained from the application for the environmental condition."

    def test_is_concrete(self):
        condition = DiagnosticEnvDataElementCondition()
        assert condition is not None

    def test_is_diagnostic_env_compare_condition_subclass(self):
        assert issubclass(DiagnosticEnvDataElementCondition, DiagnosticEnvCompareCondition)
        assert issubclass(DiagnosticEnvDataElementCondition, DiagnosticEnvConditionFormulaPart)
        assert issubclass(DiagnosticEnvDataElementCondition, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        assert inspect.cleandoc(DiagnosticEnvDataElementCondition.__doc__) == self.CLASS_DOCSTRING

    def test_init_has_no_docstring(self):
        assert DiagnosticEnvDataElementCondition.__init__.__doc__ is None

    def test_defaults(self):
        condition = DiagnosticEnvDataElementCondition()
        assert condition.getCompareValue() is None
        assert condition.getDataPrototypeIRef() is None
        assert condition.getSwDataDefProps() is None
        assert condition.getCompareType() is None

    def test_get_set_compare_value(self):
        condition = DiagnosticEnvDataElementCondition()
        value_spec = TextValueSpecification()
        literal = ARLiteral()
        literal.setValue("42")
        value_spec.setValue(literal)
        assert condition.setCompareValue(value_spec) is condition
        assert condition.getCompareValue() is value_spec
        condition.setCompareValue(None)
        assert condition.getCompareValue() is value_spec

    def test_get_set_data_prototype_iref(self):
        condition = DiagnosticEnvDataElementCondition()
        ref = RefType()
        ref.setDest("VARIABLE-DATA-PROTOTYPE")
        ref.setValue("/AUTOSAR/RootSwComposition/Comp1/Vdp1")
        assert condition.setDataPrototypeIRef(ref) is condition
        assert condition.getDataPrototypeIRef() is ref
        condition.setDataPrototypeIRef(None)
        assert condition.getDataPrototypeIRef() is ref

    def test_get_set_sw_data_def_props(self):
        condition = DiagnosticEnvDataElementCondition()
        props = SwDataDefProps()
        base_type_ref = RefType()
        base_type_ref.setDest("SW-BASE-TYPE")
        base_type_ref.setValue("/DataTypes/BaseTypes/uint8")
        props.setBaseTypeRef(base_type_ref)
        assert condition.setSwDataDefProps(props) is condition
        assert condition.getSwDataDefProps() is props
        assert condition.getSwDataDefProps().getBaseTypeRef().getValue() == "/DataTypes/BaseTypes/uint8"
        condition.setSwDataDefProps(None)
        assert condition.getSwDataDefProps() is props

    def test_inherited_compare_type(self):
        condition = DiagnosticEnvDataElementCondition()
        compare_type = DiagnosticCompareTypeEnum().setValue(DiagnosticCompareTypeEnum.IS_EQUAL)
        condition.setCompareType(compare_type)
        assert condition.getCompareType() is compare_type

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        assert inspect.cleandoc(DiagnosticEnvDataElementCondition.getCompareValue.__doc__) == self.COMPARE_VALUE_NOTE
        assert inspect.cleandoc(DiagnosticEnvDataElementCondition.setCompareValue.__doc__) == (self.COMPARE_VALUE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing compareValue.")
        assert inspect.cleandoc(DiagnosticEnvDataElementCondition.getDataPrototypeIRef.__doc__) == self.DATA_PROTOTYPE_NOTE
        assert inspect.cleandoc(DiagnosticEnvDataElementCondition.setDataPrototypeIRef.__doc__) == (
            self.DATA_PROTOTYPE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing dataPrototypeIRef."
        )
        assert inspect.cleandoc(DiagnosticEnvDataElementCondition.getSwDataDefProps.__doc__) == self.SW_DATA_DEF_PROPS_NOTE
        assert inspect.cleandoc(DiagnosticEnvDataElementCondition.setSwDataDefProps.__doc__) == (
            self.SW_DATA_DEF_PROPS_NOTE + "\n\nA None value is a no-op and does not overwrite an existing swDataDefProps."
        )


class Test_DiagnosticEnvModeCondition:
    """Test cases for DiagnosticEnvModeCondition (Table 4.43, p.89)."""

    CLASS_DOCSTRING = (
        "DiagnosticEnvModeCondition are atomic condition based on the comparison of the active Mode Declaration in a ModeDeclarationGroupProtoype with the constant "
        "value of a ModeDeclaration. The formulation of this condition uses only one DiagnosticEnvElement, which contains enough information to deduce the variable "
        "part (i.e. the part that changes at runtime) as well as the constant part of the comparison. Only DiagnosticCompareTypeEnum.isEqual or "
        "DiagnosticCompareTypeEnum.isNotEqual are eligible values for DiagnosticAtomicCondition.compareType.\n"
        "\n"
        "[constr_1804] Existence of DiagnosticEnvModeCondition.modeElement: For each DiagnosticEnvModeCondition, that attribute modeElement shall exist at the time "
        "when the DEXT is complete."
    )
    MODE_ELEMENT_NOTE = "This reference represents both the ModeDeclarationGroupPrototype and the ModeDeclaration relevant for the mode comparison."

    def test_is_concrete(self):
        condition = DiagnosticEnvModeCondition()
        assert condition is not None

    def test_is_diagnostic_env_compare_condition_subclass(self):
        assert issubclass(DiagnosticEnvModeCondition, DiagnosticEnvCompareCondition)
        assert issubclass(DiagnosticEnvModeCondition, DiagnosticEnvConditionFormulaPart)
        assert issubclass(DiagnosticEnvModeCondition, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        assert inspect.cleandoc(DiagnosticEnvModeCondition.__doc__) == self.CLASS_DOCSTRING

    def test_init_has_no_docstring(self):
        assert DiagnosticEnvModeCondition.__init__.__doc__ is None

    def test_defaults(self):
        condition = DiagnosticEnvModeCondition()
        assert condition.getModeElementRef() is None
        assert condition.getCompareType() is None

    def test_get_set_mode_element_ref(self):
        condition = DiagnosticEnvModeCondition()
        ref = RefType()
        ref.setDest("DIAGNOSTIC-ENV-BSW-MODE-ELEMENT")
        ref.setValue("/AUTOSAR/DiagEnvConditions/Env1/ModeElements/BswMode1")
        assert condition.setModeElementRef(ref) is condition
        assert condition.getModeElementRef() is ref
        condition.setModeElementRef(None)
        assert condition.getModeElementRef() is ref

    def test_inherited_compare_type(self):
        condition = DiagnosticEnvModeCondition()
        compare_type = DiagnosticCompareTypeEnum().setValue(DiagnosticCompareTypeEnum.IS_EQUAL)
        condition.setCompareType(compare_type)
        assert condition.getCompareType() is compare_type

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        assert inspect.cleandoc(DiagnosticEnvModeCondition.getModeElementRef.__doc__) == self.MODE_ELEMENT_NOTE
        assert inspect.cleandoc(DiagnosticEnvModeCondition.setModeElementRef.__doc__) == (self.MODE_ELEMENT_NOTE + "\n\nA None value is a no-op and does not overwrite an existing modeElementRef.")


class Test_DiagnosticEnvSwcModeElement:
    """Test cases for DiagnosticEnvSwcModeElement (Table 4.45, p.89)."""

    CLASS_DOCSTRING = (
        "This meta-class represents the ability to refer to a ModeDeclaration in a concrete System context.\n"
        "\n"
        "[constr_1805] Existence of DiagnosticEnvSwcModeElement.mode: For each DiagnosticEnvSwcModeElement, that attribute mode shall exist at the time when the DEXT is complete."
    )
    MODE_NOTE = "This reference identifies both the ModeDeclarationGroupPrototype and the ModeDeclaration for the specific mode comparison. InstanceRef implemented by: PModeInSystemInstanceRef"

    def _create(self):
        document = AUTOSAR.getInstance()
        package = document.createARPackage("EnvConds")
        return package.createDiagnosticEnvironmentalCondition("Env1")

    def test_is_concrete(self):
        env_condition = self._create()
        mode_element = DiagnosticEnvSwcModeElement(env_condition, "SwcMode1")
        assert mode_element is not None

    def test_is_diagnostic_env_mode_element_subclass(self):
        assert issubclass(DiagnosticEnvSwcModeElement, DiagnosticEnvModeElement)
        assert issubclass(DiagnosticEnvSwcModeElement, Referrable)
        assert issubclass(DiagnosticEnvSwcModeElement, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        assert inspect.cleandoc(DiagnosticEnvSwcModeElement.__doc__) == self.CLASS_DOCSTRING

    def test_init_has_no_docstring(self):
        assert DiagnosticEnvSwcModeElement.__init__.__doc__ is None

    def test_short_name_and_parent(self):
        env_condition = self._create()
        mode_element = DiagnosticEnvSwcModeElement(env_condition, "SwcMode1")
        assert mode_element.getShortName() == "SwcMode1"
        assert mode_element.getParent() is env_condition

    def test_defaults(self):
        env_condition = self._create()
        mode_element = DiagnosticEnvSwcModeElement(env_condition, "SwcMode1")
        assert mode_element.getModeIRef() is None

    def test_get_set_mode_iref(self):
        env_condition = self._create()
        mode_element = DiagnosticEnvSwcModeElement(env_condition, "SwcMode1")
        ref = RefType()
        ref.setDest("MODE-DECLARATION")
        ref.setValue("/AUTOSAR/ModeDcls/MDG1/Normal")
        assert mode_element.setModeIRef(ref) is mode_element
        assert mode_element.getModeIRef() is ref
        mode_element.setModeIRef(None)
        assert mode_element.getModeIRef() is ref

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        assert inspect.cleandoc(DiagnosticEnvSwcModeElement.getModeIRef.__doc__) == self.MODE_NOTE
        assert inspect.cleandoc(DiagnosticEnvSwcModeElement.setModeIRef.__doc__) == (self.MODE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing modeIRef.")


class Test_DiagnosticEnvBswModeElement:
    """Test cases for DiagnosticEnvBswModeElement (Table 4.46, p.90)."""

    CLASS_DOCSTRING = (
        "This meta-class represents the ability to refer to a specific ModeDeclaration in the scope of a BswModuleDescription.\n"
        "\n"
        "[constr_1806] Existence of DiagnosticEnvBswModeElement.mode: For each DiagnosticEnvBswModeElement, that attribute mode shall exist at the time when the DEXT is complete."
    )
    MODE_NOTE = (
        "This reference identifies both the ModeDeclarationGroupPrototype and the ModeDeclaration for the specific mode comparison. InstanceRef implemented by: ModeInBswModuleDescriptionInstanceRef"
    )

    def _create(self):
        document = AUTOSAR.getInstance()
        package = document.createARPackage("EnvConds")
        return package.createDiagnosticEnvironmentalCondition("Env1")

    def test_is_concrete(self):
        env_condition = self._create()
        mode_element = DiagnosticEnvBswModeElement(env_condition, "BswMode1")
        assert mode_element is not None

    def test_is_diagnostic_env_mode_element_subclass(self):
        assert issubclass(DiagnosticEnvBswModeElement, DiagnosticEnvModeElement)
        assert issubclass(DiagnosticEnvBswModeElement, Referrable)
        assert issubclass(DiagnosticEnvBswModeElement, ARObject)

    def test_class_docstring_is_spec_note_verbatim(self):
        assert inspect.cleandoc(DiagnosticEnvBswModeElement.__doc__) == self.CLASS_DOCSTRING

    def test_init_has_no_docstring(self):
        assert DiagnosticEnvBswModeElement.__init__.__doc__ is None

    def test_short_name_and_parent(self):
        env_condition = self._create()
        mode_element = DiagnosticEnvBswModeElement(env_condition, "BswMode1")
        assert mode_element.getShortName() == "BswMode1"
        assert mode_element.getParent() is env_condition

    def test_defaults(self):
        env_condition = self._create()
        mode_element = DiagnosticEnvBswModeElement(env_condition, "BswMode1")
        assert mode_element.getModeIRef() is None

    def test_get_set_mode_iref(self):
        env_condition = self._create()
        mode_element = DiagnosticEnvBswModeElement(env_condition, "BswMode1")
        ref = RefType()
        ref.setDest("MODE-DECLARATION")
        ref.setValue("/AUTOSAR/ModeDcls/MDG1/Normal")
        assert mode_element.setModeIRef(ref) is mode_element
        assert mode_element.getModeIRef() is ref
        mode_element.setModeIRef(None)
        assert mode_element.getModeIRef() is ref

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        assert inspect.cleandoc(DiagnosticEnvBswModeElement.getModeIRef.__doc__) == self.MODE_NOTE
        assert inspect.cleandoc(DiagnosticEnvBswModeElement.setModeIRef.__doc__) == (self.MODE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing modeIRef.")
