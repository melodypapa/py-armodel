import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror import BusMirrorChannelMapping, BusMirrorChannelMappingFlexray


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

    def test_class_docstring_is_spec_note_verbatim(self):
        assert inspect.cleandoc(BusMirrorChannelMappingFlexray.__doc__) == (
            "This element defines the bus mirroring between a CAN, LIN or FlexRay sourceChannel and a FlexRay targetChannel. " "Tags: atp.recommendedPackage=BusMirrorChannelMappings"
        )
