"""
This module contains tests for the AggregationTailoring class.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import AggregationTailoring


class TestAggregationTailoring:

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _obj(self):
        return AggregationTailoring(self._parent(), "AggregationTailoring")

    def test_instantiation(self):
        obj = self._obj()
        assert isinstance(obj, AggregationTailoring)
        assert obj.getTypeTailorings() in (None, [])
