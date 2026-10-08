"""
This module contains tests for the FMAttributeDef class in the
AUTOSAR GenericStructure.GeneralTemplateClasses module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import FMAttributeDef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Limit, Numerical


class TestFMAttributeDef:
    """
    Test class for FMAttributeDef functionality.
    """

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _obj(self):
        return FMAttributeDef(self._parent(), "AttrDef")

    def test_initialization(self):
        obj = self._obj()
        assert isinstance(obj, FMAttributeDef)
        assert obj.getDefaultValue() is None
        assert obj.getMax() is None
        assert obj.getMin() is None

    def test_get_set_default_value(self):
        obj = self._obj()
        numerical = Numerical()
        numerical.setValue(1.5)
        assert obj.setDefaultValue(numerical) is obj
        assert obj.getDefaultValue() is numerical

    def test_set_default_value_none_noop(self):
        obj = self._obj()
        numerical = Numerical()
        numerical.setValue(1.5)
        obj.setDefaultValue(numerical)
        assert obj.setDefaultValue(None) is obj
        assert obj.getDefaultValue() is numerical

    def test_get_set_max(self):
        obj = self._obj()
        limit = Limit()
        limit.setValue("10")
        assert obj.setMax(limit) is obj
        assert obj.getMax() is limit

    def test_set_max_none_noop(self):
        obj = self._obj()
        limit = Limit()
        limit.setValue("10")
        obj.setMax(limit)
        assert obj.setMax(None) is obj
        assert obj.getMax() is limit

    def test_get_set_min(self):
        obj = self._obj()
        limit = Limit()
        limit.setValue("1")
        assert obj.setMin(limit) is obj
        assert obj.getMin() is limit

    def test_set_min_none_noop(self):
        obj = self._obj()
        limit = Limit()
        limit.setValue("1")
        obj.setMin(limit)
        assert obj.setMin(None) is obj
        assert obj.getMin() is limit
