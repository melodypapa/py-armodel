"""Model tests for DiagnosticExtract EnvironmentalCondition classes.

DiagnosticEnvironmentalCondition (Table 4.35, p.79) with its in-pass closure:
DiagnosticEnvConditionFormula (Table 4.36), DiagnosticLogicalOperatorEnum
(Table 4.37), DiagnosticEnvConditionFormulaPart (Table 4.38) and
DiagnosticEnvModeElement (Table 4.44).
"""

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import DiagnosticCommonElement
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.EnvironmentalCondition import (
    DiagnosticEnvConditionFormula,
    DiagnosticEnvConditionFormulaPart,
    DiagnosticEnvironmentalCondition,
    DiagnosticEnvModeElement,
    DiagnosticLogicalOperatorEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable, Referrable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger

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
