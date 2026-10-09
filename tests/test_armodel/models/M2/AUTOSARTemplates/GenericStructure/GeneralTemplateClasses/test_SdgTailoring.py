"""
This module contains tests for the SdgTailoring class.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import SdgTailoring


class TestSdgTailoring:

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _obj(self):
        return SdgTailoring(self._parent(), "SdgTailoring")

    def test_instantiation(self):
        obj = self._obj()
        assert isinstance(obj, SdgTailoring)
