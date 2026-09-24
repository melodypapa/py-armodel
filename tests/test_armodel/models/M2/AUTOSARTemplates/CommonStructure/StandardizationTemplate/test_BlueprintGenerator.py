"""
Tests for the BlueprintGenerator class in the
AUTOSAR CommonStructure.StandardizationTemplate.BlueprintGenerator module.
"""

import inspect
import re

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintGenerator import (
    BlueprintGenerator,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    VerbatimString,
)
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock


class TestBlueprintGenerator:
    """
    Test class for BlueprintGenerator functionality.
    """

    def test_initialization(self):
        obj = BlueprintGenerator()
        assert obj.getExpression() is None
        assert obj.getIntroduction() is None

    def test_set_get_expression(self):
        obj = BlueprintGenerator()
        expression = VerbatimString().setValue("some ARMQL")
        assert obj.setExpression(expression) is obj
        assert obj.getExpression() == expression

    def test_set_expression_none_is_noop(self):
        obj = BlueprintGenerator()
        expression = VerbatimString().setValue("some ARMQL")
        obj.setExpression(expression)
        obj.setExpression(None)
        assert obj.getExpression() == expression

    def test_set_get_introduction(self):
        obj = BlueprintGenerator()
        introduction = DocumentationBlock()
        assert obj.setIntroduction(introduction) is obj
        assert obj.getIntroduction() == introduction

    def test_set_introduction_none_is_noop(self):
        obj = BlueprintGenerator()
        introduction = DocumentationBlock()
        obj.setIntroduction(introduction)
        obj.setIntroduction(None)
        assert obj.getIntroduction() == introduction


class TestBlueprintGeneratorSpecContract:
    """
    Spec-contract pins for BlueprintGenerator (R23-11 AUTOSAR_FO_TPS_GenericStructureTemplate
    Table E.12, pp.424-425; appendix E caption-shift: the body renders above the caption,
    main fragment p.424, introduction continuation + caption p.425). Field-to-spec
    cross-check both directions: exactly TWO attributes, expression (VerbatimString,
    0..1, attr) and introduction (DocumentationBlock, 0..1, aggr).
    """

    def test_class_docstring_verbatim(self):
        """
        Rule 0001.4 / 0012.2.4: class docstring == spec Table E.12 Note verbatim
        (the "Tags: atp.Status=valid" tail is stripped; spec wording "express" kept).
        """
        note = "This class express the Extended Language to generate blueprint derivates in complex descriptions."
        assert BlueprintGenerator.__doc__ == note

    def test_exact_own_field_set(self):
        """
        Rule 0001.3 / 0001.11: __init__ declares EXACTLY the two spec attributes
        (expression, introduction) in the markdown displayed row order and nothing else.
        """
        fields = re.findall(r"self\.(\w+)\s*:", inspect.getsource(BlueprintGenerator.__init__))
        assert fields == ["expression", "introduction"]

    def test_fields_pep526_annotated_no_type_comments(self):
        """
        Rule 0003: both members are PEP 526 annotated assignments typed to their spec
        types (Optional[VerbatimString] / Optional[DocumentationBlock]), no # type: comment.
        """
        src = inspect.getsource(BlueprintGenerator.__init__)
        assert re.search(r"self\.expression\s*:\s*Optional\[VerbatimString\]\s*=\s*None", src)
        assert re.search(r"self\.introduction\s*:\s*Optional\[DocumentationBlock\]\s*=\s*None", src)
        assert "# type:" not in src

    def test_base_is_ar_object(self):
        """
        Rule 0001.2: the spec Base row is the single ARObject (XSD 00052 complexType
        BLUEPRINT-GENERATOR composes AR-OBJECT group + own group only) — most-derived
        base is ARObject, no Identifiable/Referrable in the chain.
        """
        assert BlueprintGenerator.__bases__ == (ARObject,)
        for base in (Identifiable,):
            assert base not in BlueprintGenerator.__mro__

    def test_accessor_order_matches_displayed_rows(self):
        """
        Rule 0001.11: accessors are declared get -> set per attribute in the markdown
        displayed attribute row order (expression first, introduction second).
        """
        accessors = re.findall(r"def (get\w+|set\w+|create\w+|add\w+)", inspect.getsource(BlueprintGenerator))
        assert accessors == ["getExpression", "setExpression", "getIntroduction", "setIntroduction"]

    def test_get_expression_docstring_verbatim(self):
        """Rule 0012.2.5: the getter docstring is the spec attribute Note verbatim."""
        note = "This represents a formal term in the expression based on the extended language."
        assert BlueprintGenerator.getExpression.__doc__ == note

    def test_set_expression_docstring_note_plus_none_noop(self):
        """Rule 0012.2.5: the setter docstring is the Note verbatim + the None-no-op sentence."""
        note = "This represents a formal term in the expression based on the extended language."
        assert BlueprintGenerator.setExpression.__doc__ == note + " A None value is a no-op and does not overwrite an existing expression."

    def test_get_introduction_docstring_verbatim(self):
        """Rule 0012.2.5: the getter docstring is the spec attribute Note verbatim."""
        note = "This represents a description that documents how the blueprint generator shall be resolved when deriving objects from blueprints."
        assert BlueprintGenerator.getIntroduction.__doc__ == note

    def test_set_introduction_docstring_note_plus_none_noop(self):
        """Rule 0012.2.5: the setter docstring is the Note verbatim + the None-no-op sentence."""
        note = "This represents a description that documents how the blueprint generator shall be resolved when deriving objects from blueprints."
        assert BlueprintGenerator.setIntroduction.__doc__ == note + " A None value is a no-op and does not overwrite an existing introduction."

    def test_init_inline_comments_verbatim(self):
        """Rule 0012.2.5: the inline __init__ member comments are the spec Notes verbatim."""
        src = inspect.getsource(BlueprintGenerator.__init__)
        assert "# This represents a formal term in the expression based on the extended language." in src
        assert "# This represents a description that documents how the blueprint generator shall be resolved when deriving objects from blueprints." in src
