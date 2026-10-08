"""
This module contains tests for the PrimitiveAttributeTailoring class.
"""

import pytest
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import PrimitiveAttributeTailoring
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import AttributeTailoring


class TestPrimitiveAttributeTailoring:

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _obj(self):
        return PrimitiveAttributeTailoring(self._parent(), "PrimitiveAttributeTailoring")

    def test_instantiation(self):
        obj = self._obj()
        assert isinstance(obj, PrimitiveAttributeTailoring)
        assert obj.getDefaultValueHandling() in (None, [])
        assert obj.getSubAttributeTailorings() in (None, [])
        assert obj.getValueRestriction() in (None, [])
