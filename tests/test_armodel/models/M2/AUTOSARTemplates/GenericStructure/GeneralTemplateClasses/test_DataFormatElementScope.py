"""
This module contains tests for the DataFormatElementScope class.
"""

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import DataFormatElementScope


class TestDataFormatElementScope:

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_abstract_instantiation(self):
        with pytest.raises(TypeError):
            DataFormatElementScope(self._parent(), "DataFormatElementScope")

    def test_subclass_instantiability(self):
        class Concrete(DataFormatElementScope):
            pass

        obj = Concrete(self._parent(), "DataFormatElementScope")
        assert isinstance(obj, DataFormatElementScope)
