"""
This module contains tests for the ReferenceTailoring class.
"""

import pytest
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ReferenceTailoring
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import AttributeTailoring


class TestReferenceTailoring:

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _obj(self):
        return ReferenceTailoring(self._parent(), "ReferenceTailoring")

    def test_instantiation(self):
        obj = self._obj()
        assert isinstance(obj, ReferenceTailoring)
        assert obj.getTypeTailorings() in (None, [])
