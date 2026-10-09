"""
This module contains tests for the SecurityEventContextDataSourceEnum enumeration.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import SecurityEventContextDataSourceEnum


class TestSecurityEventContextDataSourceEnum:
    """
    Test class for SecurityEventContextDataSourceEnum functionality.
    """

    def test_member_presence_and_values(self):
        assert SecurityEventContextDataSourceEnum.USE_FIRST_CONTEXT_DATA == "USE-FIRST-CONTEXT-DATA"
        assert SecurityEventContextDataSourceEnum.USE_LAST_CONTEXT_DATA == "USE-LAST-CONTEXT-DATA"

    def test_instantiability(self):
        obj = SecurityEventContextDataSourceEnum()
        assert isinstance(obj, SecurityEventContextDataSourceEnum)
        obj.setValue(SecurityEventContextDataSourceEnum.USE_FIRST_CONTEXT_DATA)
        assert obj.getValue() == "USE-FIRST-CONTEXT-DATA"
