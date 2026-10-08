"""Model tests for the direct members of the BusMirror package.

Mirrors src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/BusMirror.py.
"""

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror import BusMirrorChannel, BusMirrorChannelMapping, MirroringProtocolEnum


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

    def test_class_docstring_is_spec_note_verbatim(self):
        note = "This element defines a bus mirroring in which the traffic from one communication bus (sourceChannel) is forwarded to another one (targetChannel)."
        assert BusMirrorChannelMapping.__doc__.strip() == note
