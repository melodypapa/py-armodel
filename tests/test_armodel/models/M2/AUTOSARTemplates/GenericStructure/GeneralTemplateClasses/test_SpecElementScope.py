"""
This module contains tests for the SpecElementScope class.
"""

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import SpecElementScope


class TestSpecElementScope:

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_abstract_instantiation(self):
        with pytest.raises(TypeError):
            SpecElementScope(self._parent(), "SpecElementScope")

    def test_subclass_instantiability(self):
        class Concrete(SpecElementScope):
            pass

        obj = Concrete(self._parent(), "SpecElementScope")
        assert isinstance(obj, SpecElementScope)
