"""Model unit tests for CouplingPortCreditBasedShaper (XSD-derived, atp.Status=candidate, no PDF table)."""

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    CouplingPortAbstractShaper,
    CouplingPortCreditBasedShaper,
)


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


@pytest.fixture
def shaper():
    return CouplingPortCreditBasedShaper(MockParent(), "CbsShaper")


class TestCouplingPortCreditBasedShaper:
    def test_registered_in_shaper_registry(self):
        assert CouplingPortAbstractShaper.getShaperClass("COUPLING-PORT-CREDIT-BASED-SHAPER") is CouplingPortCreditBasedShaper
        assert CouplingPortAbstractShaper.getShaperTag(CouplingPortCreditBasedShaper) == "COUPLING-PORT-CREDIT-BASED-SHAPER"

    def test_initialization_defaults(self, shaper):
        assert shaper.getShortName() == "CbsShaper"
        assert shaper.getIdleSlope() is None
        assert shaper.getLowerBoundary() is None
        assert shaper.getUpperBoundary() is None

    def test_get_set_idle_slope(self, shaper):
        value = PositiveInteger().setValue("1000000")
        assert shaper.setIdleSlope(value) is shaper
        assert shaper.getIdleSlope() is value

    def test_set_idle_slope_none_no_op(self, shaper):
        shaper.setIdleSlope(PositiveInteger().setValue("1000000"))
        shaper.setIdleSlope(None)
        assert shaper.getIdleSlope().getValue() == 1000000

    def test_get_set_lower_boundary(self, shaper):
        value = PositiveInteger().setValue("2000")
        assert shaper.setLowerBoundary(value) is shaper
        assert shaper.getLowerBoundary() is value

    def test_set_lower_boundary_none_no_op(self, shaper):
        shaper.setLowerBoundary(PositiveInteger().setValue("2000"))
        shaper.setLowerBoundary(None)
        assert shaper.getLowerBoundary().getValue() == 2000

    def test_get_set_upper_boundary(self, shaper):
        value = PositiveInteger().setValue("8000")
        assert shaper.setUpperBoundary(value) is shaper
        assert shaper.getUpperBoundary() is value

    def test_set_upper_boundary_none_no_op(self, shaper):
        shaper.setUpperBoundary(PositiveInteger().setValue("8000"))
        shaper.setUpperBoundary(None)
        assert shaper.getUpperBoundary().getValue() == 8000
