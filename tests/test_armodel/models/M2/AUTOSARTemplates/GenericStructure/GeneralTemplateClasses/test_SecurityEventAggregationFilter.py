"""
This module contains tests for the SecurityEventAggregationFilter class.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import SecurityEventAggregationFilter
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import AbstractSecurityEventFilter
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import SecurityEventContextDataSourceEnum, TimeValue


class TestSecurityEventAggregationFilter:
    """
    Test class for SecurityEventAggregationFilter functionality.
    """

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _obj(self):
        return SecurityEventAggregationFilter(self._parent(), "SecurityEventAggrega")

    def test_initialization(self):
        obj = self._obj()
        assert isinstance(obj, SecurityEventAggregationFilter)
        assert isinstance(obj, AbstractSecurityEventFilter)
        assert obj.getContextDataSource() is None
        assert obj.getMinimumIntervalLength() is None

    def test_get_set_contextDataSource(self):
        obj = self._obj()
        value = SecurityEventContextDataSourceEnum()
        assert obj.setContextDataSource(value) is obj
        assert obj.getContextDataSource() is value

    def test_get_set_minimumIntervalLength(self):
        obj = self._obj()
        value = TimeValue()
        assert obj.setMinimumIntervalLength(value) is obj
        assert obj.getMinimumIntervalLength() is value
