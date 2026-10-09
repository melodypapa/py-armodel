import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import BusMirrorCanIdRangeMapping, BusMirrorCanIdToCanIdMapping, BusMirrorLinPidToCanIdMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror import BusMirrorChannelMapping, BusMirrorChannelMappingCan


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
