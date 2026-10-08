"""
This module contains tests for the SecurityEventContextMappingCommConnector class.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import SecurityEventContextMappingCommConnector
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import SecurityEventContextMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TestSecurityEventContextMappingCommConnector:
    """
    Test class for SecurityEventContextMappingCommConnector functionality.
    """

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _obj(self):
        return SecurityEventContextMappingCommConnector(self._parent(), "SecurityEventContext")

    def test_initialization(self):
        obj = self._obj()
        assert isinstance(obj, SecurityEventContextMappingCommConnector)
        assert isinstance(obj, SecurityEventContextMapping)
        assert obj.getCommunicationConnectorRef() is None

    def test_get_set_communicationConnectorRef(self):
        obj = self._obj()
        value = RefType().setValue("/Pkg/X").setDest("X")
        assert obj.setCommunicationConnectorRef(value) is obj
        assert obj.getCommunicationConnectorRef() is value
