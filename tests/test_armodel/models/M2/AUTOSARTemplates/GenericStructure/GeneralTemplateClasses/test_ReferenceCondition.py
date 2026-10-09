"""
This module contains tests for the ReferenceCondition class.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ReferenceCondition
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TestReferenceCondition:

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _obj(self):
        return ReferenceCondition()

    def test_instantiation(self):
        obj = self._obj()
        assert isinstance(obj, ReferenceCondition)
        assert obj.getReferenceRef() is None

    def test_get_set_referenceRef(self):
        obj = self._obj()
        value = RefType().setValue("/Pkg/X").setDest("X")
        assert obj.setReferenceRef(value) is obj
        assert obj.getReferenceRef() is value

    def test_set_referenceRef_none_noop(self):
        obj = self._obj()
        value = RefType().setValue("/Pkg/X").setDest("X")
        obj.setReferenceRef(value)
        assert obj.setReferenceRef(None) is obj
        assert obj.getReferenceRef() is value
