"""
This module contains tests for the VariationRestrictionWithSeverity class.
"""

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ModelRestrictionTypes import VariationRestrictionWithSeverity


class TestVariationRestrictionWithSeverity:

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_abstract_instantiation(self):
        with pytest.raises(TypeError):
            VariationRestrictionWithSeverity()

    def test_subclass_instantiability(self):
        class Concrete(VariationRestrictionWithSeverity):
            pass

        obj = Concrete()
        assert isinstance(obj, VariationRestrictionWithSeverity)
