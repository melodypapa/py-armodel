"""
This module contains tests for the ConstraintTailoring class.
"""

import pytest
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ConstraintTailoring
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import DataFormatElementScope


class TestConstraintTailoring:

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _obj(self):
        return ConstraintTailoring(self._parent(), "ConstraintTailoring")

    def test_instantiation(self):
        obj = self._obj()
        assert isinstance(obj, ConstraintTailoring)
