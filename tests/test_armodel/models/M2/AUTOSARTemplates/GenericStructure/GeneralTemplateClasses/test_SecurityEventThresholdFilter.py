"""
This module contains tests for the SecurityEventThresholdFilter class.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import SecurityEventThresholdFilter
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import AbstractSecurityEventFilter
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, TimeValue


class TestSecurityEventThresholdFilter:
    """
    Test class for SecurityEventThresholdFilter functionality.
    """

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _obj(self):
        return SecurityEventThresholdFilter(self._parent(), "SecurityEventThresho")

    def test_initialization(self):
        obj = self._obj()
        assert isinstance(obj, SecurityEventThresholdFilter)
        assert isinstance(obj, AbstractSecurityEventFilter)
        assert obj.getIntervalLength() is None
        assert obj.getThresholdNumber() is None

    def test_get_set_intervalLength(self):
        obj = self._obj()
        value = TimeValue()
        assert obj.setIntervalLength(value) is obj
        assert obj.getIntervalLength() is value

    def test_get_set_thresholdNumber(self):
        obj = self._obj()
        value = PositiveInteger()
        value.setValue(3)
        assert obj.setThresholdNumber(value) is obj
        assert obj.getThresholdNumber() is value
