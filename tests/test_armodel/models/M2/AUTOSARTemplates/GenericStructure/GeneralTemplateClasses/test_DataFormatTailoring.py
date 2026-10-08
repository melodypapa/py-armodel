"""
This module contains tests for the DataFormatTailoring class.
"""

import pytest
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DataFormatTailoring


class TestDataFormatTailoring:

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _obj(self):
        return DataFormatTailoring()

    def test_instantiation(self):
        obj = self._obj()
        assert isinstance(obj, DataFormatTailoring)
        assert obj.getClassTailorings() in (None, [])
        assert obj.getConstraintTailorings() in (None, [])
