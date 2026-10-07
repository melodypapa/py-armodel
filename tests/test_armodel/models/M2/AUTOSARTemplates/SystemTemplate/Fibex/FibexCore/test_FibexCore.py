"""Model tests for the direct members of the FibexCore package.

Mirrors src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/__init__.py.
"""

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import BusMirrorChannel
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import MirroringProtocolEnum, RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore import BusMirrorChannelMapping, BusMirrorChannelMappingFlexray, BusMirrorChannelMappingUserDefined


class _ConcreteMapping(BusMirrorChannelMapping):
    pass


class TestBusMirrorChannelMapping:
    def test_abstract_instantiation_raises(self):
        with pytest.raises(TypeError):
            BusMirrorChannelMapping(None, "Mapping")

    def test_initialization(self):
        mapping = _ConcreteMapping(None, "Mapping")

        assert mapping.getShortName() == "Mapping"
        assert mapping.getMirroringProtocol() is None
        assert mapping.getSourceChannel() is None
        assert mapping.getTargetChannel() is None
        assert mapping.getTargetPduTriggeringRefs() == []

    def test_get_set_mirroring_protocol(self):
        mapping = _ConcreteMapping(None, "Mapping")
        protocol = MirroringProtocolEnum(["NONE", "VERSION-1"]).setValue("VERSION-1")

        assert mapping.setMirroringProtocol(protocol) is mapping
        assert mapping.getMirroringProtocol() is protocol
        assert mapping.getMirroringProtocol().getValue() == "VERSION-1"

        mapping.setMirroringProtocol(None)
        assert mapping.getMirroringProtocol() is protocol

    def test_get_set_source_channel(self):
        mapping = _ConcreteMapping(None, "Mapping")
        channel = BusMirrorChannel()

        assert mapping.setSourceChannel(channel) is mapping
        assert mapping.getSourceChannel() is channel

        mapping.setSourceChannel(None)
        assert mapping.getSourceChannel() is channel

    def test_get_set_target_channel(self):
        mapping = _ConcreteMapping(None, "Mapping")
        channel = BusMirrorChannel()

        assert mapping.setTargetChannel(channel) is mapping
        assert mapping.getTargetChannel() is channel

        mapping.setTargetChannel(None)
        assert mapping.getTargetChannel() is channel

    def test_add_target_pdu_triggering_ref(self):
        mapping = _ConcreteMapping(None, "Mapping")
        assert mapping.getTargetPduTriggeringRefs() == []

        ref = RefType().setValue("/BusMirror/PduTriggering")
        assert mapping.addTargetPduTriggeringRef(ref) is mapping
        assert mapping.getTargetPduTriggeringRefs() == [ref]

        mapping.addTargetPduTriggeringRef(None)
        assert len(mapping.getTargetPduTriggeringRefs()) == 1


class TestBusMirrorChannelMappingFlexray:
    def test_initialization(self):
        mapping = BusMirrorChannelMappingFlexray(None, "FlexrayMapping")

        assert isinstance(mapping, BusMirrorChannelMapping)
        assert mapping.getShortName() == "FlexrayMapping"
        assert mapping.getTransmissionDeadline() is None
        assert mapping.getMirroringProtocol() is None

    def test_get_set_transmission_deadline(self):
        mapping = BusMirrorChannelMappingFlexray(None, "FlexrayMapping")
        deadline = TimeValue().setValue("0.5")

        assert mapping.setTransmissionDeadline(deadline) is mapping
        assert mapping.getTransmissionDeadline() is deadline
        assert mapping.getTransmissionDeadline().getValue() == 0.5

        mapping.setTransmissionDeadline(None)
        assert mapping.getTransmissionDeadline() is deadline


class TestBusMirrorChannelMappingUserDefined:
    def test_initialization(self):
        mapping = BusMirrorChannelMappingUserDefined(None, "UserDefinedMapping")

        assert isinstance(mapping, BusMirrorChannelMapping)
        assert mapping.getShortName() == "UserDefinedMapping"
        assert mapping.getTransmissionDeadline() is None
        assert mapping.getMirroringProtocol() is None

    def test_get_set_transmission_deadline(self):
        mapping = BusMirrorChannelMappingUserDefined(None, "UserDefinedMapping")
        deadline = TimeValue().setValue("0.5")

        assert mapping.setTransmissionDeadline(deadline) is mapping
        assert mapping.getTransmissionDeadline() is deadline
        assert mapping.getTransmissionDeadline().getValue() == 0.5

        mapping.setTransmissionDeadline(None)
        assert mapping.getTransmissionDeadline() is deadline
