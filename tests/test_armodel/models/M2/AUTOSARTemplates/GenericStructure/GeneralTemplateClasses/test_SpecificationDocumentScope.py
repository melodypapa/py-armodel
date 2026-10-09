"""
This module contains tests for the SpecificationDocumentScope class.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import SpecificationDocumentScope
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TestSpecificationDocumentScope:

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _obj(self):
        return SpecificationDocumentScope(self._parent(), "SpecificationDocumentScope")

    def test_instantiation(self):
        obj = self._obj()
        assert isinstance(obj, SpecificationDocumentScope)
        assert obj.getCustomDocumentationRef() is None
        assert obj.getDocumentElementScopes() in (None, [])

    def test_get_set_customDocumentationRef(self):
        obj = self._obj()
        value = RefType().setValue("/Pkg/X").setDest("X")
        assert obj.setCustomDocumentationRef(value) is obj
        assert obj.getCustomDocumentationRef() is value

    def test_set_customDocumentationRef_none_noop(self):
        obj = self._obj()
        value = RefType().setValue("/Pkg/X").setDest("X")
        obj.setCustomDocumentationRef(value)
        assert obj.setCustomDocumentationRef(None) is obj
        assert obj.getCustomDocumentationRef() is value
