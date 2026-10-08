"""
This module contains tests for the FMFeatureMap class in the
AUTOSAR GenericStructure.GeneralTemplateClasses module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import FMFeatureMap
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import FMFeatureMapElement


class TestFMFeatureMap:
    """
    Test class for FMFeatureMap functionality.
    """

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _obj(self):
        return FMFeatureMap(self._parent(), "FeatureMap")

    def test_initialization(self):
        obj = self._obj()
        assert isinstance(obj, FMFeatureMap)
        assert obj.getMappings() == []

    def test_add_get_mappings(self):
        obj = self._obj()
        mapping = FMFeatureMapElement(obj, "Mapping")
        assert obj.addMapping(mapping) is obj
        assert obj.getMappings() == [mapping]
