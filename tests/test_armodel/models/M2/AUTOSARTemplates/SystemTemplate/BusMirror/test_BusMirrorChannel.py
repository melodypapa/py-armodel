from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror import BusMirrorChannel


class TestBusMirrorChannel:
    def test_initialization(self):
        channel = BusMirrorChannel()

        assert channel.getBusMirrorNetworkId() is None
        assert channel.getChannelRef() is None

    def test_get_set_bus_mirror_network_id(self):
        channel = BusMirrorChannel()

        value = PositiveInteger().setValue("512")
        assert channel.setBusMirrorNetworkId(value) is channel
        assert channel.getBusMirrorNetworkId() is value
        assert channel.getBusMirrorNetworkId().getValue() == 512

        channel.setBusMirrorNetworkId(None)
        assert channel.getBusMirrorNetworkId() is value

    def test_get_set_channel_ref(self):
        channel = BusMirrorChannel()

        ref = RefType().setValue("/BusMirror/CanPhysicalChannel")
        assert channel.setChannelRef(ref) is channel
        assert channel.getChannelRef() is ref

        channel.setChannelRef(None)
        assert channel.getChannelRef() is ref

    def test_class_docstring_is_spec_note_verbatim(self):
        note = "This element assigns a busMirrorNetworkId to the referenced channel."
        assert BusMirrorChannel.__doc__.strip() == note
