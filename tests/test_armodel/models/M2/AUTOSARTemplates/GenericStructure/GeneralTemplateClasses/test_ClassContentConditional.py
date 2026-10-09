"""
This module contains tests for the ClassContentConditional class.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ClassContentConditional


class TestClassContentConditional:

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _obj(self):
        return ClassContentConditional(self._parent(), "ClassContentConditional")

    def test_instantiation(self):
        obj = self._obj()
        assert isinstance(obj, ClassContentConditional)
        assert obj.getAttributeTailorings() in (None, [])
        assert obj.getConstraintTailorings() in (None, [])
        assert obj.getSdgTailorings() in (None, [])
