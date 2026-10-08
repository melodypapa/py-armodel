"""
This module contains tests for the SecurityEventDefinition class.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import SecurityEventDefinition
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import IdsCommonElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger


class TestSecurityEventDefinition:
    """
    Test class for SecurityEventDefinition functionality.
    """

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _obj(self):
        return SecurityEventDefinition(self._parent(), "SecurityEventDefinit")

    def test_initialization(self):
        obj = self._obj()
        assert isinstance(obj, SecurityEventDefinition)
        assert isinstance(obj, IdsCommonElement)
        assert obj.getId() is None

    def test_get_set_id(self):
        obj = self._obj()
        value = PositiveInteger()
        value.setValue(42)
        assert obj.setId(value) is obj
        assert obj.getId() is value
