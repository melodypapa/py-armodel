"""
This module contains tests for the SecurityEventOneEveryNFilter class.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import AbstractSecurityEventFilter, SecurityEventOneEveryNFilter
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger


class TestSecurityEventOneEveryNFilter:
    """
    Test class for SecurityEventOneEveryNFilter functionality.
    """

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _obj(self):
        return SecurityEventOneEveryNFilter(self._parent(), "SecurityEventOneEver")

    def test_initialization(self):
        obj = self._obj()
        assert isinstance(obj, SecurityEventOneEveryNFilter)
        assert isinstance(obj, AbstractSecurityEventFilter)
        assert obj.getN() is None

    def test_get_set_n(self):
        obj = self._obj()
        value = PositiveInteger()
        value.setValue(5)
        assert obj.setN(value) is obj
        assert obj.getN() is value
