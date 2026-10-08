"""
This module contains tests for the Baseline class.
"""

import pytest
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import Baseline


class TestBaseline:

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _obj(self):
        return Baseline()

    def test_instantiation(self):
        obj = self._obj()
        assert isinstance(obj, Baseline)
        assert obj.getCustomSdgDefRefs() in (None, [])
        assert obj.getCustomSpecificationRefs() in (None, [])
        assert obj.getStandardRevisions() in (None, [])
