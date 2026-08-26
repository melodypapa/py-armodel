import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription import (
    TimingDescription,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class ConcreteTimingDescription(TimingDescription):
    pass


class TestTimingDescription:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_abstract_class_cannot_be_instantiated(self):
        parent = self._parent()
        with pytest.raises(TypeError, match="TimingDescription is an abstract class"):
            TimingDescription(parent, "Desc1")

    def test_base_is_identifiable(self):
        assert issubclass(TimingDescription, Identifiable)

    def test_initialization_defaults(self):
        desc = ConcreteTimingDescription(self._parent(), "Desc1")
        assert desc.getShortName() == "Desc1"
        assert desc.getVariationPoint() is None

    def test_inherits_identifiable_accessors(self):
        desc = ConcreteTimingDescription(self._parent(), "Desc1")
        assert desc.getCategory() is None
        assert desc.getAdminData() is None
