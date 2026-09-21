"""Model unit tests for AbstractEthernetFrame (Table 6.229, p.578)."""

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetFrame import AbstractEthernetFrame, GenericEthernetFrame
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import Frame

SPEC_NOTE = "Ethernet specific attributes to the Frame."


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class TestAbstractEthernetFrame:
    def test_abstract_instantiation_raises(self):
        parent = MockParent()
        with pytest.raises(TypeError):
            AbstractEthernetFrame(parent, "abstract_frame")

    def test_class_docstring_is_spec_note(self):
        assert AbstractEthernetFrame.__doc__.strip() == SPEC_NOTE

    def test_init_has_no_docstring(self):
        assert AbstractEthernetFrame.__init__.__doc__ is None

    def test_inherits_frame(self):
        assert issubclass(AbstractEthernetFrame, Frame)


class TestGenericEthernetFrame:
    def test_initialization_defaults(self):
        parent = MockParent()
        frame = GenericEthernetFrame(parent, "generic_frame")
        assert frame.getShortName() == "generic_frame"
        assert isinstance(frame, Frame)
        assert isinstance(frame, AbstractEthernetFrame)
        assert frame.getFrameLength() is None
        assert frame.getPduToFrameMappings() == []
