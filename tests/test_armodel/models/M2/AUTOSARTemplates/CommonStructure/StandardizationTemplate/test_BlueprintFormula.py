"""
Tests for the BlueprintFormula class in the
AUTOSAR CommonStructure.StandardizationTemplate.BlueprintFormula module.
"""

import inspect
import re

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintFormula import (
    BlueprintFormula,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.FormulaLanguage import FormulaExpression
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import SwSystemconstDependentFormula
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageVerbatim


class TestBlueprintFormula:
    """
    Test class for BlueprintFormula functionality.
    """

    def test_initialization(self):
        obj = BlueprintFormula()
        assert obj.getEcucRef() is None
        assert obj.getVerbatim() is None
        assert obj.getSyscRef() is None
        assert obj.getSyscStringRef() is None

    def test_concrete_class_instantiable(self):
        obj = BlueprintFormula()
        assert obj is not None

    def test_set_get_ecuc_ref(self):
        obj = BlueprintFormula()
        ref = RefType().setValue("/EcucModuleDef/MyModule")
        assert obj.setEcucRef(ref) is obj
        assert obj.getEcucRef() == ref

    def test_set_ecuc_ref_none_is_noop(self):
        obj = BlueprintFormula()
        ref = RefType().setValue("/EcucModuleDef/MyModule")
        obj.setEcucRef(ref)
        obj.setEcucRef(None)
        assert obj.getEcucRef() == ref

    def test_set_get_verbatim(self):
        obj = BlueprintFormula()
        verbatim = MultiLanguageVerbatim()
        assert obj.setVerbatim(verbatim) is obj
        assert obj.getVerbatim() == verbatim

    def test_set_verbatim_none_is_noop(self):
        obj = BlueprintFormula()
        verbatim = MultiLanguageVerbatim()
        obj.setVerbatim(verbatim)
        obj.setVerbatim(None)
        assert obj.getVerbatim() == verbatim

    def test_inherited_base_accessors(self):
        """
        The spec Base chain is live: the abstract SwSystemconstDependentFormula
        accessors (syscRef / syscStringRef) work on the concrete subclass.
        """
        obj = BlueprintFormula()
        ref = RefType().setValue("/SwSystemconst/MyConst")
        assert obj.setSyscRef(ref) is obj
        assert obj.getSyscRef() == ref
        string_ref = RefType().setValue("/SwSystemconst/MyOtherConst")
        assert obj.setSyscStringRef(string_ref) is obj
        assert obj.getSyscStringRef() == string_ref


class TestBlueprintFormulaSpecContract:
    """
    Spec-contract pins for BlueprintFormula (R23-11 AUTOSAR_FO_TPS_StandardizationTemplate
    Table C.16, p.163; appendix C caption-shift: the body renders above the caption on the
    same page). Field-to-spec cross-check both directions: exactly TWO attributes, ecuc
    (EcucDefinitionElement, 1, ref) and verbatim (MultiLanguageVerbatim, 1, aggr).
    """

    def test_class_docstring_verbatim(self):
        """
        Rule 0001.4 / 0012.2.4: class docstring == spec Table C.16 Note verbatim
        (spec wording "express" kept).
        """
        note = "This class express the extension of the Formula Language to provide formalized blueprint-Value resp. blueprintCondition."
        assert BlueprintFormula.__doc__ == note

    def test_exact_own_field_set(self):
        """
        Rule 0001.3 / 0001.11: __init__ declares EXACTLY the two spec attributes
        (ecucRef, verbatim) in the markdown displayed row order and nothing else.
        """
        fields = re.findall(r"self\.(\w+)\s*:", inspect.getsource(BlueprintFormula.__init__))
        assert fields == ["ecucRef", "verbatim"]

    def test_fields_pep526_annotated_no_type_comments(self):
        """
        Rule 0003: both members are PEP 526 annotated assignments typed to their spec
        types (Optional[RefType] / Optional[MultiLanguageVerbatim]), no # type: comment.
        """
        src = inspect.getsource(BlueprintFormula.__init__)
        assert re.search(r"self\.ecucRef\s*:\s*Optional\[RefType\]\s*=\s*None", src)
        assert re.search(r"self\.verbatim\s*:\s*Optional\[MultiLanguageVerbatim\]\s*=\s*None", src)
        assert "# type:" not in src

    def test_base_chain(self):
        """
        Rule 0001.2: the spec Base row is ARObject, FormulaExpression,
        SwSystemconstDependentFormula — most-derived provided base is
        SwSystemconstDependentFormula (ConditionByFormula precedent); the
        FormulaExpression (atpMixedString) and ARObject ancestry is in the MRO.
        """
        assert BlueprintFormula.__bases__ == (SwSystemconstDependentFormula,)
        for base in (ARObject, FormulaExpression, SwSystemconstDependentFormula):
            assert base in BlueprintFormula.__mro__

    def test_accessor_order_matches_displayed_rows(self):
        """
        Rule 0001.11: accessors are declared get -> set per attribute in the markdown
        displayed attribute row order (ecuc first, verbatim second).
        """
        accessors = re.findall(r"def (get\w+|set\w+|create\w+|add\w+)", inspect.getsource(BlueprintFormula))
        assert accessors == ["getEcucRef", "setEcucRef", "getVerbatim", "setVerbatim"]

    def test_get_ecuc_ref_docstring_verbatim(self):
        """Rule 0012.2.5: the getter docstring is the spec attribute Note verbatim."""
        note = "The EcucDefinitionElement serves as a argument for the formular."
        assert BlueprintFormula.getEcucRef.__doc__ == note

    def test_set_ecuc_ref_docstring_note_plus_none_noop(self):
        """Rule 0012.2.5: the setter docstring is the Note verbatim + the None-no-op sentence."""
        note = "The EcucDefinitionElement serves as a argument for the formular."
        assert BlueprintFormula.setEcucRef.__doc__ == note + " A None value is a no-op and does not overwrite an existing ecucRef."

    def test_get_verbatim_docstring_verbatim(self):
        """Rule 0012.2.5: the getter docstring is the spec attribute Note verbatim."""
        note = 'This represents an informal term in the expression as verbatim text. Note that the result of this is same as formula keyword "undefined".'
        assert BlueprintFormula.getVerbatim.__doc__ == note

    def test_set_verbatim_docstring_note_plus_none_noop(self):
        """Rule 0012.2.5: the setter docstring is the Note verbatim + the None-no-op sentence."""
        note = 'This represents an informal term in the expression as verbatim text. Note that the result of this is same as formula keyword "undefined".'
        assert BlueprintFormula.setVerbatim.__doc__ == note + " A None value is a no-op and does not overwrite an existing verbatim."

    def test_init_inline_comments_verbatim(self):
        """Rule 0012.2.5: the inline __init__ member comments are the spec Notes verbatim."""
        src = inspect.getsource(BlueprintFormula.__init__)
        assert "# The EcucDefinitionElement serves as a argument for the formular." in src
        assert '# This represents an informal term in the expression as verbatim text. Note that the result of this is same as formula keyword "undefined".' in src

    def test_no_init_docstring(self):
        """Rule 0012.2.5.2: __init__ carries inline member comments, no docstring."""
        assert BlueprintFormula.__init__.__doc__ is None
