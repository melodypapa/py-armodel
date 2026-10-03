"""Model unit tests for CouplingPortAbstractShaper (XSD-only abstract class, no PDF/markdown table)."""

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    CouplingPortAbstractShaper,
)


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class ConcreteShaper(CouplingPortAbstractShaper):
    pass


@pytest.fixture(autouse=True)
def isolated_registry():
    saved = dict(CouplingPortAbstractShaper._shaper_registry)
    yield
    CouplingPortAbstractShaper._shaper_registry.clear()
    CouplingPortAbstractShaper._shaper_registry.update(saved)


class TestCouplingPortAbstractShaper:
    def test_cannot_instantiate_abstract(self):
        with pytest.raises(TypeError):
            CouplingPortAbstractShaper(MockParent(), "Shaper")

    def test_abstract_guard_message(self):
        with pytest.raises(TypeError, match="CouplingPortAbstractShaper is an abstract class."):
            CouplingPortAbstractShaper(MockParent(), "Shaper")

    def test_concrete_subclass_instantiable(self):
        shaper = ConcreteShaper(MockParent(), "Shaper1")
        assert shaper.getShortName() == "Shaper1"

    def test_concrete_subclass_is_identifiable(self):
        shaper = ConcreteShaper(MockParent(), "Shaper1")
        assert isinstance(shaper, CouplingPortAbstractShaper)
        assert isinstance(shaper, Identifiable)

    def test_registry_round_trips_tag_to_class(self):
        CouplingPortAbstractShaper.registerShaper("CONCRETE-COUPLING-PORT-SHAPER", ConcreteShaper)
        assert CouplingPortAbstractShaper.getShaperClass("CONCRETE-COUPLING-PORT-SHAPER") is ConcreteShaper
        assert CouplingPortAbstractShaper.getShaperTag(ConcreteShaper) == "CONCRETE-COUPLING-PORT-SHAPER"

    def test_registry_unknown_tag_returns_none(self):
        assert CouplingPortAbstractShaper.getShaperClass("NO-SUCH-SHAPER") is None

    def test_registry_unregistered_class_returns_none(self):
        class OtherShaper(CouplingPortAbstractShaper):
            pass

        assert CouplingPortAbstractShaper.getShaperTag(OtherShaper) is None

    def test_builtin_shapers_registered_at_import(self):
        assert CouplingPortAbstractShaper.getShaperClass("COUPLING-PORT-ASYNCHRONOUS-TRAFFIC-SHAPER") is not None
        assert CouplingPortAbstractShaper.getShaperClass("COUPLING-PORT-CREDIT-BASED-SHAPER") is not None

    def test_registry_helpers_have_docstrings(self):
        assert CouplingPortAbstractShaper.registerShaper.__doc__
        assert CouplingPortAbstractShaper.getShaperClass.__doc__
        assert CouplingPortAbstractShaper.getShaperTag.__doc__
