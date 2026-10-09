"""
This module contains tests for the DataExchangePoint class.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DataExchangePoint


class TestDataExchangePoint:

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _obj(self):
        return DataExchangePoint(self._parent(), "DataExchangePoint")

    def test_instantiation(self):
        obj = self._obj()
        assert isinstance(obj, DataExchangePoint)
