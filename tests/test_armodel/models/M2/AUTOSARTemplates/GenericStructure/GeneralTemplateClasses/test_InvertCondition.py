"""
This module contains tests for the InvertCondition class.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import InvertCondition


class TestInvertCondition:

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _obj(self):
        return InvertCondition()

    def test_instantiation(self):
        obj = self._obj()
        assert isinstance(obj, InvertCondition)
        assert obj.getCondition() in (None, [])
