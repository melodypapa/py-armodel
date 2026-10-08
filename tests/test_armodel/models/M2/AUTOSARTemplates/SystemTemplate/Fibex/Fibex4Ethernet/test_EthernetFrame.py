"""Model unit tests for AbstractEthernetFrame (Table 6.229, p.578)."""

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetFrame import AbstractEthernetFrame, GenericEthernetFrame, UserDefinedEthernetFrame
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import Frame

SPEC_NOTE = "Ethernet specific attributes to the Frame."
GENERIC_SPEC_NOTE = "This element is used for EthernetFrames without additional attributes that are routed by the EthIf. Tags: atp.recommendedPackage=Frames"
USER_DEFINED_SPEC_NOTE = "UserDefinedEthernetFrame allows the description of a frame-based communication to Complex Drivers that are located above the EthDrv. Tags: atp.recommendedPackage=Frames"


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

    def test_class_docstring_is_spec_note(self):
        assert GenericEthernetFrame.__doc__.strip() == GENERIC_SPEC_NOTE

    def test_init_has_no_docstring(self):
        assert GenericEthernetFrame.__init__.__doc__ is None

    def test_inherits_abstract_ethernet_frame(self):
        assert issubclass(GenericEthernetFrame, AbstractEthernetFrame)


class TestUserDefinedEthernetFrame:
    def test_initialization_defaults(self):
        parent = MockParent()
        frame = UserDefinedEthernetFrame(parent, "user_frame")
        assert frame.getShortName() == "user_frame"
        assert isinstance(frame, Frame)
        assert isinstance(frame, AbstractEthernetFrame)
        assert frame.getFrameLength() is None
        assert frame.getPduToFrameMappings() == []

    def test_class_docstring_is_spec_note(self):
        assert UserDefinedEthernetFrame.__doc__.strip() == USER_DEFINED_SPEC_NOTE

    def test_init_has_no_docstring(self):
        assert UserDefinedEthernetFrame.__init__.__doc__ is None

    def test_inherits_abstract_ethernet_frame(self):
        assert issubclass(UserDefinedEthernetFrame, AbstractEthernetFrame)
