"""
This module contains tests for the DefaultValueApplicationStrategyEnum enumeration.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DefaultValueApplicationStrategyEnum


class TestDefaultValueApplicationStrategyEnum:
    def test_member_presence_and_values(self):
        assert DefaultValueApplicationStrategyEnum.DEFAULT_IF_REVISION_UPDATE == "DEFAULT-IF-REVISION-UPDATE"
        assert DefaultValueApplicationStrategyEnum.DEFAULT_IF_UNDEFINED == "DEFAULT-IF-UNDEFINED"
        assert DefaultValueApplicationStrategyEnum.NO_DEFAULT == "NO-DEFAULT"
        assert DefaultValueApplicationStrategyEnum.BUILD == "BUILD"
        assert DefaultValueApplicationStrategyEnum.CODEGENERATION == "CODEGENERATION"

    def test_instantiability(self):
        obj = DefaultValueApplicationStrategyEnum()
        assert isinstance(obj, DefaultValueApplicationStrategyEnum)
        obj.setValue(DefaultValueApplicationStrategyEnum.DEFAULT_IF_REVISION_UPDATE)
        assert obj.getValue() == "DEFAULT-IF-REVISION-UPDATE"
