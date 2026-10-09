"""
This module contains tests for the FMFeatureSelection class in the
AUTOSAR GenericStructure.GeneralTemplateClasses module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import FMAttributeValue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Enumerations import BindingTimeEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import FMFeatureSelection
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import FMFeatureSelectionState, RefType


class TestFMFeatureSelection:
    """
    Test class for FMFeatureSelection functionality.
    """

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _obj(self):
        return FMFeatureSelection(self._parent(), "Selection")

    def test_initialization(self):
        obj = self._obj()
        assert isinstance(obj, FMFeatureSelection)
        assert obj.getAttributeValues() == []
        assert obj.getFeatureRef() is None
        assert obj.getMaximumSelectedBindingTime() is None
        assert obj.getMinimumSelectedBindingTime() is None
        assert obj.getState() is None

    def test_add_get_attribute_values(self):
        obj = self._obj()
        value = FMAttributeValue()
        assert obj.addAttributeValue(value) is obj
        assert obj.getAttributeValues() == [value]

    def test_get_set_feature_ref(self):
        obj = self._obj()
        ref = RefType().setValue("/Pkg/Feature").setDest("FM-FEATURE")
        assert obj.setFeatureRef(ref) is obj
        assert obj.getFeatureRef() is ref

    def test_set_feature_ref_none_noop(self):
        obj = self._obj()
        ref = RefType().setValue("/Pkg/Feature").setDest("FM-FEATURE")
        obj.setFeatureRef(ref)
        assert obj.setFeatureRef(None) is obj
        assert obj.getFeatureRef() is ref

    def test_get_set_maximum_selected_binding_time(self):
        obj = self._obj()
        binding_time = BindingTimeEnum()
        binding_time.setValue("SYSTEM-DESIGN-TIME")
        assert obj.setMaximumSelectedBindingTime(binding_time) is obj
        assert obj.getMaximumSelectedBindingTime() is binding_time

    def test_set_maximum_selected_binding_time_none_noop(self):
        obj = self._obj()
        binding_time = BindingTimeEnum()
        binding_time.setValue("SYSTEM-DESIGN-TIME")
        obj.setMaximumSelectedBindingTime(binding_time)
        assert obj.setMaximumSelectedBindingTime(None) is obj
        assert obj.getMaximumSelectedBindingTime() is binding_time

    def test_get_set_minimum_selected_binding_time(self):
        obj = self._obj()
        binding_time = BindingTimeEnum()
        binding_time.setValue("PRE-COMPILE-TIME")
        assert obj.setMinimumSelectedBindingTime(binding_time) is obj
        assert obj.getMinimumSelectedBindingTime() is binding_time

    def test_set_minimum_selected_binding_time_none_noop(self):
        obj = self._obj()
        binding_time = BindingTimeEnum()
        binding_time.setValue("PRE-COMPILE-TIME")
        obj.setMinimumSelectedBindingTime(binding_time)
        assert obj.setMinimumSelectedBindingTime(None) is obj
        assert obj.getMinimumSelectedBindingTime() is binding_time

    def test_get_set_state(self):
        obj = self._obj()
        state = FMFeatureSelectionState()
        state.setValue(FMFeatureSelectionState.SELECTED)
        assert obj.setState(state) is obj
        assert obj.getState() is state

    def test_set_state_none_noop(self):
        obj = self._obj()
        state = FMFeatureSelectionState()
        state.setValue(FMFeatureSelectionState.SELECTED)
        obj.setState(state)
        assert obj.setState(None) is obj
        assert obj.getState() is state
