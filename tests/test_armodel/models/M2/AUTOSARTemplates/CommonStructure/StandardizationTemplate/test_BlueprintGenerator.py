"""
Tests for the BlueprintGenerator class in the
AUTOSAR CommonStructure.StandardizationTemplate.BlueprintGenerator module.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintGenerator import (
    BlueprintGenerator,
)
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
