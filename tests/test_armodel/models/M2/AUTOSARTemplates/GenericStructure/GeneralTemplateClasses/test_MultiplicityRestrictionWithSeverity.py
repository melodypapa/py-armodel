"""
This module contains tests for the MultiplicityRestrictionWithSeverity class.
"""

import pytest
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import MultiplicityRestrictionWithSeverity
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import AbstractMultiplicityRestriction


class TestMultiplicityRestrictionWithSeverity:

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _obj(self):
        return MultiplicityRestrictionWithSeverity()

    def test_instantiation(self):
        obj = self._obj()
        assert isinstance(obj, MultiplicityRestrictionWithSeverity)
