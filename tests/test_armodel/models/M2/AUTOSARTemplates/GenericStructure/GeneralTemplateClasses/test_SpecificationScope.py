"""
This module contains tests for the SpecificationScope class.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import SpecificationScope


class TestSpecificationScope:

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _obj(self):
        return SpecificationScope()

    def test_instantiation(self):
        obj = self._obj()
        assert isinstance(obj, SpecificationScope)
        assert obj.getSpecificationDocumentScopes() in (None, [])
