"""
This module contains tests for the AbstractClassTailoring class.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import AbstractClassTailoring


class TestAbstractClassTailoring:

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _obj(self):
        return AbstractClassTailoring(self._parent(), "AbstractClassTailoring")

    def test_instantiation(self):
        obj = self._obj()
        assert isinstance(obj, AbstractClassTailoring)
