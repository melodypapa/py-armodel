"""
This module contains tests for the SecurityEventContextMappingBswModule class.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import SecurityEventContextMapping, SecurityEventContextMappingBswModule
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String


class TestSecurityEventContextMappingBswModule:
    """
    Test class for SecurityEventContextMappingBswModule functionality.
    """

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _obj(self):
        return SecurityEventContextMappingBswModule(self._parent(), "SecurityEventContext")

    def test_initialization(self):
        obj = self._obj()
        assert isinstance(obj, SecurityEventContextMappingBswModule)
        assert isinstance(obj, SecurityEventContextMapping)
        assert obj.getAffectedBswModule() is None

    def test_get_set_affectedBswModule(self):
        obj = self._obj()
        value = String()
        assert obj.setAffectedBswModule(value) is obj
        assert obj.getAffectedBswModule() is value
