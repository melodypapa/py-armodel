"""Model unit tests for CouplingPortAbstractShaper (XSD-derived, abstract, no PDF table)."""

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    CouplingPortAbstractShaper,
)


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class ConcreteShaper(CouplingPortAbstractShaper):
    pass


class TestCouplingPortAbstractShaper:
    def test_cannot_instantiate_abstract(self):
        with pytest.raises(TypeError):
            CouplingPortAbstractShaper(MockParent(), "Shaper")

    def test_concrete_subclass_instantiable(self):
        shaper = ConcreteShaper(MockParent(), "Shaper1")
        assert shaper.getShortName() == "Shaper1"

    def test_registry_round_trips_tag_to_class(self):
        CouplingPortAbstractShaper.registerShaper("CONCRETE-COUPLING-PORT-SHAPER", ConcreteShaper)
        assert CouplingPortAbstractShaper.getShaperClass("CONCRETE-COUPLING-PORT-SHAPER") is ConcreteShaper
        assert CouplingPortAbstractShaper.getShaperTag(ConcreteShaper) == "CONCRETE-COUPLING-PORT-SHAPER"
