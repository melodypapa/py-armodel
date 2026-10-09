"""
This module contains tests for the DocumentElementScope class.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import DocumentElementScope
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TestDocumentElementScope:

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _obj(self):
        return DocumentElementScope(self._parent(), "DocumentElementScope")

    def test_instantiation(self):
        obj = self._obj()
        assert isinstance(obj, DocumentElementScope)
        assert obj.getCustomDocumentElementRef() is None
        assert obj.getTailoringRefs() in (None, [])

    def test_get_set_customDocumentElementRef(self):
        obj = self._obj()
        value = RefType().setValue("/Pkg/X").setDest("X")
        assert obj.setCustomDocumentElementRef(value) is obj
        assert obj.getCustomDocumentElementRef() is value

    def test_set_customDocumentElementRef_none_noop(self):
        obj = self._obj()
        value = RefType().setValue("/Pkg/X").setDest("X")
        obj.setCustomDocumentElementRef(value)
        assert obj.setCustomDocumentElementRef(None) is obj
        assert obj.getCustomDocumentElementRef() is value
