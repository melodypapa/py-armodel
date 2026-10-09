"""
This module contains tests for the FMFeature class in the
AUTOSAR GenericStructure.GeneralTemplateClasses module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import FMFeatureDecomposition
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import FMFeature
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Enumerations import BindingTimeEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import FMAttributeDef, FMFeatureRelation, FMFeatureRestriction


class TestFMFeature:
    """
    Test class for FMFeature functionality.
    """

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _obj(self):
        return FMFeature(self._parent(), "Feature")

    def test_initialization(self):
        obj = self._obj()
        assert isinstance(obj, FMFeature)
        assert obj.getAttributeDefs() == []
        assert obj.getDecompositions() == []
        assert obj.getMaximumIntendedBindingTime() is None
        assert obj.getMinimumIntendedBindingTime() is None
        assert obj.getRelations() == []
        assert obj.getRestrictions() == []

    def test_add_get_attribute_defs(self):
        obj = self._obj()
        attribute_def = FMAttributeDef(obj, "AttrDef")
        assert obj.addAttributeDef(attribute_def) is obj
        assert obj.getAttributeDefs() == [attribute_def]

    def test_add_get_decompositions(self):
        obj = self._obj()
        decomposition = FMFeatureDecomposition()
        assert obj.addDecomposition(decomposition) is obj
        assert obj.getDecompositions() == [decomposition]

    def test_get_set_maximum_intended_binding_time(self):
        obj = self._obj()
        binding_time = BindingTimeEnum()
        binding_time.setValue("SYSTEM-DESIGN-TIME")
        assert obj.setMaximumIntendedBindingTime(binding_time) is obj
        assert obj.getMaximumIntendedBindingTime() is binding_time

    def test_set_maximum_intended_binding_time_none_noop(self):
        obj = self._obj()
        binding_time = BindingTimeEnum()
        binding_time.setValue("SYSTEM-DESIGN-TIME")
        obj.setMaximumIntendedBindingTime(binding_time)
        assert obj.setMaximumIntendedBindingTime(None) is obj
        assert obj.getMaximumIntendedBindingTime() is binding_time

    def test_get_set_minimum_intended_binding_time(self):
        obj = self._obj()
        binding_time = BindingTimeEnum()
        binding_time.setValue("PRE-COMPILE-TIME")
        assert obj.setMinimumIntendedBindingTime(binding_time) is obj
        assert obj.getMinimumIntendedBindingTime() is binding_time

    def test_set_minimum_intended_binding_time_none_noop(self):
        obj = self._obj()
        binding_time = BindingTimeEnum()
        binding_time.setValue("PRE-COMPILE-TIME")
        obj.setMinimumIntendedBindingTime(binding_time)
        assert obj.setMinimumIntendedBindingTime(None) is obj
        assert obj.getMinimumIntendedBindingTime() is binding_time

    def test_add_get_relations(self):
        obj = self._obj()
        relation = FMFeatureRelation(obj, "Relation")
        assert obj.addRelation(relation) is obj
        assert obj.getRelations() == [relation]

    def test_add_get_restrictions(self):
        obj = self._obj()
        restriction = FMFeatureRestriction(obj, "Restriction")
        assert obj.addRestriction(restriction) is obj
        assert obj.getRestrictions() == [restriction]
