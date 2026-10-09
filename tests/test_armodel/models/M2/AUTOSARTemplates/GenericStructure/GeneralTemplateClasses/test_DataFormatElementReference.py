"""
This module contains tests for the DataFormatElementReference class.
"""

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import DataFormatElementReference


class TestDataFormatElementReference:

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_abstract_instantiation(self):
        with pytest.raises(TypeError):
            DataFormatElementReference(self._parent(), "DataFormatElementReference")

    def test_subclass_instantiability(self):
        class Concrete(DataFormatElementReference):
            pass

        obj = Concrete(self._parent(), "DataFormatElementReference")
        assert isinstance(obj, DataFormatElementReference)
