"""Model unit tests for CouplingPortAbstractShaper (XSD-only abstract class, no PDF/markdown table)."""

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    CouplingPortAbstractShaper,
    CouplingPortAsynchronousTrafficShaper,
    CouplingPortCreditBasedShaper,
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

    def test_builtin_concrete_shapers_derive_from_abstract_base(self):
        assert issubclass(CouplingPortAsynchronousTrafficShaper, CouplingPortAbstractShaper)
        assert issubclass(CouplingPortCreditBasedShaper, CouplingPortAbstractShaper)

    def test_builtin_concrete_shapers_instantiable(self):
        for cls in (CouplingPortAsynchronousTrafficShaper, CouplingPortCreditBasedShaper):
            shaper = cls(MockParent(), "Shaper1")
            assert shaper.getShortName() == "Shaper1"
            assert isinstance(shaper, CouplingPortAbstractShaper)
