"""
This module contains tests for the SecurityEventReportingModeEnum enumeration.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import SecurityEventReportingModeEnum


class TestSecurityEventReportingModeEnum:
    """
    Test class for SecurityEventReportingModeEnum functionality.
    """

    def test_member_presence_and_values(self):
        assert SecurityEventReportingModeEnum.BRIEF == "BRIEF"
        assert SecurityEventReportingModeEnum.BRIEF_BYPASSING_FILTERS == "BRIEF-BYPASSING-FILTERS"
        assert SecurityEventReportingModeEnum.DETAILED == "DETAILED"
        assert SecurityEventReportingModeEnum.DETAILED_BYPASSING_FILTERS == "DETAILED-BYPASSING-FILTERS"
        assert SecurityEventReportingModeEnum.OFF == "OFF"

    def test_instantiability(self):
        obj = SecurityEventReportingModeEnum()
        assert isinstance(obj, SecurityEventReportingModeEnum)
        obj.setValue(SecurityEventReportingModeEnum.BRIEF)
        assert obj.getValue() == "BRIEF"
