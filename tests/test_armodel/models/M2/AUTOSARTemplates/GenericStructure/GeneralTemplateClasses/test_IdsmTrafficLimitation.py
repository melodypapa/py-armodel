"""
This module contains tests for the IdsmTrafficLimitation class in the
AUTOSAR GenericStructure.GeneralTemplateClasses module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import IdsmTrafficLimitation
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Float, PositiveInteger


class TestIdsmTrafficLimitation:
    """
    Test class for IdsmTrafficLimitation functionality.
    """

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _obj(self):
        return IdsmTrafficLimitation(self._parent(), "Limitation")

    def test_initialization(self):
        obj = self._obj()
        assert isinstance(obj, IdsmTrafficLimitation)
        assert obj.getMaxBytesInInterval() is None
        assert obj.getTimeInterval() is None

    def test_get_set_maxBytesInInterval(self):
        obj = self._obj()
        value = PositiveInteger()
        value.setValue(1024)
        assert obj.setMaxBytesInInterval(value) is obj
        assert obj.getMaxBytesInInterval() is value

    def test_set_maxBytesInInterval_none_noop(self):
        obj = self._obj()
        value = PositiveInteger()
        value.setValue(1024)
        obj.setMaxBytesInInterval(value)
        assert obj.setMaxBytesInInterval(None) is obj
        assert obj.getMaxBytesInInterval() is value

    def test_get_set_timeInterval(self):
        obj = self._obj()
        value = Float()
        value.setValue(2.5)
        assert obj.setTimeInterval(value) is obj
        assert obj.getTimeInterval() is value

    def test_set_timeInterval_none_noop(self):
        obj = self._obj()
        value = Float()
        value.setValue(2.5)
        obj.setTimeInterval(value)
        assert obj.setTimeInterval(None) is obj
        assert obj.getTimeInterval() is value
