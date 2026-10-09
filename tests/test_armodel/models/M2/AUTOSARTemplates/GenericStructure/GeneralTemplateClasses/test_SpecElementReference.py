"""
This module contains tests for the SpecElementReference class.
"""

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import SpecElementReference


class TestSpecElementReference:

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_abstract_instantiation(self):
        with pytest.raises(TypeError):
            SpecElementReference(self._parent(), "SpecElementReference")

    def test_subclass_instantiability(self):
        class Concrete(SpecElementReference):
            pass

        obj = Concrete(self._parent(), "SpecElementReference")
        assert isinstance(obj, SpecElementReference)
