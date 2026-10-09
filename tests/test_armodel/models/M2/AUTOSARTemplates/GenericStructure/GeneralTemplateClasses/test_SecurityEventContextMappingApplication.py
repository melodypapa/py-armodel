"""
This module contains tests for the SecurityEventContextMappingApplication class.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import SecurityEventContextMapping, SecurityEventContextMappingApplication
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String


class TestSecurityEventContextMappingApplication:
    """
    Test class for SecurityEventContextMappingApplication functionality.
    """

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _obj(self):
        return SecurityEventContextMappingApplication(self._parent(), "SecurityEventContext")

    def test_initialization(self):
        obj = self._obj()
        assert isinstance(obj, SecurityEventContextMappingApplication)
        assert isinstance(obj, SecurityEventContextMapping)
        assert obj.getAffectedApplication() is None

    def test_get_set_affectedApplication(self):
        obj = self._obj()
        value = String()
        assert obj.setAffectedApplication(value) is obj
        assert obj.getAffectedApplication() is value
