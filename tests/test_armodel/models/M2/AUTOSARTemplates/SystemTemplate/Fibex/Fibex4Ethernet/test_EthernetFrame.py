"""Model unit tests for AbstractEthernetFrame (Table 6.229, p.578)."""

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetFrame import AbstractEthernetFrame, GenericEthernetFrame, Ieee1722TpEthernetFrame, UserDefinedEthernetFrame
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import Frame

SPEC_NOTE = "Ethernet specific attributes to the Frame."
GENERIC_SPEC_NOTE = "This element is used for EthernetFrames without additional attributes that are routed by the EthIf. Tags: atp.recommendedPackage=Frames"
USER_DEFINED_SPEC_NOTE = "UserDefinedEthernetFrame allows the description of a frame-based communication to Complex Drivers that are located above the EthDrv. Tags: atp.recommendedPackage=Frames"
IEEE1722_TP_SPEC_NOTE = "Ieee1722Tp Ethernet Frame Tags: atp.Status=obsolete atp.recommendedPackage=Frames"


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


class TestIeee1722TpEthernetFrame:
    def test_initialization_defaults(self):
        parent = MockParent()
        frame = Ieee1722TpEthernetFrame(parent, "ieee_frame")
        assert frame.getShortName() == "ieee_frame"
        assert isinstance(frame, Frame)
        assert isinstance(frame, AbstractEthernetFrame)
        assert frame.getRelativeRepresentationTime() is None
        assert frame.getStreamIdentifier() is None
        assert frame.getSubType() is None
        assert frame.getVersion() is None
        assert frame.getFrameLength() is None
        assert frame.getPduToFrameMappings() == []

    def test_get_set_relative_representation_time(self):
        parent = MockParent()
        frame = Ieee1722TpEthernetFrame(parent, "ieee_frame")
        assert frame.setRelativeRepresentationTime(TimeValue().setValue(0.1)) is frame
        assert frame.getRelativeRepresentationTime() is not None
        assert frame.getRelativeRepresentationTime().getValue() == 0.1
        frame.setRelativeRepresentationTime(None)
        assert frame.getRelativeRepresentationTime() is not None

    def test_get_set_stream_identifier(self):
        parent = MockParent()
        frame = Ieee1722TpEthernetFrame(parent, "ieee_frame")
        assert frame.setStreamIdentifier(PositiveInteger().setValue("42")) is frame
        assert frame.getStreamIdentifier() is not None
        assert frame.getStreamIdentifier().getValue() == 42
        frame.setStreamIdentifier(None)
        assert frame.getStreamIdentifier() is not None

    def test_get_set_sub_type(self):
        parent = MockParent()
        frame = Ieee1722TpEthernetFrame(parent, "ieee_frame")
        assert frame.setSubType(PositiveInteger().setValue("7")) is frame
        assert frame.getSubType() is not None
        assert frame.getSubType().getValue() == 7
        frame.setSubType(None)
        assert frame.getSubType() is not None

    def test_get_set_version(self):
        parent = MockParent()
        frame = Ieee1722TpEthernetFrame(parent, "ieee_frame")
        assert frame.setVersion(PositiveInteger().setValue("2")) is frame
        assert frame.getVersion() is not None
        assert frame.getVersion().getValue() == 2
        frame.setVersion(None)
        assert frame.getVersion() is not None

    def test_class_docstring_is_spec_note(self):
        assert Ieee1722TpEthernetFrame.__doc__.strip() == IEEE1722_TP_SPEC_NOTE

    def test_init_has_no_docstring(self):
        assert Ieee1722TpEthernetFrame.__init__.__doc__ is None

    def test_inherits_abstract_ethernet_frame(self):
        assert issubclass(Ieee1722TpEthernetFrame, AbstractEthernetFrame)
