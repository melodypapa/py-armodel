"""
This module contains tests for the AttributeTailoring class.
"""

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import AttributeTailoring


class TestAttributeTailoring:

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_abstract_instantiation(self):
        with pytest.raises(TypeError):
            AttributeTailoring(self._parent(), "AttributeTailoring")

    def test_subclass_instantiability(self):
        class Concrete(AttributeTailoring):
            pass

        obj = Concrete(self._parent(), "AttributeTailoring")
        assert isinstance(obj, AttributeTailoring)
