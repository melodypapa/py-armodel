"""
This module contains tests for the PrimitiveAttributeCondition class.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import PrimitiveAttributeCondition
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TestPrimitiveAttributeCondition:

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _obj(self):
        return PrimitiveAttributeCondition()

    def test_instantiation(self):
        obj = self._obj()
        assert isinstance(obj, PrimitiveAttributeCondition)
        assert obj.getAttributeRef() is None

    def test_get_set_attributeRef(self):
        obj = self._obj()
        value = RefType().setValue("/Pkg/X").setDest("X")
        assert obj.setAttributeRef(value) is obj
        assert obj.getAttributeRef() is value

    def test_set_attributeRef_none_noop(self):
        obj = self._obj()
        value = RefType().setValue("/Pkg/X").setDest("X")
        obj.setAttributeRef(value)
        assert obj.setAttributeRef(None) is obj
        assert obj.getAttributeRef() is value
