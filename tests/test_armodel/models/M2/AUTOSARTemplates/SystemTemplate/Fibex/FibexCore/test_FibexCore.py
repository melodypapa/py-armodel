"""Model tests for the direct members of the FibexCore package.

Mirrors src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/__init__.py.
"""

import inspect

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    BusMirrorCanIdRangeMapping,
    BusMirrorCanIdToCanIdMapping,
    BusMirrorLinPidToCanIdMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror import BusMirrorChannel, MirroringProtocolEnum
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore import (
    BusMirrorChannelMapping,
    BusMirrorChannelMappingCan,
    BusMirrorChannelMappingFlexray,
    BusMirrorChannelMappingIp,
    BusMirrorChannelMappingUserDefined,
)


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
        protocol = MirroringProtocolEnum().setValue(MirroringProtocolEnum.VERSION1)

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


class TestBusMirrorChannelMappingCan:
    def test_initialization(self):
        mapping = BusMirrorChannelMappingCan(None, "CanMapping")

        assert isinstance(mapping, BusMirrorChannelMapping)
        assert mapping.getShortName() == "CanMapping"
        assert mapping.getCanIdRangeMappings() == []
        assert mapping.getCanIdToCanIdMappings() == []
        assert mapping.getLinPidToCanIdMappings() == []
        assert mapping.getMirrorSourceLinToCanRangeBaseId() is None
        assert mapping.getMirrorStatusCanId() is None

    def test_add_can_id_range_mapping(self):
        mapping = BusMirrorChannelMappingCan(None, "CanMapping")

        range_mapping = BusMirrorCanIdRangeMapping()
        assert mapping.addCanIdRangeMapping(range_mapping) is mapping
        assert mapping.getCanIdRangeMappings() == [range_mapping]

        mapping.addCanIdRangeMapping(None)
        assert len(mapping.getCanIdRangeMappings()) == 1

    def test_add_can_id_to_can_id_mapping(self):
        mapping = BusMirrorChannelMappingCan(None, "CanMapping")

        id_mapping = BusMirrorCanIdToCanIdMapping()
        assert mapping.addCanIdToCanIdMapping(id_mapping) is mapping
        assert mapping.getCanIdToCanIdMappings() == [id_mapping]

        mapping.addCanIdToCanIdMapping(None)
        assert len(mapping.getCanIdToCanIdMappings()) == 1

    def test_add_lin_pid_to_can_id_mapping(self):
        mapping = BusMirrorChannelMappingCan(None, "CanMapping")

        lin_mapping = BusMirrorLinPidToCanIdMapping()
        assert mapping.addLinPidToCanIdMapping(lin_mapping) is mapping
        assert mapping.getLinPidToCanIdMappings() == [lin_mapping]

        mapping.addLinPidToCanIdMapping(None)
        assert len(mapping.getLinPidToCanIdMappings()) == 1

    def test_get_set_mirror_source_lin_to_can_range_base_id(self):
        mapping = BusMirrorChannelMappingCan(None, "CanMapping")

        value = PositiveInteger().setValue("512")
        assert mapping.setMirrorSourceLinToCanRangeBaseId(value) is mapping
        assert mapping.getMirrorSourceLinToCanRangeBaseId() is value
        assert mapping.getMirrorSourceLinToCanRangeBaseId().getValue() == 512

        mapping.setMirrorSourceLinToCanRangeBaseId(None)
        assert mapping.getMirrorSourceLinToCanRangeBaseId() is value

    def test_get_set_mirror_status_can_id(self):
        mapping = BusMirrorChannelMappingCan(None, "CanMapping")

        value = PositiveInteger().setValue("2048")
        assert mapping.setMirrorStatusCanId(value) is mapping
        assert mapping.getMirrorStatusCanId() is value
        assert mapping.getMirrorStatusCanId().getValue() == 2048

        mapping.setMirrorStatusCanId(None)
        assert mapping.getMirrorStatusCanId() is value

    def test_class_docstring_is_spec_note_verbatim(self):
        assert inspect.cleandoc(BusMirrorChannelMappingCan.__doc__) == (
            "This element defines the bus mirroring between a CAN or LIN sourceChannel and a CAN targetChannel. " "Tags: atp.recommendedPackage=BusMirrorChannelMappings"
        )


class TestBusMirrorChannelMappingIp:
    def test_initialization(self):
        mapping = BusMirrorChannelMappingIp(None, "IpMapping")

        assert isinstance(mapping, BusMirrorChannelMapping)
        assert mapping.getShortName() == "IpMapping"
        assert mapping.getTransmissionDeadline() is None
        assert mapping.getMirroringProtocol() is None

    def test_get_set_transmission_deadline(self):
        mapping = BusMirrorChannelMappingIp(None, "IpMapping")
        deadline = TimeValue().setValue("0.5")

        assert mapping.setTransmissionDeadline(deadline) is mapping
        assert mapping.getTransmissionDeadline() is deadline
        assert mapping.getTransmissionDeadline().getValue() == 0.5

        mapping.setTransmissionDeadline(None)
        assert mapping.getTransmissionDeadline() is deadline

    def test_class_docstring_is_spec_note_verbatim(self):
        assert inspect.cleandoc(BusMirrorChannelMappingIp.__doc__) == ("This element defines the bus mirroring between a CAN, LIN or FlexRay sourceChannel and an Ethernet IP targetChannel.")
