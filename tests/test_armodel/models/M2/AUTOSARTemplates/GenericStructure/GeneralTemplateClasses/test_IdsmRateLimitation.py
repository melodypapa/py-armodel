"""
This module contains tests for the IdsmRateLimitation class in the
AUTOSAR GenericStructure.GeneralTemplateClasses module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import IdsmRateLimitation
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Float, PositiveInteger


class TestIdsmRateLimitation:
    """
    Test class for IdsmRateLimitation functionality.
    """

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _obj(self):
        return IdsmRateLimitation(self._parent(), "Limitation")

    def test_initialization(self):
        obj = self._obj()
        assert isinstance(obj, IdsmRateLimitation)
        assert obj.getMaxEventsInInterval() is None
        assert obj.getTimeInterval() is None

    def test_get_set_maxEventsInInterval(self):
        obj = self._obj()
        value = PositiveInteger()
        value.setValue(5)
        assert obj.setMaxEventsInInterval(value) is obj
        assert obj.getMaxEventsInInterval() is value

    def test_set_maxEventsInInterval_none_noop(self):
        obj = self._obj()
        value = PositiveInteger()
        value.setValue(5)
        obj.setMaxEventsInInterval(value)
        assert obj.setMaxEventsInInterval(None) is obj
        assert obj.getMaxEventsInInterval() is value

    def test_get_set_timeInterval(self):
        obj = self._obj()
        value = Float()
        value.setValue(1.5)
        assert obj.setTimeInterval(value) is obj
        assert obj.getTimeInterval() is value

    def test_set_timeInterval_none_noop(self):
        obj = self._obj()
        value = Float()
        value.setValue(1.5)
        obj.setTimeInterval(value)
        assert obj.setTimeInterval(None) is obj
        assert obj.getTimeInterval() is value
