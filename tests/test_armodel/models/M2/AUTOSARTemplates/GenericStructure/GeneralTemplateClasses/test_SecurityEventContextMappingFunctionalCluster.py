"""
This module contains tests for the SecurityEventContextMappingFunctionalCluster class.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import SecurityEventContextMappingFunctionalCluster
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import SecurityEventContextMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String


class TestSecurityEventContextMappingFunctionalCluster:
    """
    Test class for SecurityEventContextMappingFunctionalCluster functionality.
    """

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _obj(self):
        return SecurityEventContextMappingFunctionalCluster(self._parent(), "SecurityEventContext")

    def test_initialization(self):
        obj = self._obj()
        assert isinstance(obj, SecurityEventContextMappingFunctionalCluster)
        assert isinstance(obj, SecurityEventContextMapping)
        assert obj.getAffectedFunctionalCluster() is None

    def test_get_set_affectedFunctionalCluster(self):
        obj = self._obj()
        value = String()
        assert obj.setAffectedFunctionalCluster(value) is obj
        assert obj.getAffectedFunctionalCluster() is value
