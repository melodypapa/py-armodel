"""
This module contains tests for the SeverityEnum enumeration.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import SeverityEnum


class TestSeverityEnum:
    def test_member_presence_and_values(self):
        assert SeverityEnum.ERROR == "ERROR"
        assert SeverityEnum.INFO == "INFO"
        assert SeverityEnum.WARNING == "WARNING"
        assert SeverityEnum.NO_SHOW_CONTENT == "NO-SHOW-CONTENT"
        assert SeverityEnum.SHOW_CONTENT == "SHOW-CONTENT"

    def test_instantiability(self):
        obj = SeverityEnum()
        assert isinstance(obj, SeverityEnum)
        obj.setValue(SeverityEnum.ERROR)
        assert obj.getValue() == "ERROR"
