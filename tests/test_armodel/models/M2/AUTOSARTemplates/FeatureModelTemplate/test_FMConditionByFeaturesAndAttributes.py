"""
Tests for the FMConditionByFeaturesAndAttributes class in the
AUTOSAR FeatureModelTemplate module.
"""

import inspect
import re

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate import FMConditionByFeaturesAndAttributes, FMFormulaByFeaturesAndAttributes
from armodel.models.M2.AUTOSARTemplates.GenericStructure.FormulaLanguage import FormulaExpression
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import AtpMixedString


class TestFMConditionByFeaturesAndAttributes:
    """
    Test class for FMConditionByFeaturesAndAttributes functionality.
    """

    def test_initialization(self):
        obj = FMConditionByFeaturesAndAttributes()
        assert obj.getMixedString() is None
        assert obj.getAtpReferences() == []
        assert obj.getAtpStringReferences() == []

    def test_concrete_class_instantiable(self):
        obj = FMConditionByFeaturesAndAttributes()
        assert obj is not None

    def test_inherited_mixed_string_accessors(self):
        obj = FMConditionByFeaturesAndAttributes()
        assert obj.setMixedString("feature_a and feature_b") is obj
        assert obj.getMixedString() == "feature_a and feature_b"

    def test_set_mixed_string_none_is_noop(self):
        obj = FMConditionByFeaturesAndAttributes()
        obj.setMixedString("feature_a")
        obj.setMixedString(None)
        assert obj.getMixedString() == "feature_a"

    def test_inherited_base_accessors(self):
        """
        The spec Base chain is live: the abstract FormulaExpression accessors
        (atpReferences / atpStringReferences) work on the concrete subclass.
        """
        parent = AUTOSAR.getInstance()
        reference = parent.createARPackage("AUTOSAR")
        obj = FMConditionByFeaturesAndAttributes()
        assert obj.addAtpReference(reference) is obj
        assert obj.getAtpReferences() == [reference]
        assert obj.addAtpReference(None) is obj
        assert obj.getAtpReferences() == [reference]
        assert obj.getAtpStringReferences() == []


class TestFMConditionByFeaturesAndAttributesSpecContract:
    """
    Spec-contract pins for FMConditionByFeaturesAndAttributes (R23-11
    AUTOSAR_FO_TPS_FeatureModelExchangeFormat Table 7.2, p.62). Field-to-spec
    cross-check both directions: the table has NO attribute rows (the `-` row) —
    exactly ZERO own attributes; the content is the <<atpMixedString>> text plus
    the inherited FormulaExpression reference lists.
    """

    def test_class_docstring_verbatim(self):
        """
        Rule 0001.4 / 0012.2.4: class docstring == spec Table 7.2 Note verbatim.
        """
        note = "A boolean expression that has the syntax of the AUTOSAR formula language but uses only references to features or feature attributes (not system constants) as operands."
        assert FMConditionByFeaturesAndAttributes.__doc__ == note

    def test_exact_own_field_set(self):
        """
        Rule 0001.3 / 0001.11: Table 7.2 declares no attribute rows — __init__
        declares EXACTLY zero own fields.
        """
        fields = re.findall(r"self\.(\w+)\s*:", inspect.getsource(FMConditionByFeaturesAndAttributes.__init__))
        assert fields == []

    def test_init_no_type_comments(self):
        """
        Rule 0003: no # type: comments anywhere in __init__.
        """
        src = inspect.getsource(FMConditionByFeaturesAndAttributes.__init__)
        assert "# type:" not in src

    def test_base_chain(self):
        """
        Rule 0001.2: the spec Base row is ARObject, FMFormulaByFeaturesAndAttributes,
        FormulaExpression. Re-base applied 2026-09-26 (Rule 0012.3): the most-derived
        base FMFormulaByFeaturesAndAttributes is now synced (Table 7.1) and is the
        direct Python base; the ARObject, AtpMixedString (<<atpMixedString>>) and
        FormulaExpression ancestry stays in the MRO.
        """
        assert FMConditionByFeaturesAndAttributes.__bases__ == (FMFormulaByFeaturesAndAttributes,)
        for base in (ARObject, AtpMixedString, FormulaExpression):
            assert base in FMConditionByFeaturesAndAttributes.__mro__

    def test_no_own_accessors(self):
        """
        Rule 0001.11: zero attribute rows — the class declares no own
        accessors (get/setMixedString come from the AtpMixedString mixin and
        get/addAtpReference(s) from FormulaExpression).
        """
        accessors = re.findall(r"def (get\w+|set\w+|create\w+|add\w+)", inspect.getsource(FMConditionByFeaturesAndAttributes))
        assert accessors == []

    def test_no_init_docstring(self):
        """Rule 0012.2.5.2: __init__ carries no docstring."""
        assert FMConditionByFeaturesAndAttributes.__init__.__doc__ is None
