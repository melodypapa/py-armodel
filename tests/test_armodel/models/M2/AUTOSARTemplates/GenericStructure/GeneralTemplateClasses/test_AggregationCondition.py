"""
This module contains tests for the AggregationCondition class.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import AggregationCondition
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TestAggregationCondition:

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _obj(self):
        return AggregationCondition()

    def test_instantiation(self):
        obj = self._obj()
        assert isinstance(obj, AggregationCondition)
        assert obj.getAggregationRef() is None

    def test_get_set_aggregationRef(self):
        obj = self._obj()
        value = RefType().setValue("/Pkg/X").setDest("X")
        assert obj.setAggregationRef(value) is obj
        assert obj.getAggregationRef() is value

    def test_set_aggregationRef_none_noop(self):
        obj = self._obj()
        value = RefType().setValue("/Pkg/X").setDest("X")
        obj.setAggregationRef(value)
        assert obj.setAggregationRef(None) is obj
        assert obj.getAggregationRef() is value
