"""
Test suite for TimingCondition (CP_TPS_TimingExtensions Table 3.7, p.35, R23-11).

Validates the member defaults, getter/setter round-trips (None no-ops), the
verbatim class-level spec Note and the member declaration order (markdown
displayed row order) of the TimingCondition model class.
"""

import ast
import importlib
import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition import (
    TimingCondition,
    TimingConditionFormula,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable

CLASS_NOTE = "A TimingCondition describes a dependency on a specific condition. The element owns an expression which describes the timing condition dependency."

FORMULA_NOTE = "This is the expression describing the dependency on a specific condition."


class TestTimingCondition:
    def _create_condition(self) -> TimingCondition:
        return TimingCondition(AUTOSAR.getInstance(), "Cond1")

    def test_inheritance(self):
        assert issubclass(TimingCondition, Identifiable)

    def test_concrete_class_instantiable(self):
        condition = self._create_condition()
        assert isinstance(condition, Identifiable)
        assert condition.getShortName() == "Cond1"

    def test_class_docstring_note(self):
        assert inspect.cleandoc(TimingCondition.__doc__) == CLASS_NOTE

    def test_initialization(self):
        condition = self._create_condition()

        assert condition.getShortName() == "Cond1"
        assert condition.getTimingConditionFormula() is None

    def test_member_annotations_and_declaration_order(self):
        module = importlib.import_module("armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition")
        module_source = open(module.__file__, encoding="utf-8").read()
        tree = ast.parse(module_source)
        cls = next(n for n in ast.walk(tree) if isinstance(n, ast.ClassDef) and n.name == "TimingCondition")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = [(st.target.attr, ast.get_source_segment(module_source, st.annotation)) for st in ast.walk(init) if isinstance(st, ast.AnnAssign)]

        assert annotations == [
            ("timingConditionFormula", "Optional[TimingConditionFormula]"),
        ]

    def test_member_accessor_type_hints(self):
        assert typing.get_type_hints(TimingCondition.getTimingConditionFormula).get("return") == typing.Optional[TimingConditionFormula]
        assert typing.get_type_hints(TimingCondition.setTimingConditionFormula).get("value") == typing.Optional[TimingConditionFormula]
        assert typing.get_type_hints(TimingCondition.setTimingConditionFormula).get("return") is TimingCondition

    def test_member_docstrings_are_verbatim_spec_notes(self):
        assert inspect.cleandoc(TimingCondition.getTimingConditionFormula.__doc__) == FORMULA_NOTE
        assert inspect.cleandoc(TimingCondition.setTimingConditionFormula.__doc__) == FORMULA_NOTE + "\n\nA None value is a no-op and does not overwrite an existing timingConditionFormula."

    def test_get_set_timing_condition_formula(self):
        condition = self._create_condition()

        formula = TimingConditionFormula()
        assert condition.setTimingConditionFormula(formula) is condition
        assert condition.getTimingConditionFormula() is formula

        assert condition.setTimingConditionFormula(None) is condition
        assert condition.getTimingConditionFormula() is formula
