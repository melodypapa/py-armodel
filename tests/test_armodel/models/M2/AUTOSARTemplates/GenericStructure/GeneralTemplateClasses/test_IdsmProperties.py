"""
This module contains tests for the IdsmProperties class in the
AUTOSAR GenericStructure.GeneralTemplateClasses module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import IdsmProperties
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import IdsmRateLimitation, IdsmTrafficLimitation


class TestIdsmProperties:
    """
    Test class for IdsmProperties functionality.
    """

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _obj(self):
        return IdsmProperties(self._parent(), "IdsmProperties")

    def test_initialization(self):
        obj = self._obj()
        assert isinstance(obj, IdsmProperties)
        assert obj.getRateLimitationFilters() == []
        assert obj.getTrafficLimitationFilters() == []

    def test_add_get_rate_limitation_filters(self):
        obj = self._obj()
        limitation = IdsmRateLimitation(obj, "Rate")
        assert obj.addRateLimitationFilter(limitation) is obj
        assert obj.getRateLimitationFilters() == [limitation]

    def test_add_get_traffic_limitation_filters(self):
        obj = self._obj()
        limitation = IdsmTrafficLimitation(obj, "Traffic")
        assert obj.addTrafficLimitationFilter(limitation) is obj
        assert obj.getTrafficLimitationFilters() == [limitation]
