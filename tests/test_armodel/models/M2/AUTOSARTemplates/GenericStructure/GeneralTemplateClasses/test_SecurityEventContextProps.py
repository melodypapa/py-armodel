"""
This module contains tests for the SecurityEventContextProps class.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import SecurityEventContextProps
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger


class TestSecurityEventContextProps:
    """
    Test class for SecurityEventContextProps functionality.
    """

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _obj(self):
        return SecurityEventContextProps(self._parent(), "SecurityEventContext")

    def test_initialization(self):
        obj = self._obj()
        assert isinstance(obj, SecurityEventContextProps)
        assert isinstance(obj, Identifiable)
        assert obj.getPersistentStorage() is None
        assert obj.getSensorInstanceId() is None
        assert obj.getSeverity() is None

    def test_get_set_persistentStorage(self):
        obj = self._obj()
        value = Boolean()
        assert obj.setPersistentStorage(value) is obj
        assert obj.getPersistentStorage() is value

    def test_get_set_sensorInstanceId(self):
        obj = self._obj()
        value = PositiveInteger()
        value.setValue(7)
        assert obj.setSensorInstanceId(value) is obj
        assert obj.getSensorInstanceId() is value

    def test_get_set_severity(self):
        obj = self._obj()
        value = PositiveInteger()
        value.setValue(2)
        assert obj.setSeverity(value) is obj
        assert obj.getSeverity() is value
