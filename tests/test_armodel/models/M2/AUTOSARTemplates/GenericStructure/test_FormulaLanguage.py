from abc import ABC

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.FormulaLanguage import FormulaExpression
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Referrable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import AtpMixedString


class _RefProbe(Referrable):
    """Probe subclass — Referrable itself is abstract."""


class _ConcreteFormulaExpression(FormulaExpression):
    """Probe subclass — FormulaExpression itself is abstract (spec: abstract)."""


class TestFormulaExpression:
    def test_abstract(self):
        assert issubclass(FormulaExpression, AtpMixedString)
        assert issubclass(FormulaExpression, ARObject)
        assert issubclass(FormulaExpression, ABC)
        with pytest.raises(TypeError):
            FormulaExpression()

    def test_initialization(self):
        formula = _ConcreteFormulaExpression()
        assert formula.getAtpReferences() == []
        assert formula.getAtpStringReferences() == []

    def test_add_atp_reference(self):
        formula = _ConcreteFormulaExpression()
        ref = _RefProbe(None, "ref")
        assert formula.addAtpReference(ref) is formula
        assert formula.getAtpReferences() == [ref]
        formula.addAtpReference(None)
        assert formula.getAtpReferences() == [ref]

    def test_add_atp_string_reference(self):
        formula = _ConcreteFormulaExpression()
        ref = _RefProbe(None, "ref")
        assert formula.addAtpStringReference(ref) is formula
        assert formula.getAtpStringReferences() == [ref]
        formula.addAtpStringReference(None)
        assert formula.getAtpStringReferences() == [ref]

    def test_multiple_references_appended(self):
        formula = _ConcreteFormulaExpression()
        ref1 = _RefProbe(None, "ref1")
        ref2 = _RefProbe(None, "ref2")
        formula.addAtpReference(ref1).addAtpStringReference(ref2)
        assert formula.getAtpReferences() == [ref1]
        assert formula.getAtpStringReferences() == [ref2]
